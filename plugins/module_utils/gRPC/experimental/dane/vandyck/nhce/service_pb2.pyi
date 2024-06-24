from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteRequest(_message.Message):
    __slots__ = ("file", "offset", "delay")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    delay: int
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("bytes_written",)
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    bytes_written: int
    def __init__(self, bytes_written: _Optional[int] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("file", "offset", "size", "delay")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    size: int
    delay: int
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("bytes_read",)
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    bytes_read: int
    def __init__(self, bytes_read: _Optional[int] = ...) -> None: ...
