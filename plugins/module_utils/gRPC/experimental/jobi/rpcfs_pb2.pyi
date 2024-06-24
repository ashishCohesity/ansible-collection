from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("name", "offset", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    size: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("error", "length")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    error: int
    length: int
    def __init__(self, error: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("name", "offset", "length")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    length: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("error", "length")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    error: int
    length: int
    def __init__(self, error: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
