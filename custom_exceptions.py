class ConnectionError(Exception):
    """
    Custom exception for handling connection errors
    """
    pass


class ConcreteSourceDBConnectionError(ConnectionError):
    pass


class ConcreteTargetDBConnectionError(ConnectionError):
    pass