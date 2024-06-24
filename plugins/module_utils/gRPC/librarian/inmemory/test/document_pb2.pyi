from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ("name", "size", "snapshot_info", "not_indexed", "doc_terms")
    class SnapshotInfo(_message.Message):
        __slots__ = ("type", "snapshot_time_secs")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kVMware: _ClassVar[Document.SnapshotInfo.Type]
            kHyperV: _ClassVar[Document.SnapshotInfo.Type]
        kVMware: Document.SnapshotInfo.Type
        kHyperV: Document.SnapshotInfo.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        type: Document.SnapshotInfo.Type
        snapshot_time_secs: int
        def __init__(self, type: _Optional[_Union[Document.SnapshotInfo.Type, str]] = ..., snapshot_time_secs: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    NOT_INDEXED_FIELD_NUMBER: _ClassVar[int]
    DOC_TERMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    snapshot_info: Document.SnapshotInfo
    not_indexed: int
    doc_terms: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., snapshot_info: _Optional[_Union[Document.SnapshotInfo, _Mapping]] = ..., not_indexed: _Optional[int] = ..., doc_terms: _Optional[_Iterable[str]] = ...) -> None: ...
