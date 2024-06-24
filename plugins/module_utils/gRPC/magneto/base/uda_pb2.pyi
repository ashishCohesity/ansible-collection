from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import entity_pb2 as _entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreJobScriptFailureTolerance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kIgnoreFailure: _ClassVar[PreJobScriptFailureTolerance]
    kAtleastOneSuccess: _ClassVar[PreJobScriptFailureTolerance]
    kAllSuccess: _ClassVar[PreJobScriptFailureTolerance]
kIgnoreFailure: PreJobScriptFailureTolerance
kAtleastOneSuccess: PreJobScriptFailureTolerance
kAllSuccess: PreJobScriptFailureTolerance

class UdaSourceCapabilities(_message.Message):
    __slots__ = ("full_backup", "incr_backup", "log_backup", "auto_log_backup", "multi_object_restore", "dynamic_config", "entity_support", "et_log_backup", "resource_throttling", "pre_backup_job_script", "external_disks")
    FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    INCR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    MULTI_OBJECT_RESTORE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_THROTTLING_FIELD_NUMBER: _ClassVar[int]
    PRE_BACKUP_JOB_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    full_backup: bool
    incr_backup: bool
    log_backup: bool
    auto_log_backup: bool
    multi_object_restore: bool
    dynamic_config: bool
    entity_support: bool
    et_log_backup: bool
    resource_throttling: bool
    pre_backup_job_script: bool
    external_disks: bool
    def __init__(self, full_backup: bool = ..., incr_backup: bool = ..., log_backup: bool = ..., auto_log_backup: bool = ..., multi_object_restore: bool = ..., dynamic_config: bool = ..., entity_support: bool = ..., et_log_backup: bool = ..., resource_throttling: bool = ..., pre_backup_job_script: bool = ..., external_disks: bool = ...) -> None: ...

class UdaObjects(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: int
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class UdaCustomArgument(_message.Message):
    __slots__ = ("value", "encrypted_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    encrypted_value: bytes
    def __init__(self, value: _Optional[str] = ..., encrypted_value: _Optional[bytes] = ...) -> None: ...

class UdaBackupJobParams(_message.Message):
    __slots__ = ("uda_objects", "full_backup_args", "incremental_backup_args", "log_backup_args", "concurrency", "mounts", "source_id", "uda_s3_view_backup_properties", "entity_support", "backup_job_arguments_map", "et_log_backup", "external_disk_size_gb", "external_disk_sku")
    class BackupJobArgumentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UdaCustomArgument
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UdaCustomArgument, _Mapping]] = ...) -> None: ...
    UDA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    UDA_S3_VIEW_BACKUP_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ARGUMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_SKU_FIELD_NUMBER: _ClassVar[int]
    uda_objects: _containers.RepeatedCompositeFieldContainer[UdaObjects]
    full_backup_args: str
    incremental_backup_args: str
    log_backup_args: str
    concurrency: int
    mounts: int
    source_id: int
    uda_s3_view_backup_properties: UdaS3ViewBackupProperties
    entity_support: bool
    backup_job_arguments_map: _containers.MessageMap[str, UdaCustomArgument]
    et_log_backup: bool
    external_disk_size_gb: int
    external_disk_sku: str
    def __init__(self, uda_objects: _Optional[_Iterable[_Union[UdaObjects, _Mapping]]] = ..., full_backup_args: _Optional[str] = ..., incremental_backup_args: _Optional[str] = ..., log_backup_args: _Optional[str] = ..., concurrency: _Optional[int] = ..., mounts: _Optional[int] = ..., source_id: _Optional[int] = ..., uda_s3_view_backup_properties: _Optional[_Union[UdaS3ViewBackupProperties, _Mapping]] = ..., entity_support: bool = ..., backup_job_arguments_map: _Optional[_Mapping[str, UdaCustomArgument]] = ..., et_log_backup: bool = ..., external_disk_size_gb: _Optional[int] = ..., external_disk_sku: _Optional[str] = ...) -> None: ...

