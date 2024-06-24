from alerts.base import alert_pb2 as _alert_pb2
from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.api.common import additional_entity_info_pb2 as _additional_entity_info_pb2
from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import enums_pb2 as _enums_pb2
from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from magneto.api.objects import vmware_pb2 as _vmware_pb2
from magneto.api import worm_pb2 as _worm_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from util.message_catalog import message_catalog_pb2 as _message_catalog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("error_type", "error_detail", "detailed_error_msg")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DETAILED_ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_type: _enum_wrappers_pb2.MagnetoErrorTypeProto
    error_detail: str
    detailed_error_msg: _message_catalog_pb2.MessageProto
    def __init__(self, error_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoErrorTypeProto, _Mapping]] = ..., error_detail: _Optional[str] = ..., detailed_error_msg: _Optional[_Union[_message_catalog_pb2.MessageProto, _Mapping]] = ...) -> None: ...

class ObjectDetailedInfoProto(_message.Message):
    __slots__ = ("hash_string", "logical_size_in_bytes")
    HASH_STRING_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    hash_string: str
    logical_size_in_bytes: int
    def __init__(self, hash_string: _Optional[str] = ..., logical_size_in_bytes: _Optional[int] = ...) -> None: ...

class ObjectActionKey(_message.Message):
    __slots__ = ("environment",)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: _enum_wrappers_pb2.EnvironmentProto
    def __init__(self, environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ...) -> None: ...

