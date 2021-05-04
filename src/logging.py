import logging

from .paths import PACKAGE_PATH


__all__ = ['initialize_logger']


logger = logging.getLogger(__name__)


PACKAGE_NAME = PACKAGE_PATH.package


assert PACKAGE_NAME is not None


def initialize_logger():
    package_logger = logging.getLogger(PACKAGE_NAME)

    removeHandlers()

    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(fmt="[JS Custom] {message}", style='{')
    )
    package_logger.addHandler(handler)
    package_logger.setLevel(
        logging.getLevelName(logging.INFO)
    )
    package_logger.propagate = False


def removeHandlers():
    package_logger = logging.getLogger(PACKAGE_NAME)

    for handler in list(package_logger.handlers):
        package_logger.removeHandler(handler)
