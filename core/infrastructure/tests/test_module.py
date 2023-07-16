from core.infrastructure.modules.reader import read_excel, get_name, get_type, get_locator


class TestModule:

    def test_get_excel(self) -> None:

        result = {
            'name': 'button',
            'locator': 'btnK',
            'type': 'NAME',
            'actions': None,
            'image': None
        }

        assert read_excel('IntroPage', 'button') == result

    def test_name(self) -> None:
        assert get_name('IntroPage', 'button') == 'button'

    def test_type(self) -> None:
        assert get_type('IntroPage', 'button') == 'NAME'

    def test_locator(self) -> None:
        assert get_locator('IntroPage', 'button') == 'btnK'
