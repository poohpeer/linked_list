class Error(Exception):
    """Base exception"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class EmptyNodeException(Error):
    """Use if node=None"""
    def __init__(self, *args, **kwargs):
        Error.__init__(self, *args, **kwargs)
    pass
