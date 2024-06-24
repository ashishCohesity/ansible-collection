from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ViewActionArg(_message.Message):
    __slots__ = ("task_id",)
    VIEW_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    view_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...
