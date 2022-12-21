from datetime import datetime
import logging
from core.components.config.reader import ConfigReader
from functools import wraps


def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        config = ConfigReader()
        time = datetime.now()
        logs_path = config.read('path', 'logs')
        logging.basicConfig(filename=f'{logs_path}/{"logs.log"}',
                            datefmt=f'{time:%A | %B | %d/%m/%y | %X |}',
                            level=logging.INFO,
                            format='%(asctime)s:'
                                   '%(levelname)s:'
                                   '%(message)s')
        logging.info(f'{func.__name__}, arguments: {args, kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        logging.debug(f'{func.__name__} returned {result}')
        logging.error(f'{func.__name__} returned {result}')
        logging.fatal(f'{func.__name__} returned {result}')

        return result

    return wrapper
