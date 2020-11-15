class IncludeError(Exception):

    """
    use self when target is not include of the list you expected 
    """

    def __init__(self, caption: str,value:str):
        self.c = caption
        self.v = value

    def __str__(self) -> str:
        return f"{self.c} value(:{self.v}) is not include of the list you expected."


class RequiredError(Exception):

    """
    use self when target does not exist in request
    """

    def __init__(self, v: str):
        self.v = v

    def __str__(self) -> str:
        return f"{self.v} is required."


class NaturalError(Exception):

    """
    use self when target is not natural number.
    """

    def __init__(self, v: str):
        self.v = v

    def __str__(self) -> str:
        return f"{self.v} must be natural number."


class ForbiddenSetAttrError(Exception):

    """
    use self when target can't be set by setattr(target, value) or self.target = value
    """

    def __init__(self, v: str):
        self.v = v

    def __str__(self) -> str:
        return f"Can\'t rebind the target: {self.v}."


class MyTypeError(TypeError):

    """
    use self when target is not expected type.
    """

    def __init__(self, caption: str, expected, actual):
        self.caption = caption
        self.expected = expected
        self.actual = actual

    def __str__(self) -> str:
        return f"The value is not expected type,variable name: {self.caption} ,expected: {self.expected},actual: {self.actual}."
