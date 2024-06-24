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

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResult(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "max_length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    max_length: int
    def __init__(self, filename: _Optional[str] = ..., max_length: _Optional[int] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error_code", "error_str")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STR_FIELD_NUMBER: _ClassVar[int]
    error_code: ErrorCode
    error_str: str
    def __init__(self, error_code: _Optional[_Union[ErrorCode, str]] = ..., error_str: _Optional[str] = ...) -> None: ...

class FileIORequest(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileIOResult(_message.Message):
    __slots__ = ("error_code", "error_str", "seq_id")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STR_FIELD_NUMBER: _ClassVar[int]
    SEQ_ID_FIELD_NUMBER: _ClassVar[int]
    error_code: ErrorCode
    error_str: str
    seq_id: int
    def __init__(self, error_code: _Optional[_Union[ErrorCode, str]] = ..., error_str: _Optional[str] = ..., seq_id: _Optional[int] = ...) -> None: ...
