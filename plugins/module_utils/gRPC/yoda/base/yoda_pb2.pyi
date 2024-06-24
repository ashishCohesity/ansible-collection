from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.connectors.vmware import vmware_base_pb2 as _vmware_base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from util.disklib.base import enums_pb2 as _enums_pb2_1
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from yoda.base import reports_pb2 as _reports_pb2
from yoda.base import error_pb2 as _error_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from yoda.base import vmware_pb2 as _vmware_pb2
from yoda.base import o365_pb2 as _o365_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.util import work_item_pb2 as _work_item_pb2
from yoda.db import tag_db_pb2 as _tag_db_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCluster: _ClassVar[AuditType]
    kFiler: _ClassVar[AuditType]

class TenantOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kMigration: _ClassVar[TenantOperationType]
    kDeletion: _ClassVar[TenantOperationType]
kCluster: AuditType
kFiler: AuditType
kMigration: TenantOperationType
kDeletion: TenantOperationType

class SnapshotReplicas(_message.Message):
    __slots__ = ("replica_vec",)
    class Replica(_message.Message):
        __slots__ = ("target", "expiry_time_usecs", "archive_uid", "is_cloud_domain_archive")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        IS_CLOUD_DOMAIN_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
        target: _policy_pb2.SnapshotTarget
        expiry_time_usecs: int
        archive_uid: _universal_id_pb2.UniversalIdProto
        is_cloud_domain_archive: bool
        def __init__(self, target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_cloud_domain_archive: bool = ...) -> None: ...
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    replica_vec: _containers.RepeatedCompositeFieldContainer[SnapshotReplicas.Replica]
    def __init__(self, replica_vec: _Optional[_Iterable[_Union[SnapshotReplicas.Replica, _Mapping]]] = ...) -> None: ...

