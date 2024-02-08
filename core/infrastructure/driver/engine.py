import requests
import warnings
from os import system
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.infrastructure.modules.cloud_reader import get_name_api, get_locator_api, get_type_api
from core.infrastructure.modules.enums import Type
from core.tools.image_compare.image_compare_executor import ImageCompare
from core.infrastructure.driver.manager import DriverManager
from core.infrastructure.modules.methods import *
from core.infrastructure.modules.reader import *
from allure_commons.types import AttachmentType
from browsermobproxy import Server
from typing import Optional
from core.tools.api.constants import Authorization


warnings.filterwarnings('ignore')
log = Logger()


@dataclass
class DriverEngine(DriverManager):

    screen: Optional[str] = None

    def get_web(self, web_link: str, maximize_window=True) -> None:
        self.driver.get(web_link)
        allure_log(header='url link',
                   content=f'webdriver used:\n {self.driver} \n started: \n {web_link}')
        log.level.info(f'webdriver used:\n {self.driver} \n started: \n {web_link}')
        if maximize_window:
            self.driver.maximize_window()

    def get_element(self, name: str, seconds=10) -> webdriver:

        self.driver.implicitly_wait(seconds)
        element_name, element_type, element_locator = self.__get_element_properties(sheet_name=self.screen, value=name)
        output = f'element name: {element_name} | elements locator: {element_locator} | element type: {element_type}'

        try:
            if element_type in Type.__members__:
                log.level.info(output)
                return self.driver.find_element(Type[element_type].value, element_locator)

        except Exception as e:
            # self.attach_screenshot()
            raise e

    @staticmethod
    def __get_element_properties(**kwargs) -> tuple:
        element_name = get_name_api(**kwargs)
        element_locator = get_locator_api(**kwargs)
        element_type = get_type_api(**kwargs)
        return element_name, element_locator, element_type

    def get_dynamic_element(self, attribute: str, name: str, seconds=10) -> webdriver:

        # explanation ............ //*[contains(@<attribute>, <name>)]
        # example ................ //*[contains(@name, "btnK")]

        self.driver.implicitly_wait(seconds)
        element_locator = get_locator(self.screen, name)
        element_type = get_type(self.screen, name)
        path = f"//*[contains(@{attribute}, '{element_locator}')]"

        match element_type:

            case 'DYNAMIC':
                try:
                    return self.driver.find_elements(By.XPATH, path)[0]

                except Exception as e:
                    raise e

    def take_screenshot(self,
                        element: WebElement,
                        name: str,
                        compare_images=False,
                        embed_into_cell=True,
                        original_image_path=None) -> None:

        image_compare_data = fr"{GLOBAL_PATH}\{read_config('json', 'image_compare_data')}"
        updated_image_path = fr'{SCREENSHOTS}\{name}.png'
        element.screenshot(updated_image_path)

        if compare_images:
            write_json(path=image_compare_data, key="original_image_path", value=original_image_path)
            write_json(path=image_compare_data, key="actual_image_path", value=[updated_image_path])
            app = ImageCompare()
            path = fr'{GLOBAL_PATH}\{read_config("json", "image_compare_data")}'
            app.execute(path)

        if embed_into_cell:
            write_excel(sheet_name=self.screen, value=updated_image_path)

    def wait_for_element(self, name: str, seconds=5) -> None:
        element_locator = get_locator(self.screen, name)
        wait = WebDriverWait(self.driver, seconds)
        return wait.until(expected_conditions.visibility_of_element_located(('', element_locator)))

    def dropdown(self, by: By, locator: str) -> webdriver:
        select = Select(self.driver.find_element(by, get_locator(self.screen, locator)))
        return select.select_by_visible_text(locator)

    def count_elements(self, name: str, tag: str, selector: Type) -> int:

        """
        :param: name ............... name is retrieved from get_element()
        :param: tag ................ div, tr, etc... type it as it is
        :param: selector ........... inherits By class
        """

        table = self.get_element(name)
        rows = len(table.find_elements(selector, f'.//{tag}'))
        print(fr'number of rows in this page is: {rows}')
        return rows

    def press_keyboard_key(self, key: str, hold=False) -> ActionChains | None:
        action = ActionChains(self.driver)
        press = action.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL)
        if hold:
            press = action.key_down(Keys.CONTROL + 'T').send_keys(key).key_up(Keys.CONTROL)
            return press.perform()
        return press.perform()

    def scroll_page(self, direction: str, px: int) -> None:

        """
        :param: px ................ pixels
        :param: up or down

        """

        # screen_height: int = self.driver.execute_script("return window.innerHeight")
        
        match direction:
            case "up":
                self.driver.execute_script(f"window.scrollBy(0, {-px});")

            case "down":
                self.driver.execute_script(f"window.scrollBy(0, {px});")

    def attach_screenshot(self) -> None:
        allure.attach(fixture_funcction=self.driver.get_screenshot_as_png(),
                      name="Screenshot",
                      attachment_type=AttachmentType.PNG)

    def switch_to_new_tab(self, url: str) -> None:
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'T')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)
        return self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_main_tab(self) -> None:
        window_handles = self.driver.window_handles
        return self.driver.switch_to.window(window_handles[0])

    def handle_basic_auth(self, username: str, password: str) -> None:
        url = f"{username}:{password}@{self.driver.current_url}"
        self.driver.get(url)

    def capture_network_traffic(self, proxy_path: str) -> list[str]:
        server = Server(proxy_path)
        server.start()
        proxy = server.create_proxy()

        selenium_proxy = self.driver.common.proxy.Proxy({
            "httpProxy": proxy.proxy,
            "httpsProxy": proxy.proxy,
            "noProxy": None,
            "proxyType": "MANUAL",
        })

        capabilities = self.driver.common.desired_capabilities.DesiredCapabilities.CHROME.copy()
        selenium_proxy.add_to_capabilities(capabilities)
        driver = self.driver.Chrome(desired_capabilities=capabilities)
        proxy.new_har("traffic")
        har = proxy.har
        server.stop()

        return [driver, har]

    def count_rows(self, name: str, structure: str) -> int:

        """
        :param name .................. element name
        :param structure ............. div, tr, etc..
        :return:  integer
        """

        locator = get_locator(self.screen, name)
        table = self.driver.find_element(Type.XPATH, locator)
        rows = table.find_elements(By.XPATH, structure)
        return len(rows)

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except self.driver is None:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")
            raise Exception("driver's N/A")

    def load_cookies(self) -> None:
        with open(COOKIES) as file:
            cookies = json.load(file)
            for each in cookies:
                output = {
                    "name": each["name"],
                    "value": each["value"]
                }
            self.driver.add_cookie(output)

    def save_storage(self) -> None:
        local_storage = self.driver.execute_script(
            "var items = {}, ls = window.localStorage; for (var i = 0; i < ls.length; i++)  items[ls.key(i)] = ls.getItem(ls.key(i)); return items;")
        with open(COOKIES, "w") as f:
            json.dump(local_storage, f)

    def load_storage(self):
        with open(COOKIES, "r") as file:
            local_storage = json.load(file)
        for each in local_storage:
            for key, value in each.items():
                self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")


