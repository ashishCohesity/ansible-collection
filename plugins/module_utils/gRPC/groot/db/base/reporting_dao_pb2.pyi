from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentTypeDao(_message.Message):
    __slots__ = ("env_id", "env_name")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_NAME_FIELD_NUMBER: _ClassVar[int]
    env_id: int
    env_name: str
    def __init__(self, env_id: _Optional[int] = ..., env_name: _Optional[str] = ...) -> None: ...

class JobStatusTypeDao(_message.Message):
    __slots__ = ("job_status_id", "job_status_name")
    JOB_STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    job_status_id: int
    job_status_name: str
    def __init__(self, job_status_id: _Optional[int] = ..., job_status_name: _Optional[str] = ...) -> None: ...

class JobStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActive: _ClassVar[JobStatus.Type]
        kPaused: _ClassVar[JobStatus.Type]
        kDeleted: _ClassVar[JobStatus.Type]
        kInActive: _ClassVar[JobStatus.Type]
    kActive: JobStatus.Type
    kPaused: JobStatus.Type
    kDeleted: JobStatus.Type
    kInActive: JobStatus.Type
    def __init__(self) -> None: ...

class BackupJobDao(_message.Message):
    __slots__ = ("job_id", "cluster_id", "cluster_incarnation_id", "job_uid_job_id", "job_name", "job_env_type", "source_env_type", "job_status", "creation_time_usecs", "last_modified_time_usecs", "policy", "tenant_id", "is_replication_rx_job")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REPLICATION_RX_JOB_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    cluster_id: int
    cluster_incarnation_id: int
    job_uid_job_id: int
    job_name: str
    job_env_type: EnvironmentTypeDao
    source_env_type: EnvironmentTypeDao
    job_status: JobStatusTypeDao
    creation_time_usecs: int
    last_modified_time_usecs: int
    policy: ProtectionPolicyDao
    tenant_id: str
    is_replication_rx_job: bool
    def __init__(self, job_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., job_uid_job_id: _Optional[int] = ..., job_name: _Optional[str] = ..., job_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., source_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., job_status: _Optional[_Union[JobStatusTypeDao, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., last_modified_time_usecs: _Optional[int] = ..., policy: _Optional[_Union[ProtectionPolicyDao, _Mapping]] = ..., tenant_id: _Optional[str] = ..., is_replication_rx_job: bool = ...) -> None: ...

class RegisteredSourceDao(_message.Message):
    __slots__ = ("source_id", "source_name", "source_env_type", "registration_time_usecs", "last_refresh_time_usecs", "is_registered", "tenant_id")
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    source_id: int
    source_name: str
    source_env_type: EnvironmentTypeDao
    registration_time_usecs: int
    last_refresh_time_usecs: int
    is_registered: bool
    tenant_id: str
    def __init__(self, source_id: _Optional[int] = ..., source_name: _Optional[str] = ..., source_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., registration_time_usecs: _Optional[int] = ..., last_refresh_time_usecs: _Optional[int] = ..., is_registered: bool = ..., tenant_id: _Optional[str] = ...) -> None: ...

class LeafEntityDao(_message.Message):
    __slots__ = ("entity_id", "entity_name", "entity_env_type", "parent", "is_protected", "is_deleted", "logical_size_in_bytes")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    entity_name: str
    entity_env_type: EnvironmentTypeDao
    parent: RegisteredSourceDao
    is_protected: bool
    is_deleted: bool
    logical_size_in_bytes: int
    def __init__(self, entity_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., entity_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., parent: _Optional[_Union[RegisteredSourceDao, _Mapping]] = ..., is_protected: bool = ..., is_deleted: bool = ..., logical_size_in_bytes: _Optional[int] = ...) -> None: ...

class JobEntityDao(_message.Message):
    __slots__ = ("job_id", "entity_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    entity_id: int
    def __init__(self, job_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...

class ArchivalTargetTypeDao(_message.Message):
    __slots__ = ("type_id", "type_name")
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    type_name: str
    def __init__(self, type_id: _Optional[int] = ..., type_name: _Optional[str] = ...) -> None: ...

class ArchivalTargetDao(_message.Message):
    __slots__ = ("target_id", "target_name", "cluster_id", "cluster_incarnation_id", "archival_target_type", "creation_time_usecs", "last_update_time_usecs", "logical_data_transferred_bytes", "physical_data_transferred_bytes", "archival_usage_bytes", "tiering_usage_bytes", "is_deleted")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_DATA_TRANSFERRED_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_DATA_TRANSFERRED_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIERING_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    target_name: str
    cluster_id: int
    cluster_incarnation_id: int
    archival_target_type: ArchivalTargetTypeDao
    creation_time_usecs: int
    last_update_time_usecs: int
    logical_data_transferred_bytes: int
    physical_data_transferred_bytes: int
    archival_usage_bytes: int
    tiering_usage_bytes: int
    is_deleted: bool
    def __init__(self, target_id: _Optional[int] = ..., target_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., archival_target_type: _Optional[_Union[ArchivalTargetTypeDao, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ..., logical_data_transferred_bytes: _Optional[int] = ..., physical_data_transferred_bytes: _Optional[int] = ..., archival_usage_bytes: _Optional[int] = ..., tiering_usage_bytes: _Optional[int] = ..., is_deleted: bool = ...) -> None: ...

class ClusterDao(_message.Message):
    __slots__ = ("cluster_id", "cluster_name", "creation_time_usecs", "software_version", "hardware_models", "is_encryption_enabled", "cluster_capacity_bytes", "physical_usage_bytes", "timezone", "product_models", "min_usable_physical_capacity_bytes", "raw_capacity_bytes")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODELS_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_MODELS_FIELD_NUMBER: _ClassVar[int]
    MIN_USABLE_PHYSICAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    RAW_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_name: str
    creation_time_usecs: int
    software_version: str
    hardware_models: str
    is_encryption_enabled: bool
    cluster_capacity_bytes: int
    physical_usage_bytes: int
    timezone: str
    product_models: str
    min_usable_physical_capacity_bytes: int
    raw_capacity_bytes: int
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., creation_time_usecs: _Optional[int] = ..., software_version: _Optional[str] = ..., hardware_models: _Optional[str] = ..., is_encryption_enabled: bool = ..., cluster_capacity_bytes: _Optional[int] = ..., physical_usage_bytes: _Optional[int] = ..., timezone: _Optional[str] = ..., product_models: _Optional[str] = ..., min_usable_physical_capacity_bytes: _Optional[int] = ..., raw_capacity_bytes: _Optional[int] = ...) -> None: ...

class PartitionDao(_message.Message):
    __slots__ = ("partition_id", "partition_name", "cluster_id", "host_name", "virtual_ips", "vlan_ips")
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_IPS_FIELD_NUMBER: _ClassVar[int]
    VLAN_IPS_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    partition_name: str
    cluster_id: int
    host_name: str
    virtual_ips: str
    vlan_ips: str
    def __init__(self, partition_id: _Optional[int] = ..., partition_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., host_name: _Optional[str] = ..., virtual_ips: _Optional[str] = ..., vlan_ips: _Optional[str] = ...) -> None: ...

class RackDao(_message.Message):
    __slots__ = ("rack_id", "rack_name", "location")
    RACK_ID_FIELD_NUMBER: _ClassVar[int]
    RACK_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    rack_id: int
    rack_name: str
    location: bytes
    def __init__(self, rack_id: _Optional[int] = ..., rack_name: _Optional[str] = ..., location: _Optional[bytes] = ...) -> None: ...

class ChassisDao(_message.Message):
    __slots__ = ("chassis_id", "chassis_name", "rack_dao", "location", "hardware_model")
    CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_NAME_FIELD_NUMBER: _ClassVar[int]
    RACK_DAO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    chassis_id: int
    chassis_name: str
    rack_dao: RackDao
    location: bytes
    hardware_model: str
    def __init__(self, chassis_id: _Optional[int] = ..., chassis_name: _Optional[str] = ..., rack_dao: _Optional[_Union[RackDao, _Mapping]] = ..., location: _Optional[bytes] = ..., hardware_model: _Optional[str] = ...) -> None: ...

class RemovalStatus(_message.Message):
    __slots__ = ("status_id", "status_name")
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    status_id: int
    status_name: str
    def __init__(self, status_id: _Optional[int] = ..., status_name: _Optional[str] = ...) -> None: ...

class NodeDao(_message.Message):
    __slots__ = ("node_id", "partition_dao", "node_ip", "software_version", "status", "chassis_dao", "hardware_model", "product_model")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DAO_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_DAO_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    partition_dao: PartitionDao
    node_ip: str
    software_version: str
    status: RemovalStatus
    chassis_dao: ChassisDao
    hardware_model: str
    product_model: str
    def __init__(self, node_id: _Optional[int] = ..., partition_dao: _Optional[_Union[PartitionDao, _Mapping]] = ..., node_ip: _Optional[str] = ..., software_version: _Optional[str] = ..., status: _Optional[_Union[RemovalStatus, _Mapping]] = ..., chassis_dao: _Optional[_Union[ChassisDao, _Mapping]] = ..., hardware_model: _Optional[str] = ..., product_model: _Optional[str] = ...) -> None: ...

class ViewBoxDao(_message.Message):
    __slots__ = ("view_box_id", "view_box_name", "partition_dao", "redundancy_type", "deduplication_type", "compression_type", "is_deduplication_enabled", "is_cloud_tiering_enabled", "is_deleted")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DAO_FIELD_NUMBER: _ClassVar[int]
    REDUNDANCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DEDUPLICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_TIERING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    view_box_name: str
    partition_dao: PartitionDao
    redundancy_type: str
    deduplication_type: str
    compression_type: str
    is_deduplication_enabled: bool
    is_cloud_tiering_enabled: bool
    is_deleted: bool
    def __init__(self, view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ..., partition_dao: _Optional[_Union[PartitionDao, _Mapping]] = ..., redundancy_type: _Optional[str] = ..., deduplication_type: _Optional[str] = ..., compression_type: _Optional[str] = ..., is_deduplication_enabled: bool = ..., is_cloud_tiering_enabled: bool = ..., is_deleted: bool = ...) -> None: ...

class ViewAccessProtocolDao(_message.Message):
    __slots__ = ("access_protocol_id", "access_protocol_type")
    ACCESS_PROTOCOL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROTOCOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_protocol_id: int
    access_protocol_type: str
    def __init__(self, access_protocol_id: _Optional[int] = ..., access_protocol_type: _Optional[str] = ...) -> None: ...

class ViewDataLockDao(_message.Message):
    __slots__ = ("data_lock_id", "data_lock_type")
    DATA_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
    data_lock_id: int
    data_lock_type: str
    def __init__(self, data_lock_id: _Optional[int] = ..., data_lock_type: _Optional[str] = ...) -> None: ...

class ViewDao(_message.Message):
    __slots__ = ("view_id", "view_name", "view_box_id", "cluster_id", "cluster_incarnation_id", "logical_usage_bytes", "logical_quota_bytes", "deduplication_type", "qos_policy", "access_protocol", "nfs_mount_path", "smb_mount_path", "is_deleted", "tenant_id", "s3_mount_path", "data_lock")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_QUOTA_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    QOS_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    S3_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_name: str
    view_box_id: int
    cluster_id: int
    cluster_incarnation_id: int
    logical_usage_bytes: int
    logical_quota_bytes: int
    deduplication_type: str
    qos_policy: str
    access_protocol: ViewAccessProtocolDao
    nfs_mount_path: str
    smb_mount_path: str
    is_deleted: bool
    tenant_id: str
    s3_mount_path: str
    data_lock: ViewDataLockDao
    def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., logical_usage_bytes: _Optional[int] = ..., logical_quota_bytes: _Optional[int] = ..., deduplication_type: _Optional[str] = ..., qos_policy: _Optional[str] = ..., access_protocol: _Optional[_Union[ViewAccessProtocolDao, _Mapping]] = ..., nfs_mount_path: _Optional[str] = ..., smb_mount_path: _Optional[str] = ..., is_deleted: bool = ..., tenant_id: _Optional[str] = ..., s3_mount_path: _Optional[str] = ..., data_lock: _Optional[_Union[ViewDataLockDao, _Mapping]] = ...) -> None: ...

class ViewAliasDao(_message.Message):
    __slots__ = ("alias_name", "view_id", "cluster_id", "cluster_incarnation_id", "view_path", "is_deleted")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    view_id: int
    cluster_id: int
    cluster_incarnation_id: int
    view_path: str
    is_deleted: bool
    def __init__(self, alias_name: _Optional[str] = ..., view_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., view_path: _Optional[str] = ..., is_deleted: bool = ...) -> None: ...

class JobRunStatusDao(_message.Message):
    __slots__ = ("status_id", "status_name")
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    status_id: int
    status_name: str
    def __init__(self, status_id: _Optional[int] = ..., status_name: _Optional[str] = ...) -> None: ...

class JobRunBasicInfoDao(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "job_id", "job_run_id", "parent_source_id", "view_box_id")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    job_id: int
    job_run_id: int
    parent_source_id: int
    view_box_id: int
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., parent_source_id: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class JobRunDao(_message.Message):
    __slots__ = ("basic_info", "start_time_usecs", "duration_usecs", "end_time_usecs", "is_full_backup", "sla_violated", "status", "error_msg", "total_num_entities", "success_num_entities", "failure_num_entities", "source_logical_size_bytes", "source_delta_size_bytes", "data_written_size_bytes", "snapshot_expiry_time_usecs", "legal_hold")
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    basic_info: JobRunBasicInfoDao
    start_time_usecs: int
    duration_usecs: int
    end_time_usecs: int
    is_full_backup: bool
    sla_violated: bool
    status: JobRunStatusDao
    error_msg: str
    total_num_entities: int
    success_num_entities: int
    failure_num_entities: int
    source_logical_size_bytes: int
    source_delta_size_bytes: int
    data_written_size_bytes: int
    snapshot_expiry_time_usecs: int
    legal_hold: bool
    def __init__(self, basic_info: _Optional[_Union[JobRunBasicInfoDao, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., is_full_backup: bool = ..., sla_violated: bool = ..., status: _Optional[_Union[JobRunStatusDao, _Mapping]] = ..., error_msg: _Optional[str] = ..., total_num_entities: _Optional[int] = ..., success_num_entities: _Optional[int] = ..., failure_num_entities: _Optional[int] = ..., source_logical_size_bytes: _Optional[int] = ..., source_delta_size_bytes: _Optional[int] = ..., data_written_size_bytes: _Optional[int] = ..., snapshot_expiry_time_usecs: _Optional[int] = ..., legal_hold: bool = ...) -> None: ...

class JobRunEntityDao(_message.Message):
    __slots__ = ("basic_info", "task_id", "start_time_usecs", "duration_usecs", "end_time_usecs", "entity_id", "entity_env_type", "is_full_backup", "status", "source_logical_size_bytes", "source_delta_size_bytes", "data_written_size_bytes", "is_latest_attempt", "admitted_time_usecs", "permit_grant_time_usecs")
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_LATEST_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ADMITTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_GRANT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    basic_info: JobRunBasicInfoDao
    task_id: int
    start_time_usecs: int
    duration_usecs: int
    end_time_usecs: int
    entity_id: int
    entity_env_type: EnvironmentTypeDao
    is_full_backup: bool
    status: JobRunStatusDao
    source_logical_size_bytes: int
    source_delta_size_bytes: int
    data_written_size_bytes: int
    is_latest_attempt: bool
    admitted_time_usecs: int
    permit_grant_time_usecs: int
    def __init__(self, basic_info: _Optional[_Union[JobRunBasicInfoDao, _Mapping]] = ..., task_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., entity_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., is_full_backup: bool = ..., status: _Optional[_Union[JobRunStatusDao, _Mapping]] = ..., source_logical_size_bytes: _Optional[int] = ..., source_delta_size_bytes: _Optional[int] = ..., data_written_size_bytes: _Optional[int] = ..., is_latest_attempt: bool = ..., admitted_time_usecs: _Optional[int] = ..., permit_grant_time_usecs: _Optional[int] = ...) -> None: ...

class JobRunReplicationDao(_message.Message):
    __slots__ = ("basic_info", "task_id", "start_time_usecs", "duration_usecs", "end_time_usecs", "remote_cluster_id", "status", "logical_size_bytes_transferred", "physical_size_bytes_transferred", "snapshot_expiry_time_usecs")
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    basic_info: JobRunBasicInfoDao
    task_id: int
    start_time_usecs: int
    duration_usecs: int
    end_time_usecs: int
    remote_cluster_id: int
    status: JobRunStatusDao
    logical_size_bytes_transferred: int
    physical_size_bytes_transferred: int
    snapshot_expiry_time_usecs: int
    def __init__(self, basic_info: _Optional[_Union[JobRunBasicInfoDao, _Mapping]] = ..., task_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., remote_cluster_id: _Optional[int] = ..., status: _Optional[_Union[JobRunStatusDao, _Mapping]] = ..., logical_size_bytes_transferred: _Optional[int] = ..., physical_size_bytes_transferred: _Optional[int] = ..., snapshot_expiry_time_usecs: _Optional[int] = ...) -> None: ...

class JobRunReplicationEntityDao(_message.Message):
    __slots__ = ("basic_info", "task_id", "start_time_usecs", "duration_usecs", "end_time_usecs", "remote_cluster_id", "entity_id", "entity_env_type", "status", "logical_size_bytes_transferred", "physical_size_bytes_transferred")
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    basic_info: JobRunBasicInfoDao
    task_id: int
    start_time_usecs: int
    duration_usecs: int
    end_time_usecs: int
    remote_cluster_id: int
    entity_id: int
    entity_env_type: EnvironmentTypeDao
    status: JobRunStatusDao
    logical_size_bytes_transferred: int
    physical_size_bytes_transferred: int
    def __init__(self, basic_info: _Optional[_Union[JobRunBasicInfoDao, _Mapping]] = ..., task_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., remote_cluster_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., entity_env_type: _Optional[_Union[EnvironmentTypeDao, _Mapping]] = ..., status: _Optional[_Union[JobRunStatusDao, _Mapping]] = ..., logical_size_bytes_transferred: _Optional[int] = ..., physical_size_bytes_transferred: _Optional[int] = ...) -> None: ...

class JobRunArchivalDao(_message.Message):
    __slots__ = ("basic_info", "task_id", "start_time_usecs", "duration_usecs", "end_time_usecs", "vault_id", "status", "is_full_archive", "archive_job_size_bytes", "logical_size_bytes_transferred", "physical_size_bytes_transferred", "run_start_time_usecs", "snapshot_expiry_time_usecs")
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_JOB_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    basic_info: JobRunBasicInfoDao
    task_id: int
    start_time_usecs: int
    duration_usecs: int
    end_time_usecs: int
    vault_id: int
    status: JobRunStatusDao
    is_full_archive: bool
    archive_job_size_bytes: int
    logical_size_bytes_transferred: int
    physical_size_bytes_transferred: int
    run_start_time_usecs: int
    snapshot_expiry_time_usecs: int
    def __init__(self, basic_info: _Optional[_Union[JobRunBasicInfoDao, _Mapping]] = ..., task_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., vault_id: _Optional[int] = ..., status: _Optional[_Union[JobRunStatusDao, _Mapping]] = ..., is_full_archive: bool = ..., archive_job_size_bytes: _Optional[int] = ..., logical_size_bytes_transferred: _Optional[int] = ..., physical_size_bytes_transferred: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., snapshot_expiry_time_usecs: _Optional[int] = ...) -> None: ...

class RestoreTypeDao(_message.Message):
    __slots__ = ("restore_type_id", "restore_type_name")
    RESTORE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    restore_type_id: int
    restore_type_name: str
    def __init__(self, restore_type_id: _Optional[int] = ..., restore_type_name: _Optional[str] = ...) -> None: ...

class RestoreStatusDao(_message.Message):
    __slots__ = ("status_id", "status_name")
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    status_id: int
    status_name: str
    def __init__(self, status_id: _Optional[int] = ..., status_name: _Optional[str] = ...) -> None: ...

class RestoreSourceTypeDao(_message.Message):
    __slots__ = ("source_type_id", "source_type_name")
    SOURCE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    source_type_id: int
    source_type_name: str
    def __init__(self, source_type_id: _Optional[int] = ..., source_type_name: _Optional[str] = ...) -> None: ...

class RestoredObjectDao(_message.Message):
    __slots__ = ("entity_id", "cluster_id", "cluster_incarnation_id", "protection_job_id", "protection_job_run_id", "restore_task_id", "restore_task_name", "restore_type", "start_time_usecs", "end_time_usecs", "status", "tenant_id", "restore_source_type")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    cluster_id: int
    cluster_incarnation_id: int
    protection_job_id: int
    protection_job_run_id: int
    restore_task_id: int
    restore_task_name: str
    restore_type: RestoreTypeDao
    start_time_usecs: int
    end_time_usecs: int
    status: RestoreStatusDao
    tenant_id: str
    restore_source_type: RestoreSourceTypeDao
    def __init__(self, entity_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., protection_job_id: _Optional[int] = ..., protection_job_run_id: _Optional[int] = ..., restore_task_id: _Optional[int] = ..., restore_task_name: _Optional[str] = ..., restore_type: _Optional[_Union[RestoreTypeDao, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status: _Optional[_Union[RestoreStatusDao, _Mapping]] = ..., tenant_id: _Optional[str] = ..., restore_source_type: _Optional[_Union[RestoreSourceTypeDao, _Mapping]] = ...) -> None: ...

class RestoreTaskDao(_message.Message):
    __slots__ = ("restore_task_id", "restore_task_name", "start_time_usecs", "end_time_usecs", "status", "restore_user", "total_logical_size_bytes", "total_physical_size_bytes")
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_USER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    restore_task_id: int
    restore_task_name: str
    start_time_usecs: int
    end_time_usecs: int
    status: RestoreStatusDao
    restore_user: str
    total_logical_size_bytes: int
    total_physical_size_bytes: int
    def __init__(self, restore_task_id: _Optional[int] = ..., restore_task_name: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status: _Optional[_Union[RestoreStatusDao, _Mapping]] = ..., restore_user: _Optional[str] = ..., total_logical_size_bytes: _Optional[int] = ..., total_physical_size_bytes: _Optional[int] = ...) -> None: ...

class ClusterEntityTypeDao(_message.Message):
    __slots__ = ("entity_type_id", "entity_name")
    ENTITY_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_type_id: int
    entity_name: str
    def __init__(self, entity_type_id: _Optional[int] = ..., entity_name: _Optional[str] = ...) -> None: ...

class IOPerformanceStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "entity_type", "entity_id", "read_iops", "read_throughput_bytes_per_sec", "read_latency_msecs", "write_iops", "write_throughput_bytes_per_sec", "write_latency_msecs")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    READ_IOPS_FIELD_NUMBER: _ClassVar[int]
    READ_THROUGHPUT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    READ_LATENCY_MSECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_IOPS_FIELD_NUMBER: _ClassVar[int]
    WRITE_THROUGHPUT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_LATENCY_MSECS_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    entity_type: ClusterEntityTypeDao
    entity_id: int
    read_iops: int
    read_throughput_bytes_per_sec: int
    read_latency_msecs: int
    write_iops: int
    write_throughput_bytes_per_sec: int
    write_latency_msecs: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., entity_type: _Optional[_Union[ClusterEntityTypeDao, _Mapping]] = ..., entity_id: _Optional[int] = ..., read_iops: _Optional[int] = ..., read_throughput_bytes_per_sec: _Optional[int] = ..., read_latency_msecs: _Optional[int] = ..., write_iops: _Optional[int] = ..., write_throughput_bytes_per_sec: _Optional[int] = ..., write_latency_msecs: _Optional[int] = ...) -> None: ...

class ResourceUsageStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "entity_type", "entity_id", "cpu_usage_percent", "memory_usage_percent")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    entity_type: ClusterEntityTypeDao
    entity_id: int
    cpu_usage_percent: float
    memory_usage_percent: float
    def __init__(self, timestamp_usecs: _Optional[int] = ..., entity_type: _Optional[_Union[ClusterEntityTypeDao, _Mapping]] = ..., entity_id: _Optional[int] = ..., cpu_usage_percent: _Optional[float] = ..., memory_usage_percent: _Optional[float] = ...) -> None: ...

class StorageUsageStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "entity_type", "entity_id", "logical_size_bytes", "physical_size_bytes", "cloud_data_written_bytes", "cloud_total_physical_usage_bytes", "data_in_bytes", "data_in_bytes_after_dedup", "data_written_bytes", "local_data_written_bytes", "local_tier_resiliency_impact_bytes", "local_total_physical_usage_bytes", "outdated_logical_usage_bytes", "storage_consumed_bytes", "total_logical_usage_bytes")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_AFTER_DEDUP_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIER_RESILIENCY_IMPACT_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONSUMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    entity_type: ClusterEntityTypeDao
    entity_id: int
    logical_size_bytes: int
    physical_size_bytes: int
    cloud_data_written_bytes: int
    cloud_total_physical_usage_bytes: int
    data_in_bytes: int
    data_in_bytes_after_dedup: int
    data_written_bytes: int
    local_data_written_bytes: int
    local_tier_resiliency_impact_bytes: int
    local_total_physical_usage_bytes: int
    outdated_logical_usage_bytes: int
    storage_consumed_bytes: int
    total_logical_usage_bytes: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., entity_type: _Optional[_Union[ClusterEntityTypeDao, _Mapping]] = ..., entity_id: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., cloud_data_written_bytes: _Optional[int] = ..., cloud_total_physical_usage_bytes: _Optional[int] = ..., data_in_bytes: _Optional[int] = ..., data_in_bytes_after_dedup: _Optional[int] = ..., data_written_bytes: _Optional[int] = ..., local_data_written_bytes: _Optional[int] = ..., local_tier_resiliency_impact_bytes: _Optional[int] = ..., local_total_physical_usage_bytes: _Optional[int] = ..., outdated_logical_usage_bytes: _Optional[int] = ..., storage_consumed_bytes: _Optional[int] = ..., total_logical_usage_bytes: _Optional[int] = ...) -> None: ...

class RemoteClusterDao(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "name", "is_deleted", "tenant_id", "remote_tenant_id")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    name: str
    is_deleted: bool
    tenant_id: str
    remote_tenant_id: str
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., name: _Optional[str] = ..., is_deleted: bool = ..., tenant_id: _Optional[str] = ..., remote_tenant_id: _Optional[str] = ...) -> None: ...

class RemoteClusterViewBoxDao(_message.Message):
    __slots__ = ("local_view_box_id", "view_box_id", "view_box_name", "cluster", "is_deleted")
    LOCAL_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    local_view_box_id: int
    view_box_id: int
    view_box_name: str
    cluster: RemoteClusterDao
    is_deleted: bool
    def __init__(self, local_view_box_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ..., cluster: _Optional[_Union[RemoteClusterDao, _Mapping]] = ..., is_deleted: bool = ...) -> None: ...

class ProtectionPolicyStatusTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class SchedulePeriodicityTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleDayTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleWeekTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleDayOfYearTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleTypeDao(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ProtectionPolicyDataLockDao(_message.Message):
    __slots__ = ("data_lock_id", "data_lock_type")
    DATA_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
    data_lock_id: int
    data_lock_type: str
    def __init__(self, data_lock_id: _Optional[int] = ..., data_lock_type: _Optional[str] = ...) -> None: ...

class ProtectionPolicyDao(_message.Message):
    __slots__ = ("id", "name", "description", "status", "num_retries", "retry_delay_mins", "start_window_interval_mins", "last_modification_time_usecs", "data_lock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_MINS_FIELD_NUMBER: _ClassVar[int]
    START_WINDOW_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    status: ProtectionPolicyStatusTypeDao
    num_retries: int
    retry_delay_mins: int
    start_window_interval_mins: int
    last_modification_time_usecs: int
    data_lock: ProtectionPolicyDataLockDao
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[ProtectionPolicyStatusTypeDao, _Mapping]] = ..., num_retries: _Optional[int] = ..., retry_delay_mins: _Optional[int] = ..., start_window_interval_mins: _Optional[int] = ..., last_modification_time_usecs: _Optional[int] = ..., data_lock: _Optional[_Union[ProtectionPolicyDataLockDao, _Mapping]] = ...) -> None: ...

class BackUpScheduleDao(_message.Message):
    __slots__ = ("periodicity", "mins", "day", "week", "retention_days", "schedule_type", "policy", "year_day")
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    MINS_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    YEAR_DAY_FIELD_NUMBER: _ClassVar[int]
    periodicity: SchedulePeriodicityTypeDao
    mins: int
    day: ScheduleDayTypeDao
    week: ScheduleWeekTypeDao
    retention_days: int
    schedule_type: ScheduleTypeDao
    policy: ProtectionPolicyDao
    year_day: ScheduleDayOfYearTypeDao
    def __init__(self, periodicity: _Optional[_Union[SchedulePeriodicityTypeDao, _Mapping]] = ..., mins: _Optional[int] = ..., day: _Optional[_Union[ScheduleDayTypeDao, _Mapping]] = ..., week: _Optional[_Union[ScheduleWeekTypeDao, _Mapping]] = ..., retention_days: _Optional[int] = ..., schedule_type: _Optional[_Union[ScheduleTypeDao, _Mapping]] = ..., policy: _Optional[_Union[ProtectionPolicyDao, _Mapping]] = ..., year_day: _Optional[_Union[ScheduleDayOfYearTypeDao, _Mapping]] = ...) -> None: ...

class PolicyReplicationScheduleDao(_message.Message):
    __slots__ = ("policy", "replication_target", "periodicity", "frequency", "retention_days")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    policy: ProtectionPolicyDao
    replication_target: RemoteClusterDao
    periodicity: SchedulePeriodicityTypeDao
    frequency: int
    retention_days: int
    def __init__(self, policy: _Optional[_Union[ProtectionPolicyDao, _Mapping]] = ..., replication_target: _Optional[_Union[RemoteClusterDao, _Mapping]] = ..., periodicity: _Optional[_Union[SchedulePeriodicityTypeDao, _Mapping]] = ..., frequency: _Optional[int] = ..., retention_days: _Optional[int] = ...) -> None: ...

class PolicyArchivalScheduleDao(_message.Message):
    __slots__ = ("policy", "archival_target", "periodicity", "frequency", "retention_days")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    policy: ProtectionPolicyDao
    archival_target: ArchivalTargetDao
    periodicity: SchedulePeriodicityTypeDao
    frequency: int
    retention_days: int
    def __init__(self, policy: _Optional[_Union[ProtectionPolicyDao, _Mapping]] = ..., archival_target: _Optional[_Union[ArchivalTargetDao, _Mapping]] = ..., periodicity: _Optional[_Union[SchedulePeriodicityTypeDao, _Mapping]] = ..., frequency: _Optional[int] = ..., retention_days: _Optional[int] = ...) -> None: ...

class TenantDao(_message.Message):
    __slots__ = ("tenant_id", "name", "description", "parent_tenant_id", "is_active", "created_time_msecs", "last_updated_time_msecs", "is_deleted")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARENT_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    name: str
    description: str
    parent_tenant_id: str
    is_active: bool
    created_time_msecs: int
    last_updated_time_msecs: int
    is_deleted: bool
    def __init__(self, tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., parent_tenant_id: _Optional[str] = ..., is_active: bool = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., is_deleted: bool = ...) -> None: ...

class TenantViewBoxMapDao(_message.Message):
    __slots__ = ("tenant_id", "view_box_id", "is_deleted")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    view_box_id: int
    is_deleted: bool
    def __init__(self, tenant_id: _Optional[str] = ..., view_box_id: _Optional[int] = ..., is_deleted: bool = ...) -> None: ...

class TenantProtectionPolicyMapDao(_message.Message):
    __slots__ = ("tenant_id", "protection_policy_id", "is_deleted")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    protection_policy_id: str
    is_deleted: bool
    def __init__(self, tenant_id: _Optional[str] = ..., protection_policy_id: _Optional[str] = ..., is_deleted: bool = ...) -> None: ...

class PipelineRunStatusDao(_message.Message):
    __slots__ = ("status_id", "status_name")
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    status_id: int
    status_name: str
    def __init__(self, status_id: _Optional[int] = ..., status_name: _Optional[str] = ...) -> None: ...

class ApolloPipelineRunDao(_message.Message):
    __slots__ = ("pipeline", "instance_id", "start_time_usecs", "end_time_usecs", "error_msg", "status_id")
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    pipeline: str
    instance_id: int
    start_time_usecs: int
    end_time_usecs: int
    error_msg: str
    status_id: int
    def __init__(self, pipeline: _Optional[str] = ..., instance_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error_msg: _Optional[str] = ..., status_id: _Optional[int] = ...) -> None: ...

class IndexingStatusDao(_message.Message):
    __slots__ = ("status_id", "status_name")
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    status_id: int
    status_name: str
    def __init__(self, status_id: _Optional[int] = ..., status_name: _Optional[str] = ...) -> None: ...

class YodaIndexRunDao(_message.Message):
    __slots__ = ("entity_id", "protection_job_id", "protection_job_run_id", "cluster_id", "cluster_incarnation_id", "start_time_usecs", "end_time_usecs", "status_id", "entity_env_type")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    protection_job_id: int
    protection_job_run_id: int
    cluster_id: int
    cluster_incarnation_id: int
    start_time_usecs: int
    end_time_usecs: int
    status_id: int
    entity_env_type: int
    def __init__(self, entity_id: _Optional[int] = ..., protection_job_id: _Optional[int] = ..., protection_job_run_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status_id: _Optional[int] = ..., entity_env_type: _Optional[int] = ...) -> None: ...

class TenantStorageStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "tenant_id", "view_box_id", "data_in_bytes", "data_in_bytes_after_dedup", "data_written_bytes", "local_data_written_bytes", "local_tier_resiliency_impact_bytes", "local_total_physical_usage_bytes", "outdated_logical_usage_bytes", "storage_consumed_bytes", "total_logical_usage_bytes", "cloud_data_written_bytes", "cloud_total_physical_usage_bytes")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_AFTER_DEDUP_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIER_RESILIENCY_IMPACT_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONSUMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    tenant_id: str
    view_box_id: int
    data_in_bytes: int
    data_in_bytes_after_dedup: int
    data_written_bytes: int
    local_data_written_bytes: int
    local_tier_resiliency_impact_bytes: int
    local_total_physical_usage_bytes: int
    outdated_logical_usage_bytes: int
    storage_consumed_bytes: int
    total_logical_usage_bytes: int
    cloud_data_written_bytes: int
    cloud_total_physical_usage_bytes: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., tenant_id: _Optional[str] = ..., view_box_id: _Optional[int] = ..., data_in_bytes: _Optional[int] = ..., data_in_bytes_after_dedup: _Optional[int] = ..., data_written_bytes: _Optional[int] = ..., local_data_written_bytes: _Optional[int] = ..., local_tier_resiliency_impact_bytes: _Optional[int] = ..., local_total_physical_usage_bytes: _Optional[int] = ..., outdated_logical_usage_bytes: _Optional[int] = ..., storage_consumed_bytes: _Optional[int] = ..., total_logical_usage_bytes: _Optional[int] = ..., cloud_data_written_bytes: _Optional[int] = ..., cloud_total_physical_usage_bytes: _Optional[int] = ...) -> None: ...

