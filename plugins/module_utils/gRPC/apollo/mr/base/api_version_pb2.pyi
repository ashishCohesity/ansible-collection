from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class APIVersion(_message.Message):
    __slots__ = ("mr_version", "action_exec_version")
    MR_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXEC_VERSION_FIELD_NUMBER: _ClassVar[int]
    mr_version: int
    action_exec_version: int
    def __init__(self, mr_version: _Optional[int] = ..., action_exec_version: _Optional[int] = ...) -> None: ...
