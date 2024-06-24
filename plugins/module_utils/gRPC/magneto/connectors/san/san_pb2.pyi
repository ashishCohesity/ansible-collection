from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import san_pb2 as _san_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Provisioning(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[Provisioning.Type]
        kThin: _ClassVar[Provisioning.Type]
    kNone: Provisioning.Type
    kThin: Provisioning.Type
    def __init__(self) -> None: ...

class Compression(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[Compression.Type]
        kStandard: _ClassVar[Compression.Type]
    kNone: Compression.Type
    kStandard: Compression.Type
    def __init__(self) -> None: ...

class Deduplication(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[Deduplication.Type]
        kStandard: _ClassVar[Deduplication.Type]
    kNone: Deduplication.Type
    kStandard: Deduplication.Type
    def __init__(self) -> None: ...

class VolumeDisk(_message.Message):
    __slots__ = ("source", "storage_pool_id", "provisioning", "compression", "deduplication", "parent_name", "intermediate_snapshot_name", "intermediate_snapshot_id")
    SAN_VOLUME_DISK_FIELD_NUMBER: _ClassVar[int]
    san_volume_disk: _descriptor.FieldDescriptor
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    source: str
    storage_pool_id: str
    provisioning: Provisioning.Type
    compression: Compression.Type
    deduplication: Deduplication.Type
    parent_name: str
    intermediate_snapshot_name: str
    intermediate_snapshot_id: str
    def __init__(self, source: _Optional[str] = ..., storage_pool_id: _Optional[str] = ..., provisioning: _Optional[_Union[Provisioning.Type, str]] = ..., compression: _Optional[_Union[Compression.Type, str]] = ..., deduplication: _Optional[_Union[Deduplication.Type, str]] = ..., parent_name: _Optional[str] = ..., intermediate_snapshot_name: _Optional[str] = ..., intermediate_snapshot_id: _Optional[str] = ...) -> None: ...

class SparseVolumeConfig(_message.Message):
    __slots__ = ("san_volume",)
    SAN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    san_volume: _san_pb2.SanLogicalUnit
    def __init__(self, san_volume: _Optional[_Union[_san_pb2.SanLogicalUnit, _Mapping]] = ...) -> None: ...

class PrimarySnapshotAttribute(_message.Message):
    __slots__ = ("create_timestamp_usecs", "expiry_timestamp_usecs", "allow_deletion")
    CREATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DELETION_FIELD_NUMBER: _ClassVar[int]
    create_timestamp_usecs: int
    expiry_timestamp_usecs: int
    allow_deletion: bool
    def __init__(self, create_timestamp_usecs: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., allow_deletion: bool = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "intermediate_snapshot_name", "status", "error", "san_volume", "sub_tasks_vec", "block_size", "has_base_snapshot_error", "disconnect_volume_error", "delete_volume_snapshot_error", "delete_intermediate_snapshot_error", "changed_areas_persisted", "intermediate_snapshot_id", "availability_group", "primary_snapshot_attribute", "volume_clone_parent_name", "storage_array_snapshot", "storage_array_snapshot_id", "storage_array_snapshot_name")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPermitGranted: _ClassVar[SnapshotInfo.Status]
        kSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kPostSnapshotScriptExecuted: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPermitGranted: SnapshotInfo.Status
    kSnapshotDone: SnapshotInfo.Status
    kPostSnapshotScriptExecuted: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    SAN_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    san_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SAN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    HAS_BASE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_VOLUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_VOLUME_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_INTERMEDIATE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AREAS_PERSISTED_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SNAPSHOT_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CLONE_PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    intermediate_snapshot_name: str
    status: SnapshotInfo.Status
    error: _error_pb2.ErrorProto
    san_volume: _san_pb2.SanLogicalUnit
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    block_size: int
    has_base_snapshot_error: bool
    disconnect_volume_error: _error_pb2.ErrorProto
    delete_volume_snapshot_error: _error_pb2.ErrorProto
    delete_intermediate_snapshot_error: _error_pb2.ErrorProto
    changed_areas_persisted: bool
    intermediate_snapshot_id: str
    availability_group: _san_pb2.AvailabilityGroup
    primary_snapshot_attribute: PrimarySnapshotAttribute
    volume_clone_parent_name: str
    storage_array_snapshot: bool
    storage_array_snapshot_id: str
    storage_array_snapshot_name: str
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., intermediate_snapshot_name: _Optional[str] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., san_volume: _Optional[_Union[_san_pb2.SanLogicalUnit, _Mapping]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., block_size: _Optional[int] = ..., has_base_snapshot_error: bool = ..., disconnect_volume_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_volume_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_intermediate_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., changed_areas_persisted: bool = ..., intermediate_snapshot_id: _Optional[str] = ..., availability_group: _Optional[_Union[_san_pb2.AvailabilityGroup, _Mapping]] = ..., primary_snapshot_attribute: _Optional[_Union[PrimarySnapshotAttribute, _Mapping]] = ..., volume_clone_parent_name: _Optional[str] = ..., storage_array_snapshot: bool = ..., storage_array_snapshot_id: _Optional[str] = ..., storage_array_snapshot_name: _Optional[str] = ...) -> None: ...

class GroupSnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "group_snapshot_name", "group_snapshot_id", "status", "volume_snapshot_vec", "error", "delete_group_snapshot_error", "primary_snapshot_attribute", "delete_cloned_group_error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[GroupSnapshotInfo.Status]
        kBackupFinished: _ClassVar[GroupSnapshotInfo.Status]
        kPermitGranted: _ClassVar[GroupSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[GroupSnapshotInfo.Status]
        kSnapshotDone: _ClassVar[GroupSnapshotInfo.Status]
        kPostSnapshotScriptExecuted: _ClassVar[GroupSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[GroupSnapshotInfo.Status]
        kSetupVolumesSnapshotInfoDone: _ClassVar[GroupSnapshotInfo.Status]
    kStarted: GroupSnapshotInfo.Status
    kBackupFinished: GroupSnapshotInfo.Status
    kPermitGranted: GroupSnapshotInfo.Status
    kPrepareBackupDone: GroupSnapshotInfo.Status
    kSnapshotDone: GroupSnapshotInfo.Status
    kPostSnapshotScriptExecuted: GroupSnapshotInfo.Status
    kProgressMonitorsCreated: GroupSnapshotInfo.Status
    kSetupVolumesSnapshotInfoDone: GroupSnapshotInfo.Status
    class VolumeSnapshot(_message.Message):
        __slots__ = ("volume_snapshot_info", "original_volume_serial")
        VOLUME_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_VOLUME_SERIAL_FIELD_NUMBER: _ClassVar[int]
        volume_snapshot_info: _magneto_pb2.SnapshotInfoProto
        original_volume_serial: str
        def __init__(self, volume_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., original_volume_serial: _Optional[str] = ...) -> None: ...
    SAN_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    san_group_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    GROUP_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_GROUP_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SNAPSHOT_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLONED_GROUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    group_snapshot_name: str
    group_snapshot_id: str
    status: GroupSnapshotInfo.Status
    volume_snapshot_vec: _containers.RepeatedCompositeFieldContainer[GroupSnapshotInfo.VolumeSnapshot]
    error: _error_pb2.ErrorProto
    delete_group_snapshot_error: _error_pb2.ErrorProto
    primary_snapshot_attribute: PrimarySnapshotAttribute
    delete_cloned_group_error: _error_pb2.ErrorProto
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., group_snapshot_name: _Optional[str] = ..., group_snapshot_id: _Optional[str] = ..., status: _Optional[_Union[GroupSnapshotInfo.Status, str]] = ..., volume_snapshot_vec: _Optional[_Iterable[_Union[GroupSnapshotInfo.VolumeSnapshot, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_group_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., primary_snapshot_attribute: _Optional[_Union[PrimarySnapshotAttribute, _Mapping]] = ..., delete_cloned_group_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SANExternalGroupSnapshotInfo(_message.Message):
    __slots__ = ("group_snapshot_type",)
    class GroupSnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPureProtectionGroupSnapshot: _ClassVar[SANExternalGroupSnapshotInfo.GroupSnapshotType]
        kVolumeGroupSnapshot: _ClassVar[SANExternalGroupSnapshotInfo.GroupSnapshotType]
    kPureProtectionGroupSnapshot: SANExternalGroupSnapshotInfo.GroupSnapshotType
    kVolumeGroupSnapshot: SANExternalGroupSnapshotInfo.GroupSnapshotType
    SAN_EXTERNAL_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    san_external_group_snapshot_info: _descriptor.FieldDescriptor
    GROUP_SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    group_snapshot_type: SANExternalGroupSnapshotInfo.GroupSnapshotType
    def __init__(self, group_snapshot_type: _Optional[_Union[SANExternalGroupSnapshotInfo.GroupSnapshotType, str]] = ...) -> None: ...

class SANExternalSnapshotInfo(_message.Message):
    __slots__ = ("san_resource_vec",)
    class SANExternalResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVolume: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
        kVolumeSnapshot: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
        kVolumeClone: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
        kVolumeGroup: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
        kVolumeGroupSnapshot: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
        kVolumeGroupClone: _ClassVar[SANExternalSnapshotInfo.SANExternalResourceType]
    kVolume: SANExternalSnapshotInfo.SANExternalResourceType
    kVolumeSnapshot: SANExternalSnapshotInfo.SANExternalResourceType
    kVolumeClone: SANExternalSnapshotInfo.SANExternalResourceType
    kVolumeGroup: SANExternalSnapshotInfo.SANExternalResourceType
    kVolumeGroupSnapshot: SANExternalSnapshotInfo.SANExternalResourceType
    kVolumeGroupClone: SANExternalSnapshotInfo.SANExternalResourceType
    class SANExternalResource(_message.Message):
        __slots__ = ("id", "name", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        type: SANExternalSnapshotInfo.SANExternalResourceType
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[SANExternalSnapshotInfo.SANExternalResourceType, str]] = ...) -> None: ...
    SAN_EXTERNAL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    san_external_snapshot_info: _descriptor.FieldDescriptor
    SAN_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    san_resource_vec: _containers.RepeatedCompositeFieldContainer[SANExternalSnapshotInfo.SANExternalResource]
    def __init__(self, san_resource_vec: _Optional[_Iterable[_Union[SANExternalSnapshotInfo.SANExternalResource, _Mapping]]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "error", "snapshot_info_proto_vec", "to_recover_san_volume", "recovered_san_volume", "sub_tasks_vec", "total_bytes_to_write_to_source", "disconnect_volume_error", "delete_recovery_volume_error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kCheckSnapshotFinished: _ClassVar[RestoreInfo.Status]
        kCloneFilesFinished: _ClassVar[RestoreInfo.Status]
        kSubTasksCreated: _ClassVar[RestoreInfo.Status]
        kSubTasksFinished: _ClassVar[RestoreInfo.Status]
        kEndRestoreFinished: _ClassVar[RestoreInfo.Status]
        kPermitGranted: _ClassVar[RestoreInfo.Status]
        kCheckRecoveryObjectFinished: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kCheckSnapshotFinished: RestoreInfo.Status
    kCloneFilesFinished: RestoreInfo.Status
    kSubTasksCreated: RestoreInfo.Status
    kSubTasksFinished: RestoreInfo.Status
    kEndRestoreFinished: RestoreInfo.Status
    kPermitGranted: RestoreInfo.Status
    kCheckRecoveryObjectFinished: RestoreInfo.Status
    SAN_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    san_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_SAN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    RECOVERED_SAN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_VOLUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_RECOVERY_VOLUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    error: _error_pb2.ErrorProto
    snapshot_info_proto_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.SnapshotInfoProto]
    to_recover_san_volume: _san_pb2.SanLogicalUnit
    recovered_san_volume: _san_pb2.SanLogicalUnit
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    total_bytes_to_write_to_source: int
    disconnect_volume_error: _error_pb2.ErrorProto
    delete_recovery_volume_error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_info_proto_vec: _Optional[_Iterable[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]]] = ..., to_recover_san_volume: _Optional[_Union[_san_pb2.SanLogicalUnit, _Mapping]] = ..., recovered_san_volume: _Optional[_Union[_san_pb2.SanLogicalUnit, _Mapping]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., disconnect_volume_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_recovery_volume_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GroupRestoreInfo(_message.Message):
    __slots__ = ("status", "error", "volume_restore_info_vec", "recovered_san_group", "delete_recovery_san_group_error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[GroupRestoreInfo.Status]
        kCheckRecoveryGroupFinished: _ClassVar[GroupRestoreInfo.Status]
        kRecoveryGroupCreated: _ClassVar[GroupRestoreInfo.Status]
        kCloneFilesFinished: _ClassVar[GroupRestoreInfo.Status]
        kPermitGranted: _ClassVar[GroupRestoreInfo.Status]
        kVolumesRestored: _ClassVar[GroupRestoreInfo.Status]
        kVolumesConfigured: _ClassVar[GroupRestoreInfo.Status]
        kEndRestoreFinished: _ClassVar[GroupRestoreInfo.Status]
    kStarted: GroupRestoreInfo.Status
    kCheckRecoveryGroupFinished: GroupRestoreInfo.Status
    kRecoveryGroupCreated: GroupRestoreInfo.Status
    kCloneFilesFinished: GroupRestoreInfo.Status
    kPermitGranted: GroupRestoreInfo.Status
    kVolumesRestored: GroupRestoreInfo.Status
    kVolumesConfigured: GroupRestoreInfo.Status
    kEndRestoreFinished: GroupRestoreInfo.Status
    class VolumeRestoreInfo(_message.Message):
        __slots__ = ("volume_restore_info",)
        VOLUME_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
        volume_restore_info: _magneto_pb2.RestoreInfoProto
        def __init__(self, volume_restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ...) -> None: ...
    GROUP_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    group_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RECOVERED_SAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_RECOVERY_SAN_GROUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: GroupRestoreInfo.Status
    error: _error_pb2.ErrorProto
    volume_restore_info_vec: _containers.RepeatedCompositeFieldContainer[GroupRestoreInfo.VolumeRestoreInfo]
    recovered_san_group: _san_pb2.SanGroupUnit
    delete_recovery_san_group_error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[GroupRestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_restore_info_vec: _Optional[_Iterable[_Union[GroupRestoreInfo.VolumeRestoreInfo, _Mapping]]] = ..., recovered_san_group: _Optional[_Union[_san_pb2.SanGroupUnit, _Mapping]] = ..., delete_recovery_san_group_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("disk_delta_info",)
    SAN_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    san_snapshot_scribe_info: _descriptor.FieldDescriptor
    DISK_DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    disk_delta_info: _cbt_delta_pb2.CBTDeltaInfo
    def __init__(self, disk_delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ...) -> None: ...
