from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Object(_message.Message):
    __slots__ = ("account_id", "tenant_id", "type", "id", "name", "snapshots", "base_snapshot_handle")
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMailbox: _ClassVar[Object.ObjectType]
        kOneDrive: _ClassVar[Object.ObjectType]
        kVM: _ClassVar[Object.ObjectType]
        kCohesityView: _ClassVar[Object.ObjectType]
    kMailbox: Object.ObjectType
    kOneDrive: Object.ObjectType
    kVM: Object.ObjectType
    kCohesityView: Object.ObjectType
    class SnapshotInfo(_message.Message):
        __slots__ = ("snapshot_handle", "tags")
        SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        snapshot_handle: SnapshotHandle
        tags: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, snapshot_handle: _Optional[_Union[SnapshotHandle, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    type: Object.ObjectType
    id: bytes
    name: str
    snapshots: _containers.RepeatedCompositeFieldContainer[Object.SnapshotInfo]
    base_snapshot_handle: SnapshotHandle
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., type: _Optional[_Union[Object.ObjectType, str]] = ..., id: _Optional[bytes] = ..., name: _Optional[str] = ..., snapshots: _Optional[_Iterable[_Union[Object.SnapshotInfo, _Mapping]]] = ..., base_snapshot_handle: _Optional[_Union[SnapshotHandle, _Mapping]] = ...) -> None: ...

class SnapshotHandle(_message.Message):
    __slots__ = ("magneto_job_id", "run_start_time_usecs")
    MAGNETO_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    magneto_job_id: int
    run_start_time_usecs: int
    def __init__(self, magneto_job_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...

class SubObjectHandle(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    name: str
    def __init__(self, id: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class DocumentType(_message.Message):
    __slots__ = ("type", "name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[DocumentType.Type]
        kTextFile: _ClassVar[DocumentType.Type]
        kPDF: _ClassVar[DocumentType.Type]
        kDoc: _ClassVar[DocumentType.Type]
        kDocx: _ClassVar[DocumentType.Type]
        kPpt: _ClassVar[DocumentType.Type]
        kPptx: _ClassVar[DocumentType.Type]
        kXls: _ClassVar[DocumentType.Type]
        kXlsx: _ClassVar[DocumentType.Type]
        kRtf: _ClassVar[DocumentType.Type]
        kOdf: _ClassVar[DocumentType.Type]
        kO365EmailBlob: _ClassVar[DocumentType.Type]
    kUnknown: DocumentType.Type
    kTextFile: DocumentType.Type
    kPDF: DocumentType.Type
    kDoc: DocumentType.Type
    kDocx: DocumentType.Type
    kPpt: DocumentType.Type
    kPptx: DocumentType.Type
    kXls: DocumentType.Type
    kXlsx: DocumentType.Type
    kRtf: DocumentType.Type
    kOdf: DocumentType.Type
    kO365EmailBlob: DocumentType.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type: DocumentType.Type
    name: str
    def __init__(self, type: _Optional[_Union[DocumentType.Type, str]] = ..., name: _Optional[str] = ...) -> None: ...

class DocumentLocator(_message.Message):
    __slots__ = ("object_id", "object_type", "snapshot_handle", "sub_object_handle", "doc_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SUB_OBJECT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: bytes
    object_type: Object.ObjectType
    snapshot_handle: SnapshotHandle
    sub_object_handle: SubObjectHandle
    doc_id: bytes
    def __init__(self, object_id: _Optional[bytes] = ..., object_type: _Optional[_Union[Object.ObjectType, str]] = ..., snapshot_handle: _Optional[_Union[SnapshotHandle, _Mapping]] = ..., sub_object_handle: _Optional[_Union[SubObjectHandle, _Mapping]] = ..., doc_id: _Optional[bytes] = ...) -> None: ...
