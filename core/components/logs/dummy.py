import logging
from core.components.config.reader import ConfigReader
from datetime import datetime


config = ConfigReader()
time = datetime.now()


logs_path = config.read('path', 'logs')
logging.basicConfig(filename=f'{logs_path}/{"logs.log"}',
                    datefmt=f'{time:%A | %B | %d/%m/%y | %X}',
                    level=logging.DEBUG,
                    format='%(asctime)s:'
                             '%(levelname)s:'
                             '%(message)s')
logging.debug('aaa')

