from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateResp(_message.Message):
    __slots__ = ("err",)
    ERR_FIELD_NUMBER: _ClassVar[int]
    err: int
    def __init__(self, err: _Optional[int] = ...) -> None: ...

class ReadReq(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadResp(_message.Message):
    __slots__ = ("err", "bytesRead", "data")
    ERR_FIELD_NUMBER: _ClassVar[int]
    BYTESREAD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    err: int
    bytesRead: int
    data: bytes
    def __init__(self, err: _Optional[int] = ..., bytesRead: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteReq(_message.Message):
    __slots__ = ("filename", "offset", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    data: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteResp(_message.Message):
    __slots__ = ("err", "bytesWritten")
    ERR_FIELD_NUMBER: _ClassVar[int]
    BYTESWRITTEN_FIELD_NUMBER: _ClassVar[int]
    err: int
    bytesWritten: int
    def __init__(self, err: _Optional[int] = ..., bytesWritten: _Optional[int] = ...) -> None: ...
