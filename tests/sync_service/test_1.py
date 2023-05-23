from selenium.webdriver.common.by import By
from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine('Jira')


def get_xpath_text_by_index(xpath: str, _from: int, to: int) -> None:
    old_xpath = xpath.split('div')[:-1]
    new_xpath = 'div'.join(old_xpath)
    for index in range(_from, to):
        return engine.driver.find_element(By.XPATH, new_xpath).text


class TestIntroPage:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://www.google.com/search?q=gov&ei=iCA9ZLGvOIvixc8Ph9aI2Ac&ved=0ahUKEwixk8XN27D-AhULcfEDHQcrAnsQ4dUDCA8&uact=5&oq=gov&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCAAQigUQsQMQkQIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCC4QgAQ6DQgAEIoFELEDEIMBEEM6EwguEIoFELEDEIMBEMcBENEDEEM6DgguEIoFEMcBENEDEJECOg4IABCKBRCxAxCDARCRAjoHCAAQigUQQzoWCC4QigUQsQMQgwEQxwEQ0QMQQxDqBDohCC4QigUQsQMQgwEQxwEQ0QMQQxDqBBDcBBDeBBDgBBgBSgQIQRgAUABYnAJg2AVoAHABeACAAaYCiAH-BZIBAzItM5gBAKABAcABAdoBBggBEAEYFA&sclient=gws-wiz-serp', maximize_window=True)

    def test_navigation(self) -> None:
        print(get_xpath_text_by_index('//*[@id="rso"]/div[6]/div', 1, 5))

    def test_exit_all(self) -> None:
        engine.teardown()
