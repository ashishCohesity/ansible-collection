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

class ReadWriteRequest(_message.Message):
    __slots__ = ("file_num", "io_op_num", "offset", "length")
    FILE_NUM_FIELD_NUMBER: _ClassVar[int]
    IO_OP_NUM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_num: int
    io_op_num: int
    offset: int
    length: int
    def __init__(self, file_num: _Optional[int] = ..., io_op_num: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileServiceRequestResult(_message.Message):
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
