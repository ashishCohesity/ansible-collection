from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReturnCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Success: _ClassVar[ReturnCode]
    FileAlreadyExists: _ClassVar[ReturnCode]
    FileDoesNotExist: _ClassVar[ReturnCode]
    PermissionDenied: _ClassVar[ReturnCode]
    BadRequest: _ClassVar[ReturnCode]
    UnknownError: _ClassVar[ReturnCode]
Success: ReturnCode
FileAlreadyExists: ReturnCode
FileDoesNotExist: ReturnCode
PermissionDenied: ReturnCode
BadRequest: ReturnCode
UnknownError: ReturnCode

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("exit_code",)
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code: ReturnCode
    def __init__(self, exit_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("exit_code",)
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code: ReturnCode
    def __init__(self, exit_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "to_write")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TO_WRITE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    to_write: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., to_write: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("exit_code",)
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code: ReturnCode
    def __init__(self, exit_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...
