class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def bark() -> None:
        print('bark')

    @staticmethod
    def get_bark() -> str:
        return 'bark'


dog = Dog('tim', 32)
dog.bark()
print(dog.get_bark())

