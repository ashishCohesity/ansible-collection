from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Checkpoint(_message.Message):
    __slots__ = ("nodes", "dir")
    NODES_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedScalarFieldContainer[int]
    dir: bool
    def __init__(self, nodes: _Optional[_Iterable[int]] = ..., dir: bool = ...) -> None: ...