class StorageConsumerTypeDao(_message.Message):
    __slots__ = ("type_id", "type_name")
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    type_name: str
    def __init__(self, type_id: _Optional[int] = ..., type_name: _Optional[str] = ...) -> None: ...

class ViewStorageStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "view_id", "consumer_type", "data_in_bytes", "data_in_bytes_after_dedup", "data_written_bytes", "local_data_written_bytes", "local_tier_resiliency_impact_bytes", "local_total_physical_usage_bytes", "outdated_logical_usage_bytes", "storage_consumed_bytes", "total_logical_usage_bytes", "cloud_data_written_bytes", "cloud_total_physical_usage_bytes")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_AFTER_DEDUP_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIER_RESILIENCY_IMPACT_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONSUMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    view_id: int
    consumer_type: StorageConsumerTypeDao
    data_in_bytes: int
    data_in_bytes_after_dedup: int
    data_written_bytes: int
    local_data_written_bytes: int
    local_tier_resiliency_impact_bytes: int
    local_total_physical_usage_bytes: int
    outdated_logical_usage_bytes: int
    storage_consumed_bytes: int
    total_logical_usage_bytes: int
    cloud_data_written_bytes: int
    cloud_total_physical_usage_bytes: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., view_id: _Optional[int] = ..., consumer_type: _Optional[_Union[StorageConsumerTypeDao, _Mapping]] = ..., data_in_bytes: _Optional[int] = ..., data_in_bytes_after_dedup: _Optional[int] = ..., data_written_bytes: _Optional[int] = ..., local_data_written_bytes: _Optional[int] = ..., local_tier_resiliency_impact_bytes: _Optional[int] = ..., local_total_physical_usage_bytes: _Optional[int] = ..., outdated_logical_usage_bytes: _Optional[int] = ..., storage_consumed_bytes: _Optional[int] = ..., total_logical_usage_bytes: _Optional[int] = ..., cloud_data_written_bytes: _Optional[int] = ..., cloud_total_physical_usage_bytes: _Optional[int] = ...) -> None: ...