class TaggedSnapshots(_message.Message):
    __slots__ = ("job_instance_id_vec",)
    JOB_INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    job_instance_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, job_instance_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class AddSnapshotArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "snapshot_timestamp_usecs", "object_name", "job_name", "object_aliases", "deprecated_view_path", "view_name", "snapshot_dir", "view_box_id", "preferred_read_node_id", "logical_size_bytes", "delta_size_bytes", "physical_size_bytes", "primary_physical_size_bytes", "base_instance_id", "disk_vec", "indexing_policy", "cluster_partition_id", "registered_source", "is_full_backup", "extended_info", "replica_info", "attribute_map", "progress_monitor_task_path", "progress_monitor_created", "extract_volume_mapping_only", "volume_map", "skip_disk_or_volume", "snapshot_type", "backup_type", "scheduled_backup_type", "tenant_id", "nas_backup_type_vec", "enable_system_backup", "auto_protected_source", "parent_work_item_id", "DEPRECATED_is_direct_archive_snapshot", "DEPRECATED_nas_backup_checkpoint_file_name", "DEPRECATED_nas_backup_error_rocksdb_name", "nas_checkpoint_params", "skip_local_replica_in_search", "skip_indexing_for_cloud_archive_direct_job", "snap_change_info_params", "is_reindexing_request")
    class DiskInfo(_message.Message):
        __slots__ = ("disk_file_name", "disk_format", "delta_size_bytes", "mount_point", "volume_guid")
        DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
        DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
        disk_file_name: str
        disk_format: _enums_pb2_1.DiskFormat.Type
        delta_size_bytes: int
        mount_point: str
        volume_guid: str
        def __init__(self, disk_file_name: _Optional[str] = ..., disk_format: _Optional[_Union[_enums_pb2_1.DiskFormat.Type, str]] = ..., delta_size_bytes: _Optional[int] = ..., mount_point: _Optional[str] = ..., volume_guid: _Optional[str] = ...) -> None: ...
    class ExtendedInformation(_message.Message):
        __slots__ = ("type", "vmware_add_snapshot_arg", "o365_add_snapshot_arg", "uda_add_snapshot_arg", "record_stats")
        class UdaAddSnapshotArg(_message.Message):
            __slots__ = ("entity_support",)
            ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
            entity_support: bool
            def __init__(self, entity_support: bool = ...) -> None: ...
        class RecordStats(_message.Message):
            __slots__ = ("added", "deleted", "modified")
            ADDED_FIELD_NUMBER: _ClassVar[int]
            DELETED_FIELD_NUMBER: _ClassVar[int]
            MODIFIED_FIELD_NUMBER: _ClassVar[int]
            added: int
            deleted: int
            modified: int
            def __init__(self, added: _Optional[int] = ..., deleted: _Optional[int] = ..., modified: _Optional[int] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VMWARE_ADD_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
        O365_ADD_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
        UDA_ADD_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
        RECORD_STATS_FIELD_NUMBER: _ClassVar[int]
        type: _enums_pb2.Environment.Type
        vmware_add_snapshot_arg: _vmware_pb2.VMwareAddSnapshotArg
        o365_add_snapshot_arg: _o365_pb2.O365AddSnapshotArg
        uda_add_snapshot_arg: AddSnapshotArg.ExtendedInformation.UdaAddSnapshotArg
        record_stats: AddSnapshotArg.ExtendedInformation.RecordStats
        def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., vmware_add_snapshot_arg: _Optional[_Union[_vmware_pb2.VMwareAddSnapshotArg, _Mapping]] = ..., o365_add_snapshot_arg: _Optional[_Union[_o365_pb2.O365AddSnapshotArg, _Mapping]] = ..., uda_add_snapshot_arg: _Optional[_Union[AddSnapshotArg.ExtendedInformation.UdaAddSnapshotArg, _Mapping]] = ..., record_stats: _Optional[_Union[AddSnapshotArg.ExtendedInformation.RecordStats, _Mapping]] = ...) -> None: ...
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    class NasCheckpointParams(_message.Message):
        __slots__ = ("checkpoint_file_name", "error_rocksdb_name", "skipped_checkpoint_file_name", "case_insensitive", "traversal_type", "sibling_order_type", "filtering_policy", "backup_additional_entities_to_skip_vec", "include_smb_dir_reparse_point", "skip_smb_offline_files")
        CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
        TRAVERSAL_TYPE_FIELD_NUMBER: _ClassVar[int]
        SIBLING_ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_ADDITIONAL_ENTITIES_TO_SKIP_VEC_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_SMB_DIR_REPARSE_POINT_FIELD_NUMBER: _ClassVar[int]
        SKIP_SMB_OFFLINE_FILES_FIELD_NUMBER: _ClassVar[int]
        checkpoint_file_name: str
        error_rocksdb_name: str
        skipped_checkpoint_file_name: str
        case_insensitive: bool
        traversal_type: _directory_walker_pb2.TraversalType.Type
        sibling_order_type: _directory_walker_pb2.SiblingOrderType.Type
        filtering_policy: _env_params_pb2_1.FilteringPolicyProto
        backup_additional_entities_to_skip_vec: _containers.RepeatedScalarFieldContainer[str]
        include_smb_dir_reparse_point: bool
        skip_smb_offline_files: bool
        def __init__(self, checkpoint_file_name: _Optional[str] = ..., error_rocksdb_name: _Optional[str] = ..., skipped_checkpoint_file_name: _Optional[str] = ..., case_insensitive: bool = ..., traversal_type: _Optional[_Union[_directory_walker_pb2.TraversalType.Type, str]] = ..., sibling_order_type: _Optional[_Union[_directory_walker_pb2.SiblingOrderType.Type, str]] = ..., filtering_policy: _Optional[_Union[_env_params_pb2_1.FilteringPolicyProto, _Mapping]] = ..., backup_additional_entities_to_skip_vec: _Optional[_Iterable[str]] = ..., include_smb_dir_reparse_point: bool = ..., skip_smb_offline_files: bool = ...) -> None: ...
    class SnapChangeInfoParams(_message.Message):
        __slots__ = ("rocksdb_name", "file_name", "uses_custom_rocks_db_comparator", "use_compressed_cache_file", "snap_change_num_entries", "is_full_directory_walk", "master_rocksdb_name")
        ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        USES_CUSTOM_ROCKS_DB_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
        USE_COMPRESSED_CACHE_FILE_FIELD_NUMBER: _ClassVar[int]
        SNAP_CHANGE_NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_DIRECTORY_WALK_FIELD_NUMBER: _ClassVar[int]
        MASTER_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
        rocksdb_name: str
        file_name: str
        uses_custom_rocks_db_comparator: bool
        use_compressed_cache_file: bool
        snap_change_num_entries: int
        is_full_directory_walk: bool
        master_rocksdb_name: str
        def __init__(self, rocksdb_name: _Optional[str] = ..., file_name: _Optional[str] = ..., uses_custom_rocks_db_comparator: bool = ..., use_compressed_cache_file: bool = ..., snap_change_num_entries: _Optional[int] = ..., is_full_directory_walk: bool = ..., master_rocksdb_name: _Optional[str] = ...) -> None: ...
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ALIASES_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_READ_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_CREATED_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_VOLUME_MAPPING_ONLY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MAP_FIELD_NUMBER: _ClassVar[int]
    SKIP_DISK_OR_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAS_BACKUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    AUTO_PROTECTED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_WORK_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_IS_DIRECT_ARCHIVE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_NAS_BACKUP_CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_NAS_BACKUP_ERROR_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
    NAS_CHECKPOINT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_LOCAL_REPLICA_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SKIP_INDEXING_FOR_CLOUD_ARCHIVE_DIRECT_JOB_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_INFO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_REINDEXING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    snapshot_timestamp_usecs: int
    object_name: str
    job_name: str
    object_aliases: _containers.RepeatedScalarFieldContainer[str]
    deprecated_view_path: str
    view_name: str
    snapshot_dir: str
    view_box_id: int
    preferred_read_node_id: int
    logical_size_bytes: int
    delta_size_bytes: int
    physical_size_bytes: int
    primary_physical_size_bytes: int
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    disk_vec: _containers.RepeatedCompositeFieldContainer[AddSnapshotArg.DiskInfo]
    indexing_policy: _env_params_pb2_1.IndexingPolicyProto
    cluster_partition_id: int
    registered_source: _entity_pb2.EntityProto
    is_full_backup: bool
    extended_info: AddSnapshotArg.ExtendedInformation
    replica_info: SnapshotReplicas
    attribute_map: _containers.RepeatedCompositeFieldContainer[AddSnapshotArg.KeyValuePair]
    progress_monitor_task_path: str
    progress_monitor_created: bool
    extract_volume_mapping_only: bool
    volume_map: _volume_info_pb2.VolumeNameMap
    skip_disk_or_volume: bool
    snapshot_type: _magneto_pb2.ObjectSnapshotType.Type
    backup_type: _enums_pb2.Environment.Type
    scheduled_backup_type: _enums_pb2.ScheduledBackupType.Type
    tenant_id: str
    nas_backup_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
    enable_system_backup: bool
    auto_protected_source: _entity_pb2.EntityProto
    parent_work_item_id: int
    DEPRECATED_is_direct_archive_snapshot: bool
    DEPRECATED_nas_backup_checkpoint_file_name: str
    DEPRECATED_nas_backup_error_rocksdb_name: str
    nas_checkpoint_params: AddSnapshotArg.NasCheckpointParams
    skip_local_replica_in_search: bool
    skip_indexing_for_cloud_archive_direct_job: bool
    snap_change_info_params: AddSnapshotArg.SnapChangeInfoParams
    is_reindexing_request: bool
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., object_name: _Optional[str] = ..., job_name: _Optional[str] = ..., object_aliases: _Optional[_Iterable[str]] = ..., deprecated_view_path: _Optional[str] = ..., view_name: _Optional[str] = ..., snapshot_dir: _Optional[str] = ..., view_box_id: _Optional[int] = ..., preferred_read_node_id: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., delta_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., primary_physical_size_bytes: _Optional[int] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., disk_vec: _Optional[_Iterable[_Union[AddSnapshotArg.DiskInfo, _Mapping]]] = ..., indexing_policy: _Optional[_Union[_env_params_pb2_1.IndexingPolicyProto, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_full_backup: bool = ..., extended_info: _Optional[_Union[AddSnapshotArg.ExtendedInformation, _Mapping]] = ..., replica_info: _Optional[_Union[SnapshotReplicas, _Mapping]] = ..., attribute_map: _Optional[_Iterable[_Union[AddSnapshotArg.KeyValuePair, _Mapping]]] = ..., progress_monitor_task_path: _Optional[str] = ..., progress_monitor_created: bool = ..., extract_volume_mapping_only: bool = ..., volume_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., skip_disk_or_volume: bool = ..., snapshot_type: _Optional[_Union[_magneto_pb2.ObjectSnapshotType.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., scheduled_backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., tenant_id: _Optional[str] = ..., nas_backup_type_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ..., enable_system_backup: bool = ..., auto_protected_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_work_item_id: _Optional[int] = ..., DEPRECATED_is_direct_archive_snapshot: bool = ..., DEPRECATED_nas_backup_checkpoint_file_name: _Optional[str] = ..., DEPRECATED_nas_backup_error_rocksdb_name: _Optional[str] = ..., nas_checkpoint_params: _Optional[_Union[AddSnapshotArg.NasCheckpointParams, _Mapping]] = ..., skip_local_replica_in_search: bool = ..., skip_indexing_for_cloud_archive_direct_job: bool = ..., snap_change_info_params: _Optional[_Union[AddSnapshotArg.SnapChangeInfoParams, _Mapping]] = ..., is_reindexing_request: bool = ...) -> None: ...

class AddSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSnapshotReplicasArg(_message.Message):
    __slots__ = ("object_id_vec", "instance_id", "replica_info", "cluster_partition_id", "expire_all_snapshots")
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_ALL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    object_id_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.MagnetoObjectId]
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    replica_info: SnapshotReplicas
    cluster_partition_id: int
    expire_all_snapshots: bool
    def __init__(self, object_id_vec: _Optional[_Iterable[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., replica_info: _Optional[_Union[SnapshotReplicas, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., expire_all_snapshots: bool = ...) -> None: ...

class UpdateSnapshotReplicasResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveSnapshotArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "instance_id_vec", "cluster_partition_id", "view_box_id", "view_name_vec", "backup_type", "aux_db_id_vec", "tenant_id")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUX_DB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    cluster_partition_id: int
    view_box_id: int
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    backup_type: _enums_pb2.Environment.Type
    aux_db_id_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., cluster_partition_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name_vec: _Optional[_Iterable[str]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., aux_db_id_vec: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class RemoveSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveObjectArg(_message.Message):
    __slots__ = ("object_id", "cluster_partition_id")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    cluster_partition_id: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ...) -> None: ...

class RemoveObjectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRecursiveFolderSizeArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "dir_path", "volume_name", "cookie")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    dir_path: str
    volume_name: str
    cookie: bytes
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., dir_path: _Optional[str] = ..., volume_name: _Optional[str] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class GetRecursiveFolderSizeResult(_message.Message):
    __slots__ = ("error", "size_bytes", "cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    size_bytes: int
    cookie: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., size_bytes: _Optional[int] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class ExtractFileRangeArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "filepath", "vmware_vmx_file", "requested_vmware_file_type", "cluster_partition_id", "start_offset", "length", "snapshot_location", "DEPRECATED_view_path", "DEPRECATED_snapshot_dir")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    VMWARE_VMX_FILE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_VMWARE_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    filepath: str
    vmware_vmx_file: bool
    requested_vmware_file_type: _vmware_base_pb2.FileType
    cluster_partition_id: int
    start_offset: int
    length: int
    snapshot_location: SnapFSPath
    DEPRECATED_view_path: str
    DEPRECATED_snapshot_dir: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., filepath: _Optional[str] = ..., vmware_vmx_file: bool = ..., requested_vmware_file_type: _Optional[_Union[_vmware_base_pb2.FileType, str]] = ..., cluster_partition_id: _Optional[int] = ..., start_offset: _Optional[int] = ..., length: _Optional[int] = ..., snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., DEPRECATED_view_path: _Optional[str] = ..., DEPRECATED_snapshot_dir: _Optional[str] = ...) -> None: ...

class ExtractNFSFileRangeArg(_message.Message):
    __slots__ = ("is_nfs_file", "partition_id", "view_box_id", "view_name", "file_path", "start_offset", "length_bytes")
    IS_NFS_FILE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    is_nfs_file: bool
    partition_id: int
    view_box_id: int
    view_name: str
    file_path: str
    start_offset: int
    length_bytes: int
    def __init__(self, is_nfs_file: bool = ..., partition_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., start_offset: _Optional[int] = ..., length_bytes: _Optional[int] = ...) -> None: ...

class ExtractFileRangeResult(_message.Message):
    __slots__ = ("error", "file_length", "start_offset", "data", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_length: int
    start_offset: int
    data: bytes
    eof: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_length: _Optional[int] = ..., start_offset: _Optional[int] = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class GetReportArg(_message.Message):
    __slots__ = ("report_type", "time_interval_size_secs", "num_time_intervals", "topn", "aggregate_for_primary", "job_id_set", "view_box_id_set", "registered_source_hash_set", "object_id_set", "entity_id_set", "partition_id_set")
    class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTopFiles: _ClassVar[GetReportArg.ReportType]
        kCategories: _ClassVar[GetReportArg.ReportType]
        kSourceGrowth: _ClassVar[GetReportArg.ReportType]
        kObjectGrowth: _ClassVar[GetReportArg.ReportType]
        kObjectIndex: _ClassVar[GetReportArg.ReportType]
    kTopFiles: GetReportArg.ReportType
    kCategories: GetReportArg.ReportType
    kSourceGrowth: GetReportArg.ReportType
    kObjectGrowth: GetReportArg.ReportType
    kObjectIndex: GetReportArg.ReportType
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_SIZE_SECS_FIELD_NUMBER: _ClassVar[int]
    NUM_TIME_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    TOPN_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FOR_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_SET_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_SET_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_HASH_SET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_SET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_SET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_SET_FIELD_NUMBER: _ClassVar[int]
    report_type: GetReportArg.ReportType
    time_interval_size_secs: int
    num_time_intervals: int
    topn: int
    aggregate_for_primary: bool
    job_id_set: _containers.RepeatedScalarFieldContainer[int]
    view_box_id_set: _containers.RepeatedScalarFieldContainer[int]
    registered_source_hash_set: _containers.RepeatedScalarFieldContainer[int]
    object_id_set: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.MagnetoObjectId]
    entity_id_set: _containers.RepeatedScalarFieldContainer[int]
    partition_id_set: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, report_type: _Optional[_Union[GetReportArg.ReportType, str]] = ..., time_interval_size_secs: _Optional[int] = ..., num_time_intervals: _Optional[int] = ..., topn: _Optional[int] = ..., aggregate_for_primary: bool = ..., job_id_set: _Optional[_Iterable[int]] = ..., view_box_id_set: _Optional[_Iterable[int]] = ..., registered_source_hash_set: _Optional[_Iterable[int]] = ..., object_id_set: _Optional[_Iterable[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]]] = ..., entity_id_set: _Optional[_Iterable[int]] = ..., partition_id_set: _Optional[_Iterable[int]] = ...) -> None: ...

class GetReportResult(_message.Message):
    __slots__ = ("top_files", "categories", "source_growth", "objects", "objects_index", "error")
    TOP_FILES_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GROWTH_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_INDEX_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    top_files: _reports_pb2.TopFilesReport
    categories: _reports_pb2.CategoryUsageReport
    source_growth: _reports_pb2.SourceGrowthReport
    objects: _reports_pb2.ObjectReport
    objects_index: _reports_pb2.ObjectIndexReport
    error: _error_pb2.ErrorProto
    def __init__(self, top_files: _Optional[_Union[_reports_pb2.TopFilesReport, _Mapping]] = ..., categories: _Optional[_Union[_reports_pb2.CategoryUsageReport, _Mapping]] = ..., source_growth: _Optional[_Union[_reports_pb2.SourceGrowthReport, _Mapping]] = ..., objects: _Optional[_Union[_reports_pb2.ObjectReport, _Mapping]] = ..., objects_index: _Optional[_Union[_reports_pb2.ObjectIndexReport, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupMasterResult(_message.Message):
    __slots__ = ("ip", "port", "node_id", "error")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    node_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., node_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetPendingInfoArg(_message.Message):
    __slots__ = ("queue_type",)
    class QueueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kYodaQueue: _ClassVar[GetPendingInfoArg.QueueType]
        kAuditQueue: _ClassVar[GetPendingInfoArg.QueueType]
        kLibrarianMigrationWorkQueue: _ClassVar[GetPendingInfoArg.QueueType]
        kESMigrationWorkQueue: _ClassVar[GetPendingInfoArg.QueueType]
    kYodaQueue: GetPendingInfoArg.QueueType
    kAuditQueue: GetPendingInfoArg.QueueType
    kLibrarianMigrationWorkQueue: GetPendingInfoArg.QueueType
    kESMigrationWorkQueue: GetPendingInfoArg.QueueType
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    queue_type: GetPendingInfoArg.QueueType
    def __init__(self, queue_type: _Optional[_Union[GetPendingInfoArg.QueueType, str]] = ...) -> None: ...

class GetPendingInfoResult(_message.Message):
    __slots__ = ("num_pending_work_items", "num_pending_wal_ops", "error")
    NUM_PENDING_WORK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_PENDING_WAL_OPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    num_pending_work_items: int
    num_pending_wal_ops: int
    error: _error_pb2.ErrorProto
    def __init__(self, num_pending_work_items: _Optional[int] = ..., num_pending_wal_ops: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetCrackedFileVersionsArg(_message.Message):
    __slots__ = ("object_id", "filename", "from_object_snapshots_only", "cluster_partition_id", "tenant_id", "instance_ids_to_include", "snapshot_backup_type")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FROM_OBJECT_SNAPSHOTS_ONLY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_IDS_TO_INCLUDE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    filename: str
    from_object_snapshots_only: bool
    cluster_partition_id: int
    tenant_id: str
    instance_ids_to_include: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    snapshot_backup_type: _enums_pb2.Environment.Type
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., filename: _Optional[str] = ..., from_object_snapshots_only: bool = ..., cluster_partition_id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., instance_ids_to_include: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., snapshot_backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class GetCrackedFileVersionsResult(_message.Message):
    __slots__ = ("error", "instance_ids", "versions", "from_object_snapshots")
    class VersionInfo(_message.Message):
        __slots__ = ("size_bytes", "mtime_usecs", "instance_id", "has_local_replica", "has_remote_replica", "has_archival_replica", "replica_info", "scheduled_backup_type", "backup_source_inode_id", "version_metadata")
        class VersionMetadata(_message.Message):
            __slots__ = ("unique_item_identifier",)
            UNIQUE_ITEM_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            unique_item_identifier: str
            def __init__(self, unique_item_identifier: _Optional[str] = ...) -> None: ...
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        HAS_LOCAL_REPLICA_FIELD_NUMBER: _ClassVar[int]
        HAS_REMOTE_REPLICA_FIELD_NUMBER: _ClassVar[int]
        HAS_ARCHIVAL_REPLICA_FIELD_NUMBER: _ClassVar[int]
        REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_METADATA_FIELD_NUMBER: _ClassVar[int]
        size_bytes: int
        mtime_usecs: int
        instance_id: _yoda_types_pb2.MagnetoInstanceId
        has_local_replica: bool
        has_remote_replica: bool
        has_archival_replica: bool
        replica_info: SnapshotReplicas
        scheduled_backup_type: _enums_pb2.ScheduledBackupType.Type
        backup_source_inode_id: int
        version_metadata: GetCrackedFileVersionsResult.VersionInfo.VersionMetadata
        def __init__(self, size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., has_local_replica: bool = ..., has_remote_replica: bool = ..., has_archival_replica: bool = ..., replica_info: _Optional[_Union[SnapshotReplicas, _Mapping]] = ..., scheduled_backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., backup_source_inode_id: _Optional[int] = ..., version_metadata: _Optional[_Union[GetCrackedFileVersionsResult.VersionInfo.VersionMetadata, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    FROM_OBJECT_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    instance_ids: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    versions: _containers.RepeatedCompositeFieldContainer[GetCrackedFileVersionsResult.VersionInfo]
    from_object_snapshots: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., instance_ids: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., versions: _Optional[_Iterable[_Union[GetCrackedFileVersionsResult.VersionInfo, _Mapping]]] = ..., from_object_snapshots: bool = ...) -> None: ...

class SnapFSPath(_message.Message):
    __slots__ = ("view_box_id", "view_name", "path_in_view")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    view_name: str
    path_in_view: str
    def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., path_in_view: _Optional[str] = ...) -> None: ...

class GetCrackedFileRestoreInfoArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "vm_snapshot_location", "filename_vec", "point_in_time_usecs")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VM_SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_VEC_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    vm_snapshot_location: SnapFSPath
    filename_vec: _containers.RepeatedScalarFieldContainer[str]
    point_in_time_usecs: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., vm_snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., filename_vec: _Optional[_Iterable[str]] = ..., point_in_time_usecs: _Optional[int] = ...) -> None: ...

class GetCrackedFileRestoreInfoResult(_message.Message):
    __slots__ = ("error", "object_id", "instance_id", "os_type", "file_info_vec")
    class FileInfo(_message.Message):
        __slots__ = ("filename", "is_directory", "file_error", "volume_info")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        FILE_ERROR_FIELD_NUMBER: _ClassVar[int]
        VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        filename: str
        is_directory: bool
        file_error: _error_pb2.ErrorProto
        volume_info: _volume_info_pb2.VolumeInfo
        def __init__(self, filename: _Optional[str] = ..., is_directory: bool = ..., file_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    os_type: _reports_pb2.OSType.Type
    file_info_vec: _containers.RepeatedCompositeFieldContainer[GetCrackedFileRestoreInfoResult.FileInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., os_type: _Optional[_Union[_reports_pb2.OSType.Type, str]] = ..., file_info_vec: _Optional[_Iterable[_Union[GetCrackedFileRestoreInfoResult.FileInfo, _Mapping]]] = ...) -> None: ...

class GCSnapshotsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GCTagsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VMBrowsingCookie(_message.Message):
    __slots__ = ("use_mapping",)
    USE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    use_mapping: int
    def __init__(self, use_mapping: _Optional[int] = ...) -> None: ...

class VMVolumeInfoArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "vm_snapshot_location", "supported_volumes_only", "compute_volume_info", "point_in_time_usecs", "populate_mount_io_info")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VM_SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VOLUMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    POPULATE_MOUNT_IO_INFO_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    vm_snapshot_location: SnapFSPath
    supported_volumes_only: bool
    compute_volume_info: bool
    point_in_time_usecs: int
    populate_mount_io_info: bool
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., vm_snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., supported_volumes_only: bool = ..., compute_volume_info: bool = ..., point_in_time_usecs: _Optional[int] = ..., populate_mount_io_info: bool = ...) -> None: ...

class VMVolumeInfoResult(_message.Message):
    __slots__ = ("error", "volume_name_map", "browsing_cookie", "volume_mount_io_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    BROWSING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_IO_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_name_map: _volume_info_pb2.VolumeNameMap
    browsing_cookie: VMBrowsingCookie
    volume_mount_io_info: _reports_pb2.VolumeMappingReport.VolumeMountIOInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_name_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., browsing_cookie: _Optional[_Union[VMBrowsingCookie, _Mapping]] = ..., volume_mount_io_info: _Optional[_Union[_reports_pb2.VolumeMappingReport.VolumeMountIOInfo, _Mapping]] = ...) -> None: ...

class FileStatInfo(_message.Message):
    __slots__ = ("size", "mtime_usecs", "type", "backup_source_inode_id", "sharepoint_item_metadata")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SOURCE_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_ITEM_METADATA_FIELD_NUMBER: _ClassVar[int]
    size: int
    mtime_usecs: int
    type: ReadDirResult.DirEntry.Type
    backup_source_inode_id: int
    sharepoint_item_metadata: _o365_pb2.SharepointItemMetadata
    def __init__(self, size: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., type: _Optional[_Union[ReadDirResult.DirEntry.Type, str]] = ..., backup_source_inode_id: _Optional[int] = ..., sharepoint_item_metadata: _Optional[_Union[_o365_pb2.SharepointItemMetadata, _Mapping]] = ...) -> None: ...

class ReadDirCookie(_message.Message):
    __slots__ = ("cookie_val", "librarian_cookie")
    COOKIE_VAL_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    cookie_val: int
    librarian_cookie: str
    def __init__(self, cookie_val: _Optional[int] = ..., librarian_cookie: _Optional[str] = ...) -> None: ...

class ReadDirArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "dir_path", "max_entries", "stat_file_entries", "volume_name", "browsing_cookie", "read_dir_cookie", "snapshot_location", "use_librarian", "point_in_time_usecs")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    STAT_FILE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    BROWSING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_COOKIE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    USE_LIBRARIAN_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    dir_path: bytes
    max_entries: int
    stat_file_entries: bool
    volume_name: str
    browsing_cookie: VMBrowsingCookie
    read_dir_cookie: ReadDirCookie
    snapshot_location: SnapFSPath
    use_librarian: bool
    point_in_time_usecs: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., dir_path: _Optional[bytes] = ..., max_entries: _Optional[int] = ..., stat_file_entries: bool = ..., volume_name: _Optional[str] = ..., browsing_cookie: _Optional[_Union[VMBrowsingCookie, _Mapping]] = ..., read_dir_cookie: _Optional[_Union[ReadDirCookie, _Mapping]] = ..., snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., use_librarian: bool = ..., point_in_time_usecs: _Optional[int] = ...) -> None: ...

class ReadDirResult(_message.Message):
    __slots__ = ("error", "entry_vec", "browsing_cookie", "read_dir_cookie")
    class DirEntry(_message.Message):
        __slots__ = ("type", "name", "fstat_info")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[ReadDirResult.DirEntry.Type]
            kDirectory: _ClassVar[ReadDirResult.DirEntry.Type]
            kSymlink: _ClassVar[ReadDirResult.DirEntry.Type]
        kFile: ReadDirResult.DirEntry.Type
        kDirectory: ReadDirResult.DirEntry.Type
        kSymlink: ReadDirResult.DirEntry.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FSTAT_INFO_FIELD_NUMBER: _ClassVar[int]
        type: ReadDirResult.DirEntry.Type
        name: bytes
        fstat_info: FileStatInfo
        def __init__(self, type: _Optional[_Union[ReadDirResult.DirEntry.Type, str]] = ..., name: _Optional[bytes] = ..., fstat_info: _Optional[_Union[FileStatInfo, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    BROWSING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entry_vec: _containers.RepeatedCompositeFieldContainer[ReadDirResult.DirEntry]
    browsing_cookie: VMBrowsingCookie
    read_dir_cookie: ReadDirCookie
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entry_vec: _Optional[_Iterable[_Union[ReadDirResult.DirEntry, _Mapping]]] = ..., browsing_cookie: _Optional[_Union[VMBrowsingCookie, _Mapping]] = ..., read_dir_cookie: _Optional[_Union[ReadDirCookie, _Mapping]] = ...) -> None: ...

class FileStatArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "file_path", "snapshot_location", "volume_name", "browsing_cookie", "use_librarian", "point_in_time_usecs")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    BROWSING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    USE_LIBRARIAN_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    file_path: bytes
    snapshot_location: SnapFSPath
    volume_name: str
    browsing_cookie: VMBrowsingCookie
    use_librarian: bool
    point_in_time_usecs: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., file_path: _Optional[bytes] = ..., snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., volume_name: _Optional[str] = ..., browsing_cookie: _Optional[_Union[VMBrowsingCookie, _Mapping]] = ..., use_librarian: bool = ..., point_in_time_usecs: _Optional[int] = ...) -> None: ...

class FileStatResult(_message.Message):
    __slots__ = ("error", "fstat_info", "browsing_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FSTAT_INFO_FIELD_NUMBER: _ClassVar[int]
    BROWSING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    fstat_info: FileStatInfo
    browsing_cookie: VMBrowsingCookie
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fstat_info: _Optional[_Union[FileStatInfo, _Mapping]] = ..., browsing_cookie: _Optional[_Union[VMBrowsingCookie, _Mapping]] = ...) -> None: ...

class GetMRResultFormatsArg(_message.Message):
    __slots__ = ("file_prefix", "file_location")
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    file_prefix: bytes
    file_location: SnapFSPath
    def __init__(self, file_prefix: _Optional[bytes] = ..., file_location: _Optional[_Union[SnapFSPath, _Mapping]] = ...) -> None: ...

class GetMRResultFormatsResult(_message.Message):
    __slots__ = ("error", "formats")
    class FormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCsv: _ClassVar[GetMRResultFormatsResult.FormatType]
    kCsv: GetMRResultFormatsResult.FormatType
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    formats: _containers.RepeatedScalarFieldContainer[GetMRResultFormatsResult.FormatType]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., formats: _Optional[_Iterable[_Union[GetMRResultFormatsResult.FormatType, str]]] = ...) -> None: ...

