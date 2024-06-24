from bridge.base import error_pb2 as _error_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.api.common import entity_operations_pb2 as _entity_operations_pb2
from magneto.api.common import oracle_pb2 as _oracle_pb2
from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import cloud_deploy_pb2 as _cloud_deploy_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.base.entities import exchange_pb2 as _exchange_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.base import gatekeeper_pb2 as _gatekeeper_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1_1
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base import uda_pb2 as _uda_pb2
from magneto.base import vmware_common_pb2 as _vmware_common_pb2
from magneto.connectors.ms_graph import graph_external_pb2 as _graph_external_pb2
from magneto.master.base import master_cdp_pb2 as _master_cdp_pb2
from magneto.master.base import master_standby_pb2 as _master_standby_pb2
from magneto.master.base import enums_pb2 as _enums_pb2_1
from magneto.master.base import summary_pb2 as _summary_pb2
from magneto.utils import capability_pb2 as _capability_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APIRequestAttr(_message.Message):
    __slots__ = ("type", "timeout_secs", "use_read_replica")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUIUser: _ClassVar[APIRequestAttr.Type]
        kUIAuto: _ClassVar[APIRequestAttr.Type]
        kUserReport: _ClassVar[APIRequestAttr.Type]
        kDataCollection: _ClassVar[APIRequestAttr.Type]
        kMagnetoInternal: _ClassVar[APIRequestAttr.Type]
        kHelios: _ClassVar[APIRequestAttr.Type]
    kUIUser: APIRequestAttr.Type
    kUIAuto: APIRequestAttr.Type
    kUserReport: APIRequestAttr.Type
    kDataCollection: APIRequestAttr.Type
    kMagnetoInternal: APIRequestAttr.Type
    kHelios: APIRequestAttr.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    USE_READ_REPLICA_FIELD_NUMBER: _ClassVar[int]
    type: APIRequestAttr.Type
    timeout_secs: int
    use_read_replica: bool
    def __init__(self, type: _Optional[_Union[APIRequestAttr.Type, str]] = ..., timeout_secs: _Optional[int] = ..., use_read_replica: bool = ...) -> None: ...

class BackupJobTaskStateBaseProto(_message.Message):
    __slots__ = ("type", "job_id", "job_uid", "primary_job_uid", "perform_source_side_dedup", "enable_brick_level_checksum", "dedup_disabled_source_id_vec", "job_instance_id", "attempt_num", "view_box_id", "view_name", "inode_id_floor", "status", "public_status", "waiting_reason", "error", "warnings", "user_message", "cancellation_requested", "cancellation_reason", "entity_ids_to_cancel", "pause_state", "sources", "start_time_usecs", "admitted_time_usecs", "end_time_usecs", "permit_grant_time_usecs", "subtask_to_permit_grant_time_usecs_map_DEPRECATED", "total_source_size_bytes", "total_bytes_read_from_source", "total_bytes_to_read_from_source", "total_bytes_tiered", "total_logical_backup_size_bytes", "total_usage_size_bytes", "is_tiering_goal_met", "stats_counter_id", "total_physical_backup_size_bytes", "sla_violated", "sla_deadline_time_usecs", "quiesce", "continue_on_quiesce_failure", "is_full_backup", "is_autoprotect", "backup_type", "progress_monitor_task_path", "global_include_exclude", "source_filters", "physical_file_parallel_backup_enabled", "successfully_protected_entities", "perform_brick_based_dedup", "total_pause_time_usecs", "network_realm_id", "connector_group_id")
    class EntityIdsToCancelEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _enums_pb2_1.CancellationReason.Type
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_enums_pb2_1.CancellationReason.Type, str]] = ...) -> None: ...
    class PauseState(_message.Message):
        __slots__ = ("status", "user_initiated_pause_requested_time_usecs", "blackout_window_pause_requested_time_usecs", "user_initiated_resume_during_blackout_window")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        USER_INITIATED_PAUSE_REQUESTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        BLACKOUT_WINDOW_PAUSE_REQUESTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        USER_INITIATED_RESUME_DURING_BLACKOUT_WINDOW_FIELD_NUMBER: _ClassVar[int]
        status: _enums_pb2_1.PauseStatus.Type
        user_initiated_pause_requested_time_usecs: int
        blackout_window_pause_requested_time_usecs: int
        user_initiated_resume_during_blackout_window: bool
        def __init__(self, status: _Optional[_Union[_enums_pb2_1.PauseStatus.Type, str]] = ..., user_initiated_pause_requested_time_usecs: _Optional[int] = ..., blackout_window_pause_requested_time_usecs: _Optional[int] = ..., user_initiated_resume_during_blackout_window: bool = ...) -> None: ...
    class SourceState(_message.Message):
        __slots__ = ("source", "attempt_source_vec", "backup_source_params", "scheduled_time_usecs", "next_run_advancement_time_secs", "protected_entities")
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_SOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        NEXT_RUN_ADVANCEMENT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        source: _entity_pb2.EntityProto
        attempt_source_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        backup_source_params: _env_params_pb2_1_1.BackupSourceParams
        scheduled_time_usecs: int
        next_run_advancement_time_secs: int
        protected_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        def __init__(self, source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., attempt_source_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., backup_source_params: _Optional[_Union[_env_params_pb2_1_1.BackupSourceParams, _Mapping]] = ..., scheduled_time_usecs: _Optional[int] = ..., next_run_advancement_time_secs: _Optional[int] = ..., protected_entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
    class SubtaskToPermitGrantTimeUsecsMapDEPRECATEDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_SOURCE_SIDE_DEDUP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DISABLED_SOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    WAITING_REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_TO_CANCEL_FIELD_NUMBER: _ClassVar[int]
    PAUSE_STATE_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ADMITTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_GRANT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SUBTASK_TO_PERMIT_GRANT_TIME_USECS_MAP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SOURCE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TIERED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_USAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_TIERING_GOAL_MET_FIELD_NUMBER: _ClassVar[int]
    STATS_COUNTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
    SLA_DEADLINE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_QUIESCE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOPROTECT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INCLUDE_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_FILE_PARALLEL_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFULLY_PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PERFORM_BRICK_BASED_DEDUP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAUSE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    job_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    primary_job_uid: _universal_id_pb2.UniversalIdProto
    perform_source_side_dedup: bool
    enable_brick_level_checksum: bool
    dedup_disabled_source_id_vec: _containers.RepeatedScalarFieldContainer[int]
    job_instance_id: int
    attempt_num: int
    view_box_id: int
    view_name: str
    inode_id_floor: int
    status: _enums_pb2_1.BackupJobTaskStatus
    public_status: _enums_pb2.PublicTaskStatus.Type
    waiting_reason: str
    error: _error_pb2_1.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    user_message: str
    cancellation_requested: bool
    cancellation_reason: _enums_pb2_1.CancellationReason.Type
    entity_ids_to_cancel: _containers.ScalarMap[int, _enums_pb2_1.CancellationReason.Type]
    pause_state: BackupJobTaskStateBaseProto.PauseState
    sources: _containers.RepeatedCompositeFieldContainer[BackupJobTaskStateBaseProto.SourceState]
    start_time_usecs: int
    admitted_time_usecs: int
    end_time_usecs: int
    permit_grant_time_usecs: int
    subtask_to_permit_grant_time_usecs_map_DEPRECATED: _containers.ScalarMap[int, int]
    total_source_size_bytes: int
    total_bytes_read_from_source: int
    total_bytes_to_read_from_source: int
    total_bytes_tiered: int
    total_logical_backup_size_bytes: int
    total_usage_size_bytes: int
    is_tiering_goal_met: bool
    stats_counter_id: str
    total_physical_backup_size_bytes: int
    sla_violated: bool
    sla_deadline_time_usecs: int
    quiesce: bool
    continue_on_quiesce_failure: bool
    is_full_backup: bool
    is_autoprotect: bool
    backup_type: _enums_pb2.ScheduledBackupType.Type
    progress_monitor_task_path: str
    global_include_exclude: _env_params_pb2_1_1.PhysicalFileBackupParams.GlobalIncludeExclude
    source_filters: _magneto_pb2.SourceFilters
    physical_file_parallel_backup_enabled: bool
    successfully_protected_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    perform_brick_based_dedup: bool
    total_pause_time_usecs: int
    network_realm_id: int
    connector_group_id: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., primary_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., perform_source_side_dedup: bool = ..., enable_brick_level_checksum: bool = ..., dedup_disabled_source_id_vec: _Optional[_Iterable[int]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., inode_id_floor: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2_1.BackupJobTaskStatus, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., waiting_reason: _Optional[str] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., user_message: _Optional[str] = ..., cancellation_requested: bool = ..., cancellation_reason: _Optional[_Union[_enums_pb2_1.CancellationReason.Type, str]] = ..., entity_ids_to_cancel: _Optional[_Mapping[int, _enums_pb2_1.CancellationReason.Type]] = ..., pause_state: _Optional[_Union[BackupJobTaskStateBaseProto.PauseState, _Mapping]] = ..., sources: _Optional[_Iterable[_Union[BackupJobTaskStateBaseProto.SourceState, _Mapping]]] = ..., start_time_usecs: _Optional[int] = ..., admitted_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., permit_grant_time_usecs: _Optional[int] = ..., subtask_to_permit_grant_time_usecs_map_DEPRECATED: _Optional[_Mapping[int, int]] = ..., total_source_size_bytes: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., total_bytes_to_read_from_source: _Optional[int] = ..., total_bytes_tiered: _Optional[int] = ..., total_logical_backup_size_bytes: _Optional[int] = ..., total_usage_size_bytes: _Optional[int] = ..., is_tiering_goal_met: bool = ..., stats_counter_id: _Optional[str] = ..., total_physical_backup_size_bytes: _Optional[int] = ..., sla_violated: bool = ..., sla_deadline_time_usecs: _Optional[int] = ..., quiesce: bool = ..., continue_on_quiesce_failure: bool = ..., is_full_backup: bool = ..., is_autoprotect: bool = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., progress_monitor_task_path: _Optional[str] = ..., global_include_exclude: _Optional[_Union[_env_params_pb2_1_1.PhysicalFileBackupParams.GlobalIncludeExclude, _Mapping]] = ..., source_filters: _Optional[_Union[_magneto_pb2.SourceFilters, _Mapping]] = ..., physical_file_parallel_backup_enabled: bool = ..., successfully_protected_entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., perform_brick_based_dedup: bool = ..., total_pause_time_usecs: _Optional[int] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ...) -> None: ...

class BackupTaskStateProto(_message.Message):
    __slots__ = ("base", "task_id", "task_version", "parent_source", "space_usage_policy", "scheduled_constituent_id", "scheduled_gandalf_session_id", "previous_snapshot_info", "previous_backup_size", "previous_run_start_time_usecs", "reconsider_chosen_prev_snapshot", "storage_snapshot_info", "current_snapshot_info", "snapshot_delta", "use_uuid_to_match_previous_vmdk", "use_uuid_for_encoded_filename", "backup_verified", "stats_container_id", "agent_incarnation_id", "qos_principal_name", "additional_params", "rx_replication_error", "query_changed_blocks_error", "san_transport_error", "snapshot_deleted", "app_entity_state_vec", "vapp_info", "in_progress_state", "action_executor_target_type", "slave_task_state_in_scribe_setting", "transient_host_entity", "transient_datacenter_entity", "transient_connector_params", "transient_vcd_connector_params", "entity_backup_stats", "limit_resource_hogging_by_single_task", "adapter_specific_flags")
    class AppEntityState(_message.Message):
        __slots__ = ("app_entity", "public_status", "error", "warnings", "progress_monitor_task_path", "total_logical_bytes", "total_bytes_read_from_source", "start_time_usecs", "end_time_usecs", "relative_snapshot_dir")
        APP_ENTITY_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
        app_entity: _entity_pb2.EntityProto
        public_status: _enums_pb2.PublicTaskStatus.Type
        error: _error_pb2_1.ErrorProto
        warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
        progress_monitor_task_path: str
        total_logical_bytes: int
        total_bytes_read_from_source: int
        start_time_usecs: int
        end_time_usecs: int
        relative_snapshot_dir: str
        def __init__(self, app_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., progress_monitor_task_path: _Optional[str] = ..., total_logical_bytes: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...
    class InProgressTaskStateProto(_message.Message):
        __slots__ = ("acquired_app_entity_lock_vec",)
        ACQUIRED_APP_ENTITY_LOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        acquired_app_entity_lock_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        def __init__(self, acquired_app_entity_lock_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
    class EntityBackupStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _magneto_external_base_pb2.EntityBackupStats
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_magneto_external_base_pb2.EntityBackupStats, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SPACE_USAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RECONSIDER_CHOSEN_PREV_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELTA_FIELD_NUMBER: _ClassVar[int]
    USE_UUID_TO_MATCH_PREVIOUS_VMDK_FIELD_NUMBER: _ClassVar[int]
    USE_UUID_FOR_ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RX_REPLICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUERY_CHANGED_BLOCKS_ERROR_FIELD_NUMBER: _ClassVar[int]
    SAN_TRANSPORT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETED_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_STATE_IN_SCRIBE_SETTING_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_DATACENTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_VCD_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BACKUP_STATS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_RESOURCE_HOGGING_BY_SINGLE_TASK_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_SPECIFIC_FLAGS_FIELD_NUMBER: _ClassVar[int]
    base: BackupJobTaskStateBaseProto
    task_id: int
    task_version: int
    parent_source: _entity_pb2.EntityProto
    space_usage_policy: _magneto_pb2.SpaceUsagePolicy
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    previous_snapshot_info: _magneto_pb2.SnapshotInfoProto
    previous_backup_size: int
    previous_run_start_time_usecs: int
    reconsider_chosen_prev_snapshot: bool
    storage_snapshot_info: _storage_pb2.EntitySnapshotInfoProto
    current_snapshot_info: _magneto_pb2.SnapshotInfoProto
    snapshot_delta: _magneto_pb2.SnapshotDeltaProto
    use_uuid_to_match_previous_vmdk: bool
    use_uuid_for_encoded_filename: bool
    backup_verified: bool
    stats_container_id: int
    agent_incarnation_id: int
    qos_principal_name: str
    additional_params: _magneto_pb2.BackupTaskAdditionalParams
    rx_replication_error: _error_pb2_1.ErrorProto
    query_changed_blocks_error: bool
    san_transport_error: bool
    snapshot_deleted: bool
    app_entity_state_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskStateProto.AppEntityState]
    vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
    in_progress_state: BackupTaskStateProto.InProgressTaskStateProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    slave_task_state_in_scribe_setting: _enums_pb2_1.TaskStateInScribeSetting
    transient_host_entity: _entity_pb2.EntityProto
    transient_datacenter_entity: _entity_pb2.EntityProto
    transient_connector_params: _magneto_pb2.ConnectorParams
    transient_vcd_connector_params: _magneto_pb2.ConnectorParams
    entity_backup_stats: _containers.MessageMap[int, _magneto_external_base_pb2.EntityBackupStats]
    limit_resource_hogging_by_single_task: bool
    adapter_specific_flags: _magneto_pb2.AdapterSpecificFlagsProto
    def __init__(self, base: _Optional[_Union[BackupJobTaskStateBaseProto, _Mapping]] = ..., task_id: _Optional[int] = ..., task_version: _Optional[int] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., space_usage_policy: _Optional[_Union[_magneto_pb2.SpaceUsagePolicy, _Mapping]] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., previous_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., previous_backup_size: _Optional[int] = ..., previous_run_start_time_usecs: _Optional[int] = ..., reconsider_chosen_prev_snapshot: bool = ..., storage_snapshot_info: _Optional[_Union[_storage_pb2.EntitySnapshotInfoProto, _Mapping]] = ..., current_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., snapshot_delta: _Optional[_Union[_magneto_pb2.SnapshotDeltaProto, _Mapping]] = ..., use_uuid_to_match_previous_vmdk: bool = ..., use_uuid_for_encoded_filename: bool = ..., backup_verified: bool = ..., stats_container_id: _Optional[int] = ..., agent_incarnation_id: _Optional[int] = ..., qos_principal_name: _Optional[str] = ..., additional_params: _Optional[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]] = ..., rx_replication_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., query_changed_blocks_error: bool = ..., san_transport_error: bool = ..., snapshot_deleted: bool = ..., app_entity_state_vec: _Optional[_Iterable[_Union[BackupTaskStateProto.AppEntityState, _Mapping]]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ..., in_progress_state: _Optional[_Union[BackupTaskStateProto.InProgressTaskStateProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., slave_task_state_in_scribe_setting: _Optional[_Union[_enums_pb2_1.TaskStateInScribeSetting, str]] = ..., transient_host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., transient_datacenter_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., transient_connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., transient_vcd_connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., entity_backup_stats: _Optional[_Mapping[int, _magneto_external_base_pb2.EntityBackupStats]] = ..., limit_resource_hogging_by_single_task: bool = ..., adapter_specific_flags: _Optional[_Union[_magneto_pb2.AdapterSpecificFlagsProto, _Mapping]] = ...) -> None: ...

class BackupJobAttemptStateProto(_message.Message):
    __slots__ = ("base", "max_attempts", "first_attempt_start_time_usecs", "exclude_sources_DEPRECATED", "exclude_sources", "active_tasks", "finished_tasks", "num_successful_tasks", "num_failed_tasks", "num_cancelled_tasks", "num_skipped_tasks", "stats_containers_created", "storage_snapshot_task_id", "failed_to_schedule", "snapshots_deleted")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_ATTEMPT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOURCES_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_TASKS_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINERS_CREATED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    FAILED_TO_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    base: BackupJobTaskStateBaseProto
    max_attempts: int
    first_attempt_start_time_usecs: int
    exclude_sources_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    exclude_sources: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupJobProto.ExcludeSource]
    active_tasks: _containers.RepeatedCompositeFieldContainer[BackupTaskStateProto]
    finished_tasks: _containers.RepeatedCompositeFieldContainer[BackupTaskStateProto]
    num_successful_tasks: int
    num_failed_tasks: int
    num_cancelled_tasks: int
    num_skipped_tasks: int
    stats_containers_created: bool
    storage_snapshot_task_id: int
    failed_to_schedule: bool
    snapshots_deleted: bool
    def __init__(self, base: _Optional[_Union[BackupJobTaskStateBaseProto, _Mapping]] = ..., max_attempts: _Optional[int] = ..., first_attempt_start_time_usecs: _Optional[int] = ..., exclude_sources_DEPRECATED: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., exclude_sources: _Optional[_Iterable[_Union[_magneto_pb2.BackupJobProto.ExcludeSource, _Mapping]]] = ..., active_tasks: _Optional[_Iterable[_Union[BackupTaskStateProto, _Mapping]]] = ..., finished_tasks: _Optional[_Iterable[_Union[BackupTaskStateProto, _Mapping]]] = ..., num_successful_tasks: _Optional[int] = ..., num_failed_tasks: _Optional[int] = ..., num_cancelled_tasks: _Optional[int] = ..., num_skipped_tasks: _Optional[int] = ..., stats_containers_created: bool = ..., storage_snapshot_task_id: _Optional[int] = ..., failed_to_schedule: bool = ..., snapshots_deleted: bool = ...) -> None: ...

class BackupJobRunStateProto(_message.Message):
    __slots__ = ("base", "worm_retention", "source_env_type", "active_attempt", "finished_attempts", "snapshot_targets_DEPRECATED", "rx_replication_error", "is_out_of_band_run", "leverage_storage_snapshots", "leverage_san_transport", "leverage_nutanix_snapshots", "is_missed_run", "copy_snapshot_params_vec", "snapshots_deleted", "snapshots_deleted_timestamp_usecs", "metadata_deleted", "metadata_deleted_timestamp_usecs", "additional_param_vec", "blackout_window_action", "deadline_time_usecs", "env_backup_params", "yoda_progress_monitor_root_path", "origin_cluster_name", "dr_to_cloud_params", "additional_run_info", "run_label", "is_failover_run", "storage_array_snapshot", "run_timeout_vec", "task_timeout_vec", "latest_finished_tasks", "num_successful_tasks", "num_failed_tasks", "num_cancelled_tasks", "num_skipped_tasks", "num_app_instances", "num_successful_app_objects", "num_failed_app_objects", "num_cancelled_app_objects", "originator_type", "archive_job_uid", "retention_policy", "ignorable_errors_in_error_db", "oob_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGETS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RX_REPLICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_RUN_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_STORAGE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_NUTANIX_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    IS_MISSED_RUN_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    METADATA_DELETED_FIELD_NUMBER: _ClassVar[int]
    METADATA_DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_VEC_FIELD_NUMBER: _ClassVar[int]
    BLACKOUT_WINDOW_ACTION_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    YODA_PROGRESS_MONITOR_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DR_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_RUN_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    RUN_TIMEOUT_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_TIMEOUT_VEC_FIELD_NUMBER: _ClassVar[int]
    LATEST_FINISHED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    IGNORABLE_ERRORS_IN_ERROR_DB_FIELD_NUMBER: _ClassVar[int]
    OOB_UID_FIELD_NUMBER: _ClassVar[int]
    base: BackupJobTaskStateBaseProto
    worm_retention: _worm_pb2.WormRetentionProto
    source_env_type: _enums_pb2.Environment.Type
    active_attempt: BackupJobAttemptStateProto
    finished_attempts: _containers.RepeatedCompositeFieldContainer[BackupJobAttemptStateProto]
    snapshot_targets_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_policy_pb2.SnapshotTarget]
    rx_replication_error: _error_pb2_1.ErrorProto
    is_out_of_band_run: bool
    leverage_storage_snapshots: bool
    leverage_san_transport: bool
    leverage_nutanix_snapshots: bool
    is_missed_run: bool
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[CopySnapshotParams]
    snapshots_deleted: bool
    snapshots_deleted_timestamp_usecs: int
    metadata_deleted: bool
    metadata_deleted_timestamp_usecs: int
    additional_param_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupTaskAdditionalParams]
    blackout_window_action: _enums_pb2_1.BlackoutWindowAction.Type
    deadline_time_usecs: int
    env_backup_params: _env_params_pb2_1_1.EnvBackupParams
    yoda_progress_monitor_root_path: str
    origin_cluster_name: str
    dr_to_cloud_params: _magneto_pb2.BackupJobProto.DRToCloudParams
    additional_run_info: _magneto_pb2.AdditionalRunInfo
    run_label: str
    is_failover_run: bool
    storage_array_snapshot: bool
    run_timeout_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.CancellationTimeout]
    task_timeout_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.CancellationTimeout]
    latest_finished_tasks: _containers.RepeatedCompositeFieldContainer[BackupTaskStateProto]
    num_successful_tasks: int
    num_failed_tasks: int
    num_cancelled_tasks: int
    num_skipped_tasks: int
    num_app_instances: int
    num_successful_app_objects: int
    num_failed_app_objects: int
    num_cancelled_app_objects: int
    originator_type: _policy_pb2.SnapshotTarget.Type
    archive_job_uid: _universal_id_pb2.UniversalIdProto
    retention_policy: _policy_pb2.RetentionPolicyProto
    ignorable_errors_in_error_db: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    oob_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, base: _Optional[_Union[BackupJobTaskStateBaseProto, _Mapping]] = ..., worm_retention: _Optional[_Union[_worm_pb2.WormRetentionProto, _Mapping]] = ..., source_env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., active_attempt: _Optional[_Union[BackupJobAttemptStateProto, _Mapping]] = ..., finished_attempts: _Optional[_Iterable[_Union[BackupJobAttemptStateProto, _Mapping]]] = ..., snapshot_targets_DEPRECATED: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTarget, _Mapping]]] = ..., rx_replication_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., is_out_of_band_run: bool = ..., leverage_storage_snapshots: bool = ..., leverage_san_transport: bool = ..., leverage_nutanix_snapshots: bool = ..., is_missed_run: bool = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[CopySnapshotParams, _Mapping]]] = ..., snapshots_deleted: bool = ..., snapshots_deleted_timestamp_usecs: _Optional[int] = ..., metadata_deleted: bool = ..., metadata_deleted_timestamp_usecs: _Optional[int] = ..., additional_param_vec: _Optional[_Iterable[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]]] = ..., blackout_window_action: _Optional[_Union[_enums_pb2_1.BlackoutWindowAction.Type, str]] = ..., deadline_time_usecs: _Optional[int] = ..., env_backup_params: _Optional[_Union[_env_params_pb2_1_1.EnvBackupParams, _Mapping]] = ..., yoda_progress_monitor_root_path: _Optional[str] = ..., origin_cluster_name: _Optional[str] = ..., dr_to_cloud_params: _Optional[_Union[_magneto_pb2.BackupJobProto.DRToCloudParams, _Mapping]] = ..., additional_run_info: _Optional[_Union[_magneto_pb2.AdditionalRunInfo, _Mapping]] = ..., run_label: _Optional[str] = ..., is_failover_run: bool = ..., storage_array_snapshot: bool = ..., run_timeout_vec: _Optional[_Iterable[_Union[_policy_pb2.CancellationTimeout, _Mapping]]] = ..., task_timeout_vec: _Optional[_Iterable[_Union[_policy_pb2.CancellationTimeout, _Mapping]]] = ..., latest_finished_tasks: _Optional[_Iterable[_Union[BackupTaskStateProto, _Mapping]]] = ..., num_successful_tasks: _Optional[int] = ..., num_failed_tasks: _Optional[int] = ..., num_cancelled_tasks: _Optional[int] = ..., num_skipped_tasks: _Optional[int] = ..., num_app_instances: _Optional[int] = ..., num_successful_app_objects: _Optional[int] = ..., num_failed_app_objects: _Optional[int] = ..., num_cancelled_app_objects: _Optional[int] = ..., originator_type: _Optional[_Union[_policy_pb2.SnapshotTarget.Type, str]] = ..., archive_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ..., ignorable_errors_in_error_db: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., oob_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ScribeRowFooterInfoProto(_message.Message):
    __slots__ = ("magic_number", "size", "timestamp", "num_rows", "row_index")
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    ROW_INDEX_FIELD_NUMBER: _ClassVar[int]
    magic_number: int
    size: int
    timestamp: int
    num_rows: int
    row_index: int
    def __init__(self, magic_number: _Optional[int] = ..., size: _Optional[int] = ..., timestamp: _Optional[int] = ..., num_rows: _Optional[int] = ..., row_index: _Optional[int] = ...) -> None: ...

