from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInstanceIdentifier(_message.Message):
    __slots__ = ("id", "incarnation_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    incarnation_id: int
    def __init__(self, id: _Optional[int] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
