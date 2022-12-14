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
        compare.find_difference(path1, path2, resolution=(1200, 1200), show_full_data=True)

    # def test3(self) -> None:
    #     compare = CompareImages()
    #     self.assertEquals(compare.find_difference(path2, path2), 100)
    #
    # def test4(self) -> None:
    #     compare = CompareImages()
    #     self.assertLessEqual(compare.find_difference(path4, path5, show_full_data=False), 90)


test_compare_images = TestCompareImages()


def main() -> None:
    test = TestCompareImages()
    test.test1()


if __name__ == '__main__':
    main()
