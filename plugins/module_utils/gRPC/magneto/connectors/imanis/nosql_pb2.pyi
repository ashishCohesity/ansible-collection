from atom.base import event_pb2 as _event_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.master.stub import stub_pb2 as _stub_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("live_view_name", "job_instance_id", "attempt_num", "progress_percent", "error", "stats", "task_id", "nosql_cdp_service_state", "cdp_logs_info_path", "job_end_time_usecs", "should_populate_cdp_logs", "snapshot_start_time_usecs", "successful_entities", "fetched_successful_entities", "backup_task_state")
    class BackupTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.BackupTaskState]
        kCheckImanisVersion: _ClassVar[SnapshotInfo.BackupTaskState]
        kUpdateNosqlCdpService: _ClassVar[SnapshotInfo.BackupTaskState]
        kMaybeCancelPreviousBackupJob: _ClassVar[SnapshotInfo.BackupTaskState]
        kMaybeDeleteLiveView: _ClassVar[SnapshotInfo.BackupTaskState]
        kClonePreviousSnapshot: _ClassVar[SnapshotInfo.BackupTaskState]
        kCreateView: _ClassVar[SnapshotInfo.BackupTaskState]
        kMaybeFlushCdpLogs: _ClassVar[SnapshotInfo.BackupTaskState]
        kGetViewIdAndSendEntities: _ClassVar[SnapshotInfo.BackupTaskState]
        kWaitForJobCompletion: _ClassVar[SnapshotInfo.BackupTaskState]
        kGetCompletedJobDetails: _ClassVar[SnapshotInfo.BackupTaskState]
        kDeleteTrashDir: _ClassVar[SnapshotInfo.BackupTaskState]
        kCloneView: _ClassVar[SnapshotInfo.BackupTaskState]
        kWaitForCancelCompletion: _ClassVar[SnapshotInfo.BackupTaskState]
        kFinalizeCancellation: _ClassVar[SnapshotInfo.BackupTaskState]
    kStarted: SnapshotInfo.BackupTaskState
    kCheckImanisVersion: SnapshotInfo.BackupTaskState
    kUpdateNosqlCdpService: SnapshotInfo.BackupTaskState
    kMaybeCancelPreviousBackupJob: SnapshotInfo.BackupTaskState
    kMaybeDeleteLiveView: SnapshotInfo.BackupTaskState
    kClonePreviousSnapshot: SnapshotInfo.BackupTaskState
    kCreateView: SnapshotInfo.BackupTaskState
    kMaybeFlushCdpLogs: SnapshotInfo.BackupTaskState
    kGetViewIdAndSendEntities: SnapshotInfo.BackupTaskState
    kWaitForJobCompletion: SnapshotInfo.BackupTaskState
    kGetCompletedJobDetails: SnapshotInfo.BackupTaskState
    kDeleteTrashDir: SnapshotInfo.BackupTaskState
    kCloneView: SnapshotInfo.BackupTaskState
    kWaitForCancelCompletion: SnapshotInfo.BackupTaskState
    kFinalizeCancellation: SnapshotInfo.BackupTaskState
    NOSQL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    nosql_snapshot_info: _descriptor.FieldDescriptor
    LIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOSQL_CDP_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    CDP_LOGS_INFO_PATH_FIELD_NUMBER: _ClassVar[int]
    JOB_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_CDP_LOGS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    FETCHED_SUCCESSFUL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    live_view_name: str
    job_instance_id: int
    attempt_num: int
    progress_percent: int
    error: _error_pb2.ErrorProto
    stats: _nosql_pb2.NoSqlStats
    task_id: int
    nosql_cdp_service_state: UpdateNosqlCdpServiceOpState
    cdp_logs_info_path: str
    job_end_time_usecs: int
    should_populate_cdp_logs: bool
    snapshot_start_time_usecs: int
    successful_entities: _containers.RepeatedScalarFieldContainer[int]
    fetched_successful_entities: bool
    backup_task_state: SnapshotInfo.BackupTaskState
    def __init__(self, live_view_name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[_nosql_pb2.NoSqlStats, _Mapping]] = ..., task_id: _Optional[int] = ..., nosql_cdp_service_state: _Optional[_Union[UpdateNosqlCdpServiceOpState, _Mapping]] = ..., cdp_logs_info_path: _Optional[str] = ..., job_end_time_usecs: _Optional[int] = ..., should_populate_cdp_logs: bool = ..., snapshot_start_time_usecs: _Optional[int] = ..., successful_entities: _Optional[_Iterable[int]] = ..., fetched_successful_entities: bool = ..., backup_task_state: _Optional[_Union[SnapshotInfo.BackupTaskState, str]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("subsequent_restore_task_ids",)
    NOSQL_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    nosql_restore_info: _descriptor.FieldDescriptor
    SUBSEQUENT_RESTORE_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    subsequent_restore_task_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, subsequent_restore_task_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("recover_task_state", "progress_percent", "error", "stats")
    class RecoverTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kViewCloned: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kSecondaryViewCloned: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kCDPFilesCloned: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kPermitGranted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kEntitiesSubmitted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kRestoreJobSubmitted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kRestoreJobCompleted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kDeleteSecondaryView: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kDeleteView: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kFinished: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kCancelJob: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kCloneLogRestoreView: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kDeleteLogRestoreView: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kFinaliseRestore: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kFinaliseRestoreJobSubmitted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kFinaliseRestoreJobCompleted: _ClassVar[RestoreEntityInfo.RecoverTaskState]
        kViewMetadataFetched: _ClassVar[RestoreEntityInfo.RecoverTaskState]
    kStarted: RestoreEntityInfo.RecoverTaskState
    kViewCloned: RestoreEntityInfo.RecoverTaskState
    kSecondaryViewCloned: RestoreEntityInfo.RecoverTaskState
    kCDPFilesCloned: RestoreEntityInfo.RecoverTaskState
    kPermitGranted: RestoreEntityInfo.RecoverTaskState
    kEntitiesSubmitted: RestoreEntityInfo.RecoverTaskState
    kRestoreJobSubmitted: RestoreEntityInfo.RecoverTaskState
    kRestoreJobCompleted: RestoreEntityInfo.RecoverTaskState
    kDeleteSecondaryView: RestoreEntityInfo.RecoverTaskState
    kDeleteView: RestoreEntityInfo.RecoverTaskState
    kFinished: RestoreEntityInfo.RecoverTaskState
    kCancelJob: RestoreEntityInfo.RecoverTaskState
    kCloneLogRestoreView: RestoreEntityInfo.RecoverTaskState
    kDeleteLogRestoreView: RestoreEntityInfo.RecoverTaskState
    kFinaliseRestore: RestoreEntityInfo.RecoverTaskState
    kFinaliseRestoreJobSubmitted: RestoreEntityInfo.RecoverTaskState
    kFinaliseRestoreJobCompleted: RestoreEntityInfo.RecoverTaskState
    kViewMetadataFetched: RestoreEntityInfo.RecoverTaskState
    NOSQL_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    nosql_restore_entity_info: _descriptor.FieldDescriptor
    RECOVER_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    recover_task_state: RestoreEntityInfo.RecoverTaskState
    progress_percent: int
    error: _error_pb2.ErrorProto
    stats: _nosql_pb2.NoSqlStats
    def __init__(self, recover_task_state: _Optional[_Union[RestoreEntityInfo.RecoverTaskState, str]] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[_nosql_pb2.NoSqlStats, _Mapping]] = ...) -> None: ...

