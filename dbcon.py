import logging
from logging import Logger
from typing import Protocol, runtime_checkable

from custom_exceptions import ConcreteSourceDBConnectionError, ConcreteTargetDBConnectionError
logger: Logger = logging.getLogger(__name__)


@runtime_checkable
class IDBConnector(Protocol):
    """
    Interface that establishes dbconnections protocol
    """

    def __init__(self):
        ...

    def connect_to_db(self):
        ...

    def get_connection_status(self):
        ...


class GenericConnector:
    dbname = None
    username = None
    connection_str = None

    def __init__(self):
        self.connected = False

    def connect_to_db(self):
        self.connected = True
        logger.info(f"Connected to {self.dbname} with user {self.username} and"
                    f"connection details '{self.connection_str}'.")
        return self.dbname

    def get_connection_status(self):
        pass


class ConcreteSourceDBConnector(GenericConnector):
    dbname = 'my_source_database'
    username = 'my_user'
    connection_str = 'my_source_connection_string'

    def get_connection_status(self):
        if not self.connected:
            raise ConcreteSourceDBConnectionError
        else:
            logger.info("Successfully connected to Source Database")


class ConcreteTargetDBConnector(GenericConnector):
    dbname = 'my_target_database'
    username = 'my_user'
    connection_str = 'my_target_connection_string'

    def get_connection_status(self):
        if not self.connected:
            raise ConcreteTargetDBConnectionError
        else:
            logger.info("Successfully connected to Source Database")
