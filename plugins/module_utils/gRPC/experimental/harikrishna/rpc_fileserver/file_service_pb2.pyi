from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorMessage(_message.Message):
    __slots__ = ("error_type", "error_string")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorMessage.ErrorType]
        kInvalid: _ClassVar[ErrorMessage.ErrorType]
        kUnableToCreate: _ClassVar[ErrorMessage.ErrorType]
        kUnknownError: _ClassVar[ErrorMessage.ErrorType]
        kUnableToOpen: _ClassVar[ErrorMessage.ErrorType]
        kInvalidRange: _ClassVar[ErrorMessage.ErrorType]
    kNoError: ErrorMessage.ErrorType
    kInvalid: ErrorMessage.ErrorType
    kUnableToCreate: ErrorMessage.ErrorType
    kUnknownError: ErrorMessage.ErrorType
    kUnableToOpen: ErrorMessage.ErrorType
    kInvalidRange: ErrorMessage.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STRING_FIELD_NUMBER: _ClassVar[int]
    error_type: ErrorMessage.ErrorType
    error_string: str
    def __init__(self, error_type: _Optional[_Union[ErrorMessage.ErrorType, str]] = ..., error_string: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: ErrorMessage
    def __init__(self, error_message: _Optional[_Union[ErrorMessage, _Mapping]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("timestamp", "error_message")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    error_message: ErrorMessage
    def __init__(self, timestamp: _Optional[int] = ..., error_message: _Optional[_Union[ErrorMessage, _Mapping]] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("timestamp", "error_message")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    error_message: ErrorMessage
    def __init__(self, timestamp: _Optional[int] = ..., error_message: _Optional[_Union[ErrorMessage, _Mapping]] = ...) -> None: ...