class CopyBackupSubTaskStateProto(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "run_start_time_usecs", "task_uid", "parent_task_uid", "ancestor_replication_uid_hint", "entity", "backup_task_id", "start_time_usecs", "end_time_usecs", "status", "public_status", "error", "cancellation_requested", "snapshot_target", "replication_info", "bridge_constituent_id", "progress_monitor_task_path", "disable_rx_megafile", "is_out_of_band_sub_task", "conversion_task_id", "conversion_cleanup_task_id", "should_convert", "cloud_deploy_task_state", "action_executor_target_type", "object_level_copy", "entity_vec", "onprem_deploy_task_state", "is_final_request", "fail_progress_monitor_on_already_exists_error", "copy_sub_task_timeout_mins", "total_duration_usecs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kScheduled: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kConversionPending: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kAssigned: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kAccepted: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kFinishing: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kFinished: _ClassVar[CopyBackupSubTaskStateProto.Status]
        kCancelled: _ClassVar[CopyBackupSubTaskStateProto.Status]
    kStarted: CopyBackupSubTaskStateProto.Status
    kScheduled: CopyBackupSubTaskStateProto.Status
    kConversionPending: CopyBackupSubTaskStateProto.Status
    kAssigned: CopyBackupSubTaskStateProto.Status
    kAccepted: CopyBackupSubTaskStateProto.Status
    kFinishing: CopyBackupSubTaskStateProto.Status
    kFinished: CopyBackupSubTaskStateProto.Status
    kCancelled: CopyBackupSubTaskStateProto.Status
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_UID_HINT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RX_MEGAFILE_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CLEANUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CONVERT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    ONPREM_DEPLOY_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FAIL_PROGRESS_MONITOR_ON_ALREADY_EXISTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    COPY_SUB_TASK_TIMEOUT_MINS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    run_start_time_usecs: int
    task_uid: _universal_id_pb2.UniversalIdProto
    parent_task_uid: _universal_id_pb2.UniversalIdProto
    ancestor_replication_uid_hint: _universal_id_pb2.UniversalIdProto
    entity: _entity_pb2.EntityProto
    backup_task_id: int
    start_time_usecs: int
    end_time_usecs: int
    status: CopyBackupSubTaskStateProto.Status
    public_status: _enums_pb2.PublicTaskStatus.Type
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    snapshot_target: _policy_pb2.SnapshotTarget
    replication_info: ReplicationInfoBase
    bridge_constituent_id: int
    progress_monitor_task_path: str
    disable_rx_megafile: bool
    is_out_of_band_sub_task: bool
    conversion_task_id: int
    conversion_cleanup_task_id: int
    should_convert: bool
    cloud_deploy_task_state: CloudDeployTaskStateProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    object_level_copy: bool
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    onprem_deploy_task_state: OnPremDeployTaskStateProto
    is_final_request: bool
    fail_progress_monitor_on_already_exists_error: bool
    copy_sub_task_timeout_mins: int
    total_duration_usecs: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., parent_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., ancestor_replication_uid_hint: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., backup_task_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status: _Optional[_Union[CopyBackupSubTaskStateProto.Status, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., replication_info: _Optional[_Union[ReplicationInfoBase, _Mapping]] = ..., bridge_constituent_id: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., disable_rx_megafile: bool = ..., is_out_of_band_sub_task: bool = ..., conversion_task_id: _Optional[int] = ..., conversion_cleanup_task_id: _Optional[int] = ..., should_convert: bool = ..., cloud_deploy_task_state: _Optional[_Union[CloudDeployTaskStateProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., object_level_copy: bool = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., onprem_deploy_task_state: _Optional[_Union[OnPremDeployTaskStateProto, _Mapping]] = ..., is_final_request: bool = ..., fail_progress_monitor_on_already_exists_error: bool = ..., copy_sub_task_timeout_mins: _Optional[int] = ..., total_duration_usecs: _Optional[int] = ...) -> None: ...

class PrimaryBackupRunStats(_message.Message):
    __slots__ = ("num_successful_tasks", "num_failed_tasks", "num_cancelled_tasks", "num_skipped_tasks", "num_successful_app_objects", "num_failed_app_objects", "num_cancelled_app_objects", "total_logical_backup_size_bytes", "total_bytes_read_from_source", "yoda_progress_monitor_root_path")
    NUM_SUCCESSFUL_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_TASKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    YODA_PROGRESS_MONITOR_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    num_successful_tasks: int
    num_failed_tasks: int
    num_cancelled_tasks: int
    num_skipped_tasks: int
    num_successful_app_objects: int
    num_failed_app_objects: int
    num_cancelled_app_objects: int
    total_logical_backup_size_bytes: int
    total_bytes_read_from_source: int
    yoda_progress_monitor_root_path: str
    def __init__(self, num_successful_tasks: _Optional[int] = ..., num_failed_tasks: _Optional[int] = ..., num_cancelled_tasks: _Optional[int] = ..., num_skipped_tasks: _Optional[int] = ..., num_successful_app_objects: _Optional[int] = ..., num_failed_app_objects: _Optional[int] = ..., num_cancelled_app_objects: _Optional[int] = ..., total_logical_backup_size_bytes: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., yoda_progress_monitor_root_path: _Optional[str] = ...) -> None: ...

class CopyObjectBaseInfo(_message.Message):
    __slots__ = ("entity", "public_status", "start_time_usecs", "end_time_usecs", "expiry_time_usecs", "legal_hold_enabled", "is_manually_deleted", "progress_monitor_task_path", "stats", "error", "warnings")
    class Stats(_message.Message):
        __slots__ = ("logical_size_bytes", "bytes_read_from_source", "logical_bytes_transferred", "physical_bytes_transferred", "avg_logical_transfer_rate_bps", "total_file_count", "total_changed_file_count", "file_walk_done", "front_end_size_info")
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CHANGED_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FILE_WALK_DONE_FIELD_NUMBER: _ClassVar[int]
        FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
        logical_size_bytes: int
        bytes_read_from_source: int
        logical_bytes_transferred: int
        physical_bytes_transferred: int
        avg_logical_transfer_rate_bps: int
        total_file_count: int
        total_changed_file_count: int
        file_walk_done: bool
        front_end_size_info: _stats_pb2.SizeInfo
        def __init__(self, logical_size_bytes: _Optional[int] = ..., bytes_read_from_source: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., total_file_count: _Optional[int] = ..., total_changed_file_count: _Optional[int] = ..., file_walk_done: bool = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_MANUALLY_DELETED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    public_status: _enums_pb2.PublicTaskStatus.Type
    start_time_usecs: int
    end_time_usecs: int
    expiry_time_usecs: int
    legal_hold_enabled: bool
    is_manually_deleted: bool
    progress_monitor_task_path: str
    stats: CopyObjectBaseInfo.Stats
    error: _error_pb2_1.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., expiry_time_usecs: _Optional[int] = ..., legal_hold_enabled: bool = ..., is_manually_deleted: bool = ..., progress_monitor_task_path: _Optional[str] = ..., stats: _Optional[_Union[CopyObjectBaseInfo.Stats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ...) -> None: ...

class CopyBackupRunTaskStateProto(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "run_start_time_usecs", "task_uid", "start_time_usecs", "end_time_usecs", "backup_type", "status", "public_status", "error", "cancellation_requested", "snapshot_target", "retention_policy", "expiry_time_usecs", "data_lock_constraints", "legal_hold_enabled", "entity_expiry_time_usecs_map", "entity_legal_hold_map", "granularity_bucket_vec", "archival_info", "replication_info", "local_copy_info", "bridge_constituent_id", "progress_monitor_task_path", "object_level_copy", "copy_partially_successful_run", "disable_rx_megafile", "is_out_of_band_task", "linked_task_info", "active_copy_sub_tasks", "finished_copy_sub_tasks", "metadata_deleted", "should_convert", "cloud_deploy_view_name", "display_sub_tasks_status_based_on_parent", "total_duration_usecs", "view_level_copy", "copy_task_type", "sla_violated", "primary_backup_run_stats", "copy_task_object_info_vec", "task_with_scheduled_state", "fail_progress_monitor_on_already_exists_error", "user_message", "copy_task_timeout_mins", "yoda_max_expiry_time_local_task_enabled")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kScheduled: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kAssigned: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kAccepted: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kFinishing: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kFinished: _ClassVar[CopyBackupRunTaskStateProto.Status]
        kCancelled: _ClassVar[CopyBackupRunTaskStateProto.Status]
    kStarted: CopyBackupRunTaskStateProto.Status
    kScheduled: CopyBackupRunTaskStateProto.Status
    kAssigned: CopyBackupRunTaskStateProto.Status
    kAccepted: CopyBackupRunTaskStateProto.Status
    kFinishing: CopyBackupRunTaskStateProto.Status
    kFinished: CopyBackupRunTaskStateProto.Status
    kCancelled: CopyBackupRunTaskStateProto.Status
    class CopyTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIncoming: _ClassVar[CopyBackupRunTaskStateProto.CopyTaskType]
        kOutgoing: _ClassVar[CopyBackupRunTaskStateProto.CopyTaskType]
    kIncoming: CopyBackupRunTaskStateProto.CopyTaskType
    kOutgoing: CopyBackupRunTaskStateProto.CopyTaskType
    class EntityExpiryTimeUsecsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class EntityLegalHoldMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class LinkedTaskInfo(_message.Message):
        __slots__ = ("task_uid", "snapshot_target")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        snapshot_target: _policy_pb2.SnapshotTarget
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ...) -> None: ...
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_EXPIRY_TIME_USECS_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LEGAL_HOLD_MAP_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCAL_COPY_INFO_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_PARTIALLY_SUCCESSFUL_RUN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RX_MEGAFILE_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_TASK_FIELD_NUMBER: _ClassVar[int]
    LINKED_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_COPY_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_COPY_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_DELETED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CONVERT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SUB_TASKS_STATUS_BASED_ON_PARENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BACKUP_RUN_STATS_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_WITH_SCHEDULED_STATE_FIELD_NUMBER: _ClassVar[int]
    FAIL_PROGRESS_MONITOR_ON_ALREADY_EXISTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_TIMEOUT_MINS_FIELD_NUMBER: _ClassVar[int]
    YODA_MAX_EXPIRY_TIME_LOCAL_TASK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    run_start_time_usecs: int
    task_uid: _universal_id_pb2.UniversalIdProto
    start_time_usecs: int
    end_time_usecs: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    status: CopyBackupRunTaskStateProto.Status
    public_status: _enums_pb2.PublicTaskStatus.Type
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    snapshot_target: _policy_pb2.SnapshotTarget
    retention_policy: _policy_pb2.RetentionPolicyProto
    expiry_time_usecs: int
    data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    legal_hold_enabled: bool
    entity_expiry_time_usecs_map: _containers.ScalarMap[int, int]
    entity_legal_hold_map: _containers.ScalarMap[int, bool]
    granularity_bucket_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.GranularityBucket]
    archival_info: ArchivalInfoBase
    replication_info: ReplicationInfoBase
    local_copy_info: LocalCopyInfoBase
    bridge_constituent_id: int
    progress_monitor_task_path: str
    object_level_copy: bool
    copy_partially_successful_run: bool
    disable_rx_megafile: bool
    is_out_of_band_task: bool
    linked_task_info: CopyBackupRunTaskStateProto.LinkedTaskInfo
    active_copy_sub_tasks: _containers.RepeatedCompositeFieldContainer[CopyBackupSubTaskStateProto]
    finished_copy_sub_tasks: _containers.RepeatedCompositeFieldContainer[CopyBackupSubTaskStateProto]
    metadata_deleted: bool
    should_convert: bool
    cloud_deploy_view_name: str
    display_sub_tasks_status_based_on_parent: bool
    total_duration_usecs: int
    view_level_copy: bool
    copy_task_type: CopyBackupRunTaskStateProto.CopyTaskType
    sla_violated: bool
    primary_backup_run_stats: PrimaryBackupRunStats
    copy_task_object_info_vec: _containers.RepeatedCompositeFieldContainer[CopyObjectBaseInfo]
    task_with_scheduled_state: bool
    fail_progress_monitor_on_already_exists_error: bool
    user_message: str
    copy_task_timeout_mins: int
    yoda_max_expiry_time_local_task_enabled: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., status: _Optional[_Union[CopyBackupRunTaskStateProto.Status, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ..., data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., legal_hold_enabled: bool = ..., entity_expiry_time_usecs_map: _Optional[_Mapping[int, int]] = ..., entity_legal_hold_map: _Optional[_Mapping[int, bool]] = ..., granularity_bucket_vec: _Optional[_Iterable[_Union[_policy_pb2.GranularityBucket, _Mapping]]] = ..., archival_info: _Optional[_Union[ArchivalInfoBase, _Mapping]] = ..., replication_info: _Optional[_Union[ReplicationInfoBase, _Mapping]] = ..., local_copy_info: _Optional[_Union[LocalCopyInfoBase, _Mapping]] = ..., bridge_constituent_id: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., object_level_copy: bool = ..., copy_partially_successful_run: bool = ..., disable_rx_megafile: bool = ..., is_out_of_band_task: bool = ..., linked_task_info: _Optional[_Union[CopyBackupRunTaskStateProto.LinkedTaskInfo, _Mapping]] = ..., active_copy_sub_tasks: _Optional[_Iterable[_Union[CopyBackupSubTaskStateProto, _Mapping]]] = ..., finished_copy_sub_tasks: _Optional[_Iterable[_Union[CopyBackupSubTaskStateProto, _Mapping]]] = ..., metadata_deleted: bool = ..., should_convert: bool = ..., cloud_deploy_view_name: _Optional[str] = ..., display_sub_tasks_status_based_on_parent: bool = ..., total_duration_usecs: _Optional[int] = ..., view_level_copy: bool = ..., copy_task_type: _Optional[_Union[CopyBackupRunTaskStateProto.CopyTaskType, str]] = ..., sla_violated: bool = ..., primary_backup_run_stats: _Optional[_Union[PrimaryBackupRunStats, _Mapping]] = ..., copy_task_object_info_vec: _Optional[_Iterable[_Union[CopyObjectBaseInfo, _Mapping]]] = ..., task_with_scheduled_state: bool = ..., fail_progress_monitor_on_already_exists_error: bool = ..., user_message: _Optional[str] = ..., copy_task_timeout_mins: _Optional[int] = ..., yoda_max_expiry_time_local_task_enabled: bool = ...) -> None: ...

class CopyBackupRunStateProto(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "run_start_time_usecs", "start_time_usecs", "end_time_usecs", "status", "error", "active_tasks", "finished_tasks", "is_out_of_band_run", "copy_snapshot_params_vec", "total_duration_usecs", "locking_required", "is_cascaded_copy", "is_gc_initiated", "initiated_by_dso_role")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CopyBackupRunStateProto.Status]
        kCopyTasksCreated: _ClassVar[CopyBackupRunStateProto.Status]
        kFinished: _ClassVar[CopyBackupRunStateProto.Status]
        kCancelled: _ClassVar[CopyBackupRunStateProto.Status]
    kStarted: CopyBackupRunStateProto.Status
    kCopyTasksCreated: CopyBackupRunStateProto.Status
    kFinished: CopyBackupRunStateProto.Status
    kCancelled: CopyBackupRunStateProto.Status
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TASKS_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_RUN_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    LOCKING_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    IS_CASCADED_COPY_FIELD_NUMBER: _ClassVar[int]
    IS_GC_INITIATED_FIELD_NUMBER: _ClassVar[int]
    INITIATED_BY_DSO_ROLE_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    run_start_time_usecs: int
    start_time_usecs: int
    end_time_usecs: int
    status: CopyBackupRunStateProto.Status
    error: _error_pb2_1.ErrorProto
    active_tasks: _containers.RepeatedCompositeFieldContainer[CopyBackupRunTaskStateProto]
    finished_tasks: _containers.RepeatedCompositeFieldContainer[CopyBackupRunTaskStateProto]
    is_out_of_band_run: bool
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[CopySnapshotParams]
    total_duration_usecs: int
    locking_required: bool
    is_cascaded_copy: bool
    is_gc_initiated: bool
    initiated_by_dso_role: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status: _Optional[_Union[CopyBackupRunStateProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., active_tasks: _Optional[_Iterable[_Union[CopyBackupRunTaskStateProto, _Mapping]]] = ..., finished_tasks: _Optional[_Iterable[_Union[CopyBackupRunTaskStateProto, _Mapping]]] = ..., is_out_of_band_run: bool = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[CopySnapshotParams, _Mapping]]] = ..., total_duration_usecs: _Optional[int] = ..., locking_required: bool = ..., is_cascaded_copy: bool = ..., is_gc_initiated: bool = ..., initiated_by_dso_role: bool = ...) -> None: ...

class ProtectionRunStateProto(_message.Message):
    __slots__ = ("backup_run", "copy_run", "protection_run_shell", "originator_type")
    BACKUP_RUN_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_RUN_SHELL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    backup_run: BackupJobRunStateProto
    copy_run: CopyBackupRunStateProto
    protection_run_shell: ProtectionRunShellInfoProto
    originator_type: _policy_pb2.SnapshotTarget.Type
    def __init__(self, backup_run: _Optional[_Union[BackupJobRunStateProto, _Mapping]] = ..., copy_run: _Optional[_Union[CopyBackupRunStateProto, _Mapping]] = ..., protection_run_shell: _Optional[_Union[ProtectionRunShellInfoProto, _Mapping]] = ..., originator_type: _Optional[_Union[_policy_pb2.SnapshotTarget.Type, str]] = ...) -> None: ...

class ProtectionRunShellInfoProto(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "job_instance_id", "public_status", "backup_type", "error")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    job_instance_id: int
    public_status: _enums_pb2.PublicTaskStatus.Type
    backup_type: _enums_pb2.ScheduledBackupType.Type
    error: _error_pb2_1.ErrorProto
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class BackupJobRunsProto(_message.Message):
    __slots__ = ("job_description", "protection_runs")
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_RUNS_FIELD_NUMBER: _ClassVar[int]
    job_description: _magneto_pb2.BackupJobProto
    protection_runs: _containers.RepeatedCompositeFieldContainer[ProtectionRunStateProto]
    def __init__(self, job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., protection_runs: _Optional[_Iterable[_Union[ProtectionRunStateProto, _Mapping]]] = ...) -> None: ...

class LookupMasterArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ...) -> None: ...

class LookupMasterResult(_message.Message):
    __slots__ = ("error", "ip", "port", "read_replica_ip", "read_replica_port")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICA_IP_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICA_PORT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    ip: str
    port: int
    read_replica_ip: str
    read_replica_port: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., read_replica_ip: _Optional[str] = ..., read_replica_port: _Optional[int] = ...) -> None: ...

class CreateOrUpdateProtectionPolicyArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "protection_policy", "delete_policy", "dso_role", "request_source_ip", "request_source_type", "expected_policy_mtime_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DELETE_POLICY_FIELD_NUMBER: _ClassVar[int]
    DSO_ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_POLICY_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    protection_policy: _policy_pb2.ProtectionPolicyProto
    delete_policy: bool
    dso_role: bool
    request_source_ip: str
    request_source_type: str
    expected_policy_mtime_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., delete_policy: bool = ..., dso_role: bool = ..., request_source_ip: _Optional[str] = ..., request_source_type: _Optional[str] = ..., expected_policy_mtime_usecs: _Optional[int] = ...) -> None: ...

class CreateOrUpdateProtectionPolicyResult(_message.Message):
    __slots__ = ("error", "policy_id", "protection_policy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    policy_id: str
    protection_policy: _policy_pb2.ProtectionPolicyProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., policy_id: _Optional[str] = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ...) -> None: ...

class GetProtectionPoliciesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "policy_id_vec", "user_info", "policy_type_vec", "origin", "fetch_replicated_policies", "include_deleted_policies")
    class PolicyOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[GetProtectionPoliciesArg.PolicyOrigin]
        kLocal: _ClassVar[GetProtectionPoliciesArg.PolicyOrigin]
        kHelios: _ClassVar[GetProtectionPoliciesArg.PolicyOrigin]
        kAll: _ClassVar[GetProtectionPoliciesArg.PolicyOrigin]
    kUnknown: GetProtectionPoliciesArg.PolicyOrigin
    kLocal: GetProtectionPoliciesArg.PolicyOrigin
    kHelios: GetProtectionPoliciesArg.PolicyOrigin
    kAll: GetProtectionPoliciesArg.PolicyOrigin
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    FETCH_REPLICATED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    policy_id_vec: _containers.RepeatedScalarFieldContainer[str]
    user_info: _permissions_pb2.UserInformation
    policy_type_vec: _containers.RepeatedScalarFieldContainer[_policy_pb2.ProtectionPolicyProto.PolicyType]
    origin: GetProtectionPoliciesArg.PolicyOrigin
    fetch_replicated_policies: bool
    include_deleted_policies: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., policy_id_vec: _Optional[_Iterable[str]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., policy_type_vec: _Optional[_Iterable[_Union[_policy_pb2.ProtectionPolicyProto.PolicyType, str]]] = ..., origin: _Optional[_Union[GetProtectionPoliciesArg.PolicyOrigin, str]] = ..., fetch_replicated_policies: bool = ..., include_deleted_policies: bool = ...) -> None: ...

class GetProtectionPoliciesResult(_message.Message):
    __slots__ = ("error", "result_vec")
    class ProtectionPolicyResult(_message.Message):
        __slots__ = ("error", "protection_policy")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2_1.ErrorProto
        protection_policy: _policy_pb2.ProtectionPolicyProto
        def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    result_vec: _containers.RepeatedCompositeFieldContainer[GetProtectionPoliciesResult.ProtectionPolicyResult]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[GetProtectionPoliciesResult.ProtectionPolicyResult, _Mapping]]] = ...) -> None: ...

class ProtectionPolicySummaryProto(_message.Message):
    __slots__ = ("protection_policy", "last_backup_run_summary", "backup_runs_summary", "entity_summary_vec", "backup_job_summary_vec")
    class LastBackupRunSummary(_message.Message):
        __slots__ = ("num_protected_objects", "num_running_backups", "num_successful_backups", "num_failed_backups", "num_cancelled_backups", "num_sla_violations", "total_logical_backup_size_bytes")
        NUM_PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        NUM_RUNNING_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        NUM_SUCCESSFUL_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        NUM_FAILED_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        NUM_CANCELLED_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        NUM_SLA_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        num_protected_objects: int
        num_running_backups: int
        num_successful_backups: int
        num_failed_backups: int
        num_cancelled_backups: int
        num_sla_violations: int
        total_logical_backup_size_bytes: int
        def __init__(self, num_protected_objects: _Optional[int] = ..., num_running_backups: _Optional[int] = ..., num_successful_backups: _Optional[int] = ..., num_failed_backups: _Optional[int] = ..., num_cancelled_backups: _Optional[int] = ..., num_sla_violations: _Optional[int] = ..., total_logical_backup_size_bytes: _Optional[int] = ...) -> None: ...
    class BackupRunsSummary(_message.Message):
        __slots__ = ("num_successful_backup_runs", "num_total_backup_runs", "num_successful_replication_runs", "num_total_replication_runs", "num_successful_archive_runs", "num_total_archive_runs")
        NUM_SUCCESSFUL_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_TOTAL_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_SUCCESSFUL_REPLICATION_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_TOTAL_REPLICATION_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_SUCCESSFUL_ARCHIVE_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_TOTAL_ARCHIVE_RUNS_FIELD_NUMBER: _ClassVar[int]
        num_successful_backup_runs: int
        num_total_backup_runs: int
        num_successful_replication_runs: int
        num_total_replication_runs: int
        num_successful_archive_runs: int
        num_total_archive_runs: int
        def __init__(self, num_successful_backup_runs: _Optional[int] = ..., num_total_backup_runs: _Optional[int] = ..., num_successful_replication_runs: _Optional[int] = ..., num_total_replication_runs: _Optional[int] = ..., num_successful_archive_runs: _Optional[int] = ..., num_total_archive_runs: _Optional[int] = ...) -> None: ...
    class ProtectedEntitySummary(_message.Message):
        __slots__ = ("entity", "rpo_job_description", "last_protection_run", "next_backup_time_usecs")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        RPO_JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LAST_PROTECTION_RUN_FIELD_NUMBER: _ClassVar[int]
        NEXT_BACKUP_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        rpo_job_description: _magneto_pb2.BackupJobProto
        last_protection_run: ProtectionRunStateProto
        next_backup_time_usecs: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., rpo_job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., last_protection_run: _Optional[_Union[ProtectionRunStateProto, _Mapping]] = ..., next_backup_time_usecs: _Optional[int] = ...) -> None: ...
    class BackupJobSummary(_message.Message):
        __slots__ = ("job_description", "last_protection_run")
        JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LAST_PROTECTION_RUN_FIELD_NUMBER: _ClassVar[int]
        job_description: _magneto_pb2.BackupJobProto
        last_protection_run: ProtectionRunStateProto
        def __init__(self, job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., last_protection_run: _Optional[_Union[ProtectionRunStateProto, _Mapping]] = ...) -> None: ...
    PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LAST_BACKUP_RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUNS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    protection_policy: _policy_pb2.ProtectionPolicyProto
    last_backup_run_summary: ProtectionPolicySummaryProto.LastBackupRunSummary
    backup_runs_summary: ProtectionPolicySummaryProto.BackupRunsSummary
    entity_summary_vec: _containers.RepeatedCompositeFieldContainer[ProtectionPolicySummaryProto.ProtectedEntitySummary]
    backup_job_summary_vec: _containers.RepeatedCompositeFieldContainer[ProtectionPolicySummaryProto.BackupJobSummary]
    def __init__(self, protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., last_backup_run_summary: _Optional[_Union[ProtectionPolicySummaryProto.LastBackupRunSummary, _Mapping]] = ..., backup_runs_summary: _Optional[_Union[ProtectionPolicySummaryProto.BackupRunsSummary, _Mapping]] = ..., entity_summary_vec: _Optional[_Iterable[_Union[ProtectionPolicySummaryProto.ProtectedEntitySummary, _Mapping]]] = ..., backup_job_summary_vec: _Optional[_Iterable[_Union[ProtectionPolicySummaryProto.BackupJobSummary, _Mapping]]] = ...) -> None: ...

class GetProtectionPolicySummaryArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "policy_id", "include_last_backup_run_summary", "include_all_backup_runs_summary", "time_range", "limit_num_objects", "pagination_cookie", "user_info")
    class PaginationCookie(_message.Message):
        __slots__ = ("last_job_uid", "last_backup_run_summary", "backup_runs_summary")
        LAST_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        LAST_BACKUP_RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_RUNS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        last_job_uid: _universal_id_pb2.UniversalIdProto
        last_backup_run_summary: ProtectionPolicySummaryProto.LastBackupRunSummary
        backup_runs_summary: ProtectionPolicySummaryProto.BackupRunsSummary
        def __init__(self, last_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_backup_run_summary: _Optional[_Union[ProtectionPolicySummaryProto.LastBackupRunSummary, _Mapping]] = ..., backup_runs_summary: _Optional[_Union[ProtectionPolicySummaryProto.BackupRunsSummary, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LAST_BACKUP_RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_BACKUP_RUNS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    policy_id: str
    include_last_backup_run_summary: bool
    include_all_backup_runs_summary: bool
    time_range: TimeRange
    limit_num_objects: int
    pagination_cookie: GetProtectionPolicySummaryArg.PaginationCookie
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., policy_id: _Optional[str] = ..., include_last_backup_run_summary: bool = ..., include_all_backup_runs_summary: bool = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., limit_num_objects: _Optional[int] = ..., pagination_cookie: _Optional[_Union[GetProtectionPolicySummaryArg.PaginationCookie, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class GetProtectionPolicySummaryResult(_message.Message):
    __slots__ = ("error", "policy_summary", "pagination_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    policy_summary: ProtectionPolicySummaryProto
    pagination_cookie: GetProtectionPolicySummaryArg.PaginationCookie
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., policy_summary: _Optional[_Union[ProtectionPolicySummaryProto, _Mapping]] = ..., pagination_cookie: _Optional[_Union[GetProtectionPolicySummaryArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class CreateBackupJobArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_description", "run_once_immediately", "entities_to_protect")
    class EntitiesToProtect(_message.Message):
        __slots__ = ("rpo_policy_id", "protection_env", "entity_id_vec")
        RPO_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_ENV_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        rpo_policy_id: str
        protection_env: _enums_pb2.Environment.Type
        entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, rpo_policy_id: _Optional[str] = ..., protection_env: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RUN_ONCE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TO_PROTECT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_description: _magneto_pb2.BackupJobProto
    run_once_immediately: bool
    entities_to_protect: CreateBackupJobArg.EntitiesToProtect
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., run_once_immediately: bool = ..., entities_to_protect: _Optional[_Union[CreateBackupJobArg.EntitiesToProtect, _Mapping]] = ...) -> None: ...

class CreateBackupJobResult(_message.Message):
    __slots__ = ("error", "job_id", "job_uid", "protected_entities", "job_description")
    class ProtectedEntity(_message.Message):
        __slots__ = ("error", "entity_id", "job_uid")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2_1.ErrorProto
        entity_id: int
        job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    protected_entities: _containers.RepeatedCompositeFieldContainer[CreateBackupJobResult.ProtectedEntity]
    job_description: _magneto_pb2.BackupJobProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., protected_entities: _Optional[_Iterable[_Union[CreateBackupJobResult.ProtectedEntity, _Mapping]]] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ...) -> None: ...

class UpdateBackupJobArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_description", "deactivate_entities", "request_source_ip", "request_source_type", "expected_job_mtime_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_JOB_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_description: _magneto_pb2.BackupJobProto
    deactivate_entities: bool
    request_source_ip: str
    request_source_type: str
    expected_job_mtime_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., deactivate_entities: bool = ..., request_source_ip: _Optional[str] = ..., request_source_type: _Optional[str] = ..., expected_job_mtime_usecs: _Optional[int] = ...) -> None: ...

class UpdateBackupJobResult(_message.Message):
    __slots__ = ("error", "job_description")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_description: _magneto_pb2.BackupJobProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ...) -> None: ...

class CancelProtectionJobRunArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_instance_id", "run_start_time_usecs", "entity_id_vec", "copy_task_uid", "rx_task_uid")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    RX_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_instance_id: int
    run_start_time_usecs: int
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    copy_task_uid: _universal_id_pb2.UniversalIdProto
    rx_task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., copy_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelProtectionJobRunResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class CopySnapshotParams(_message.Message):
    __slots__ = ("snapshot_target", "retention_policy", "enable_legal_hold", "release_legal_hold", "copy_only_fully_successful_runs")
    SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    RELEASE_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    COPY_ONLY_FULLY_SUCCESSFUL_RUNS_FIELD_NUMBER: _ClassVar[int]
    snapshot_target: _policy_pb2.SnapshotTarget
    retention_policy: _policy_pb2.RetentionPolicyProto
    enable_legal_hold: bool
    release_legal_hold: bool
    copy_only_fully_successful_runs: bool
    def __init__(self, snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ..., enable_legal_hold: bool = ..., release_legal_hold: bool = ..., copy_only_fully_successful_runs: bool = ...) -> None: ...

class RunBackupJobOnceArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "backup_type", "additional_param_vec", "copy_snapshot_params_vec", "user_info", "run_label", "is_full_backup_DEPRECATED")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    additional_param_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupTaskAdditionalParams]
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[CopySnapshotParams]
    user_info: _permissions_pb2.UserInformation
    run_label: str
    is_full_backup_DEPRECATED: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., additional_param_vec: _Optional[_Iterable[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]]] = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[CopySnapshotParams, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., run_label: _Optional[str] = ..., is_full_backup_DEPRECATED: bool = ...) -> None: ...

class RunBackupJobOnceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "attributes")
    class Attributes(_message.Message):
        __slots__ = ("job_uid",)
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    attributes: TimeRange.Attributes
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., attributes: _Optional[_Union[TimeRange.Attributes, _Mapping]] = ...) -> None: ...

class EntityPaginationParams(_message.Message):
    __slots__ = ("parent_entity_id", "max_num_entities", "pagination_cursor")
    class PaginationCursor(_message.Message):
        __slots__ = ("after_cursor_entity_id", "before_cursor_entity_id")
        AFTER_CURSOR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        BEFORE_CURSOR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        after_cursor_entity_id: int
        before_cursor_entity_id: int
        def __init__(self, after_cursor_entity_id: _Optional[int] = ..., before_cursor_entity_id: _Optional[int] = ...) -> None: ...
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_CURSOR_FIELD_NUMBER: _ClassVar[int]
    parent_entity_id: int
    max_num_entities: int
    pagination_cursor: EntityPaginationParams.PaginationCursor
    def __init__(self, parent_entity_id: _Optional[int] = ..., max_num_entities: _Optional[int] = ..., pagination_cursor: _Optional[_Union[EntityPaginationParams.PaginationCursor, _Mapping]] = ...) -> None: ...

class BackupJobSummaryProto(_message.Message):
    __slots__ = ("job_description", "num_successful_job_runs", "num_failed_job_runs", "num_cancelled_job_runs", "num_sla_violations", "avg_run_time_usecs", "min_run_time_usecs", "max_run_time_usecs", "num_objects_backed_up", "total_bytes_read_from_source", "total_logical_backup_size_bytes", "total_physical_backup_size_bytes", "last_protection_run", "active_change_mode_state", "finished_change_mode_state", "authorized_tenant_id_vec", "is_cloud_archive_direct", "is_protect_once", "missing_entity_info_vec", "invalid_entity_info_vec", "missing_entity_id_vec")
    class MissingEntityInfo(_message.Message):
        __slots__ = ("entity_id", "entity_name", "parent_source")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        entity_name: str
        parent_source: _entity_pb2.EntityProto
        def __init__(self, entity_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    NUM_CANCELLED_JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    NUM_SLA_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    AVG_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MIN_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MAX_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECTS_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_PROTECTION_RUN_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CHANGE_MODE_STATE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_CHANGE_MODE_STATE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
    IS_PROTECT_ONCE_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    INVALID_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    job_description: _magneto_pb2.BackupJobProto
    num_successful_job_runs: int
    num_failed_job_runs: int
    num_cancelled_job_runs: int
    num_sla_violations: int
    avg_run_time_usecs: int
    min_run_time_usecs: int
    max_run_time_usecs: int
    num_objects_backed_up: int
    total_bytes_read_from_source: int
    total_logical_backup_size_bytes: int
    total_physical_backup_size_bytes: int
    last_protection_run: ProtectionRunStateProto
    active_change_mode_state: ChangeBackupJobModeProto
    finished_change_mode_state: ChangeBackupJobModeProto
    authorized_tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    is_cloud_archive_direct: bool
    is_protect_once: bool
    missing_entity_info_vec: _containers.RepeatedCompositeFieldContainer[BackupJobSummaryProto.MissingEntityInfo]
    invalid_entity_info_vec: _containers.RepeatedCompositeFieldContainer[BackupJobSummaryProto.MissingEntityInfo]
    missing_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., num_successful_job_runs: _Optional[int] = ..., num_failed_job_runs: _Optional[int] = ..., num_cancelled_job_runs: _Optional[int] = ..., num_sla_violations: _Optional[int] = ..., avg_run_time_usecs: _Optional[int] = ..., min_run_time_usecs: _Optional[int] = ..., max_run_time_usecs: _Optional[int] = ..., num_objects_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., total_logical_backup_size_bytes: _Optional[int] = ..., total_physical_backup_size_bytes: _Optional[int] = ..., last_protection_run: _Optional[_Union[ProtectionRunStateProto, _Mapping]] = ..., active_change_mode_state: _Optional[_Union[ChangeBackupJobModeProto, _Mapping]] = ..., finished_change_mode_state: _Optional[_Union[ChangeBackupJobModeProto, _Mapping]] = ..., authorized_tenant_id_vec: _Optional[_Iterable[str]] = ..., is_cloud_archive_direct: bool = ..., is_protect_once: bool = ..., missing_entity_info_vec: _Optional[_Iterable[_Union[BackupJobSummaryProto.MissingEntityInfo, _Mapping]]] = ..., invalid_entity_info_vec: _Optional[_Iterable[_Union[BackupJobSummaryProto.MissingEntityInfo, _Mapping]]] = ..., missing_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetBackupJobSummaryArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "protection_type_mask", "job_uid_vec", "job_id_vec", "only_return_basic_summary", "time_range", "source", "type_vec", "sid_vec", "user_info", "process_deleted_jobs", "process_inactive_jobs", "process_active_jobs", "process_deleted_jobs_and_backups", "return_stubbing_jobs", "only_return_job_description", "prune_exclusion_sources", "return_internal_jobs", "storage_domain_id", "return_only_worm_protected_jobs", "return_missing_entities", "include_gc_runs_in_basic_summary", "prune_sources", "return_only_entity_ids")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_TYPE_MASK_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_BASIC_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESS_DELETED_JOBS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INACTIVE_JOBS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ACTIVE_JOBS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_DELETED_JOBS_AND_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    RETURN_STUBBING_JOBS_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRUNE_EXCLUSION_SOURCES_FIELD_NUMBER: _ClassVar[int]
    RETURN_INTERNAL_JOBS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_WORM_PROTECTED_JOBS_FIELD_NUMBER: _ClassVar[int]
    RETURN_MISSING_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_GC_RUNS_IN_BASIC_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PRUNE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    protection_type_mask: int
    job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    job_id_vec: _containers.RepeatedScalarFieldContainer[int]
    only_return_basic_summary: bool
    time_range: TimeRange
    source: _entity_pb2.EntityProto
    type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    process_deleted_jobs: bool
    process_inactive_jobs: bool
    process_active_jobs: bool
    process_deleted_jobs_and_backups: bool
    return_stubbing_jobs: bool
    only_return_job_description: bool
    prune_exclusion_sources: bool
    return_internal_jobs: bool
    storage_domain_id: int
    return_only_worm_protected_jobs: bool
    return_missing_entities: bool
    include_gc_runs_in_basic_summary: bool
    prune_sources: bool
    return_only_entity_ids: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., protection_type_mask: _Optional[int] = ..., job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., job_id_vec: _Optional[_Iterable[int]] = ..., only_return_basic_summary: bool = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., process_deleted_jobs: bool = ..., process_inactive_jobs: bool = ..., process_active_jobs: bool = ..., process_deleted_jobs_and_backups: bool = ..., return_stubbing_jobs: bool = ..., only_return_job_description: bool = ..., prune_exclusion_sources: bool = ..., return_internal_jobs: bool = ..., storage_domain_id: _Optional[int] = ..., return_only_worm_protected_jobs: bool = ..., return_missing_entities: bool = ..., include_gc_runs_in_basic_summary: bool = ..., prune_sources: bool = ..., return_only_entity_ids: bool = ...) -> None: ...

class GetBackupJobSummaryResult(_message.Message):
    __slots__ = ("error", "jobs", "num_jobs_without_valid_run")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_JOBS_WITHOUT_VALID_RUN_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    jobs: _containers.RepeatedCompositeFieldContainer[BackupJobSummaryProto]
    num_jobs_without_valid_run: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., jobs: _Optional[_Iterable[_Union[BackupJobSummaryProto, _Mapping]]] = ..., num_jobs_without_valid_run: _Optional[int] = ...) -> None: ...

class GetBackupJobRunsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_uid", "protection_type_mask", "job_run_start_time_usecs", "time_range", "filter_by_copy_task_end_time", "filter_by_end_time", "limit_num_runs", "only_return_basic_run_info", "only_return_shell_info", "source", "sid_vec", "user_info", "include_extension_info", "only_return_backup_run_info", "only_return_copy_run_info", "return_stubbing_jobs", "use_cases", "run_types", "tags", "truncate_response", "copy_run_filter")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_TYPE_MASK_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_BY_COPY_TASK_END_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_BY_END_TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_RUNS_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_BASIC_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_SHELL_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXTENSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_BACKUP_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_COPY_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    RETURN_STUBBING_JOBS_FIELD_NUMBER: _ClassVar[int]
    USE_CASES_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_FILTER_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    protection_type_mask: int
    job_run_start_time_usecs: int
    time_range: TimeRange
    filter_by_copy_task_end_time: bool
    filter_by_end_time: bool
    limit_num_runs: int
    only_return_basic_run_info: bool
    only_return_shell_info: bool
    source: _entity_pb2.EntityProto
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    include_extension_info: bool
    only_return_backup_run_info: bool
    only_return_copy_run_info: bool
    return_stubbing_jobs: bool
    use_cases: BackupJobRunsUseCases
    run_types: _containers.RepeatedScalarFieldContainer[_enums_pb2.ScheduledBackupType.Type]
    tags: _containers.RepeatedScalarFieldContainer[str]
    truncate_response: bool
    copy_run_filter: CopyRunFilter
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., protection_type_mask: _Optional[int] = ..., job_run_start_time_usecs: _Optional[int] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., filter_by_copy_task_end_time: bool = ..., filter_by_end_time: bool = ..., limit_num_runs: _Optional[int] = ..., only_return_basic_run_info: bool = ..., only_return_shell_info: bool = ..., source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., include_extension_info: bool = ..., only_return_backup_run_info: bool = ..., only_return_copy_run_info: bool = ..., return_stubbing_jobs: bool = ..., use_cases: _Optional[_Union[BackupJobRunsUseCases, _Mapping]] = ..., run_types: _Optional[_Iterable[_Union[_enums_pb2.ScheduledBackupType.Type, str]]] = ..., tags: _Optional[_Iterable[str]] = ..., truncate_response: bool = ..., copy_run_filter: _Optional[_Union[CopyRunFilter, _Mapping]] = ...) -> None: ...

class GetBackupJobRunsResult(_message.Message):
    __slots__ = ("error", "job_runs", "backup_job_run_summary", "is_response_truncated")
    class BackupJobRunSummaryProto(_message.Message):
        __slots__ = ("num_total_backup_runs",)
        NUM_TOTAL_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        num_total_backup_runs: int
        def __init__(self, num_total_backup_runs: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    IS_RESPONSE_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_runs: _containers.RepeatedCompositeFieldContainer[BackupJobRunsProto]
    backup_job_run_summary: GetBackupJobRunsResult.BackupJobRunSummaryProto
    is_response_truncated: bool
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_runs: _Optional[_Iterable[_Union[BackupJobRunsProto, _Mapping]]] = ..., backup_job_run_summary: _Optional[_Union[GetBackupJobRunsResult.BackupJobRunSummaryProto, _Mapping]] = ..., is_response_truncated: bool = ...) -> None: ...

class CopyRunFilter(_message.Message):
    __slots__ = ("snapshot_target_type_vec", "public_task_status")
    SNAPSHOT_TARGET_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    snapshot_target_type_vec: _containers.RepeatedScalarFieldContainer[_policy_pb2.SnapshotTarget.Type]
    public_task_status: _enums_pb2.PublicTaskStatus.Type
    def __init__(self, snapshot_target_type_vec: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTarget.Type, str]]] = ..., public_task_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ...) -> None: ...

class BackupJobRunsUseCases(_message.Message):
    __slots__ = ("is_object_runs_page",)
    IS_OBJECT_RUNS_PAGE_FIELD_NUMBER: _ClassVar[int]
    is_object_runs_page: bool
    def __init__(self, is_object_runs_page: bool = ...) -> None: ...

class BackupJobLeafSources(_message.Message):
    __slots__ = ("error", "job_id", "leaf_sources")
    class LeafSourceInfo(_message.Message):
        __slots__ = ("source", "next_start_time_usecs", "next_backup_type", "aggregated_protected_info_vec", "aggregated_unprotected_info_vec", "is_next_backup_full")
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        NEXT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        NEXT_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        AGGREGATED_PROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        AGGREGATED_UNPROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_NEXT_BACKUP_FULL_FIELD_NUMBER: _ClassVar[int]
        source: _entity_pb2.EntityProto
        next_start_time_usecs: int
        next_backup_type: _enums_pb2.ScheduledBackupType.Type
        aggregated_protected_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo]
        aggregated_unprotected_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo]
        is_next_backup_full: bool
        def __init__(self, source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., next_start_time_usecs: _Optional[int] = ..., next_backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., aggregated_protected_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ..., aggregated_unprotected_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ..., is_next_backup_full: bool = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_SOURCES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_id: int
    leaf_sources: _containers.RepeatedCompositeFieldContainer[BackupJobLeafSources.LeafSourceInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_id: _Optional[int] = ..., leaf_sources: _Optional[_Iterable[_Union[BackupJobLeafSources.LeafSourceInfo, _Mapping]]] = ...) -> None: ...

class GetBackupJobLeafSourcesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "protection_type_mask", "sid_vec", "user_info", "parent_source", "source", "type")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_TYPE_MASK_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    protection_type_mask: int
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    parent_source: _entity_pb2.EntityProto
    source: _entity_pb2.EntityProto
    type: _enums_pb2.Environment.Type
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., protection_type_mask: _Optional[int] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class GetBackupJobLeafSourcesResult(_message.Message):
    __slots__ = ("error", "job_sources")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_SOURCES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_sources: _containers.RepeatedCompositeFieldContainer[BackupJobLeafSources]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_sources: _Optional[_Iterable[_Union[BackupJobLeafSources, _Mapping]]] = ...) -> None: ...

class GetSqlAAGHostClusterArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "seed_entity_id_vec", "require_entire_hosts", "seed_host_entity_id_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SEED_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ENTIRE_HOSTS_FIELD_NUMBER: _ClassVar[int]
    SEED_HOST_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    seed_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    require_entire_hosts: bool
    seed_host_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., seed_entity_id_vec: _Optional[_Iterable[int]] = ..., require_entire_hosts: bool = ..., seed_host_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetSqlAAGHostClusterResult(_message.Message):
    __slots__ = ("error", "aag_host_info_vec", "meets_aag_constraints")
    class AAGHostInfo(_message.Message):
        __slots__ = ("host_entity_hierarchy", "db_entity_vec", "aag_info_vec", "error", "unknown_host_name")
        class AAGInfo(_message.Message):
            __slots__ = ("aag_entity", "db_entity_vec")
            AAG_ENTITY_FIELD_NUMBER: _ClassVar[int]
            DB_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
            aag_entity: _entity_pb2.EntityProto
            db_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
            def __init__(self, aag_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., db_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
        HOST_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
        DB_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
        AAG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        host_entity_hierarchy: _magneto_pb2.EntityHierarchyProto
        db_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        aag_info_vec: _containers.RepeatedCompositeFieldContainer[GetSqlAAGHostClusterResult.AAGHostInfo.AAGInfo]
        error: _error_pb2_1.ErrorProto
        unknown_host_name: str
        def __init__(self, host_entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., db_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., aag_info_vec: _Optional[_Iterable[_Union[GetSqlAAGHostClusterResult.AAGHostInfo.AAGInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., unknown_host_name: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AAG_HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MEETS_AAG_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    aag_host_info_vec: _containers.RepeatedCompositeFieldContainer[GetSqlAAGHostClusterResult.AAGHostInfo]
    meets_aag_constraints: bool
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., aag_host_info_vec: _Optional[_Iterable[_Union[GetSqlAAGHostClusterResult.AAGHostInfo, _Mapping]]] = ..., meets_aag_constraints: bool = ...) -> None: ...

class EntityAccessInfo(_message.Message):
    __slots__ = ("endpoint", "type", "host_type", "credentials", "use_outlook_ews_oauth", "office365_region", "proxy_entity_id_vec", "agent_endpoint", "agent_port")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    USE_OUTLOOK_EWS_OAUTH_FIELD_NUMBER: _ClassVar[int]
    OFFICE365_REGION_FIELD_NUMBER: _ClassVar[int]
    PROXY_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    type: _enums_pb2.Environment.Type
    host_type: _enums_pb2.HostEnv.Type
    credentials: _credentials_pb2.Credentials
    use_outlook_ews_oauth: bool
    office365_region: str
    proxy_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    agent_endpoint: str
    agent_port: int
    def __init__(self, endpoint: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., use_outlook_ews_oauth: bool = ..., office365_region: _Optional[str] = ..., proxy_entity_id_vec: _Optional[_Iterable[int]] = ..., agent_endpoint: _Optional[str] = ..., agent_port: _Optional[int] = ...) -> None: ...

class RegisterEntityArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity", "entity_access_info", "source_side_dedup_enabled", "force_register", "discard_persistent_uid", "registered_entity_params", "user_info", "is_internal_encrypted", "user_encryption_key", "re_register", "restore_config", "throttling_policy")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_REGISTER_FIELD_NUMBER: _ClassVar[int]
    DISCARD_PERSISTENT_UID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    USER_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    RE_REGISTER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_POLICY_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity: _entity_pb2.EntityProto
    entity_access_info: EntityAccessInfo
    source_side_dedup_enabled: bool
    force_register: bool
    discard_persistent_uid: bool
    registered_entity_params: _magneto_pb2.RegisteredEntityParams
    user_info: _permissions_pb2.UserInformation
    is_internal_encrypted: bool
    user_encryption_key: str
    re_register: bool
    restore_config: bool
    throttling_policy: _magneto_pb2.ThrottlingPolicy
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_access_info: _Optional[_Union[EntityAccessInfo, _Mapping]] = ..., source_side_dedup_enabled: bool = ..., force_register: bool = ..., discard_persistent_uid: bool = ..., registered_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., is_internal_encrypted: bool = ..., user_encryption_key: _Optional[str] = ..., re_register: bool = ..., restore_config: bool = ..., throttling_policy: _Optional[_Union[_magneto_pb2.ThrottlingPolicy, _Mapping]] = ...) -> None: ...

class VCDRegisterEntityResult(_message.Message):
    __slots__ = ("vcenter_info_list",)
    VCENTER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    vcenter_info_list: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VCDVCenterInfo]
    def __init__(self, vcenter_info_list: _Optional[_Iterable[_Union[_magneto_pb2.VCDVCenterInfo, _Mapping]]] = ...) -> None: ...

class CassandraRegisterEntityResult(_message.Message):
    __slots__ = ("cassandra_connect_params", "cassandra_additional_params")
    CASSANDRA_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    cassandra_connect_params: _nosql_pb2.CassandraConnectParams
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    def __init__(self, cassandra_connect_params: _Optional[_Union[_nosql_pb2.CassandraConnectParams, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ...) -> None: ...

class HdfsRegisterEntityResult(_message.Message):
    __slots__ = ("hdfs_connect_params",)
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hdfs_connect_params: _nosql_pb2.HdfsConnectParams
    def __init__(self, hdfs_connect_params: _Optional[_Union[_nosql_pb2.HdfsConnectParams, _Mapping]] = ...) -> None: ...

class HiveRegisterEntityResult(_message.Message):
    __slots__ = ("hive_connect_params",)
    HIVE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hive_connect_params: _nosql_pb2.HiveConnectParams
    def __init__(self, hive_connect_params: _Optional[_Union[_nosql_pb2.HiveConnectParams, _Mapping]] = ...) -> None: ...

class HBaseRegisterEntityResult(_message.Message):
    __slots__ = ("hbase_connect_params",)
    HBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hbase_connect_params: _nosql_pb2.HBaseConnectParams
    def __init__(self, hbase_connect_params: _Optional[_Union[_nosql_pb2.HBaseConnectParams, _Mapping]] = ...) -> None: ...

class O365RegisterEntityResult(_message.Message):
    __slots__ = ("async_registration",)
    ASYNC_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    async_registration: bool
    def __init__(self, async_registration: bool = ...) -> None: ...

class EnvRegisterEntityResult(_message.Message):
    __slots__ = ("vcd_register_entity_result", "cassandra_register_entity_result", "hdfs_register_entity_result", "hive_register_entity_result", "hbase_register_entity_result", "o365_register_entity_result")
    VCD_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    HDFS_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    HIVE_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    HBASE_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    vcd_register_entity_result: VCDRegisterEntityResult
    cassandra_register_entity_result: CassandraRegisterEntityResult
    hdfs_register_entity_result: HdfsRegisterEntityResult
    hive_register_entity_result: HiveRegisterEntityResult
    hbase_register_entity_result: HBaseRegisterEntityResult
    o365_register_entity_result: O365RegisterEntityResult
    def __init__(self, vcd_register_entity_result: _Optional[_Union[VCDRegisterEntityResult, _Mapping]] = ..., cassandra_register_entity_result: _Optional[_Union[CassandraRegisterEntityResult, _Mapping]] = ..., hdfs_register_entity_result: _Optional[_Union[HdfsRegisterEntityResult, _Mapping]] = ..., hive_register_entity_result: _Optional[_Union[HiveRegisterEntityResult, _Mapping]] = ..., hbase_register_entity_result: _Optional[_Union[HBaseRegisterEntityResult, _Mapping]] = ..., o365_register_entity_result: _Optional[_Union[O365RegisterEntityResult, _Mapping]] = ...) -> None: ...

class RegisterEntityResult(_message.Message):
    __slots__ = ("error", "entity", "env_register_entity_result", "vcd_register_entity_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENV_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    VCD_REGISTER_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity: _entity_pb2.EntityProto
    env_register_entity_result: EnvRegisterEntityResult
    vcd_register_entity_result: VCDRegisterEntityResult
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., env_register_entity_result: _Optional[_Union[EnvRegisterEntityResult, _Mapping]] = ..., vcd_register_entity_result: _Optional[_Union[VCDRegisterEntityResult, _Mapping]] = ...) -> None: ...

class RegisterOrUpdateAppOwnerArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "owner_entity", "app_env_vec", "credentials", "app_credentials_vec", "uses_persistent_agent", "unregister_owner", "user_info", "is_internal_encrypted", "user_encryption_key", "network_realm_id", "expected_entity_mtime_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    APP_ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    USES_PERSISTENT_AGENT_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_OWNER_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    USER_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    owner_entity: _entity_pb2.EntityProto
    app_env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    credentials: _credentials_pb2.Credentials
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.AppCredentials]
    uses_persistent_agent: bool
    unregister_owner: bool
    user_info: _permissions_pb2.UserInformation
    is_internal_encrypted: bool
    user_encryption_key: str
    network_realm_id: int
    expected_entity_mtime_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., owner_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., app_env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.AppCredentials, _Mapping]]] = ..., uses_persistent_agent: bool = ..., unregister_owner: bool = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., is_internal_encrypted: bool = ..., user_encryption_key: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., expected_entity_mtime_usecs: _Optional[int] = ...) -> None: ...

class RegisterOrUpdateAppOwnerResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateBackupRunArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_uid", "entity_vec", "object_id", "run_start_time_usecs", "copy_snapshot_params_vec", "dso_role", "updated_expiry_time_usecs", "request_source_ip", "request_source_type", "last_updated_username", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    DSO_ROLE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_uid: _universal_id_pb2.UniversalIdProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    object_id: int
    run_start_time_usecs: int
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[CopySnapshotParams]
    dso_role: bool
    updated_expiry_time_usecs: int
    request_source_ip: str
    request_source_type: str
    last_updated_username: str
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., object_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[CopySnapshotParams, _Mapping]]] = ..., dso_role: bool = ..., updated_expiry_time_usecs: _Optional[int] = ..., request_source_ip: _Optional[str] = ..., request_source_type: _Optional[str] = ..., last_updated_username: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class UpdateBackupRunResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateEntityArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity", "new_entity_access_info", "source_side_dedup_enabled", "delete_entity", "operation_spec", "force_delete_entity", "retry_entity_registration", "dag_backup_preference", "registered_entity_params", "is_internal_encrypted", "user_encryption_key", "vm_uses_persistent_agent", "is_proxy_machine", "expected_entity_mtime_usecs", "throttling_policy", "request_timestamp_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITY_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RETRY_ENTITY_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    DAG_BACKUP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    USER_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    VM_USES_PERSISTENT_AGENT_FIELD_NUMBER: _ClassVar[int]
    IS_PROXY_MACHINE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity: _entity_pb2.EntityProto
    new_entity_access_info: EntityAccessInfo
    source_side_dedup_enabled: bool
    delete_entity: bool
    operation_spec: _entity_operations_pb2.EntityOperationSpecProto
    force_delete_entity: bool
    retry_entity_registration: bool
    dag_backup_preference: _exchange_pb2.ExchangeDAGBackupPreference
    registered_entity_params: _magneto_pb2.RegisteredEntityParams
    is_internal_encrypted: bool
    user_encryption_key: str
    vm_uses_persistent_agent: bool
    is_proxy_machine: bool
    expected_entity_mtime_usecs: int
    throttling_policy: _magneto_pb2.ThrottlingPolicy
    request_timestamp_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., new_entity_access_info: _Optional[_Union[EntityAccessInfo, _Mapping]] = ..., source_side_dedup_enabled: bool = ..., delete_entity: bool = ..., operation_spec: _Optional[_Union[_entity_operations_pb2.EntityOperationSpecProto, _Mapping]] = ..., force_delete_entity: bool = ..., retry_entity_registration: bool = ..., dag_backup_preference: _Optional[_Union[_exchange_pb2.ExchangeDAGBackupPreference, _Mapping]] = ..., registered_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ..., is_internal_encrypted: bool = ..., user_encryption_key: _Optional[str] = ..., vm_uses_persistent_agent: bool = ..., is_proxy_machine: bool = ..., expected_entity_mtime_usecs: _Optional[int] = ..., throttling_policy: _Optional[_Union[_magneto_pb2.ThrottlingPolicy, _Mapping]] = ..., request_timestamp_usecs: _Optional[int] = ...) -> None: ...

