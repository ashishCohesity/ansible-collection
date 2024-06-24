from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("filename", "length", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    length: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("filename", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("status", "timestamp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: bool
    timestamp: int
    def __init__(self, status: bool = ..., timestamp: _Optional[int] = ...) -> None: ...
