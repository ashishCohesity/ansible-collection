from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestConfigClientProto(_message.Message):
    __slots__ = ("version", "id", "name")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    version: int
    id: int
    name: str
    def __init__(self, version: _Optional[int] = ..., id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
