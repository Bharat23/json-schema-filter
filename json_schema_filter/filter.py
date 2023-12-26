from typing import Dict

from jsonschema import validators
from jsonschema.validators import Draft202012Validator

from .validators import Registry
from .logging import logger

class Filterer:
    def filter_now(self, input_data):
        """
        """
        if not isinstance(input_data, list):
            input_data = [input_data]
        for idx, data in enumerate(input_data):
            errors = self.iter_errors(data)
            is_match = True
            messages = []
            for inner_idx, err in enumerate(errors):
                path = "->".join(err.json_path.split(".")[1:])
                messages.append(f"{inner_idx+1}. {path}: {err.message}")
                is_match = False
            if not is_match:
                output = f"Filtered item: [{idx}]\n" + "\t" + "\n\t".join(messages)
                logger.warning(output)

class JsonSchemaFilter:

    def __new__(cls, schema: Dict, schema_version = Draft202012Validator) -> "JsonSchemaFilter":
        all_validators = dict(schema_version.VALIDATORS) 
        all_validators.update(Registry.registered_validators)
        MyValidator = validators.create(meta_schema=schema_version.META_SCHEMA, validators=all_validators)
        MyFilter = type('Filter', (MyValidator, Filterer), {"abc": "lambda"})
        return MyFilter(schema=schema)

    def __init__(self, schema: Dict, schema_version = Draft202012Validator) -> None:
        self.validator = schema_version