class UpdateEntityResult(_message.Message):
    __slots__ = ("error", "entity")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity: _entity_pb2.EntityProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class AddOrUpdateEntitiesMetadataArg(_message.Message):
    __slots__ = ("entity_args",)
    class EntityArg(_message.Message):
        __slots__ = ("id", "external_metadata")
        ID_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
        id: _entity_pb2.EntityIdProto
        external_metadata: _magneto_pb2.EntityExternalMetadataProto
        def __init__(self, id: _Optional[_Union[_entity_pb2.EntityIdProto, _Mapping]] = ..., external_metadata: _Optional[_Union[_magneto_pb2.EntityExternalMetadataProto, _Mapping]] = ...) -> None: ...
    ENTITY_ARGS_FIELD_NUMBER: _ClassVar[int]
    entity_args: _containers.RepeatedCompositeFieldContainer[AddOrUpdateEntitiesMetadataArg.EntityArg]
    def __init__(self, entity_args: _Optional[_Iterable[_Union[AddOrUpdateEntitiesMetadataArg.EntityArg, _Mapping]]] = ...) -> None: ...

class AddOrUpdateEntitiesMetadataResult(_message.Message):
    __slots__ = ("err", "entity_results")
    class EntityResult(_message.Message):
        __slots__ = ("id", "err")
        ID_FIELD_NUMBER: _ClassVar[int]
        ERR_FIELD_NUMBER: _ClassVar[int]
        id: _entity_pb2.EntityIdProto
        err: _error_pb2_1.ErrorProto
        def __init__(self, id: _Optional[_Union[_entity_pb2.EntityIdProto, _Mapping]] = ..., err: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...
    ERR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    err: _error_pb2_1.ErrorProto
    entity_results: _containers.RepeatedCompositeFieldContainer[AddOrUpdateEntitiesMetadataResult.EntityResult]
    def __init__(self, err: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity_results: _Optional[_Iterable[_Union[AddOrUpdateEntitiesMetadataResult.EntityResult, _Mapping]]] = ...) -> None: ...

class PatchEntityArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "request_timestamp_usecs", "entity_id", "registered_entity_params", "is_internal_encrypted", "user_encryption_key", "expected_entity_mtime_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    USER_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    request_timestamp_usecs: int
    entity_id: int
    registered_entity_params: _magneto_pb2.RegisteredEntityParams
    is_internal_encrypted: bool
    user_encryption_key: str
    expected_entity_mtime_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., request_timestamp_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., registered_entity_params: _Optional[_Union[_magneto_pb2.RegisteredEntityParams, _Mapping]] = ..., is_internal_encrypted: bool = ..., user_encryption_key: _Optional[str] = ..., expected_entity_mtime_usecs: _Optional[int] = ...) -> None: ...

class PatchEntityResult(_message.Message):
    __slots__ = ("error", "entity")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity: _entity_pb2.EntityProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class O365EntityFilters(_message.Message):
    __slots__ = ("has_valid_mailbox", "has_valid_onedrive", "is_security_group")
    HAS_VALID_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    HAS_VALID_ONEDRIVE_FIELD_NUMBER: _ClassVar[int]
    IS_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    has_valid_mailbox: bool
    has_valid_onedrive: bool
    is_security_group: bool
    def __init__(self, has_valid_mailbox: bool = ..., has_valid_onedrive: bool = ..., is_security_group: bool = ...) -> None: ...

class EntityFilters(_message.Message):
    __slots__ = ("o365_filters", "source_state")
    class SourceStateFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[EntityFilters.SourceStateFilter]
        kInMaintenance: _ClassVar[EntityFilters.SourceStateFilter]
    kNone: EntityFilters.SourceStateFilter
    kInMaintenance: EntityFilters.SourceStateFilter
    O365_FILTERS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
    o365_filters: O365EntityFilters
    source_state: int
    def __init__(self, o365_filters: _Optional[_Union[O365EntityFilters, _Mapping]] = ..., source_state: _Optional[int] = ...) -> None: ...

class EntityContentFilter(_message.Message):
    __slots__ = ("include_external_metadata",)
    INCLUDE_EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    include_external_metadata: bool
    def __init__(self, include_external_metadata: bool = ...) -> None: ...

class GetEntityHierarchyArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity", "type_vec", "only_return_one_level", "num_levels", "refresh_entity_hierarchy", "sid_vec", "user_info", "include_entity_permission_info", "request_timestamp_usecs", "prune_tag_hierarchy", "prune_non_critical_info", "entity_pagination_params", "include_source_credentials", "encryption_key", "filters", "return_object_protection_info", "content_filters")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_ONE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NUM_LEVELS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ENTITY_PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PRUNE_TAG_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    PRUNE_NON_CRITICAL_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PAGINATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SOURCE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    RETURN_OBJECT_PROTECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity: _entity_pb2.EntityProto
    type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    only_return_one_level: bool
    num_levels: int
    refresh_entity_hierarchy: bool
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    include_entity_permission_info: bool
    request_timestamp_usecs: int
    prune_tag_hierarchy: bool
    prune_non_critical_info: bool
    entity_pagination_params: EntityPaginationParams
    include_source_credentials: bool
    encryption_key: str
    filters: EntityFilters
    return_object_protection_info: bool
    content_filters: EntityContentFilter
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., only_return_one_level: bool = ..., num_levels: _Optional[int] = ..., refresh_entity_hierarchy: bool = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., include_entity_permission_info: bool = ..., request_timestamp_usecs: _Optional[int] = ..., prune_tag_hierarchy: bool = ..., prune_non_critical_info: bool = ..., entity_pagination_params: _Optional[_Union[EntityPaginationParams, _Mapping]] = ..., include_source_credentials: bool = ..., encryption_key: _Optional[str] = ..., filters: _Optional[_Union[EntityFilters, _Mapping]] = ..., return_object_protection_info: bool = ..., content_filters: _Optional[_Union[EntityContentFilter, _Mapping]] = ...) -> None: ...

class GetEntityHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy", "entity_permission_info_vec", "object_based_protection_info", "entity_pagination_params")
    class ObjectBasedProtectionInfo(_message.Message):
        __slots__ = ("entity_id", "has_active_object_protection_spec", "auto_protect_parent_id")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        HAS_ACTIVE_OBJECT_PROTECTION_SPEC_FIELD_NUMBER: _ClassVar[int]
        AUTO_PROTECT_PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        has_active_object_protection_spec: bool
        auto_protect_parent_id: int
        def __init__(self, entity_id: _Optional[int] = ..., has_active_object_protection_spec: bool = ..., auto_protect_parent_id: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_BASED_PROTECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PAGINATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    object_based_protection_info: _containers.RepeatedCompositeFieldContainer[GetEntityHierarchyResult.ObjectBasedProtectionInfo]
    entity_pagination_params: EntityPaginationParams
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., object_based_protection_info: _Optional[_Iterable[_Union[GetEntityHierarchyResult.ObjectBasedProtectionInfo, _Mapping]]] = ..., entity_pagination_params: _Optional[_Union[EntityPaginationParams, _Mapping]] = ...) -> None: ...

class GetEntitiesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "ids", "must_exist_in_entity_hierarchy", "include_hash_string", "include_entity_permission_info", "should_return_inferred_permissions")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    MUST_EXIST_IN_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HASH_STRING_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ENTITY_PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETURN_INFERRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    ids: _containers.RepeatedScalarFieldContainer[int]
    must_exist_in_entity_hierarchy: bool
    include_hash_string: bool
    include_entity_permission_info: bool
    should_return_inferred_permissions: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., ids: _Optional[_Iterable[int]] = ..., must_exist_in_entity_hierarchy: bool = ..., include_hash_string: bool = ..., include_entity_permission_info: bool = ..., should_return_inferred_permissions: bool = ...) -> None: ...

class GetEntitiesResult(_message.Message):
    __slots__ = ("error", "entities", "entity_permission_info_vec", "unknown_entity_id_vec", "hash_string_vec", "logical_size_in_bytes_vec", "entity_operation_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    HASH_STRING_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_OPERATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    unknown_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    hash_string_vec: _containers.RepeatedScalarFieldContainer[str]
    logical_size_in_bytes_vec: _containers.RepeatedScalarFieldContainer[int]
    entity_operation_info_vec: _containers.RepeatedCompositeFieldContainer[_entity_operations_pb2.EntityOperationInfoProto]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., unknown_entity_id_vec: _Optional[_Iterable[int]] = ..., hash_string_vec: _Optional[_Iterable[str]] = ..., logical_size_in_bytes_vec: _Optional[_Iterable[int]] = ..., entity_operation_info_vec: _Optional[_Iterable[_Union[_entity_operations_pb2.EntityOperationInfoProto, _Mapping]]] = ...) -> None: ...

class GetEntityIdsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "type_vec", "o365_filters", "only_in_entity_hierarchy", "only_return_leaf_entities", "include_non_protectable_leaf_entites", "network_realm_id", "user_info")
    class O365Filters(_message.Message):
        __slots__ = ("azure_uuid_vec",)
        AZURE_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
        azure_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, azure_uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ONLY_IN_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    ONLY_RETURN_LEAF_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NON_PROTECTABLE_LEAF_ENTITES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    o365_filters: GetEntityIdsArg.O365Filters
    only_in_entity_hierarchy: bool
    only_return_leaf_entities: bool
    include_non_protectable_leaf_entites: bool
    network_realm_id: int
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., o365_filters: _Optional[_Union[GetEntityIdsArg.O365Filters, _Mapping]] = ..., only_in_entity_hierarchy: bool = ..., only_return_leaf_entities: bool = ..., include_non_protectable_leaf_entites: bool = ..., network_realm_id: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class GetEntityIdsResult(_message.Message):
    __slots__ = ("error", "entities")
    class EntityInfo(_message.Message):
        __slots__ = ("id", "in_entity_hierarchy", "is_leaf_entity", "is_registered_entity", "is_top_level_entity")
        ID_FIELD_NUMBER: _ClassVar[int]
        IN_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
        IS_LEAF_ENTITY_FIELD_NUMBER: _ClassVar[int]
        IS_REGISTERED_ENTITY_FIELD_NUMBER: _ClassVar[int]
        IS_TOP_LEVEL_ENTITY_FIELD_NUMBER: _ClassVar[int]
        id: int
        in_entity_hierarchy: bool
        is_leaf_entity: bool
        is_registered_entity: bool
        is_top_level_entity: bool
        def __init__(self, id: _Optional[int] = ..., in_entity_hierarchy: bool = ..., is_leaf_entity: bool = ..., is_registered_entity: bool = ..., is_top_level_entity: bool = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[GetEntityIdsResult.EntityInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[GetEntityIdsResult.EntityInfo, _Mapping]]] = ...) -> None: ...

class GetOrCreateEntityIdsResult(_message.Message):
    __slots__ = ("error", "entities")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class CollectSourceDiagnosticsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id", "type")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id: int
    type: _enums_pb2.Environment.Type
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class CollectSourceDiagnosticsResult(_message.Message):
    __slots__ = ("error", "user_message", "diag_tarball")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DIAG_TARBALL_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    user_message: str
    diag_tarball: str
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_message: _Optional[str] = ..., diag_tarball: _Optional[str] = ...) -> None: ...

class GetBackupRunsForSourceArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "source", "time_range", "include_extension_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXTENSION_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    source: _entity_pb2.EntityProto
    time_range: TimeRange
    include_extension_info: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., include_extension_info: bool = ...) -> None: ...

class GetBackupRunsForSourceResult(_message.Message):
    __slots__ = ("error", "job_runs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_runs: _containers.RepeatedCompositeFieldContainer[BackupJobRunsProto]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_runs: _Optional[_Iterable[_Union[BackupJobRunsProto, _Mapping]]] = ...) -> None: ...

class WriteBlobArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "blob_name", "blob_data")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    blob_name: str
    blob_data: bytes
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., blob_name: _Optional[str] = ..., blob_data: _Optional[bytes] = ...) -> None: ...

class WriteBlobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class ReadBlobArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "blob_name_prefix")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    blob_name_prefix: str
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., blob_name_prefix: _Optional[str] = ...) -> None: ...

class ReadBlobResult(_message.Message):
    __slots__ = ("error", "blobs")
    class Blob(_message.Message):
        __slots__ = ("name", "data")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: bytes
        def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    blobs: _containers.RepeatedCompositeFieldContainer[ReadBlobResult.Blob]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., blobs: _Optional[_Iterable[_Union[ReadBlobResult.Blob, _Mapping]]] = ...) -> None: ...

class GetGateKeeperInfoArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "task_and_sub_task_ids")
    class TaskAndSubTaskId(_message.Message):
        __slots__ = ("task_id", "sub_task_id")
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        sub_task_id: int
        def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TASK_AND_SUB_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    task_and_sub_task_ids: _containers.RepeatedCompositeFieldContainer[GetGateKeeperInfoArg.TaskAndSubTaskId]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., task_and_sub_task_ids: _Optional[_Iterable[_Union[GetGateKeeperInfoArg.TaskAndSubTaskId, _Mapping]]] = ...) -> None: ...

class GetGateKeeperInfoResult(_message.Message):
    __slots__ = ("error", "task_infos")
    class TaskInfo(_message.Message):
        __slots__ = ("task", "task_state")
        TASK_FIELD_NUMBER: _ClassVar[int]
        TASK_STATE_FIELD_NUMBER: _ClassVar[int]
        task: _gatekeeper_pb2.Task
        task_state: _gatekeeper_pb2.TaskState
        def __init__(self, task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., task_state: _Optional[_Union[_gatekeeper_pb2.TaskState, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_INFOS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    task_infos: _containers.RepeatedCompositeFieldContainer[GetGateKeeperInfoResult.TaskInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., task_infos: _Optional[_Iterable[_Union[GetGateKeeperInfoResult.TaskInfo, _Mapping]]] = ...) -> None: ...

class CreateRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "action", "name", "user", "continue_restore_on_error", "restore_vlan_params", "user_info", "objects", "restore_parent_source", "is_multi_stage_restore", "rename_restored_object_param", "rename_restored_vapp_param", "resource_pool_entity", "restored_objects_network_config", "power_state_config", "vcd_config", "datastore_entity_vec", "restore_vmware_vm_params", "restore_hyperv_vm_params", "restore_acropolis_vms_params", "restore_kubernetes_namespaces_params", "restore_kvm_vms_params", "restore_outlook_params", "vault_restore_params", "restore_one_drive_params", "nosql_recover_job_params", "uda_recover_job_params", "target_view_name", "view_params", "mount_volumes_params", "deploy_vms_to_cloud_params", "skip_image_deploy", "skip_rigel_for_restore", "custom_tag_vec", "recover_volumes_params", "recover_file_volumes_params_vec", "recover_virtual_disk_params", "preserve_tags", "preserve_custom_attributes", "restore_site_params", "restore_public_folders_params", "restore_teams_params", "restore_groups_params", "sfdc_recover_job_params", "data_transfer_info", "is_original_restore", "leverage_san_transport", "restore_s3_params", "restore_san_params", "restore_target_entity_id", "download_chats_params")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_RESTORE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_STAGE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_VAPP_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMWARE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_HYPERV_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ACROPOLIS_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KUBERNETES_NAMESPACES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KVM_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OUTLOOK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VAULT_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ONE_DRIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_IMAGE_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VOLUMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECOVER_FILE_VOLUMES_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIRTUAL_DISK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PUBLIC_FOLDERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEAMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_GROUPS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_ORIGINAL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_S3_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CHATS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    action: _magneto_pb2.RestoreType.Type
    name: str
    user: str
    continue_restore_on_error: bool
    restore_vlan_params: _common_pb2.VlanParams
    user_info: _permissions_pb2.UserInformation
    objects: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreObject]
    restore_parent_source: _entity_pb2.EntityProto
    is_multi_stage_restore: bool
    rename_restored_object_param: _magneto_pb2.RenameObjectParamProto
    rename_restored_vapp_param: _magneto_pb2.RenameObjectParamProto
    resource_pool_entity: _entity_pb2.EntityProto
    restored_objects_network_config: _magneto_pb2.RestoredObjectNetworkConfigProto
    power_state_config: _magneto_pb2.PowerStateConfigProto
    vcd_config: RestoredObjectVCDConfigProto
    datastore_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    restore_vmware_vm_params: _vmware_common_pb2.RestoreVMwareVMParams
    restore_hyperv_vm_params: _magneto_pb2.RestoreHyperVVMParams
    restore_acropolis_vms_params: _magneto_pb2.RestoreAcropolisVMsParams
    restore_kubernetes_namespaces_params: _magneto_pb2.RestoreKubernetesNamespacesParams
    restore_kvm_vms_params: _magneto_pb2.RestoreKVMVMsParams
    restore_outlook_params: _magneto_pb2.RestoreOutlookParams
    vault_restore_params: _vault_pb2.VaultParams.RestoreParams
    restore_one_drive_params: _magneto_pb2.RestoreOneDriveParams
    nosql_recover_job_params: _nosql_pb2.NoSqlRecoverJobParams
    uda_recover_job_params: _uda_pb2.UdaRecoverJobParams
    target_view_name: str
    view_params: ViewParams
    mount_volumes_params: _magneto_pb2.MountVolumesParams
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    skip_image_deploy: bool
    skip_rigel_for_restore: bool
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_cloud_deploy_pb2.CustomTag]
    recover_volumes_params: _magneto_pb2.RecoverVolumesParams
    recover_file_volumes_params_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreFilesParams]
    recover_virtual_disk_params: _magneto_pb2.RecoverVirtualDiskParams
    preserve_tags: bool
    preserve_custom_attributes: bool
    restore_site_params: _magneto_pb2.RestoreSiteParams
    restore_public_folders_params: _magneto_pb2.RestoreO365PublicFoldersParams
    restore_teams_params: _magneto_pb2.RestoreO365TeamsParams
    restore_groups_params: _magneto_pb2.RestoreO365GroupsParams
    sfdc_recover_job_params: _sfdc_pb2.SfdcRecoverJobParams
    data_transfer_info: _env_params_pb2_1_1.DataTransferInfo
    is_original_restore: bool
    leverage_san_transport: bool
    restore_s3_params: _magneto_pb2.RestoreS3Params
    restore_san_params: _magneto_pb2.RestoreSanParams
    restore_target_entity_id: int
    download_chats_params: _magneto_pb2.DownloadChatsParams
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., action: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., continue_restore_on_error: bool = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_magneto_pb2.RestoreObject, _Mapping]]] = ..., restore_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_multi_stage_restore: bool = ..., rename_restored_object_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., rename_restored_vapp_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[_magneto_pb2.RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[_magneto_pb2.PowerStateConfigProto, _Mapping]] = ..., vcd_config: _Optional[_Union[RestoredObjectVCDConfigProto, _Mapping]] = ..., datastore_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., restore_vmware_vm_params: _Optional[_Union[_vmware_common_pb2.RestoreVMwareVMParams, _Mapping]] = ..., restore_hyperv_vm_params: _Optional[_Union[_magneto_pb2.RestoreHyperVVMParams, _Mapping]] = ..., restore_acropolis_vms_params: _Optional[_Union[_magneto_pb2.RestoreAcropolisVMsParams, _Mapping]] = ..., restore_kubernetes_namespaces_params: _Optional[_Union[_magneto_pb2.RestoreKubernetesNamespacesParams, _Mapping]] = ..., restore_kvm_vms_params: _Optional[_Union[_magneto_pb2.RestoreKVMVMsParams, _Mapping]] = ..., restore_outlook_params: _Optional[_Union[_magneto_pb2.RestoreOutlookParams, _Mapping]] = ..., vault_restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ..., restore_one_drive_params: _Optional[_Union[_magneto_pb2.RestoreOneDriveParams, _Mapping]] = ..., nosql_recover_job_params: _Optional[_Union[_nosql_pb2.NoSqlRecoverJobParams, _Mapping]] = ..., uda_recover_job_params: _Optional[_Union[_uda_pb2.UdaRecoverJobParams, _Mapping]] = ..., target_view_name: _Optional[str] = ..., view_params: _Optional[_Union[ViewParams, _Mapping]] = ..., mount_volumes_params: _Optional[_Union[_magneto_pb2.MountVolumesParams, _Mapping]] = ..., deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ..., skip_image_deploy: bool = ..., skip_rigel_for_restore: bool = ..., custom_tag_vec: _Optional[_Iterable[_Union[_cloud_deploy_pb2.CustomTag, _Mapping]]] = ..., recover_volumes_params: _Optional[_Union[_magneto_pb2.RecoverVolumesParams, _Mapping]] = ..., recover_file_volumes_params_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreFilesParams, _Mapping]]] = ..., recover_virtual_disk_params: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskParams, _Mapping]] = ..., preserve_tags: bool = ..., preserve_custom_attributes: bool = ..., restore_site_params: _Optional[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]] = ..., restore_public_folders_params: _Optional[_Union[_magneto_pb2.RestoreO365PublicFoldersParams, _Mapping]] = ..., restore_teams_params: _Optional[_Union[_magneto_pb2.RestoreO365TeamsParams, _Mapping]] = ..., restore_groups_params: _Optional[_Union[_magneto_pb2.RestoreO365GroupsParams, _Mapping]] = ..., sfdc_recover_job_params: _Optional[_Union[_sfdc_pb2.SfdcRecoverJobParams, _Mapping]] = ..., data_transfer_info: _Optional[_Union[_env_params_pb2_1_1.DataTransferInfo, _Mapping]] = ..., is_original_restore: bool = ..., leverage_san_transport: bool = ..., restore_s3_params: _Optional[_Union[_magneto_pb2.RestoreS3Params, _Mapping]] = ..., restore_san_params: _Optional[_Union[_magneto_pb2.RestoreSanParams, _Mapping]] = ..., restore_target_entity_id: _Optional[int] = ..., download_chats_params: _Optional[_Union[_magneto_pb2.DownloadChatsParams, _Mapping]] = ...) -> None: ...

class CreateRestoreTaskResult(_message.Message):
    __slots__ = ("error", "restore_task_id", "user_message", "restore_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    restore_task_id: int
    user_message: str
    restore_info: RestoreWrapperProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., restore_task_id: _Optional[int] = ..., user_message: _Optional[str] = ..., restore_info: _Optional[_Union[RestoreWrapperProto, _Mapping]] = ...) -> None: ...

class CreateRestoreMultiAppTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "name", "user", "user_info", "action", "restore_app_params_vec", "restore_vlan_params")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    name: str
    user: str
    user_info: _permissions_pb2.UserInformation
    action: _magneto_pb2.RestoreType.Type
    restore_app_params_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreAppParams]
    restore_vlan_params: _common_pb2.VlanParams
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., action: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., restore_app_params_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreAppParams, _Mapping]]] = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ...) -> None: ...

class CreateRestoreMultiAppTaskResult(_message.Message):
    __slots__ = ("error", "restore_task_id", "user_message")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    restore_task_id: int
    user_message: str
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., restore_task_id: _Optional[int] = ..., user_message: _Optional[str] = ...) -> None: ...

class CreateRestoreAppTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "action", "name", "user", "restore_app_params", "restore_vlan_params", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    action: _magneto_pb2.RestoreType.Type
    name: str
    user: str
    restore_app_params: _magneto_pb2.RestoreAppParams
    restore_vlan_params: _common_pb2.VlanParams
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., action: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., restore_app_params: _Optional[_Union[_magneto_pb2.RestoreAppParams, _Mapping]] = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class CreateRestoreAppTaskResult(_message.Message):
    __slots__ = ("error", "restore_task_id", "user_message", "restore_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    restore_task_id: int
    user_message: str
    restore_info: RestoreWrapperProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., restore_task_id: _Optional[int] = ..., user_message: _Optional[str] = ..., restore_info: _Optional[_Union[RestoreWrapperProto, _Mapping]] = ...) -> None: ...

class ModifyRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "user_info", "restore_task_id", "child_restore_task_ids", "sql_options", "ad_options", "oracle_options", "options")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_RESTORE_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    SQL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AD_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    user_info: _permissions_pb2.UserInformation
    restore_task_id: int
    child_restore_task_ids: _containers.RepeatedScalarFieldContainer[int]
    sql_options: _magneto_pb2.SqlUpdateRestoreTaskOptions
    ad_options: _magneto_pb2.ADUpdateRestoreTaskOptions
    oracle_options: _magneto_pb2.OracleUpdateRestoreTaskOptions
    options: _magneto_pb2.UpdateRestoreTaskOptions
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., restore_task_id: _Optional[int] = ..., child_restore_task_ids: _Optional[_Iterable[int]] = ..., sql_options: _Optional[_Union[_magneto_pb2.SqlUpdateRestoreTaskOptions, _Mapping]] = ..., ad_options: _Optional[_Union[_magneto_pb2.ADUpdateRestoreTaskOptions, _Mapping]] = ..., oracle_options: _Optional[_Union[_magneto_pb2.OracleUpdateRestoreTaskOptions, _Mapping]] = ..., options: _Optional[_Union[_magneto_pb2.UpdateRestoreTaskOptions, _Mapping]] = ...) -> None: ...

class ModifyRestoreTaskResult(_message.Message):
    __slots__ = ("error", "user_message")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    user_message: str
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_message: _Optional[str] = ...) -> None: ...

class CheckRestoreAppTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "restore_app_params")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    restore_app_params: _magneto_pb2.RestoreAppParams
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., restore_app_params: _Optional[_Union[_magneto_pb2.RestoreAppParams, _Mapping]] = ...) -> None: ...