class JobStorageStatsDao(_message.Message):
    __slots__ = ("timestamp_usecs", "job_id", "consumer_type", "data_in_bytes", "data_in_bytes_after_dedup", "data_written_bytes", "local_data_written_bytes", "local_tier_resiliency_impact_bytes", "local_total_physical_usage_bytes", "outdated_logical_usage_bytes", "storage_consumed_bytes", "total_logical_usage_bytes", "cloud_data_written_bytes", "cloud_total_physical_usage_bytes")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_IN_BYTES_AFTER_DEDUP_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIER_RESILIENCY_IMPACT_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONSUMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATA_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TOTAL_PHYSICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    job_id: int
    consumer_type: StorageConsumerTypeDao
    data_in_bytes: int
    data_in_bytes_after_dedup: int
    data_written_bytes: int
    local_data_written_bytes: int
    local_tier_resiliency_impact_bytes: int
    local_total_physical_usage_bytes: int
    outdated_logical_usage_bytes: int
    storage_consumed_bytes: int
    total_logical_usage_bytes: int
    cloud_data_written_bytes: int
    cloud_total_physical_usage_bytes: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., job_id: _Optional[int] = ..., consumer_type: _Optional[_Union[StorageConsumerTypeDao, _Mapping]] = ..., data_in_bytes: _Optional[int] = ..., data_in_bytes_after_dedup: _Optional[int] = ..., data_written_bytes: _Optional[int] = ..., local_data_written_bytes: _Optional[int] = ..., local_tier_resiliency_impact_bytes: _Optional[int] = ..., local_total_physical_usage_bytes: _Optional[int] = ..., outdated_logical_usage_bytes: _Optional[int] = ..., storage_consumed_bytes: _Optional[int] = ..., total_logical_usage_bytes: _Optional[int] = ..., cloud_data_written_bytes: _Optional[int] = ..., cloud_total_physical_usage_bytes: _Optional[int] = ...) -> None: ...
