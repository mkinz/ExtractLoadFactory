import logging
from logging import Logger
from typing import Protocol, runtime_checkable
from datetime import datetime
from dbcon import IDBConnector

logger: Logger = logging.getLogger(__name__)

    
@runtime_checkable
class IExtractor(Protocol):
    """"
    Interface that defines an extractor protocol
    """
    def extract(self, source_db_connection: IDBConnector, date_time: datetime):
        ...

        
class GenericConcreteExtractor:
    def extract(self, source_db_connection: IDBConnector, query: str):
        logger.debug(f"Extract completed from {source_db_connection}.myschema.mytable_A using query: '{query}' ")
        return "### Mock extracted Data ###"
