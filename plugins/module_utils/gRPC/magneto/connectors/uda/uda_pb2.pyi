from magneto.agents.stub import uda_param_pb2 as _uda_param_pb2
from magneto.base.entities import azure_pb2 as _azure_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import uda_pb2 as _uda_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import entity_pb2 as _entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("backup_view_name", "job_instance_id", "attempt_num", "progress_percent", "error", "stats", "task_id", "backup_state", "page", "process_info", "pulse_log_index", "mountpoint_vec", "view_id", "cancel_job_retry_current_count", "log_backup_start_epoch_secs", "log_backup_end_epoch_secs", "control_node", "log_view_name", "log_view_id", "auto_log_view_mounted", "auto_log_mountpoint_vec", "mount_vips", "job_status_retry_count", "cloned_auto_log_view_name", "data_backup_epoch_secs", "snapshot_time_usecs", "bifrost_constituent_id", "heimdall_disk_request_id", "heimdall_disk_mountpoint", "ancestor_entity", "abort", "azure_info", "cohesity_cp_copy_mode")
    class BackupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.BackupState]
        kViewFinalized: _ClassVar[SnapshotInfo.BackupState]
        kMaybeViewCreated: _ClassVar[SnapshotInfo.BackupState]
        kMaybeViewMounted: _ClassVar[SnapshotInfo.BackupState]
        kSentEntities: _ClassVar[SnapshotInfo.BackupState]
        kStartedAttempt: _ClassVar[SnapshotInfo.BackupState]
        kFinishedAttempt: _ClassVar[SnapshotInfo.BackupState]
        kJobDetailsFetched: _ClassVar[SnapshotInfo.BackupState]
        kMaybeViewUnmounted: _ClassVar[SnapshotInfo.BackupState]
        kClonedView: _ClassVar[SnapshotInfo.BackupState]
        kFinished: _ClassVar[SnapshotInfo.BackupState]
        kCancelJob: _ClassVar[SnapshotInfo.BackupState]
        kAutoLogViewFinalized: _ClassVar[SnapshotInfo.BackupState]
        kMaybeAutoLogViewCreated: _ClassVar[SnapshotInfo.BackupState]
        kClonedAutoLogView: _ClassVar[SnapshotInfo.BackupState]
        kGotAllEndPoints: _ClassVar[SnapshotInfo.BackupState]
        kRemovedStaleMounts: _ClassVar[SnapshotInfo.BackupState]
        kDeletedPreviousView: _ClassVar[SnapshotInfo.BackupState]
        kCreatedIndexingView: _ClassVar[SnapshotInfo.BackupState]
        kMaybeAutoViewMounted: _ClassVar[SnapshotInfo.BackupState]
        kMaybeModifyView: _ClassVar[SnapshotInfo.BackupState]
        kMaybeModifyAutoLogView: _ClassVar[SnapshotInfo.BackupState]
        kPermitGranted: _ClassVar[SnapshotInfo.BackupState]
        kPreBackupDone: _ClassVar[SnapshotInfo.BackupState]
        kMaybeExternalDiskAdded: _ClassVar[SnapshotInfo.BackupState]
        kMaybeExternalDiskRemoved: _ClassVar[SnapshotInfo.BackupState]
    kStarted: SnapshotInfo.BackupState
    kViewFinalized: SnapshotInfo.BackupState
    kMaybeViewCreated: SnapshotInfo.BackupState
    kMaybeViewMounted: SnapshotInfo.BackupState
    kSentEntities: SnapshotInfo.BackupState
    kStartedAttempt: SnapshotInfo.BackupState
    kFinishedAttempt: SnapshotInfo.BackupState
    kJobDetailsFetched: SnapshotInfo.BackupState
    kMaybeViewUnmounted: SnapshotInfo.BackupState
    kClonedView: SnapshotInfo.BackupState
    kFinished: SnapshotInfo.BackupState
    kCancelJob: SnapshotInfo.BackupState
    kAutoLogViewFinalized: SnapshotInfo.BackupState
    kMaybeAutoLogViewCreated: SnapshotInfo.BackupState
    kClonedAutoLogView: SnapshotInfo.BackupState
    kGotAllEndPoints: SnapshotInfo.BackupState
    kRemovedStaleMounts: SnapshotInfo.BackupState
    kDeletedPreviousView: SnapshotInfo.BackupState
    kCreatedIndexingView: SnapshotInfo.BackupState
    kMaybeAutoViewMounted: SnapshotInfo.BackupState
    kMaybeModifyView: SnapshotInfo.BackupState
    kMaybeModifyAutoLogView: SnapshotInfo.BackupState
    kPermitGranted: SnapshotInfo.BackupState
    kPreBackupDone: SnapshotInfo.BackupState
    kMaybeExternalDiskAdded: SnapshotInfo.BackupState
    kMaybeExternalDiskRemoved: SnapshotInfo.BackupState
    class CohesityCpCopyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloudSnapFS: _ClassVar[SnapshotInfo.CohesityCpCopyMode]
        kRemoteWanSnapFS: _ClassVar[SnapshotInfo.CohesityCpCopyMode]
    kCloudSnapFS: SnapshotInfo.CohesityCpCopyMode
    kRemoteWanSnapFS: SnapshotInfo.CohesityCpCopyMode
    UDA_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    uda_snapshot_info: _descriptor.FieldDescriptor
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STATE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    PULSE_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_JOB_RETRY_CURRENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_START_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_END_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_NODE_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_VIEW_MOUNTED_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOG_MOUNTPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VIPS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLONED_AUTO_LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_BACKUP_EPOCH_SECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEIMDALL_DISK_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HEIMDALL_DISK_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    AZURE_INFO_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CP_COPY_MODE_FIELD_NUMBER: _ClassVar[int]
    backup_view_name: str
    job_instance_id: int
    attempt_num: int
    progress_percent: int
    error: _error_pb2.ErrorProto
    stats: _uda_pb2.UdaStats
    task_id: int
    backup_state: SnapshotInfo.BackupState
    page: int
    process_info: _uda_param_pb2.ProcessInfo
    pulse_log_index: int
    mountpoint_vec: _containers.RepeatedScalarFieldContainer[str]
    view_id: int
    cancel_job_retry_current_count: int
    log_backup_start_epoch_secs: int
    log_backup_end_epoch_secs: int
    control_node: str
    log_view_name: str
    log_view_id: int
    auto_log_view_mounted: bool
    auto_log_mountpoint_vec: _containers.RepeatedScalarFieldContainer[str]
    mount_vips: _containers.RepeatedScalarFieldContainer[str]
    job_status_retry_count: int
    cloned_auto_log_view_name: str
    data_backup_epoch_secs: int
    snapshot_time_usecs: int
    bifrost_constituent_id: int
    heimdall_disk_request_id: str
    heimdall_disk_mountpoint: str
    ancestor_entity: _entity_pb2.EntityProto
    abort: bool
    azure_info: _azure_pb2.AzureSnapshotProps
    cohesity_cp_copy_mode: SnapshotInfo.CohesityCpCopyMode
    def __init__(self, backup_view_name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[_uda_pb2.UdaStats, _Mapping]] = ..., task_id: _Optional[int] = ..., backup_state: _Optional[_Union[SnapshotInfo.BackupState, str]] = ..., page: _Optional[int] = ..., process_info: _Optional[_Union[_uda_param_pb2.ProcessInfo, _Mapping]] = ..., pulse_log_index: _Optional[int] = ..., mountpoint_vec: _Optional[_Iterable[str]] = ..., view_id: _Optional[int] = ..., cancel_job_retry_current_count: _Optional[int] = ..., log_backup_start_epoch_secs: _Optional[int] = ..., log_backup_end_epoch_secs: _Optional[int] = ..., control_node: _Optional[str] = ..., log_view_name: _Optional[str] = ..., log_view_id: _Optional[int] = ..., auto_log_view_mounted: bool = ..., auto_log_mountpoint_vec: _Optional[_Iterable[str]] = ..., mount_vips: _Optional[_Iterable[str]] = ..., job_status_retry_count: _Optional[int] = ..., cloned_auto_log_view_name: _Optional[str] = ..., data_backup_epoch_secs: _Optional[int] = ..., snapshot_time_usecs: _Optional[int] = ..., bifrost_constituent_id: _Optional[int] = ..., heimdall_disk_request_id: _Optional[str] = ..., heimdall_disk_mountpoint: _Optional[str] = ..., ancestor_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., abort: bool = ..., azure_info: _Optional[_Union[_azure_pb2.AzureSnapshotProps, _Mapping]] = ..., cohesity_cp_copy_mode: _Optional[_Union[SnapshotInfo.CohesityCpCopyMode, str]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ()
    UDA_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    uda_restore_info: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("recover_task_state", "progress_percent", "error", "stats", "process_info", "pulse_log_index", "warnings", "task_id", "page", "cancel_job_retry_current_count", "mountpoint_map", "log_mountpoint_map", "control_node", "view_vips", "cloned_view_id", "cloned_log_view_id", "job_status_retry_count", "bifrost_constituent_id", "heimdall_disk_request_id", "heimdall_disk_mountpoint", "abort")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreEntityInfo.State]
        kClonedFullBackupView: _ClassVar[RestoreEntityInfo.State]
        kClonedLogBackupView: _ClassVar[RestoreEntityInfo.State]
        kMountedFullBackupView: _ClassVar[RestoreEntityInfo.State]
        kMountedLogBackupView: _ClassVar[RestoreEntityInfo.State]
        kPermitGranted: _ClassVar[RestoreEntityInfo.State]
        kEntitiesSubmitted: _ClassVar[RestoreEntityInfo.State]
        kRestoreJobSubmitted: _ClassVar[RestoreEntityInfo.State]
        kRestoreJobCompletedOrCanceled: _ClassVar[RestoreEntityInfo.State]
        kRestoreJobDetailsFetched: _ClassVar[RestoreEntityInfo.State]
        kUnmountedFullBackupView: _ClassVar[RestoreEntityInfo.State]
        kUnmountedLogBackupView: _ClassVar[RestoreEntityInfo.State]
        kFullBackupViewDeleted: _ClassVar[RestoreEntityInfo.State]
        kLogBackupViewDeleted: _ClassVar[RestoreEntityInfo.State]
        kFinished: _ClassVar[RestoreEntityInfo.State]
        kCancelJob: _ClassVar[RestoreEntityInfo.State]
        kGotAllEndPoints: _ClassVar[RestoreEntityInfo.State]
        kMaybeExternalDiskAdded: _ClassVar[RestoreEntityInfo.State]
        kMaybeExternalDiskRemoved: _ClassVar[RestoreEntityInfo.State]
    kStarted: RestoreEntityInfo.State
    kClonedFullBackupView: RestoreEntityInfo.State
    kClonedLogBackupView: RestoreEntityInfo.State
    kMountedFullBackupView: RestoreEntityInfo.State
    kMountedLogBackupView: RestoreEntityInfo.State
    kPermitGranted: RestoreEntityInfo.State
    kEntitiesSubmitted: RestoreEntityInfo.State
    kRestoreJobSubmitted: RestoreEntityInfo.State
    kRestoreJobCompletedOrCanceled: RestoreEntityInfo.State
    kRestoreJobDetailsFetched: RestoreEntityInfo.State
    kUnmountedFullBackupView: RestoreEntityInfo.State
    kUnmountedLogBackupView: RestoreEntityInfo.State
    kFullBackupViewDeleted: RestoreEntityInfo.State
    kLogBackupViewDeleted: RestoreEntityInfo.State
    kFinished: RestoreEntityInfo.State
    kCancelJob: RestoreEntityInfo.State
    kGotAllEndPoints: RestoreEntityInfo.State
    kMaybeExternalDiskAdded: RestoreEntityInfo.State
    kMaybeExternalDiskRemoved: RestoreEntityInfo.State
    class MountpointMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MountedPathInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MountedPathInfo, _Mapping]] = ...) -> None: ...
    class LogMountpointMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MountedPathInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MountedPathInfo, _Mapping]] = ...) -> None: ...
    UDA_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    uda_restore_entity_info: _descriptor.FieldDescriptor
    RECOVER_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    PULSE_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_JOB_RETRY_CURRENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_MAP_FIELD_NUMBER: _ClassVar[int]
    LOG_MOUNTPOINT_MAP_FIELD_NUMBER: _ClassVar[int]
    CONTROL_NODE_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    CLONED_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CLONED_LOG_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEIMDALL_DISK_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HEIMDALL_DISK_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    recover_task_state: RestoreEntityInfo.State
    progress_percent: int
    error: _error_pb2.ErrorProto
    stats: _uda_pb2.UdaStats
    process_info: _uda_param_pb2.ProcessInfo
    pulse_log_index: int
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    task_id: int
    page: int
    cancel_job_retry_current_count: int
    mountpoint_map: _containers.MessageMap[str, MountedPathInfo]
    log_mountpoint_map: _containers.MessageMap[str, MountedPathInfo]
    control_node: str
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    cloned_view_id: int
    cloned_log_view_id: int
    job_status_retry_count: int
    bifrost_constituent_id: int
    heimdall_disk_request_id: str
    heimdall_disk_mountpoint: str
    abort: bool
    def __init__(self, recover_task_state: _Optional[_Union[RestoreEntityInfo.State, str]] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[_uda_pb2.UdaStats, _Mapping]] = ..., process_info: _Optional[_Union[_uda_param_pb2.ProcessInfo, _Mapping]] = ..., pulse_log_index: _Optional[int] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., task_id: _Optional[int] = ..., page: _Optional[int] = ..., cancel_job_retry_current_count: _Optional[int] = ..., mountpoint_map: _Optional[_Mapping[str, MountedPathInfo]] = ..., log_mountpoint_map: _Optional[_Mapping[str, MountedPathInfo]] = ..., control_node: _Optional[str] = ..., view_vips: _Optional[_Iterable[str]] = ..., cloned_view_id: _Optional[int] = ..., cloned_log_view_id: _Optional[int] = ..., job_status_retry_count: _Optional[int] = ..., bifrost_constituent_id: _Optional[int] = ..., heimdall_disk_request_id: _Optional[str] = ..., heimdall_disk_mountpoint: _Optional[str] = ..., abort: bool = ...) -> None: ...

class MountedPathInfo(_message.Message):
    __slots__ = ("mounted_path_vec", "view_vips")
    MOUNTED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_VIPS_FIELD_NUMBER: _ClassVar[int]
    mounted_path_vec: _containers.RepeatedScalarFieldContainer[str]
    view_vips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mounted_path_vec: _Optional[_Iterable[str]] = ..., view_vips: _Optional[_Iterable[str]] = ...) -> None: ...
