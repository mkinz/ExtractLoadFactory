import logging
from logging import Logger
from datetime import datetime
from _collections_abc import Iterable

from factories import ConcreteDataRefresherFactoryA

logging.basicConfig(level=logging.DEBUG)
logger: Logger = logging.getLogger(__name__)


def get_factory() -> Iterable:
    factories = {
        "A": ConcreteDataRefresherFactoryA
    }

    for work_set in factories.keys():
        yield factories[work_set]



def main():
    pass


if __name__ == '__main__':
    main()
