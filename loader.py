import logging
import pandas as pd
from logging import Logger
from typing import Protocol, runtime_checkable
from datetime import datetime
from dbcon import IDBConnector

logger: Logger = logging.getLogger(__name__)


@runtime_checkable
class ILoader(Protocol):
    """
    Interface that establishes loader protocol
    """

    def load_data(self, target_db_connection: IDBConnector, data_to_load: pd.DataFrame, date_time: datetime):
        ...


class GenericConcreteLoader:

    def load_data(self, target_db_connection: IDBConnector, schema: str, tablename: str, data_to_load: pd.DataFrame) -> None:
        query = f"update {target_db_connection}.{schema}.{tablename}" \
                f" set data = '{data_to_load}'" \

        logger.debug(f"ran the following query: {query}")
        return target_db_connection
