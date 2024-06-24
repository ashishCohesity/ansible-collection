from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReturnCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Success: _ClassVar[ReturnCode]
    AlreadyExists: _ClassVar[ReturnCode]
    DoesNotExist: _ClassVar[ReturnCode]
    PermissionDenied: _ClassVar[ReturnCode]
    UnknownError: _ClassVar[ReturnCode]
Success: ReturnCode
AlreadyExists: ReturnCode
DoesNotExist: ReturnCode
PermissionDenied: ReturnCode
UnknownError: ReturnCode

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("rc",)
    RC_FIELD_NUMBER: _ClassVar[int]
    rc: ReturnCode
    def __init__(self, rc: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("rc", "data")
    RC_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    rc: ReturnCode
    data: bytes
    def __init__(self, rc: _Optional[_Union[ReturnCode, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "offset", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    data: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("rc",)
    RC_FIELD_NUMBER: _ClassVar[int]
    rc: ReturnCode
    def __init__(self, rc: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...
