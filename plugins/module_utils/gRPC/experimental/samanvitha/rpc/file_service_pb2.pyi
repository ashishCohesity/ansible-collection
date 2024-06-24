from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("error_type", "error_message")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[Error.ErrorType]
        kFileNotFound: _ClassVar[Error.ErrorType]
        kAlreadyExists: _ClassVar[Error.ErrorType]
        kUnknownError: _ClassVar[Error.ErrorType]
        kInvalid: _ClassVar[Error.ErrorType]
    kNoError: Error.ErrorType
    kFileNotFound: Error.ErrorType
    kAlreadyExists: Error.ErrorType
    kUnknownError: Error.ErrorType
    kInvalid: Error.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_type: Error.ErrorType
    error_message: str
    def __init__(self, error_type: _Optional[_Union[Error.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("error", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: Error
    data: bytes
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "offset", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    data: bytes
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
