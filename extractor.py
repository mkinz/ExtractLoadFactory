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

        
class ConcreteExtractorInstanceA:
    def extract(self, source_db_connection: IDBConnector, date_time: datetime):
        query = f"select * from myschema.mytable_A where date = {date_time}"
        logger.debug(query)
        logger.debug(f"Extract completed from {source_db_connection}.myschema.mytable_A ")
        return "### Mock extracted Data from Source A ###"


class ConcreteExtractorInstanceB:
    def extract(self, source_db_connection: IDBConnector, date_time: datetime):
        query = f"select * from myschema.mytable_B where date = {date_time}"
        logger.debug(query)
        logger.debug(f"Extract completed from {source_db_connection}.myschema.mytable_B ")
        return "### Mock extracted Data from Source B ###"
