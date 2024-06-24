from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api import magneto_external_objects_pb2 as _magneto_external_objects_pb2
from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateFailoverRxArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "tx_cluster_id", "tx_cluster_incarnation_id", "replica_view_id", "rx_magneto_entity_id_vec", "rx_job_uid", "orchestrator_identifier", "job_environment")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    RX_MAGNETO_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    JOB_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    replica_view_id: int
    rx_magneto_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    rx_job_uid: _universal_id_pb2.UniversalIdProto
    orchestrator_identifier: str
    job_environment: _enum_wrappers_pb2.EnvironmentProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., replica_view_id: _Optional[int] = ..., rx_magneto_entity_id_vec: _Optional[_Iterable[int]] = ..., rx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., orchestrator_identifier: _Optional[str] = ..., job_environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ...) -> None: ...

class InitiateFailoverRxResult(_message.Message):
    __slots__ = ("base", "tx_view_id", "rx_tx_entity_id_map", "tx_active_job_uid", "in_terminal_state", "entity_provenance_lookup_error")
    class RxTxEntityIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    RX_TX_ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    TX_ACTIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    IN_TERMINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROVENANCE_LOOKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    tx_view_id: int
    rx_tx_entity_id_map: _containers.ScalarMap[int, int]
    tx_active_job_uid: _universal_id_pb2.UniversalIdProto
    in_terminal_state: bool
    entity_provenance_lookup_error: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., tx_view_id: _Optional[int] = ..., rx_tx_entity_id_map: _Optional[_Mapping[int, int]] = ..., tx_active_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., in_terminal_state: bool = ..., entity_provenance_lookup_error: bool = ...) -> None: ...

class ScheduleFailoverBackupAndReplicationArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "rx_cluster_id", "rx_cluster_incarnation_id", "tx_view_id", "tx_magneto_entity_id_vec", "tx_active_job_uid", "backup_type", "cancel_non_failover_backups_and_replications", "pause_policy_based_runs", "failover_cmd_orchestrator_params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    TX_MAGNETO_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TX_ACTIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_NON_FAILOVER_BACKUPS_AND_REPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_POLICY_BASED_RUNS_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CMD_ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    tx_view_id: int
    tx_magneto_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    tx_active_job_uid: _universal_id_pb2.UniversalIdProto
    backup_type: _enum_wrappers_pb2.MagnetoBackupType
    cancel_non_failover_backups_and_replications: bool
    pause_policy_based_runs: bool
    failover_cmd_orchestrator_params: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., tx_view_id: _Optional[int] = ..., tx_magneto_entity_id_vec: _Optional[_Iterable[int]] = ..., tx_active_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., cancel_non_failover_backups_and_replications: bool = ..., pause_policy_based_runs: bool = ..., failover_cmd_orchestrator_params: _Optional[bytes] = ...) -> None: ...

class ScheduleFailoverBackupAndReplicationResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class PollScheduledFailoverBackupAndReplicationArg(_message.Message):
    __slots__ = ("base", "failover_unique_id_vec", "failover_cmd_orchestrator_params", "fetch_additional_runs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CMD_ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FETCH_ADDITIONAL_RUNS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id_vec: _containers.RepeatedScalarFieldContainer[str]
    failover_cmd_orchestrator_params: bytes
    fetch_additional_runs: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id_vec: _Optional[_Iterable[str]] = ..., failover_cmd_orchestrator_params: _Optional[bytes] = ..., fetch_additional_runs: bool = ...) -> None: ...

class PollScheduledFailoverBackupAndReplicationResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("failover_unique_id", "error", "cancellations_pending", "latest_protection_group_run", "latest_scheduled_protection_run_pending", "finished_protection_group_run_vec")
        FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CANCELLATIONS_PENDING_FIELD_NUMBER: _ClassVar[int]
        LATEST_PROTECTION_GROUP_RUN_FIELD_NUMBER: _ClassVar[int]
        LATEST_SCHEDULED_PROTECTION_RUN_PENDING_FIELD_NUMBER: _ClassVar[int]
        FINISHED_PROTECTION_GROUP_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
        failover_unique_id: str
        error: _magneto_external_base_pb2.ErrorProto
        cancellations_pending: bool
        latest_protection_group_run: _magneto_external_objects_pb2.ProtectionGroupRunInfo
        latest_scheduled_protection_run_pending: bool
        finished_protection_group_run_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_objects_pb2.ProtectionGroupRunInfo]
        def __init__(self, failover_unique_id: _Optional[str] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., cancellations_pending: bool = ..., latest_protection_group_run: _Optional[_Union[_magneto_external_objects_pb2.ProtectionGroupRunInfo, _Mapping]] = ..., latest_scheduled_protection_run_pending: bool = ..., finished_protection_group_run_vec: _Optional[_Iterable[_Union[_magneto_external_objects_pb2.ProtectionGroupRunInfo, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[PollScheduledFailoverBackupAndReplicationResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[PollScheduledFailoverBackupAndReplicationResult.Result, _Mapping]]] = ...) -> None: ...

class FinalizeFailoverTxArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "rx_cluster_id", "rx_cluster_incarnation_id", "tx_view_id", "tx_magneto_entity_id_vec", "tx_active_job_uid", "keep_tx_job_active", "failover_cmd_orchestrator_params", "remove_entity_from_all_jobs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    TX_MAGNETO_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TX_ACTIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    KEEP_TX_JOB_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CMD_ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ENTITY_FROM_ALL_JOBS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    tx_view_id: int
    tx_magneto_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    tx_active_job_uid: _universal_id_pb2.UniversalIdProto
    keep_tx_job_active: bool
    failover_cmd_orchestrator_params: bytes
    remove_entity_from_all_jobs: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., tx_view_id: _Optional[int] = ..., tx_magneto_entity_id_vec: _Optional[_Iterable[int]] = ..., tx_active_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., keep_tx_job_active: bool = ..., failover_cmd_orchestrator_params: _Optional[bytes] = ..., remove_entity_from_all_jobs: bool = ...) -> None: ...

class FinalizeFailoverTxResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class LinkFailedOverEntitiesArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "source_target_entity_id_map")
    class SourceTargetEntityIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TARGET_ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    source_target_entity_id_map: _containers.ScalarMap[int, int]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., source_target_entity_id_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class LinkFailedOverEntitiesResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class FinalizeFailoverRxArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "do_not_protect", "entity_id_vec", "rx_job_uid", "enable_reverse_replication", "create_object_backup", "rx_failover_policy_id", "rx_failover_environment")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_PROTECT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REVERSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_OBJECT_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RX_FAILOVER_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    RX_FAILOVER_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    do_not_protect: bool
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    rx_job_uid: _universal_id_pb2.UniversalIdProto
    enable_reverse_replication: bool
    create_object_backup: bool
    rx_failover_policy_id: str
    rx_failover_environment: _enum_wrappers_pb2.EnvironmentProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., do_not_protect: bool = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., rx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., enable_reverse_replication: bool = ..., create_object_backup: bool = ..., rx_failover_policy_id: _Optional[str] = ..., rx_failover_environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ...) -> None: ...

class FinalizeFailoverRxResult(_message.Message):
    __slots__ = ("base", "rx_job_uid", "enable_reverse_replication_error", "entity_id_vec", "object_error_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REVERSE_REPLICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    rx_job_uid: _universal_id_pb2.UniversalIdProto
    enable_reverse_replication_error: _magneto_external_base_pb2.ErrorProto
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    object_error_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ErrorProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., rx_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., enable_reverse_replication_error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., object_error_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class CancelFailoverArg(_message.Message):
    __slots__ = ("base", "failover_unique_id", "cancel_tx_failover", "failover_cmd_orchestrator_params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TX_FAILOVER_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CMD_ORCHESTRATOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_unique_id: str
    cancel_tx_failover: bool
    failover_cmd_orchestrator_params: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_unique_id: _Optional[str] = ..., cancel_tx_failover: bool = ..., failover_cmd_orchestrator_params: _Optional[bytes] = ...) -> None: ...

class CancelFailoverResult(_message.Message):
    __slots__ = ("base", "cancelled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    cancelled: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., cancelled: bool = ...) -> None: ...

class LookupFailoversArg(_message.Message):
    __slots__ = ("base", "failover_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    failover_uid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., failover_uid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class LookupFailoversResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("failover_uid", "replication_stats_vec")
        FAILOVER_UID_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
        failover_uid: str
        replication_stats_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
        def __init__(self, failover_uid: _Optional[str] = ..., replication_stats_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[LookupFailoversResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[LookupFailoversResult.Result, _Mapping]]] = ...) -> None: ...

class InitiateTenantFailoverArg(_message.Message):
    __slots__ = ("base", "migration_uid", "user_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    migration_uid: str
    user_info: _permissions_external_pb2.UserInformationProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., migration_uid: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ...) -> None: ...

class InitiateTenantFailoverResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class InitiateSnapshotMigrationArg(_message.Message):
    __slots__ = ("base", "migration_uid", "user_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    migration_uid: str
    user_info: _permissions_external_pb2.UserInformationProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., migration_uid: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ...) -> None: ...

class InitiateSnapshotMigrationResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class FetchCloudSnapshotDoneArg(_message.Message):
    __slots__ = ("base", "migration_uid", "error", "archive_uid", "user_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    migration_uid: str
    error: _magneto_external_base_pb2.ErrorProto
    archive_uid: _universal_id_pb2.UniversalIdProto
    user_info: _permissions_external_pb2.UserInformationProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., migration_uid: _Optional[str] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ...) -> None: ...

class FetchCloudSnapshotDoneResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class FinalizeTenantFailoverArg(_message.Message):
    __slots__ = ("base", "migration_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    migration_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class FinalizeTenantFailoverResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class CancelTenantFailoverArg(_message.Message):
    __slots__ = ("base", "migration_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    migration_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class CancelTenantFailoverResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class CleanupTenantDataArg(_message.Message):
    __slots__ = ("base", "user_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    user_info: _permissions_external_pb2.UserInformationProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ...) -> None: ...

class CleanupTenantDataResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...
