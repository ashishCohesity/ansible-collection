from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileSystemRequest(_message.Message):
    __slots__ = ("filename", "offset", "len", "request_type")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Create: _ClassVar[FileSystemRequest.RequestType]
        Read: _ClassVar[FileSystemRequest.RequestType]
        Write: _ClassVar[FileSystemRequest.RequestType]
    Create: FileSystemRequest.RequestType
    Read: FileSystemRequest.RequestType
    Write: FileSystemRequest.RequestType
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    request_type: FileSystemRequest.RequestType
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., request_type: _Optional[_Union[FileSystemRequest.RequestType, str]] = ...) -> None: ...

class FileSystemResult(_message.Message):
    __slots__ = ("error_type",)
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[FileSystemResult.ErrorType]
        kOpenError: _ClassVar[FileSystemResult.ErrorType]
        kReadError: _ClassVar[FileSystemResult.ErrorType]
        kWriteError: _ClassVar[FileSystemResult.ErrorType]
    kNoError: FileSystemResult.ErrorType
    kOpenError: FileSystemResult.ErrorType
    kReadError: FileSystemResult.ErrorType
    kWriteError: FileSystemResult.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_type: FileSystemResult.ErrorType
    def __init__(self, error_type: _Optional[_Union[FileSystemResult.ErrorType, str]] = ...) -> None: ...
