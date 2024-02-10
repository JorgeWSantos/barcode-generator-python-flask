from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)


# body = {
#     "data": {
#         "elemento1": 123.15,
#         "elemento2": "hello",
#         "elemento3": 123
#     }
# }

# body_validator = Validator({
#     "data": {
#         "type": "dict",
#         "schema": {
#             "elemento1": { "type": "float", "required": True, "empty": False },
#             "elemento2": { "type": "string", "required": True, "empty": True },
#             "elemento3": { "type": "string", "required": False, "empty": False },
#         }
#     }
# })

# response = body_validator.validate(body)

# print(response)
# print(body_validator.errors)
