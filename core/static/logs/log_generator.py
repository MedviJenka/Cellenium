from datetime import datetime
import logging
from core.components.config.reader import ConfigReader
from functools import wraps

config = ConfigReader()
time = datetime.now()
log_path = config.read('path', 'logs')
time_stamp = f'{time: "%A | %B | %d/%m/%y | %X"}'


def log_setup(level):
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    if log_path:
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Create a StreamHandler to log to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


# def log(func) -> logging:
#
#     @wraps(func)
#     def decorator(*args, **kwargs) -> callable:
#
#         result = func(*args, **kwargs)
#         logging.info(f"Function {func.__name__} called args: {args, kwargs} and returned {result}")
#         logging.basicConfig(filename=f'{log_path}/{"logs.log"}',
#                             datefmt=f'{time: "%A | %B | %d/%m/%y | %X"}',
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             level=logging.INFO)
#         return result
#
#     return decorator
