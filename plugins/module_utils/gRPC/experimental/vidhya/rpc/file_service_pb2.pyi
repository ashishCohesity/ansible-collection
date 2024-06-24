from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kFileExists: _ClassVar[Status]
    kNoError: _ClassVar[Status]
    kFailed: _ClassVar[Status]
kFileExists: Status
kNoError: Status
kFailed: Status

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, str]] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    data: bytes
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, str]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "read_length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    READ_LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    read_length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., read_length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("file_content", "status")
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    file_content: bytes
    status: Status
    def __init__(self, file_content: _Optional[bytes] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...
