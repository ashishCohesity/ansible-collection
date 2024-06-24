from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("is_success", "err_str")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    err_str: str
    def __init__(self, is_success: bool = ..., err_str: _Optional[str] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("is_success", "err_str", "sequence_num")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    err_str: str
    sequence_num: int
    def __init__(self, is_success: bool = ..., err_str: _Optional[str] = ..., sequence_num: _Optional[int] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("file_name", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("is_success", "err_str", "num_bytes_written", "sequence_num")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    err_str: str
    num_bytes_written: int
    sequence_num: int
    def __init__(self, is_success: bool = ..., err_str: _Optional[str] = ..., num_bytes_written: _Optional[int] = ..., sequence_num: _Optional[int] = ...) -> None: ...
