from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[Error]
    kCreateFileFailed: _ClassVar[Error]
    kOpenFileFailed: _ClassVar[Error]
    kWriteFileFailed: _ClassVar[Error]
    kReadFileFailed: _ClassVar[Error]
    kInvalidPath: _ClassVar[Error]
    kInvalidData: _ClassVar[Error]
    kInvalidLength: _ClassVar[Error]
kNoError: Error
kCreateFileFailed: Error
kOpenFileFailed: Error
kWriteFileFailed: Error
kReadFileFailed: Error
kInvalidPath: Error
kInvalidData: Error
kInvalidLength: Error

class CreateFileRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error", "error_detail")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error: Error
    error_detail: str
    def __init__(self, error: _Optional[_Union[Error, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("path", "offset", "data")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    data: bytes
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "error_detail")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error: Error
    error_detail: str
    def __init__(self, error: _Optional[_Union[Error, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("path", "offset", "length")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    length: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "error_detail", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: Error
    error_detail: str
    data: bytes
    def __init__(self, error: _Optional[_Union[Error, str]] = ..., error_detail: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
