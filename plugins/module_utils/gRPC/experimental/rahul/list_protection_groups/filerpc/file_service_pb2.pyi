from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("fid", "max_len")
    FID_FIELD_NUMBER: _ClassVar[int]
    MAX_LEN_FIELD_NUMBER: _ClassVar[int]
    fid: int
    max_len: int
    def __init__(self, fid: _Optional[int] = ..., max_len: _Optional[int] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("is_success", "message")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    message: str
    def __init__(self, is_success: bool = ..., message: _Optional[str] = ...) -> None: ...

class FileRequest(_message.Message):
    __slots__ = ("fid", "offset", "length")
    FID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    fid: int
    offset: int
    length: int
    def __init__(self, fid: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileResult(_message.Message):
    __slots__ = ("is_success", "message", "data", "timestamp")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    message: str
    data: str
    timestamp: int
    def __init__(self, is_success: bool = ..., message: _Optional[str] = ..., data: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
