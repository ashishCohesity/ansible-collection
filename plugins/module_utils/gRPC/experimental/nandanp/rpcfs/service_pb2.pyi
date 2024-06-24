from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResult(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class FileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len", "op", "buf")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        read: _ClassVar[FileRangeRequest.Operation]
        write: _ClassVar[FileRangeRequest.Operation]
    read: FileRangeRequest.Operation
    write: FileRangeRequest.Operation
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    op: FileRangeRequest.Operation
    buf: str
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., op: _Optional[_Union[FileRangeRequest.Operation, str]] = ..., buf: _Optional[str] = ...) -> None: ...

class FileSystemResponse(_message.Message):
    __slots__ = ("status", "nbytes", "buf")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NBYTES_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    status: bool
    nbytes: int
    buf: str
    def __init__(self, status: bool = ..., nbytes: _Optional[int] = ..., buf: _Optional[str] = ...) -> None: ...
