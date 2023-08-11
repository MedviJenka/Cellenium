from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine('IntroPage')


class TestIntroPage:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://www.google.com/search?q=gov&ei=iCA9ZLGvOIvixc8Ph9aI2Ac&ved=0ahUKEwixk8XN27D-AhULcfEDHQcrAnsQ4dUDCA8&uact=5&oq=gov&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCAAQigUQsQMQkQIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCC4QgAQ6DQgAEIoFELEDEIMBEEM6EwguEIoFELEDEIMBEMcBENEDEEM6DgguEIoFEMcBENEDEJECOg4IABCKBRCxAxCDARCRAjoHCAAQigUQQzoWCC4QigUQsQMQgwEQxwEQ0QMQQxDqBDohCC4QigUQsQMQgwEQxwEQ0QMQQxDqBBDcBBDeBBDgBBgBSgQIQRgAUABYnAJg2AVoAHABeACAAaYCiAH-BZIBAzItM5gBAKABAcABAdoBBggBEAEYFA&sclient=gws-wiz-serp', maximize_window=True)

    def test_navigation(self) -> None:
        ...

    def test_exit_all(self) -> None:
        engine.teardown()
