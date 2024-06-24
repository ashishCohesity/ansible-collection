from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[ErrorCode]
    kFileAlreadyExists: _ClassVar[ErrorCode]
    kFileNotFound: _ClassVar[ErrorCode]
    kUnknownError: _ClassVar[ErrorCode]
    kInvalidRequest: _ClassVar[ErrorCode]
kSuccess: ErrorCode
kFileAlreadyExists: ErrorCode
kFileNotFound: ErrorCode
kUnknownError: ErrorCode
kInvalidRequest: ErrorCode

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "max_length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    max_length: int
    def __init__(self, filename: _Optional[str] = ..., max_length: _Optional[int] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("status_code", "error_msg")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    status_code: ErrorCode
    error_msg: str
    def __init__(self, status_code: _Optional[_Union[ErrorCode, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class FileIORequest(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileIOResponse(_message.Message):
    __slots__ = ("status_code", "error_msg", "sequence_id")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    status_code: ErrorCode
    error_msg: str
    sequence_id: int
    def __init__(self, status_code: _Optional[_Union[ErrorCode, str]] = ..., error_msg: _Optional[str] = ..., sequence_id: _Optional[int] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