class ObjectProto(_message.Message):
    __slots__ = ("id", "object_string_id", "name", "environment", "parent_id", "parent_string_id", "permission_info", "detailed_info", "vmware_object_info", "additional_entity_info_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DETAILED_INFO_FIELD_NUMBER: _ClassVar[int]
    VMWARE_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    object_string_id: str
    name: str
    environment: _enum_wrappers_pb2.EnvironmentProto
    parent_id: int
    parent_string_id: str
    permission_info: _permissions_external_pb2.EntityPermissionInfoProto
    detailed_info: ObjectDetailedInfoProto
    vmware_object_info: _vmware_pb2.Object
    additional_entity_info_vec: _containers.RepeatedCompositeFieldContainer[_additional_entity_info_pb2.AdditionalEntityInfo]
    def __init__(self, id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., name: _Optional[str] = ..., environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., parent_id: _Optional[int] = ..., parent_string_id: _Optional[str] = ..., permission_info: _Optional[_Union[_permissions_external_pb2.EntityPermissionInfoProto, _Mapping]] = ..., detailed_info: _Optional[_Union[ObjectDetailedInfoProto, _Mapping]] = ..., vmware_object_info: _Optional[_Union[_vmware_pb2.Object, _Mapping]] = ..., additional_entity_info_vec: _Optional[_Iterable[_Union[_additional_entity_info_pb2.AdditionalEntityInfo, _Mapping]]] = ...) -> None: ...

class ArchivalTargetProto(_message.Message):
    __slots__ = ("vault_id", "archival_type", "name")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    archival_type: _enums_pb2.ArchivalTargetType.Type
    name: str
    def __init__(self, vault_id: _Optional[int] = ..., archival_type: _Optional[_Union[_enums_pb2.ArchivalTargetType.Type, str]] = ..., name: _Optional[str] = ...) -> None: ...

class AwsParams(_message.Message):
    __slots__ = ("region", "vpc", "subnet")
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    region: ObjectProto
    vpc: ObjectProto
    subnet: ObjectProto
    def __init__(self, region: _Optional[_Union[ObjectProto, _Mapping]] = ..., vpc: _Optional[_Union[ObjectProto, _Mapping]] = ..., subnet: _Optional[_Union[ObjectProto, _Mapping]] = ...) -> None: ...

class AzureParams(_message.Message):
    __slots__ = ("network_resource_group", "resource_group", "storage_account", "storage_container", "storage_resource_group", "temp_vm_resource_group", "temp_vm_storage_account", "temp_vm_storage_container", "temp_vm_subnet", "temp_vm_virtual_network")
    NETWORK_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_SUBNET_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_VIRTUAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    network_resource_group: ObjectProto
    resource_group: ObjectProto
    storage_account: ObjectProto
    storage_container: ObjectProto
    storage_resource_group: ObjectProto
    temp_vm_resource_group: ObjectProto
    temp_vm_storage_account: ObjectProto
    temp_vm_storage_container: ObjectProto
    temp_vm_subnet: ObjectProto
    temp_vm_virtual_network: ObjectProto
    def __init__(self, network_resource_group: _Optional[_Union[ObjectProto, _Mapping]] = ..., resource_group: _Optional[_Union[ObjectProto, _Mapping]] = ..., storage_account: _Optional[_Union[ObjectProto, _Mapping]] = ..., storage_container: _Optional[_Union[ObjectProto, _Mapping]] = ..., storage_resource_group: _Optional[_Union[ObjectProto, _Mapping]] = ..., temp_vm_resource_group: _Optional[_Union[ObjectProto, _Mapping]] = ..., temp_vm_storage_account: _Optional[_Union[ObjectProto, _Mapping]] = ..., temp_vm_storage_container: _Optional[_Union[ObjectProto, _Mapping]] = ..., temp_vm_subnet: _Optional[_Union[ObjectProto, _Mapping]] = ..., temp_vm_virtual_network: _Optional[_Union[ObjectProto, _Mapping]] = ...) -> None: ...

class CloudSpinTargetProto(_message.Message):
    __slots__ = ("type", "target_entity")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAzure: _ClassVar[CloudSpinTargetProto.Type]
        kAWS: _ClassVar[CloudSpinTargetProto.Type]
        kGCP: _ClassVar[CloudSpinTargetProto.Type]
    kAzure: CloudSpinTargetProto.Type
    kAWS: CloudSpinTargetProto.Type
    kGCP: CloudSpinTargetProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    type: CloudSpinTargetProto.Type
    target_entity: ObjectProto
    def __init__(self, type: _Optional[_Union[CloudSpinTargetProto.Type, str]] = ..., target_entity: _Optional[_Union[ObjectProto, _Mapping]] = ...) -> None: ...

class OnPremTargetProto(_message.Message):
    __slots__ = ("environment", "target_entity")
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    environment: _enum_wrappers_pb2.EnvironmentProto
    target_entity: ObjectProto
    def __init__(self, environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., target_entity: _Optional[_Union[ObjectProto, _Mapping]] = ...) -> None: ...

class SnapshotTargetProto(_message.Message):
    __slots__ = ("type", "replication_target", "archival_target", "cloud_deploy_target", "onprem_deploy_target")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLocal: _ClassVar[SnapshotTargetProto.Type]
        kRemote: _ClassVar[SnapshotTargetProto.Type]
        kArchival: _ClassVar[SnapshotTargetProto.Type]
        kCloudDeploy: _ClassVar[SnapshotTargetProto.Type]
        kCloudReplication: _ClassVar[SnapshotTargetProto.Type]
        kOnPremDeploy: _ClassVar[SnapshotTargetProto.Type]
    kLocal: SnapshotTargetProto.Type
    kRemote: SnapshotTargetProto.Type
    kArchival: SnapshotTargetProto.Type
    kCloudDeploy: SnapshotTargetProto.Type
    kCloudReplication: SnapshotTargetProto.Type
    kOnPremDeploy: SnapshotTargetProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_TARGET_FIELD_NUMBER: _ClassVar[int]
    ONPREM_DEPLOY_TARGET_FIELD_NUMBER: _ClassVar[int]
    type: SnapshotTargetProto.Type
    replication_target: ClusterIdentifierProto
    archival_target: ArchivalTargetProto
    cloud_deploy_target: CloudSpinTargetProto
    onprem_deploy_target: OnPremTargetProto
    def __init__(self, type: _Optional[_Union[SnapshotTargetProto.Type, str]] = ..., replication_target: _Optional[_Union[ClusterIdentifierProto, _Mapping]] = ..., archival_target: _Optional[_Union[ArchivalTargetProto, _Mapping]] = ..., cloud_deploy_target: _Optional[_Union[CloudSpinTargetProto, _Mapping]] = ..., onprem_deploy_target: _Optional[_Union[OnPremTargetProto, _Mapping]] = ...) -> None: ...

class ClusterIdentifierProto(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "cluster_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    cluster_name: str
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class TimeInterval(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class SnapshotExpiryInfoProto(_message.Message):
    __slots__ = ("expiry_time_secs", "is_expired", "is_deleted", "is_manually_marked_for_deletion", "on_legal_hold", "datalock_info")
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_MANUALLY_MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    ON_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    DATALOCK_INFO_FIELD_NUMBER: _ClassVar[int]
    expiry_time_secs: int
    is_expired: bool
    is_deleted: bool
    is_manually_marked_for_deletion: bool
    on_legal_hold: bool
    datalock_info: _worm_pb2.DataLockConstraintsProto
    def __init__(self, expiry_time_secs: _Optional[int] = ..., is_expired: bool = ..., is_deleted: bool = ..., is_manually_marked_for_deletion: bool = ..., on_legal_hold: bool = ..., datalock_info: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ...) -> None: ...

class EntitySizeInfo(_message.Message):
    __slots__ = ("source_provisioned_logical_size_bytes", "source_data_size_bytes")
    SOURCE_PROVISIONED_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    source_provisioned_logical_size_bytes: int
    source_data_size_bytes: int
    def __init__(self, source_provisioned_logical_size_bytes: _Optional[int] = ..., source_data_size_bytes: _Optional[int] = ...) -> None: ...

class EntityBackupStats(_message.Message):
    __slots__ = ("entity_size_info", "source_protected_logical_size_bytes", "source_protected_data_size_bytes", "source_protected_data_size_bytes_computation_method", "bytes_read", "bytes_written")
    class ComputationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[EntityBackupStats.ComputationMethod]
        kAgentBased: _ClassVar[EntityBackupStats.ComputationMethod]
        kVirtualizationGuestUtils: _ClassVar[EntityBackupStats.ComputationMethod]
        kApollo: _ClassVar[EntityBackupStats.ComputationMethod]
    kUnknown: EntityBackupStats.ComputationMethod
    kAgentBased: EntityBackupStats.ComputationMethod
    kVirtualizationGuestUtils: EntityBackupStats.ComputationMethod
    kApollo: EntityBackupStats.ComputationMethod
    ENTITY_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTECTED_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTECTED_DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTECTED_DATA_SIZE_BYTES_COMPUTATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    entity_size_info: EntitySizeInfo
    source_protected_logical_size_bytes: int
    source_protected_data_size_bytes: int
    source_protected_data_size_bytes_computation_method: EntityBackupStats.ComputationMethod
    bytes_read: int
    bytes_written: int
    def __init__(self, entity_size_info: _Optional[_Union[EntitySizeInfo, _Mapping]] = ..., source_protected_logical_size_bytes: _Optional[int] = ..., source_protected_data_size_bytes: _Optional[int] = ..., source_protected_data_size_bytes_computation_method: _Optional[_Union[EntityBackupStats.ComputationMethod, str]] = ..., bytes_read: _Optional[int] = ..., bytes_written: _Optional[int] = ...) -> None: ...

class SnapshotStats(_message.Message):
    __slots__ = ("logical_size_bytes", "bytes_read", "bytes_written", "front_end_size_info")
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    logical_size_bytes: int
    bytes_read: int
    bytes_written: int
    front_end_size_info: _stats_pb2.SizeInfo
    def __init__(self, logical_size_bytes: _Optional[int] = ..., bytes_read: _Optional[int] = ..., bytes_written: _Optional[int] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ...) -> None: ...

class TaskBaseProto(_message.Message):
    __slots__ = ("status", "start_time_usecs", "end_time_usecs", "is_full_copy", "error", "warning_messages", "warning_proto_vec", "progress_monitor_path")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_COPY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNING_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    status: _enum_wrappers_pb2.MagnetoPublicStatus
    start_time_usecs: int
    end_time_usecs: int
    is_full_copy: bool
    error: ErrorProto
    warning_messages: _containers.RepeatedScalarFieldContainer[str]
    warning_proto_vec: _containers.RepeatedCompositeFieldContainer[ErrorProto]
    progress_monitor_path: str
    def __init__(self, status: _Optional[_Union[_enum_wrappers_pb2.MagnetoPublicStatus, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., is_full_copy: bool = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ..., warning_messages: _Optional[_Iterable[str]] = ..., warning_proto_vec: _Optional[_Iterable[_Union[ErrorProto, _Mapping]]] = ..., progress_monitor_path: _Optional[str] = ...) -> None: ...

class LocalBackupRunInfo(_message.Message):
    __slots__ = ("base", "snapshot_id", "is_sla_violated", "run_type", "successful_objects_count", "failed_objects_count", "cancelled_objects_count", "skipped_objects_count", "local_snapshot_stats", "indexing_task_id", "snapshot_expiry_info", "run_label")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SNAPSHOT_STATS_FIELD_NUMBER: _ClassVar[int]
    INDEXING_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_INFO_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    base: TaskBaseProto
    snapshot_id: str
    is_sla_violated: bool
    run_type: _enum_wrappers_pb2.MagnetoBackupType
    successful_objects_count: int
    failed_objects_count: int
    cancelled_objects_count: int
    skipped_objects_count: int
    local_snapshot_stats: SnapshotStats
    indexing_task_id: int
    snapshot_expiry_info: SnapshotExpiryInfoProto
    run_label: str
    def __init__(self, base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., snapshot_id: _Optional[str] = ..., is_sla_violated: bool = ..., run_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., successful_objects_count: _Optional[int] = ..., failed_objects_count: _Optional[int] = ..., cancelled_objects_count: _Optional[int] = ..., skipped_objects_count: _Optional[int] = ..., local_snapshot_stats: _Optional[_Union[SnapshotStats, _Mapping]] = ..., indexing_task_id: _Optional[int] = ..., snapshot_expiry_info: _Optional[_Union[SnapshotExpiryInfoProto, _Mapping]] = ..., run_label: _Optional[str] = ...) -> None: ...

class ReplicationInfoProto(_message.Message):
    __slots__ = ("base", "task_uid", "target_cluster_info", "percentage_completed", "stats", "snapshot_expiry_info")
    class ReplicationStats(_message.Message):
        __slots__ = ("logical_size_bytes", "logical_bytes_transferred", "physical_bytes_transferred")
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        logical_size_bytes: int
        logical_bytes_transferred: int
        physical_bytes_transferred: int
        def __init__(self, logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_INFO_FIELD_NUMBER: _ClassVar[int]
    base: TaskBaseProto
    task_uid: _universal_id_pb2.UniversalIdProto
    target_cluster_info: ClusterIdentifierProto
    percentage_completed: int
    stats: ReplicationInfoProto.ReplicationStats
    snapshot_expiry_info: SnapshotExpiryInfoProto
    def __init__(self, base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., target_cluster_info: _Optional[_Union[ClusterIdentifierProto, _Mapping]] = ..., percentage_completed: _Optional[int] = ..., stats: _Optional[_Union[ReplicationInfoProto.ReplicationStats, _Mapping]] = ..., snapshot_expiry_info: _Optional[_Union[SnapshotExpiryInfoProto, _Mapping]] = ...) -> None: ...

class ArchivalInfoProto(_message.Message):
    __slots__ = ("base", "task_uid", "target", "stats", "is_incremental_archive", "snapshot_expiry_info", "is_cloud_domain_archive", "is_cad_archive")
    class ArchivalStats(_message.Message):
        __slots__ = ("logical_size_bytes", "logical_bytes_transferred", "physical_bytes_transferred", "avg_logical_transfer_rate_bps", "bytes_read", "total_file_count", "total_changed_file_count", "file_walk_done", "front_end_size_info")
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
        BYTES_READ_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CHANGED_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FILE_WALK_DONE_FIELD_NUMBER: _ClassVar[int]
        FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
        logical_size_bytes: int
        logical_bytes_transferred: int
        physical_bytes_transferred: int
        avg_logical_transfer_rate_bps: int
        bytes_read: int
        total_file_count: int
        total_changed_file_count: int
        file_walk_done: bool
        front_end_size_info: _stats_pb2.SizeInfo
        def __init__(self, logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., bytes_read: _Optional[int] = ..., total_file_count: _Optional[int] = ..., total_changed_file_count: _Optional[int] = ..., file_walk_done: bool = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_DOMAIN_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    base: TaskBaseProto
    task_uid: _universal_id_pb2.UniversalIdProto
    target: ArchivalTargetProto
    stats: ArchivalInfoProto.ArchivalStats
    is_incremental_archive: bool
    snapshot_expiry_info: SnapshotExpiryInfoProto
    is_cloud_domain_archive: bool
    is_cad_archive: bool
    def __init__(self, base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., target: _Optional[_Union[ArchivalTargetProto, _Mapping]] = ..., stats: _Optional[_Union[ArchivalInfoProto.ArchivalStats, _Mapping]] = ..., is_incremental_archive: bool = ..., snapshot_expiry_info: _Optional[_Union[SnapshotExpiryInfoProto, _Mapping]] = ..., is_cloud_domain_archive: bool = ..., is_cad_archive: bool = ...) -> None: ...

class CloudSpinInfoProto(_message.Message):
    __slots__ = ("base", "target", "stats")
    class CloudSpinStats(_message.Message):
        __slots__ = ("physical_bytes_transferred",)
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        physical_bytes_transferred: int
        def __init__(self, physical_bytes_transferred: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    base: TaskBaseProto
    target: CloudSpinTargetProto
    stats: CloudSpinInfoProto.CloudSpinStats
    def __init__(self, base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., target: _Optional[_Union[CloudSpinTargetProto, _Mapping]] = ..., stats: _Optional[_Union[CloudSpinInfoProto.CloudSpinStats, _Mapping]] = ...) -> None: ...

class OnPremDeployInfoProto(_message.Message):
    __slots__ = ("base", "target", "restored_entity")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    RESTORED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    base: TaskBaseProto
    target: OnPremTargetProto
    restored_entity: ObjectProto
    def __init__(self, base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., target: _Optional[_Union[OnPremTargetProto, _Mapping]] = ..., restored_entity: _Optional[_Union[ObjectProto, _Mapping]] = ...) -> None: ...

class EntitySnapshotInfoProto(_message.Message):
    __slots__ = ("uid", "label", "created_timestamp_usecs", "updated_timestamp_usecs", "is_manual_snapshot")
    UID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    uid: str
    label: str
    created_timestamp_usecs: int
    updated_timestamp_usecs: int
    is_manual_snapshot: bool
    def __init__(self, uid: _Optional[str] = ..., label: _Optional[str] = ..., created_timestamp_usecs: _Optional[int] = ..., updated_timestamp_usecs: _Optional[int] = ..., is_manual_snapshot: bool = ...) -> None: ...

class ArgumentBase(_message.Message):
    __slots__ = ("is_forwarded", "max_count", "pagination_cookie", "user_info", "api_request_attr", "idempotence_cookie")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    max_count: int
    pagination_cookie: bytes
    user_info: _permissions_external_pb2.UserInformationProto
    api_request_attr: GrpcAPIRequestAttr
    idempotence_cookie: str
    def __init__(self, is_forwarded: bool = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[bytes] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ..., api_request_attr: _Optional[_Union[GrpcAPIRequestAttr, _Mapping]] = ..., idempotence_cookie: _Optional[str] = ...) -> None: ...

class ResultBase(_message.Message):
    __slots__ = ("error", "pagination_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    pagination_cookie: bytes
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., pagination_cookie: _Optional[bytes] = ...) -> None: ...

class RemoteScriptProto(_message.Message):
    __slots__ = ("script_path", "script_params", "timeout_secs", "continue_task_on_error", "is_active", "remote_host_params")
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_TASK_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HOST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    script_path: str
    script_params: str
    timeout_secs: int
    continue_task_on_error: bool
    is_active: bool
    remote_host_params: RemoteHostConnectorProto
    def __init__(self, script_path: _Optional[str] = ..., script_params: _Optional[str] = ..., timeout_secs: _Optional[int] = ..., continue_task_on_error: bool = ..., is_active: bool = ..., remote_host_params: _Optional[_Union[RemoteHostConnectorProto, _Mapping]] = ...) -> None: ...

class RemoteHostConnectorProto(_message.Message):
    __slots__ = ("host_type", "host_address", "credentials")
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host_type: _enum_wrappers_pb2.HostEnvProto
    host_address: str
    credentials: CredentialsProto
    def __init__(self, host_type: _Optional[_Union[_enum_wrappers_pb2.HostEnvProto, _Mapping]] = ..., host_address: _Optional[str] = ..., credentials: _Optional[_Union[CredentialsProto, _Mapping]] = ...) -> None: ...

class PrePostScriptsProto(_message.Message):
    __slots__ = ("pre_script", "post_snapshot_script", "post_backup_script")
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SNAPSHOT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    pre_script: RemoteScriptProto
    post_snapshot_script: RemoteScriptProto
    post_backup_script: RemoteScriptProto
    def __init__(self, pre_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., post_snapshot_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., post_backup_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ...) -> None: ...

class CredentialsProto(_message.Message):
    __slots__ = ("username", "password", "encrypted_password", "token")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: bytes
    encrypted_password: bytes
    token: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[bytes] = ..., encrypted_password: _Optional[bytes] = ..., token: _Optional[str] = ...) -> None: ...

class Time(_message.Message):
    __slots__ = ("hour", "minute")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...

class DiskInfoProto(_message.Message):
    __slots__ = ("controller_type", "unit_number", "bus_number")
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    controller_type: str
    unit_number: int
    bus_number: int
    def __init__(self, controller_type: _Optional[str] = ..., unit_number: _Optional[int] = ..., bus_number: _Optional[int] = ...) -> None: ...

class BackupAlertingPolicyProto(_message.Message):
    __slots__ = ("policy_vec", "delivery_target_vec")
    class Policy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFailure: _ClassVar[BackupAlertingPolicyProto.Policy]
        kSlaViolation: _ClassVar[BackupAlertingPolicyProto.Policy]
        kSuccess: _ClassVar[BackupAlertingPolicyProto.Policy]
    kFailure: BackupAlertingPolicyProto.Policy
    kSlaViolation: BackupAlertingPolicyProto.Policy
    kSuccess: BackupAlertingPolicyProto.Policy
    POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    policy_vec: _containers.RepeatedScalarFieldContainer[BackupAlertingPolicyProto.Policy]
    delivery_target_vec: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DeliveryRuleProto.DeliveryTarget]
    def __init__(self, policy_vec: _Optional[_Iterable[_Union[BackupAlertingPolicyProto.Policy, str]]] = ..., delivery_target_vec: _Optional[_Iterable[_Union[_alert_pb2.DeliveryRuleProto.DeliveryTarget, _Mapping]]] = ...) -> None: ...

class ObjectBackupActionParams(_message.Message):
    __slots__ = ("protect_now_params", "unprotect_params")
    class ProtectNowParams(_message.Message):
        __slots__ = ("perform_local_snapshot_only", "backup_type", "run_label")
        PERFORM_LOCAL_SNAPSHOT_ONLY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
        perform_local_snapshot_only: bool
        backup_type: _enum_wrappers_pb2.MagnetoBackupType
        run_label: str
        def __init__(self, perform_local_snapshot_only: bool = ..., backup_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., run_label: _Optional[str] = ...) -> None: ...
    class UnProtectParams(_message.Message):
        __slots__ = ("should_delete_all_snapshots", "force_unprotect")
        SHOULD_DELETE_ALL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        FORCE_UNPROTECT_FIELD_NUMBER: _ClassVar[int]
        should_delete_all_snapshots: bool
        force_unprotect: bool
        def __init__(self, should_delete_all_snapshots: bool = ..., force_unprotect: bool = ...) -> None: ...
    PROTECT_NOW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UNPROTECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    protect_now_params: ObjectBackupActionParams.ProtectNowParams
    unprotect_params: ObjectBackupActionParams.UnProtectParams
    def __init__(self, protect_now_params: _Optional[_Union[ObjectBackupActionParams.ProtectNowParams, _Mapping]] = ..., unprotect_params: _Optional[_Union[ObjectBackupActionParams.UnProtectParams, _Mapping]] = ...) -> None: ...

class GrpcAPIRequestAttr(_message.Message):
    __slots__ = ("type", "timeout_secs")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUIUser: _ClassVar[GrpcAPIRequestAttr.Type]
        kUIAuto: _ClassVar[GrpcAPIRequestAttr.Type]
        kUserReport: _ClassVar[GrpcAPIRequestAttr.Type]
        kDataCollection: _ClassVar[GrpcAPIRequestAttr.Type]
        kMagnetoInternal: _ClassVar[GrpcAPIRequestAttr.Type]
        kHelios: _ClassVar[GrpcAPIRequestAttr.Type]
    kUIUser: GrpcAPIRequestAttr.Type
    kUIAuto: GrpcAPIRequestAttr.Type
    kUserReport: GrpcAPIRequestAttr.Type
    kDataCollection: GrpcAPIRequestAttr.Type
    kMagnetoInternal: GrpcAPIRequestAttr.Type
    kHelios: GrpcAPIRequestAttr.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    type: GrpcAPIRequestAttr.Type
    timeout_secs: int
    def __init__(self, type: _Optional[_Union[GrpcAPIRequestAttr.Type, str]] = ..., timeout_secs: _Optional[int] = ...) -> None: ...

class ProtectionGroupSpec(_message.Message):
    __slots__ = ("uid", "name")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    name: str
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class RunAndTaskIds(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "task_ids")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., task_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ProtectionRunSelectorProto(_message.Message):
    __slots__ = ("include_public_statuses", "start_time_interval", "exclude_runs_filter")
    class Filter(_message.Message):
        __slots__ = ("expired_on_target",)
        EXPIRED_ON_TARGET_FIELD_NUMBER: _ClassVar[int]
        expired_on_target: SnapshotTargetProto
        def __init__(self, expired_on_target: _Optional[_Union[SnapshotTargetProto, _Mapping]] = ...) -> None: ...
    INCLUDE_PUBLIC_STATUSES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_RUNS_FILTER_FIELD_NUMBER: _ClassVar[int]
    include_public_statuses: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.MagnetoPublicStatus]
    start_time_interval: TimeInterval
    exclude_runs_filter: ProtectionRunSelectorProto.Filter
    def __init__(self, include_public_statuses: _Optional[_Iterable[_Union[_enum_wrappers_pb2.MagnetoPublicStatus, _Mapping]]] = ..., start_time_interval: _Optional[_Union[TimeInterval, _Mapping]] = ..., exclude_runs_filter: _Optional[_Union[ProtectionRunSelectorProto.Filter, _Mapping]] = ...) -> None: ...

class EntitySelectorProto(_message.Message):
    __slots__ = ("registered_entities", "all_entities")
    REGISTERED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ALL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    registered_entities: bool
    all_entities: bool
    def __init__(self, registered_entities: bool = ..., all_entities: bool = ...) -> None: ...

class DataLocatorProto(_message.Message):
    __slots__ = ("type", "node_disk_info", "vault_info", "view_info", "top_level_folder")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNodeDisk: _ClassVar[DataLocatorProto.Type]
        kView: _ClassVar[DataLocatorProto.Type]
        kVault: _ClassVar[DataLocatorProto.Type]
    kNodeDisk: DataLocatorProto.Type
    kView: DataLocatorProto.Type
    kVault: DataLocatorProto.Type
    class NodeDisk(_message.Message):
        __slots__ = ("disk_id", "expected_node_ip", "expected_mount_path")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_NODE_IP_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        expected_node_ip: str
        expected_mount_path: str
        def __init__(self, disk_id: _Optional[int] = ..., expected_node_ip: _Optional[str] = ..., expected_mount_path: _Optional[str] = ...) -> None: ...
    class Vault(_message.Message):
        __slots__ = ("vault_id",)
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        vault_id: int
        def __init__(self, vault_id: _Optional[int] = ...) -> None: ...
    class View(_message.Message):
        __slots__ = ("view_name",)
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        def __init__(self, view_name: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    VAULT_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_FOLDER_FIELD_NUMBER: _ClassVar[int]
    type: DataLocatorProto.Type
    node_disk_info: DataLocatorProto.NodeDisk
    vault_info: DataLocatorProto.Vault
    view_info: DataLocatorProto.View
    top_level_folder: str
    def __init__(self, type: _Optional[_Union[DataLocatorProto.Type, str]] = ..., node_disk_info: _Optional[_Union[DataLocatorProto.NodeDisk, _Mapping]] = ..., vault_info: _Optional[_Union[DataLocatorProto.Vault, _Mapping]] = ..., view_info: _Optional[_Union[DataLocatorProto.View, _Mapping]] = ..., top_level_folder: _Optional[str] = ...) -> None: ...

class TimeRangeUsecs(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("day", "start_time", "end_time")
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Day.Type
    start_time: Time
    end_time: Time
    def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., start_time: _Optional[_Union[Time, _Mapping]] = ..., end_time: _Optional[_Union[Time, _Mapping]] = ...) -> None: ...

class ScheduleProto(_message.Message):
    __slots__ = ("type", "periodic_time_windows", "time_ranges", "timezone")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownSchedule: _ClassVar[ScheduleProto.Type]
        kPeriodicTimeWindows: _ClassVar[ScheduleProto.Type]
        kCustomIntervals: _ClassVar[ScheduleProto.Type]
    kUnknownSchedule: ScheduleProto.Type
    kPeriodicTimeWindows: ScheduleProto.Type
    kCustomIntervals: ScheduleProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    type: ScheduleProto.Type
    periodic_time_windows: _containers.RepeatedCompositeFieldContainer[TimeWindow]
    time_ranges: _containers.RepeatedCompositeFieldContainer[TimeRangeUsecs]
    timezone: str
    def __init__(self, type: _Optional[_Union[ScheduleProto.Type, str]] = ..., periodic_time_windows: _Optional[_Iterable[_Union[TimeWindow, _Mapping]]] = ..., time_ranges: _Optional[_Iterable[_Union[TimeRangeUsecs, _Mapping]]] = ..., timezone: _Optional[str] = ...) -> None: ...

class MaintenanceModeConfigProto(_message.Message):
    __slots__ = ("workflow_intervention_spec_vec", "activation_time_intervals", "maintenance_schedule", "user_message")
    class Intervention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownIntervention: _ClassVar[MaintenanceModeConfigProto.Intervention]
        kNoIntervention: _ClassVar[MaintenanceModeConfigProto.Intervention]
        kCancel: _ClassVar[MaintenanceModeConfigProto.Intervention]
    kUnknownIntervention: MaintenanceModeConfigProto.Intervention
    kNoIntervention: MaintenanceModeConfigProto.Intervention
    kCancel: MaintenanceModeConfigProto.Intervention
    class WorkflowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownType: _ClassVar[MaintenanceModeConfigProto.WorkflowType]
        kBackupRun: _ClassVar[MaintenanceModeConfigProto.WorkflowType]
    kUnknownType: MaintenanceModeConfigProto.WorkflowType
    kBackupRun: MaintenanceModeConfigProto.WorkflowType
    class WorkflowInterventionSpec(_message.Message):
        __slots__ = ("workflow_type", "intervention")
        WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
        INTERVENTION_FIELD_NUMBER: _ClassVar[int]
        workflow_type: MaintenanceModeConfigProto.WorkflowType
        intervention: MaintenanceModeConfigProto.Intervention
        def __init__(self, workflow_type: _Optional[_Union[MaintenanceModeConfigProto.WorkflowType, str]] = ..., intervention: _Optional[_Union[MaintenanceModeConfigProto.Intervention, str]] = ...) -> None: ...
    WORKFLOW_INTERVENTION_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TIME_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    workflow_intervention_spec_vec: _containers.RepeatedCompositeFieldContainer[MaintenanceModeConfigProto.WorkflowInterventionSpec]
    activation_time_intervals: _containers.RepeatedCompositeFieldContainer[TimeRangeUsecs]
    maintenance_schedule: ScheduleProto
    user_message: str
    def __init__(self, workflow_intervention_spec_vec: _Optional[_Iterable[_Union[MaintenanceModeConfigProto.WorkflowInterventionSpec, _Mapping]]] = ..., activation_time_intervals: _Optional[_Iterable[_Union[TimeRangeUsecs, _Mapping]]] = ..., maintenance_schedule: _Optional[_Union[ScheduleProto, _Mapping]] = ..., user_message: _Optional[str] = ...) -> None: ...

class ObjectRunIdentifier(_message.Message):
    __slots__ = ("object_id", "object_string_id", "environment", "run_start_time_usecs")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    object_string_id: str
    environment: _enum_wrappers_pb2.EnvironmentProto
    run_start_time_usecs: int
    def __init__(self, object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...
