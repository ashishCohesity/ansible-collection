from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api import magneto_failover_pb2 as _magneto_failover_pb2
from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import policy_pb2 as _policy_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailoverVersionProto(_message.Message):
    __slots__ = ("version", "api_version")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    api_version: int
    def __init__(self, version: _Optional[int] = ..., api_version: _Optional[int] = ...) -> None: ...

class FailoverTransientStateProto(_message.Message):
    __slots__ = ("initiate_failover_rx", "finalize_failover_rx", "tx_failover_run", "finalize_status", "restore_tasks_status", "backup_runs_state")
    class InitiateFailoverRx(_message.Message):
        __slots__ = ("saved_job_description",)
        SAVED_JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        saved_job_description: _magneto_pb2.BackupJobProto
        def __init__(self, saved_job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ...) -> None: ...
    class FinalizeFailoverRx(_message.Message):
        __slots__ = ("policy_id", "new_protection_policy", "job_uid", "new_backup_job", "object_id_vec")
        POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        NEW_PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        NEW_BACKUP_JOB_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        policy_id: str
        new_protection_policy: _policy_pb2.ProtectionPolicyProto
        job_uid: _universal_id_pb2.UniversalIdProto
        new_backup_job: _magneto_pb2.BackupJobProto
        object_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, policy_id: _Optional[str] = ..., new_protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., new_backup_job: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class TxFailoverRun(_message.Message):
        __slots__ = ("status", "run_start_time_usecs", "backup_type", "cancel_non_failover_backups_and_replications", "pause_policy_based_runs", "protection_policy")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
            kJobPauseDone: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
            kNonFailoverBackupRunsDone: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
            kNonFailoverReplicationTasksDone: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
            kRunNowInvoked: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
            kRunStartTimePersisted: _ClassVar[FailoverTransientStateProto.TxFailoverRun.Status]
        kStarted: FailoverTransientStateProto.TxFailoverRun.Status
        kJobPauseDone: FailoverTransientStateProto.TxFailoverRun.Status
        kNonFailoverBackupRunsDone: FailoverTransientStateProto.TxFailoverRun.Status
        kNonFailoverReplicationTasksDone: FailoverTransientStateProto.TxFailoverRun.Status
        kRunNowInvoked: FailoverTransientStateProto.TxFailoverRun.Status
        kRunStartTimePersisted: FailoverTransientStateProto.TxFailoverRun.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        CANCEL_NON_FAILOVER_BACKUPS_AND_REPLICATIONS_FIELD_NUMBER: _ClassVar[int]
        PAUSE_POLICY_BASED_RUNS_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        status: FailoverTransientStateProto.TxFailoverRun.Status
        run_start_time_usecs: int
        backup_type: _enums_pb2.ScheduledBackupType.Type
        cancel_non_failover_backups_and_replications: bool
        pause_policy_based_runs: bool
        protection_policy: _policy_pb2.ProtectionPolicyProto
        def __init__(self, status: _Optional[_Union[FailoverTransientStateProto.TxFailoverRun.Status, str]] = ..., run_start_time_usecs: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., cancel_non_failover_backups_and_replications: bool = ..., pause_policy_based_runs: bool = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ...) -> None: ...
    class FinalizeFailoverStatus(_message.Message):
        __slots__ = ("tx_status", "rx_status")
        TX_STATUS_FIELD_NUMBER: _ClassVar[int]
        RX_STATUS_FIELD_NUMBER: _ClassVar[int]
        tx_status: _enums_pb2.PublicTaskStatus.Type
        rx_status: _enums_pb2.PublicTaskStatus.Type
        def __init__(self, tx_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., rx_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ...) -> None: ...
    class TenantFailoverRestoreTasksStatus(_message.Message):
        __slots__ = ("status", "error", "vault_cookie")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kInitialized: _ClassVar[FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status]
            kFinished: _ClassVar[FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status]
        kInitialized: FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status
        kFinished: FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        VAULT_COOKIE_FIELD_NUMBER: _ClassVar[int]
        status: FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status
        error: _error_pb2.ErrorProto
        vault_cookie: bytes
        def __init__(self, status: _Optional[_Union[FailoverTransientStateProto.TenantFailoverRestoreTasksStatus.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vault_cookie: _Optional[bytes] = ...) -> None: ...
    class TenantFailoverBackupRunsState(_message.Message):
        __slots__ = ("status", "error", "object_id_vec", "pending_archive_uid_map_deprecated", "pending_archive_uid_map", "fetch_archive_uids_cookie", "last_processed_object_id")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kInitialized: _ClassVar[FailoverTransientStateProto.TenantFailoverBackupRunsState.Status]
            kCalculatedObjects_deprecated: _ClassVar[FailoverTransientStateProto.TenantFailoverBackupRunsState.Status]
            kFinished: _ClassVar[FailoverTransientStateProto.TenantFailoverBackupRunsState.Status]
        kInitialized: FailoverTransientStateProto.TenantFailoverBackupRunsState.Status
        kCalculatedObjects_deprecated: FailoverTransientStateProto.TenantFailoverBackupRunsState.Status
        kFinished: FailoverTransientStateProto.TenantFailoverBackupRunsState.Status
        class PendingArchiveUidMapDeprecatedEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
        class ArchiveObjectInfo(_message.Message):
            __slots__ = ("object_id", "environment_type")
            OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            ENVIRONMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            object_id: int
            environment_type: _enums_pb2.Environment.Type
            def __init__(self, object_id: _Optional[int] = ..., environment_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...
        class PendingArchiveUidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: FailoverTransientStateProto.TenantFailoverBackupRunsState.ArchiveObjectInfo
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FailoverTransientStateProto.TenantFailoverBackupRunsState.ArchiveObjectInfo, _Mapping]] = ...) -> None: ...
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        PENDING_ARCHIVE_UID_MAP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        PENDING_ARCHIVE_UID_MAP_FIELD_NUMBER: _ClassVar[int]
        FETCH_ARCHIVE_UIDS_COOKIE_FIELD_NUMBER: _ClassVar[int]
        LAST_PROCESSED_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        status: FailoverTransientStateProto.TenantFailoverBackupRunsState.Status
        error: _error_pb2.ErrorProto
        object_id_vec: _containers.RepeatedScalarFieldContainer[int]
        pending_archive_uid_map_deprecated: _containers.ScalarMap[str, bool]
        pending_archive_uid_map: _containers.MessageMap[str, FailoverTransientStateProto.TenantFailoverBackupRunsState.ArchiveObjectInfo]
        fetch_archive_uids_cookie: str
        last_processed_object_id: int
        def __init__(self, status: _Optional[_Union[FailoverTransientStateProto.TenantFailoverBackupRunsState.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ..., pending_archive_uid_map_deprecated: _Optional[_Mapping[str, bool]] = ..., pending_archive_uid_map: _Optional[_Mapping[str, FailoverTransientStateProto.TenantFailoverBackupRunsState.ArchiveObjectInfo]] = ..., fetch_archive_uids_cookie: _Optional[str] = ..., last_processed_object_id: _Optional[int] = ...) -> None: ...
    INITIATE_FAILOVER_RX_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FAILOVER_RX_FIELD_NUMBER: _ClassVar[int]
    TX_FAILOVER_RUN_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASKS_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUNS_STATE_FIELD_NUMBER: _ClassVar[int]
    initiate_failover_rx: FailoverTransientStateProto.InitiateFailoverRx
    finalize_failover_rx: FailoverTransientStateProto.FinalizeFailoverRx
    tx_failover_run: FailoverTransientStateProto.TxFailoverRun
    finalize_status: FailoverTransientStateProto.FinalizeFailoverStatus
    restore_tasks_status: FailoverTransientStateProto.TenantFailoverRestoreTasksStatus
    backup_runs_state: FailoverTransientStateProto.TenantFailoverBackupRunsState
    def __init__(self, initiate_failover_rx: _Optional[_Union[FailoverTransientStateProto.InitiateFailoverRx, _Mapping]] = ..., finalize_failover_rx: _Optional[_Union[FailoverTransientStateProto.FinalizeFailoverRx, _Mapping]] = ..., tx_failover_run: _Optional[_Union[FailoverTransientStateProto.TxFailoverRun, _Mapping]] = ..., finalize_status: _Optional[_Union[FailoverTransientStateProto.FinalizeFailoverStatus, _Mapping]] = ..., restore_tasks_status: _Optional[_Union[FailoverTransientStateProto.TenantFailoverRestoreTasksStatus, _Mapping]] = ..., backup_runs_state: _Optional[_Union[FailoverTransientStateProto.TenantFailoverBackupRunsState, _Mapping]] = ...) -> None: ...

class FailoverCommandArg(_message.Message):
    __slots__ = ("schedule", "poll", "finalize", "cancel", "orchestrator_params")
    class OrchestratorParams(_message.Message):
        __slots__ = ("failover_unique_id", "orchestrator_identifier", "tx_view_id", "rx_tx_entity_id_map", "tx_job_uid", "failover_cmd_orchestrator_params", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id")
        class RxTxEntityIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        ORCHESTRATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        TX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        RX_TX_ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        TX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        FAILOVER_CMD_ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        failover_unique_id: str
        orchestrator_identifier: str
        tx_view_id: int
        rx_tx_entity_id_map: _containers.ScalarMap[int, int]
        tx_job_uid: _universal_id_pb2.UniversalIdProto
        failover_cmd_orchestrator_params: bytes
        tx_cluster_id: int
        tx_cluster_incarnation_id: int
        rx_cluster_id: int
        rx_cluster_incarnation_id: int
        def __init__(self, failover_unique_id: _Optional[str] = ..., orchestrator_identifier: _Optional[str] = ..., tx_view_id: _Optional[int] = ..., rx_tx_entity_id_map: _Optional[_Mapping[int, int]] = ..., tx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., failover_cmd_orchestrator_params: _Optional[bytes] = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ...) -> None: ...
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    POLL_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    schedule: _magneto_failover_pb2.ScheduleFailoverBackupAndReplicationArg
    poll: _magneto_failover_pb2.PollScheduledFailoverBackupAndReplicationArg
    finalize: _magneto_failover_pb2.FinalizeFailoverTxArg
    cancel: _magneto_failover_pb2.CancelFailoverArg
    orchestrator_params: FailoverCommandArg.OrchestratorParams
    def __init__(self, schedule: _Optional[_Union[_magneto_failover_pb2.ScheduleFailoverBackupAndReplicationArg, _Mapping]] = ..., poll: _Optional[_Union[_magneto_failover_pb2.PollScheduledFailoverBackupAndReplicationArg, _Mapping]] = ..., finalize: _Optional[_Union[_magneto_failover_pb2.FinalizeFailoverTxArg, _Mapping]] = ..., cancel: _Optional[_Union[_magneto_failover_pb2.CancelFailoverArg, _Mapping]] = ..., orchestrator_params: _Optional[_Union[FailoverCommandArg.OrchestratorParams, _Mapping]] = ...) -> None: ...

class FailoverCommandResult(_message.Message):
    __slots__ = ("schedule", "poll", "finalize", "cancel")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    POLL_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    schedule: _magneto_failover_pb2.ScheduleFailoverBackupAndReplicationResult
    poll: _magneto_failover_pb2.PollScheduledFailoverBackupAndReplicationResult
    finalize: _magneto_failover_pb2.FinalizeFailoverTxResult
    cancel: _magneto_failover_pb2.CancelFailoverResult
    def __init__(self, schedule: _Optional[_Union[_magneto_failover_pb2.ScheduleFailoverBackupAndReplicationResult, _Mapping]] = ..., poll: _Optional[_Union[_magneto_failover_pb2.PollScheduledFailoverBackupAndReplicationResult, _Mapping]] = ..., finalize: _Optional[_Union[_magneto_failover_pb2.FinalizeFailoverTxResult, _Mapping]] = ..., cancel: _Optional[_Union[_magneto_failover_pb2.CancelFailoverResult, _Mapping]] = ...) -> None: ...

class FailoverStateProto(_message.Message):
    __slots__ = ("failover_unique_id", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "view_id", "entity_id_vec", "tx_job_uid", "rx_job_uid", "rx_active_job_uid", "status", "tx_state", "failover_command", "orchestrator_identifier", "tx_view_id", "rx_tx_entity_id_map", "tenant_failover_state", "user_info", "creation_time_usecs", "last_update_time_usecs", "auto_terminated", "num_successful_schedule_rpcs", "replication_stats_vec", "transient_state")
    class TxState(_message.Message):
        __slots__ = ("job_paused_before_first_scheduled_run", "backup_run_start_time_usecs_vec", "error")
        JOB_PAUSED_BEFORE_FIRST_SCHEDULED_RUN_FIELD_NUMBER: _ClassVar[int]
        BACKUP_RUN_START_TIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        job_paused_before_first_scheduled_run: bool
        backup_run_start_time_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
        error: _error_pb2.ErrorProto
        def __init__(self, job_paused_before_first_scheduled_run: bool = ..., backup_run_start_time_usecs_vec: _Optional[_Iterable[int]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class FailoverCommand(_message.Message):
        __slots__ = ("arg", "result")
        ARG_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        arg: FailoverCommandArg
        result: FailoverCommandResult
        def __init__(self, arg: _Optional[_Union[FailoverCommandArg, _Mapping]] = ..., result: _Optional[_Union[FailoverCommandResult, _Mapping]] = ...) -> None: ...
    class RxTxEntityIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class TenantFailoverState(_message.Message):
        __slots__ = ("status", "error", "retrieved_restore_tasks", "retrieved_backup_runs", "cancellation_requested")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[FailoverStateProto.TenantFailoverState.Status]
            kFinished: _ClassVar[FailoverStateProto.TenantFailoverState.Status]
        kStarted: FailoverStateProto.TenantFailoverState.Status
        kFinished: FailoverStateProto.TenantFailoverState.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        RETRIEVED_RESTORE_TASKS_FIELD_NUMBER: _ClassVar[int]
        RETRIEVED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        status: FailoverStateProto.TenantFailoverState.Status
        error: _error_pb2.ErrorProto
        retrieved_restore_tasks: bool
        retrieved_backup_runs: bool
        cancellation_requested: bool
        def __init__(self, status: _Optional[_Union[FailoverStateProto.TenantFailoverState.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., retrieved_restore_tasks: bool = ..., retrieved_backup_runs: bool = ..., cancellation_requested: bool = ...) -> None: ...
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RX_ACTIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TX_STATE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    RX_TX_ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    TENANT_FAILOVER_STATE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    AUTO_TERMINATED_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_SCHEDULE_RPCS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    failover_unique_id: str
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    view_id: int
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    tx_job_uid: _universal_id_pb2.UniversalIdProto
    rx_job_uid: _universal_id_pb2.UniversalIdProto
    rx_active_job_uid: _universal_id_pb2.UniversalIdProto
    status: _enums_pb2.PublicTaskStatus.Type
    tx_state: FailoverStateProto.TxState
    failover_command: FailoverStateProto.FailoverCommand
    orchestrator_identifier: str
    tx_view_id: int
    rx_tx_entity_id_map: _containers.ScalarMap[int, int]
    tenant_failover_state: FailoverStateProto.TenantFailoverState
    user_info: _permissions_external_pb2.UserInformationProto
    creation_time_usecs: int
    last_update_time_usecs: int
    auto_terminated: bool
    num_successful_schedule_rpcs: int
    replication_stats_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
    transient_state: FailoverTransientStateProto
    def __init__(self, failover_unique_id: _Optional[str] = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., view_id: _Optional[int] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., tx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_active_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., tx_state: _Optional[_Union[FailoverStateProto.TxState, _Mapping]] = ..., failover_command: _Optional[_Union[FailoverStateProto.FailoverCommand, _Mapping]] = ..., orchestrator_identifier: _Optional[str] = ..., tx_view_id: _Optional[int] = ..., rx_tx_entity_id_map: _Optional[_Mapping[int, int]] = ..., tenant_failover_state: _Optional[_Union[FailoverStateProto.TenantFailoverState, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ..., auto_terminated: bool = ..., num_successful_schedule_rpcs: _Optional[int] = ..., replication_stats_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ..., transient_state: _Optional[_Union[FailoverTransientStateProto, _Mapping]] = ...) -> None: ...
