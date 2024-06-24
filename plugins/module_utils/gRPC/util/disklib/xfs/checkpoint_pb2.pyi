from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class XFSCheckpoint(_message.Message):
    __slots__ = ("nodes", "dir", "completed")
    NODES_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedScalarFieldContainer[int]
    dir: bool
    completed: bool
    def __init__(self, nodes: _Optional[_Iterable[int]] = ..., dir: bool = ..., completed: bool = ...) -> None: ...
