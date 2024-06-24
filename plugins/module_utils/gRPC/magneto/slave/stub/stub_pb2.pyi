from bifrost.task import bifrost_task_pb2 as _bifrost_task_pb2
from bridge.base import error_pb2 as _error_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.api.common import azure_sql_pb2 as _azure_sql_pb2
from magneto.api.common import aws_rds_pb2 as _aws_rds_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import cloud_deploy_pb2 as _cloud_deploy_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.base import gatekeeper_pb2 as _gatekeeper_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.base import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base import uda_pb2 as _uda_pb2
from magneto.master.base import master_pb2 as _master_pb2
from magneto.master.base import remote_actions_pb2 as _remote_actions_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartBackupTaskArg(_message.Message):
    __slots__ = ("api_version", "type", "backup_type", "expected_slave_incarnation_id", "request_sequencer", "job_id", "job_name", "job_instance_id", "attempt_start_time_usecs", "attempt_num", "task_id", "task_version", "view_box_id", "view_name", "qos_principal_name", "use_uuid_to_match_previous_vmdk", "use_uuid_for_encoded_filename", "connector_params", "entity", "root_entity", "host_entity", "datacenter_entity", "protected_entities", "entity_credentials", "app_credentials", "previous_snapshot_info", "current_snapshot_info", "stats_container_id", "cancellation_requested", "pause_requested", "ignorable_errors_in_error_db", "quiesce", "continue_on_quiesce_failure", "progress_monitor_task_path", "agent_info", "additional_params", "backup_source_params", "source_side_dedup_enabled", "delete_external_snapshot_vec", "env_backup_params", "storage_snapshot_info", "dr_to_cloud_params", "space_usage_policy", "user_info", "vapp_info", "archive_job_uid", "is_direct_archive_enabled", "global_include_exclude", "action_executor_target_type", "alerting_policy", "store_task_state_in_scribe", "source_filters", "vcd_connector_params", "priority", "proxy_machine_details", "is_powershell_task", "is_cloud_archive_direct", "is_fci_node_multiregistration_enabled", "enable_brick_level_checksum", "indexing_policy", "skip_rigel_for_backup", "data_transfer_info", "brick_based_dedup_enabled", "should_prevent_task_resource_hogging", "force_snap_fs_walk", "registered_entity_params", "adapter_specific_flags")
    class ProxyMachineDetails(_message.Message):
        __slots__ = ("connector_params", "root_entity", "entity", "take_host_permit")
        CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        TAKE_HOST_PERMIT_FIELD_NUMBER: _ClassVar[int]
        connector_params: _magneto_pb2.ConnectorParams
        root_entity: _entity_pb2.EntityProto
        entity: _entity_pb2.EntityProto
        take_host_permit: bool
        def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., take_host_permit: bool = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_VERSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_UUID_TO_MATCH_PREVIOUS_VMDK_FIELD_NUMBER: _ClassVar[int]
    USE_UUID_FOR_ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    PAUSE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    IGNORABLE_ERRORS_IN_ERROR_DB_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_QUIESCE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DELETE_EXTERNAL_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    ENV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    DR_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SPACE_USAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INCLUDE_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    STORE_TASK_STATE_IN_SCRIBE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    VCD_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PROXY_MACHINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IS_POWERSHELL_TASK_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_NODE_MULTIREGISTRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    BRICK_BASED_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_PREVENT_TASK_RESOURCE_HOGGING_FIELD_NUMBER: _ClassVar[int]
    FORCE_SNAP_FS_WALK_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_SPECIFIC_FLAGS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    type: _enums_pb2.Environment.Type
    backup_type: _enums_pb2.ScheduledBackupType.Type
    expected_slave_incarnation_id: int
    request_sequencer: int
    job_id: int
    job_name: str
    job_instance_id: int
    attempt_start_time_usecs: int
    attempt_num: int
    task_id: int
    task_version: int
    view_box_id: int
    view_name: str
    qos_principal_name: str
    use_uuid_to_match_previous_vmdk: bool
    use_uuid_for_encoded_filename: bool
    connector_params: _magneto_pb2.ConnectorParams
    entity: _entity_pb2.EntityProto
    root_entity: _entity_pb2.EntityProto
    host_entity: _entity_pb2.EntityProto
    datacenter_entity: _entity_pb2.EntityProto
    protected_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    entity_credentials: _credentials_pb2.Credentials
    app_credentials: _credentials_pb2.AppCredentials
    previous_snapshot_info: _magneto_pb2.SnapshotInfoProto
    current_snapshot_info: _magneto_pb2.SnapshotInfoProto
    stats_container_id: int
    cancellation_requested: bool
    pause_requested: bool
    ignorable_errors_in_error_db: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    quiesce: bool
    continue_on_quiesce_failure: bool
    progress_monitor_task_path: str
    agent_info: _agent_pb2.AgentInfoProto
    additional_params: _magneto_pb2.BackupTaskAdditionalParams
    backup_source_params: _env_params_pb2_1.BackupSourceParams
    source_side_dedup_enabled: bool
    delete_external_snapshot_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.ExternalSnapshotInfo]
    env_backup_params: _env_params_pb2_1.EnvBackupParams
    storage_snapshot_info: _storage_pb2.EntitySnapshotInfoProto
    dr_to_cloud_params: _magneto_pb2.BackupJobProto.DRToCloudParams
    space_usage_policy: _magneto_pb2.SpaceUsagePolicy
    user_info: _permissions_pb2.UserInformation
    vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
    archive_job_uid: _universal_id_pb2.UniversalIdProto
    is_direct_archive_enabled: bool
    global_include_exclude: _env_params_pb2_1.PhysicalFileBackupParams.GlobalIncludeExclude
    action_executor_target_type: _enums_pb2.TargetType.Type
    alerting_policy: _env_params_pb2_1.AlertingPolicyProto
    store_task_state_in_scribe: bool
    source_filters: _magneto_pb2.SourceFilters
    vcd_connector_params: _magneto_pb2.ConnectorParams
    priority: _magneto_pb2.Priority
    proxy_machine_details: StartBackupTaskArg.ProxyMachineDetails
    is_powershell_task: bool
    is_cloud_archive_direct: bool
    is_fci_node_multiregistration_enabled: bool
    enable_brick_level_checksum: bool
    indexing_policy: _env_params_pb2_1.IndexingPolicyProto
    skip_rigel_for_backup: bool
    data_transfer_info: _env_params_pb2_1.DataTransferInfo
    brick_based_dedup_enabled: bool
    should_prevent_task_resource_hogging: bool
    force_snap_fs_walk: bool
    registered_entity_params: _magneto_pb2.RegisteredEntityParams
    adapter_specific_flags: _magneto_pb2.AdapterSpecificFlagsProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., job_id: _Optional[int] = ..., job_name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., attempt_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., task_id: _Optional[int] = ..., task_version: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., qos_principal_name: _Optional[str] = ..., use_uuid_to_match_previous_vmdk: bool = ..., use_uuid_for_encoded_filename: bool = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datacenter_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., protected_entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., app_credentials: _Optional[_Union[_credentials_pb2.AppCredentials, _Mapping]] = ..., previous_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., current_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., stats_container_id: _Optional[int] = ..., cancellation_requested: bool = ..., pause_requested: bool = ..., ignorable_errors_in_error_db: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., quiesce: bool = ..., continue_on_quiesce_failure: bool = ..., progress_monitor_task_path: _Optional[str] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., additional_params: _Optional[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]] = ..., backup_source_params: _Optional[_Union[_env_params_pb2_1.BackupSourceParams, _Mapping]] = ..., source_side_dedup_enabled: bool = ..., delete_external_snapshot_vec: _Optional[_Iterable[_Union[_magneto_pb2.ExternalSnapshotInfo, _Mapping]]] = ..., env_backup_params: _Optional[_Union[_env_params_pb2_1.EnvBackupParams, _Mapping]] = ..., storage_snapshot_info: _Optional[_Union[_storage_pb2.EntitySnapshotInfoProto, _Mapping]] = ..., dr_to_cloud_params: _Optional[_Union[_magneto_pb2.BackupJobProto.DRToCloudParams, _Mapping]] = ..., space_usage_policy: _Optional[_Union[_magneto_pb2.SpaceUsagePolicy, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ..., archive_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_direct_archive_enabled: bool = ..., global_include_exclude: _Optional[_Union[_env_params_pb2_1.PhysicalFileBackupParams.GlobalIncludeExclude, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., alerting_policy: _Optional[_Union[_env_params_pb2_1.AlertingPolicyProto, _Mapping]] = ..., store_task_state_in_scribe: bool = ..., source_filters: _Optional[_Union[_magneto_pb2.SourceFilters, _Mapping]] = ..., vcd_connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., priority: _Optional[_Union[_magneto_pb2.Priority, str]] = ..., proxy_machine_details: _Optional[_Union[StartBackupTaskArg.ProxyMachineDetails, _Mapping]] = ..., is_powershell_task: bool = ..., is_cloud_archive_direct: bool = ..., is_fci_node_multiregistration_enabled: bool = ..., enable_brick_level_checksum: bool = ..., indexing_policy: _Optional[_Union[_env_params_pb2_1.IndexingPolicyProto, _Mapping]] = ..., skip_rigel_for_backup: bool = ..., data_transfer_info: _Optional[_Union[_env_params_pb2_1.DataTransferInfo, _Mapping]] = ..., brick_based_dedup_enabled: bool = ..., should_prevent_task_resource_hogging: bool = ..., force_snap_fs_walk: bool = ..., registered_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ..., adapter_specific_flags: _Optional[_Union[_magneto_pb2.AdapterSpecificFlagsProto, _Mapping]] = ...) -> None: ...

class StartBackupTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifySlaveTaskArg(_message.Message):
    __slots__ = ("api_version", "type", "task_id", "expected_slave_incarnation_id")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    type: _enums_pb2.Environment.Type
    task_id: int
    expected_slave_incarnation_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., task_id: _Optional[int] = ..., expected_slave_incarnation_id: _Optional[int] = ...) -> None: ...

class NotifySlaveTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelBackupTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "task_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    task_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelBackupTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseBackupTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "task_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    task_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class PauseBackupTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartFetchStorageInfoTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "job_id", "task_id", "source_info_vec", "parent_source", "parent_source_connection_params", "storage_source_info_vec", "cancellation_requested", "progress_monitor_task_path", "entities_storage_info", "storage_array_snapshot")
    class SourceInfo(_message.Message):
        __slots__ = ("entity", "backup_source_params", "hyperv_source_info")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        HYPERV_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        backup_source_params: _env_params_pb2_1.BackupSourceParams
        hyperv_source_info: StartFetchStorageInfoTaskArg.HyperVSourceInfo
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., backup_source_params: _Optional[_Union[_env_params_pb2_1.BackupSourceParams, _Mapping]] = ..., hyperv_source_info: _Optional[_Union[StartFetchStorageInfoTaskArg.HyperVSourceInfo, _Mapping]] = ...) -> None: ...
    class HyperVSourceInfo(_message.Message):
        __slots__ = ("host_entity",)
        HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
        host_entity: _entity_pb2.EntityProto
        def __init__(self, host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    class StorageSourceInfo(_message.Message):
        __slots__ = ("parent_source", "parent_source_connection_params", "parent_source_reg_entity_params")
        PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
        PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
        PARENT_SOURCE_REG_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
        parent_source: _entity_pb2.EntityProto
        parent_source_connection_params: _magneto_pb2.ConnectorParams
        parent_source_reg_entity_params: _magneto_pb2.RegisteredEntityParams
        def __init__(self, parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., parent_source_reg_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_STORAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    job_id: int
    task_id: int
    source_info_vec: _containers.RepeatedCompositeFieldContainer[StartFetchStorageInfoTaskArg.SourceInfo]
    parent_source: _entity_pb2.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    storage_source_info_vec: _containers.RepeatedCompositeFieldContainer[StartFetchStorageInfoTaskArg.StorageSourceInfo]
    cancellation_requested: bool
    progress_monitor_task_path: str
    entities_storage_info: _storage_pb2.EntitiesStorageInfoProto
    storage_array_snapshot: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., job_id: _Optional[int] = ..., task_id: _Optional[int] = ..., source_info_vec: _Optional[_Iterable[_Union[StartFetchStorageInfoTaskArg.SourceInfo, _Mapping]]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., storage_source_info_vec: _Optional[_Iterable[_Union[StartFetchStorageInfoTaskArg.StorageSourceInfo, _Mapping]]] = ..., cancellation_requested: bool = ..., progress_monitor_task_path: _Optional[str] = ..., entities_storage_info: _Optional[_Union[_storage_pb2.EntitiesStorageInfoProto, _Mapping]] = ..., storage_array_snapshot: bool = ...) -> None: ...

class StartFetchStorageInfoTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelFetchStorageInfoTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "task_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    task_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelFetchStorageInfoTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartTakeGroupSnapshotTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "job_id", "job_instance_id", "job_name", "task_id", "source_info_vec", "primary_device_set", "parent_source", "parent_source_connection_params", "primary_storage_source", "primary_storage_connection_params", "parent_source_reg_entity_params", "quiesce", "env_backup_params", "entities_group_snapshot_info", "error", "cancellation_requested", "progress_monitor_task_path", "storage_array_snapshot", "leverage_san_storage_snapshot_v2", "view_name", "view_box_id", "backup_type", "attempt_num", "qos_principal_name", "additional_params", "action_executor_target_type", "san_protocol")
    class SourceInfo(_message.Message):
        __slots__ = ("entity", "backup_source_params", "vmware_source_info", "previous_snapshot_info", "stats_container_id")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        VMWARE_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        backup_source_params: _env_params_pb2_1.BackupSourceParams
        vmware_source_info: _magneto_pb2.VMwareSourceInfo
        previous_snapshot_info: _magneto_pb2.SnapshotInfoProto
        stats_container_id: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., backup_source_params: _Optional[_Union[_env_params_pb2_1.BackupSourceParams, _Mapping]] = ..., vmware_source_info: _Optional[_Union[_magneto_pb2.VMwareSourceInfo, _Mapping]] = ..., previous_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., stats_container_id: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DEVICE_SET_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_REG_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    ENV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAN_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    job_id: int
    job_instance_id: int
    job_name: str
    task_id: int
    source_info_vec: _containers.RepeatedCompositeFieldContainer[StartTakeGroupSnapshotTaskArg.SourceInfo]
    primary_device_set: _containers.RepeatedCompositeFieldContainer[_storage_pb2.StorageDeviceProto]
    parent_source: _entity_pb2.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    primary_storage_source: _entity_pb2.EntityProto
    primary_storage_connection_params: _magneto_pb2.ConnectorParams
    parent_source_reg_entity_params: _magneto_pb2.RegisteredEntityParams
    quiesce: bool
    env_backup_params: _env_params_pb2_1.EnvBackupParams
    entities_group_snapshot_info: _storage_pb2.EntitiesGroupSnapshotInfoProto
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    progress_monitor_task_path: str
    storage_array_snapshot: bool
    leverage_san_storage_snapshot_v2: bool
    view_name: str
    view_box_id: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    attempt_num: int
    qos_principal_name: str
    additional_params: _magneto_pb2.BackupTaskAdditionalParams
    action_executor_target_type: _enums_pb2.TargetType.Type
    san_protocol: _storage_pb2.SanProtocol
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., job_name: _Optional[str] = ..., task_id: _Optional[int] = ..., source_info_vec: _Optional[_Iterable[_Union[StartTakeGroupSnapshotTaskArg.SourceInfo, _Mapping]]] = ..., primary_device_set: _Optional[_Iterable[_Union[_storage_pb2.StorageDeviceProto, _Mapping]]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., primary_storage_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., primary_storage_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., parent_source_reg_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ..., quiesce: bool = ..., env_backup_params: _Optional[_Union[_env_params_pb2_1.EnvBackupParams, _Mapping]] = ..., entities_group_snapshot_info: _Optional[_Union[_storage_pb2.EntitiesGroupSnapshotInfoProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., progress_monitor_task_path: _Optional[str] = ..., storage_array_snapshot: bool = ..., leverage_san_storage_snapshot_v2: bool = ..., view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., attempt_num: _Optional[int] = ..., qos_principal_name: _Optional[str] = ..., additional_params: _Optional[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., san_protocol: _Optional[_Union[_storage_pb2.SanProtocol, str]] = ...) -> None: ...

class StartTakeGroupSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelTakeGroupSnapshotTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "task_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    task_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelTakeGroupSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartTeardownGroupSnapshotTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "job_id", "task_id", "entities_group_snapshot_info", "parent_source", "parent_source_connection_params", "primary_storage_source", "primary_storage_connection_params", "progress_monitor_task_path", "teardown_info", "leverage_san_storage_snapshot_v2")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_INFO_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    job_id: int
    task_id: int
    entities_group_snapshot_info: _storage_pb2.EntitiesGroupSnapshotInfoProto
    parent_source: _entity_pb2.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    primary_storage_source: _entity_pb2.EntityProto
    primary_storage_connection_params: _magneto_pb2.ConnectorParams
    progress_monitor_task_path: str
    teardown_info: _storage_pb2.TeardownGroupSnapshotInfoProto
    leverage_san_storage_snapshot_v2: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., job_id: _Optional[int] = ..., task_id: _Optional[int] = ..., entities_group_snapshot_info: _Optional[_Union[_storage_pb2.EntitiesGroupSnapshotInfoProto, _Mapping]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., primary_storage_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., primary_storage_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., teardown_info: _Optional[_Union[_storage_pb2.TeardownGroupSnapshotInfoProto, _Mapping]] = ..., leverage_san_storage_snapshot_v2: bool = ...) -> None: ...

class StartTeardownGroupSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "task_id", "task_uid", "name", "restore_parent_source", "connector_params", "cancellation_requested", "restore_vlan_params", "restore_type", "entities", "view_box_id", "view_name", "rename_restored_object_param", "rename_restored_vapp_param", "power_on", "continue_restore_on_error", "error", "progress_monitor_task_path", "agent_info", "volume_info_vec", "additional_params", "custom_tag_vec", "skip_cloning_view", "restored_data_storage_domain_id", "restore_files_params", "restore_files_info", "ignore_set_attr_error", "create_view", "fail_progress_monitor_on_already_exists_error", "restore_info", "previous_restore_info", "restore_vmware_vm_params", "restore_hyperv_vm_params", "restore_acropolis_vms_params", "restore_kvm_vms_params", "restore_outlook_params", "user_info", "mount_volumes_params", "mount_volumes_info", "deploy_vms_to_cloud_params", "new_aws_convert_and_deploy_ready", "skip_image_deploy", "recover_volumes_params", "cloud_deploy_info", "should_request_permit", "recover_virtual_disk_params", "recover_virtual_disk_info", "restore_kubernetes_namespaces_params", "nosql_connect_params", "nosql_recover_job_params", "uda_recover_job_params", "restore_one_drive_params", "preserve_tags", "view_params", "include_vm_config", "uptier_task", "job_id", "job_name", "job_instance_id", "restore_site_params", "restore_public_folders_params", "restore_teams_params", "restore_groups_params", "conversion_params", "sfdc_recover_job_params", "restore_s3_params", "restore_san_params", "download_chats_params", "source_view_name_DEPRECATED", "action_executor_target_type", "proxy_machine_details", "is_powershell_task", "is_object_protection", "storage_array_snapshot", "skip_rigel_for_restore", "skip_mbx_permit_for_pst", "data_transfer_info", "parent_restore_job_id")
    Extensions: _python_message._ExtensionDict
    class RestoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRecoverVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kCloneVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverApp: _ClassVar[StartRestoreTaskArg.RestoreType]
        kCloneApp: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRestoreFiles: _ClassVar[StartRestoreTaskArg.RestoreType]
        kMountVolumes: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverSanVolume: _ClassVar[StartRestoreTaskArg.RestoreType]
        kConvertAndDeployVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kMountFileVolume: _ClassVar[StartRestoreTaskArg.RestoreType]
        kSystem: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverVolumes: _ClassVar[StartRestoreTaskArg.RestoreType]
        kDeployVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverEmails: _ClassVar[StartRestoreTaskArg.RestoreType]
        kConvertVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverVirtualDisks: _ClassVar[StartRestoreTaskArg.RestoreType]
        kCloneRefreshApp: _ClassVar[StartRestoreTaskArg.RestoreType]
        kCloneAppView: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverNamespaces: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverO365Drive: _ClassVar[StartRestoreTaskArg.RestoreType]
        kCloneVMsToView: _ClassVar[StartRestoreTaskArg.RestoreType]
        kHydrateView: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverNoSql: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverSites: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverO365PublicFolders: _ClassVar[StartRestoreTaskArg.RestoreType]
        kLogApply: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverUda: _ClassVar[StartRestoreTaskArg.RestoreType]
        kConvertToPst: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverO365Teams: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverO365Groups: _ClassVar[StartRestoreTaskArg.RestoreType]
        kReHydrateVMs: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverRDS: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverAurora: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverSfdc: _ClassVar[StartRestoreTaskArg.RestoreType]
        kHydrateViewV2: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverS3: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverSanGroup: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverAzureSQL: _ClassVar[StartRestoreTaskArg.RestoreType]
        kDownloadChats: _ClassVar[StartRestoreTaskArg.RestoreType]
        kRecoverRDSPostgres: _ClassVar[StartRestoreTaskArg.RestoreType]
    kRecoverVMs: StartRestoreTaskArg.RestoreType
    kCloneVMs: StartRestoreTaskArg.RestoreType
    kRecoverApp: StartRestoreTaskArg.RestoreType
    kCloneApp: StartRestoreTaskArg.RestoreType
    kRestoreFiles: StartRestoreTaskArg.RestoreType
    kMountVolumes: StartRestoreTaskArg.RestoreType
    kRecoverSanVolume: StartRestoreTaskArg.RestoreType
    kConvertAndDeployVMs: StartRestoreTaskArg.RestoreType
    kMountFileVolume: StartRestoreTaskArg.RestoreType
    kSystem: StartRestoreTaskArg.RestoreType
    kRecoverVolumes: StartRestoreTaskArg.RestoreType
    kDeployVMs: StartRestoreTaskArg.RestoreType
    kRecoverEmails: StartRestoreTaskArg.RestoreType
    kConvertVMs: StartRestoreTaskArg.RestoreType
    kRecoverVirtualDisks: StartRestoreTaskArg.RestoreType
    kCloneRefreshApp: StartRestoreTaskArg.RestoreType
    kCloneAppView: StartRestoreTaskArg.RestoreType
    kRecoverNamespaces: StartRestoreTaskArg.RestoreType
    kRecoverO365Drive: StartRestoreTaskArg.RestoreType
    kCloneVMsToView: StartRestoreTaskArg.RestoreType
    kHydrateView: StartRestoreTaskArg.RestoreType
    kRecoverNoSql: StartRestoreTaskArg.RestoreType
    kRecoverSites: StartRestoreTaskArg.RestoreType
    kRecoverO365PublicFolders: StartRestoreTaskArg.RestoreType
    kLogApply: StartRestoreTaskArg.RestoreType
    kRecoverUda: StartRestoreTaskArg.RestoreType
    kConvertToPst: StartRestoreTaskArg.RestoreType
    kRecoverO365Teams: StartRestoreTaskArg.RestoreType
    kRecoverO365Groups: StartRestoreTaskArg.RestoreType
    kReHydrateVMs: StartRestoreTaskArg.RestoreType
    kRecoverRDS: StartRestoreTaskArg.RestoreType
    kRecoverAurora: StartRestoreTaskArg.RestoreType
    kRecoverSfdc: StartRestoreTaskArg.RestoreType
    kHydrateViewV2: StartRestoreTaskArg.RestoreType
    kRecoverS3: StartRestoreTaskArg.RestoreType
    kRecoverSanGroup: StartRestoreTaskArg.RestoreType
    kRecoverAzureSQL: StartRestoreTaskArg.RestoreType
    kDownloadChats: StartRestoreTaskArg.RestoreType
    kRecoverRDSPostgres: StartRestoreTaskArg.RestoreType
    class RestoreEntity(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "entity", "root_entity", "host_entity", "standby_entity", "entity_credentials", "progress_monitor_task_path", "restoring_files_from_archived_snapshot", "job_id", "job_uid", "job_instance_id", "job_start_time_usecs", "attempt_num", "retrieve_archive_view_name", "failed_over", "restore_acropolis_vm_param", "snapshot_info", "replication_info", "restore_kvm_vm_param", "nosql_recover_params", "uda_recover_params", "sfdc_recover_params", "san_recover_params", "connector_params", "restore_vapp_info", "one_drive_restore_entity_params", "restore_azure_sql_params", "restore_rds_postgres_params")
        Extensions: _python_message._ExtensionDict
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
        STANDBY_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        RESTORING_FILES_FROM_ARCHIVED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
        RETRIEVE_ARCHIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        FAILED_OVER_FIELD_NUMBER: _ClassVar[int]
        RESTORE_ACROPOLIS_VM_PARAM_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        RESTORE_KVM_VM_PARAM_FIELD_NUMBER: _ClassVar[int]
        NOSQL_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        UDA_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        SFDC_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        SAN_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
        ONE_DRIVE_RESTORE_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_AZURE_SQL_PARAMS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_RDS_POSTGRES_PARAMS_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        entity: _entity_pb2.EntityProto
        root_entity: _entity_pb2.EntityProto
        host_entity: _entity_pb2.EntityProto
        standby_entity: _entity_pb2.EntityProto
        entity_credentials: _credentials_pb2.Credentials
        progress_monitor_task_path: str
        restoring_files_from_archived_snapshot: bool
        job_id: int
        job_uid: _universal_id_pb2.UniversalIdProto
        job_instance_id: int
        job_start_time_usecs: int
        attempt_num: int
        retrieve_archive_view_name: str
        failed_over: bool
        restore_acropolis_vm_param: _magneto_pb2.RestoreAcropolisVMParam
        snapshot_info: _magneto_pb2.SnapshotInfoProto
        replication_info: _magneto_pb2.CloudDeployInfoProto
        restore_kvm_vm_param: _magneto_pb2.RestoreKVMVMParam
        nosql_recover_params: _magneto_pb2.NoSqlRecoverParams
        uda_recover_params: _magneto_pb2.UdaRecoverParams
        sfdc_recover_params: _magneto_pb2.SfdcRecoverParams
        san_recover_params: _magneto_pb2.SANRecoverParams
        connector_params: _magneto_pb2.ConnectorParams
        restore_vapp_info: _magneto_pb2.RestoreVappInfo
        one_drive_restore_entity_params: _magneto_pb2.O365OneDriveRestoreEntityParams
        restore_azure_sql_params: _azure_sql_pb2.RestoreAzureSQLParams
        restore_rds_postgres_params: _aws_rds_pb2.RestoreRDSPostgresParams
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., standby_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., restoring_files_from_archived_snapshot: bool = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., retrieve_archive_view_name: _Optional[str] = ..., failed_over: bool = ..., restore_acropolis_vm_param: _Optional[_Union[_magneto_pb2.RestoreAcropolisVMParam, _Mapping]] = ..., snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., replication_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., restore_kvm_vm_param: _Optional[_Union[_magneto_pb2.RestoreKVMVMParam, _Mapping]] = ..., nosql_recover_params: _Optional[_Union[_magneto_pb2.NoSqlRecoverParams, _Mapping]] = ..., uda_recover_params: _Optional[_Union[_magneto_pb2.UdaRecoverParams, _Mapping]] = ..., sfdc_recover_params: _Optional[_Union[_magneto_pb2.SfdcRecoverParams, _Mapping]] = ..., san_recover_params: _Optional[_Union[_magneto_pb2.SANRecoverParams, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., restore_vapp_info: _Optional[_Union[_magneto_pb2.RestoreVappInfo, _Mapping]] = ..., one_drive_restore_entity_params: _Optional[_Union[_magneto_pb2.O365OneDriveRestoreEntityParams, _Mapping]] = ..., restore_azure_sql_params: _Optional[_Union[_azure_sql_pb2.RestoreAzureSQLParams, _Mapping]] = ..., restore_rds_postgres_params: _Optional[_Union[_aws_rds_pb2.RestoreRDSPostgresParams, _Mapping]] = ...) -> None: ...
    class ProxyMachineDetails(_message.Message):
        __slots__ = ("connector_params", "root_entity", "entity")
        CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        connector_params: _magneto_pb2.ConnectorParams
        root_entity: _entity_pb2.EntityProto
        entity: _entity_pb2.EntityProto
        def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_VAPP_PARAM_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_RESTORE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONING_VIEW_FIELD_NUMBER: _ClassVar[int]
    RESTORED_DATA_STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SET_ATTR_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    FAIL_PROGRESS_MONITOR_ON_ALREADY_EXISTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMWARE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_HYPERV_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ACROPOLIS_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KVM_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OUTLOOK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_INFO_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NEW_AWS_CONVERT_AND_DEPLOY_READY_FIELD_NUMBER: _ClassVar[int]
    SKIP_IMAGE_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VOLUMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_REQUEST_PERMIT_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIRTUAL_DISK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIRTUAL_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KUBERNETES_NAMESPACES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ONE_DRIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PUBLIC_FOLDERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEAMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_GROUPS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_S3_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CHATS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROXY_MACHINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IS_POWERSHELL_TASK_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    SKIP_MBX_PERMIT_FOR_PST_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESTORE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    task_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    name: str
    restore_parent_source: _entity_pb2.EntityProto
    connector_params: _magneto_pb2.ConnectorParams
    cancellation_requested: bool
    restore_vlan_params: _common_pb2.VlanParams
    restore_type: StartRestoreTaskArg.RestoreType
    entities: _containers.RepeatedCompositeFieldContainer[StartRestoreTaskArg.RestoreEntity]
    view_box_id: int
    view_name: str
    rename_restored_object_param: _magneto_pb2.RenameObjectParamProto
    rename_restored_vapp_param: _magneto_pb2.RenameObjectParamProto
    power_on: bool
    continue_restore_on_error: bool
    error: _error_pb2_1.ErrorProto
    progress_monitor_task_path: str
    agent_info: _agent_pb2.AgentInfoProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.VolumeInfo]
    additional_params: _magneto_pb2.RestoreTaskAdditionalParams
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_cloud_deploy_pb2.CustomTag]
    skip_cloning_view: bool
    restored_data_storage_domain_id: int
    restore_files_params: _magneto_pb2.RestoreFilesParams
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    ignore_set_attr_error: bool
    create_view: bool
    fail_progress_monitor_on_already_exists_error: bool
    restore_info: _magneto_pb2.RestoreInfoProto
    previous_restore_info: _magneto_pb2.RestoreInfoProto
    restore_vmware_vm_params: _vmware_common_pb2.RestoreVMwareVMParams
    restore_hyperv_vm_params: _magneto_pb2.RestoreHyperVVMParams
    restore_acropolis_vms_params: _magneto_pb2.RestoreAcropolisVMsParams
    restore_kvm_vms_params: _magneto_pb2.RestoreKVMVMsParams
    restore_outlook_params: _magneto_pb2.RestoreOutlookParams
    user_info: _permissions_pb2.UserInformation
    mount_volumes_params: _magneto_pb2.MountVolumesParams
    mount_volumes_info: _magneto_pb2.MountVolumesInfoProto
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    new_aws_convert_and_deploy_ready: bool
    skip_image_deploy: bool
    recover_volumes_params: _magneto_pb2.RecoverVolumesParams
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    should_request_permit: bool
    recover_virtual_disk_params: _magneto_pb2.RecoverVirtualDiskParams
    recover_virtual_disk_info: _magneto_pb2.RecoverVirtualDiskInfoProto
    restore_kubernetes_namespaces_params: _magneto_pb2.RestoreKubernetesNamespacesParams
    nosql_connect_params: _magneto_pb2.NoSqlConnectParams
    nosql_recover_job_params: _nosql_pb2.NoSqlRecoverJobParams
    uda_recover_job_params: _uda_pb2.UdaRecoverJobParams
    restore_one_drive_params: _magneto_pb2.RestoreOneDriveParams
    preserve_tags: bool
    view_params: _master_pb2.ViewParams
    include_vm_config: bool
    uptier_task: bool
    job_id: int
    job_name: str
    job_instance_id: int
    restore_site_params: _magneto_pb2.RestoreSiteParams
    restore_public_folders_params: _magneto_pb2.RestoreO365PublicFoldersParams
    restore_teams_params: _magneto_pb2.RestoreO365TeamsParams
    restore_groups_params: _magneto_pb2.RestoreO365GroupsParams
    conversion_params: _master_pb2.ConversionParams
    sfdc_recover_job_params: _sfdc_pb2.SfdcRecoverJobParams
    restore_s3_params: _magneto_pb2.RestoreS3Params
    restore_san_params: _magneto_pb2.RestoreSanParams
    download_chats_params: _magneto_pb2.DownloadChatsParams
    source_view_name_DEPRECATED: str
    action_executor_target_type: _enums_pb2.TargetType.Type
    proxy_machine_details: StartRestoreTaskArg.ProxyMachineDetails
    is_powershell_task: bool
    is_object_protection: bool
    storage_array_snapshot: bool
    skip_rigel_for_restore: bool
    skip_mbx_permit_for_pst: bool
    data_transfer_info: _env_params_pb2_1.DataTransferInfo
    parent_restore_job_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., task_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., restore_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., cancellation_requested: bool = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., restore_type: _Optional[_Union[StartRestoreTaskArg.RestoreType, str]] = ..., entities: _Optional[_Iterable[_Union[StartRestoreTaskArg.RestoreEntity, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., rename_restored_object_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., rename_restored_vapp_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., power_on: bool = ..., continue_restore_on_error: bool = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_volume_info_pb2.VolumeInfo, _Mapping]]] = ..., additional_params: _Optional[_Union[_magneto_pb2.RestoreTaskAdditionalParams, _Mapping]] = ..., custom_tag_vec: _Optional[_Iterable[_Union[_cloud_deploy_pb2.CustomTag, _Mapping]]] = ..., skip_cloning_view: bool = ..., restored_data_storage_domain_id: _Optional[int] = ..., restore_files_params: _Optional[_Union[_magneto_pb2.RestoreFilesParams, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ..., ignore_set_attr_error: bool = ..., create_view: bool = ..., fail_progress_monitor_on_already_exists_error: bool = ..., restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ..., previous_restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ..., restore_vmware_vm_params: _Optional[_Union[_vmware_common_pb2.RestoreVMwareVMParams, _Mapping]] = ..., restore_hyperv_vm_params: _Optional[_Union[_magneto_pb2.RestoreHyperVVMParams, _Mapping]] = ..., restore_acropolis_vms_params: _Optional[_Union[_magneto_pb2.RestoreAcropolisVMsParams, _Mapping]] = ..., restore_kvm_vms_params: _Optional[_Union[_magneto_pb2.RestoreKVMVMsParams, _Mapping]] = ..., restore_outlook_params: _Optional[_Union[_magneto_pb2.RestoreOutlookParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., mount_volumes_params: _Optional[_Union[_magneto_pb2.MountVolumesParams, _Mapping]] = ..., mount_volumes_info: _Optional[_Union[_magneto_pb2.MountVolumesInfoProto, _Mapping]] = ..., deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ..., new_aws_convert_and_deploy_ready: bool = ..., skip_image_deploy: bool = ..., recover_volumes_params: _Optional[_Union[_magneto_pb2.RecoverVolumesParams, _Mapping]] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., should_request_permit: bool = ..., recover_virtual_disk_params: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskParams, _Mapping]] = ..., recover_virtual_disk_info: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskInfoProto, _Mapping]] = ..., restore_kubernetes_namespaces_params: _Optional[_Union[_magneto_pb2.RestoreKubernetesNamespacesParams, _Mapping]] = ..., nosql_connect_params: _Optional[_Union[_magneto_pb2.NoSqlConnectParams, _Mapping]] = ..., nosql_recover_job_params: _Optional[_Union[_nosql_pb2.NoSqlRecoverJobParams, _Mapping]] = ..., uda_recover_job_params: _Optional[_Union[_uda_pb2.UdaRecoverJobParams, _Mapping]] = ..., restore_one_drive_params: _Optional[_Union[_magneto_pb2.RestoreOneDriveParams, _Mapping]] = ..., preserve_tags: bool = ..., view_params: _Optional[_Union[_master_pb2.ViewParams, _Mapping]] = ..., include_vm_config: bool = ..., uptier_task: bool = ..., job_id: _Optional[int] = ..., job_name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., restore_site_params: _Optional[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]] = ..., restore_public_folders_params: _Optional[_Union[_magneto_pb2.RestoreO365PublicFoldersParams, _Mapping]] = ..., restore_teams_params: _Optional[_Union[_magneto_pb2.RestoreO365TeamsParams, _Mapping]] = ..., restore_groups_params: _Optional[_Union[_magneto_pb2.RestoreO365GroupsParams, _Mapping]] = ..., conversion_params: _Optional[_Union[_master_pb2.ConversionParams, _Mapping]] = ..., sfdc_recover_job_params: _Optional[_Union[_sfdc_pb2.SfdcRecoverJobParams, _Mapping]] = ..., restore_s3_params: _Optional[_Union[_magneto_pb2.RestoreS3Params, _Mapping]] = ..., restore_san_params: _Optional[_Union[_magneto_pb2.RestoreSanParams, _Mapping]] = ..., download_chats_params: _Optional[_Union[_magneto_pb2.DownloadChatsParams, _Mapping]] = ..., source_view_name_DEPRECATED: _Optional[str] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., proxy_machine_details: _Optional[_Union[StartRestoreTaskArg.ProxyMachineDetails, _Mapping]] = ..., is_powershell_task: bool = ..., is_object_protection: bool = ..., storage_array_snapshot: bool = ..., skip_rigel_for_restore: bool = ..., skip_mbx_permit_for_pst: bool = ..., data_transfer_info: _Optional[_Union[_env_params_pb2_1.DataTransferInfo, _Mapping]] = ..., parent_restore_job_id: _Optional[int] = ...) -> None: ...

class StartRestoreTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "expected_slave_incarnation_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    expected_slave_incarnation_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., expected_slave_incarnation_id: _Optional[int] = ...) -> None: ...

class CancelRestoreTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartDestroyCloneTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "restore_type", "task_id", "perform_clone_task_id", "connector_params", "view_box_id", "view_box_deleted", "view_name", "delete_view", "folder_entity", "datastore_entity", "destroy_clone_vm_task_info", "destroy_mount_volumes_task_info", "destroy_clone_app_task_info", "agent_info", "deploy_vms_to_cloud_params", "force_delete", "vcd_config", "action_executor_target_type", "user_info")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_DELETED_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_VM_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_MOUNT_VOLUMES_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    restore_type: _magneto_pb2.RestoreType.Type
    task_id: int
    perform_clone_task_id: int
    connector_params: _magneto_pb2.ConnectorParams
    view_box_id: int
    view_box_deleted: bool
    view_name: str
    delete_view: bool
    folder_entity: _entity_pb2.EntityProto
    datastore_entity: _entity_pb2.EntityProto
    destroy_clone_vm_task_info: _magneto_pb2.DestroyClonedVMTaskInfoProto
    destroy_mount_volumes_task_info: _magneto_pb2.DestroyMountVolumesTaskInfoProto
    destroy_clone_app_task_info: _magneto_pb2.DestroyCloneAppTaskInfoProto
    agent_info: _agent_pb2.AgentInfoProto
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    force_delete: bool
    vcd_config: _master_pb2.RestoredObjectVCDConfigProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_type: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., task_id: _Optional[int] = ..., perform_clone_task_id: _Optional[int] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_box_deleted: bool = ..., view_name: _Optional[str] = ..., delete_view: bool = ..., folder_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., destroy_clone_vm_task_info: _Optional[_Union[_magneto_pb2.DestroyClonedVMTaskInfoProto, _Mapping]] = ..., destroy_mount_volumes_task_info: _Optional[_Union[_magneto_pb2.DestroyMountVolumesTaskInfoProto, _Mapping]] = ..., destroy_clone_app_task_info: _Optional[_Union[_magneto_pb2.DestroyCloneAppTaskInfoProto, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ..., force_delete: bool = ..., vcd_config: _Optional[_Union[_master_pb2.RestoredObjectVCDConfigProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class StartDestroyCloneTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartDeactivateJobEntitiesArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "type", "task_id", "connector_params", "deactivate_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    type: _enums_pb2.Environment.Type
    task_id: int
    connector_params: _magneto_pb2.ConnectorParams
    deactivate_info: _magneto_pb2.DeactivateJobEntitiesInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., task_id: _Optional[int] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., deactivate_info: _Optional[_Union[_magneto_pb2.DeactivateJobEntitiesInfoProto, _Mapping]] = ...) -> None: ...

class StartDeactivateJobEntitiesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupDiskUpdateArg(_message.Message):
    __slots__ = ("task_start_time_usecs", "read_start_time_usecs", "read_end_time_usecs", "write_start_time_usecs", "write_end_time_usecs", "total_read_time_usecs", "total_write_time_usecs", "total_bytes_read", "error", "transport_mode")
    TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WRITE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    task_start_time_usecs: int
    read_start_time_usecs: int
    read_end_time_usecs: int
    write_start_time_usecs: int
    write_end_time_usecs: int
    total_read_time_usecs: int
    total_write_time_usecs: int
    total_bytes_read: int
    error: _error_pb2.ErrorProto
    transport_mode: str
    def __init__(self, task_start_time_usecs: _Optional[int] = ..., read_start_time_usecs: _Optional[int] = ..., read_end_time_usecs: _Optional[int] = ..., write_start_time_usecs: _Optional[int] = ..., write_end_time_usecs: _Optional[int] = ..., total_read_time_usecs: _Optional[int] = ..., total_write_time_usecs: _Optional[int] = ..., total_bytes_read: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., transport_mode: _Optional[str] = ...) -> None: ...

class EndSubTaskUpdateArg(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class RestoreDiskUpdateArg(_message.Message):
    __slots__ = ("task_start_time_usecs", "read_start_time_usecs", "read_end_time_usecs", "write_start_time_usecs", "write_end_time_usecs", "total_read_time_usecs", "total_write_time_usecs", "total_bytes_written", "error")
    TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WRITE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_start_time_usecs: int
    read_start_time_usecs: int
    read_end_time_usecs: int
    write_start_time_usecs: int
    write_end_time_usecs: int
    total_read_time_usecs: int
    total_write_time_usecs: int
    total_bytes_written: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_start_time_usecs: _Optional[int] = ..., read_start_time_usecs: _Optional[int] = ..., read_end_time_usecs: _Optional[int] = ..., write_start_time_usecs: _Optional[int] = ..., write_end_time_usecs: _Optional[int] = ..., total_read_time_usecs: _Optional[int] = ..., total_write_time_usecs: _Optional[int] = ..., total_bytes_written: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateDatastoreLatenciesArg(_message.Message):
    __slots__ = ("api_version", "registered_entity", "timestamp_usecs", "datastore_latencies")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_LATENCIES_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    registered_entity: _entity_pb2.EntityProto
    timestamp_usecs: int
    datastore_latencies: _magneto_pb2.DatastoreLatencies
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., registered_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., timestamp_usecs: _Optional[int] = ..., datastore_latencies: _Optional[_Union[_magneto_pb2.DatastoreLatencies, _Mapping]] = ...) -> None: ...

class UpdateDatastoreLatenciesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermitTaskUpdateArg(_message.Message):
    __slots__ = ("api_version", "task", "constituent_id", "target_type", "proxy_info", "o365_granted_resource_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    O365_GRANTED_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task: _gatekeeper_pb2.Task
    constituent_id: int
    target_type: _enums_pb2.TargetType.Type
    proxy_info: _proxy_pb2.ProxyInfo
    o365_granted_resource_vec: _containers.RepeatedCompositeFieldContainer[_gatekeeper_pb2.TaskState.O365Grant]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., constituent_id: _Optional[int] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ..., o365_granted_resource_vec: _Optional[_Iterable[_Union[_gatekeeper_pb2.TaskState.O365Grant, _Mapping]]] = ...) -> None: ...

class PermitTaskUpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExecRemoteReplicationActionsArg(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _remote_actions_pb2.RemoteReplicationActions
    def __init__(self, actions: _Optional[_Union[_remote_actions_pb2.RemoteReplicationActions, _Mapping]] = ...) -> None: ...

class ExecRemoteReplicationActionsResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _remote_actions_pb2.RemoteReplicationActionsResult
    def __init__(self, result: _Optional[_Union[_remote_actions_pb2.RemoteReplicationActionsResult, _Mapping]] = ...) -> None: ...

class StartVerifyEntityRegistrationArg(_message.Message):
    __slots__ = ("api_version", "task_id", "connector_params", "registration", "user_info", "is_fci_node_multiregistration_enabled")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_NODE_MULTIREGISTRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    connector_params: _magneto_pb2.ConnectorParams
    registration: _master_pb2.EntityRegistrationInfoProto
    user_info: _permissions_pb2.UserInformation
    is_fci_node_multiregistration_enabled: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., registration: _Optional[_Union[_master_pb2.EntityRegistrationInfoProto, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., is_fci_node_multiregistration_enabled: bool = ...) -> None: ...

class StartVerifyEntityRegistrationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartConversionTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "request_sequencer", "task_id", "conversion_params", "conversion_info_proto", "action_executor_target_type")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    request_sequencer: int
    task_id: int
    conversion_params: _master_pb2.ConversionParams
    conversion_info_proto: _magneto_pb2.ConversionInfoProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., task_id: _Optional[int] = ..., conversion_params: _Optional[_Union[_master_pb2.ConversionParams, _Mapping]] = ..., conversion_info_proto: _Optional[_Union[_magneto_pb2.ConversionInfoProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ...) -> None: ...

class StartConversionTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartCloudDeployTaskArg(_message.Message):
    __slots__ = ("api_version", "task_type", "expected_slave_incarnation_id", "request_sequencer", "env_type", "task_id", "task_uid", "parent_source", "connector_params", "cancellation_requested", "source_entities", "view_box_id", "view_name", "error", "progress_monitor_task_path", "deploy_vms_to_cloud_params", "cloud_deploy_info", "incremental_processing_enabled", "action_executor_target_type", "fail_progress_monitor_on_already_exists_error")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kConvertVMs: _ClassVar[StartCloudDeployTaskArg.Type]
        kDeployVMs: _ClassVar[StartCloudDeployTaskArg.Type]
        kReplicateSnapshots: _ClassVar[StartCloudDeployTaskArg.Type]
    kConvertVMs: StartCloudDeployTaskArg.Type
    kDeployVMs: StartCloudDeployTaskArg.Type
    kReplicateSnapshots: StartCloudDeployTaskArg.Type
    class SourceEntity(_message.Message):
        __slots__ = ("entity", "root_entity", "view_name", "snapshot_relative_dir_path", "progress_monitor_task_path", "job_id", "job_uid", "name", "job_instance_id", "job_start_time_usecs", "attempt_num", "failed_over", "snapshot_info", "replication_info", "retrieve_archive_view_name", "previous_cloud_deploy_info", "connector_params")
        class PreviousCloudDeployInfo(_message.Message):
            __slots__ = ("snapshot_relative_dir_path", "cloud_deploy_info")
            SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
            CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
            snapshot_relative_dir_path: str
            cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto.CloudDeployEntity
            def __init__(self, snapshot_relative_dir_path: _Optional[str] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto.CloudDeployEntity, _Mapping]] = ...) -> None: ...
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
        FAILED_OVER_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        RETRIEVE_ARCHIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        root_entity: _entity_pb2.EntityProto
        view_name: str
        snapshot_relative_dir_path: str
        progress_monitor_task_path: str
        job_id: int
        job_uid: _universal_id_pb2.UniversalIdProto
        name: str
        job_instance_id: int
        job_start_time_usecs: int
        attempt_num: int
        failed_over: bool
        snapshot_info: _magneto_pb2.SnapshotInfoProto
        replication_info: _magneto_pb2.CloudDeployInfoProto
        retrieve_archive_view_name: str
        previous_cloud_deploy_info: StartCloudDeployTaskArg.SourceEntity.PreviousCloudDeployInfo
        connector_params: _magneto_pb2.ConnectorParams
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., failed_over: bool = ..., snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., replication_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., retrieve_archive_view_name: _Optional[str] = ..., previous_cloud_deploy_info: _Optional[_Union[StartCloudDeployTaskArg.SourceEntity.PreviousCloudDeployInfo, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_PROCESSING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAIL_PROGRESS_MONITOR_ON_ALREADY_EXISTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_type: StartCloudDeployTaskArg.Type
    expected_slave_incarnation_id: int
    request_sequencer: int
    env_type: _enums_pb2.Environment.Type
    task_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    parent_source: _entity_pb2.EntityProto
    connector_params: _magneto_pb2.ConnectorParams
    cancellation_requested: bool
    source_entities: _containers.RepeatedCompositeFieldContainer[StartCloudDeployTaskArg.SourceEntity]
    view_box_id: int
    view_name: str
    error: _error_pb2_1.ErrorProto
    progress_monitor_task_path: str
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    incremental_processing_enabled: bool
    action_executor_target_type: _enums_pb2.TargetType.Type
    fail_progress_monitor_on_already_exists_error: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_type: _Optional[_Union[StartCloudDeployTaskArg.Type, str]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., request_sequencer: _Optional[int] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., task_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., cancellation_requested: bool = ..., source_entities: _Optional[_Iterable[_Union[StartCloudDeployTaskArg.SourceEntity, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., incremental_processing_enabled: bool = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., fail_progress_monitor_on_already_exists_error: bool = ...) -> None: ...

class StartCloudDeployTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelCloudDeployTaskArg(_message.Message):
    __slots__ = ("api_version", "expected_slave_incarnation_id", "task_id", "task_uid")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    expected_slave_incarnation_id: int
    task_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., expected_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelCloudDeployTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
