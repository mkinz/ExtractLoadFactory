class ConnectionError(Exception):
    """
    Custom exception for handling connection errors
    """
    pass


class ConcreteDBConnectionError(ConnectionError):
    pass