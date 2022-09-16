import logging
from core.utils.config.reader import ConfigReader
from datetime import datetime
import os
import functools
import sys


config = ConfigReader()


# class CustomFormatter(logging.Formatter):
#
#     def format(self, record):
#         if hasattr(record, 'func_name_override'):
#             record.funcName = record.func_name_override
#         if hasattr(record, 'file_name_override'):
#             record.filename = record.file_name_override
#         return super(CustomFormatter, self).format(record)
#
#
# def get_logger(log_name=__name__, log_dir=config.read('path', 'logs')):
#     t = datetime.now()
#     time = f'{t:%A %D %X}'
#     log_path = log_name if os.path.exists(log_name) else os.path.join(log_dir, f'{log_name}.log')
#     logger = logging.Logger(log_name)
#     handler = logging.FileHandler(log_path, 'a+')
#     handler.setFormatter(CustomFormatter(f'{time} - %(levelname)-10s - %(filename)s - %(funcName)s - %(message)s'))
#     logger.addHandler(handler)
#     logger.setLevel(logging.DEBUG)
#     return logger
#
#
# def log_decorator(_func=None):
#     def log_decorator_info(func):
#         @functools.wraps(func)
#         def log_decorator_wrapper(self, *args, **kwargs):
#             """Build logger object"""
#             logger_obj = get_logger(log_name=self.log_file_name, log_dir=self.log_file_dir)
#
#             """log function begining"""
#             logger_obj.info("Begin function")
#             try:
#                 """ log return value from the function """
#                 value = func(self, *args, **kwargs)
#                 logger_obj.info(f"Returned: - End function {value!r}")
#             except Exception:
#                 """log exception if occurs in function"""
#                 logger_obj.error(f"Exception: {str(sys.exc_info()[1])}")
#                 raise
#             return value
#         return log_decorator_wrapper
#     if _func is None:
#         return log_decorator_info
#     else:
#         return log_decorator_info(_func)


def get_logger(function):
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        log_name = __name__
        log_dir = config.read('path', 'logs')
        log_path = log_name if os.path.exists(log_name) else os.path.join(log_dir, f'{log_name}.log')
        logger = logging.Logger(log_name)
        handler = logging.FileHandler(log_path, 'a+')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return function(*args, **kwargs)
    return decorator


# @dataclass
# class LogGenerator:
#
#     config = ConfigReader()
#     logger: logging = logging.getLogger(__name__)
#     path: str = config.read('path', 'logs')
#     file_handler: logging = logging.FileHandler(fr'{ path }/{ __name__ }.log')
#
#     def generate(self) -> None:
#         t = datetime.now()
#         time = f'{t: %A %D %X}'
#         return self.logger.addHandler(self.file_handler)
#
#
# log = LogGenerator()
# log.generate()
