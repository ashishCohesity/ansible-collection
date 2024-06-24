from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import uda_pb2 as _uda_pb2
from magneto.base import entity_pb2 as _entity_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAILED: _ClassVar[ProcessState]
    SUCCESS: _ClassVar[ProcessState]
    PARTIAL_SUCCESS: _ClassVar[ProcessState]
    FAILED_NEEDS_FULL_BACKUP: _ClassVar[ProcessState]
    STARTED: _ClassVar[ProcessState]
    FAILED_TRY_ANOTHER_CONTROL_NODE: _ClassVar[ProcessState]

class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FULL_BACKUP: _ClassVar[JobType]
    INCREMENTAL_BACKUP: _ClassVar[JobType]
    LOG_BACKUP: _ClassVar[JobType]
    RESTORE: _ClassVar[JobType]
    PITR_RESTORE: _ClassVar[JobType]
    ENTITY_REFRESH: _ClassVar[JobType]
    PG_CLEANUP: _ClassVar[JobType]
FAILED: ProcessState
SUCCESS: ProcessState
PARTIAL_SUCCESS: ProcessState
FAILED_NEEDS_FULL_BACKUP: ProcessState
STARTED: ProcessState
FAILED_TRY_ANOTHER_CONTROL_NODE: ProcessState
FULL_BACKUP: JobType
INCREMENTAL_BACKUP: JobType
LOG_BACKUP: JobType
RESTORE: JobType
PITR_RESTORE: JobType
ENTITY_REFRESH: JobType
PG_CLEANUP: JobType

class DiscoverUdaSourceArg(_message.Message):
    __slots__ = ("header", "script_dir", "source_args", "credentials", "hosts", "source_args_map", "cohesity_endpoints", "source_uuid")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    script_dir: str
    source_args: str
    credentials: _credentials_pb2.Credentials
    hosts: _containers.RepeatedScalarFieldContainer[str]
    source_args_map: _containers.ScalarMap[str, str]
    cohesity_endpoints: _containers.RepeatedScalarFieldContainer[str]
    source_uuid: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., script_dir: _Optional[str] = ..., source_args: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., hosts: _Optional[_Iterable[str]] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., cohesity_endpoints: _Optional[_Iterable[str]] = ..., source_uuid: _Optional[str] = ...) -> None: ...

class DiscoverUdaSourceResult(_message.Message):
    __slots__ = ("error", "source_name", "source_uuid", "preferred_control_nodes", "fresh_full_backup_view", "capabilities", "live_data_view", "use_s3_view", "live_log_view", "object_types", "static_live_log_view", "restrict_parallel_data_log_backups", "parallel_log_backups", "et_enable_log_backup_policy", "et_enable_run_now", "max_backup_resources", "max_log_backup_resources", "max_restore_resources", "max_anyjob_resources", "pre_backup_job_script_failure_tolerance")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_CONTROL_NODES_FIELD_NUMBER: _ClassVar[int]
    FRESH_FULL_BACKUP_VIEW_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    LIVE_DATA_VIEW_FIELD_NUMBER: _ClassVar[int]
    USE_S3_VIEW_FIELD_NUMBER: _ClassVar[int]
    LIVE_LOG_VIEW_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    STATIC_LIVE_LOG_VIEW_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_PARALLEL_DATA_LOG_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_LOG_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    ET_ENABLE_LOG_BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ET_ENABLE_RUN_NOW_FIELD_NUMBER: _ClassVar[int]
    MAX_BACKUP_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_BACKUP_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESTORE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_ANYJOB_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    PRE_BACKUP_JOB_SCRIPT_FAILURE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    source_name: str
    source_uuid: str
    preferred_control_nodes: _containers.RepeatedScalarFieldContainer[str]
    fresh_full_backup_view: bool
    capabilities: _uda_pb2.UdaSourceCapabilities
    live_data_view: bool
    use_s3_view: bool
    live_log_view: bool
    object_types: _containers.RepeatedScalarFieldContainer[str]
    static_live_log_view: bool
    restrict_parallel_data_log_backups: bool
    parallel_log_backups: bool
    et_enable_log_backup_policy: bool
    et_enable_run_now: bool
    max_backup_resources: int
    max_log_backup_resources: int
    max_restore_resources: int
    max_anyjob_resources: int
    pre_backup_job_script_failure_tolerance: _uda_pb2.PreJobScriptFailureTolerance
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., source_name: _Optional[str] = ..., source_uuid: _Optional[str] = ..., preferred_control_nodes: _Optional[_Iterable[str]] = ..., fresh_full_backup_view: bool = ..., capabilities: _Optional[_Union[_uda_pb2.UdaSourceCapabilities, _Mapping]] = ..., live_data_view: bool = ..., use_s3_view: bool = ..., live_log_view: bool = ..., object_types: _Optional[_Iterable[str]] = ..., static_live_log_view: bool = ..., restrict_parallel_data_log_backups: bool = ..., parallel_log_backups: bool = ..., et_enable_log_backup_policy: bool = ..., et_enable_run_now: bool = ..., max_backup_resources: _Optional[int] = ..., max_log_backup_resources: _Optional[int] = ..., max_restore_resources: _Optional[int] = ..., max_anyjob_resources: _Optional[int] = ..., pre_backup_job_script_failure_tolerance: _Optional[_Union[_uda_pb2.PreJobScriptFailureTolerance, str]] = ...) -> None: ...

