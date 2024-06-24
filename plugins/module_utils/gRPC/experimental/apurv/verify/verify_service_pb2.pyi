from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyRequest(_message.Message):
    __slots__ = ("filepath", "length", "page_seeds")
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PAGE_SEEDS_FIELD_NUMBER: _ClassVar[int]
    filepath: str
    length: int
    page_seeds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, filepath: _Optional[str] = ..., length: _Optional[int] = ..., page_seeds: _Optional[_Iterable[int]] = ...) -> None: ...

class VerifyResult(_message.Message):
    __slots__ = ("corrupt",)
    CORRUPT_FIELD_NUMBER: _ClassVar[int]
    corrupt: bool
    def __init__(self, corrupt: bool = ...) -> None: ...
