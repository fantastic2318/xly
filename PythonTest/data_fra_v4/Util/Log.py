import os

from loguru import logger

from data_fra_v4.settings.config import logfilePath


class Log:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        logger.add(os.path.join(logfilePath, 'runtime_{time}.log'))

    def debug(self, message):
        logger.debug(message)

    def info(self, message):
        logger.info(message)


log = Log()
# if __name__ == "__main__":
#     log = Log()
#     log.debug("debugdebugdebug")