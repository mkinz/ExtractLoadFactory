import logging
from logging import Logger
from typing import Protocol

logger: Logger = logging.getLogger(__name__)


class DBConnector(Protocol):
    def connect_to_db(self):
        pass


class SourceDBConnector:
    dbname = 'my_source_database'
    username = 'my_user'
    connection_str = 'my_source_connection_string'

    def connect_to_db(self):
        logger.info(f"Connected to {self.dbname} with user {self.username} and"
                    f"connection details '{self.connection_str}'.")
        return self.dbname


class TargetDBConnector:
    dbname = 'my_target_database'
    username = 'my_user'
    connection_str = 'my_target_connection_string'

    def connect_to_db(self):
        logger.info(f"Connected to {self.dbname} with user {self.username} and"
                    f"connection details '{self.connection_str}'.")
        return self.dbname
