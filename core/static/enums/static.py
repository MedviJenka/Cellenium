from enum import Enum
from pathlib import Path


class Static(Enum):
    CURRENT_PATH = Path.cwd()