class UpdateNoSqlBackupTaskResult(_message.Message):
    __slots__ = ("protected_entity_logs_vec", "start_sequencer", "end_sequencer")
    class ProtectedEntityLog(_message.Message):
        __slots__ = ("entity_id", "log_data_vec")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        log_data_vec: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.NoSqlLogData]
        def __init__(self, entity_id: _Optional[int] = ..., log_data_vec: _Optional[_Iterable[_Union[_nosql_pb2.NoSqlLogData, _Mapping]]] = ...) -> None: ...
    UPDATE_NOSQL_BACKUP_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    update_nosql_backup_task_result: _descriptor.FieldDescriptor
    PROTECTED_ENTITY_LOGS_VEC_FIELD_NUMBER: _ClassVar[int]
    START_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    END_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    protected_entity_logs_vec: _containers.RepeatedCompositeFieldContainer[UpdateNoSqlBackupTaskResult.ProtectedEntityLog]
    start_sequencer: _event_pb2.Sequencer
    end_sequencer: _event_pb2.Sequencer
    def __init__(self, protected_entity_logs_vec: _Optional[_Iterable[_Union[UpdateNoSqlBackupTaskResult.ProtectedEntityLog, _Mapping]]] = ..., start_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ...) -> None: ...

class UpdateNosqlCdpServiceOpState(_message.Message):
    __slots__ = ("cdp_task_id", "backup_job_instance_id", "state", "cdp_dir_created_entities_vec", "metadata_updated_entities_vec", "error")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kViewCreated: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kDirectoriesCreated: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kEntityMetadataUpdated: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kSendEntitiesDone: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kUpdateCdpServiceTriggered: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kNosqlCdpServiceUpdated: _ClassVar[UpdateNosqlCdpServiceOpState.State]
        kDisabledCdpInAtomForDroppedEntities: _ClassVar[UpdateNosqlCdpServiceOpState.State]
    kNotStarted: UpdateNosqlCdpServiceOpState.State
    kViewCreated: UpdateNosqlCdpServiceOpState.State
    kDirectoriesCreated: UpdateNosqlCdpServiceOpState.State
    kEntityMetadataUpdated: UpdateNosqlCdpServiceOpState.State
    kSendEntitiesDone: UpdateNosqlCdpServiceOpState.State
    kUpdateCdpServiceTriggered: UpdateNosqlCdpServiceOpState.State
    kNosqlCdpServiceUpdated: UpdateNosqlCdpServiceOpState.State
    kDisabledCdpInAtomForDroppedEntities: UpdateNosqlCdpServiceOpState.State
    CDP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CDP_DIR_CREATED_ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_UPDATED_ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    cdp_task_id: int
    backup_job_instance_id: int
    state: UpdateNosqlCdpServiceOpState.State
    cdp_dir_created_entities_vec: _containers.RepeatedScalarFieldContainer[int]
    metadata_updated_entities_vec: _containers.RepeatedScalarFieldContainer[int]
    error: _error_pb2.ErrorProto
    def __init__(self, cdp_task_id: _Optional[int] = ..., backup_job_instance_id: _Optional[int] = ..., state: _Optional[_Union[UpdateNosqlCdpServiceOpState.State, str]] = ..., cdp_dir_created_entities_vec: _Optional[_Iterable[int]] = ..., metadata_updated_entities_vec: _Optional[_Iterable[int]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
