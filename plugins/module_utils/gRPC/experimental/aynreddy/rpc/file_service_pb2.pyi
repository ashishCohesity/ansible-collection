from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[ServerError]
    kTimeout: _ClassVar[ServerError]
    kAlreadyExists: _ClassVar[ServerError]
    kPermissionDenied: _ClassVar[ServerError]
    kFileNotFound: _ClassVar[ServerError]
    kIOFail: _ClassVar[ServerError]
    kErrorCount: _ClassVar[ServerError]
kNoError: ServerError
kTimeout: ServerError
kAlreadyExists: ServerError
kPermissionDenied: ServerError
kFileNotFound: ServerError
kIOFail: ServerError
kErrorCount: ServerError

class CreateFileArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error_code", "error_msg")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_code: ServerError
    error_msg: str
    def __init__(self, error_code: _Optional[_Union[ServerError, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "size", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    size: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("error_code", "error_msg")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_code: ServerError
    error_msg: str
    def __init__(self, error_code: _Optional[_Union[ServerError, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("file_name", "size", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    size: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("error_code", "error_msg")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_code: ServerError
    error_msg: str
    def __init__(self, error_code: _Optional[_Union[ServerError, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
