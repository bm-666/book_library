from enum import StrEnum

class ResponseStatus(StrEnum):
    COMMAND_NOT_AVAILABLE = 'command_not_available'
    DOES_NOT_EXIST = 'object_does_not_exist'
    FORBIDDEN = 'forbidden'
    INCORRECT_PARAMETER = 'incorrect_parameter'
    OBJECT_NOT_AVAILABLE = 'object_not_available'
    SUCCESS = 'success'
