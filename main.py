import logging
from logging import Logger
from datetime import datetime
from _collections_abc import Iterable

from factories import ConcreteDataRefresherFactoryA, ConcreteDataRefresherFactoryB
from custom_exceptions import ConcreteSourceDBConnectionError, ConcreteTargetDBConnectionError

logging.basicConfig(level=logging.DEBUG)
logger: Logger = logging.getLogger(__name__)


def get_factory() -> Iterable:
    factories = {
        "A": ConcreteDataRefresherFactoryA(),
        "B": ConcreteDataRefresherFactoryB()
    }

    for work_set in factories:
        yield factories[work_set]


class Runner:

    def run_app(self):
        logger.info("Initializing ExtractLoadFactory...")
        today = datetime.today()

        for fac in get_factory():
            try:

                # get objects
                source_db_connector_object = fac.get_source_connector()
                target_db_connector_object = fac.get_target_connector()
                loader_object = fac.get_loader()
                extractor_object = fac.get_extractor()
                validator_object = fac.get_validator()

                # connect to source
                source_conn = source_db_connector_object.connect_to_db()
                source_db_connector_object.get_connection_status()
                extracted_data = extractor_object.extract(source_conn, "select * from test_table limit 5")

                # run data validation
                validator_object.validate(extracted_data)
                if validator_object.validated_data:

                    # connect to target
                    target_conn = target_db_connector_object.connect_to_db()
                    target_db_connector_object.get_connection_status()

                    # load data to target
                    loader_object.load_data(target_conn, "myschema", "mytable", extracted_data)

            except ConnectionError:
                logger.info("Connection was unabled to be established.")

            logger.info("Extract and Load complete.\n")


def main():
    runner = Runner()
    runner.run_app()


if __name__ == '__main__':
    main()
