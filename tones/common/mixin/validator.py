from tones.common.exception import *


class ValidatorMixIn:

    def is_required(self, target, caption: str):
        if target is None:
            raise RequiredError(caption)

    def is_include_of(self, target, whole: list, caption: str):
        if target not in whole:
            raise IncludeError(caption, str(target))

    def is_natural(self, target: int, caption):
        if target < 0:
            raise NaturalError(caption)

    def is_type_of(self, target, ideal: type, caption: str):
        if type(target) is not ideal:
            raise MyTypeError(caption, str(ideal), str(type(target)))
