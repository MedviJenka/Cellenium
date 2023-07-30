from core.infrastructure.modules.reader import get_name, get_type, get_locator, _read_excel


def test_excel() -> None:
    assert _read_excel('IntroPage', 'button') == {
        'name': 'button',
        'locator': 'btnK',
        'type': 'NAME',
        'actions': None,
        'image': None,
    }


def test_get_name() -> None:
    assert get_name('IntroPage', 'button') == 'button'


def test_get_type() -> None:
    assert get_type('IntroPage', 'button') == 'NAME'


def test_get_locator() -> None:
    assert get_locator('IntroPage', 'button') == 'btnK'
