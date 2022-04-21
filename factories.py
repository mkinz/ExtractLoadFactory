import logging
from logging import Logger
from typing import Protocol

from dbcon import DBConnector, SourceDBConnector, TargetDBConnector
from extractor import Extractor, ConcreteExtractorInstanceA, ConcreteExtractorInstanceB
from loader import Loader, ConcreteLoaderInstanceA, ConcreteLoaderInstanceB
from validators import IValidator, ConcreteValidator

logger: Logger = logging.getLogger(__name__)


class DataRefresherFactory(Protocol):

    def get_source_connector(self) -> DBConnector:
        """returns a new source dbconnector instance"""
        ...

    def get_extractor(self) -> Extractor:
        """returns a new extractor instance"""
        ...

    def get_target_connector(self) -> DBConnector:
        """returns a new target dbconnector instance"""
        ...

    def get_loader(self) -> Loader:
        """returns a new loader instance"""
        ...

    def get_validator(self) -> IValidator:
        """returns a validator instance"""
        ...


class GenericConcreteDataRefresherFactory:

    def get_source_connector(self) -> DBConnector:
        return SourceDBConnector()

    def get_extractor(self) -> Extractor:
        pass

    def get_target_connector(self) -> DBConnector:
        return TargetDBConnector()

    def get_loader(self) -> Loader:
        pass

    def get_validator(self) -> IValidator:
        return ConcreteValidator()


class ConcreteDataRefresherFactoryA(GenericConcreteDataRefresherFactory):

    def get_extractor(self) -> Extractor:
        return ConcreteExtractorInstanceA()

    def get_loader(self) -> Loader:
        return ConcreteLoaderInstanceA()


class ConcreteDataRefresherFactoryB(GenericConcreteDataRefresherFactory):
    
    def get_extractor(self) -> Extractor:
        return ConcreteExtractorInstanceB()

    def get_loader(self) -> Loader:
        return ConcreteLoaderInstanceB()
