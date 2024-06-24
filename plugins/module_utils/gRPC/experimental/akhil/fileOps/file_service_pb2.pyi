from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("error_type", "error_message")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[CreateResponse.ErrorType]
        kUnableToCreate: _ClassVar[CreateResponse.ErrorType]
    kNoError: CreateResponse.ErrorType
    kUnableToCreate: CreateResponse.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_type: CreateResponse.ErrorType
    error_message: str
    def __init__(self, error_type: _Optional[_Union[CreateResponse.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("buffer", "error_type", "error_message")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ReadResponse.ErrorType]
        kUnknownError: _ClassVar[ReadResponse.ErrorType]
        kUnableToOpen: _ClassVar[ReadResponse.ErrorType]
        kInvalidRange: _ClassVar[ReadResponse.ErrorType]
    kNoError: ReadResponse.ErrorType
    kUnknownError: ReadResponse.ErrorType
    kUnableToOpen: ReadResponse.ErrorType
    kInvalidRange: ReadResponse.ErrorType
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    buffer: str
    error_type: ReadResponse.ErrorType
    error_message: str
    def __init__(self, buffer: _Optional[str] = ..., error_type: _Optional[_Union[ReadResponse.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len", "input")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    input: str
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., input: _Optional[str] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("error_type", "error_message")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[WriteResponse.ErrorType]
        kUnableToCreate: _ClassVar[WriteResponse.ErrorType]
        kUnknownError: _ClassVar[WriteResponse.ErrorType]
        kInvalidRange: _ClassVar[WriteResponse.ErrorType]
    kNoError: WriteResponse.ErrorType
    kUnableToCreate: WriteResponse.ErrorType
    kUnknownError: WriteResponse.ErrorType
    kInvalidRange: WriteResponse.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_type: WriteResponse.ErrorType
    error_message: str
    def __init__(self, error_type: _Optional[_Union[WriteResponse.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
