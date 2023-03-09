from enum import Enum


PROJECT_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'
CONFIG_PATH = fr'C:\Users\medvi\OneDrive\Desktop\Cellenium\core\static\utils\config.ini'


class Functional(Enum):
    STARTUP  = 1
    RUN      = 2
    TEARDOWN = 3
