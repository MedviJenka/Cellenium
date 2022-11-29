import sys
from functools import wraps


def log_decorator(_func=None):
    def log_decorator_info(func):
        @wraps(func)
        def log_decorator_wrapper(self, *args, **kwargs):
            """Build logger object"""
            logger_obj = log.get_logger(log_file_name=self.log_file_name, log_sub_dir=self.log_file_dir)

            """log function beginning"""
            logger_obj.info("Begin function")
            try:
                """ log return value from the function """
                value = func(self, *args, **kwargs)
                logger_obj.info(f"Returned: - End function {value!r}")
            except:
                """log exception if occurs in function"""
                logger_obj.error(f"Exception: {str(sys.exc_info()[1])}")
                raise
            return value
        return log_decorator_wrapper
    if _func is None:
        return log_decorator_info
    else:
        return log_decorator_info(_func)
