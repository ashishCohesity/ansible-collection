from magneto.api import object_protection_pb2 as _object_protection_pb2
from magneto.master.base import master_pb2 as _master_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalBackupRunArchiveInfo(_message.Message):
    __slots__ = ("spec_info", "spec_metadata", "backup_run_state")
    SPEC_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEC_METADATA_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    spec_info: _object_protection_pb2.ObjectSpecInfo
    spec_metadata: ObjectSpecMetadata
    backup_run_state: _master_pb2.BackupJobRunStateProto
    def __init__(self, spec_info: _Optional[_Union[_object_protection_pb2.ObjectSpecInfo, _Mapping]] = ..., spec_metadata: _Optional[_Union[ObjectSpecMetadata, _Mapping]] = ..., backup_run_state: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ...) -> None: ...

class ObjectSpecMetadata(_message.Message):
    __slots__ = ("entity", "parent_source", "eh_parent_source", "last_pause_modification_time_usecs", "required_feature_vec", "entity_permission_info", "auto_protect_owner_entity")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EH_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSE_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
    AUTO_PROTECT_OWNER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    parent_source: _entity_pb2.EntityProto
    eh_parent_source: _entity_pb2.EntityProto
    last_pause_modification_time_usecs: int
    required_feature_vec: _containers.RepeatedScalarFieldContainer[str]
    entity_permission_info: _permissions_pb2.EntityPermissionInfo
    auto_protect_owner_entity: _entity_pb2.EntityProto
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., eh_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., last_pause_modification_time_usecs: _Optional[int] = ..., required_feature_vec: _Optional[_Iterable[str]] = ..., entity_permission_info: _Optional[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]] = ..., auto_protect_owner_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