class VerifyUdaSourceArg(_message.Message):
    __slots__ = ("header", "script_dir", "source_args", "credentials", "capabilities", "hosts", "source_args_map", "cohesity_endpoints", "source_uuid")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    script_dir: str
    source_args: str
    credentials: _credentials_pb2.Credentials
    capabilities: _uda_pb2.UdaSourceCapabilities
    hosts: _containers.RepeatedScalarFieldContainer[str]
    source_args_map: _containers.ScalarMap[str, str]
    cohesity_endpoints: _containers.RepeatedScalarFieldContainer[str]
    source_uuid: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., script_dir: _Optional[str] = ..., source_args: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., capabilities: _Optional[_Union[_uda_pb2.UdaSourceCapabilities, _Mapping]] = ..., hosts: _Optional[_Iterable[str]] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., cohesity_endpoints: _Optional[_Iterable[str]] = ..., source_uuid: _Optional[str] = ...) -> None: ...

class UdaObject(_message.Message):
    __slots__ = ("objName", "parent", "type", "full_name", "size", "isLeaf", "tags", "uuid")
    OBJNAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ISLEAF_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    objName: str
    parent: str
    type: str
    full_name: str
    size: int
    isLeaf: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    def __init__(self, objName: _Optional[str] = ..., parent: _Optional[str] = ..., type: _Optional[str] = ..., full_name: _Optional[str] = ..., size: _Optional[int] = ..., isLeaf: bool = ..., tags: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ...) -> None: ...

class GetUdaObjectsArg(_message.Message):
    __slots__ = ("header", "credentials", "script_dir", "source_args", "offset", "source_id", "job_type", "process_info", "hosts", "source_args_map")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    credentials: _credentials_pb2.Credentials
    script_dir: str
    source_args: str
    offset: int
    source_id: int
    job_type: JobType
    process_info: ProcessInfo
    hosts: _containers.RepeatedScalarFieldContainer[str]
    source_args_map: _containers.ScalarMap[str, str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., script_dir: _Optional[str] = ..., source_args: _Optional[str] = ..., offset: _Optional[int] = ..., source_id: _Optional[int] = ..., job_type: _Optional[_Union[JobType, str]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., hosts: _Optional[_Iterable[str]] = ..., source_args_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetUdaObjectsResult(_message.Message):
    __slots__ = ("error", "objects", "next_offset", "process_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    objects: _containers.RepeatedCompositeFieldContainer[UdaObject]
    next_offset: int
    process_info: ProcessInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[UdaObject, _Mapping]]] = ..., next_offset: _Optional[int] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ...) -> None: ...