@dataclass
class APIEngine:

    """
    class_params: base_url ........................... A string representing the base URL for the HTTP requests.

    class_params: status_code ........................ A boolean, if True, returns response status code.

    :params: query_path (required) ................... A string representing the endpoint.
                                                       path to be appended to the base URL.
    :params: headers (optional) ...................... A dictionary containing the headers to be sent with the request.

    :params (optional) ............................... A dictionary containing the query parameters.
                                                       to be sent with the request.
    :params: verify (optional) ....................... A boolean indicating whether to verify the SSL certificate.

    :returns: response in a json format
    """

    base_url: str = ''
    status_code: bool = False

    def get_request(self, query_path: str, params=Optional[dict], verify=False) -> any:
        url = f'{self.base_url}/{query_path}'
        response = requests.get(url, headers=Authorization.HEADERS, params=params, verify=verify)
        if self.status_code:
            return f'response: {response.status_code}'

        log.level.debug(f'sent {response} with status code: {response.status_code}')
        return response.json()

    def post_request(self, query_path: str, body: dict[str], params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.post(url, headers=Authorization.HEADERS, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log.level.dubug(f'sent {response} with status code: {response.status_code}')
        return response.json()

    def put_request(self, query_path: str, body: dict[str], params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.put(url, headers=Authorization.HEADERS, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log.level.debug(f'sent {response} with status code: {response.status_code}')
        return response.json()

    def delete_request(self, query_path: str, params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.delete(url, headers=Authorization.HEADERS, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log.level.debug(f'sent {response} with status code: {response.status_code}')
        return response.json()
