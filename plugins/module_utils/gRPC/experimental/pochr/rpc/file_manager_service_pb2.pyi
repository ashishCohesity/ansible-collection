from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientRequest(_message.Message):
    __slots__ = ("type", "filename", "offset", "length")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATE: _ClassVar[ClientRequest.Type]
        READ: _ClassVar[ClientRequest.Type]
        WRITE: _ClassVar[ClientRequest.Type]
    CREATE: ClientRequest.Type
    READ: ClientRequest.Type
    WRITE: ClientRequest.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    type: ClientRequest.Type
    filename: str
    offset: int
    length: int
    def __init__(self, type: _Optional[_Union[ClientRequest.Type, str]] = ..., filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ServerResponse(_message.Message):
    __slots__ = ("success", "info", "sequence_id", "error_type")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ServerResponse.ErrorType]
        kInvalid: _ClassVar[ServerResponse.ErrorType]
        kWriteError: _ClassVar[ServerResponse.ErrorType]
        kPermissionDenied: _ClassVar[ServerResponse.ErrorType]
        kFileNotFound: _ClassVar[ServerResponse.ErrorType]
    kNoError: ServerResponse.ErrorType
    kInvalid: ServerResponse.ErrorType
    kWriteError: ServerResponse.ErrorType
    kPermissionDenied: ServerResponse.ErrorType
    kFileNotFound: ServerResponse.ErrorType
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    info: str
    sequence_id: int
    error_type: ServerResponse.ErrorType
    def __init__(self, success: bool = ..., info: _Optional[str] = ..., sequence_id: _Optional[int] = ..., error_type: _Optional[_Union[ServerResponse.ErrorType, str]] = ...) -> None: ...
