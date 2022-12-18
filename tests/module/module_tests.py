from core.components.driver.engine import CompareImages
import unittest


path1 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\json\data.json'


class TestCompareImages(unittest.TestCase):

    def test1(self) -> None:
        compare = CompareImages()
        compare.find_difference(path1)

    def test2(self) -> None:
        compare = CompareImages()
        assert compare.find_difference(path1)


test_compare_images = TestCompareImages()


def main() -> None:
    ...


if __name__ == '__main__':
    main()
