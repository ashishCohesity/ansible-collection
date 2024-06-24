from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImportNoArenaNestedMessage(_message.Message):
    __slots__ = ("d",)
    D_FIELD_NUMBER: _ClassVar[int]
    d: int
    def __init__(self, d: _Optional[int] = ...) -> None: ...
