from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DocumentStats(_message.Message):
    __slots__ = ("doc_stats_vec",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[DocumentStats.Type]
        kNotUpdated: _ClassVar[DocumentStats.Type]
        kNewDocument: _ClassVar[DocumentStats.Type]
        kUpdateDocument: _ClassVar[DocumentStats.Type]
        kDeleteDocument: _ClassVar[DocumentStats.Type]
    kUnused: DocumentStats.Type
    kNotUpdated: DocumentStats.Type
    kNewDocument: DocumentStats.Type
    kUpdateDocument: DocumentStats.Type
    kDeleteDocument: DocumentStats.Type
    class KeyValuePair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: DocumentStats.Type
        value: int
        def __init__(self, key: _Optional[_Union[DocumentStats.Type, str]] = ..., value: _Optional[int] = ...) -> None: ...
    DOC_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    doc_stats_vec: _containers.RepeatedCompositeFieldContainer[DocumentStats.KeyValuePair]
    def __init__(self, doc_stats_vec: _Optional[_Iterable[_Union[DocumentStats.KeyValuePair, _Mapping]]] = ...) -> None: ...
