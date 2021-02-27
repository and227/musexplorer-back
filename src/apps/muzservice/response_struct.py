from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum

@dataclass_json
@dataclass
class ViewObject:
    status: str     # Статус
    data: object    # instance_object_json


@dataclass_json
@dataclass
class ErrorViewObject:
    status: str     # Статус
    message: str    # instance_object_json


class StatusResponse(Enum):
    SUCCESS = 'success'
    FAIL = 'fail'
    ERROR = 'error'