class ProcessInfo(_message.Message):
    __slots__ = ("pid", "start_time", "process_state", "error_info")
    class ErrorInfo(_message.Message):
        __slots__ = ("retry_control_node",)
        RETRY_CONTROL_NODE_FIELD_NUMBER: _ClassVar[int]
        retry_control_node: str
        def __init__(self, retry_control_node: _Optional[str] = ...) -> None: ...
    PID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    PROCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    pid: int
    start_time: int
    process_state: ProcessState
    error_info: ProcessInfo.ErrorInfo
    def __init__(self, pid: _Optional[int] = ..., start_time: _Optional[int] = ..., process_state: _Optional[_Union[ProcessState, str]] = ..., error_info: _Optional[_Union[ProcessInfo.ErrorInfo, _Mapping]] = ...) -> None: ...

class RunId(_message.Message):
    __slots__ = ("job_id", "job_run_id", "attempt_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_run_id: int
    attempt_id: int
    def __init__(self, job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., attempt_id: _Optional[int] = ...) -> None: ...

class SendUdaEntitiesArg(_message.Message):
    __slots__ = ("header", "run_id", "page_number", "job_type", "entities", "entity_support")
    class Entity(_message.Message):
        __slots__ = ("entity", "new_name", "pitr_epoch_secs", "overwrite", "run_start_time_usecs", "data_backup_epoch_secs")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        NEW_NAME_FIELD_NUMBER: _ClassVar[int]
        PITR_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
        OVERWRITE_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        DATA_BACKUP_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        new_name: str
        pitr_epoch_secs: int
        overwrite: bool
        run_start_time_usecs: int
        data_backup_epoch_secs: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., new_name: _Optional[str] = ..., pitr_epoch_secs: _Optional[int] = ..., overwrite: bool = ..., run_start_time_usecs: _Optional[int] = ..., data_backup_epoch_secs: _Optional[int] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    page_number: int
    job_type: JobType
    entities: _containers.RepeatedCompositeFieldContainer[SendUdaEntitiesArg.Entity]
    entity_support: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., page_number: _Optional[int] = ..., job_type: _Optional[_Union[JobType, str]] = ..., entities: _Optional[_Iterable[_Union[SendUdaEntitiesArg.Entity, _Mapping]]] = ..., entity_support: bool = ...) -> None: ...

class UdaRequestResourceUsageArg(_message.Message):
    __slots__ = ("header", "job_type", "script_dir", "credentials", "source_args", "source_args_map", "job_args", "job_args_map")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class JobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    job_type: JobType
    script_dir: str
    credentials: _credentials_pb2.Credentials
    source_args: str
    source_args_map: _containers.ScalarMap[str, str]
    job_args: str
    job_args_map: _containers.ScalarMap[str, str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., script_dir: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., source_args: _Optional[str] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., job_args: _Optional[str] = ..., job_args_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UdaRequestResourceUsageResult(_message.Message):
    __slots__ = ("error", "usage_requested")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USAGE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    usage_requested: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., usage_requested: _Optional[int] = ...) -> None: ...

