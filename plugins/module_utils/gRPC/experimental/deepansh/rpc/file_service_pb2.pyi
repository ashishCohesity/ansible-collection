from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadFileArg(_message.Message):
    __slots__ = ("name", "offset", "len")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteFileArg(_message.Message):
    __slots__ = ("name", "offset", "len")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("service_num",)
    SERVICE_NUM_FIELD_NUMBER: _ClassVar[int]
    service_num: int
    def __init__(self, service_num: _Optional[int] = ...) -> None: ...
