import logging
from dataclasses import dataclass
from core.utils.config.reader import ConfigReader


@dataclass
class LogGenerator:

    config = ConfigReader()
    logger: logging = logging.getLogger(__name__)
    path: str = config.read('path', 'logs')
    file_handler: logging = logging.FileHandler(fr'{ path }/{ __name__ }.log')

    def generate(self) -> None:
        return self.logger.addHandler(self.file_handler)


log = LogGenerator()
log.generate()
