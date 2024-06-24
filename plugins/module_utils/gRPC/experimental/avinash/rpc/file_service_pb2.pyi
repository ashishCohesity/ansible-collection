from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileServiceRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    data: bytes
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileServiceResponse(_message.Message):
    __slots__ = ("error_type", "data", "eof")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[FileServiceResponse.ErrorType]
        kAlreadyExists: _ClassVar[FileServiceResponse.ErrorType]
        kUnknownError: _ClassVar[FileServiceResponse.ErrorType]
    kNoError: FileServiceResponse.ErrorType
    kAlreadyExists: FileServiceResponse.ErrorType
    kUnknownError: FileServiceResponse.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error_type: FileServiceResponse.ErrorType
    data: bytes
    eof: bool
    def __init__(self, error_type: _Optional[_Union[FileServiceResponse.ErrorType, str]] = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...
