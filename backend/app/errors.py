# NOTE: Currently this module is not used
"""Custom Exceptions"""

class Duplicate(Exception):
    """Duplicate Exception is used for data duplication"""
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)

class Missing(Exception):
    """Missing Exception is used for data missing"""
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)
