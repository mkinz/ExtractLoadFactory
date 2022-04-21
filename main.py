import logging
from logging import Logger
from datetime import datetime
from _collections_abc import Iterable

from factories import ConcreteDataRefresherFactoryA, ConcreteDataRefresherFactoryB

logging.basicConfig(level=logging.DEBUG)
logger: Logger = logging.getLogger(__name__)


class ConnectionError(Exception):
    """
    Custom exception for handling connection errors
    """
    pass


class SourceConnectionError(ConnectionError):
    pass


class TargetConnectionError(ConnectionError):
    pass


def get_factory() -> Iterable:
    factories = {
        "A": ConcreteDataRefresherFactoryA(),
        "B": ConcreteDataRefresherFactoryB()
    }

    for work_set in factories.keys():
        yield factories[work_set]


def run_app():
    logger.info("Initializing ExtractLoadFactory...")
    today = datetime.today()

    for fac in get_factory():
        try:
            source_db_connector_object = fac.get_source_connector()
            source_conn = source_db_connector_object.connect_to_db()
            if not source_db_connector_object.connected:
                raise SourceConnectionError

            extractor_object = fac.get_extractor()
            extracted_data = extractor_object.extract(source_conn, today)

            target_db_connector_object = fac.get_target_connector()
            target_conn = target_db_connector_object.connect_to_db()
            if not target_db_connector_object.connected:
                raise TargetConnectionError

            loader_object = fac.get_loader()
            loader_object.validate_input(extracted_data)
            loader_object.load_data(target_conn, extracted_data, today)
        except ConnectionError:
            logger.info("Connection was unabled to be established.")

        logger.info("Extract and Load complete.\n")


def main():
    run_app()


if __name__ == '__main__':
    main()
