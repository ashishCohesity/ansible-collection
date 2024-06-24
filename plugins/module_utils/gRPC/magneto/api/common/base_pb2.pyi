from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IndexingPolicyProto(_message.Message):
    __slots__ = ("enable_indexing", "allow_prefixes", "deny_prefixes")
    ENABLE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    DENY_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    enable_indexing: bool
    allow_prefixes: _containers.RepeatedScalarFieldContainer[str]
    deny_prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enable_indexing: bool = ..., allow_prefixes: _Optional[_Iterable[str]] = ..., deny_prefixes: _Optional[_Iterable[str]] = ...) -> None: ...
