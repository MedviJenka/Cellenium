from os import system
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.tools.image_compare.image_compare_executor import ImageCompare
from core.infrastructure.driver.manager import DriverManager
from core.infrastructure.modules.methods import *
from core.infrastructure.modules.reader import *
from allure_commons.types import AttachmentType
from browsermobproxy import Server


@dataclass
class DriverEngine(DriverManager):

    """
    :TODO: test lines 171 and on

    :class: DriverManager ................. inherits selenium webdriver functionality for navigating into
                                            a deeper state of selenium:
                                            example: engine = DriverEngine(...)
                                                     self.engine.driver...

    :param: screen ........................ screen reads from page_base.xlsx sheet name and iterates through
                                            different screens, overall for usability and order.

    """

    screen: Optional[str] = ''

    def get_web(self, web_link: str, maximize_window=True) -> None:
        self.driver.get(web_link)
        allure_log(header='url link',
                   content=f'webdriver used:\n {self.driver} \n started: \n {web_link}')
        if maximize_window:
            self.driver.maximize_window()

    def get_element(self, name: str, seconds=10) -> webdriver:

        self.driver.implicitly_wait(seconds)
        element_locator = get_locator(self.screen, name)
        element_type = get_type(self.screen, name)
        element_name = get_name(self.screen, name)
        actions = get_actions(self.screen, name)
        output = f'element name: {element_name} | elements locator: {element_locator} | element type: {element_type}'

        try:

            allure_log(header='elements used', content=output)

            match element_type:

                case 'NAME':
                    return self.driver.find_element(Type.NAME, element_locator)

                case 'ID':
                    return self.driver.find_element(Type.ID, element_locator)

                case 'CSS':
                    return self.driver.find_element(Type.CSS, element_locator)

                case 'XPATH':

                    xpath = self.driver.find_elements(By.XPATH, element_locator)

                    if actions == 'MULTIPLE_ELEMENTS':

                        for matched_element in xpath:
                            text = matched_element.text
                            allure_log(header='elements list',
                                       content=f'used: {actions}, data: \n{text}')
                    else:
                        allure_log(header='elements: used', content=f'elements: \n{element_locator}')
                        return xpath

                case 'TEXT':
                    return self.driver.find_element(Type.TEXT, element_locator)

                case 'CLASS':
                    return self.driver.find_element(Type.CLASS, element_locator)

        except Exception as e:
            self.attach_screenshot()
            raise e

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

    def press_keyboard_key(self, key: str, hold=False) -> ActionChains:
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
