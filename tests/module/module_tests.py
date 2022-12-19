from core.components.driver.engine import CompareImages
import unittest


path1 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\img.png'
path2 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\img_1.png'


class TestCompareImages(unittest.TestCase):

    def test1(self) -> None:
        compare = CompareImages()
        compare.find_difference(path1, path2)

    def test2(self) -> None:
        compare = CompareImages()
        compare.find_difference(path1, path2, resolution=(1200, 1200))
        self.assertIsNone(compare.find_difference(path1, path2))


test_compare_images = TestCompareImages()


def main() -> None:
    test = TestCompareImages()
    test.test1()


if __name__ == '__main__':
    main()
