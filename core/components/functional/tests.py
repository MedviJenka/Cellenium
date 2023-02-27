from unittest import TestCase
from core.components.functional.methods import run_test, negative


class Test(TestCase):

    def test1(self) -> None:
        self.assertEqual(1 + 1, 2)

    def test2(self) -> None:
        self.assertEqual(1 + 2, 3)

    def test3(self) -> None:
        self.assertNotEqual(1 + 1, 1)

    @negative(ZeroDivisionError)
    def test4(self) -> None:
        assert 1 / 0


if __name__ == '__main__':
    run_test(Test(), ['test1', 'test2', 'test3'])