class UdaPreJobRunTasksArg(_message.Message):
    __slots__ = ("header", "run_id", "parallel_streams", "auto_log_backup_enabled", "job_args", "view_vips", "auto_log_backup_retention_mins", "hosts", "et_log_backup_enabled", "et_run_id", "script_dir", "et_backup_job_args_map", "external_disk_mountpoint", "data_view_mount_dirs", "log_view_mount_dirs", "retention_mins", "credentials", "job_type", "data_view_name", "log_view_name", "view_box_name", "source_args", "source_args_map", "job_args_map")
    class EtBackupJobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class JobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_RETENTION_MINS_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ET_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    ET_BACKUP_JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MINS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    parallel_streams: int
    auto_log_backup_enabled: bool
    job_args: str
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    auto_log_backup_retention_mins: int
    hosts: _containers.RepeatedScalarFieldContainer[str]
    et_log_backup_enabled: bool
    et_run_id: str
    script_dir: str
    et_backup_job_args_map: _containers.ScalarMap[str, str]
    external_disk_mountpoint: str
    data_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    log_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    retention_mins: int
    credentials: _credentials_pb2.Credentials
    job_type: JobType
    data_view_name: str
    log_view_name: str
    view_box_name: str
    source_args: str
    source_args_map: _containers.ScalarMap[str, str]
    job_args_map: _containers.ScalarMap[str, str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., parallel_streams: _Optional[int] = ..., auto_log_backup_enabled: bool = ..., job_args: _Optional[str] = ..., view_vips: _Optional[_Iterable[str]] = ..., auto_log_backup_retention_mins: _Optional[int] = ..., hosts: _Optional[_Iterable[str]] = ..., et_log_backup_enabled: bool = ..., et_run_id: _Optional[str] = ..., script_dir: _Optional[str] = ..., et_backup_job_args_map: _Optional[_Mapping[str, str]] = ..., external_disk_mountpoint: _Optional[str] = ..., data_view_mount_dirs: _Optional[_Iterable[str]] = ..., log_view_mount_dirs: _Optional[_Iterable[str]] = ..., retention_mins: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., data_view_name: _Optional[str] = ..., log_view_name: _Optional[str] = ..., view_box_name: _Optional[str] = ..., source_args: _Optional[str] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., job_args_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UdaPreJobRunTasksResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class StartUdaBackupArg(_message.Message):
    __slots__ = ("header", "run_id", "backup_args", "script_dir", "retention_mins", "parallel_streams", "auto_log_backup_enabled", "credentials", "job_type", "data_view_name", "log_view_name", "data_view_mount_dirs", "log_view_mount_dirs", "view_vips", "auto_log_backup_retention_mins", "s3_endpoint", "s3_access_key", "s3_secret_key", "hosts", "source_args", "source_args_map", "backup_job_args_map", "et_log_backup_enabled", "et_run_id", "et_backup_job_args_map", "external_disk_mountpoint", "view_box_name")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BackupJobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class EtBackupJobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MINS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_RETENTION_MINS_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ET_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ET_BACKUP_JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    backup_args: str
    script_dir: str
    retention_mins: int
    parallel_streams: int
    auto_log_backup_enabled: bool
    credentials: _credentials_pb2.Credentials
    job_type: JobType
    data_view_name: str
    log_view_name: str
    data_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    log_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    auto_log_backup_retention_mins: int
    s3_endpoint: str
    s3_access_key: str
    s3_secret_key: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    source_args: str
    source_args_map: _containers.ScalarMap[str, str]
    backup_job_args_map: _containers.ScalarMap[str, str]
    et_log_backup_enabled: bool
    et_run_id: str
    et_backup_job_args_map: _containers.ScalarMap[str, str]
    external_disk_mountpoint: str
    view_box_name: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., backup_args: _Optional[str] = ..., script_dir: _Optional[str] = ..., retention_mins: _Optional[int] = ..., parallel_streams: _Optional[int] = ..., auto_log_backup_enabled: bool = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., data_view_name: _Optional[str] = ..., log_view_name: _Optional[str] = ..., data_view_mount_dirs: _Optional[_Iterable[str]] = ..., log_view_mount_dirs: _Optional[_Iterable[str]] = ..., view_vips: _Optional[_Iterable[str]] = ..., auto_log_backup_retention_mins: _Optional[int] = ..., s3_endpoint: _Optional[str] = ..., s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., hosts: _Optional[_Iterable[str]] = ..., source_args: _Optional[str] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., backup_job_args_map: _Optional[_Mapping[str, str]] = ..., et_log_backup_enabled: bool = ..., et_run_id: _Optional[str] = ..., et_backup_job_args_map: _Optional[_Mapping[str, str]] = ..., external_disk_mountpoint: _Optional[str] = ..., view_box_name: _Optional[str] = ...) -> None: ...

