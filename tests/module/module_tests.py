from core.components.driver.manager import CompareImages
import unittest


path1 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web.jpg'
path2 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web2.jpg'
path3 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web3.jpg'


class TestCompareImages(unittest.TestCase):

    def test1(self) -> None:
        compare = CompareImages()
        self.assertIsNone(compare.find_difference(path1, path2, show_full_data=True))

    def test2(self) -> None:
        compare = CompareImages()
        self.assertIsNone(compare.find_difference(path2, path3, show_full_data=True))

    def test3(self) -> None:
        compare = CompareImages()
        self.assertEquals(compare.find_difference(path2, path2), 100)

    def test4(self) -> None:
        compare = CompareImages()
        self.assertGreater(compare.find_difference(path1, path3), 90)


test_compare_images = TestCompareImages()


def main() -> None:
    ...


if __name__ == '__main__':
    main()
