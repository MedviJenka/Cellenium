from core.components.driver.engine import CompareImages
import unittest


path1 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\json\data.json'


compare = CompareImages()


class TestCompareImages(unittest.TestCase):

    def test1(self) -> None:
        compare.find_difference(path1)

    def test2(self) -> None:
        assert compare.find_difference(path1)


test_compare_images = TestCompareImages()


def main() -> None:
    test = TestCompareImages()
    test.test1()


if __name__ == '__main__':
    main()
