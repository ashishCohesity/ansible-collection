from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteStudent(_message.Message):
    __slots__ = ("id", "name", "address")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    address: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class ReadStudent(_message.Message):
    __slots__ = ("id", "address")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    def __init__(self, id: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...