class FixCfileIndexArg(_message.Message):
    __slots__ = ("object_id", "cluster_partition_id")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    cluster_partition_id: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ...) -> None: ...

class ScanBucketArg(_message.Message):
    __slots__ = ("table_name", "bucket_id", "audit_type")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    bucket_id: int
    audit_type: AuditType
    def __init__(self, table_name: _Optional[str] = ..., bucket_id: _Optional[int] = ..., audit_type: _Optional[_Union[AuditType, str]] = ...) -> None: ...

class ScanBucketResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GCAuditLogsArg(_message.Message):
    __slots__ = ("audit_type",)
    AUDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    audit_type: AuditType
    def __init__(self, audit_type: _Optional[_Union[AuditType, str]] = ...) -> None: ...

class GCAuditLogsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ConsumeAuditLogsArg(_message.Message):
    __slots__ = ("audit_type",)
    AUDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    audit_type: AuditType
    def __init__(self, audit_type: _Optional[_Union[AuditType, str]] = ...) -> None: ...

class ConsumeAuditLogsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GCArchivalDbsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GCZipCheckpointsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GCLibrarianMigrationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FixESIndicesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCrackedFileIndexingStatusArg(_message.Message):
    __slots__ = ("object_id", "instance_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ...) -> None: ...

class GetCrackedFileIndexingStatusResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelBulkFilesDownloadArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class CancelBulkFilesDownloadResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepareBulkFilesDownloadArg(_message.Message):
    __slots__ = ("object_id", "instance_id", "filepath_vec", "task_id", "snapshot_location", "download_location", "archive_filename", "cluster_partition_id", "progress_monitor_task_path")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    filepath_vec: _containers.RepeatedScalarFieldContainer[str]
    task_id: int
    snapshot_location: SnapFSPath
    download_location: SnapFSPath
    archive_filename: str
    cluster_partition_id: int
    progress_monitor_task_path: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., filepath_vec: _Optional[_Iterable[str]] = ..., task_id: _Optional[int] = ..., snapshot_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., download_location: _Optional[_Union[SnapFSPath, _Mapping]] = ..., archive_filename: _Optional[str] = ..., cluster_partition_id: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ...) -> None: ...

class PrepareBulkFilesDownloadResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ThreadProgressInfo(_message.Message):
    __slots__ = ("session_id", "node_id", "thread_id", "object_id", "progress_type", "timestamp_usecs", "maybe_hung", "op_type", "filesystem_type")
    class ProgressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ThreadProgressInfo.ProgressType]
        kProgress: _ClassVar[ThreadProgressInfo.ProgressType]
        kComplete: _ClassVar[ThreadProgressInfo.ProgressType]
    kStarted: ThreadProgressInfo.ProgressType
    kProgress: ThreadProgressInfo.ProgressType
    kComplete: ThreadProgressInfo.ProgressType
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMount: _ClassVar[ThreadProgressInfo.OpType]
        kIndexing: _ClassVar[ThreadProgressInfo.OpType]
        kReadDir: _ClassVar[ThreadProgressInfo.OpType]
        kExtractFileRange: _ClassVar[ThreadProgressInfo.OpType]
        kFileStat: _ClassVar[ThreadProgressInfo.OpType]
        kVolumeMapping: _ClassVar[ThreadProgressInfo.OpType]
        kUnmount: _ClassVar[ThreadProgressInfo.OpType]
        kZip: _ClassVar[ThreadProgressInfo.OpType]
    kMount: ThreadProgressInfo.OpType
    kIndexing: ThreadProgressInfo.OpType
    kReadDir: ThreadProgressInfo.OpType
    kExtractFileRange: ThreadProgressInfo.OpType
    kFileStat: ThreadProgressInfo.OpType
    kVolumeMapping: ThreadProgressInfo.OpType
    kUnmount: ThreadProgressInfo.OpType
    kZip: ThreadProgressInfo.OpType
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    MAYBE_HUNG_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    thread_id: int
    object_id: str
    progress_type: ThreadProgressInfo.ProgressType
    timestamp_usecs: int
    maybe_hung: bool
    op_type: ThreadProgressInfo.OpType
    filesystem_type: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., thread_id: _Optional[int] = ..., object_id: _Optional[str] = ..., progress_type: _Optional[_Union[ThreadProgressInfo.ProgressType, str]] = ..., timestamp_usecs: _Optional[int] = ..., maybe_hung: bool = ..., op_type: _Optional[_Union[ThreadProgressInfo.OpType, str]] = ..., filesystem_type: _Optional[str] = ...) -> None: ...