class StartUdaBackupResult(_message.Message):
    __slots__ = ("error", "process_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    process_info: ProcessInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ...) -> None: ...

class GetUdaJobStatusArg(_message.Message):
    __slots__ = ("header", "run_id", "process_info", "pulse_log_index", "job_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    PULSE_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    process_info: ProcessInfo
    pulse_log_index: int
    job_type: JobType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., pulse_log_index: _Optional[int] = ..., job_type: _Optional[_Union[JobType, str]] = ...) -> None: ...

class GetUdaJobStatusResult(_message.Message):
    __slots__ = ("error", "status", "progress_percent", "pulse_logs", "pulse_log_index")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[GetUdaJobStatusResult.Status]
        kCompleted: _ClassVar[GetUdaJobStatusResult.Status]
    kRunning: GetUdaJobStatusResult.Status
    kCompleted: GetUdaJobStatusResult.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PULSE_LOGS_FIELD_NUMBER: _ClassVar[int]
    PULSE_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: GetUdaJobStatusResult.Status
    progress_percent: int
    pulse_logs: _containers.RepeatedScalarFieldContainer[str]
    pulse_log_index: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[GetUdaJobStatusResult.Status, str]] = ..., progress_percent: _Optional[int] = ..., pulse_logs: _Optional[_Iterable[str]] = ..., pulse_log_index: _Optional[int] = ...) -> None: ...

class GetUdaBackupDetailsArg(_message.Message):
    __slots__ = ("header", "run_id", "process_info", "job_type", "entity_support", "fetch_entities_to_index")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    FETCH_ENTITIES_TO_INDEX_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    process_info: ProcessInfo
    job_type: JobType
    entity_support: bool
    fetch_entities_to_index: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., entity_support: bool = ..., fetch_entities_to_index: bool = ...) -> None: ...

class GetUdaBackupDetailsResult(_message.Message):
    __slots__ = ("error", "warnings", "process_info", "stats", "log_backup_start_epoch_secs", "log_backup_end_epoch_secs", "data_backup_epoch_secs", "entities_to_index")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_START_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_END_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    DATA_BACKUP_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TO_INDEX_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    process_info: ProcessInfo
    stats: _uda_pb2.UdaStats
    log_backup_start_epoch_secs: int
    log_backup_end_epoch_secs: int
    data_backup_epoch_secs: int
    entities_to_index: _containers.RepeatedCompositeFieldContainer[EntityToIndex]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., stats: _Optional[_Union[_uda_pb2.UdaStats, _Mapping]] = ..., log_backup_start_epoch_secs: _Optional[int] = ..., log_backup_end_epoch_secs: _Optional[int] = ..., data_backup_epoch_secs: _Optional[int] = ..., entities_to_index: _Optional[_Iterable[_Union[EntityToIndex, _Mapping]]] = ...) -> None: ...

class EntityToIndex(_message.Message):
    __slots__ = ("full_name", "object_size")
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    full_name: str
    object_size: int
    def __init__(self, full_name: _Optional[str] = ..., object_size: _Optional[int] = ...) -> None: ...

