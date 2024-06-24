from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("success", "error_msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_msg: str
    def __init__(self, success: bool = ..., error_msg: _Optional[str] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("file_path", "offset")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset: int
    def __init__(self, file_path: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("success", "error_msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_msg: str
    def __init__(self, success: bool = ..., error_msg: _Optional[str] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("file_path", "offset", "length")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset: int
    length: int
    def __init__(self, file_path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("success", "error_msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_msg: str
    def __init__(self, success: bool = ..., error_msg: _Optional[str] = ...) -> None: ...