class LibrarianMigrationWork(_message.Message):
    __slots__ = ("object_id", "cluster_partition_id", "control_item_type")
    class ControlItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInitiator: _ClassVar[LibrarianMigrationWork.ControlItemType]
        kAccumulator: _ClassVar[LibrarianMigrationWork.ControlItemType]
        kFinisher: _ClassVar[LibrarianMigrationWork.ControlItemType]
    kInitiator: LibrarianMigrationWork.ControlItemType
    kAccumulator: LibrarianMigrationWork.ControlItemType
    kFinisher: LibrarianMigrationWork.ControlItemType
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    cluster_partition_id: int
    control_item_type: LibrarianMigrationWork.ControlItemType
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., control_item_type: _Optional[_Union[LibrarianMigrationWork.ControlItemType, str]] = ...) -> None: ...

class GCLibrarianTagsWork(_message.Message):
    __slots__ = ("object_id", "tags_to_gc_vec", "cluster_partition_id", "librarian_scan_prefix")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_TO_GC_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_SCAN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    tags_to_gc_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_partition_id: int
    librarian_scan_prefix: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., tags_to_gc_vec: _Optional[_Iterable[str]] = ..., cluster_partition_id: _Optional[int] = ..., librarian_scan_prefix: _Optional[str] = ...) -> None: ...

