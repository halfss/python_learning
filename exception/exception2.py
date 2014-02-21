class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class InputErro(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