class CheckRestoreAppTaskResult(_message.Message):
    __slots__ = ("error", "user_message", "entity_info")
    class FullSnapshotInfo(_message.Message):
        __slots__ = ("run_start_time_usecs", "entity_size", "backup_type")
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ENTITY_SIZE_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        run_start_time_usecs: int
        entity_size: int
        backup_type: _enums_pb2.ScheduledBackupType.Type
        def __init__(self, run_start_time_usecs: _Optional[int] = ..., entity_size: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ...) -> None: ...
    class LogSnapshotInfo(_message.Message):
        __slots__ = ("run_start_time_usecs", "snapshot_size")
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_SIZE_FIELD_NUMBER: _ClassVar[int]
        run_start_time_usecs: int
        snapshot_size: int
        def __init__(self, run_start_time_usecs: _Optional[int] = ..., snapshot_size: _Optional[int] = ...) -> None: ...
    class EntityInfo(_message.Message):
        __slots__ = ("entity", "full_snapshot_info", "log_snapshot_info_vec")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        FULL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        LOG_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        full_snapshot_info: CheckRestoreAppTaskResult.FullSnapshotInfo
        log_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[CheckRestoreAppTaskResult.LogSnapshotInfo]
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., full_snapshot_info: _Optional[_Union[CheckRestoreAppTaskResult.FullSnapshotInfo, _Mapping]] = ..., log_snapshot_info_vec: _Optional[_Iterable[_Union[CheckRestoreAppTaskResult.LogSnapshotInfo, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    user_message: str
    entity_info: CheckRestoreAppTaskResult.EntityInfo
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_message: _Optional[str] = ..., entity_info: _Optional[_Union[CheckRestoreAppTaskResult.EntityInfo, _Mapping]] = ...) -> None: ...

class TimeRangeInfo(_message.Message):
    __slots__ = ("time_range_vec", "user_message", "error")
    TIME_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    time_range_vec: _containers.RepeatedCompositeFieldContainer[TimeRange]
    user_message: str
    error: _error_pb2_1.ErrorProto
    def __init__(self, time_range_vec: _Optional[_Iterable[_Union[TimeRange, _Mapping]]] = ..., user_message: _Optional[str] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class MirrorParams(_message.Message):
    __slots__ = ("paused", "previous_view_name", "finalized")
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    paused: bool
    previous_view_name: str
    finalized: bool
    def __init__(self, paused: bool = ..., previous_view_name: _Optional[str] = ..., finalized: bool = ...) -> None: ...

class GetRestoreAppTimeRangesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "type", "restore_app_object_vec", "owner_object_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNER_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    type: _enums_pb2.Environment.Type
    restore_app_object_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreAppObject]
    owner_object_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreObject]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_app_object_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreAppObject, _Mapping]]] = ..., owner_object_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreObject, _Mapping]]] = ...) -> None: ...

class GetRestoreAppTimeRangesResult(_message.Message):
    __slots__ = ("error", "owner_object_time_range_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OWNER_OBJECT_TIME_RANGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    owner_object_time_range_info_vec: _containers.RepeatedCompositeFieldContainer[TimeRangeInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., owner_object_time_range_info_vec: _Optional[_Iterable[_Union[TimeRangeInfo, _Mapping]]] = ...) -> None: ...

class GetRestorePointsForTimeRangeArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "type", "entity_id", "job_uids", "time_range")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    type: _enums_pb2.Environment.Type
    entity_id: int
    job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    time_range: TimeRange
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., entity_id: _Optional[int] = ..., job_uids: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ...) -> None: ...

class GetRestorePointsForTimeRangeResult(_message.Message):
    __slots__ = ("error", "time_range_info", "full_snapshots")
    class FullSnapshotInfo(_message.Message):
        __slots__ = ("restore_object", "snapshot_targets")
        RESTORE_OBJECT_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TARGETS_FIELD_NUMBER: _ClassVar[int]
        restore_object: _magneto_pb2.RestoreObject
        snapshot_targets: _containers.RepeatedCompositeFieldContainer[_policy_pb2.SnapshotTarget]
        def __init__(self, restore_object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ..., snapshot_targets: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTarget, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    FULL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    time_range_info: TimeRangeInfo
    full_snapshots: _containers.RepeatedCompositeFieldContainer[GetRestorePointsForTimeRangeResult.FullSnapshotInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., time_range_info: _Optional[_Union[TimeRangeInfo, _Mapping]] = ..., full_snapshots: _Optional[_Iterable[_Union[GetRestorePointsForTimeRangeResult.FullSnapshotInfo, _Mapping]]] = ...) -> None: ...

class GetRestoreMetaDataRangesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "type", "entity_id", "job_uids", "time_range")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    type: _enums_pb2.Environment.Type
    entity_id: int
    job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    time_range: TimeRange
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., entity_id: _Optional[int] = ..., job_uids: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ...) -> None: ...

class GetRestoreMetaDataRangesResult(_message.Message):
    __slots__ = ("error", "oracle_archive_log_restore_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    oracle_archive_log_restore_info: _magneto_pb2.OracleArchiveLogInfo
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., oracle_archive_log_restore_info: _Optional[_Union[_magneto_pb2.OracleArchiveLogInfo, _Mapping]] = ...) -> None: ...

class RestoreTaskStateBaseProto(_message.Message):
    __slots__ = ("type", "name", "user", "task_id", "task_uid", "status", "refresh_status", "public_status", "error", "warnings", "preprocessing_error", "user_messages", "parent_source_connection_params", "start_time_usecs", "end_time_usecs", "scheduled_constituent_id", "scheduled_gandalf_session_id", "restore_vlan_params", "cancellation_requested", "user_info", "total_logical_size_bytes", "total_physical_size_bytes", "is_internal")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSING_ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    type: _magneto_pb2.RestoreType.Type
    name: str
    user: str
    task_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    status: _enums_pb2_1.RestoreTaskStatus.Type
    refresh_status: _enums_pb2_1.RefreshTaskStatus.Type
    public_status: _enums_pb2.PublicTaskStatus.Type
    error: _error_pb2_1.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    preprocessing_error: _error_pb2_1.ErrorProto
    user_messages: _containers.RepeatedScalarFieldContainer[str]
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    start_time_usecs: int
    end_time_usecs: int
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    restore_vlan_params: _common_pb2.VlanParams
    cancellation_requested: bool
    user_info: _permissions_pb2.UserInformation
    total_logical_size_bytes: int
    total_physical_size_bytes: int
    is_internal: bool
    def __init__(self, type: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., task_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., status: _Optional[_Union[_enums_pb2_1.RestoreTaskStatus.Type, str]] = ..., refresh_status: _Optional[_Union[_enums_pb2_1.RefreshTaskStatus.Type, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., preprocessing_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_messages: _Optional[_Iterable[str]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., cancellation_requested: bool = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., total_logical_size_bytes: _Optional[int] = ..., total_physical_size_bytes: _Optional[int] = ..., is_internal: bool = ...) -> None: ...

class RestoredObjectVCDConfigProto(_message.Message):
    __slots__ = ("is_vapp", "vcenter_connector_params", "vapp_entity", "vdc_entity", "is_vapp_template", "restored_vapp_info", "restored_vapp_template_info", "restored_vapp_object", "restored_vapp_template_object")
    IS_VAPP_FIELD_NUMBER: _ClassVar[int]
    VCENTER_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VAPP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VDC_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_VAPP_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RESTORED_VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORED_VAPP_TEMPLATE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORED_VAPP_OBJECT_FIELD_NUMBER: _ClassVar[int]
    RESTORED_VAPP_TEMPLATE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    is_vapp: bool
    vcenter_connector_params: _magneto_pb2.ConnectorParams
    vapp_entity: _entity_pb2.EntityProto
    vdc_entity: _entity_pb2.EntityProto
    is_vapp_template: bool
    restored_vapp_info: _entity_pb2.EntityProto
    restored_vapp_template_info: _entity_pb2.EntityProto
    restored_vapp_object: _magneto_pb2.RestoreObject
    restored_vapp_template_object: _magneto_pb2.RestoreObject
    def __init__(self, is_vapp: bool = ..., vcenter_connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., vapp_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., vdc_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_vapp_template: bool = ..., restored_vapp_info: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restored_vapp_template_info: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restored_vapp_object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ..., restored_vapp_template_object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ...) -> None: ...

class PerformRestoreTaskStateProto(_message.Message):
    __slots__ = ("base", "full_view_name", "view_box_id", "restored_data_storage_domain_id", "progress_monitor_task_path", "parent_restore_job_id", "objects", "volume_info_vec", "restored_to_different_source", "restore_parent_source", "restore_sub_task_vec", "parent_restore_task_id", "multi_restore_task_id", "should_finish_first_task_id", "child_destroy_task_id", "child_clone_task_id", "retrieve_archive_task_uid_vec", "retrieve_archive_progress_monitor_task_path", "retrieve_archive_view_name", "retrieve_archive_stub_view_name", "stub_view_relative_dir_name", "retrieve_archive_task_vec", "skip_cloning_retrieve_archive_view", "cdp_restore_task_id", "cdp_restore_progress_monitor_task_path", "cdp_restore_task", "cdp_restore_view_name", "vm_restore_reuse_cdp_view", "can_teardown", "is_multi_stage_restore", "restore_files_task_state", "restore_app_task_state", "mount_volumes_task_state", "recover_volumes_task_state", "recover_disks_task_state", "deploy_vms_to_cloud_task_state", "cloud_deploy_info", "objects_progress_monitor_task_paths", "restore_standby_task_state", "multi_stage_restore_task_state", "rename_restored_object_param", "rename_restored_vapp_param", "resource_pool_entity", "restored_objects_network_config", "power_state_config", "datastore_entity_vec", "vcd_config", "selected_datastore_idx", "continue_restore_on_error", "restore_vmware_vm_params", "restore_hyperv_vm_params", "restore_acropolis_vms_params", "restore_kvm_vms_params", "restore_outlook_params", "vault_restore_params", "restore_kubernetes_namespaces_params", "restore_one_drive_params", "nosql_connect_params", "nosql_recover_job_params", "uda_recover_job_params", "restore_site_params", "restore_public_folders_params", "restore_teams_params", "restore_groups_params", "sfdc_recover_job_params", "sfdc_connect_params", "restore_s3_params", "restore_san_params", "encryption_params", "mirror_params", "download_chats_params", "create_view", "view_params", "skip_image_deploy", "skip_rigel_for_restore", "custom_tag_vec", "restore_info", "restore_view_datastore_entity", "folder_entity", "restore_task_purged", "related_restore_task_id", "clone_app_view_info", "physical_flr_parallel_restore", "vcd_storage_profile_datastore_moref_vec", "physical_flr_use_new_locking_method", "backup_run_lock_vec", "data_transfer_info", "view_name_DEPRECATED", "object_name_DEPRECATED", "path_prefix_DEPRECATED", "preserve_tags", "include_vm_config", "action_executor_target_type", "leverage_san_transport", "restore_target_entity_id", "request_sha1_checksum")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FULL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORED_DATA_STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESTORE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORED_TO_DIFFERENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MULTI_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_FINISH_FIRST_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_DESTROY_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_RELATIVE_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONING_RETRIEVE_ARCHIVE_VIEW_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_TASK_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_REUSE_CDP_VIEW_FIELD_NUMBER: _ClassVar[int]
    CAN_TEARDOWN_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_STAGE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VOLUMES_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RECOVER_DISKS_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_PROGRESS_MONITOR_TASK_PATHS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_STANDBY_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_VAPP_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DATASTORE_IDX_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_RESTORE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMWARE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_HYPERV_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ACROPOLIS_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KVM_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OUTLOOK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VAULT_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KUBERNETES_NAMESPACES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ONE_DRIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PUBLIC_FOLDERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEAMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_GROUPS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_S3_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CHATS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_IMAGE_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VIEW_DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_PURGED_FIELD_NUMBER: _ClassVar[int]
    RELATED_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_APP_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_FLR_PARALLEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    VCD_STORAGE_PROFILE_DATASTORE_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_FLR_USE_NEW_LOCKING_METHOD_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_LOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SHA1_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    base: RestoreTaskStateBaseProto
    full_view_name: str
    view_box_id: int
    restored_data_storage_domain_id: int
    progress_monitor_task_path: str
    parent_restore_job_id: int
    objects: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreObject]
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.VolumeInfo]
    restored_to_different_source: bool
    restore_parent_source: _entity_pb2.EntityProto
    restore_sub_task_vec: _containers.RepeatedScalarFieldContainer[int]
    parent_restore_task_id: int
    multi_restore_task_id: int
    should_finish_first_task_id: int
    child_destroy_task_id: int
    child_clone_task_id: int
    retrieve_archive_task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    retrieve_archive_progress_monitor_task_path: str
    retrieve_archive_view_name: str
    retrieve_archive_stub_view_name: str
    stub_view_relative_dir_name: str
    retrieve_archive_task_vec: _containers.RepeatedCompositeFieldContainer[RetrieveArchiveTaskStateProto]
    skip_cloning_retrieve_archive_view: bool
    cdp_restore_task_id: int
    cdp_restore_progress_monitor_task_path: str
    cdp_restore_task: PerformRestoreTaskStateProto
    cdp_restore_view_name: str
    vm_restore_reuse_cdp_view: bool
    can_teardown: bool
    is_multi_stage_restore: bool
    restore_files_task_state: RestoreFilesTaskStateProto
    restore_app_task_state: RestoreAppTaskStateProto
    mount_volumes_task_state: MountVolumesTaskStateProto
    recover_volumes_task_state: RecoverVolumesTaskStateProto
    recover_disks_task_state: RecoverDisksTaskStateProto
    deploy_vms_to_cloud_task_state: DeployVMsToCloudTaskStateProto
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    objects_progress_monitor_task_paths: _containers.RepeatedScalarFieldContainer[str]
    restore_standby_task_state: RestoreStandbyTaskStateProto
    multi_stage_restore_task_state: MultiStageRestoreTaskStateProto
    rename_restored_object_param: _magneto_pb2.RenameObjectParamProto
    rename_restored_vapp_param: _magneto_pb2.RenameObjectParamProto
    resource_pool_entity: _entity_pb2.EntityProto
    restored_objects_network_config: _magneto_pb2.RestoredObjectNetworkConfigProto
    power_state_config: _magneto_pb2.PowerStateConfigProto
    datastore_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    vcd_config: RestoredObjectVCDConfigProto
    selected_datastore_idx: int
    continue_restore_on_error: bool
    restore_vmware_vm_params: _vmware_common_pb2.RestoreVMwareVMParams
    restore_hyperv_vm_params: _magneto_pb2.RestoreHyperVVMParams
    restore_acropolis_vms_params: _magneto_pb2.RestoreAcropolisVMsParams
    restore_kvm_vms_params: _magneto_pb2.RestoreKVMVMsParams
    restore_outlook_params: _magneto_pb2.RestoreOutlookParams
    vault_restore_params: _vault_pb2.VaultParams.RestoreParams
    restore_kubernetes_namespaces_params: _magneto_pb2.RestoreKubernetesNamespacesParams
    restore_one_drive_params: _magneto_pb2.RestoreOneDriveParams
    nosql_connect_params: _magneto_pb2.NoSqlConnectParams
    nosql_recover_job_params: _nosql_pb2.NoSqlRecoverJobParams
    uda_recover_job_params: _uda_pb2.UdaRecoverJobParams
    restore_site_params: _magneto_pb2.RestoreSiteParams
    restore_public_folders_params: _magneto_pb2.RestoreO365PublicFoldersParams
    restore_teams_params: _magneto_pb2.RestoreO365TeamsParams
    restore_groups_params: _magneto_pb2.RestoreO365GroupsParams
    sfdc_recover_job_params: _sfdc_pb2.SfdcRecoverJobParams
    sfdc_connect_params: _sfdc_pb2.RegisteredEntitySfdcParams
    restore_s3_params: _magneto_pb2.RestoreS3Params
    restore_san_params: _magneto_pb2.RestoreSanParams
    encryption_params: _cloud_deploy_pb2.EncryptionParams
    mirror_params: MirrorParams
    download_chats_params: _magneto_pb2.DownloadChatsParams
    create_view: bool
    view_params: ViewParams
    skip_image_deploy: bool
    skip_rigel_for_restore: bool
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_cloud_deploy_pb2.CustomTag]
    restore_info: _magneto_pb2.RestoreInfoProto
    restore_view_datastore_entity: _entity_pb2.EntityProto
    folder_entity: _entity_pb2.EntityProto
    restore_task_purged: bool
    related_restore_task_id: int
    clone_app_view_info: _magneto_pb2.CloneAppViewInfoProto
    physical_flr_parallel_restore: bool
    vcd_storage_profile_datastore_moref_vec: _containers.RepeatedScalarFieldContainer[str]
    physical_flr_use_new_locking_method: bool
    backup_run_lock_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupRunId]
    data_transfer_info: _env_params_pb2_1_1.DataTransferInfo
    view_name_DEPRECATED: str
    object_name_DEPRECATED: str
    path_prefix_DEPRECATED: str
    preserve_tags: bool
    include_vm_config: bool
    action_executor_target_type: _enums_pb2.TargetType.Type
    leverage_san_transport: bool
    restore_target_entity_id: int
    request_sha1_checksum: bytes
    def __init__(self, base: _Optional[_Union[RestoreTaskStateBaseProto, _Mapping]] = ..., full_view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., restored_data_storage_domain_id: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., parent_restore_job_id: _Optional[int] = ..., objects: _Optional[_Iterable[_Union[_magneto_pb2.RestoreObject, _Mapping]]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_volume_info_pb2.VolumeInfo, _Mapping]]] = ..., restored_to_different_source: bool = ..., restore_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_sub_task_vec: _Optional[_Iterable[int]] = ..., parent_restore_task_id: _Optional[int] = ..., multi_restore_task_id: _Optional[int] = ..., should_finish_first_task_id: _Optional[int] = ..., child_destroy_task_id: _Optional[int] = ..., child_clone_task_id: _Optional[int] = ..., retrieve_archive_task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., retrieve_archive_progress_monitor_task_path: _Optional[str] = ..., retrieve_archive_view_name: _Optional[str] = ..., retrieve_archive_stub_view_name: _Optional[str] = ..., stub_view_relative_dir_name: _Optional[str] = ..., retrieve_archive_task_vec: _Optional[_Iterable[_Union[RetrieveArchiveTaskStateProto, _Mapping]]] = ..., skip_cloning_retrieve_archive_view: bool = ..., cdp_restore_task_id: _Optional[int] = ..., cdp_restore_progress_monitor_task_path: _Optional[str] = ..., cdp_restore_task: _Optional[_Union[PerformRestoreTaskStateProto, _Mapping]] = ..., cdp_restore_view_name: _Optional[str] = ..., vm_restore_reuse_cdp_view: bool = ..., can_teardown: bool = ..., is_multi_stage_restore: bool = ..., restore_files_task_state: _Optional[_Union[RestoreFilesTaskStateProto, _Mapping]] = ..., restore_app_task_state: _Optional[_Union[RestoreAppTaskStateProto, _Mapping]] = ..., mount_volumes_task_state: _Optional[_Union[MountVolumesTaskStateProto, _Mapping]] = ..., recover_volumes_task_state: _Optional[_Union[RecoverVolumesTaskStateProto, _Mapping]] = ..., recover_disks_task_state: _Optional[_Union[RecoverDisksTaskStateProto, _Mapping]] = ..., deploy_vms_to_cloud_task_state: _Optional[_Union[DeployVMsToCloudTaskStateProto, _Mapping]] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., objects_progress_monitor_task_paths: _Optional[_Iterable[str]] = ..., restore_standby_task_state: _Optional[_Union[RestoreStandbyTaskStateProto, _Mapping]] = ..., multi_stage_restore_task_state: _Optional[_Union[MultiStageRestoreTaskStateProto, _Mapping]] = ..., rename_restored_object_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., rename_restored_vapp_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[_magneto_pb2.RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[_magneto_pb2.PowerStateConfigProto, _Mapping]] = ..., datastore_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., vcd_config: _Optional[_Union[RestoredObjectVCDConfigProto, _Mapping]] = ..., selected_datastore_idx: _Optional[int] = ..., continue_restore_on_error: bool = ..., restore_vmware_vm_params: _Optional[_Union[_vmware_common_pb2.RestoreVMwareVMParams, _Mapping]] = ..., restore_hyperv_vm_params: _Optional[_Union[_magneto_pb2.RestoreHyperVVMParams, _Mapping]] = ..., restore_acropolis_vms_params: _Optional[_Union[_magneto_pb2.RestoreAcropolisVMsParams, _Mapping]] = ..., restore_kvm_vms_params: _Optional[_Union[_magneto_pb2.RestoreKVMVMsParams, _Mapping]] = ..., restore_outlook_params: _Optional[_Union[_magneto_pb2.RestoreOutlookParams, _Mapping]] = ..., vault_restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ..., restore_kubernetes_namespaces_params: _Optional[_Union[_magneto_pb2.RestoreKubernetesNamespacesParams, _Mapping]] = ..., restore_one_drive_params: _Optional[_Union[_magneto_pb2.RestoreOneDriveParams, _Mapping]] = ..., nosql_connect_params: _Optional[_Union[_magneto_pb2.NoSqlConnectParams, _Mapping]] = ..., nosql_recover_job_params: _Optional[_Union[_nosql_pb2.NoSqlRecoverJobParams, _Mapping]] = ..., uda_recover_job_params: _Optional[_Union[_uda_pb2.UdaRecoverJobParams, _Mapping]] = ..., restore_site_params: _Optional[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]] = ..., restore_public_folders_params: _Optional[_Union[_magneto_pb2.RestoreO365PublicFoldersParams, _Mapping]] = ..., restore_teams_params: _Optional[_Union[_magneto_pb2.RestoreO365TeamsParams, _Mapping]] = ..., restore_groups_params: _Optional[_Union[_magneto_pb2.RestoreO365GroupsParams, _Mapping]] = ..., sfdc_recover_job_params: _Optional[_Union[_sfdc_pb2.SfdcRecoverJobParams, _Mapping]] = ..., sfdc_connect_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., restore_s3_params: _Optional[_Union[_magneto_pb2.RestoreS3Params, _Mapping]] = ..., restore_san_params: _Optional[_Union[_magneto_pb2.RestoreSanParams, _Mapping]] = ..., encryption_params: _Optional[_Union[_cloud_deploy_pb2.EncryptionParams, _Mapping]] = ..., mirror_params: _Optional[_Union[MirrorParams, _Mapping]] = ..., download_chats_params: _Optional[_Union[_magneto_pb2.DownloadChatsParams, _Mapping]] = ..., create_view: bool = ..., view_params: _Optional[_Union[ViewParams, _Mapping]] = ..., skip_image_deploy: bool = ..., skip_rigel_for_restore: bool = ..., custom_tag_vec: _Optional[_Iterable[_Union[_cloud_deploy_pb2.CustomTag, _Mapping]]] = ..., restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ..., restore_view_datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., folder_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_task_purged: bool = ..., related_restore_task_id: _Optional[int] = ..., clone_app_view_info: _Optional[_Union[_magneto_pb2.CloneAppViewInfoProto, _Mapping]] = ..., physical_flr_parallel_restore: bool = ..., vcd_storage_profile_datastore_moref_vec: _Optional[_Iterable[str]] = ..., physical_flr_use_new_locking_method: bool = ..., backup_run_lock_vec: _Optional[_Iterable[_Union[_magneto_pb2.BackupRunId, _Mapping]]] = ..., data_transfer_info: _Optional[_Union[_env_params_pb2_1_1.DataTransferInfo, _Mapping]] = ..., view_name_DEPRECATED: _Optional[str] = ..., object_name_DEPRECATED: _Optional[str] = ..., path_prefix_DEPRECATED: _Optional[str] = ..., preserve_tags: bool = ..., include_vm_config: bool = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., leverage_san_transport: bool = ..., restore_target_entity_id: _Optional[int] = ..., request_sha1_checksum: _Optional[bytes] = ...) -> None: ...

class PerformRestoreJobStateProto(_message.Message):
    __slots__ = ("type", "name", "user", "restore_job_id", "restore_job_uid", "progress_monitor_task_path", "restore_task_vec", "continue_restore_on_error", "restored_to_different_source", "restore_parent_source", "parent_source_connection_params", "restore_acropolis_vms_params", "restore_kubernetes_namespaces_params", "nosql_connect_params", "nosql_recover_job_params", "view_box_id", "start_time_usecs", "admitted_time_usecs", "end_time_usecs", "status", "error", "warnings", "cancellation_requested", "restore_kvm_vms_params", "restore_vmware_vm_params", "power_state_config", "deploy_vms_to_cloud_task_state", "user_info", "rename_restored_object_param", "restored_objects_network_config", "preserve_tags", "restore_task_state_proto_tmpl", "restore_site_params", "restore_public_folders_params", "restore_teams_params", "restore_groups_params", "physical_flr_parallel_restore", "vcd_config", "objects", "rename_restored_vapp_param", "skip_image_deploy", "skip_rigel_for_restore", "custom_tag_vec", "target_view_name", "view_params", "data_transfer_info", "leverage_san_transport", "restore_s3_params", "encryption_params", "uda_recover_job_params", "restore_target_entity_id", "request_sha1_checksum", "download_chats_params")
    class RestoreTask(_message.Message):
        __slots__ = ("object", "task_id", "object_progress_monitor_task_path", "preprocessing_error")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        PREPROCESSING_ERROR_FIELD_NUMBER: _ClassVar[int]
        object: _magneto_pb2.RestoreObject
        task_id: int
        object_progress_monitor_task_path: str
        preprocessing_error: _error_pb2_1.ErrorProto
        def __init__(self, object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ..., task_id: _Optional[int] = ..., object_progress_monitor_task_path: _Optional[str] = ..., preprocessing_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_RESTORE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORED_TO_DIFFERENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ACROPOLIS_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KUBERNETES_NAMESPACES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ADMITTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_KVM_VMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMWARE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_STATE_PROTO_TMPL_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PUBLIC_FOLDERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEAMS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_GROUPS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_FLR_PARALLEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_VAPP_PARAM_FIELD_NUMBER: _ClassVar[int]
    SKIP_IMAGE_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_S3_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SHA1_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CHATS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: _magneto_pb2.RestoreType.Type
    name: str
    user: str
    restore_job_id: int
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    progress_monitor_task_path: str
    restore_task_vec: _containers.RepeatedCompositeFieldContainer[PerformRestoreJobStateProto.RestoreTask]
    continue_restore_on_error: bool
    restored_to_different_source: bool
    restore_parent_source: _entity_pb2.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    restore_acropolis_vms_params: _magneto_pb2.RestoreAcropolisVMsParams
    restore_kubernetes_namespaces_params: _magneto_pb2.RestoreKubernetesNamespacesParams
    nosql_connect_params: _magneto_pb2.NoSqlConnectParams
    nosql_recover_job_params: _nosql_pb2.NoSqlRecoverJobParams
    view_box_id: int
    start_time_usecs: int
    admitted_time_usecs: int
    end_time_usecs: int
    status: _enums_pb2_1.RestoreJobStatus.Type
    error: _error_pb2_1.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    cancellation_requested: bool
    restore_kvm_vms_params: _magneto_pb2.RestoreKVMVMsParams
    restore_vmware_vm_params: _vmware_common_pb2.RestoreVMwareVMParams
    power_state_config: _magneto_pb2.PowerStateConfigProto
    deploy_vms_to_cloud_task_state: DeployVMsToCloudTaskStateProto
    user_info: _permissions_pb2.UserInformation
    rename_restored_object_param: _magneto_pb2.RenameObjectParamProto
    restored_objects_network_config: _magneto_pb2.RestoredObjectNetworkConfigProto
    preserve_tags: bool
    restore_task_state_proto_tmpl: PerformRestoreTaskStateProto
    restore_site_params: _magneto_pb2.RestoreSiteParams
    restore_public_folders_params: _magneto_pb2.RestoreO365PublicFoldersParams
    restore_teams_params: _magneto_pb2.RestoreO365TeamsParams
    restore_groups_params: _magneto_pb2.RestoreO365GroupsParams
    physical_flr_parallel_restore: bool
    vcd_config: RestoredObjectVCDConfigProto
    objects: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreObject]
    rename_restored_vapp_param: _magneto_pb2.RenameObjectParamProto
    skip_image_deploy: bool
    skip_rigel_for_restore: bool
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_cloud_deploy_pb2.CustomTag]
    target_view_name: str
    view_params: ViewParams
    data_transfer_info: _env_params_pb2_1_1.DataTransferInfo
    leverage_san_transport: bool
    restore_s3_params: _magneto_pb2.RestoreS3Params
    encryption_params: _cloud_deploy_pb2.EncryptionParams
    uda_recover_job_params: _uda_pb2.UdaRecoverJobParams
    restore_target_entity_id: int
    request_sha1_checksum: bytes
    download_chats_params: _magneto_pb2.DownloadChatsParams
    def __init__(self, type: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., restore_job_id: _Optional[int] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., restore_task_vec: _Optional[_Iterable[_Union[PerformRestoreJobStateProto.RestoreTask, _Mapping]]] = ..., continue_restore_on_error: bool = ..., restored_to_different_source: bool = ..., restore_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., restore_acropolis_vms_params: _Optional[_Union[_magneto_pb2.RestoreAcropolisVMsParams, _Mapping]] = ..., restore_kubernetes_namespaces_params: _Optional[_Union[_magneto_pb2.RestoreKubernetesNamespacesParams, _Mapping]] = ..., nosql_connect_params: _Optional[_Union[_magneto_pb2.NoSqlConnectParams, _Mapping]] = ..., nosql_recover_job_params: _Optional[_Union[_nosql_pb2.NoSqlRecoverJobParams, _Mapping]] = ..., view_box_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., admitted_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2_1.RestoreJobStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., cancellation_requested: bool = ..., restore_kvm_vms_params: _Optional[_Union[_magneto_pb2.RestoreKVMVMsParams, _Mapping]] = ..., restore_vmware_vm_params: _Optional[_Union[_vmware_common_pb2.RestoreVMwareVMParams, _Mapping]] = ..., power_state_config: _Optional[_Union[_magneto_pb2.PowerStateConfigProto, _Mapping]] = ..., deploy_vms_to_cloud_task_state: _Optional[_Union[DeployVMsToCloudTaskStateProto, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., rename_restored_object_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[_magneto_pb2.RestoredObjectNetworkConfigProto, _Mapping]] = ..., preserve_tags: bool = ..., restore_task_state_proto_tmpl: _Optional[_Union[PerformRestoreTaskStateProto, _Mapping]] = ..., restore_site_params: _Optional[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]] = ..., restore_public_folders_params: _Optional[_Union[_magneto_pb2.RestoreO365PublicFoldersParams, _Mapping]] = ..., restore_teams_params: _Optional[_Union[_magneto_pb2.RestoreO365TeamsParams, _Mapping]] = ..., restore_groups_params: _Optional[_Union[_magneto_pb2.RestoreO365GroupsParams, _Mapping]] = ..., physical_flr_parallel_restore: bool = ..., vcd_config: _Optional[_Union[RestoredObjectVCDConfigProto, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_magneto_pb2.RestoreObject, _Mapping]]] = ..., rename_restored_vapp_param: _Optional[_Union[_magneto_pb2.RenameObjectParamProto, _Mapping]] = ..., skip_image_deploy: bool = ..., skip_rigel_for_restore: bool = ..., custom_tag_vec: _Optional[_Iterable[_Union[_cloud_deploy_pb2.CustomTag, _Mapping]]] = ..., target_view_name: _Optional[str] = ..., view_params: _Optional[_Union[ViewParams, _Mapping]] = ..., data_transfer_info: _Optional[_Union[_env_params_pb2_1_1.DataTransferInfo, _Mapping]] = ..., leverage_san_transport: bool = ..., restore_s3_params: _Optional[_Union[_magneto_pb2.RestoreS3Params, _Mapping]] = ..., encryption_params: _Optional[_Union[_cloud_deploy_pb2.EncryptionParams, _Mapping]] = ..., uda_recover_job_params: _Optional[_Union[_uda_pb2.UdaRecoverJobParams, _Mapping]] = ..., restore_target_entity_id: _Optional[int] = ..., request_sha1_checksum: _Optional[bytes] = ..., download_chats_params: _Optional[_Union[_magneto_pb2.DownloadChatsParams, _Mapping]] = ...) -> None: ...

