from core.infrastructure.modules.reader import read_json


if __name__ == '__main__':
    a = read_json(path=r'C:\Users\medvi\OneDrive\Desktop\Cellenium\core\utils\data\test_suites.json')
    print(a['suites'])