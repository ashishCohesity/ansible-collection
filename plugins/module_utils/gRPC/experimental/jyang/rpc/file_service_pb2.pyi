from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("file_num", "max_file_length")
    FILE_NUM_FIELD_NUMBER: _ClassVar[int]
    MAX_FILE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_num: int
    max_file_length: int
    def __init__(self, file_num: _Optional[int] = ..., max_file_length: _Optional[int] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("status", "timestamp", "success", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    timestamp: int
    success: bool
    message: str
    def __init__(self, status: _Optional[int] = ..., timestamp: _Optional[int] = ..., success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ReadWriteFileRequest(_message.Message):
    __slots__ = ("file_num", "offset", "length")
    FILE_NUM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_num: int
    offset: int
    length: int
    def __init__(self, file_num: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadWriteFileResponse(_message.Message):
    __slots__ = ("success", "message", "data", "timestamp")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    data: str
    timestamp: int
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., data: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
