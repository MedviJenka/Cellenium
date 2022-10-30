from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class ConfigReader:

    config = ConfigParser()
    path: str = r'C:\Users\evgenyp\Cellenium\core\components\config\config.ini'

    def read(self, key: str, value: str) -> str:
        self.config.read(self.path)
        return self.config.get(key, value)
