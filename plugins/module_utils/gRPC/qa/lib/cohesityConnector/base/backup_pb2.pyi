from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IndexingPolicy(_message.Message):
    __slots__ = ("include_prefix_vec", "exclude_prefix_vec")
    INCLUDE_PREFIX_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PREFIX_VEC_FIELD_NUMBER: _ClassVar[int]
    include_prefix_vec: _containers.RepeatedScalarFieldContainer[str]
    exclude_prefix_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_prefix_vec: _Optional[_Iterable[str]] = ..., exclude_prefix_vec: _Optional[_Iterable[str]] = ...) -> None: ...