class RestoreFilesTaskStateProto(_message.Message):
    __slots__ = ("restore_params", "restore_files_info")
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_params: _magneto_pb2.RestoreFilesParams
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    def __init__(self, restore_params: _Optional[_Union[_magneto_pb2.RestoreFilesParams, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ...) -> None: ...

class RestoreStandbyTaskStateProto(_message.Message):
    __slots__ = ("standby_restore_complete",)
    STANDBY_RESTORE_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    standby_restore_complete: bool
    def __init__(self, standby_restore_complete: bool = ...) -> None: ...

class MountVolumesTaskStateProto(_message.Message):
    __slots__ = ("mount_params", "mount_info", "host_entity", "full_nas_path")
    MOUNT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FULL_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    mount_params: _magneto_pb2.MountVolumesParams
    mount_info: _magneto_pb2.MountVolumesInfoProto
    host_entity: _entity_pb2.EntityProto
    full_nas_path: str
    def __init__(self, mount_params: _Optional[_Union[_magneto_pb2.MountVolumesParams, _Mapping]] = ..., mount_info: _Optional[_Union[_magneto_pb2.MountVolumesInfoProto, _Mapping]] = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., full_nas_path: _Optional[str] = ...) -> None: ...

class RecoverVolumesTaskStateProto(_message.Message):
    __slots__ = ("params", "task_result_vec")
    class TaskResult(_message.Message):
        __slots__ = ("dst_guid", "progress_monitor_task_path", "error")
        DST_GUID_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        dst_guid: str
        progress_monitor_task_path: str
        error: _error_pb2_1.ErrorProto
        def __init__(self, dst_guid: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TASK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    params: _magneto_pb2.RecoverVolumesParams
    task_result_vec: _containers.RepeatedCompositeFieldContainer[RecoverVolumesTaskStateProto.TaskResult]
    def __init__(self, params: _Optional[_Union[_magneto_pb2.RecoverVolumesParams, _Mapping]] = ..., task_result_vec: _Optional[_Iterable[_Union[RecoverVolumesTaskStateProto.TaskResult, _Mapping]]] = ...) -> None: ...

class RecoverDisksTaskStateProto(_message.Message):
    __slots__ = ("recover_virtual_disk_params", "recover_virtual_disk_info")
    RECOVER_VIRTUAL_DISK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIRTUAL_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    recover_virtual_disk_params: _magneto_pb2.RecoverVirtualDiskParams
    recover_virtual_disk_info: _magneto_pb2.RecoverVirtualDiskInfoProto
    def __init__(self, recover_virtual_disk_params: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskParams, _Mapping]] = ..., recover_virtual_disk_info: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskInfoProto, _Mapping]] = ...) -> None: ...

class DeployVMsToCloudTaskStateProto(_message.Message):
    __slots__ = ("deploy_vms_to_cloud_params",)
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    def __init__(self, deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ...) -> None: ...

class MultiStageRestoreTaskStateProto(_message.Message):
    __slots__ = ("multi_stage_restore_options", "sync_time_usecs", "sync_size_bytes")
    MULTI_STAGE_RESTORE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SYNC_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SYNC_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    multi_stage_restore_options: _magneto_pb2.UpdateRestoreTaskOptions
    sync_time_usecs: int
    sync_size_bytes: int
    def __init__(self, multi_stage_restore_options: _Optional[_Union[_magneto_pb2.UpdateRestoreTaskOptions, _Mapping]] = ..., sync_time_usecs: _Optional[int] = ..., sync_size_bytes: _Optional[int] = ...) -> None: ...

class RestoreAppTaskStateProto(_message.Message):
    __slots__ = ("restore_app_params", "last_finished_log_backup_start_time_usecs", "app_restore_progress_monitor_subtask_path", "child_restore_app_params_vec")
    RESTORE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LAST_FINISHED_LOG_BACKUP_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    APP_RESTORE_PROGRESS_MONITOR_SUBTASK_PATH_FIELD_NUMBER: _ClassVar[int]
    CHILD_RESTORE_APP_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_app_params: _magneto_pb2.RestoreAppParams
    last_finished_log_backup_start_time_usecs: int
    app_restore_progress_monitor_subtask_path: str
    child_restore_app_params_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreAppParams]
    def __init__(self, restore_app_params: _Optional[_Union[_magneto_pb2.RestoreAppParams, _Mapping]] = ..., last_finished_log_backup_start_time_usecs: _Optional[int] = ..., app_restore_progress_monitor_subtask_path: _Optional[str] = ..., child_restore_app_params_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreAppParams, _Mapping]]] = ...) -> None: ...

class DestroyClonedTaskStateProto(_message.Message):
    __slots__ = ("task_id", "perform_clone_task_id", "parent_task_id", "type", "restore_type", "user", "clone_task_name", "status", "error", "force_delete", "parent_source_connection_params", "full_view_name", "view_box_id", "start_time_usecs", "end_time_usecs", "scheduled_constituent_id", "scheduled_gandalf_session_id", "user_info", "destroy_clone_vm_task_info", "datastore_entity", "folder_entity", "destroy_mount_volumes_task_info", "destroy_clone_app_task_info", "deploy_vms_to_cloud_task_state", "vcd_config", "action_executor_target_type", "view_name_DEPRECATED")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CLONE_TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FULL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_VM_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DESTROY_MOUNT_VOLUMES_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    perform_clone_task_id: int
    parent_task_id: int
    type: _enums_pb2.Environment.Type
    restore_type: _magneto_pb2.RestoreType.Type
    user: str
    clone_task_name: str
    status: _enums_pb2_1.DestroyClonedTaskStatus.Type
    error: _error_pb2_1.ErrorProto
    force_delete: bool
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    full_view_name: str
    view_box_id: int
    start_time_usecs: int
    end_time_usecs: int
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    user_info: _permissions_pb2.UserInformation
    destroy_clone_vm_task_info: _magneto_pb2.DestroyClonedVMTaskInfoProto
    datastore_entity: _entity_pb2.EntityProto
    folder_entity: _entity_pb2.EntityProto
    destroy_mount_volumes_task_info: _magneto_pb2.DestroyMountVolumesTaskInfoProto
    destroy_clone_app_task_info: _magneto_pb2.DestroyCloneAppTaskInfoProto
    deploy_vms_to_cloud_task_state: DeployVMsToCloudTaskStateProto
    vcd_config: RestoredObjectVCDConfigProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    view_name_DEPRECATED: str
    def __init__(self, task_id: _Optional[int] = ..., perform_clone_task_id: _Optional[int] = ..., parent_task_id: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_type: _Optional[_Union[_magneto_pb2.RestoreType.Type, str]] = ..., user: _Optional[str] = ..., clone_task_name: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2_1.DestroyClonedTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., force_delete: bool = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., full_view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., destroy_clone_vm_task_info: _Optional[_Union[_magneto_pb2.DestroyClonedVMTaskInfoProto, _Mapping]] = ..., datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., folder_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., destroy_mount_volumes_task_info: _Optional[_Union[_magneto_pb2.DestroyMountVolumesTaskInfoProto, _Mapping]] = ..., destroy_clone_app_task_info: _Optional[_Union[_magneto_pb2.DestroyCloneAppTaskInfoProto, _Mapping]] = ..., deploy_vms_to_cloud_task_state: _Optional[_Union[DeployVMsToCloudTaskStateProto, _Mapping]] = ..., vcd_config: _Optional[_Union[RestoredObjectVCDConfigProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., view_name_DEPRECATED: _Optional[str] = ...) -> None: ...

class RestoreWrapperProto(_message.Message):
    __slots__ = ("perform_restore_task_state", "perform_refresh_task_state_vec", "perform_restore_job_state", "destroy_cloned_task_state_vec", "owner_restore_wrapper_proto", "restore_sub_task_wrapper_proto_vec")
    PERFORM_RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_REFRESH_TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    PERFORM_RESTORE_JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONED_TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNER_RESTORE_WRAPPER_PROTO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SUB_TASK_WRAPPER_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    perform_restore_task_state: PerformRestoreTaskStateProto
    perform_refresh_task_state_vec: _containers.RepeatedCompositeFieldContainer[PerformRestoreTaskStateProto]
    perform_restore_job_state: PerformRestoreJobStateProto
    destroy_cloned_task_state_vec: _containers.RepeatedCompositeFieldContainer[DestroyClonedTaskStateProto]
    owner_restore_wrapper_proto: RestoreWrapperProto
    restore_sub_task_wrapper_proto_vec: _containers.RepeatedCompositeFieldContainer[RestoreWrapperProto]
    def __init__(self, perform_restore_task_state: _Optional[_Union[PerformRestoreTaskStateProto, _Mapping]] = ..., perform_refresh_task_state_vec: _Optional[_Iterable[_Union[PerformRestoreTaskStateProto, _Mapping]]] = ..., perform_restore_job_state: _Optional[_Union[PerformRestoreJobStateProto, _Mapping]] = ..., destroy_cloned_task_state_vec: _Optional[_Iterable[_Union[DestroyClonedTaskStateProto, _Mapping]]] = ..., owner_restore_wrapper_proto: _Optional[_Union[RestoreWrapperProto, _Mapping]] = ..., restore_sub_task_wrapper_proto_vec: _Optional[_Iterable[_Union[RestoreWrapperProto, _Mapping]]] = ...) -> None: ...

class RestoreArchiveMDProto(_message.Message):
    __slots__ = ("restore_wrapper_proto",)
    RESTORE_WRAPPER_PROTO_FIELD_NUMBER: _ClassVar[int]
    restore_wrapper_proto: RestoreWrapperProto
    def __init__(self, restore_wrapper_proto: _Optional[_Union[RestoreWrapperProto, _Mapping]] = ...) -> None: ...

class GetRestoreTasksArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "restore_type_vec", "limit_num_finished_tasks", "pagination_cookie", "time_range", "task_id", "sid_vec", "user_info", "env_type_vec", "storage_domain_id", "return_child_tasks")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_FINISHED_TASKS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_CHILD_TASKS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    restore_type_vec: _containers.RepeatedScalarFieldContainer[_magneto_pb2.RestoreType.Type]
    limit_num_finished_tasks: int
    pagination_cookie: bytes
    time_range: TimeRange
    task_id: int
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    env_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    storage_domain_id: int
    return_child_tasks: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., restore_type_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreType.Type, str]]] = ..., limit_num_finished_tasks: _Optional[int] = ..., pagination_cookie: _Optional[bytes] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., task_id: _Optional[int] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., env_type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., storage_domain_id: _Optional[int] = ..., return_child_tasks: bool = ...) -> None: ...

class GetRestoreTasksResult(_message.Message):
    __slots__ = ("error", "active_restore_tasks", "finished_restore_tasks", "pagination_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_RESTORE_TASKS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_RESTORE_TASKS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    active_restore_tasks: _containers.RepeatedCompositeFieldContainer[RestoreWrapperProto]
    finished_restore_tasks: _containers.RepeatedCompositeFieldContainer[RestoreWrapperProto]
    pagination_cookie: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., active_restore_tasks: _Optional[_Iterable[_Union[RestoreWrapperProto, _Mapping]]] = ..., finished_restore_tasks: _Optional[_Iterable[_Union[RestoreWrapperProto, _Mapping]]] = ..., pagination_cookie: _Optional[bytes] = ...) -> None: ...

class DestroyCloneTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "clone_task_id", "user", "target_entity_credentials", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    clone_task_id: int
    user: str
    target_entity_credentials: _credentials_pb2.Credentials
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., clone_task_id: _Optional[int] = ..., user: _Optional[str] = ..., target_entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class DestroyCloneTaskResult(_message.Message):
    __slots__ = ("error", "destroy_clone_task_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    destroy_clone_task_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., destroy_clone_task_id: _Optional[int] = ...) -> None: ...

class GetRestoreViewsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ...) -> None: ...

class GetRestoreViewsResult(_message.Message):
    __slots__ = ("error", "view_infos", "retrieve_archive_view_infos")
    class ViewInfo(_message.Message):
        __slots__ = ("name", "view_box_id", "restore_task_names")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_TASK_NAMES_FIELD_NUMBER: _ClassVar[int]
        name: str
        view_box_id: int
        restore_task_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., restore_task_names: _Optional[_Iterable[str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFOS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_VIEW_INFOS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    view_infos: _containers.RepeatedCompositeFieldContainer[GetRestoreViewsResult.ViewInfo]
    retrieve_archive_view_infos: _containers.RepeatedCompositeFieldContainer[GetRestoreViewsResult.ViewInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., view_infos: _Optional[_Iterable[_Union[GetRestoreViewsResult.ViewInfo, _Mapping]]] = ..., retrieve_archive_view_infos: _Optional[_Iterable[_Union[GetRestoreViewsResult.ViewInfo, _Mapping]]] = ...) -> None: ...

class GetJobAuditTrailArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ...) -> None: ...

class GetJobAuditTrailResult(_message.Message):
    __slots__ = ("error", "audit_trail")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TRAIL_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    audit_trail: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupJobProto]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., audit_trail: _Optional[_Iterable[_Union[_magneto_pb2.BackupJobProto, _Mapping]]] = ...) -> None: ...

class CreateRestoreFilesTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "name", "user", "restore_vlan_params", "source_object_info", "params", "user_info", "parent_task_uid")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    name: str
    user: str
    restore_vlan_params: _common_pb2.VlanParams
    source_object_info: _magneto_pb2.RestoreObject
    params: _magneto_pb2.RestoreFilesParams
    user_info: _permissions_pb2.UserInformation
    parent_task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., restore_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., source_object_info: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ..., params: _Optional[_Union[_magneto_pb2.RestoreFilesParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., parent_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CreateRestoreFilesTaskResult(_message.Message):
    __slots__ = ("error", "task_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    task_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class CreateDownloadFilesTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "name", "user", "source_object_info", "params", "user_info", "parent_task_uid")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    name: str
    user: str
    source_object_info: _magneto_pb2.RestoreObject
    params: _magneto_pb2.RestoreFilesParams
    user_info: _permissions_pb2.UserInformation
    parent_task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., source_object_info: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ..., params: _Optional[_Union[_magneto_pb2.RestoreFilesParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., parent_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CreateDownloadFilesTaskResult(_message.Message):
    __slots__ = ("error", "task_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    task_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class RetrieveArchiveInfo(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "logical_size_bytes", "logical_bytes_transferred", "avg_logical_transfer_rate_bps", "bytes_transferred", "target_view_name", "stub_view_name", "stub_view_relative_dir_name", "skip_cloning_view", "error", "user_action_required_msg", "retrieved_entity_vec", "progress_monitor_task_path")
    class RetrievedEntity(_message.Message):
        __slots__ = ("entity", "start_timestamp_usecs", "end_timestamp_usecs", "status", "error", "relative_snapshot_dir", "logical_size_bytes", "logical_bytes_transferred", "bytes_transferred", "progress_monitor_task_path", "uptier_expiry_timestamp_usecs")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCreated: _ClassVar[RetrieveArchiveInfo.RetrievedEntity.Status]
            kRunning: _ClassVar[RetrieveArchiveInfo.RetrievedEntity.Status]
            kFinished: _ClassVar[RetrieveArchiveInfo.RetrievedEntity.Status]
            kCancelled: _ClassVar[RetrieveArchiveInfo.RetrievedEntity.Status]
        kCreated: RetrieveArchiveInfo.RetrievedEntity.Status
        kRunning: RetrieveArchiveInfo.RetrievedEntity.Status
        kFinished: RetrieveArchiveInfo.RetrievedEntity.Status
        kCancelled: RetrieveArchiveInfo.RetrievedEntity.Status
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        UPTIER_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        start_timestamp_usecs: int
        end_timestamp_usecs: int
        status: RetrieveArchiveInfo.RetrievedEntity.Status
        error: _error_pb2_1.ErrorProto
        relative_snapshot_dir: str
        logical_size_bytes: int
        logical_bytes_transferred: int
        bytes_transferred: int
        progress_monitor_task_path: str
        uptier_expiry_timestamp_usecs: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., status: _Optional[_Union[RetrieveArchiveInfo.RetrievedEntity.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., relative_snapshot_dir: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., uptier_expiry_timestamp_usecs: _Optional[int] = ...) -> None: ...
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_RELATIVE_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONING_VIEW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_ACTION_REQUIRED_MSG_FIELD_NUMBER: _ClassVar[int]
    RETRIEVED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    logical_size_bytes: int
    logical_bytes_transferred: int
    avg_logical_transfer_rate_bps: int
    bytes_transferred: int
    target_view_name: str
    stub_view_name: str
    stub_view_relative_dir_name: str
    skip_cloning_view: bool
    error: _error_pb2_1.ErrorProto
    user_action_required_msg: str
    retrieved_entity_vec: _containers.RepeatedCompositeFieldContainer[RetrieveArchiveInfo.RetrievedEntity]
    progress_monitor_task_path: str
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., target_view_name: _Optional[str] = ..., stub_view_name: _Optional[str] = ..., stub_view_relative_dir_name: _Optional[str] = ..., skip_cloning_view: bool = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_action_required_msg: _Optional[str] = ..., retrieved_entity_vec: _Optional[_Iterable[_Union[RetrieveArchiveInfo.RetrievedEntity, _Mapping]]] = ..., progress_monitor_task_path: _Optional[str] = ...) -> None: ...

class RetrieveArchiveTaskStateProto(_message.Message):
    __slots__ = ("task_uid", "name", "user", "job_uid", "archive_task_uid", "archival_target", "backup_run_start_time_usecs", "restore_task_id", "entity_vec", "download_files_info", "restore_archive_files_info", "view_box_id", "progress_monitor_task_path", "status", "error", "start_time_usecs", "end_time_usecs", "cancellation_requested", "retrieval_info", "vault_restore_params", "is_uptier_restore_job", "glacier_flr_restore_option", "view_name_DEPRECATED", "full_view_name_DEPRECATED")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RetrieveArchiveTaskStateProto.Status]
        kScheduled: _ClassVar[RetrieveArchiveTaskStateProto.Status]
        kFinished: _ClassVar[RetrieveArchiveTaskStateProto.Status]
        kCancelled: _ClassVar[RetrieveArchiveTaskStateProto.Status]
    kStarted: RetrieveArchiveTaskStateProto.Status
    kScheduled: RetrieveArchiveTaskStateProto.Status
    kFinished: RetrieveArchiveTaskStateProto.Status
    kCancelled: RetrieveArchiveTaskStateProto.Status
    class DownloadFilesInfo(_message.Message):
        __slots__ = ("target_view_name", "target_dir_path", "object_id", "magneto_instance_id", "file_path_vec", "skip_restore_in_stub_view")
        TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        TARGET_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        SKIP_RESTORE_IN_STUB_VIEW_FIELD_NUMBER: _ClassVar[int]
        target_view_name: str
        target_dir_path: str
        object_id: _magneto_pb2.MagnetoObjectId
        magneto_instance_id: _yoda_types_pb2.MagnetoInstanceId
        file_path_vec: _containers.RepeatedScalarFieldContainer[str]
        skip_restore_in_stub_view: bool
        def __init__(self, target_view_name: _Optional[str] = ..., target_dir_path: _Optional[str] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., magneto_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., file_path_vec: _Optional[_Iterable[str]] = ..., skip_restore_in_stub_view: bool = ...) -> None: ...
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARCHIVE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    VAULT_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_UPTIER_RESTORE_JOB_FIELD_NUMBER: _ClassVar[int]
    GLACIER_FLR_RESTORE_OPTION_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FULL_VIEW_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    name: str
    user: str
    job_uid: _universal_id_pb2.UniversalIdProto
    archive_task_uid: _universal_id_pb2.UniversalIdProto
    archival_target: _policy_pb2.ArchivalTarget
    backup_run_start_time_usecs: int
    restore_task_id: int
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    download_files_info: RetrieveArchiveTaskStateProto.DownloadFilesInfo
    restore_archive_files_info: RetrieveArchiveTaskStateProto.DownloadFilesInfo
    view_box_id: int
    progress_monitor_task_path: str
    status: RetrieveArchiveTaskStateProto.Status
    error: _error_pb2_1.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    cancellation_requested: bool
    retrieval_info: RetrieveArchiveInfo
    vault_restore_params: _vault_pb2.VaultParams.RestoreParams
    is_uptier_restore_job: bool
    glacier_flr_restore_option: _magneto_pb2.RestoreFilesParams.GlacierFLRRestoreOption
    view_name_DEPRECATED: str
    full_view_name_DEPRECATED: str
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., user: _Optional[str] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archive_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archival_target: _Optional[_Union[_policy_pb2.ArchivalTarget, _Mapping]] = ..., backup_run_start_time_usecs: _Optional[int] = ..., restore_task_id: _Optional[int] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., download_files_info: _Optional[_Union[RetrieveArchiveTaskStateProto.DownloadFilesInfo, _Mapping]] = ..., restore_archive_files_info: _Optional[_Union[RetrieveArchiveTaskStateProto.DownloadFilesInfo, _Mapping]] = ..., view_box_id: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., status: _Optional[_Union[RetrieveArchiveTaskStateProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., cancellation_requested: bool = ..., retrieval_info: _Optional[_Union[RetrieveArchiveInfo, _Mapping]] = ..., vault_restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ..., is_uptier_restore_job: bool = ..., glacier_flr_restore_option: _Optional[_Union[_magneto_pb2.RestoreFilesParams.GlacierFLRRestoreOption, str]] = ..., view_name_DEPRECATED: _Optional[str] = ..., full_view_name_DEPRECATED: _Optional[str] = ...) -> None: ...

class BackupRunReplicationMDProto(_message.Message):
    __slots__ = ("job_description", "object_level_copy", "backup_run_state", "backup_task_state", "snapshot_expiry_usecs", "rx_view_box_id", "fs", "api_version", "parent_task_id", "rx_cluster_instance_id", "is_final_request", "replicate_failed_backup_tasks_DEPRECATED")
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    RX_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    FS_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_FAILED_BACKUP_TASKS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    job_description: _magneto_pb2.BackupJobProto
    object_level_copy: bool
    backup_run_state: BackupJobRunStateProto
    backup_task_state: BackupTaskStateProto
    snapshot_expiry_usecs: int
    rx_view_box_id: int
    fs: str
    api_version: _api_version_pb2.APIVersion
    parent_task_id: _universal_id_pb2.UniversalIdProto
    rx_cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    is_final_request: bool
    replicate_failed_backup_tasks_DEPRECATED: bool
    def __init__(self, job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., object_level_copy: bool = ..., backup_run_state: _Optional[_Union[BackupJobRunStateProto, _Mapping]] = ..., backup_task_state: _Optional[_Union[BackupTaskStateProto, _Mapping]] = ..., snapshot_expiry_usecs: _Optional[int] = ..., rx_view_box_id: _Optional[int] = ..., fs: _Optional[str] = ..., api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., parent_task_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., is_final_request: bool = ..., replicate_failed_backup_tasks_DEPRECATED: bool = ...) -> None: ...

class ReplicationInfoBase(_message.Message):
    __slots__ = ("error", "remote_cluster_name", "start_time_usecs", "end_time_usecs", "view_name", "logical_size_bytes", "pct_completed", "logical_bytes_transferred", "bytes_transferred", "rx_cluster_incarnation_id", "filtered_backup_task_id_map", "existing_expiry_time_usecs", "existing_data_lock_constraints", "existing_worm_retention_on_rx", "is_target_datalock_capable", "metadata_actions_completed", "blackout_remaining_time_usecs", "estimated_logical_bytes_to_transfer", "is_full_replication", "enable_nfs_smb_permissions")
    class FilteredBackupTaskIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERED_BACKUP_TASK_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    EXISTING_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXISTING_DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    EXISTING_WORM_RETENTION_ON_RX_FIELD_NUMBER: _ClassVar[int]
    IS_TARGET_DATALOCK_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    BLACKOUT_REMAINING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NFS_SMB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    remote_cluster_name: str
    start_time_usecs: int
    end_time_usecs: int
    view_name: str
    logical_size_bytes: int
    pct_completed: int
    logical_bytes_transferred: int
    bytes_transferred: int
    rx_cluster_incarnation_id: int
    filtered_backup_task_id_map: _containers.ScalarMap[int, bool]
    existing_expiry_time_usecs: int
    existing_data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    existing_worm_retention_on_rx: _worm_pb2.WormRetentionProto
    is_target_datalock_capable: bool
    metadata_actions_completed: int
    blackout_remaining_time_usecs: int
    estimated_logical_bytes_to_transfer: int
    is_full_replication: bool
    enable_nfs_smb_permissions: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., remote_cluster_name: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., view_name: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., filtered_backup_task_id_map: _Optional[_Mapping[int, bool]] = ..., existing_expiry_time_usecs: _Optional[int] = ..., existing_data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., existing_worm_retention_on_rx: _Optional[_Union[_worm_pb2.WormRetentionProto, _Mapping]] = ..., is_target_datalock_capable: bool = ..., metadata_actions_completed: _Optional[int] = ..., blackout_remaining_time_usecs: _Optional[int] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., is_full_replication: bool = ..., enable_nfs_smb_permissions: bool = ...) -> None: ...

class LocalCopyInfoBase(_message.Message):
    __slots__ = ("yoda_notified_task_ids", "yoda_object_level_notify_enabled")
    class YodaNotifiedTaskIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    YODA_NOTIFIED_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    YODA_OBJECT_LEVEL_NOTIFY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    yoda_notified_task_ids: _containers.ScalarMap[int, bool]
    yoda_object_level_notify_enabled: bool
    def __init__(self, yoda_notified_task_ids: _Optional[_Mapping[int, bool]] = ..., yoda_object_level_notify_enabled: bool = ...) -> None: ...

class BackupRunArchiveMDProto(_message.Message):
    __slots__ = ("job_description", "backup_run_state", "capability_proto", "opaque_metadata", "backup_run_details")
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    job_description: _magneto_pb2.BackupJobProto
    backup_run_state: BackupJobRunStateProto
    capability_proto: _capability_pb2.CapabilityProto
    opaque_metadata: bytes
    backup_run_details: BackupRunArchivePropertyProto
    def __init__(self, job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., backup_run_state: _Optional[_Union[BackupJobRunStateProto, _Mapping]] = ..., capability_proto: _Optional[_Union[_capability_pb2.CapabilityProto, _Mapping]] = ..., opaque_metadata: _Optional[bytes] = ..., backup_run_details: _Optional[_Union[BackupRunArchivePropertyProto, _Mapping]] = ...) -> None: ...

class BackupRunArchivePropertyProto(_message.Message):
    __slots__ = ("env_type", "user_info", "is_indexing_enabled", "entity_archival_info")
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_INDEXING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ARCHIVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    user_info: _permissions_pb2.UserInformation
    is_indexing_enabled: bool
    entity_archival_info: _containers.RepeatedCompositeFieldContainer[EntityArchivalInfo]
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., is_indexing_enabled: bool = ..., entity_archival_info: _Optional[_Iterable[_Union[EntityArchivalInfo, _Mapping]]] = ...) -> None: ...

class EntityArchivalInfo(_message.Message):
    __slots__ = ("name", "aliases")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    name: str
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class ArchivalInfoBase(_message.Message):
    __slots__ = ("error", "start_time_usecs", "end_time_usecs", "logical_size_bytes", "logical_bytes_transferred", "avg_logical_transfer_rate_bps", "bytes_transferred", "user_action_required_msg", "progress_monitor_task_path", "is_incremental_archive", "original_task_uid", "is_cloud_domain_archive", "archive_worm_properties", "is_cad_archive", "entity_string_id_to_front_end_size_info_map")
    class EntityStringIdToFrontEndSizeInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _stats_pb2.SizeInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    USER_ACTION_REQUIRED_MSG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_DOMAIN_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STRING_ID_TO_FRONT_END_SIZE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    logical_size_bytes: int
    logical_bytes_transferred: int
    avg_logical_transfer_rate_bps: int
    bytes_transferred: int
    user_action_required_msg: str
    progress_monitor_task_path: str
    is_incremental_archive: bool
    original_task_uid: _universal_id_pb2.UniversalIdProto
    is_cloud_domain_archive: bool
    archive_worm_properties: _worm_pb2.ArchiveWORMProperties
    is_cad_archive: bool
    entity_string_id_to_front_end_size_info_map: _containers.MessageMap[str, _stats_pb2.SizeInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., user_action_required_msg: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., is_incremental_archive: bool = ..., original_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_cloud_domain_archive: bool = ..., archive_worm_properties: _Optional[_Union[_worm_pb2.ArchiveWORMProperties, _Mapping]] = ..., is_cad_archive: bool = ..., entity_string_id_to_front_end_size_info_map: _Optional[_Mapping[str, _stats_pb2.SizeInfo]] = ...) -> None: ...

class DeactivateJobStateProto(_message.Message):
    __slots__ = ("task_id", "job_uid", "user", "deactivate_entities", "status", "error", "parent_source_connection_params", "start_time_usecs", "end_time_usecs", "deactivate_info", "scheduled_constituent_id", "scheduled_gandalf_session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    user: str
    deactivate_entities: bool
    status: _enums_pb2_1.DeactivateJobStatus.Type
    error: _error_pb2_1.ErrorProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    start_time_usecs: int
    end_time_usecs: int
    deactivate_info: _magneto_pb2.DeactivateJobEntitiesInfoProto
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., user: _Optional[str] = ..., deactivate_entities: bool = ..., status: _Optional[_Union[_enums_pb2_1.DeactivateJobStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., deactivate_info: _Optional[_Union[_magneto_pb2.DeactivateJobEntitiesInfoProto, _Mapping]] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ...) -> None: ...

class ChangeBackupJobModeProto(_message.Message):
    __slots__ = ("deactivate_job_state",)
    DEACTIVATE_JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    deactivate_job_state: DeactivateJobStateProto
    def __init__(self, deactivate_job_state: _Optional[_Union[DeactivateJobStateProto, _Mapping]] = ...) -> None: ...

class UpdateBackupRunTaskProto(_message.Message):
    __slots__ = ("task_id", "job_uid", "run_start_time_usecs", "updated_expiry_time_usecs", "status")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    updated_expiry_time_usecs: int
    status: _enums_pb2_1.UpdateBackupRunTaskStatus.Type
    def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., updated_expiry_time_usecs: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2_1.UpdateBackupRunTaskStatus.Type, str]] = ...) -> None: ...

class ViewParams(_message.Message):
    __slots__ = ("view_description", "storage_policy_override", "qos_mapping_vec", "disable_nfs_access", "client_subnet_whitelist_vec", "worm_lock_expiry_usecs", "protocol_access_info")
    VIEW_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_VEC_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    view_description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos_mapping_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    disable_nfs_access: bool
    client_subnet_whitelist_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    worm_lock_expiry_usecs: int
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    def __init__(self, view_description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos_mapping_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ..., disable_nfs_access: bool = ..., client_subnet_whitelist_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., worm_lock_expiry_usecs: _Optional[int] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ...) -> None: ...

class EntityRegistrationInfoProto(_message.Message):
    __slots__ = ("app_env_vec", "entity", "entity_credentials", "app_credentials_vec", "agent_info", "analyze_appstatus_from_time_offset_sec", "analyze_appstatus_to_time_offset_sec")
    APP_ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_APPSTATUS_FROM_TIME_OFFSET_SEC_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_APPSTATUS_TO_TIME_OFFSET_SEC_FIELD_NUMBER: _ClassVar[int]
    app_env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    entity: _entity_pb2.EntityProto
    entity_credentials: _credentials_pb2.Credentials
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.AppCredentials]
    agent_info: _agent_pb2.AgentInfoProto
    analyze_appstatus_from_time_offset_sec: int
    analyze_appstatus_to_time_offset_sec: int
    def __init__(self, app_env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.AppCredentials, _Mapping]]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., analyze_appstatus_from_time_offset_sec: _Optional[int] = ..., analyze_appstatus_to_time_offset_sec: _Optional[int] = ...) -> None: ...

