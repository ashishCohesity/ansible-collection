from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATE: _ClassVar[RequestType]
    READ: _ClassVar[RequestType]
    WRITE: _ClassVar[RequestType]

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[ErrorCode]
    kInvalid: _ClassVar[ErrorCode]
    kWriteError: _ClassVar[ErrorCode]
    kPermissionDenied: _ClassVar[ErrorCode]
    kUnknownError: _ClassVar[ErrorCode]
CREATE: RequestType
READ: RequestType
WRITE: RequestType
kNoError: ErrorCode
kInvalid: ErrorCode
kWriteError: ErrorCode
kPermissionDenied: ErrorCode
kUnknownError: ErrorCode

class FileServiceArgs(_message.Message):
    __slots__ = ("filepath", "offset", "len", "requestType")
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    filepath: str
    offset: int
    len: int
    requestType: RequestType
    def __init__(self, filepath: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., requestType: _Optional[_Union[RequestType, str]] = ...) -> None: ...

class FileServiceResult(_message.Message):
    __slots__ = ("sequence_id", "error")
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sequence_id: int
    error: ErrorCode
    def __init__(self, sequence_id: _Optional[int] = ..., error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...
