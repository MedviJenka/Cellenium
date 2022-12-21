import logging


log_file = "./logfile.log"
log_level = logging.DEBUG
logging.basicConfig(level=log_level, filename=log_file, filemode="w+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger("baker_logger")


def wrap(pre, post):
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            pre(func)
            result = func(*args, **kwargs)
            post(func)
            return result
        return call
    return decorate


def entering(func):
    """ Pre function logging """
    logger.debug("Entered %s", func.__name__)


def exiting(func):
    """ Post function logging """
    logger.debug("Exited  %s", func.__name__)


@wrap(entering, exiting)
def bake_pie(amount):
    """ Bakes a certain amount of pies """
    print("I baked %d pies" % amount)
