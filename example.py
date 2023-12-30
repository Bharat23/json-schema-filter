# from yaml import safe_load
# from pprint import pprint
# from json_schema_filter import JsonSchemaFilter

# # import the schema
# with open("input_to_schema.yaml", "r+") as f:
#     schema_2 = safe_load(f.read())

# filter = JsonSchemaFilter(schema_2)

# input_data = [
#     {
#         "name": "asdasd",
#         "place": "",
#         "age": 1,
#         "tags": [
#             {"key": "StackId", "value": "test-stack"},
#             {"key": "some", "value": "else"},
#         ],
#     },
#     {
#         "name": "asdasd",
#         "age": 10,
#         "address": {"street": "ads"},
#         "tags": [
#             {"key": "StackId", "value": "test-stack"},
#             {"key": "some", "value": "else"},
#         ],
#     },
# ]
# pprint(filter.filter(input_data))

from json_schema_filter import JsonSchemaFilter

schema = {
    "properties": {
        "name": {
            "type": "string",
            "equals": "Shakespeare"
        }
    },
    "required": ["name"]
}

input_data = [
    {"name": "what is in the name"},
    {"name": "Shakespeare"},
    {"name": "hamlet"},
]

print(JsonSchemaFilter(schema).filter(input_data))