class IndexingMetadataStats(_message.Message):
    __slots__ = ("object_id", "instance_id", "base_instance_id", "doc_stats_vec", "error_type", "indexing_error", "start_time_usecs", "end_time_usecs", "time_taken_usecs", "op_type", "histogram_vec", "volume_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotUpdated: _ClassVar[IndexingMetadataStats.Type]
        kNewDocument: _ClassVar[IndexingMetadataStats.Type]
        kUpdateDocument: _ClassVar[IndexingMetadataStats.Type]
        kDeleteDocument: _ClassVar[IndexingMetadataStats.Type]
    kNotUpdated: IndexingMetadataStats.Type
    kNewDocument: IndexingMetadataStats.Type
    kUpdateDocument: IndexingMetadataStats.Type
    kDeleteDocument: IndexingMetadataStats.Type
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[IndexingMetadataStats.ErrorType]
        kBaseInstanceNotPresent: _ClassVar[IndexingMetadataStats.ErrorType]
        kIndexingPolicyChanged: _ClassVar[IndexingMetadataStats.ErrorType]
    kNoError: IndexingMetadataStats.ErrorType
    kBaseInstanceNotPresent: IndexingMetadataStats.ErrorType
    kIndexingPolicyChanged: IndexingMetadataStats.ErrorType
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIndexing: _ClassVar[IndexingMetadataStats.OperationType]
        kRemoval: _ClassVar[IndexingMetadataStats.OperationType]
    kIndexing: IndexingMetadataStats.OperationType
    kRemoval: IndexingMetadataStats.OperationType
    class KeyValuePair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: IndexingMetadataStats.Type
        value: int
        def __init__(self, key: _Optional[_Union[IndexingMetadataStats.Type, str]] = ..., value: _Optional[int] = ...) -> None: ...
    class HistogramSketch(_message.Message):
        __slots__ = ("sketch_entity_type", "sketch_vec")
        class SketchEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFileExtension: _ClassVar[IndexingMetadataStats.HistogramSketch.SketchEntityType]
            kDirectory: _ClassVar[IndexingMetadataStats.HistogramSketch.SketchEntityType]
            kAddedFileExtension: _ClassVar[IndexingMetadataStats.HistogramSketch.SketchEntityType]
            kDeletedFileExtension: _ClassVar[IndexingMetadataStats.HistogramSketch.SketchEntityType]
        kFileExtension: IndexingMetadataStats.HistogramSketch.SketchEntityType
        kDirectory: IndexingMetadataStats.HistogramSketch.SketchEntityType
        kAddedFileExtension: IndexingMetadataStats.HistogramSketch.SketchEntityType
        kDeletedFileExtension: IndexingMetadataStats.HistogramSketch.SketchEntityType
        class Tuple(_message.Message):
            __slots__ = ("key", "frequency")
            KEY_FIELD_NUMBER: _ClassVar[int]
            FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            key: str
            frequency: float
            def __init__(self, key: _Optional[str] = ..., frequency: _Optional[float] = ...) -> None: ...
        SKETCH_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        SKETCH_VEC_FIELD_NUMBER: _ClassVar[int]
        sketch_entity_type: IndexingMetadataStats.HistogramSketch.SketchEntityType
        sketch_vec: _containers.RepeatedCompositeFieldContainer[IndexingMetadataStats.HistogramSketch.Tuple]
        def __init__(self, sketch_entity_type: _Optional[_Union[IndexingMetadataStats.HistogramSketch.SketchEntityType, str]] = ..., sketch_vec: _Optional[_Iterable[_Union[IndexingMetadataStats.HistogramSketch.Tuple, _Mapping]]] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DOC_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEXING_ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    doc_stats_vec: _containers.RepeatedCompositeFieldContainer[IndexingMetadataStats.KeyValuePair]
    error_type: IndexingMetadataStats.ErrorType
    indexing_error: _error_pb2.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    time_taken_usecs: int
    op_type: IndexingMetadataStats.OperationType
    histogram_vec: _containers.RepeatedCompositeFieldContainer[IndexingMetadataStats.HistogramSketch]
    volume_name: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., doc_stats_vec: _Optional[_Iterable[_Union[IndexingMetadataStats.KeyValuePair, _Mapping]]] = ..., error_type: _Optional[_Union[IndexingMetadataStats.ErrorType, str]] = ..., indexing_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ..., op_type: _Optional[_Union[IndexingMetadataStats.OperationType, str]] = ..., histogram_vec: _Optional[_Iterable[_Union[IndexingMetadataStats.HistogramSketch, _Mapping]]] = ..., volume_name: _Optional[str] = ...) -> None: ...

class RangeUsage(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUseClosedRanges: _ClassVar[RangeUsage.Type]
        kUseOpenRanges: _ClassVar[RangeUsage.Type]
        kDisabled: _ClassVar[RangeUsage.Type]
    kUseClosedRanges: RangeUsage.Type
    kUseOpenRanges: RangeUsage.Type
    kDisabled: RangeUsage.Type
    def __init__(self) -> None: ...

class ConsumePubSubDataArg(_message.Message):
    __slots__ = ("topic", "consumer_group_id")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    topic: str
    consumer_group_id: int
    def __init__(self, topic: _Optional[str] = ..., consumer_group_id: _Optional[int] = ...) -> None: ...

class ConsumePubSubDataResult(_message.Message):
    __slots__ = ("consumed_data_vec",)
    CONSUMED_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    consumed_data_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, consumed_data_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ApplyTagsArg(_message.Message):
    __slots__ = ("object_id", "tags_to_be_added_vec", "document_ids_vec", "job_instance_ids_vec", "tenant_id", "entity_id", "entity_uuid", "job_run_start_time_vec")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_TO_BE_ADDED_VEC_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_VEC_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    tags_to_be_added_vec: _containers.RepeatedScalarFieldContainer[str]
    document_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    job_instance_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    tenant_id: str
    entity_id: _entity_pb2.EntityProto
    entity_uuid: str
    job_run_start_time_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., tags_to_be_added_vec: _Optional[_Iterable[str]] = ..., document_ids_vec: _Optional[_Iterable[str]] = ..., job_instance_ids_vec: _Optional[_Iterable[int]] = ..., tenant_id: _Optional[str] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_uuid: _Optional[str] = ..., job_run_start_time_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ApplyTagsResult(_message.Message):
    __slots__ = ("error", "doc_errors")
    class DocErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DOC_ERRORS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    doc_errors: _containers.MessageMap[str, _error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., doc_errors: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ...) -> None: ...

class RemoveTagsArg(_message.Message):
    __slots__ = ("object_id", "tags_to_be_removed_vec", "document_ids_vec", "job_instance_ids_vec", "tenant_id", "entity_id", "entity_uuid", "job_run_start_time_vec")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_TO_BE_REMOVED_VEC_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_VEC_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    tags_to_be_removed_vec: _containers.RepeatedScalarFieldContainer[str]
    document_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    job_instance_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    tenant_id: str
    entity_id: _entity_pb2.EntityProto
    entity_uuid: str
    job_run_start_time_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., tags_to_be_removed_vec: _Optional[_Iterable[str]] = ..., document_ids_vec: _Optional[_Iterable[str]] = ..., job_instance_ids_vec: _Optional[_Iterable[int]] = ..., tenant_id: _Optional[str] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_uuid: _Optional[str] = ..., job_run_start_time_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class RemoveTagsResult(_message.Message):
    __slots__ = ("error", "doc_errors")
    class DocErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DOC_ERRORS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    doc_errors: _containers.MessageMap[str, _error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., doc_errors: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ...) -> None: ...

class CreateTagArg(_message.Message):
    __slots__ = ("tag", "tenant_id")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tag: _tag_db_pb2.Tag
    tenant_id: str
    def __init__(self, tag: _Optional[_Union[_tag_db_pb2.Tag, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CreateTagResult(_message.Message):
    __slots__ = ("error", "uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uuid: _Optional[str] = ...) -> None: ...

class UpdateTagArg(_message.Message):
    __slots__ = ("tag", "tenant_id")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tag: _tag_db_pb2.Tag
    tenant_id: str
    def __init__(self, tag: _Optional[_Union[_tag_db_pb2.Tag, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class UpdateTagResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteTagArg(_message.Message):
    __slots__ = ("uuid", "tenant_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    tenant_id: str
    def __init__(self, uuid: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class DeleteTagResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetTagsArg(_message.Message):
    __slots__ = ("tag_vec", "tag_namespace_vec", "tenant_id_vec", "show_inactive", "uuid_vec")
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_NAMESPACE_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOW_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    tag_vec: _containers.RepeatedScalarFieldContainer[str]
    tag_namespace_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    show_inactive: bool
    uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag_vec: _Optional[_Iterable[str]] = ..., tag_namespace_vec: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., show_inactive: bool = ..., uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTagsResult(_message.Message):
    __slots__ = ("error", "tag_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    tag_vec: _containers.RepeatedCompositeFieldContainer[_tag_db_pb2.Tag]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tag_vec: _Optional[_Iterable[_Union[_tag_db_pb2.Tag, _Mapping]]] = ...) -> None: ...

class GlobalEntityTagsImageUpdate(_message.Message):
    __slots__ = ("uuid", "tag_uuid_vec", "snapshot_tag_vec")
    class SnapshotTag(_message.Message):
        __slots__ = ("tag_uuid", "run_uuid_vec")
        TAG_UUID_FIELD_NUMBER: _ClassVar[int]
        RUN_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
        tag_uuid: str
        run_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, tag_uuid: _Optional[str] = ..., run_uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    TAG_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    tag_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_tag_vec: _containers.RepeatedCompositeFieldContainer[GlobalEntityTagsImageUpdate.SnapshotTag]
    def __init__(self, uuid: _Optional[str] = ..., tag_uuid_vec: _Optional[_Iterable[str]] = ..., snapshot_tag_vec: _Optional[_Iterable[_Union[GlobalEntityTagsImageUpdate.SnapshotTag, _Mapping]]] = ...) -> None: ...

class GcEntityTagsArg(_message.Message):
    __slots__ = ("tags_to_gc_vec",)
    TAGS_TO_GC_VEC_FIELD_NUMBER: _ClassVar[int]
    tags_to_gc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags_to_gc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class TagUpdate(_message.Message):
    __slots__ = ("type", "apply_tags_arg", "remove_tags_arg", "image_update_arg", "tag")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApplyTags: _ClassVar[TagUpdate.Type]
        kRemoveTags: _ClassVar[TagUpdate.Type]
        kGlobalEntityTagsImage: _ClassVar[TagUpdate.Type]
        kTagMetadata: _ClassVar[TagUpdate.Type]
    kApplyTags: TagUpdate.Type
    kRemoveTags: TagUpdate.Type
    kGlobalEntityTagsImage: TagUpdate.Type
    kTagMetadata: TagUpdate.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLY_TAGS_ARG_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TAGS_ARG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    type: TagUpdate.Type
    apply_tags_arg: ApplyTagsArg
    remove_tags_arg: RemoveTagsArg
    image_update_arg: GlobalEntityTagsImageUpdate
    tag: _tag_db_pb2.Tag
    def __init__(self, type: _Optional[_Union[TagUpdate.Type, str]] = ..., apply_tags_arg: _Optional[_Union[ApplyTagsArg, _Mapping]] = ..., remove_tags_arg: _Optional[_Union[RemoveTagsArg, _Mapping]] = ..., image_update_arg: _Optional[_Union[GlobalEntityTagsImageUpdate, _Mapping]] = ..., tag: _Optional[_Union[_tag_db_pb2.Tag, _Mapping]] = ...) -> None: ...

class TenantObjectDbCheckpoint(_message.Message):
    __slots__ = ("export_cookie", "cur_export_id", "last_checkpointed_objectdb_row_key")
    EXPORT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CUR_EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKPOINTED_OBJECTDB_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    export_cookie: bytes
    cur_export_id: str
    last_checkpointed_objectdb_row_key: str
    def __init__(self, export_cookie: _Optional[bytes] = ..., cur_export_id: _Optional[str] = ..., last_checkpointed_objectdb_row_key: _Optional[str] = ...) -> None: ...

class LatestObjectDbExport(_message.Message):
    __slots__ = ("status", "export_id")
    class ExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[LatestObjectDbExport.ExportStatus]
        kSuccess: _ClassVar[LatestObjectDbExport.ExportStatus]
        kFailed: _ClassVar[LatestObjectDbExport.ExportStatus]
        kInvalid: _ClassVar[LatestObjectDbExport.ExportStatus]
    kInProgress: LatestObjectDbExport.ExportStatus
    kSuccess: LatestObjectDbExport.ExportStatus
    kFailed: LatestObjectDbExport.ExportStatus
    kInvalid: LatestObjectDbExport.ExportStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    status: LatestObjectDbExport.ExportStatus
    export_id: str
    def __init__(self, status: _Optional[_Union[LatestObjectDbExport.ExportStatus, str]] = ..., export_id: _Optional[str] = ...) -> None: ...

class TenantVersionRecord(_message.Message):
    __slots__ = ("cur_version", "prev_version", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVersionUpdated: _ClassVar[TenantVersionRecord.Status]
        kVersionFinalized: _ClassVar[TenantVersionRecord.Status]
    kVersionUpdated: TenantVersionRecord.Status
    kVersionFinalized: TenantVersionRecord.Status
    CUR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PREV_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    cur_version: int
    prev_version: int
    status: TenantVersionRecord.Status
    def __init__(self, cur_version: _Optional[int] = ..., prev_version: _Optional[int] = ..., status: _Optional[_Union[TenantVersionRecord.Status, str]] = ...) -> None: ...

class TenantCloudConfig(_message.Message):
    __slots__ = ("tenant_id", "region", "es_fqdn", "s3_bucket_name", "s3_prefix", "es_iam_role_arn", "s3_iam_role_arn", "tenant_migration_intent", "azure_config", "is_migrated", "version_record", "init_status", "tenant_deletion_intent", "objectdb_checkpoint", "latest_export_id_status", "objectdb_import_checkpoint", "latest_import_id_status")
    class InitStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TenantCloudConfig.InitStatus]
        kDshmUpdated: _ClassVar[TenantCloudConfig.InitStatus]
        kS3VersionUpdated: _ClassVar[TenantCloudConfig.InitStatus]
        kVersionFinalized: _ClassVar[TenantCloudConfig.InitStatus]
    kStarted: TenantCloudConfig.InitStatus
    kDshmUpdated: TenantCloudConfig.InitStatus
    kS3VersionUpdated: TenantCloudConfig.InitStatus
    kVersionFinalized: TenantCloudConfig.InitStatus
    class TenantMigrationIntent(_message.Message):
        __slots__ = ("migration_status", "object_id_key_to_partition_id_map")
        class MigrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNotStarted: _ClassVar[TenantCloudConfig.TenantMigrationIntent.MigrationStatus]
            kInProgress: _ClassVar[TenantCloudConfig.TenantMigrationIntent.MigrationStatus]
            kCompleted: _ClassVar[TenantCloudConfig.TenantMigrationIntent.MigrationStatus]
        kNotStarted: TenantCloudConfig.TenantMigrationIntent.MigrationStatus
        kInProgress: TenantCloudConfig.TenantMigrationIntent.MigrationStatus
        kCompleted: TenantCloudConfig.TenantMigrationIntent.MigrationStatus
        class ObjectIdKeyToPartitionIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_KEY_TO_PARTITION_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        migration_status: TenantCloudConfig.TenantMigrationIntent.MigrationStatus
        object_id_key_to_partition_id_map: _containers.ScalarMap[str, int]
        def __init__(self, migration_status: _Optional[_Union[TenantCloudConfig.TenantMigrationIntent.MigrationStatus, str]] = ..., object_id_key_to_partition_id_map: _Optional[_Mapping[str, int]] = ...) -> None: ...
    class AzureCloudConfig(_message.Message):
        __slots__ = ("vault_url", "client_id", "secret_name", "container_name", "storage_account_name")
        VAULT_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        vault_url: str
        client_id: str
        secret_name: str
        container_name: str
        storage_account_name: str
        def __init__(self, vault_url: _Optional[str] = ..., client_id: _Optional[str] = ..., secret_name: _Optional[str] = ..., container_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ...) -> None: ...
    class TenantDeletionIntent(_message.Message):
        __slots__ = ("deletion_status", "object_id_key_to_partition_id_map")
        class DeletionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNotStarted: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kStarted: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kObjDbCleaned: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kIndexDeleted: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kS3Deleted: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kAuxDbCleaned: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
            kCompleted: _ClassVar[TenantCloudConfig.TenantDeletionIntent.DeletionStatus]
        kNotStarted: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kStarted: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kObjDbCleaned: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kIndexDeleted: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kS3Deleted: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kAuxDbCleaned: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        kCompleted: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        class ObjectIdKeyToPartitionIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        DELETION_STATUS_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_KEY_TO_PARTITION_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        deletion_status: TenantCloudConfig.TenantDeletionIntent.DeletionStatus
        object_id_key_to_partition_id_map: _containers.ScalarMap[str, int]
        def __init__(self, deletion_status: _Optional[_Union[TenantCloudConfig.TenantDeletionIntent.DeletionStatus, str]] = ..., object_id_key_to_partition_id_map: _Optional[_Mapping[str, int]] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ES_FQDN_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ES_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    S3_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    TENANT_MIGRATION_INTENT_FIELD_NUMBER: _ClassVar[int]
    AZURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    VERSION_RECORD_FIELD_NUMBER: _ClassVar[int]
    INIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_DELETION_INTENT_FIELD_NUMBER: _ClassVar[int]
    OBJECTDB_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPORT_ID_STATUS_FIELD_NUMBER: _ClassVar[int]
    OBJECTDB_IMPORT_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_IMPORT_ID_STATUS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    region: str
    es_fqdn: str
    s3_bucket_name: str
    s3_prefix: str
    es_iam_role_arn: str
    s3_iam_role_arn: str
    tenant_migration_intent: TenantCloudConfig.TenantMigrationIntent
    azure_config: TenantCloudConfig.AzureCloudConfig
    is_migrated: bool
    version_record: TenantVersionRecord
    init_status: TenantCloudConfig.InitStatus
    tenant_deletion_intent: TenantCloudConfig.TenantDeletionIntent
    objectdb_checkpoint: TenantObjectDbCheckpoint
    latest_export_id_status: LatestObjectDbExport
    objectdb_import_checkpoint: TenantObjectDbCheckpoint
    latest_import_id_status: LatestObjectDbExport
    def __init__(self, tenant_id: _Optional[str] = ..., region: _Optional[str] = ..., es_fqdn: _Optional[str] = ..., s3_bucket_name: _Optional[str] = ..., s3_prefix: _Optional[str] = ..., es_iam_role_arn: _Optional[str] = ..., s3_iam_role_arn: _Optional[str] = ..., tenant_migration_intent: _Optional[_Union[TenantCloudConfig.TenantMigrationIntent, _Mapping]] = ..., azure_config: _Optional[_Union[TenantCloudConfig.AzureCloudConfig, _Mapping]] = ..., is_migrated: bool = ..., version_record: _Optional[_Union[TenantVersionRecord, _Mapping]] = ..., init_status: _Optional[_Union[TenantCloudConfig.InitStatus, str]] = ..., tenant_deletion_intent: _Optional[_Union[TenantCloudConfig.TenantDeletionIntent, _Mapping]] = ..., objectdb_checkpoint: _Optional[_Union[TenantObjectDbCheckpoint, _Mapping]] = ..., latest_export_id_status: _Optional[_Union[LatestObjectDbExport, _Mapping]] = ..., objectdb_import_checkpoint: _Optional[_Union[TenantObjectDbCheckpoint, _Mapping]] = ..., latest_import_id_status: _Optional[_Union[LatestObjectDbExport, _Mapping]] = ...) -> None: ...

class AddTenantCloudConfigResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ESMigrationWork(_message.Message):
    __slots__ = ("index_name", "task_id", "control_item_type", "retry_count")
    class ControlItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInitiator: _ClassVar[ESMigrationWork.ControlItemType]
        kAccumulator: _ClassVar[ESMigrationWork.ControlItemType]
        kVerifier: _ClassVar[ESMigrationWork.ControlItemType]
        kFinisher: _ClassVar[ESMigrationWork.ControlItemType]
    kInitiator: ESMigrationWork.ControlItemType
    kAccumulator: ESMigrationWork.ControlItemType
    kVerifier: ESMigrationWork.ControlItemType
    kFinisher: ESMigrationWork.ControlItemType
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    task_id: str
    control_item_type: ESMigrationWork.ControlItemType
    retry_count: int
    def __init__(self, index_name: _Optional[str] = ..., task_id: _Optional[str] = ..., control_item_type: _Optional[_Union[ESMigrationWork.ControlItemType, str]] = ..., retry_count: _Optional[int] = ...) -> None: ...

class RemoveVersionsFromIndexArg(_message.Message):
    __slots__ = ("object_id", "instance_id_vec", "cluster_partition_id", "tenant_id", "mails_identifier", "files_identifier")
    class MailsIdentifier(_message.Message):
        __slots__ = ("folder_key", "item_key")
        FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        ITEM_KEY_FIELD_NUMBER: _ClassVar[int]
        folder_key: str
        item_key: str
        def __init__(self, folder_key: _Optional[str] = ..., item_key: _Optional[str] = ...) -> None: ...
    class FilesIdentifier(_message.Message):
        __slots__ = ("path",)
        PATH_FIELD_NUMBER: _ClassVar[int]
        path: str
        def __init__(self, path: _Optional[str] = ...) -> None: ...
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MAILS_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FILES_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    cluster_partition_id: int
    tenant_id: str
    mails_identifier: _containers.RepeatedCompositeFieldContainer[RemoveVersionsFromIndexArg.MailsIdentifier]
    files_identifier: _containers.RepeatedCompositeFieldContainer[RemoveVersionsFromIndexArg.FilesIdentifier]
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., cluster_partition_id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., mails_identifier: _Optional[_Iterable[_Union[RemoveVersionsFromIndexArg.MailsIdentifier, _Mapping]]] = ..., files_identifier: _Optional[_Iterable[_Union[RemoveVersionsFromIndexArg.FilesIdentifier, _Mapping]]] = ...) -> None: ...

class RemoveVersionsFromIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
