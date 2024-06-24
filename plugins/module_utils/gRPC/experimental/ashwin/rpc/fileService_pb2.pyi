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

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("filename", "length", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    length: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    data: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("success", "err_msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    err_msg: str
    def __init__(self, success: bool = ..., err_msg: _Optional[str] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("err_msg", "success", "text")
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    err_msg: str
    success: bool
    text: bytes
    def __init__(self, err_msg: _Optional[str] = ..., success: bool = ..., text: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("success", "err_msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    err_msg: str
    def __init__(self, success: bool = ..., err_msg: _Optional[str] = ...) -> None: ...
