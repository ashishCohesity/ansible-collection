from atom.base import atom_pb2 as _atom_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.connectors.vmware import vmware_pb2 as _vmware_pb2_1
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityCdpStateProto(_message.Message):
    __slots__ = ("entity", "job_uid", "is_cdp_enabled", "pre_process_status", "cdp_filter_status", "image_backup_info", "hydration_point_info", "cdp_log_info", "state_intent", "process_events_info", "cluster_compute_resource_entity_id", "cdp_version", "log_run_info", "is_replicated_entity", "replication_strategy", "post_process_status", "alert_info", "sync_repl_info_map", "tx_entity_id", "tx_job_uid", "is_stale", "guardrails_info", "is_journal_sharded", "allow_re_enable_cdp", "purge_data_events")
    class ReplicationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPeriodic: _ClassVar[EntityCdpStateProto.ReplicationStrategy]
        kSync: _ClassVar[EntityCdpStateProto.ReplicationStrategy]
    kPeriodic: EntityCdpStateProto.ReplicationStrategy
    kSync: EntityCdpStateProto.ReplicationStrategy
    class PreProcessingStatus(_message.Message):
        __slots__ = ("state", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.PreProcessingStatus.State]
            kStarted: _ClassVar[EntityCdpStateProto.PreProcessingStatus.State]
            kInProgress: _ClassVar[EntityCdpStateProto.PreProcessingStatus.State]
            kFinished: _ClassVar[EntityCdpStateProto.PreProcessingStatus.State]
            kError: _ClassVar[EntityCdpStateProto.PreProcessingStatus.State]
        kUnknown: EntityCdpStateProto.PreProcessingStatus.State
        kStarted: EntityCdpStateProto.PreProcessingStatus.State
        kInProgress: EntityCdpStateProto.PreProcessingStatus.State
        kFinished: EntityCdpStateProto.PreProcessingStatus.State
        kError: EntityCdpStateProto.PreProcessingStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.PreProcessingStatus.State
        error: _error_pb2.ErrorProto
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.PreProcessingStatus.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class CDPFilterStatus(_message.Message):
        __slots__ = ("state", "version", "error", "filter_issues", "storage_policy_attached_offline", "last_filter_alert_raised_time_secs", "io_filter_properties")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kNotInstalled: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kInstallFilterInProgress: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kFilterInstalled: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kUninstallFilterInProgress: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kUpgradeFilterInProgress: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kUpgradeFilterFailed: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kUninstallFilterFailed: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kFilterInstalledIOInactive: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kIOInactive: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kIOActivationInProgress: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kIOActive: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kIODeactivationInProgress: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
            kWaitingForCDPPolicyAttach: _ClassVar[EntityCdpStateProto.CDPFilterStatus.State]
        kUnknown: EntityCdpStateProto.CDPFilterStatus.State
        kNotInstalled: EntityCdpStateProto.CDPFilterStatus.State
        kInstallFilterInProgress: EntityCdpStateProto.CDPFilterStatus.State
        kFilterInstalled: EntityCdpStateProto.CDPFilterStatus.State
        kUninstallFilterInProgress: EntityCdpStateProto.CDPFilterStatus.State
        kUpgradeFilterInProgress: EntityCdpStateProto.CDPFilterStatus.State
        kUpgradeFilterFailed: EntityCdpStateProto.CDPFilterStatus.State
        kUninstallFilterFailed: EntityCdpStateProto.CDPFilterStatus.State
        kFilterInstalledIOInactive: EntityCdpStateProto.CDPFilterStatus.State
        kIOInactive: EntityCdpStateProto.CDPFilterStatus.State
        kIOActivationInProgress: EntityCdpStateProto.CDPFilterStatus.State
        kIOActive: EntityCdpStateProto.CDPFilterStatus.State
        kIODeactivationInProgress: EntityCdpStateProto.CDPFilterStatus.State
        kWaitingForCDPPolicyAttach: EntityCdpStateProto.CDPFilterStatus.State
        class FilterIssuesOnHosts(_message.Message):
            __slots__ = ("action", "host_io_filter_issues")
            ACTION_FIELD_NUMBER: _ClassVar[int]
            HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
            action: str
            host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.IoFilterHostIssue]
            def __init__(self, action: _Optional[str] = ..., host_io_filter_issues: _Optional[_Iterable[_Union[_vmware_pb2_1.IoFilterHostIssue, _Mapping]]] = ...) -> None: ...
        STATE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
        STORAGE_POLICY_ATTACHED_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        LAST_FILTER_ALERT_RAISED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        IO_FILTER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.CDPFilterStatus.State
        version: str
        error: _error_pb2.ErrorProto
        filter_issues: EntityCdpStateProto.CDPFilterStatus.FilterIssuesOnHosts
        storage_policy_attached_offline: bool
        last_filter_alert_raised_time_secs: int
        io_filter_properties: _vmware_pb2.IoFilterStoragePolicyProperties
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.CDPFilterStatus.State, str]] = ..., version: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., filter_issues: _Optional[_Union[EntityCdpStateProto.CDPFilterStatus.FilterIssuesOnHosts, _Mapping]] = ..., storage_policy_attached_offline: bool = ..., last_filter_alert_raised_time_secs: _Optional[int] = ..., io_filter_properties: _Optional[_Union[_vmware_pb2.IoFilterStoragePolicyProperties, _Mapping]] = ...) -> None: ...
    class ImageBackupInfo(_message.Message):
        __slots__ = ("state", "details", "last_backup_task_id", "last_backup_start_time_usecs", "last_backup_end_time_usecs", "error", "vmsd_file_path", "snapshot_create_time_secs")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.ImageBackupInfo.State]
            kTakeBackup: _ClassVar[EntityCdpStateProto.ImageBackupInfo.State]
            kInProgress: _ClassVar[EntityCdpStateProto.ImageBackupInfo.State]
            kComplete: _ClassVar[EntityCdpStateProto.ImageBackupInfo.State]
            kError: _ClassVar[EntityCdpStateProto.ImageBackupInfo.State]
        kUnknown: EntityCdpStateProto.ImageBackupInfo.State
        kTakeBackup: EntityCdpStateProto.ImageBackupInfo.State
        kInProgress: EntityCdpStateProto.ImageBackupInfo.State
        kComplete: EntityCdpStateProto.ImageBackupInfo.State
        kError: EntityCdpStateProto.ImageBackupInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        LAST_BACKUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_BACKUP_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_BACKUP_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        VMSD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.ImageBackupInfo.State
        details: str
        last_backup_task_id: int
        last_backup_start_time_usecs: int
        last_backup_end_time_usecs: int
        error: _error_pb2.ErrorProto
        vmsd_file_path: str
        snapshot_create_time_secs: int
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.ImageBackupInfo.State, str]] = ..., details: _Optional[str] = ..., last_backup_task_id: _Optional[int] = ..., last_backup_start_time_usecs: _Optional[int] = ..., last_backup_end_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vmsd_file_path: _Optional[str] = ..., snapshot_create_time_secs: _Optional[int] = ...) -> None: ...
    class HydrationPointInfo(_message.Message):
        __slots__ = ("state", "last_hydration_task_id", "last_hydration_timestamp_usecs", "last_successful_hydration_timestamp_usecs", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.HydrationPointInfo.State]
            kInProgress: _ClassVar[EntityCdpStateProto.HydrationPointInfo.State]
            kComplete: _ClassVar[EntityCdpStateProto.HydrationPointInfo.State]
            kError: _ClassVar[EntityCdpStateProto.HydrationPointInfo.State]
        kUnknown: EntityCdpStateProto.HydrationPointInfo.State
        kInProgress: EntityCdpStateProto.HydrationPointInfo.State
        kComplete: EntityCdpStateProto.HydrationPointInfo.State
        kError: EntityCdpStateProto.HydrationPointInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        LAST_HYDRATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_HYDRATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_SUCCESSFUL_HYDRATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.HydrationPointInfo.State
        last_hydration_task_id: int
        last_hydration_timestamp_usecs: int
        last_successful_hydration_timestamp_usecs: int
        error: _error_pb2.ErrorProto
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.HydrationPointInfo.State, str]] = ..., last_hydration_task_id: _Optional[int] = ..., last_hydration_timestamp_usecs: _Optional[int] = ..., last_successful_hydration_timestamp_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class CDPLogInfo(_message.Message):
        __slots__ = ("view_box_id", "log_view_dir")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        LOG_VIEW_DIR_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        log_view_dir: str
        def __init__(self, view_box_id: _Optional[int] = ..., log_view_dir: _Optional[str] = ...) -> None: ...
    class StateIntent(_message.Message):
        __slots__ = ("filter_intent", "take_backup")
        class FilterIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kIOActive: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kIOInactive: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kInstallFilter: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kUninstallFilter: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kUpgradeFilter: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
            kNone: _ClassVar[EntityCdpStateProto.StateIntent.FilterIntent]
        kUnknown: EntityCdpStateProto.StateIntent.FilterIntent
        kIOActive: EntityCdpStateProto.StateIntent.FilterIntent
        kIOInactive: EntityCdpStateProto.StateIntent.FilterIntent
        kInstallFilter: EntityCdpStateProto.StateIntent.FilterIntent
        kUninstallFilter: EntityCdpStateProto.StateIntent.FilterIntent
        kUpgradeFilter: EntityCdpStateProto.StateIntent.FilterIntent
        kNone: EntityCdpStateProto.StateIntent.FilterIntent
        FILTER_INTENT_FIELD_NUMBER: _ClassVar[int]
        TAKE_BACKUP_FIELD_NUMBER: _ClassVar[int]
        filter_intent: EntityCdpStateProto.StateIntent.FilterIntent
        take_backup: bool
        def __init__(self, filter_intent: _Optional[_Union[EntityCdpStateProto.StateIntent.FilterIntent, str]] = ..., take_backup: bool = ...) -> None: ...
    class ProcessEventsInfo(_message.Message):
        __slots__ = ("latest_processed_migration_time_usecs",)
        LATEST_PROCESSED_MIGRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        latest_processed_migration_time_usecs: int
        def __init__(self, latest_processed_migration_time_usecs: _Optional[int] = ...) -> None: ...
    class LogRunInfo(_message.Message):
        __slots__ = ("state", "last_log_run_timestamp_usecs", "last_applied_io_timestamp_usecs", "last_switched_epoch", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.LogRunInfo.State]
            kInProgress: _ClassVar[EntityCdpStateProto.LogRunInfo.State]
            kComplete: _ClassVar[EntityCdpStateProto.LogRunInfo.State]
            kError: _ClassVar[EntityCdpStateProto.LogRunInfo.State]
        kUnknown: EntityCdpStateProto.LogRunInfo.State
        kInProgress: EntityCdpStateProto.LogRunInfo.State
        kComplete: EntityCdpStateProto.LogRunInfo.State
        kError: EntityCdpStateProto.LogRunInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        LAST_LOG_RUN_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_APPLIED_IO_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_SWITCHED_EPOCH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.LogRunInfo.State
        last_log_run_timestamp_usecs: int
        last_applied_io_timestamp_usecs: int
        last_switched_epoch: _atom_pb2.EpochProto
        error: _error_pb2.ErrorProto
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.LogRunInfo.State, str]] = ..., last_log_run_timestamp_usecs: _Optional[int] = ..., last_applied_io_timestamp_usecs: _Optional[int] = ..., last_switched_epoch: _Optional[_Union[_atom_pb2.EpochProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class PostProcessingStatus(_message.Message):
        __slots__ = ("state", "retry_count", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.PostProcessingStatus.State]
            kStarted: _ClassVar[EntityCdpStateProto.PostProcessingStatus.State]
            kInProgress: _ClassVar[EntityCdpStateProto.PostProcessingStatus.State]
            kFinished: _ClassVar[EntityCdpStateProto.PostProcessingStatus.State]
            kError: _ClassVar[EntityCdpStateProto.PostProcessingStatus.State]
        kUnknown: EntityCdpStateProto.PostProcessingStatus.State
        kStarted: EntityCdpStateProto.PostProcessingStatus.State
        kInProgress: EntityCdpStateProto.PostProcessingStatus.State
        kFinished: EntityCdpStateProto.PostProcessingStatus.State
        kError: EntityCdpStateProto.PostProcessingStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.PostProcessingStatus.State
        retry_count: int
        error: _error_pb2.ErrorProto
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.PostProcessingStatus.State, str]] = ..., retry_count: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class AlertInfo(_message.Message):
        __slots__ = ("type", "msg")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.AlertInfo.Type]
            kCDPDisabled: _ClassVar[EntityCdpStateProto.AlertInfo.Type]
        kUnknown: EntityCdpStateProto.AlertInfo.Type
        kCDPDisabled: EntityCdpStateProto.AlertInfo.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MSG_FIELD_NUMBER: _ClassVar[int]
        type: EntityCdpStateProto.AlertInfo.Type
        msg: str
        def __init__(self, type: _Optional[_Union[EntityCdpStateProto.AlertInfo.Type, str]] = ..., msg: _Optional[str] = ...) -> None: ...
    class SyncReplicationInfo(_message.Message):
        __slots__ = ("state", "error", "remote_cluster_id", "last_replicated_run_start_time_usecs", "last_replicated_backup_type", "rx_hole_info", "last_fetched_state_time_usecs")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kStart: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kSyncReplicate: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kWaitingForSnapshot: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kSteady: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kStop: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kInitInProgress: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
            kSnapshotInProgress: _ClassVar[EntityCdpStateProto.SyncReplicationInfo.State]
        kUnknown: EntityCdpStateProto.SyncReplicationInfo.State
        kStart: EntityCdpStateProto.SyncReplicationInfo.State
        kSyncReplicate: EntityCdpStateProto.SyncReplicationInfo.State
        kWaitingForSnapshot: EntityCdpStateProto.SyncReplicationInfo.State
        kSteady: EntityCdpStateProto.SyncReplicationInfo.State
        kStop: EntityCdpStateProto.SyncReplicationInfo.State
        kInitInProgress: EntityCdpStateProto.SyncReplicationInfo.State
        kSnapshotInProgress: EntityCdpStateProto.SyncReplicationInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_REPLICATED_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_REPLICATED_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        RX_HOLE_INFO_FIELD_NUMBER: _ClassVar[int]
        LAST_FETCHED_STATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        state: EntityCdpStateProto.SyncReplicationInfo.State
        error: _error_pb2.ErrorProto
        remote_cluster_id: int
        last_replicated_run_start_time_usecs: int
        last_replicated_backup_type: _enums_pb2.ScheduledBackupType.Type
        rx_hole_info: CDPHoleInfo
        last_fetched_state_time_usecs: int
        def __init__(self, state: _Optional[_Union[EntityCdpStateProto.SyncReplicationInfo.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., remote_cluster_id: _Optional[int] = ..., last_replicated_run_start_time_usecs: _Optional[int] = ..., last_replicated_backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., rx_hole_info: _Optional[_Union[CDPHoleInfo, _Mapping]] = ..., last_fetched_state_time_usecs: _Optional[int] = ...) -> None: ...
    class SyncReplInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EntityCdpStateProto.SyncReplicationInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EntityCdpStateProto.SyncReplicationInfo, _Mapping]] = ...) -> None: ...
    class GuardrailsInfo(_message.Message):
        __slots__ = ("hydration_skip_start_time_usecs", "esx_max_io_throughput_mbps", "last_esx_max_throughput_processing_time_usecs", "disable_intent", "last_cdp_disabled_time_usecs", "cdp_disabled_time_usecs_vec", "error")
        class DisableIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[EntityCdpStateProto.GuardrailsInfo.DisableIntent]
            kDisableCDP: _ClassVar[EntityCdpStateProto.GuardrailsInfo.DisableIntent]
            kPermanentDisableCDP: _ClassVar[EntityCdpStateProto.GuardrailsInfo.DisableIntent]
            kNone: _ClassVar[EntityCdpStateProto.GuardrailsInfo.DisableIntent]
        kUnknown: EntityCdpStateProto.GuardrailsInfo.DisableIntent
        kDisableCDP: EntityCdpStateProto.GuardrailsInfo.DisableIntent
        kPermanentDisableCDP: EntityCdpStateProto.GuardrailsInfo.DisableIntent
        kNone: EntityCdpStateProto.GuardrailsInfo.DisableIntent
        HYDRATION_SKIP_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ESX_MAX_IO_THROUGHPUT_MBPS_FIELD_NUMBER: _ClassVar[int]
        LAST_ESX_MAX_THROUGHPUT_PROCESSING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_INTENT_FIELD_NUMBER: _ClassVar[int]
        LAST_CDP_DISABLED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CDP_DISABLED_TIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        hydration_skip_start_time_usecs: int
        esx_max_io_throughput_mbps: int
        last_esx_max_throughput_processing_time_usecs: int
        disable_intent: EntityCdpStateProto.GuardrailsInfo.DisableIntent
        last_cdp_disabled_time_usecs: int
        cdp_disabled_time_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
        error: _error_pb2.ErrorProto
        def __init__(self, hydration_skip_start_time_usecs: _Optional[int] = ..., esx_max_io_throughput_mbps: _Optional[int] = ..., last_esx_max_throughput_processing_time_usecs: _Optional[int] = ..., disable_intent: _Optional[_Union[EntityCdpStateProto.GuardrailsInfo.DisableIntent, str]] = ..., last_cdp_disabled_time_usecs: _Optional[int] = ..., cdp_disabled_time_usecs_vec: _Optional[_Iterable[int]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    IS_CDP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRE_PROCESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    CDP_FILTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    CDP_LOG_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_EVENTS_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_COMPUTE_RESOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CDP_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOG_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_REPLICATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    ALERT_INFO_FIELD_NUMBER: _ClassVar[int]
    SYNC_REPL_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    TX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    IS_STALE_FIELD_NUMBER: _ClassVar[int]
    GUARDRAILS_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RE_ENABLE_CDP_FIELD_NUMBER: _ClassVar[int]
    PURGE_DATA_EVENTS_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    job_uid: _universal_id_pb2.UniversalIdProto
    is_cdp_enabled: bool
    pre_process_status: EntityCdpStateProto.PreProcessingStatus
    cdp_filter_status: EntityCdpStateProto.CDPFilterStatus
    image_backup_info: EntityCdpStateProto.ImageBackupInfo
    hydration_point_info: EntityCdpStateProto.HydrationPointInfo
    cdp_log_info: EntityCdpStateProto.CDPLogInfo
    state_intent: EntityCdpStateProto.StateIntent
    process_events_info: EntityCdpStateProto.ProcessEventsInfo
    cluster_compute_resource_entity_id: int
    cdp_version: _common_pb2.CDPVersion
    log_run_info: EntityCdpStateProto.LogRunInfo
    is_replicated_entity: bool
    replication_strategy: EntityCdpStateProto.ReplicationStrategy
    post_process_status: EntityCdpStateProto.PostProcessingStatus
    alert_info: EntityCdpStateProto.AlertInfo
    sync_repl_info_map: _containers.MessageMap[int, EntityCdpStateProto.SyncReplicationInfo]
    tx_entity_id: int
    tx_job_uid: _universal_id_pb2.UniversalIdProto
    is_stale: bool
    guardrails_info: EntityCdpStateProto.GuardrailsInfo
    is_journal_sharded: bool
    allow_re_enable_cdp: bool
    purge_data_events: bool
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_cdp_enabled: bool = ..., pre_process_status: _Optional[_Union[EntityCdpStateProto.PreProcessingStatus, _Mapping]] = ..., cdp_filter_status: _Optional[_Union[EntityCdpStateProto.CDPFilterStatus, _Mapping]] = ..., image_backup_info: _Optional[_Union[EntityCdpStateProto.ImageBackupInfo, _Mapping]] = ..., hydration_point_info: _Optional[_Union[EntityCdpStateProto.HydrationPointInfo, _Mapping]] = ..., cdp_log_info: _Optional[_Union[EntityCdpStateProto.CDPLogInfo, _Mapping]] = ..., state_intent: _Optional[_Union[EntityCdpStateProto.StateIntent, _Mapping]] = ..., process_events_info: _Optional[_Union[EntityCdpStateProto.ProcessEventsInfo, _Mapping]] = ..., cluster_compute_resource_entity_id: _Optional[int] = ..., cdp_version: _Optional[_Union[_common_pb2.CDPVersion, str]] = ..., log_run_info: _Optional[_Union[EntityCdpStateProto.LogRunInfo, _Mapping]] = ..., is_replicated_entity: bool = ..., replication_strategy: _Optional[_Union[EntityCdpStateProto.ReplicationStrategy, str]] = ..., post_process_status: _Optional[_Union[EntityCdpStateProto.PostProcessingStatus, _Mapping]] = ..., alert_info: _Optional[_Union[EntityCdpStateProto.AlertInfo, _Mapping]] = ..., sync_repl_info_map: _Optional[_Mapping[int, EntityCdpStateProto.SyncReplicationInfo]] = ..., tx_entity_id: _Optional[int] = ..., tx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_stale: bool = ..., guardrails_info: _Optional[_Union[EntityCdpStateProto.GuardrailsInfo, _Mapping]] = ..., is_journal_sharded: bool = ..., allow_re_enable_cdp: bool = ..., purge_data_events: bool = ...) -> None: ...

class CDPHoleInfo(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...
