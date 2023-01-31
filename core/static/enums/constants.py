from enum import Enum
from pathlib import Path


class Data(Enum):
    CURRENT_PATH = Path.cwd()


class Rest(Enum):
    GET = 1
    POST = 2
