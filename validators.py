import logging
import pandas as pd
from logging import Logger
from abc import ABC, abstractmethod

logger: Logger = logging.getLogger(__name__)


class IValidator(ABC):
    """
    Class to handle data validation responsibility
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, data_to_validate: pd.DataFrame) -> None:
        pass


class ConcreteValidator(IValidator):
    def __init__(self):
        self.validated_data = False

    def validate(self, data_to_validate: pd.DataFrame) -> None:
        if len(data_to_validate) > 0:
            self.validated_data = True
            logger.info("Data Validated! Proceeding to load stage...")
        else:
            logger.info("Could not validate data. Exiting...")
