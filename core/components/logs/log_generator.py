from datetime import datetime
import logging
from dataclasses import dataclass
from core.components.config.reader import ConfigReader

"""
@staticmethod
def log(function):
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        config = ConfigReader()
        log_name = __name__
        log_dir = config.read('path', 'logs')
        log_path = log_name if os.path.exists(log_name) else os.path.join(log_dir, f'{log_name}.log')
        logger = logging.Logger(log_name)
        handler = logging.FileHandler(log_path, 'a+')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return function(*args, **kwargs)
    return decorator
"""





@dataclass
class Log:

    config = ConfigReader()
    time = datetime.now()
    logs_path = config.read('path', 'logs')
    logging.basicConfig(filename=f'{logs_path}/{"logs.log"}',
                        datefmt=f'{time:%A | %B | %d/%m/%y | %X |}',
                        level=logging.DEBUG,
                        format='%(asctime)s:'
                                 '%(levelname)s:'
                                 '%(message)s')

    @staticmethod
    def get_log() -> logging:
        logger = logging.getLogger()
        logger.setLevel('INFO')
        logger.setLevel('DEBUG')
        logger.setLevel('WARNING')
        logger.setLevel('ERROR')
        logger.setLevel('FATAL')