class VerifyEntityRegistrationTaskStateProto(_message.Message):
    __slots__ = ("task_id", "registration_info", "scheduled_constituent_id", "scheduled_gandalf_session_id", "status", "error", "start_time_usecs", "end_time_usecs", "verification_info_proto", "is_refresh", "user_info")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    registration_info: EntityRegistrationInfoProto
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    status: _enums_pb2.VerificationStatus.Type
    error: _error_pb2_1.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    verification_info_proto: _magneto_pb2.VerificationInfoProto
    is_refresh: bool
    user_info: _permissions_pb2.UserInformation
    def __init__(self, task_id: _Optional[int] = ..., registration_info: _Optional[_Union[EntityRegistrationInfoProto, _Mapping]] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2.VerificationStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., verification_info_proto: _Optional[_Union[_magneto_pb2.VerificationInfoProto, _Mapping]] = ..., is_refresh: bool = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class ConversionParams(_message.Message):
    __slots__ = ("view_box_id", "entity", "backup_snapshot_info", "backup_view_name", "view_name", "restore_entity", "restore_parent_entity", "convert_dir", "job_uid", "run_start_time_usecs")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONVERT_DIR_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    entity: _entity_pb2.EntityProto
    backup_snapshot_info: _magneto_pb2.SnapshotInfoProto
    backup_view_name: str
    view_name: str
    restore_entity: _magneto_pb2.RestoreInfoProto.RestoreEntity
    restore_parent_entity: _entity_pb2.EntityProto
    convert_dir: str
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    def __init__(self, view_box_id: _Optional[int] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., backup_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., backup_view_name: _Optional[str] = ..., view_name: _Optional[str] = ..., restore_entity: _Optional[_Union[_magneto_pb2.RestoreInfoProto.RestoreEntity, _Mapping]] = ..., restore_parent_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., convert_dir: _Optional[str] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...

class ConversionTaskStateProto(_message.Message):
    __slots__ = ("task_id", "conversion_params", "scheduled_constituent_id", "scheduled_gandalf_session_id", "status", "error", "start_time_usecs", "end_time_usecs", "conversion_info_proto", "action_executor_target_type")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    conversion_params: ConversionParams
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    status: _enums_pb2.ConversionStatus.Type
    error: _error_pb2_1.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    conversion_info_proto: _magneto_pb2.ConversionInfoProto
    action_executor_target_type: _enums_pb2.TargetType.Type
    def __init__(self, task_id: _Optional[int] = ..., conversion_params: _Optional[_Union[ConversionParams, _Mapping]] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2.ConversionStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., conversion_info_proto: _Optional[_Union[_magneto_pb2.ConversionInfoProto, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ...) -> None: ...

class ConversionCleanupTaskStateProto(_message.Message):
    __slots__ = ("task_id", "conversion_task_id", "status", "error", "start_time_usecs", "end_time_usecs")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    conversion_task_id: int
    status: _enums_pb2.ConversionCleanupStatus.Type
    error: _error_pb2_1.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, task_id: _Optional[int] = ..., conversion_task_id: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2.ConversionCleanupStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class CloudDeployTaskStateProto(_message.Message):
    __slots__ = ("task_id", "scheduled_constituent_id", "scheduled_gandalf_session_id", "cloud_deploy_info")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    def __init__(self, task_id: _Optional[int] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ...) -> None: ...

class OnPremDeployTaskStateProto(_message.Message):
    __slots__ = ("task_id", "scheduled_constituent_id", "scheduled_gandalf_session_id", "restore_info")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    restore_info: _magneto_pb2.RestoreInfoProto
    def __init__(self, task_id: _Optional[int] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ...) -> None: ...

class UpgradeAgentArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "agent_entity_vec", "installer_locations_vec")
    class InstallerLocation(_message.Message):
        __slots__ = ("host_type", "uri", "linux_pkg_type", "agent_type")
        HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        LINUX_PKG_TYPE_FIELD_NUMBER: _ClassVar[int]
        AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        host_type: _enums_pb2.HostEnv.Type
        uri: str
        linux_pkg_type: _agent_pb2.AgentInfoProto.LinuxAgentPackageType
        agent_type: _agent_pb2.AgentInfoProto.AgentType
        def __init__(self, host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., uri: _Optional[str] = ..., linux_pkg_type: _Optional[_Union[_agent_pb2.AgentInfoProto.LinuxAgentPackageType, str]] = ..., agent_type: _Optional[_Union[_agent_pb2.AgentInfoProto.AgentType, str]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_LOCATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    agent_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    installer_locations_vec: _containers.RepeatedCompositeFieldContainer[UpgradeAgentArg.InstallerLocation]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., agent_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., installer_locations_vec: _Optional[_Iterable[_Union[UpgradeAgentArg.InstallerLocation, _Mapping]]] = ...) -> None: ...

class UpgradeAgentResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateCDPComponentsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "op_type", "entity_vec")
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpgrade: _ClassVar[UpdateCDPComponentsArg.OpType]
        kUninstall: _ClassVar[UpdateCDPComponentsArg.OpType]
    kUpgrade: UpdateCDPComponentsArg.OpType
    kUninstall: UpdateCDPComponentsArg.OpType
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    op_type: UpdateCDPComponentsArg.OpType
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., op_type: _Optional[_Union[UpdateCDPComponentsArg.OpType, str]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class UpdateCDPComponentsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateUpgradeTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "task_description")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    task_description: _magneto_pb2.UpgradeTaskStateProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., task_description: _Optional[_Union[_magneto_pb2.UpgradeTaskStateProto, _Mapping]] = ...) -> None: ...

class CreateUpgradeTaskResult(_message.Message):
    __slots__ = ("error", "task_description")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    task_description: _magneto_pb2.UpgradeTaskStateProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., task_description: _Optional[_Union[_magneto_pb2.UpgradeTaskStateProto, _Mapping]] = ...) -> None: ...

class GetUpgradeTaskStatusArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "upgrade_task_ids_vec", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_TASK_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    upgrade_task_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., upgrade_task_ids_vec: _Optional[_Iterable[int]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class GetUpgradeTaskStatusResult(_message.Message):
    __slots__ = ("error", "upgrade_tasks_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    upgrade_tasks_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.UpgradeTaskStateProto]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., upgrade_tasks_vec: _Optional[_Iterable[_Union[_magneto_pb2.UpgradeTaskStateProto, _Mapping]]] = ...) -> None: ...

class CancelUpgradeTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "id", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    id: int
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., id: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class CancelUpgradeTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetPermissionInfoForEntitiesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetPermissionInfoForEntitiesResult(_message.Message):
    __slots__ = ("error", "entity_permission_info_vec", "unknown_entity_id_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    unknown_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., unknown_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdatePermissionInfoForEntitiesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_permission_info_vec", "user_info", "expected_permit_mtime_usecs_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PERMIT_MTIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    user_info: _permissions_pb2.UserInformation
    expected_permit_mtime_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., expected_permit_mtime_usecs_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdatePermissionInfoForEntitiesResult(_message.Message):
    __slots__ = ("error", "unknown_entity_id_vec", "invalid_entity_id_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INVALID_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    unknown_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    invalid_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., unknown_entity_id_vec: _Optional[_Iterable[int]] = ..., invalid_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetEntityPermissionInfosForSIDsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "sid_vec", "include_view_entities")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIEW_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    include_view_entities: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., include_view_entities: bool = ...) -> None: ...

class GetEntityPermissionInfosForSIDsResult(_message.Message):
    __slots__ = ("error", "sid_entity_info_vec")
    class SIDEntityInfo(_message.Message):
        __slots__ = ("sid", "entity_info_vec")
        class EntityInfo(_message.Message):
            __slots__ = ("entity_proto", "parent_entity_proto", "entity_permission_info")
            ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
            PARENT_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
            ENTITY_PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
            entity_proto: _entity_pb2.EntityProto
            parent_entity_proto: _entity_pb2.EntityProto
            entity_permission_info: _permissions_pb2.EntityPermissionInfo
            def __init__(self, entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_permission_info: _Optional[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]] = ...) -> None: ...
        SID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        entity_info_vec: _containers.RepeatedCompositeFieldContainer[GetEntityPermissionInfosForSIDsResult.SIDEntityInfo.EntityInfo]
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., entity_info_vec: _Optional[_Iterable[_Union[GetEntityPermissionInfosForSIDsResult.SIDEntityInfo.EntityInfo, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SID_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    sid_entity_info_vec: _containers.RepeatedCompositeFieldContainer[GetEntityPermissionInfosForSIDsResult.SIDEntityInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., sid_entity_info_vec: _Optional[_Iterable[_Union[GetEntityPermissionInfosForSIDsResult.SIDEntityInfo, _Mapping]]] = ...) -> None: ...

class ValidateEntitiesAccessArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id_vec", "user_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class ValidateEntitiesAccessResult(_message.Message):
    __slots__ = ("error", "disallowed_entity_id_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISALLOWED_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    disallowed_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., disallowed_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GlobalSettings(_message.Message):
    __slots__ = ("auto_upgrade_agents", "allow_sql_fci_host_standalone_registration")
    AUTO_UPGRADE_AGENTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SQL_FCI_HOST_STANDALONE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    auto_upgrade_agents: bool
    allow_sql_fci_host_standalone_registration: bool
    def __init__(self, auto_upgrade_agents: bool = ..., allow_sql_fci_host_standalone_registration: bool = ...) -> None: ...

class SetSettingsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "settings")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    settings: GlobalSettings
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., settings: _Optional[_Union[GlobalSettings, _Mapping]] = ...) -> None: ...

class SetSettingsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetSettingsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ...) -> None: ...

class GetSettingsResult(_message.Message):
    __slots__ = ("error", "settings")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    settings: GlobalSettings
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., settings: _Optional[_Union[GlobalSettings, _Mapping]] = ...) -> None: ...

class ProtectionStatus(_message.Message):
    __slots__ = ("status", "error", "warnings")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[ProtectionStatus.Type]
        kRunning: _ClassVar[ProtectionStatus.Type]
        kWarning: _ClassVar[ProtectionStatus.Type]
        kCancelled: _ClassVar[ProtectionStatus.Type]
        kError: _ClassVar[ProtectionStatus.Type]
    kSuccess: ProtectionStatus.Type
    kRunning: ProtectionStatus.Type
    kWarning: ProtectionStatus.Type
    kCancelled: ProtectionStatus.Type
    kError: ProtectionStatus.Type
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    status: ProtectionStatus.Type
    error: _error_pb2_1.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    def __init__(self, status: _Optional[_Union[ProtectionStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ...) -> None: ...

class GetProtectionInfoForEntitiesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "time_range", "status_vec", "num_consecutive_task_errors", "snapshot_type_vec", "entity_id_vec", "job_id_vec", "job_type_vec", "registered_entity_id", "include_expired_snapshots", "return_all_snapshots", "limit_num_snapshots", "pagination_cookie", "sid_vec", "user_info")
    class PaginationCookie(_message.Message):
        __slots__ = ("last_timestamp_usecs", "entity_id")
        LAST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        last_timestamp_usecs: int
        entity_id: int
        def __init__(self, last_timestamp_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSECUTIVE_TASK_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPIRED_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ALL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    time_range: TimeRange
    status_vec: _containers.RepeatedScalarFieldContainer[ProtectionStatus.Type]
    num_consecutive_task_errors: int
    snapshot_type_vec: _containers.RepeatedScalarFieldContainer[_policy_pb2.SnapshotTarget.Type]
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    job_id_vec: _containers.RepeatedScalarFieldContainer[int]
    job_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    registered_entity_id: int
    include_expired_snapshots: bool
    return_all_snapshots: bool
    limit_num_snapshots: int
    pagination_cookie: GetProtectionInfoForEntitiesArg.PaginationCookie
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., status_vec: _Optional[_Iterable[_Union[ProtectionStatus.Type, str]]] = ..., num_consecutive_task_errors: _Optional[int] = ..., snapshot_type_vec: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTarget.Type, str]]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., job_id_vec: _Optional[_Iterable[int]] = ..., job_type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., registered_entity_id: _Optional[int] = ..., include_expired_snapshots: bool = ..., return_all_snapshots: bool = ..., limit_num_snapshots: _Optional[int] = ..., pagination_cookie: _Optional[_Union[GetProtectionInfoForEntitiesArg.PaginationCookie, _Mapping]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class GetProtectionInfoForEntitiesResult(_message.Message):
    __slots__ = ("error", "entity_protection_info_vec", "pagination_cookie")
    class EntityProtectionInfo(_message.Message):
        __slots__ = ("entity", "registered_entity", "num_snapshots", "num_success", "num_errors", "num_warnings", "num_cancellations", "num_active", "num_expired", "total_logical_size_bytes", "total_logical_bytes_transferred", "copy_task_summary_vec", "latest_snapshot", "latest_successful_snapshot", "oldest_successful_snapshot", "latest_failed_snapshot", "oldest_failed_snapshot", "snapshot_info_vec")
        class SnapshotInfo(_message.Message):
            __slots__ = ("job_id", "job_uid", "job_name", "job_user_info", "job_instance_id", "attempt_num", "backup_schedule_type", "backup_status", "start_time_usecs", "end_time_usecs", "run_start_time_usecs", "logical_size_bytes", "logical_bytes_transferred", "copy_task_info_vec")
            class CopyTaskInfo(_message.Message):
                __slots__ = ("snapshot_target", "copy_status", "expiry_time_usecs")
                SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
                COPY_STATUS_FIELD_NUMBER: _ClassVar[int]
                EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
                snapshot_target: _policy_pb2.SnapshotTarget
                copy_status: ProtectionStatus
                expiry_time_usecs: int
                def __init__(self, snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., copy_status: _Optional[_Union[ProtectionStatus, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ...) -> None: ...
            JOB_ID_FIELD_NUMBER: _ClassVar[int]
            JOB_UID_FIELD_NUMBER: _ClassVar[int]
            JOB_NAME_FIELD_NUMBER: _ClassVar[int]
            JOB_USER_INFO_FIELD_NUMBER: _ClassVar[int]
            JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
            ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
            BACKUP_SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
            BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
            START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
            COPY_TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            job_id: int
            job_uid: _universal_id_pb2.UniversalIdProto
            job_name: str
            job_user_info: _permissions_pb2.UserInformation
            job_instance_id: int
            attempt_num: int
            backup_schedule_type: _enums_pb2.ScheduledBackupType.Type
            backup_status: ProtectionStatus
            start_time_usecs: int
            end_time_usecs: int
            run_start_time_usecs: int
            logical_size_bytes: int
            logical_bytes_transferred: int
            copy_task_info_vec: _containers.RepeatedCompositeFieldContainer[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo.CopyTaskInfo]
            def __init__(self, job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_name: _Optional[str] = ..., job_user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., backup_schedule_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., backup_status: _Optional[_Union[ProtectionStatus, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., copy_task_info_vec: _Optional[_Iterable[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo.CopyTaskInfo, _Mapping]]] = ...) -> None: ...
        class CopyTaskSummary(_message.Message):
            __slots__ = ("snapshot_target", "num_success", "num_errors", "num_cancellations", "num_active", "latest_successful_snapshot")
            SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
            NUM_SUCCESS_FIELD_NUMBER: _ClassVar[int]
            NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
            NUM_CANCELLATIONS_FIELD_NUMBER: _ClassVar[int]
            NUM_ACTIVE_FIELD_NUMBER: _ClassVar[int]
            LATEST_SUCCESSFUL_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
            snapshot_target: _policy_pb2.SnapshotTarget
            num_success: int
            num_errors: int
            num_cancellations: int
            num_active: int
            latest_successful_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
            def __init__(self, snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., num_success: _Optional[int] = ..., num_errors: _Optional[int] = ..., num_cancellations: _Optional[int] = ..., num_active: _Optional[int] = ..., latest_successful_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ...) -> None: ...
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_ENTITY_FIELD_NUMBER: _ClassVar[int]
        NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        NUM_SUCCESS_FIELD_NUMBER: _ClassVar[int]
        NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
        NUM_WARNINGS_FIELD_NUMBER: _ClassVar[int]
        NUM_CANCELLATIONS_FIELD_NUMBER: _ClassVar[int]
        NUM_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        NUM_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        COPY_TASK_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
        LATEST_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        LATEST_SUCCESSFUL_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        OLDEST_SUCCESSFUL_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        LATEST_FAILED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        OLDEST_FAILED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        registered_entity: _entity_pb2.EntityProto
        num_snapshots: int
        num_success: int
        num_errors: int
        num_warnings: int
        num_cancellations: int
        num_active: int
        num_expired: int
        total_logical_size_bytes: int
        total_logical_bytes_transferred: int
        copy_task_summary_vec: _containers.RepeatedCompositeFieldContainer[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.CopyTaskSummary]
        latest_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
        latest_successful_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
        oldest_successful_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
        latest_failed_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
        oldest_failed_snapshot: GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo
        snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo]
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., registered_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., num_snapshots: _Optional[int] = ..., num_success: _Optional[int] = ..., num_errors: _Optional[int] = ..., num_warnings: _Optional[int] = ..., num_cancellations: _Optional[int] = ..., num_active: _Optional[int] = ..., num_expired: _Optional[int] = ..., total_logical_size_bytes: _Optional[int] = ..., total_logical_bytes_transferred: _Optional[int] = ..., copy_task_summary_vec: _Optional[_Iterable[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.CopyTaskSummary, _Mapping]]] = ..., latest_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ..., latest_successful_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ..., oldest_successful_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ..., latest_failed_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ..., oldest_failed_snapshot: _Optional[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]] = ..., snapshot_info_vec: _Optional[_Iterable[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo.SnapshotInfo, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROTECTION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entity_protection_info_vec: _containers.RepeatedCompositeFieldContainer[GetProtectionInfoForEntitiesResult.EntityProtectionInfo]
    pagination_cookie: GetProtectionInfoForEntitiesArg.PaginationCookie
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entity_protection_info_vec: _Optional[_Iterable[_Union[GetProtectionInfoForEntitiesResult.EntityProtectionInfo, _Mapping]]] = ..., pagination_cookie: _Optional[_Union[GetProtectionInfoForEntitiesArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class ResolveEntitiesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "parent_entity", "entity_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    parent_entity: _entity_pb2.EntityProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., parent_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class ResolveEntitiesResult(_message.Message):
    __slots__ = ("error", "resolved_parent_entity", "entity_vec", "resolved_vec", "unresolved_count")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_VEC_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    resolved_parent_entity: _entity_pb2.EntityProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    resolved_vec: _containers.RepeatedScalarFieldContainer[bool]
    unresolved_count: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., resolved_parent_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., resolved_vec: _Optional[_Iterable[bool]] = ..., unresolved_count: _Optional[int] = ...) -> None: ...

class CancelRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "task_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    task_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelRestoreTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetSummaryArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "summary_type_vec", "time_range", "user_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kJobRuns: _ClassVar[GetSummaryArg.Type]
        kProtection: _ClassVar[GetSummaryArg.Type]
        kProtectedObjects: _ClassVar[GetSummaryArg.Type]
        kRestore: _ClassVar[GetSummaryArg.Type]
    kJobRuns: GetSummaryArg.Type
    kProtection: GetSummaryArg.Type
    kProtectedObjects: GetSummaryArg.Type
    kRestore: GetSummaryArg.Type
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    summary_type_vec: _containers.RepeatedScalarFieldContainer[GetSummaryArg.Type]
    time_range: TimeRange
    user_info: _permissions_pb2.UserInformation
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., summary_type_vec: _Optional[_Iterable[_Union[GetSummaryArg.Type, str]]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class GetSummaryResult(_message.Message):
    __slots__ = ("error", "job_runs", "protection", "protected_objects", "restore_objects")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_runs: _summary_pb2.BackupJobRuns
    protection: _summary_pb2.Protection
    protected_objects: _summary_pb2.ProtectedObjects
    restore_objects: _summary_pb2.RestoreObjects
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_runs: _Optional[_Union[_summary_pb2.BackupJobRuns, _Mapping]] = ..., protection: _Optional[_Union[_summary_pb2.Protection, _Mapping]] = ..., protected_objects: _Optional[_Union[_summary_pb2.ProtectedObjects, _Mapping]] = ..., restore_objects: _Optional[_Union[_summary_pb2.RestoreObjects, _Mapping]] = ...) -> None: ...

class GetVirtualDiskInfoArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "user_info", "object")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    user_info: _permissions_pb2.UserInformation
    object: _magneto_pb2.RestoreObject
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ...) -> None: ...

class GetVirtualDiskInfoResult(_message.Message):
    __slots__ = ("error", "virtual_disk_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    virtual_disk_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VirtualDiskInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., virtual_disk_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.VirtualDiskInfo, _Mapping]]] = ...) -> None: ...

class GetCdpInfoArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "user_info", "job_uids", "entity_vec", "pagination_cookie")
    class PaginationCookie(_message.Message):
        __slots__ = ("last_entity",)
        LAST_ENTITY_FIELD_NUMBER: _ClassVar[int]
        last_entity: _entity_pb2.EntityProto
        def __init__(self, last_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    user_info: _permissions_pb2.UserInformation
    job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    pagination_cookie: GetCdpInfoArg.PaginationCookie
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., job_uids: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., pagination_cookie: _Optional[_Union[GetCdpInfoArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class GetCdpInfoResult(_message.Message):
    __slots__ = ("error", "cdp_info_summary", "cdp_state_vec", "unknown_entity_vec", "pagination_cookie")
    class CdpInfoSummary(_message.Message):
        __slots__ = ("num_entities_cdp_active",)
        NUM_ENTITIES_CDP_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        num_entities_cdp_active: int
        def __init__(self, num_entities_cdp_active: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CDP_INFO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CDP_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    cdp_info_summary: GetCdpInfoResult.CdpInfoSummary
    cdp_state_vec: _containers.RepeatedCompositeFieldContainer[_master_cdp_pb2.EntityCdpStateProto]
    unknown_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    pagination_cookie: GetCdpInfoArg.PaginationCookie
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cdp_info_summary: _Optional[_Union[GetCdpInfoResult.CdpInfoSummary, _Mapping]] = ..., cdp_state_vec: _Optional[_Iterable[_Union[_master_cdp_pb2.EntityCdpStateProto, _Mapping]]] = ..., unknown_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., pagination_cookie: _Optional[_Union[GetCdpInfoArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class DeleteBackupJobPostProcessProto(_message.Message):
    __slots__ = ("job_uid", "job_id", "status")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_id: int
    status: _enums_pb2_1.DeleteBackupJobPostProcessStatus.Type
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_id: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2_1.DeleteBackupJobPostProcessStatus.Type, str]] = ...) -> None: ...

class GetBackupJobRunErrorsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_run_start_time_usecs", "task_id", "object_id", "limit_num_errors", "pagination_resume_token")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_run_start_time_usecs: int
    task_id: int
    object_id: int
    limit_num_errors: int
    pagination_resume_token: str
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_run_start_time_usecs: _Optional[int] = ..., task_id: _Optional[int] = ..., object_id: _Optional[int] = ..., limit_num_errors: _Optional[int] = ..., pagination_resume_token: _Optional[str] = ...) -> None: ...

class GetBackupJobRunErrorsResult(_message.Message):
    __slots__ = ("error", "name_vec", "error_vec", "pagination_resume_token", "persist_error_vec", "aggregated_o365_error_report", "errored_mail_info_vec")
    class O365ErroredMailInfo(_message.Message):
        __slots__ = ("sender", "subject")
        SENDER_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        sender: str
        subject: str
        def __init__(self, sender: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PERSIST_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_O365_ERROR_REPORT_FIELD_NUMBER: _ClassVar[int]
    ERRORED_MAIL_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    name_vec: _containers.RepeatedScalarFieldContainer[str]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    pagination_resume_token: str
    persist_error_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.PersistError]
    aggregated_o365_error_report: _graph_external_pb2.O365ErrorDBReportEntry
    errored_mail_info_vec: _containers.RepeatedCompositeFieldContainer[GetBackupJobRunErrorsResult.O365ErroredMailInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., name_vec: _Optional[_Iterable[str]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., pagination_resume_token: _Optional[str] = ..., persist_error_vec: _Optional[_Iterable[_Union[_magneto_pb2.PersistError, _Mapping]]] = ..., aggregated_o365_error_report: _Optional[_Union[_graph_external_pb2.O365ErrorDBReportEntry, _Mapping]] = ..., errored_mail_info_vec: _Optional[_Iterable[_Union[GetBackupJobRunErrorsResult.O365ErroredMailInfo, _Mapping]]] = ...) -> None: ...

class GetBackupJobSuccessFilesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_run_start_time_usecs", "task_id", "object_id", "limit_num_files", "pagination_resume_token_checkpt", "pagination_resume_token_error")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_CHECKPT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_run_start_time_usecs: int
    task_id: int
    object_id: int
    limit_num_files: int
    pagination_resume_token_checkpt: int
    pagination_resume_token_error: str
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_run_start_time_usecs: _Optional[int] = ..., task_id: _Optional[int] = ..., object_id: _Optional[int] = ..., limit_num_files: _Optional[int] = ..., pagination_resume_token_checkpt: _Optional[int] = ..., pagination_resume_token_error: _Optional[str] = ...) -> None: ...

class GetBackupJobSuccessFilesResult(_message.Message):
    __slots__ = ("error", "success_files", "pagination_resume_token_checkpt", "pagination_resume_token_error")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FILES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_CHECKPT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    success_files: _containers.RepeatedScalarFieldContainer[str]
    pagination_resume_token_checkpt: int
    pagination_resume_token_error: str
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., success_files: _Optional[_Iterable[str]] = ..., pagination_resume_token_checkpt: _Optional[int] = ..., pagination_resume_token_error: _Optional[str] = ...) -> None: ...

class GetFileRestoreErrorsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "task_id", "limit_num_errors", "pagination_resume_token")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    task_id: int
    limit_num_errors: int
    pagination_resume_token: str
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., task_id: _Optional[int] = ..., limit_num_errors: _Optional[int] = ..., pagination_resume_token: _Optional[str] = ...) -> None: ...

class GetFileRestoreErrorsResult(_message.Message):
    __slots__ = ("error", "name_vec", "error_vec", "pagination_resume_token", "persist_error_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PERSIST_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    name_vec: _containers.RepeatedScalarFieldContainer[str]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2_1.ErrorProto]
    pagination_resume_token: str
    persist_error_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.PersistError]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., name_vec: _Optional[_Iterable[str]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2_1.ErrorProto, _Mapping]]] = ..., pagination_resume_token: _Optional[str] = ..., persist_error_vec: _Optional[_Iterable[_Union[_magneto_pb2.PersistError, _Mapping]]] = ...) -> None: ...

class GetRestoreSuccessFilesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "task_id", "limit_num_files", "pagination_resume_token", "checkpt_root_dir_num")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHECKPT_ROOT_DIR_NUM_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    task_id: int
    limit_num_files: int
    pagination_resume_token: int
    checkpt_root_dir_num: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., task_id: _Optional[int] = ..., limit_num_files: _Optional[int] = ..., pagination_resume_token: _Optional[int] = ..., checkpt_root_dir_num: _Optional[int] = ...) -> None: ...

