import logging
from logging import Logger
from typing import Protocol, runtime_checkable

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


class ConcreteSourceDBConnector(GenericConnector):
    dbname = 'my_source_database'
    username = 'my_user'
    connection_str = 'my_source_connection_string'


class ConcreteTargetDBConnector(GenericConnector):
    dbname = 'my_target_database'
    username = 'my_user'
    connection_str = 'my_target_connection_string'