class CancelUdaJobArg(_message.Message):
    __slots__ = ("header", "run_id", "process_info", "credentials", "job_type", "script_dir", "s3_endpoint", "s3_access_key", "s3_secret_key", "job_args", "source_args", "job_args_map", "source_args_map")
    class JobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    process_info: ProcessInfo
    credentials: _credentials_pb2.Credentials
    job_type: JobType
    script_dir: str
    s3_endpoint: str
    s3_access_key: str
    s3_secret_key: str
    job_args: str
    source_args: str
    job_args_map: _containers.ScalarMap[str, str]
    source_args_map: _containers.ScalarMap[str, str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., script_dir: _Optional[str] = ..., s3_endpoint: _Optional[str] = ..., s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., job_args: _Optional[str] = ..., source_args: _Optional[str] = ..., job_args_map: _Optional[_Mapping[str, str]] = ..., source_args_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StartUdaRestoreArg(_message.Message):
    __slots__ = ("header", "run_id", "restore_args", "script_dir", "parallel_streams", "credentials", "data_view_name", "log_view_name", "data_view_mount_dirs", "log_view_mount_dirs", "job_type", "view_vips", "s3_endpoint", "s3_access_key", "s3_secret_key", "hosts", "source_args", "backup_run_info", "source_args_map", "restore_job_args_map", "external_disk_mountpoint", "view_box_name", "restore_target_entity")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RestoreJobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_MOUNT_DIRS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    restore_args: str
    script_dir: str
    parallel_streams: int
    credentials: _credentials_pb2.Credentials
    data_view_name: str
    log_view_name: str
    data_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    log_view_mount_dirs: _containers.RepeatedScalarFieldContainer[str]
    job_type: JobType
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    s3_endpoint: str
    s3_access_key: str
    s3_secret_key: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    source_args: str
    backup_run_info: BackupRunInfo
    source_args_map: _containers.ScalarMap[str, str]
    restore_job_args_map: _containers.ScalarMap[str, str]
    external_disk_mountpoint: str
    view_box_name: str
    restore_target_entity: _entity_pb2.EntityProto
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., restore_args: _Optional[str] = ..., script_dir: _Optional[str] = ..., parallel_streams: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., data_view_name: _Optional[str] = ..., log_view_name: _Optional[str] = ..., data_view_mount_dirs: _Optional[_Iterable[str]] = ..., log_view_mount_dirs: _Optional[_Iterable[str]] = ..., job_type: _Optional[_Union[JobType, str]] = ..., view_vips: _Optional[_Iterable[str]] = ..., s3_endpoint: _Optional[str] = ..., s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., hosts: _Optional[_Iterable[str]] = ..., source_args: _Optional[str] = ..., backup_run_info: _Optional[_Union[BackupRunInfo, _Mapping]] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., restore_job_args_map: _Optional[_Mapping[str, str]] = ..., external_disk_mountpoint: _Optional[str] = ..., view_box_name: _Optional[str] = ..., restore_target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class BackupRunInfo(_message.Message):
    __slots__ = ("environment", "job_id", "job_run_id", "job_uid", "protection_source_id", "job_start_time_usecs")
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    environment: _enums_pb2.Environment.Type
    job_id: int
    job_run_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    protection_source_id: int
    job_start_time_usecs: int
    def __init__(self, environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., protection_source_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ...) -> None: ...

class StartUdaRestoreResult(_message.Message):
    __slots__ = ("error", "process_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    process_info: ProcessInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ...) -> None: ...

class GetUdaRestoreDetailsArg(_message.Message):
    __slots__ = ("header", "run_id", "process_info", "job_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_id: RunId
    process_info: ProcessInfo
    job_type: JobType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_id: _Optional[_Union[RunId, _Mapping]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., job_type: _Optional[_Union[JobType, str]] = ...) -> None: ...

class GetUdaRestoreDetailsResult(_message.Message):
    __slots__ = ("error", "warnings", "process_info", "stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    process_info: ProcessInfo
    stats: _uda_pb2.UdaStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., process_info: _Optional[_Union[ProcessInfo, _Mapping]] = ..., stats: _Optional[_Union[_uda_pb2.UdaStats, _Mapping]] = ...) -> None: ...

class MountUdaViewArg(_message.Message):
    __slots__ = ("header", "server_info_vec", "mountpoint_identifier", "local_mount_dir", "persist_reboot", "mounts_required", "windows_mount_params")
    class MountServerInfo(_message.Message):
        __slots__ = ("server_addr", "server_path")
        SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
        SERVER_PATH_FIELD_NUMBER: _ClassVar[int]
        server_addr: str
        server_path: str
        def __init__(self, server_addr: _Optional[str] = ..., server_path: _Optional[str] = ...) -> None: ...
    class WindowsMountParams(_message.Message):
        __slots__ = ("username", "password", "ad_auth_enabled")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        AD_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: str
        ad_auth_enabled: bool
        def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., ad_auth_enabled: bool = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SERVER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MOUNT_DIR_FIELD_NUMBER: _ClassVar[int]
    PERSIST_REBOOT_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_MOUNT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    server_info_vec: _containers.RepeatedCompositeFieldContainer[MountUdaViewArg.MountServerInfo]
    mountpoint_identifier: str
    local_mount_dir: str
    persist_reboot: bool
    mounts_required: int
    windows_mount_params: MountUdaViewArg.WindowsMountParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., server_info_vec: _Optional[_Iterable[_Union[MountUdaViewArg.MountServerInfo, _Mapping]]] = ..., mountpoint_identifier: _Optional[str] = ..., local_mount_dir: _Optional[str] = ..., persist_reboot: bool = ..., mounts_required: _Optional[int] = ..., windows_mount_params: _Optional[_Union[MountUdaViewArg.WindowsMountParams, _Mapping]] = ...) -> None: ...

class MountUdaViewResult(_message.Message):
    __slots__ = ("error", "mount_info_vec", "failed_mount_info_vec")
    class MountInfo(_message.Message):
        __slots__ = ("server_info", "mount_path")
        SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        server_info: MountUdaViewArg.MountServerInfo
        mount_path: str
        def __init__(self, server_info: _Optional[_Union[MountUdaViewArg.MountServerInfo, _Mapping]] = ..., mount_path: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FAILED_MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mount_info_vec: _containers.RepeatedCompositeFieldContainer[MountUdaViewResult.MountInfo]
    failed_mount_info_vec: _containers.RepeatedCompositeFieldContainer[MountUdaViewResult.MountInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mount_info_vec: _Optional[_Iterable[_Union[MountUdaViewResult.MountInfo, _Mapping]]] = ..., failed_mount_info_vec: _Optional[_Iterable[_Union[MountUdaViewResult.MountInfo, _Mapping]]] = ...) -> None: ...

class UnmountUdaViewArg(_message.Message):
    __slots__ = ("header", "mountpoint_vec", "local_mount_dir", "job_id", "job_types")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MOUNT_DIR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mountpoint_vec: _containers.RepeatedScalarFieldContainer[str]
    local_mount_dir: str
    job_id: int
    job_types: _containers.RepeatedScalarFieldContainer[JobType]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mountpoint_vec: _Optional[_Iterable[str]] = ..., local_mount_dir: _Optional[str] = ..., job_id: _Optional[int] = ..., job_types: _Optional[_Iterable[_Union[JobType, str]]] = ...) -> None: ...

class CleanupUdaJobArg(_message.Message):
    __slots__ = ("header", "job_id", "script_dir", "credentials", "source_args", "source_args_map", "full_backup_args", "incremental_backup_args", "log_backup_args", "backup_job_args_map", "data_view_name", "log_view_name", "view_vips", "hosts", "auto_log_backup_enabled", "et_log_backup_enabled")
    class SourceArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BackupJobArgsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
    DATA_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    job_id: int
    script_dir: str
    credentials: _credentials_pb2.Credentials
    source_args: str
    source_args_map: _containers.ScalarMap[str, str]
    full_backup_args: str
    incremental_backup_args: str
    log_backup_args: str
    backup_job_args_map: _containers.ScalarMap[str, str]
    data_view_name: str
    log_view_name: str
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    auto_log_backup_enabled: bool
    et_log_backup_enabled: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., job_id: _Optional[int] = ..., script_dir: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., source_args: _Optional[str] = ..., source_args_map: _Optional[_Mapping[str, str]] = ..., full_backup_args: _Optional[str] = ..., incremental_backup_args: _Optional[str] = ..., log_backup_args: _Optional[str] = ..., backup_job_args_map: _Optional[_Mapping[str, str]] = ..., data_view_name: _Optional[str] = ..., log_view_name: _Optional[str] = ..., view_vips: _Optional[_Iterable[str]] = ..., hosts: _Optional[_Iterable[str]] = ..., auto_log_backup_enabled: bool = ..., et_log_backup_enabled: bool = ...) -> None: ...
