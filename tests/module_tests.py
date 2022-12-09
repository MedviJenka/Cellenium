from core.components.driver.manager import CompareImages
from core.components.driver.run_tests import run_single_test

path1 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\screenshots\reports\web.jpg'
path2 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\screenshots\reports\web2.jpg'
path3 = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\screenshots\reports\web3.jpg'


class TestCompareImages:

    @staticmethod
    def test1() -> None:
        compare = CompareImages()
        compare.find_difference(path1, path2, show_full_data=True)

    @staticmethod
    def test2() -> None:
        compare = CompareImages()
        compare.find_difference(path2, path3, show_full_data=True)

    @staticmethod
    def test3() -> None:
        compare = CompareImages()
        compare.find_difference(path2, path2)

    @staticmethod
    def test4() -> None:
        compare = CompareImages()
        compare.find_difference(path1, path2)


test_compare_images = TestCompareImages()


def main() -> None:
    run_single_test(TestCompareImages(), ['test1',
                                          'test2',
                                          'test3',
                                          'test4'])


if __name__ == '__main__':
    main()
