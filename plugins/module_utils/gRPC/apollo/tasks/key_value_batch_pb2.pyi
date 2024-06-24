from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KeyValueBatchProto(_message.Message):
    __slots__ = ("keys", "values")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, keys: _Optional[_Iterable[bytes]] = ..., values: _Optional[_Iterable[bytes]] = ...) -> None: ...
