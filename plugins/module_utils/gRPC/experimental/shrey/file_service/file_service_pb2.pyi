from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("name", "length", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    length: int
    offset: int
    def __init__(self, name: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("content", "error")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    error: bool
    def __init__(self, content: _Optional[bytes] = ..., error: bool = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("name", "content", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: bytes
    offset: int
    def __init__(self, name: _Optional[str] = ..., content: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...
