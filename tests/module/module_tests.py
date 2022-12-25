from core.components.driver.engine import CompareImages
import unittest


<<<<<<< HEAD
<<<<<<< HEAD
path1 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\json\data.json'
=======
path1 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\img.png'
path2 = r'C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\img_1.png'
>>>>>>> d8a3e69e02d04f669f9ad1a992eb36f842918215
=======
path1 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\json\data.json'


compare = CompareImages()
>>>>>>> 1c63e7441e62014983eb6f4635003e13f3c039ae


class TestCompareImages(unittest.TestCase):

    def test1(self) -> None:
        compare.find_difference(path1)

    def test2(self) -> None:
<<<<<<< HEAD
        compare = CompareImages()
<<<<<<< HEAD
        assert compare.find_difference(path1)
=======
        compare.find_difference(path1, path2, resolution=(1200, 1200))
        self.assertIsNone(compare.find_difference(path1, path2))
>>>>>>> d8a3e69e02d04f669f9ad1a992eb36f842918215
=======
        assert compare.find_difference(path1)
>>>>>>> 1c63e7441e62014983eb6f4635003e13f3c039ae


test_compare_images = TestCompareImages()


def main() -> None:
    test = TestCompareImages()
    test.test1()


if __name__ == '__main__':
    main()
