import logging

logging.basicConfig(
    format="%(levelname)s:%(asctime)s:%(pathname)s:%(lineno)s:%(message)s"
)
logger = logging.getLogger(__name__)


def debug(message):
    logger.debug(message, stacklevel=2)


def info(message):
    logger.info(message, stacklevel=2)


def error(message):
    logger.error(message, stacklevel=2)
