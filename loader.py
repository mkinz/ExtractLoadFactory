import logging
from logging import Logger
from typing import Protocol, runtime_checkable
from datetime import datetime
from dbcon import DBConnector

logger: Logger = logging.getLogger(__name__)

@runtime_checkable
class Loader(Protocol):
    def load_data(self, target_db_connection: DBConnector, data_to_load, date_time: datetime):
        pass


class ConcreteLoaderInstanceA:
    def load_data(self, target_db_connection: DBConnector, data_to_load, date_time: datetime):
        query = f"update {target_db_connection}.myschma.mytable" \
                f"set data = {data_to_load}" \
                f"where date = {date_time}"
        logger.debug(f"Ran the following SQL query:")
        logger.debug(query)
        logger.debug(f"Load sql query complete to {target_db_connection}.myschema.mytable.")
        return target_db_connection