from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NasPathProto(_message.Message):
    __slots__ = ("protocol", "hostname", "path", "additional_hostname_vec")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
    protocol: _enums_pb2.NasProtocol.Type
    hostname: str
    path: str
    additional_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., hostname: _Optional[str] = ..., path: _Optional[str] = ..., additional_hostname_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class NasPathSnapshotProto(_message.Message):
    __slots__ = ("nas_path", "snapshot", "clone", "parent_source_id")
    NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CLONE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    nas_path: NasPathProto
    snapshot: _entity_pb2.EntityProto
    clone: _entity_pb2.EntityProto
    parent_source_id: int
    def __init__(self, nas_path: _Optional[_Union[NasPathProto, _Mapping]] = ..., snapshot: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., clone: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_id: _Optional[int] = ...) -> None: ...

class NasExternalSnapshotInfo(_message.Message):
    __slots__ = ("snapshot", "workflow")
    class Workflow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[NasExternalSnapshotInfo.Workflow]
        kVMwareLeverageStorageSnapshot: _ClassVar[NasExternalSnapshotInfo.Workflow]
    kUnknown: NasExternalSnapshotInfo.Workflow
    kVMwareLeverageStorageSnapshot: NasExternalSnapshotInfo.Workflow
    NAS_EXTERNAL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    nas_external_snapshot_info: _descriptor.FieldDescriptor
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    snapshot: NasPathSnapshotProto
    workflow: NasExternalSnapshotInfo.Workflow
    def __init__(self, snapshot: _Optional[_Union[NasPathSnapshotProto, _Mapping]] = ..., workflow: _Optional[_Union[NasExternalSnapshotInfo.Workflow, str]] = ...) -> None: ...
