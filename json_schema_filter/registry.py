from typing import Dict, Callable

class Registry:

    registered_validators: Dict = {}

    @classmethod
    def register(cls, fn: Callable):
        cls.registered_validators[fn.__name__] = fn
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper