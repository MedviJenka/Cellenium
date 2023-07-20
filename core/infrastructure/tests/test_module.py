from core.infrastructure.modules.reader import (
    read_excel,
    get_name,
    get_type,
    get_locator,
    read_json,
    write_json
)


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

    def test_read_json_with_value(self) -> None:
        assert 'test name' in read_json('dummy.json', 'name')

    def test_read_json(self) -> None:
        expected_result = {
            "name": "test name",
            "id": 123456,
            "bool": True
        }

        assert read_json(path='dummy.json') == expected_result

    def test_write_json(self) -> None:
        write_json(path='dummy2.json', key='test', value='test value')
        assert read_json(path='dummy2.json', value='test') == 'test value'
