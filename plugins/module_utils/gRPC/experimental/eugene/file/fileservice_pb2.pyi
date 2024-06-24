from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: int
    def __init__(self, error: _Optional[int] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("filename", "data", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    data: bytes
    offset: int
    def __init__(self, filename: _Optional[str] = ..., data: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("error", "bytes_written")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    error: int
    bytes_written: int
    def __init__(self, error: _Optional[int] = ..., bytes_written: _Optional[int] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("filename", "count", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    count: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("error", "bytes_read", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: int
    bytes_read: int
    data: bytes
    def __init__(self, error: _Optional[int] = ..., bytes_read: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
