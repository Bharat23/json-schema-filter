from yaml import safe_load
from pprint import pprint
from json_schema_filter.filter import JsonSchemaFilter

with open("input_to_schema.yaml", "r+") as f:
    schema_2 = safe_load(f.read())

# pprint(schema)
# pprint(schema_2)

# final_schema = {"type": "object", "properties": {}, "required": []}
# for key, value in schema_2.items():
#     final_schema["properties"][key] = value
#     if "required" in value and value["required"]:
#         final_schema["required"].append(key)
# pprint(final_schema)

# all_validators = dict(Draft7Validator.VALIDATORS) 
# all_validators['equals'] = equals 
# MyValidator = validators.create(meta_schema=Draft7Validator.META_SCHEMA, validators=all_validators)

# pprint(schema)
# validator = MyValidator(schema=schema_2)
# pprint(schema_2)
from json_schema_filter.validators import Registry
filter = JsonSchemaFilter(schema_2)

input_data = [
    {"name": "asdasd", "age": 1, "tags": [{"key": "StackId", "value": "test-stack"}, {"key": "some", "value": "else"}]},
    {"name": "asdasd", "age": 12, "address": {"street": 1}, "tags": [{"key": "StackId", "value": "test-stack"}, {"key": "some", "value": "else"}]}
]
# filter.filter(input_data=input_data)
# errors = filter.iter_errors(input_data)
# filter.filter(input_data)
filter.filter_now(input_data)
# for err in errors:
#     print(f"{err.json_path}: {err.message}")
