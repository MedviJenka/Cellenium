from pathlib import Path


def main() -> None:
    print(f'current dir is: { Path.cwd() }')
    print(f'current home dir is: { Path.home() }')


if __name__ == '__main__':
    main()
    