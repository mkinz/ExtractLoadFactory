class ConnectionError(Exception):
    """
    Custom exception for handling connection errors
    """
    pass


class SourceConnectionError(ConnectionError):
    pass


class TargetConnectionError(ConnectionError):
    pass