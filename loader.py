import logging
import pandas as pd
from logging import Logger
from typing import Protocol, runtime_checkable
from datetime import datetime
from dbcon import DBConnector

logger: Logger = logging.getLogger(__name__)


@runtime_checkable
class Loader(Protocol):
    def __init__(self):
        ...

    def validate_input(self, data_to_load: pd.DataFrame):
        ...


    def load_data(self, target_db_connection: DBConnector, data_to_load: pd.DataFrame, date_time: datetime):
        ...


class ConcreteLoaderInstanceA:

    def  __init__(self):
        self.contains_data = False

    def validate_input(self, data_to_load):
        #if not data_to_load.empty:
        self.contains_data = True

    def load_data(self, target_db_connection: DBConnector, data_to_load: pd.DataFrame, date_time: datetime):
        query = f"update {target_db_connection}.myschma.mytable_A" \
                f"set data = {data_to_load}" \
                f"where date = {date_time}"
        if self.contains_data:
            logger.debug(f"Ran the following SQL query:")
            logger.debug(query)
            logger.debug(f"Load sql query complete to {target_db_connection}.myschema.mytable_A.")
            return target_db_connection
        else:
            logger.info("No data in input dataframe, so no data loaded.")

class ConcreteLoaderInstanceB:

    def __init__(self):
        self.contains_data = False

    def validate_input(self, data_to_load):
        #if not data_to_load.empty:
        self.contains_data = True

    def load_data(self, target_db_connection: DBConnector, data_to_load: pd.DataFrame, date_time: datetime):
        query = f"update {target_db_connection}.myschma.mytable_B" \
                f"set data = {data_to_load}" \
                f"where date = {date_time}"
        if self.contains_data:
            logger.debug(f"Ran the following SQL query:")
            logger.debug(query)
            logger.debug(f"Load sql query complete to {target_db_connection}.myschema.mytable_B.")
            return target_db_connection
        else:
            logger.info("No data in input dataframe, so no data loaded.")
