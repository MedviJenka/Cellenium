from core.infrastructure.driver.engine import DriverEngine


# TODO: find why i cant put engine as init
engine = DriverEngine('IntroPage')


class TestIntroPage:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://www.google.com/search?q=cats&source=hp&ei=cm8yZPeuCaH5sAeYuqvQAQ&iflsig=AOEireoAAAAAZDJ9gpOCy7Uv4HS85rW4oiCSU99gv7QI&ved=0ahUKEwj3r56oqZz-AhWhPOwKHRjdChoQ4dUDCAk&uact=5&oq=cats&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEIAEELEDEMcBENEDMgsIABCABBCxAxCDATIRCC4QgwEQxwEQsQMQ0QMQgAQyCAgAEIoFELEDMgsIABCKBRCxAxCDATIICAAQgAQQsQMyCwguEIoFELEDEIMBMggILhCABBDUAjIICC4QgAQQ1AIyCwgAEIoFELEDEIMBOgsILhCABBCxAxCDAToOCC4QgAQQsQMQgwEQ1AI6EQguEIoFELEDEIMBEMcBENEDUABYyAJghANoAHAAeACAAcUBiAHgApIBAzAuMpgBAKABAQ&sclient=gws-wiz', maximize_window=True)

    def test_navigate(self) -> None:
        engine.scroll_page(direction='down', px=150)

    def test_exit_all(self) -> None:
        engine.teardown()