class GetRestoreSuccessFilesResult(_message.Message):
    __slots__ = ("error", "task_id", "success_files", "pagination_resume_token", "checkpt_root_dir_num")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FILES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHECKPT_ROOT_DIR_NUM_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    task_id: int
    success_files: _containers.RepeatedScalarFieldContainer[str]
    pagination_resume_token: int
    checkpt_root_dir_num: int
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., task_id: _Optional[int] = ..., success_files: _Optional[_Iterable[str]] = ..., pagination_resume_token: _Optional[int] = ..., checkpt_root_dir_num: _Optional[int] = ...) -> None: ...

class ExecuteRunbookActionArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id_vec", "action", "restore_arg")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPowerOffVM: _ClassVar[ExecuteRunbookActionArg.Action]
        kCloudResourcesCleanup: _ClassVar[ExecuteRunbookActionArg.Action]
        kPowerOffVApp: _ClassVar[ExecuteRunbookActionArg.Action]
    kPowerOffVM: ExecuteRunbookActionArg.Action
    kCloudResourcesCleanup: ExecuteRunbookActionArg.Action
    kPowerOffVApp: ExecuteRunbookActionArg.Action
    class RestoreArgs(_message.Message):
        __slots__ = ("restore_job_id", "ami_to_instance_id_map")
        class AmiToInstanceIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        RESTORE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
        AMI_TO_INSTANCE_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        restore_job_id: int
        ami_to_instance_id_map: _containers.ScalarMap[str, str]
        def __init__(self, restore_job_id: _Optional[int] = ..., ami_to_instance_id_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARG_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    action: ExecuteRunbookActionArg.Action
    restore_arg: ExecuteRunbookActionArg.RestoreArgs
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., action: _Optional[_Union[ExecuteRunbookActionArg.Action, str]] = ..., restore_arg: _Optional[_Union[ExecuteRunbookActionArg.RestoreArgs, _Mapping]] = ...) -> None: ...

class ExecuteRunbookActionResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetOracleDebugLogsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_instance_id", "attempt_num", "db_uuid", "db_entity_id", "job_run_start_time_usecs", "limit_size_bytes")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_instance_id: int
    attempt_num: int
    db_uuid: str
    db_entity_id: int
    job_run_start_time_usecs: int
    limit_size_bytes: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., db_uuid: _Optional[str] = ..., db_entity_id: _Optional[int] = ..., job_run_start_time_usecs: _Optional[int] = ..., limit_size_bytes: _Optional[int] = ...) -> None: ...

class GetOracleDebugLogsResult(_message.Message):
    __slots__ = ("error", "log_file_vec")
    class File(_message.Message):
        __slots__ = ("file_name", "data", "file_size")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        file_name: bytes
        data: bytes
        file_size: int
        def __init__(self, file_name: _Optional[bytes] = ..., data: _Optional[bytes] = ..., file_size: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    log_file_vec: _containers.RepeatedCompositeFieldContainer[GetOracleDebugLogsResult.File]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., log_file_vec: _Optional[_Iterable[_Union[GetOracleDebugLogsResult.File, _Mapping]]] = ...) -> None: ...

class ExpandSourcesArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "app_env", "source_filters", "user_info", "source_info_vec")
    class SourceInfo(_message.Message):
        __slots__ = ("source_id", "app_entity_id_vec")
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        APP_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        source_id: int
        app_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, source_id: _Optional[int] = ..., app_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    APP_ENV_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    app_env: _enums_pb2.Environment.Type
    source_filters: _magneto_pb2.SourceFilters
    user_info: _permissions_pb2.UserInformation
    source_info_vec: _containers.RepeatedCompositeFieldContainer[ExpandSourcesArg.SourceInfo]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., app_env: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., source_filters: _Optional[_Union[_magneto_pb2.SourceFilters, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., source_info_vec: _Optional[_Iterable[_Union[ExpandSourcesArg.SourceInfo, _Mapping]]] = ...) -> None: ...

class ExpandSourcesResult(_message.Message):
    __slots__ = ("error", "user_message", "source_entity_exclude_map")
    class SourceEntityExcludeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _magneto_pb2.SourceFiltersResult
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_magneto_pb2.SourceFiltersResult, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_EXCLUDE_MAP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    user_message: _error_pb2_1.ErrorProto
    source_entity_exclude_map: _containers.MessageMap[int, _magneto_pb2.SourceFiltersResult]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., user_message: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., source_entity_exclude_map: _Optional[_Mapping[int, _magneto_pb2.SourceFiltersResult]] = ...) -> None: ...

class GetOracleRestoreMetaInfoArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_id", "job_instance_id", "db_entity_id", "oracle_restore_params", "db_uuid_DEPRECATED", "db_uuid", "attempt_num")
    class OracleRestoreParams(_message.Message):
        __slots__ = ("new_database_name", "base_dir", "home_dir", "database_file_destination", "is_clone", "is_granular_restore", "is_recovery_validation", "same_config_ir_recovery_options")
        NEW_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_DIR_FIELD_NUMBER: _ClassVar[int]
        HOME_DIR_FIELD_NUMBER: _ClassVar[int]
        DATABASE_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        IS_CLONE_FIELD_NUMBER: _ClassVar[int]
        IS_GRANULAR_RESTORE_FIELD_NUMBER: _ClassVar[int]
        IS_RECOVERY_VALIDATION_FIELD_NUMBER: _ClassVar[int]
        SAME_CONFIG_IR_RECOVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        new_database_name: str
        base_dir: str
        home_dir: str
        database_file_destination: str
        is_clone: bool
        is_granular_restore: bool
        is_recovery_validation: bool
        same_config_ir_recovery_options: _oracle_pb2.SameConfigIrRecoveryOptions
        def __init__(self, new_database_name: _Optional[str] = ..., base_dir: _Optional[str] = ..., home_dir: _Optional[str] = ..., database_file_destination: _Optional[str] = ..., is_clone: bool = ..., is_granular_restore: bool = ..., is_recovery_validation: bool = ..., same_config_ir_recovery_options: _Optional[_Union[_oracle_pb2.SameConfigIrRecoveryOptions, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_id: int
    job_instance_id: int
    db_entity_id: int
    oracle_restore_params: GetOracleRestoreMetaInfoArg.OracleRestoreParams
    db_uuid_DEPRECATED: int
    db_uuid: str
    attempt_num: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., db_entity_id: _Optional[int] = ..., oracle_restore_params: _Optional[_Union[GetOracleRestoreMetaInfoArg.OracleRestoreParams, _Mapping]] = ..., db_uuid_DEPRECATED: _Optional[int] = ..., db_uuid: _Optional[str] = ..., attempt_num: _Optional[int] = ...) -> None: ...

class GetOracleRestoreMetaInfoResult(_message.Message):
    __slots__ = ("error", "restricted_pfile_parameter_map", "cohesity_pfile_parameter_map", "inherited_pfile_parameter_map")
    class RestrictedPfileParameterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CohesityPfileParameterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class InheritedPfileParameterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_PFILE_PARAMETER_MAP_FIELD_NUMBER: _ClassVar[int]
    COHESITY_PFILE_PARAMETER_MAP_FIELD_NUMBER: _ClassVar[int]
    INHERITED_PFILE_PARAMETER_MAP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    restricted_pfile_parameter_map: _containers.ScalarMap[str, str]
    cohesity_pfile_parameter_map: _containers.ScalarMap[str, str]
    inherited_pfile_parameter_map: _containers.ScalarMap[str, str]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., restricted_pfile_parameter_map: _Optional[_Mapping[str, str]] = ..., cohesity_pfile_parameter_map: _Optional[_Mapping[str, str]] = ..., inherited_pfile_parameter_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetMagnetoHttpRpcEncryptionCapabilityArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "encryption_type")
    class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalidEncryptionType: _ClassVar[GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType]
        kAES: _ClassVar[GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType]
    kInvalidEncryptionType: GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType
    kAES: GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    encryption_type: GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., encryption_type: _Optional[_Union[GetMagnetoHttpRpcEncryptionCapabilityArg.EncryptionType, str]] = ...) -> None: ...

class GetMagnetoHttpRpcEncryptionCapabilityResult(_message.Message):
    __slots__ = ("error", "encryption_status")
    class EncryptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnsupported: _ClassVar[GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus]
        kSupported: _ClassVar[GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus]
        kWaitingForClusterUpgrade: _ClassVar[GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus]
    kUnsupported: GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus
    kSupported: GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus
    kWaitingForClusterUpgrade: GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    encryption_status: GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., encryption_status: _Optional[_Union[GetMagnetoHttpRpcEncryptionCapabilityResult.EncryptionStatus, str]] = ...) -> None: ...

class YodaReindexRequestArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "job_uid_vec", "local_job_id_vec", "range_start_time_usecs", "range_end_time_usecs")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCAL_JOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    local_job_id_vec: _containers.RepeatedScalarFieldContainer[int]
    range_start_time_usecs: int
    range_end_time_usecs: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., local_job_id_vec: _Optional[_Iterable[int]] = ..., range_start_time_usecs: _Optional[int] = ..., range_end_time_usecs: _Optional[int] = ...) -> None: ...

class YodaReindexRequestResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetStandbyInfoArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "user_info", "job_uids", "entity_id_vec", "pagination_cookie")
    class PaginationCookie(_message.Message):
        __slots__ = ("last_entity_id",)
        LAST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        last_entity_id: int
        def __init__(self, last_entity_id: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    user_info: _permissions_pb2.UserInformation
    job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    pagination_cookie: GetStandbyInfoArg.PaginationCookie
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., job_uids: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., pagination_cookie: _Optional[_Union[GetStandbyInfoArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class GetStandbyInfoResult(_message.Message):
    __slots__ = ("error", "standby_state_vec", "pagination_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    standby_state_vec: _containers.RepeatedCompositeFieldContainer[_master_standby_pb2.StandbyStateProto]
    pagination_cookie: GetStandbyInfoArg.PaginationCookie
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., standby_state_vec: _Optional[_Iterable[_Union[_master_standby_pb2.StandbyStateProto, _Mapping]]] = ..., pagination_cookie: _Optional[_Union[GetStandbyInfoArg.PaginationCookie, _Mapping]] = ...) -> None: ...

class ListContentsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "source", "parent_entity", "pagination_params")
    class PaginationParams(_message.Message):
        __slots__ = ("offset", "size")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        size: int
        def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    source: _entity_pb2.EntityProto
    parent_entity: _entity_pb2.EntityProto
    pagination_params: ListContentsArg.PaginationParams
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., parent_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., pagination_params: _Optional[_Union[ListContentsArg.PaginationParams, _Mapping]] = ...) -> None: ...

class ListContentsResult(_message.Message):
    __slots__ = ("error", "entities", "more")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    MORE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    more: bool
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., more: bool = ...) -> None: ...

class GetTeamsChannelsListArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class GetTeamsChannelsListResult(_message.Message):
    __slots__ = ("error", "channels_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    channels_list: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.O365TeamsChannel]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., channels_list: _Optional[_Iterable[_Union[_magneto_pb2.O365TeamsChannel, _Mapping]]] = ...) -> None: ...

class GetSfdcFieldsListArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class GetSfdcFieldsListResult(_message.Message):
    __slots__ = ("error", "field_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    field_list: _containers.RepeatedCompositeFieldContainer[_sfdc_pb2.Field]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., field_list: _Optional[_Iterable[_Union[_sfdc_pb2.Field, _Mapping]]] = ...) -> None: ...

class GetSfdcRecordsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "object_name", "entity_id", "mutation_type", "aurora_cluster_info", "aws_iam_role", "pagination_params", "filter_query", "object")
    class MutationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdded: _ClassVar[GetSfdcRecordsArg.MutationType]
        kDeleted: _ClassVar[GetSfdcRecordsArg.MutationType]
        kModified: _ClassVar[GetSfdcRecordsArg.MutationType]
        kAll: _ClassVar[GetSfdcRecordsArg.MutationType]
    kAdded: GetSfdcRecordsArg.MutationType
    kDeleted: GetSfdcRecordsArg.MutationType
    kModified: GetSfdcRecordsArg.MutationType
    kAll: GetSfdcRecordsArg.MutationType
    class PaginationParams(_message.Message):
        __slots__ = ("offset", "number_of_records")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_RECORDS_FIELD_NUMBER: _ClassVar[int]
        offset: int
        number_of_records: int
        def __init__(self, offset: _Optional[int] = ..., number_of_records: _Optional[int] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MUTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    AURORA_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    AWS_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILTER_QUERY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    object_name: str
    entity_id: int
    mutation_type: GetSfdcRecordsArg.MutationType
    aurora_cluster_info: _sfdc_pb2.AuroraClusterInfo
    aws_iam_role: str
    pagination_params: GetSfdcRecordsArg.PaginationParams
    filter_query: str
    object: _magneto_pb2.RestoreObject
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., object_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., mutation_type: _Optional[_Union[GetSfdcRecordsArg.MutationType, str]] = ..., aurora_cluster_info: _Optional[_Union[_sfdc_pb2.AuroraClusterInfo, _Mapping]] = ..., aws_iam_role: _Optional[str] = ..., pagination_params: _Optional[_Union[GetSfdcRecordsArg.PaginationParams, _Mapping]] = ..., filter_query: _Optional[str] = ..., object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ...) -> None: ...

class GetSfdcRecordsResult(_message.Message):
    __slots__ = ("error", "column_names", "row_data_vec")
    class RowData(_message.Message):
        __slots__ = ("column_vec",)
        COLUMN_VEC_FIELD_NUMBER: _ClassVar[int]
        column_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, column_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    ROW_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    column_names: GetSfdcRecordsResult.RowData
    row_data_vec: _containers.RepeatedCompositeFieldContainer[GetSfdcRecordsResult.RowData]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., column_names: _Optional[_Union[GetSfdcRecordsResult.RowData, _Mapping]] = ..., row_data_vec: _Optional[_Iterable[_Union[GetSfdcRecordsResult.RowData, _Mapping]]] = ...) -> None: ...

class GetSfdcDependentObjectsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "object_name", "entity_id", "object")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    object_name: str
    entity_id: int
    object: _magneto_pb2.RestoreObject
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., object_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., object: _Optional[_Union[_magneto_pb2.RestoreObject, _Mapping]] = ...) -> None: ...

class GetSfdcDependentObjectsResult(_message.Message):
    __slots__ = ("error", "parents_vec", "children_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    parents_vec: _containers.RepeatedScalarFieldContainer[str]
    children_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., parents_vec: _Optional[_Iterable[str]] = ..., children_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSchedulerStatsArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "filters", "options")
    class Filters(_message.Message):
        __slots__ = ("current_time", "interval_usecs", "tenant_ids", "env_types")
        class Interval(_message.Message):
            __slots__ = ("start_timestamp_usecs", "end_timestamp_usecs")
            START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
            END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
            start_timestamp_usecs: int
            end_timestamp_usecs: int
            def __init__(self, start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ...) -> None: ...
        CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_USECS_FIELD_NUMBER: _ClassVar[int]
        TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
        ENV_TYPES_FIELD_NUMBER: _ClassVar[int]
        current_time: bool
        interval_usecs: GetSchedulerStatsArg.Filters.Interval
        tenant_ids: _containers.RepeatedScalarFieldContainer[str]
        env_types: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
        def __init__(self, current_time: bool = ..., interval_usecs: _Optional[_Union[GetSchedulerStatsArg.Filters.Interval, _Mapping]] = ..., tenant_ids: _Optional[_Iterable[str]] = ..., env_types: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ...) -> None: ...
    class Options(_message.Message):
        __slots__ = ("return_job_stats",)
        RETURN_JOB_STATS_FIELD_NUMBER: _ClassVar[int]
        return_job_stats: bool
        def __init__(self, return_job_stats: bool = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    filters: GetSchedulerStatsArg.Filters
    options: GetSchedulerStatsArg.Options
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., filters: _Optional[_Union[GetSchedulerStatsArg.Filters, _Mapping]] = ..., options: _Optional[_Union[GetSchedulerStatsArg.Options, _Mapping]] = ...) -> None: ...

class GetSchedulerStatsResult(_message.Message):
    __slots__ = ("error", "job_stats")
    class JobStats(_message.Message):
        __slots__ = ("num_total_runs", "max_concurrent_runs", "num_jobs")
        NUM_TOTAL_RUNS_FIELD_NUMBER: _ClassVar[int]
        MAX_CONCURRENT_RUNS_FIELD_NUMBER: _ClassVar[int]
        NUM_JOBS_FIELD_NUMBER: _ClassVar[int]
        num_total_runs: int
        max_concurrent_runs: int
        num_jobs: int
        def __init__(self, num_total_runs: _Optional[int] = ..., max_concurrent_runs: _Optional[int] = ..., num_jobs: _Optional[int] = ...) -> None: ...
    class Counters(_message.Message):
        __slots__ = ("num_items", "logical_bytes", "physical_bytes")
        NUM_ITEMS_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        num_items: int
        logical_bytes: int
        physical_bytes: int
        def __init__(self, num_items: _Optional[int] = ..., logical_bytes: _Optional[int] = ..., physical_bytes: _Optional[int] = ...) -> None: ...
    class Interval(_message.Message):
        __slots__ = ("start_timestamp_usecs", "end_timestamp_usecs")
        START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        start_timestamp_usecs: int
        end_timestamp_usecs: int
        def __init__(self, start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class BackupTypeCounters(_message.Message):
        __slots__ = ("backup_type", "protected_ideal", "protected_actual", "trimmed_interval")
        BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_IDEAL_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_ACTUAL_FIELD_NUMBER: _ClassVar[int]
        TRIMMED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        backup_type: _enums_pb2.ScheduledBackupType.Type
        protected_ideal: GetSchedulerStatsResult.Counters
        protected_actual: GetSchedulerStatsResult.Counters
        trimmed_interval: GetSchedulerStatsResult.Interval
        def __init__(self, backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., protected_ideal: _Optional[_Union[GetSchedulerStatsResult.Counters, _Mapping]] = ..., protected_actual: _Optional[_Union[GetSchedulerStatsResult.Counters, _Mapping]] = ..., trimmed_interval: _Optional[_Union[GetSchedulerStatsResult.Interval, _Mapping]] = ...) -> None: ...
    class SchedulingEventCounters(_message.Message):
        __slots__ = ("cumulative_counters", "per_backup_type_counters")
        CUMULATIVE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
        PER_BACKUP_TYPE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
        cumulative_counters: GetSchedulerStatsResult.Counters
        per_backup_type_counters: _containers.RepeatedCompositeFieldContainer[GetSchedulerStatsResult.BackupTypeCounters]
        def __init__(self, cumulative_counters: _Optional[_Union[GetSchedulerStatsResult.Counters, _Mapping]] = ..., per_backup_type_counters: _Optional[_Iterable[_Union[GetSchedulerStatsResult.BackupTypeCounters, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    job_stats: GetSchedulerStatsResult.JobStats
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_stats: _Optional[_Union[GetSchedulerStatsResult.JobStats, _Mapping]] = ...) -> None: ...

class EnableCDPArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr", "entity_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class EnableCDPResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GetDataProtectSshPublicKeyArg(_message.Message):
    __slots__ = ("api_version", "api_request_attr")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    api_request_attr: APIRequestAttr
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., api_request_attr: _Optional[_Union[APIRequestAttr, _Mapping]] = ...) -> None: ...

class GetDataProtectSshPublicKeyResult(_message.Message):
    __slots__ = ("error", "public_key")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    public_key: str
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., public_key: _Optional[str] = ...) -> None: ...
