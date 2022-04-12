import logging
from logging import Logger
from typing import Protocol
from datetime import datetime
from dbcon import DBConnector

logger: Logger = logging.getLogger(__name__)

class Loader(Protocol):
    def load_data(self, target_db_connection: DBConnector, data_to_load, date_time: datetime):
        pass


class ConcreteLoaderInstanceA:
    def load_data(self, target_db_connection: DBConnector, data_to_load, date_time: datetime):
        query = f"update {target_db_connection}.myschma.mytable" \
                f"set data = {data_to_load}" \
                f"where date = {date_time}"
        logger.debug(f"Ran the following SQL:")
        logger.debug(query)
        logger.debug(f"Load sql query complete to {target_db_connection}.myschema.mytable.")
        logger.debug(f"Loaded the following data: {data_to_load}")
        return target_db_connection