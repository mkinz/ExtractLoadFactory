import logging
from logging import Logger
from typing import Protocol

from dbcon import IDBConnector, ConcreteSourceDBConnector, ConcreteTargetDBConnector
from extractor import IExtractor, GenericConcreteExtractor
from loader import ILoader, GenericConcreteLoader
from validators import IValidator, ConcreteValidator

logger: Logger = logging.getLogger(__name__)


class IDataRefresherFactory(Protocol):
    """
    Interface that establishes factory protocol
    """

    def get_source_db_connector_object(self) -> IDBConnector:
        """returns a new source dbconnector instance"""
        ...

    def get_target_db_connector_object(self) -> IDBConnector:
        """returns a new target dbconnector instance"""
        ...

    def get_extractor_object(self) -> IExtractor:
        """returns a new extractor instance"""
        ...

    def get_loader_object(self) -> ILoader:
        """returns a new loader instance"""
        ...

    def get_validator_object(self) -> IValidator:
        """returns a validator instance"""
        ...

    def get_extraction_query(self, schema: str, date_range_start: str, date_range_end: str) -> str:
        ...

    def get_data_load_query(self, schema: str, date_range_start: str, date_range_end: str) -> str:
        ...

    def get_source_table_name(self) -> str:
        ...

    def get_target_table_name(self) -> str:
        ...


class GenericConcreteDataRefresherFactory:

    def get_source_db_connector_object(self) -> IDBConnector:
        return ConcreteSourceDBConnector()

    def get_extractor_object(self) -> IExtractor:
        pass

    def get_target_db_connector_object(self) -> IDBConnector:
        return ConcreteTargetDBConnector()

    def get_loader_object(self) -> ILoader:
        pass

    def get_validator_object(self) -> IValidator:
        return ConcreteValidator()

    def get_extraction_query(self, schema: str, date_range_start: str, date_range_end: str) -> str:
        pass

    def get_data_load_query(self, schema: str, date_range_start: str, date_range_end: str) -> str:
        pass

    def get_source_table_name(self) -> str:
        pass

    def get_target_table_name(self) -> str:
        pass


class ConcreteDataRefresherFactoryA(GenericConcreteDataRefresherFactory):

    def get_extractor_object(self) -> GenericConcreteExtractor:
        return GenericConcreteExtractor()

    def get_loader_object(self) -> ILoader:
        return GenericConcreteLoader()


class ConcreteDataRefresherFactoryB(GenericConcreteDataRefresherFactory):
    
    def get_extractor_object(self) -> GenericConcreteExtractor:
        return GenericConcreteExtractor()

    def get_loader_object(self) -> ILoader:
        return GenericConcreteLoader()