class UdaS3ViewBackupProperties(_message.Message):
    __slots__ = ("s3_config", "access_key", "secret_key")
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    access_key: str
    secret_key: str
    def __init__(self, s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., access_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class UdaStats(_message.Message):
    __slots__ = ("objects_successful", "objects_failed", "bytes_transferred", "bytes_protected", "num_protected_objects", "physical_stats", "bytes_written", "bytes_read")
    OBJECTS_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FAILED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    NUM_PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    objects_successful: int
    objects_failed: int
    bytes_transferred: int
    bytes_protected: int
    num_protected_objects: int
    physical_stats: PhysicalUdaStats
    bytes_written: int
    bytes_read: int
    def __init__(self, objects_successful: _Optional[int] = ..., objects_failed: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., bytes_protected: _Optional[int] = ..., num_protected_objects: _Optional[int] = ..., physical_stats: _Optional[_Union[PhysicalUdaStats, _Mapping]] = ..., bytes_written: _Optional[int] = ..., bytes_read: _Optional[int] = ...) -> None: ...

class UdaRestoreObjectParams(_message.Message):
    __slots__ = ("restore_time_secs", "new_object_name", "overwrite")
    RESTORE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    NEW_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    restore_time_secs: int
    new_object_name: str
    overwrite: bool
    def __init__(self, restore_time_secs: _Optional[int] = ..., new_object_name: _Optional[str] = ..., overwrite: bool = ...) -> None: ...

class PhysicalUdaStats(_message.Message):
    __slots__ = ("files_created", "files_modified", "files_deleted", "files_protected")
    FILES_CREATED_FIELD_NUMBER: _ClassVar[int]
    FILES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    FILES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    files_created: int
    files_modified: int
    files_deleted: int
    files_protected: int
    def __init__(self, files_created: _Optional[int] = ..., files_modified: _Optional[int] = ..., files_deleted: _Optional[int] = ..., files_protected: _Optional[int] = ...) -> None: ...

class UdaRestoreObject(_message.Message):
    __slots__ = ("object_uuid", "object_name", "restore_params", "entity_id")
    OBJECT_UUID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    object_uuid: str
    object_name: str
    restore_params: UdaRestoreObjectParams
    entity_id: int
    def __init__(self, object_uuid: _Optional[str] = ..., object_name: _Optional[str] = ..., restore_params: _Optional[_Union[UdaRestoreObjectParams, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class UdaRecoverJobParams(_message.Message):
    __slots__ = ("concurrency", "mounts", "script_dir", "restore_args", "local_mount_dir", "hosts", "preferred_control_nodes", "source_args", "capabilities", "run_start_time_usecs", "use_s3_view", "uda_s3_view_backup_properties", "host_type", "mount_view", "source_type", "source_arguments_map", "restore_job_arguments_map", "deployment_type", "restore_target_entity", "restore_target_entity_parents", "external_disk_sku")
    class SourceArgumentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UdaCustomArgument
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UdaCustomArgument, _Mapping]] = ...) -> None: ...
    class RestoreJobArgumentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UdaCustomArgument
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UdaCustomArgument, _Mapping]] = ...) -> None: ...
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MOUNT_DIR_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_CONTROL_NODES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    USE_S3_VIEW_FIELD_NUMBER: _ClassVar[int]
    UDA_S3_VIEW_BACKUP_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VIEW_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGUMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_ARGUMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_PARENTS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_SKU_FIELD_NUMBER: _ClassVar[int]
    concurrency: int
    mounts: int
    script_dir: str
    restore_args: str
    local_mount_dir: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    preferred_control_nodes: _containers.RepeatedScalarFieldContainer[str]
    source_args: str
    capabilities: UdaSourceCapabilities
    run_start_time_usecs: int
    use_s3_view: bool
    uda_s3_view_backup_properties: UdaS3ViewBackupProperties
    host_type: _enums_pb2.HostEnv.Type
    mount_view: bool
    source_type: str
    source_arguments_map: _containers.MessageMap[str, UdaCustomArgument]
    restore_job_arguments_map: _containers.MessageMap[str, UdaCustomArgument]
    deployment_type: UdaAgentDeployment.Type
    restore_target_entity: _entity_pb2.EntityProto
    restore_target_entity_parents: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    external_disk_sku: str
    def __init__(self, concurrency: _Optional[int] = ..., mounts: _Optional[int] = ..., script_dir: _Optional[str] = ..., restore_args: _Optional[str] = ..., local_mount_dir: _Optional[str] = ..., hosts: _Optional[_Iterable[str]] = ..., preferred_control_nodes: _Optional[_Iterable[str]] = ..., source_args: _Optional[str] = ..., capabilities: _Optional[_Union[UdaSourceCapabilities, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., use_s3_view: bool = ..., uda_s3_view_backup_properties: _Optional[_Union[UdaS3ViewBackupProperties, _Mapping]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., mount_view: bool = ..., source_type: _Optional[str] = ..., source_arguments_map: _Optional[_Mapping[str, UdaCustomArgument]] = ..., restore_job_arguments_map: _Optional[_Mapping[str, UdaCustomArgument]] = ..., deployment_type: _Optional[_Union[UdaAgentDeployment.Type, str]] = ..., restore_target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_target_entity_parents: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., external_disk_sku: _Optional[str] = ...) -> None: ...

class UdaObjectsToIndex(_message.Message):
    __slots__ = ("objects",)
    class ObjectToIndex(_message.Message):
        __slots__ = ("full_name", "entity_id", "size_bytes", "entity_type")
        FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        full_name: str
        entity_id: int
        size_bytes: int
        entity_type: str
        def __init__(self, full_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., size_bytes: _Optional[int] = ..., entity_type: _Optional[str] = ...) -> None: ...
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[UdaObjectsToIndex.ObjectToIndex]
    def __init__(self, objects: _Optional[_Iterable[_Union[UdaObjectsToIndex.ObjectToIndex, _Mapping]]] = ...) -> None: ...

class UdaAgentDeployment(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAgentOnSource: _ClassVar[UdaAgentDeployment.Type]
        kAgentOnRigel: _ClassVar[UdaAgentDeployment.Type]
    kAgentOnSource: UdaAgentDeployment.Type
    kAgentOnRigel: UdaAgentDeployment.Type
    def __init__(self) -> None: ...
