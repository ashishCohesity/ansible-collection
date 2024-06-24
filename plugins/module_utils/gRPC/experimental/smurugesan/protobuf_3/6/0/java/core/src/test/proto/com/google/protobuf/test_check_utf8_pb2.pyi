from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StringWrapper(_message.Message):
    __slots__ = ("req", "opt", "rep")
    REQ_FIELD_NUMBER: _ClassVar[int]
    OPT_FIELD_NUMBER: _ClassVar[int]
    REP_FIELD_NUMBER: _ClassVar[int]
    req: str
    opt: str
    rep: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, req: _Optional[str] = ..., opt: _Optional[str] = ..., rep: _Optional[_Iterable[str]] = ...) -> None: ...

class BytesWrapper(_message.Message):
    __slots__ = ("req", "opt", "rep")
    REQ_FIELD_NUMBER: _ClassVar[int]
    OPT_FIELD_NUMBER: _ClassVar[int]
    REP_FIELD_NUMBER: _ClassVar[int]
    req: bytes
    opt: bytes
    rep: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, req: _Optional[bytes] = ..., opt: _Optional[bytes] = ..., rep: _Optional[_Iterable[bytes]] = ...) -> None: ...
