from dataclasses import dataclass


@dataclass
class App:

    answer: str = "palindrome"

    def palindrome(self, text: str) -> str:
        return self.answer if text == text[::-1] else 'not a palindrome'


app = App()


def test1() -> None:
    assert app.palindrome("level") == 'palindrome'


def test2() -> None:
    assert not app.palindrome("jenia") == 'palindrome'


def test3() -> None:
    assert app.palindrome("not") == 'not a palindrome'


if __name__ == '__main__':
    test1()
    test2()
    test3()

