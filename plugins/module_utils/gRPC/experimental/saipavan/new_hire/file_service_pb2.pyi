from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESS: _ClassVar[ResponseStatus]
    FAILURE: _ClassVar[ResponseStatus]
SUCCESS: ResponseStatus
FAILURE: ResponseStatus

class CreateFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("status", "error_msg")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    error_msg: str
    def __init__(self, status: _Optional[_Union[ResponseStatus, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_path", "offset")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset: int
    def __init__(self, file_path: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("status", "error_msg", "write_sequence")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    WRITE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    error_msg: str
    write_sequence: int
    def __init__(self, status: _Optional[_Union[ResponseStatus, str]] = ..., error_msg: _Optional[str] = ..., write_sequence: _Optional[int] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_path", "offset", "length")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset: int
    length: int
    def __init__(self, file_path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("status", "error_msg")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    error_msg: str
    def __init__(self, status: _Optional[_Union[ResponseStatus, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
