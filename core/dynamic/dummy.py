from random import randint


def random_numbers() -> int:
    result = randint(1, 10)
    print(result)
    return result


print((lambda a, b: (a + b) % 2 == 0)(random_numbers(), random_numbers()) and 'even' or 'odd')
