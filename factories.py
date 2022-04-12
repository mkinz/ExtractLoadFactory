import logging
from logging import Logger
from dataclasses import dataclass
from typing import Protocol

from dbcon import DBConnector, SourceDBConnector, TargetDBConnector
from extractor import Extractor, ConcreteExtractorInstanceA
from loader import Loader, ConcreteLoaderInstanceA

logger: Logger = logging.getLogger(__name__)


@dataclass
class DataRefresherFactory(Protocol):

    @staticmethod
    def get_source_connector() -> DBConnector:
        """returns a new source dbconnector instance"""

    @staticmethod
    def get_extractor() -> Extractor:
        """returns a new extractor instance"""

    @staticmethod
    def get_target_connector() -> DBConnector:
        """returns a new target dbconnector instance"""

    @staticmethod
    def get_loader() -> Loader:
        """returns a new loader instance"""


@dataclass
class ConcreteDataRefresherFactoryA:

    @staticmethod
    def get_source_connector() -> DBConnector:
        return SourceDBConnector()

    @staticmethod
    def get_extractor() -> Extractor:
        return ConcreteExtractorInstanceA()

    @staticmethod
    def get_target_connector() -> DBConnector:
        return TargetDBConnector()

    @staticmethod
    def get_loader() -> Loader:
        return ConcreteLoaderInstanceA()
