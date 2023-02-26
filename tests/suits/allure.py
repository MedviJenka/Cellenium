import os


def allure_report() -> None:
    os.system(r'pytest C:\Cellenium\tests\suits\google\dummy.py --alluredir=C:\Cellenium\tests\reports')
    os.system(r'allure serve C:\Cellenium\tests\reports')


if __name__ == '__main__':
    allure_report()
