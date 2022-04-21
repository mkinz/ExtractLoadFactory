import logging
from logging import Logger
from typing import Protocol

from dbcon import IDBConnector, SourceDBConnector, TargetDBConnector
from iextractor import IExtractor, ConcreteExtractorInstanceA, ConcreteExtractorInstanceB
from iloader import ILoader, ConcreteLoaderInstanceA, ConcreteLoaderInstanceB
from validators import IValidator, ConcreteValidator

logger: Logger = logging.getLogger(__name__)


class IDataRefresherFactory(Protocol):
    """
    Interface that establishes factory protocol
    """

    def get_source_connector(self) -> IDBConnector:
        """returns a new source dbconnector instance"""
        ...

    def get_extractor(self) -> IExtractor:
        """returns a new extractor instance"""
        ...

    def get_target_connector(self) -> IDBConnector:
        """returns a new target dbconnector instance"""
        ...

    def get_loader(self) -> ILoader:
        """returns a new loader instance"""
        ...

    def get_validator(self) -> IValidator:
        """returns a validator instance"""
        ...


class GenericConcreteDataRefresherFactory:

    def get_source_connector(self) -> IDBConnector:
        return SourceDBConnector()

    def get_extractor(self) -> IExtractor:
        pass

    def get_target_connector(self) -> IDBConnector:
        return TargetDBConnector()

    def get_loader(self) -> ILoader:
        pass

    def get_validator(self) -> IValidator:
        return ConcreteValidator()


class ConcreteDataRefresherFactoryA(GenericConcreteDataRefresherFactory):

    def get_extractor(self) -> IExtractor:
        return ConcreteExtractorInstanceA()

    def get_loader(self) -> ILoader:
        return ConcreteLoaderInstanceA()


class ConcreteDataRefresherFactoryB(GenericConcreteDataRefresherFactory):
    
    def get_extractor(self) -> IExtractor:
        return ConcreteExtractorInstanceB()

    def get_loader(self) -> ILoader:
        return ConcreteLoaderInstanceB()
