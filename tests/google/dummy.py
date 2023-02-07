def main(name: str) -> None:
    match name:
        case 'jenia':
            print('this is my name')
        case 'other':
            print('other')
        case _:
            print("NONE")


if __name__ == '__main__':
    main(name="other")
