from atom.base import entity_pb2 as _entity_pb2
from atom.base import event_pb2 as _event_pb2
from bookkeeper.base import bookkeeper_pb2 as _bookkeeper_pb2
from bridge.base import error_pb2 as _error_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.api.common import entity_operations_pb2 as _entity_operations_pb2
from magneto.api import object_protection_pb2 as _object_protection_pb2
from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import entity_pb2 as _entity_pb2_1
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.base import gatekeeper_pb2 as _gatekeeper_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.master.base import backup_job_data_pb2 as _backup_job_data_pb2
from magneto.master.base import enums_pb2 as _enums_pb2_1
from magneto.master.base import master_pb2 as _master_pb2
from magneto.master.base import master_cdp_pb2 as _master_cdp_pb2
from magneto.master.base import master_standby_pb2 as _master_standby_pb2
from magneto.master.entity_provenance import entity_provenance_pb2 as _entity_provenance_pb2
from magneto.master.artifact_garbage_collector import artifact_garbage_collector_pb2 as _artifact_garbage_collector_pb2
from stats.base import stats_pb2 as _stats_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookKeeperMetadataProto(_message.Message):
    __slots__ = ("group_id", "group_created", "user_info", "last_added_run_start_time_usecs", "job_name", "consumer_type")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CREATED_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_ADDED_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_created: bool
    user_info: _permissions_pb2.UserInformation
    last_added_run_start_time_usecs: int
    job_name: str
    consumer_type: _bookkeeper_pb2.ConsumerProto.Type
    def __init__(self, group_id: _Optional[int] = ..., group_created: bool = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., last_added_run_start_time_usecs: _Optional[int] = ..., job_name: _Optional[str] = ..., consumer_type: _Optional[_Union[_bookkeeper_pb2.ConsumerProto.Type, str]] = ...) -> None: ...

class ScribeKeyVec(_message.Message):
    __slots__ = ("key_vec",)
    KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    key_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupRunRange(_message.Message):
    __slots__ = ("first_run_start_time_usecs", "last_run_start_time_usecs")
    FIRST_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    first_run_start_time_usecs: int
    last_run_start_time_usecs: int
    def __init__(self, first_run_start_time_usecs: _Optional[int] = ..., last_run_start_time_usecs: _Optional[int] = ...) -> None: ...

class EntityJobMetadataInfo(_message.Message):
    __slots__ = ("job_uid", "run_range_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_range_vec: _containers.RepeatedCompositeFieldContainer[BackupRunRange]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_range_vec: _Optional[_Iterable[_Union[BackupRunRange, _Mapping]]] = ...) -> None: ...

class EntityBackupMetadata(_message.Message):
    __slots__ = ("entity_id", "job_info_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    job_info_vec: _containers.RepeatedCompositeFieldContainer[EntityJobMetadataInfo]
    def __init__(self, entity_id: _Optional[int] = ..., job_info_vec: _Optional[_Iterable[_Union[EntityJobMetadataInfo, _Mapping]]] = ...) -> None: ...

class ObjectBackupPersistentStateProto(_message.Message):
    __slots__ = ("env_specific_backup_params", "common_backup_params", "object_backup_specifications")
    ENV_SPECIFIC_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_BACKUP_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    env_specific_backup_params: _containers.RepeatedCompositeFieldContainer[_object_protection_pb2.EnvSpecificBackupParamsProto]
    common_backup_params: _containers.RepeatedCompositeFieldContainer[_object_protection_pb2.CommonBackupParamsProto]
    object_backup_specifications: _containers.RepeatedCompositeFieldContainer[_object_protection_pb2.ObjectBackupSpecificationProto]
    def __init__(self, env_specific_backup_params: _Optional[_Iterable[_Union[_object_protection_pb2.EnvSpecificBackupParamsProto, _Mapping]]] = ..., common_backup_params: _Optional[_Iterable[_Union[_object_protection_pb2.CommonBackupParamsProto, _Mapping]]] = ..., object_backup_specifications: _Optional[_Iterable[_Union[_object_protection_pb2.ObjectBackupSpecificationProto, _Mapping]]] = ...) -> None: ...

class MigratedRestoreTasksInfo(_message.Message):
    __slots__ = ("migration_uid", "restore_task_id_remapping_vec", "should_purge")
    class RemappingInfo(_message.Message):
        __slots__ = ("old_restore_task_uid", "new_restore_task_id")
        OLD_RESTORE_TASK_UID_FIELD_NUMBER: _ClassVar[int]
        NEW_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        old_restore_task_uid: _universal_id_pb2.UniversalIdProto
        new_restore_task_id: int
        def __init__(self, old_restore_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., new_restore_task_id: _Optional[int] = ...) -> None: ...
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_REMAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_PURGE_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    restore_task_id_remapping_vec: _containers.RepeatedCompositeFieldContainer[MigratedRestoreTasksInfo.RemappingInfo]
    should_purge: bool
    def __init__(self, migration_uid: _Optional[str] = ..., restore_task_id_remapping_vec: _Optional[_Iterable[_Union[MigratedRestoreTasksInfo.RemappingInfo, _Mapping]]] = ..., should_purge: bool = ...) -> None: ...

class PersistentStateProto(_message.Message):
    __slots__ = ("api_version", "persistent_state_proto_vec", "passwords_encrypted", "protection_policies", "global_protection_policies", "replicated_policies", "backup_jobs", "old_backup_jobs", "job_task_state", "finished_backup_runs", "finished_runs_scribe_keys_vec", "migrated_finished_run_shell_proto_vec", "missed_backup_runs", "garbage_collected_backup_runs", "gc_runs_scribe_keys_vec", "migrated_gc_run_shell_proto_vec", "checkpoint_capabilities", "serialized_finished_backup_runs", "serialized_gced_backup_runs", "serialized_finished_copy_runs", "is_run_predump_record", "ignored_delta_record_limit", "dirty_finished_runs_info_vec", "dirty_gced_runs_info_vec", "predump_action", "copy_run_wrapper_state", "finished_copy_runs", "storage_snapshots_task_vec", "group_snapshot_task_vec", "delete_backup_job_post_process_vec", "teardown_group_snapshot_task_vec", "backup_run_rx_wrapper_states", "finished_rx_replications", "change_mode_tasks", "restore_tasks", "retrieve_archive_tasks", "hierarchy_vec", "hierarchy_node_vec", "entity_id_map", "entity_external_metadata_info", "physical_host_volume_device_key_info_vec", "removed_physical_host_entity_vec", "external_snapshot_info_vec", "run_once_backup_jobs", "blobs", "gc_state", "agent_info_vec", "gatekeeper_state", "update_backup_run_tasks", "update_backup_objects_tasks", "verify_entity_registration_tasks", "entity_permission_info_vec", "globals", "conversion_tasks", "conversion_cleanup_tasks", "aws_proxy_manager_state", "gcp_proxy_manager_state", "yoda_notification_queue", "yoda_notification_delta_record", "scribe_state_proto", "compact_nosql_state_proto", "nosql_gc_state_proto", "bookkeeper_crud_record_vec", "clear_bookkeeper_md_delta_record", "saved_id_generator", "saved_entity_id_generator", "saved_max_entity_id_persisted", "magneto_enable_string_entity_id", "checkpoint_time_usecs", "change_id", "num_change_logs", "entity_cdp_state_proto_vec", "agent_upgrade_tasks", "last_auto_agent_upgrade_run_version", "skip_nested_volumes_check_done", "object_backup_info", "standby_state_proto_vec", "entity_metadata", "entity_provenance_edge_vec", "remove_entity_provenance_edge_vec", "deleted_entity_id_vec", "nosql_backup_job_additional_state_vec", "migrated_restore_task_info_vec", "pause_request_vec", "resume_request_vec", "entity_operation_info_vec", "enabled_auth_for_unsecure_backup_views", "vm_linking_bios_uuid_cleanup_done", "artifact_state_vec", "kvm_ovirt_manager_uuid_patched_to_hostname_done", "created_or_updated_entity_id_vec", "unindexed_backup_runs_vec", "num_non_cloud_proxy_gk_permit_migrations", "serialized_finished_copy_run_vec", "last_cluster_version_cdp_iofilter_upgradability", "added_workload_stats_for_older_backup_views", "connections", "historical_deleted_entities_pruned_iterations", "security_update_views", "forgotten_runs_info", "upgrade_info", "finished_backup_attempts_DEPRECATED", "garbage_collected_backup_attempts_DEPRECATED", "run_once_job_ids_DEPRECATED", "run_once_full_backup_job_ids_DEPRECATED", "old_backup_run_rx_states_DEPRECATED", "finished_old_rx_replication_ids_DEPRECATED", "non_cloud_proxy_gk_permits_migrated_DEPRECATED")
    class CheckpointCapabilities(_message.Message):
        __slots__ = ("runs_in_scribe_aware",)
        RUNS_IN_SCRIBE_AWARE_FIELD_NUMBER: _ClassVar[int]
        runs_in_scribe_aware: bool
        def __init__(self, runs_in_scribe_aware: bool = ...) -> None: ...
    class PostPredumpDirtyRunsInfo(_message.Message):
        __slots__ = ("job_uid", "updated_backup_runs", "runs_scribe_keys_vec", "deleted_backup_runs")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        UPDATED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        RUNS_SCRIBE_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
        DELETED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        updated_backup_runs: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobRunStateProto]
        runs_scribe_keys_vec: _containers.RepeatedCompositeFieldContainer[ScribeKeyVec]
        deleted_backup_runs: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., updated_backup_runs: _Optional[_Iterable[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]]] = ..., runs_scribe_keys_vec: _Optional[_Iterable[_Union[ScribeKeyVec, _Mapping]]] = ..., deleted_backup_runs: _Optional[_Iterable[int]] = ...) -> None: ...
    class PredumpAction(_message.Message):
        __slots__ = ("job_uid", "action", "finished_backup_runs_info", "gced_backup_runs_info")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAdd: _ClassVar[PersistentStateProto.PredumpAction.Action]
            kDiscard: _ClassVar[PersistentStateProto.PredumpAction.Action]
        kAdd: PersistentStateProto.PredumpAction.Action
        kDiscard: PersistentStateProto.PredumpAction.Action
        class RunVecInfo(_message.Message):
            __slots__ = ("num_entries", "oldest_run_start_time_usecs", "latest_run_start_time_usecs")
            NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
            OLDEST_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            LATEST_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            num_entries: int
            oldest_run_start_time_usecs: int
            latest_run_start_time_usecs: int
            def __init__(self, num_entries: _Optional[int] = ..., oldest_run_start_time_usecs: _Optional[int] = ..., latest_run_start_time_usecs: _Optional[int] = ...) -> None: ...
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        FINISHED_BACKUP_RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
        GCED_BACKUP_RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        action: PersistentStateProto.PredumpAction.Action
        finished_backup_runs_info: PersistentStateProto.PredumpAction.RunVecInfo
        gced_backup_runs_info: PersistentStateProto.PredumpAction.RunVecInfo
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., action: _Optional[_Union[PersistentStateProto.PredumpAction.Action, str]] = ..., finished_backup_runs_info: _Optional[_Union[PersistentStateProto.PredumpAction.RunVecInfo, _Mapping]] = ..., gced_backup_runs_info: _Optional[_Union[PersistentStateProto.PredumpAction.RunVecInfo, _Mapping]] = ...) -> None: ...
    class EntityExternalMetadataInfo(_message.Message):
        __slots__ = ("entity_id", "external_metadata", "is_deleted")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        external_metadata: _magneto_pb2.EntityExternalMetadataProto
        is_deleted: bool
        def __init__(self, entity_id: _Optional[int] = ..., external_metadata: _Optional[_Union[_magneto_pb2.EntityExternalMetadataProto, _Mapping]] = ..., is_deleted: bool = ...) -> None: ...
    class Blob(_message.Message):
        __slots__ = ("name", "data")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: bytes
        def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    class BookKeeperCRUDProto(_message.Message):
        __slots__ = ("job_uid", "bookkeeper_metadata")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_METADATA_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        bookkeeper_metadata: BookKeeperMetadataProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., bookkeeper_metadata: _Optional[_Union[BookKeeperMetadataProto, _Mapping]] = ...) -> None: ...
    class EntityMetadata(_message.Message):
        __slots__ = ("entity_metadata_record_type", "entity_metadata_vec")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDummy: _ClassVar[PersistentStateProto.EntityMetadata.Type]
            kCheckpoint: _ClassVar[PersistentStateProto.EntityMetadata.Type]
        kDummy: PersistentStateProto.EntityMetadata.Type
        kCheckpoint: PersistentStateProto.EntityMetadata.Type
        ENTITY_METADATA_RECORD_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_metadata_record_type: PersistentStateProto.EntityMetadata.Type
        entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[EntityBackupMetadata]
        def __init__(self, entity_metadata_record_type: _Optional[_Union[PersistentStateProto.EntityMetadata.Type, str]] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[EntityBackupMetadata, _Mapping]]] = ...) -> None: ...
    class NosqlBackupJobAdditionalStateProto(_message.Message):
        __slots__ = ("backup_job_id", "nosql_additional_state_proto")
        BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
        NOSQL_ADDITIONAL_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
        backup_job_id: int
        nosql_additional_state_proto: _nosql_pb2.NosqlAdditionalStateProto
        def __init__(self, backup_job_id: _Optional[int] = ..., nosql_additional_state_proto: _Optional[_Union[_nosql_pb2.NosqlAdditionalStateProto, _Mapping]] = ...) -> None: ...
    class ArtifactStateProto(_message.Message):
        __slots__ = ("artifact_id", "artifact_state_proto")
        ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
        artifact_id: _artifact_garbage_collector_pb2.ArtifactIdProto
        artifact_state_proto: _artifact_garbage_collector_pb2.ArtifactGCStateProto
        def __init__(self, artifact_id: _Optional[_Union[_artifact_garbage_collector_pb2.ArtifactIdProto, _Mapping]] = ..., artifact_state_proto: _Optional[_Union[_artifact_garbage_collector_pb2.ArtifactGCStateProto, _Mapping]] = ...) -> None: ...
    class BackupRunIndexingStatusProto(_message.Message):
        __slots__ = ("run_start_time_usecs_map", "job_uid")
        class RunStartTimeUsecsMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: bool
            def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
        RUN_START_TIME_USECS_MAP_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        run_start_time_usecs_map: _containers.ScalarMap[int, bool]
        job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, run_start_time_usecs_map: _Optional[_Mapping[int, bool]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class Connections(_message.Message):
        __slots__ = ("id", "interval_connections")
        class IntervalConnections(_message.Message):
            __slots__ = ("interval", "connections")
            INTERVAL_FIELD_NUMBER: _ClassVar[int]
            CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
            interval: int
            connections: int
            def __init__(self, interval: _Optional[int] = ..., connections: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        id: str
        interval_connections: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.Connections.IntervalConnections]
        def __init__(self, id: _Optional[str] = ..., interval_connections: _Optional[_Iterable[_Union[PersistentStateProto.Connections.IntervalConnections, _Mapping]]] = ...) -> None: ...
    class SecurityUpdateView(_message.Message):
        __slots__ = ("view_name", "set_security_field")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SET_SECURITY_FIELD_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        set_security_field: bool
        def __init__(self, view_name: _Optional[str] = ..., set_security_field: bool = ...) -> None: ...
    class ForgottenRunsInfo(_message.Message):
        __slots__ = ("scribe_key_gc_pending_runs",)
        class ScribeKeyGcPendingRun(_message.Message):
            __slots__ = ("job_uid", "run_start_time_usecs")
            JOB_UID_FIELD_NUMBER: _ClassVar[int]
            RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            job_uid: _universal_id_pb2.UniversalIdProto
            run_start_time_usecs: int
            def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...
        SCRIBE_KEY_GC_PENDING_RUNS_FIELD_NUMBER: _ClassVar[int]
        scribe_key_gc_pending_runs: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.ForgottenRunsInfo.ScribeKeyGcPendingRun]
        def __init__(self, scribe_key_gc_pending_runs: _Optional[_Iterable[_Union[PersistentStateProto.ForgottenRunsInfo.ScribeKeyGcPendingRun, _Mapping]]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    PASSWORDS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICIES_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_PROTECTION_POLICIES_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOBS_FIELD_NUMBER: _ClassVar[int]
    OLD_BACKUP_JOBS_FIELD_NUMBER: _ClassVar[int]
    JOB_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_RUNS_SCRIBE_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_FINISHED_RUN_SHELL_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_COLLECTED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    GC_RUNS_SCRIBE_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_GC_RUN_SHELL_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_FINISHED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_GCED_BACKUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_FINISHED_COPY_RUNS_FIELD_NUMBER: _ClassVar[int]
    IS_RUN_PREDUMP_RECORD_FIELD_NUMBER: _ClassVar[int]
    IGNORED_DELTA_RECORD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DIRTY_FINISHED_RUNS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DIRTY_GCED_RUNS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PREDUMP_ACTION_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_WRAPPER_STATE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_COPY_RUNS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOTS_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_SNAPSHOT_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUP_JOB_POST_PROCESS_VEC_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_GROUP_SNAPSHOT_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_RX_WRAPPER_STATES_FIELD_NUMBER: _ClassVar[int]
    FINISHED_RX_REPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_MODE_TASKS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASKS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_VEC_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_EXTERNAL_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_HOST_VOLUME_DEVICE_KEY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVED_PHYSICAL_HOST_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_ONCE_BACKUP_JOBS_FIELD_NUMBER: _ClassVar[int]
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    GC_STATE_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GATEKEEPER_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BACKUP_RUN_TASKS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BACKUP_OBJECTS_TASKS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_ENTITY_REGISTRATION_TASKS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GLOBALS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TASKS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CLEANUP_TASKS_FIELD_NUMBER: _ClassVar[int]
    AWS_PROXY_MANAGER_STATE_FIELD_NUMBER: _ClassVar[int]
    GCP_PROXY_MANAGER_STATE_FIELD_NUMBER: _ClassVar[int]
    YODA_NOTIFICATION_QUEUE_FIELD_NUMBER: _ClassVar[int]
    YODA_NOTIFICATION_DELTA_RECORD_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    COMPACT_NOSQL_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    NOSQL_GC_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_CRUD_RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    CLEAR_BOOKKEEPER_MD_DELTA_RECORD_FIELD_NUMBER: _ClassVar[int]
    SAVED_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    SAVED_ENTITY_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    SAVED_MAX_ENTITY_ID_PERSISTED_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ENABLE_STRING_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANGE_LOGS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CDP_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_UPGRADE_TASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTO_AGENT_UPGRADE_RUN_VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_NESTED_VOLUMES_CHECK_DONE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROVENANCE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ENTITY_PROVENANCE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETED_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NOSQL_BACKUP_JOB_ADDITIONAL_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_RESTORE_TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAUSE_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    RESUME_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_OPERATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLED_AUTH_FOR_UNSECURE_BACKUP_VIEWS_FIELD_NUMBER: _ClassVar[int]
    VM_LINKING_BIOS_UUID_CLEANUP_DONE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    KVM_OVIRT_MANAGER_UUID_PATCHED_TO_HOSTNAME_DONE_FIELD_NUMBER: _ClassVar[int]
    CREATED_OR_UPDATED_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    UNINDEXED_BACKUP_RUNS_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_NON_CLOUD_PROXY_GK_PERMIT_MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_FINISHED_COPY_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_CLUSTER_VERSION_CDP_IOFILTER_UPGRADABILITY_FIELD_NUMBER: _ClassVar[int]
    ADDED_WORKLOAD_STATS_FOR_OLDER_BACKUP_VIEWS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_DELETED_ENTITIES_PRUNED_ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_UPDATE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    FORGOTTEN_RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_INFO_FIELD_NUMBER: _ClassVar[int]
    FINISHED_BACKUP_ATTEMPTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_COLLECTED_BACKUP_ATTEMPTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RUN_ONCE_JOB_IDS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RUN_ONCE_FULL_BACKUP_JOB_IDS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    OLD_BACKUP_RUN_RX_STATES_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FINISHED_OLD_RX_REPLICATION_IDS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    NON_CLOUD_PROXY_GK_PERMITS_MIGRATED_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    persistent_state_proto_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto]
    passwords_encrypted: bool
    protection_policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.ProtectionPolicyProto]
    global_protection_policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.ProtectionPolicyProto]
    replicated_policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.ProtectionPolicyProto]
    backup_jobs: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupJobProto]
    old_backup_jobs: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupJobProto]
    job_task_state: _containers.RepeatedCompositeFieldContainer[BackupRunWrapperStateProto]
    finished_backup_runs: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobRunStateProto]
    finished_runs_scribe_keys_vec: _containers.RepeatedCompositeFieldContainer[ScribeKeyVec]
    migrated_finished_run_shell_proto_vec: _containers.RepeatedCompositeFieldContainer[_backup_job_data_pb2.BackupJobRunMetadataProto]
    missed_backup_runs: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobRunStateProto]
    garbage_collected_backup_runs: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobRunStateProto]
    gc_runs_scribe_keys_vec: _containers.RepeatedCompositeFieldContainer[ScribeKeyVec]
    migrated_gc_run_shell_proto_vec: _containers.RepeatedCompositeFieldContainer[_backup_job_data_pb2.BackupJobRunMetadataProto]
    checkpoint_capabilities: PersistentStateProto.CheckpointCapabilities
    serialized_finished_backup_runs: _containers.RepeatedCompositeFieldContainer[SerializedJobRunStateProto]
    serialized_gced_backup_runs: _containers.RepeatedCompositeFieldContainer[SerializedJobRunStateProto]
    serialized_finished_copy_runs: _containers.RepeatedCompositeFieldContainer[SerializedJobRunStateProto]
    is_run_predump_record: bool
    ignored_delta_record_limit: int
    dirty_finished_runs_info_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.PostPredumpDirtyRunsInfo]
    dirty_gced_runs_info_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.PostPredumpDirtyRunsInfo]
    predump_action: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.PredumpAction]
    copy_run_wrapper_state: _containers.RepeatedCompositeFieldContainer[CopyBackupRunWrapperStateProto]
    finished_copy_runs: _containers.RepeatedCompositeFieldContainer[_master_pb2.CopyBackupRunStateProto]
    storage_snapshots_task_vec: _containers.RepeatedCompositeFieldContainer[StorageSnapshotsTaskStateProto]
    group_snapshot_task_vec: _containers.RepeatedCompositeFieldContainer[GroupSnapshotTaskStateProto]
    delete_backup_job_post_process_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.DeleteBackupJobPostProcessProto]
    teardown_group_snapshot_task_vec: _containers.RepeatedCompositeFieldContainer[TeardownGroupSnapshotTaskStateProto]
    backup_run_rx_wrapper_states: _containers.RepeatedCompositeFieldContainer[BackupRunRxWrapperStateProto]
    finished_rx_replications: _containers.RepeatedCompositeFieldContainer[FinishedRxReplicationTaskProto]
    change_mode_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.ChangeBackupJobModeProto]
    restore_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.RestoreWrapperProto]
    retrieve_archive_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.RetrieveArchiveTaskStateProto]
    hierarchy_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto]
    hierarchy_node_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.HierarchyNode]
    entity_id_map: EntityIdMapProto
    entity_external_metadata_info: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.EntityExternalMetadataInfo]
    physical_host_volume_device_key_info_vec: _containers.RepeatedCompositeFieldContainer[PhysicalHostVolumeDeviceKeyInfo]
    removed_physical_host_entity_vec: _containers.RepeatedScalarFieldContainer[int]
    external_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.ExternalSnapshotInfo]
    run_once_backup_jobs: _containers.RepeatedCompositeFieldContainer[RunOnceBackupJobProto]
    blobs: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.Blob]
    gc_state: GarbageCollectionStateProto
    agent_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.AgentInfoProto]
    gatekeeper_state: GateKeeperStateProto
    update_backup_run_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.UpdateBackupRunTaskProto]
    update_backup_objects_tasks: _containers.RepeatedCompositeFieldContainer[UpdateBackupObjectsTaskProto]
    verify_entity_registration_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.VerifyEntityRegistrationTaskStateProto]
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    globals: _master_pb2.GlobalSettings
    conversion_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.ConversionTaskStateProto]
    conversion_cleanup_tasks: _containers.RepeatedCompositeFieldContainer[_master_pb2.ConversionCleanupTaskStateProto]
    aws_proxy_manager_state: ProxyManagerStateProto
    gcp_proxy_manager_state: ProxyManagerStateProto
    yoda_notification_queue: _containers.RepeatedCompositeFieldContainer[NotificationQueueEntryProto]
    yoda_notification_delta_record: NotificationQueueEntryProto
    scribe_state_proto: MoveToScribeStateProto
    compact_nosql_state_proto: CompactNosqlStateProto
    nosql_gc_state_proto: NosqlGarbageCollectionStateProto
    bookkeeper_crud_record_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.BookKeeperCRUDProto]
    clear_bookkeeper_md_delta_record: _universal_id_pb2.UniversalIdProto
    saved_id_generator: int
    saved_entity_id_generator: int
    saved_max_entity_id_persisted: int
    magneto_enable_string_entity_id: bool
    checkpoint_time_usecs: int
    change_id: int
    num_change_logs: int
    entity_cdp_state_proto_vec: _containers.RepeatedCompositeFieldContainer[_master_cdp_pb2.EntityCdpStateProto]
    agent_upgrade_tasks: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.UpgradeTaskStateProto]
    last_auto_agent_upgrade_run_version: str
    skip_nested_volumes_check_done: bool
    object_backup_info: ObjectBackupPersistentStateProto
    standby_state_proto_vec: _containers.RepeatedCompositeFieldContainer[_master_standby_pb2.StandbyStateProto]
    entity_metadata: PersistentStateProto.EntityMetadata
    entity_provenance_edge_vec: _containers.RepeatedCompositeFieldContainer[_entity_provenance_pb2.EntityProvenanceEdgeProto]
    remove_entity_provenance_edge_vec: _containers.RepeatedCompositeFieldContainer[_entity_provenance_pb2.EntityProvenanceEdgeProto]
    deleted_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    nosql_backup_job_additional_state_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.NosqlBackupJobAdditionalStateProto]
    migrated_restore_task_info_vec: _containers.RepeatedCompositeFieldContainer[MigratedRestoreTasksInfo]
    pause_request_vec: _containers.RepeatedCompositeFieldContainer[PauseRequest]
    resume_request_vec: _containers.RepeatedCompositeFieldContainer[ResumeRequest]
    entity_operation_info_vec: _containers.RepeatedCompositeFieldContainer[_entity_operations_pb2.EntityOperationInfoProto]
    enabled_auth_for_unsecure_backup_views: bool
    vm_linking_bios_uuid_cleanup_done: bool
    artifact_state_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.ArtifactStateProto]
    kvm_ovirt_manager_uuid_patched_to_hostname_done: bool
    created_or_updated_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    unindexed_backup_runs_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.BackupRunIndexingStatusProto]
    num_non_cloud_proxy_gk_permit_migrations: int
    serialized_finished_copy_run_vec: _containers.RepeatedCompositeFieldContainer[_backup_job_data_pb2.CopyRunShellProto]
    last_cluster_version_cdp_iofilter_upgradability: str
    added_workload_stats_for_older_backup_views: bool
    connections: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.Connections]
    historical_deleted_entities_pruned_iterations: int
    security_update_views: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.SecurityUpdateView]
    forgotten_runs_info: PersistentStateProto.ForgottenRunsInfo
    upgrade_info: UpgradeInformationProto
    finished_backup_attempts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobAttemptStateProto]
    garbage_collected_backup_attempts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobAttemptStateProto]
    run_once_job_ids_DEPRECATED: _containers.RepeatedScalarFieldContainer[int]
    run_once_full_backup_job_ids_DEPRECATED: _containers.RepeatedScalarFieldContainer[int]
    old_backup_run_rx_states_DEPRECATED: _containers.RepeatedCompositeFieldContainer[OldBackupRunRxStateProto]
    finished_old_rx_replication_ids_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    non_cloud_proxy_gk_permits_migrated_DEPRECATED: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., persistent_state_proto_vec: _Optional[_Iterable[_Union[PersistentStateProto, _Mapping]]] = ..., passwords_encrypted: bool = ..., protection_policies: _Optional[_Iterable[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]]] = ..., global_protection_policies: _Optional[_Iterable[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]]] = ..., replicated_policies: _Optional[_Iterable[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]]] = ..., backup_jobs: _Optional[_Iterable[_Union[_magneto_pb2.BackupJobProto, _Mapping]]] = ..., old_backup_jobs: _Optional[_Iterable[_Union[_magneto_pb2.BackupJobProto, _Mapping]]] = ..., job_task_state: _Optional[_Iterable[_Union[BackupRunWrapperStateProto, _Mapping]]] = ..., finished_backup_runs: _Optional[_Iterable[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]]] = ..., finished_runs_scribe_keys_vec: _Optional[_Iterable[_Union[ScribeKeyVec, _Mapping]]] = ..., migrated_finished_run_shell_proto_vec: _Optional[_Iterable[_Union[_backup_job_data_pb2.BackupJobRunMetadataProto, _Mapping]]] = ..., missed_backup_runs: _Optional[_Iterable[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]]] = ..., garbage_collected_backup_runs: _Optional[_Iterable[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]]] = ..., gc_runs_scribe_keys_vec: _Optional[_Iterable[_Union[ScribeKeyVec, _Mapping]]] = ..., migrated_gc_run_shell_proto_vec: _Optional[_Iterable[_Union[_backup_job_data_pb2.BackupJobRunMetadataProto, _Mapping]]] = ..., checkpoint_capabilities: _Optional[_Union[PersistentStateProto.CheckpointCapabilities, _Mapping]] = ..., serialized_finished_backup_runs: _Optional[_Iterable[_Union[SerializedJobRunStateProto, _Mapping]]] = ..., serialized_gced_backup_runs: _Optional[_Iterable[_Union[SerializedJobRunStateProto, _Mapping]]] = ..., serialized_finished_copy_runs: _Optional[_Iterable[_Union[SerializedJobRunStateProto, _Mapping]]] = ..., is_run_predump_record: bool = ..., ignored_delta_record_limit: _Optional[int] = ..., dirty_finished_runs_info_vec: _Optional[_Iterable[_Union[PersistentStateProto.PostPredumpDirtyRunsInfo, _Mapping]]] = ..., dirty_gced_runs_info_vec: _Optional[_Iterable[_Union[PersistentStateProto.PostPredumpDirtyRunsInfo, _Mapping]]] = ..., predump_action: _Optional[_Iterable[_Union[PersistentStateProto.PredumpAction, _Mapping]]] = ..., copy_run_wrapper_state: _Optional[_Iterable[_Union[CopyBackupRunWrapperStateProto, _Mapping]]] = ..., finished_copy_runs: _Optional[_Iterable[_Union[_master_pb2.CopyBackupRunStateProto, _Mapping]]] = ..., storage_snapshots_task_vec: _Optional[_Iterable[_Union[StorageSnapshotsTaskStateProto, _Mapping]]] = ..., group_snapshot_task_vec: _Optional[_Iterable[_Union[GroupSnapshotTaskStateProto, _Mapping]]] = ..., delete_backup_job_post_process_vec: _Optional[_Iterable[_Union[_master_pb2.DeleteBackupJobPostProcessProto, _Mapping]]] = ..., teardown_group_snapshot_task_vec: _Optional[_Iterable[_Union[TeardownGroupSnapshotTaskStateProto, _Mapping]]] = ..., backup_run_rx_wrapper_states: _Optional[_Iterable[_Union[BackupRunRxWrapperStateProto, _Mapping]]] = ..., finished_rx_replications: _Optional[_Iterable[_Union[FinishedRxReplicationTaskProto, _Mapping]]] = ..., change_mode_tasks: _Optional[_Iterable[_Union[_master_pb2.ChangeBackupJobModeProto, _Mapping]]] = ..., restore_tasks: _Optional[_Iterable[_Union[_master_pb2.RestoreWrapperProto, _Mapping]]] = ..., retrieve_archive_tasks: _Optional[_Iterable[_Union[_master_pb2.RetrieveArchiveTaskStateProto, _Mapping]]] = ..., hierarchy_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]]] = ..., hierarchy_node_vec: _Optional[_Iterable[_Union[_magneto_pb2.HierarchyNode, _Mapping]]] = ..., entity_id_map: _Optional[_Union[EntityIdMapProto, _Mapping]] = ..., entity_external_metadata_info: _Optional[_Iterable[_Union[PersistentStateProto.EntityExternalMetadataInfo, _Mapping]]] = ..., physical_host_volume_device_key_info_vec: _Optional[_Iterable[_Union[PhysicalHostVolumeDeviceKeyInfo, _Mapping]]] = ..., removed_physical_host_entity_vec: _Optional[_Iterable[int]] = ..., external_snapshot_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.ExternalSnapshotInfo, _Mapping]]] = ..., run_once_backup_jobs: _Optional[_Iterable[_Union[RunOnceBackupJobProto, _Mapping]]] = ..., blobs: _Optional[_Iterable[_Union[PersistentStateProto.Blob, _Mapping]]] = ..., gc_state: _Optional[_Union[GarbageCollectionStateProto, _Mapping]] = ..., agent_info_vec: _Optional[_Iterable[_Union[_agent_pb2.AgentInfoProto, _Mapping]]] = ..., gatekeeper_state: _Optional[_Union[GateKeeperStateProto, _Mapping]] = ..., update_backup_run_tasks: _Optional[_Iterable[_Union[_master_pb2.UpdateBackupRunTaskProto, _Mapping]]] = ..., update_backup_objects_tasks: _Optional[_Iterable[_Union[UpdateBackupObjectsTaskProto, _Mapping]]] = ..., verify_entity_registration_tasks: _Optional[_Iterable[_Union[_master_pb2.VerifyEntityRegistrationTaskStateProto, _Mapping]]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., globals: _Optional[_Union[_master_pb2.GlobalSettings, _Mapping]] = ..., conversion_tasks: _Optional[_Iterable[_Union[_master_pb2.ConversionTaskStateProto, _Mapping]]] = ..., conversion_cleanup_tasks: _Optional[_Iterable[_Union[_master_pb2.ConversionCleanupTaskStateProto, _Mapping]]] = ..., aws_proxy_manager_state: _Optional[_Union[ProxyManagerStateProto, _Mapping]] = ..., gcp_proxy_manager_state: _Optional[_Union[ProxyManagerStateProto, _Mapping]] = ..., yoda_notification_queue: _Optional[_Iterable[_Union[NotificationQueueEntryProto, _Mapping]]] = ..., yoda_notification_delta_record: _Optional[_Union[NotificationQueueEntryProto, _Mapping]] = ..., scribe_state_proto: _Optional[_Union[MoveToScribeStateProto, _Mapping]] = ..., compact_nosql_state_proto: _Optional[_Union[CompactNosqlStateProto, _Mapping]] = ..., nosql_gc_state_proto: _Optional[_Union[NosqlGarbageCollectionStateProto, _Mapping]] = ..., bookkeeper_crud_record_vec: _Optional[_Iterable[_Union[PersistentStateProto.BookKeeperCRUDProto, _Mapping]]] = ..., clear_bookkeeper_md_delta_record: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., saved_id_generator: _Optional[int] = ..., saved_entity_id_generator: _Optional[int] = ..., saved_max_entity_id_persisted: _Optional[int] = ..., magneto_enable_string_entity_id: bool = ..., checkpoint_time_usecs: _Optional[int] = ..., change_id: _Optional[int] = ..., num_change_logs: _Optional[int] = ..., entity_cdp_state_proto_vec: _Optional[_Iterable[_Union[_master_cdp_pb2.EntityCdpStateProto, _Mapping]]] = ..., agent_upgrade_tasks: _Optional[_Iterable[_Union[_magneto_pb2.UpgradeTaskStateProto, _Mapping]]] = ..., last_auto_agent_upgrade_run_version: _Optional[str] = ..., skip_nested_volumes_check_done: bool = ..., object_backup_info: _Optional[_Union[ObjectBackupPersistentStateProto, _Mapping]] = ..., standby_state_proto_vec: _Optional[_Iterable[_Union[_master_standby_pb2.StandbyStateProto, _Mapping]]] = ..., entity_metadata: _Optional[_Union[PersistentStateProto.EntityMetadata, _Mapping]] = ..., entity_provenance_edge_vec: _Optional[_Iterable[_Union[_entity_provenance_pb2.EntityProvenanceEdgeProto, _Mapping]]] = ..., remove_entity_provenance_edge_vec: _Optional[_Iterable[_Union[_entity_provenance_pb2.EntityProvenanceEdgeProto, _Mapping]]] = ..., deleted_entity_id_vec: _Optional[_Iterable[int]] = ..., nosql_backup_job_additional_state_vec: _Optional[_Iterable[_Union[PersistentStateProto.NosqlBackupJobAdditionalStateProto, _Mapping]]] = ..., migrated_restore_task_info_vec: _Optional[_Iterable[_Union[MigratedRestoreTasksInfo, _Mapping]]] = ..., pause_request_vec: _Optional[_Iterable[_Union[PauseRequest, _Mapping]]] = ..., resume_request_vec: _Optional[_Iterable[_Union[ResumeRequest, _Mapping]]] = ..., entity_operation_info_vec: _Optional[_Iterable[_Union[_entity_operations_pb2.EntityOperationInfoProto, _Mapping]]] = ..., enabled_auth_for_unsecure_backup_views: bool = ..., vm_linking_bios_uuid_cleanup_done: bool = ..., artifact_state_vec: _Optional[_Iterable[_Union[PersistentStateProto.ArtifactStateProto, _Mapping]]] = ..., kvm_ovirt_manager_uuid_patched_to_hostname_done: bool = ..., created_or_updated_entity_id_vec: _Optional[_Iterable[int]] = ..., unindexed_backup_runs_vec: _Optional[_Iterable[_Union[PersistentStateProto.BackupRunIndexingStatusProto, _Mapping]]] = ..., num_non_cloud_proxy_gk_permit_migrations: _Optional[int] = ..., serialized_finished_copy_run_vec: _Optional[_Iterable[_Union[_backup_job_data_pb2.CopyRunShellProto, _Mapping]]] = ..., last_cluster_version_cdp_iofilter_upgradability: _Optional[str] = ..., added_workload_stats_for_older_backup_views: bool = ..., connections: _Optional[_Iterable[_Union[PersistentStateProto.Connections, _Mapping]]] = ..., historical_deleted_entities_pruned_iterations: _Optional[int] = ..., security_update_views: _Optional[_Iterable[_Union[PersistentStateProto.SecurityUpdateView, _Mapping]]] = ..., forgotten_runs_info: _Optional[_Union[PersistentStateProto.ForgottenRunsInfo, _Mapping]] = ..., upgrade_info: _Optional[_Union[UpgradeInformationProto, _Mapping]] = ..., finished_backup_attempts_DEPRECATED: _Optional[_Iterable[_Union[_master_pb2.BackupJobAttemptStateProto, _Mapping]]] = ..., garbage_collected_backup_attempts_DEPRECATED: _Optional[_Iterable[_Union[_master_pb2.BackupJobAttemptStateProto, _Mapping]]] = ..., run_once_job_ids_DEPRECATED: _Optional[_Iterable[int]] = ..., run_once_full_backup_job_ids_DEPRECATED: _Optional[_Iterable[int]] = ..., old_backup_run_rx_states_DEPRECATED: _Optional[_Iterable[_Union[OldBackupRunRxStateProto, _Mapping]]] = ..., finished_old_rx_replication_ids_DEPRECATED: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., non_cloud_proxy_gk_permits_migrated_DEPRECATED: bool = ...) -> None: ...

class TenantStateProto(_message.Message):
    __slots__ = ("api_version", "hierarchy_node_vec", "hierarchy_vec", "entity_id_map", "object_spec_info", "entity_permission_info_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SPEC_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    hierarchy_node_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.HierarchyNode]
    hierarchy_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto]
    entity_id_map: EntityIdMapProto
    object_spec_info: _containers.RepeatedCompositeFieldContainer[_object_protection_pb2.ObjectSpecInfo]
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., hierarchy_node_vec: _Optional[_Iterable[_Union[_magneto_pb2.HierarchyNode, _Mapping]]] = ..., hierarchy_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]]] = ..., entity_id_map: _Optional[_Union[EntityIdMapProto, _Mapping]] = ..., object_spec_info: _Optional[_Iterable[_Union[_object_protection_pb2.ObjectSpecInfo, _Mapping]]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ...) -> None: ...

class TenantStateExportCheckpoint(_message.Message):
    __slots__ = ("export_cookie", "cur_export_id", "last_checkpointed_tenant_state")
    class ExportedTenantState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[TenantStateExportCheckpoint.ExportedTenantState]
        kEntityHierarchyDone: _ClassVar[TenantStateExportCheckpoint.ExportedTenantState]
        kObjectProtectionsDone: _ClassVar[TenantStateExportCheckpoint.ExportedTenantState]
    kNone: TenantStateExportCheckpoint.ExportedTenantState
    kEntityHierarchyDone: TenantStateExportCheckpoint.ExportedTenantState
    kObjectProtectionsDone: TenantStateExportCheckpoint.ExportedTenantState
    EXPORT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CUR_EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKPOINTED_TENANT_STATE_FIELD_NUMBER: _ClassVar[int]
    export_cookie: bytes
    cur_export_id: str
    last_checkpointed_tenant_state: TenantStateExportCheckpoint.ExportedTenantState
    def __init__(self, export_cookie: _Optional[bytes] = ..., cur_export_id: _Optional[str] = ..., last_checkpointed_tenant_state: _Optional[_Union[TenantStateExportCheckpoint.ExportedTenantState, str]] = ...) -> None: ...

class LatestTenantStateExport(_message.Message):
    __slots__ = ("status", "export_id")
    class ExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[LatestTenantStateExport.ExportStatus]
        kSuccess: _ClassVar[LatestTenantStateExport.ExportStatus]
        kFailed: _ClassVar[LatestTenantStateExport.ExportStatus]
        kInvalid: _ClassVar[LatestTenantStateExport.ExportStatus]
    kInProgress: LatestTenantStateExport.ExportStatus
    kSuccess: LatestTenantStateExport.ExportStatus
    kFailed: LatestTenantStateExport.ExportStatus
    kInvalid: LatestTenantStateExport.ExportStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    status: LatestTenantStateExport.ExportStatus
    export_id: str
    def __init__(self, status: _Optional[_Union[LatestTenantStateExport.ExportStatus, str]] = ..., export_id: _Optional[str] = ...) -> None: ...

class TenantStateImportCheckpoint(_message.Message):
    __slots__ = ("import_cookie", "cur_import_id", "last_checkpointed_tenant_state", "import_scribe_entry_num")
    class ImportedTenantState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[TenantStateImportCheckpoint.ImportedTenantState]
        kEntityHierarchyDone: _ClassVar[TenantStateImportCheckpoint.ImportedTenantState]
        kObjectProtectionsDone: _ClassVar[TenantStateImportCheckpoint.ImportedTenantState]
    kNone: TenantStateImportCheckpoint.ImportedTenantState
    kEntityHierarchyDone: TenantStateImportCheckpoint.ImportedTenantState
    kObjectProtectionsDone: TenantStateImportCheckpoint.ImportedTenantState
    IMPORT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CUR_IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKPOINTED_TENANT_STATE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SCRIBE_ENTRY_NUM_FIELD_NUMBER: _ClassVar[int]
    import_cookie: bytes
    cur_import_id: str
    last_checkpointed_tenant_state: TenantStateImportCheckpoint.ImportedTenantState
    import_scribe_entry_num: int
    def __init__(self, import_cookie: _Optional[bytes] = ..., cur_import_id: _Optional[str] = ..., last_checkpointed_tenant_state: _Optional[_Union[TenantStateImportCheckpoint.ImportedTenantState, str]] = ..., import_scribe_entry_num: _Optional[int] = ...) -> None: ...

class LatestTenantStateImport(_message.Message):
    __slots__ = ("status", "import_id", "migration_uid")
    class ImportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[LatestTenantStateImport.ImportStatus]
        kSuccess: _ClassVar[LatestTenantStateImport.ImportStatus]
        kFailed: _ClassVar[LatestTenantStateImport.ImportStatus]
        kInvalid: _ClassVar[LatestTenantStateImport.ImportStatus]
    kInProgress: LatestTenantStateImport.ImportStatus
    kSuccess: LatestTenantStateImport.ImportStatus
    kFailed: LatestTenantStateImport.ImportStatus
    kInvalid: LatestTenantStateImport.ImportStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    status: LatestTenantStateImport.ImportStatus
    import_id: str
    migration_uid: str
    def __init__(self, status: _Optional[_Union[LatestTenantStateImport.ImportStatus, str]] = ..., import_id: _Optional[str] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class TenantOperationStatus(_message.Message):
    __slots__ = ("tenant_state_export_checkpoint", "latest_export_id_status", "tenant_state_import_checkpoint", "latest_import_id_status", "tenant_state_protections_reconciliation_checkpoint", "latest_protections_reconciliation_status", "latest_snapshots_reconciliation_status")
    TENANT_STATE_EXPORT_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPORT_ID_STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_STATE_IMPORT_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_IMPORT_ID_STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_STATE_PROTECTIONS_RECONCILIATION_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_PROTECTIONS_RECONCILIATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    LATEST_SNAPSHOTS_RECONCILIATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    tenant_state_export_checkpoint: TenantStateExportCheckpoint
    latest_export_id_status: LatestTenantStateExport
    tenant_state_import_checkpoint: TenantStateImportCheckpoint
    latest_import_id_status: LatestTenantStateImport
    tenant_state_protections_reconciliation_checkpoint: TenantStateProtectionsReconciliationCheckpoint
    latest_protections_reconciliation_status: LatestProtectionsReconciliation
    latest_snapshots_reconciliation_status: LatestSnapshotsReconciliation
    def __init__(self, tenant_state_export_checkpoint: _Optional[_Union[TenantStateExportCheckpoint, _Mapping]] = ..., latest_export_id_status: _Optional[_Union[LatestTenantStateExport, _Mapping]] = ..., tenant_state_import_checkpoint: _Optional[_Union[TenantStateImportCheckpoint, _Mapping]] = ..., latest_import_id_status: _Optional[_Union[LatestTenantStateImport, _Mapping]] = ..., tenant_state_protections_reconciliation_checkpoint: _Optional[_Union[TenantStateProtectionsReconciliationCheckpoint, _Mapping]] = ..., latest_protections_reconciliation_status: _Optional[_Union[LatestProtectionsReconciliation, _Mapping]] = ..., latest_snapshots_reconciliation_status: _Optional[_Union[LatestSnapshotsReconciliation, _Mapping]] = ...) -> None: ...

class TenantStateProtectionsReconciliationCheckpoint(_message.Message):
    __slots__ = ("last_processed_spec_uid",)
    LAST_PROCESSED_SPEC_UID_FIELD_NUMBER: _ClassVar[int]
    last_processed_spec_uid: str
    def __init__(self, last_processed_spec_uid: _Optional[str] = ...) -> None: ...

class LatestProtectionsReconciliation(_message.Message):
    __slots__ = ("status", "migration_uid")
    class ProtectionsReconciliationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[LatestProtectionsReconciliation.ProtectionsReconciliationStatus]
        kInProgress: _ClassVar[LatestProtectionsReconciliation.ProtectionsReconciliationStatus]
        kSuccess: _ClassVar[LatestProtectionsReconciliation.ProtectionsReconciliationStatus]
        kFailed: _ClassVar[LatestProtectionsReconciliation.ProtectionsReconciliationStatus]
    kInvalid: LatestProtectionsReconciliation.ProtectionsReconciliationStatus
    kInProgress: LatestProtectionsReconciliation.ProtectionsReconciliationStatus
    kSuccess: LatestProtectionsReconciliation.ProtectionsReconciliationStatus
    kFailed: LatestProtectionsReconciliation.ProtectionsReconciliationStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    status: LatestProtectionsReconciliation.ProtectionsReconciliationStatus
    migration_uid: str
    def __init__(self, status: _Optional[_Union[LatestProtectionsReconciliation.ProtectionsReconciliationStatus, str]] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class LatestSnapshotsReconciliation(_message.Message):
    __slots__ = ("status", "migration_uid")
    class SnapshotsReconciliationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[LatestSnapshotsReconciliation.SnapshotsReconciliationStatus]
        kInProgress: _ClassVar[LatestSnapshotsReconciliation.SnapshotsReconciliationStatus]
        kSuccess: _ClassVar[LatestSnapshotsReconciliation.SnapshotsReconciliationStatus]
        kFailed: _ClassVar[LatestSnapshotsReconciliation.SnapshotsReconciliationStatus]
    kInvalid: LatestSnapshotsReconciliation.SnapshotsReconciliationStatus
    kInProgress: LatestSnapshotsReconciliation.SnapshotsReconciliationStatus
    kSuccess: LatestSnapshotsReconciliation.SnapshotsReconciliationStatus
    kFailed: LatestSnapshotsReconciliation.SnapshotsReconciliationStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    status: LatestSnapshotsReconciliation.SnapshotsReconciliationStatus
    migration_uid: str
    def __init__(self, status: _Optional[_Union[LatestSnapshotsReconciliation.SnapshotsReconciliationStatus, str]] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class PhysicalHostVolumeDeviceKeyInfo(_message.Message):
    __slots__ = ("host_entity_id", "volume_guid_device_key_map")
    class VolumeGuidDeviceKeyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_DEVICE_KEY_MAP_FIELD_NUMBER: _ClassVar[int]
    host_entity_id: int
    volume_guid_device_key_map: _containers.ScalarMap[str, int]
    def __init__(self, host_entity_id: _Optional[int] = ..., volume_guid_device_key_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class BackupRunWrapperStateProto(_message.Message):
    __slots__ = ("run_state", "task_state", "attempt_state_DEPRECATED")
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_STATE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    run_state: _master_pb2.BackupJobRunStateProto
    task_state: _master_pb2.BackupTaskStateProto
    attempt_state_DEPRECATED: _master_pb2.BackupJobAttemptStateProto
    def __init__(self, run_state: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., task_state: _Optional[_Union[_master_pb2.BackupTaskStateProto, _Mapping]] = ..., attempt_state_DEPRECATED: _Optional[_Union[_master_pb2.BackupJobAttemptStateProto, _Mapping]] = ...) -> None: ...

class CopyBackupRunWrapperStateProto(_message.Message):
    __slots__ = ("copy_run_state", "copy_task_state", "copy_sub_task_state")
    COPY_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    COPY_SUB_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    copy_run_state: _master_pb2.CopyBackupRunStateProto
    copy_task_state: _master_pb2.CopyBackupRunTaskStateProto
    copy_sub_task_state: _master_pb2.CopyBackupSubTaskStateProto
    def __init__(self, copy_run_state: _Optional[_Union[_master_pb2.CopyBackupRunStateProto, _Mapping]] = ..., copy_task_state: _Optional[_Union[_master_pb2.CopyBackupRunTaskStateProto, _Mapping]] = ..., copy_sub_task_state: _Optional[_Union[_master_pb2.CopyBackupSubTaskStateProto, _Mapping]] = ...) -> None: ...

class OldBackupRunRxStateProto(_message.Message):
    __slots__ = ("replication_id", "replication_info", "post_rx_error", "metadata", "status", "error", "local_job_uid", "new_entities")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[OldBackupRunRxStateProto.Status]
        kAssigned: _ClassVar[OldBackupRunRxStateProto.Status]
        kFinished: _ClassVar[OldBackupRunRxStateProto.Status]
    kStarted: OldBackupRunRxStateProto.Status
    kAssigned: OldBackupRunRxStateProto.Status
    kFinished: OldBackupRunRxStateProto.Status
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    POST_RX_ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOCAL_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_info: _master_pb2.ReplicationInfoBase
    post_rx_error: _error_pb2.ErrorProto
    metadata: _master_pb2.BackupRunReplicationMDProto
    status: OldBackupRunRxStateProto.Status
    error: _error_pb2_1.ErrorProto
    local_job_uid: _universal_id_pb2.UniversalIdProto
    new_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_info: _Optional[_Union[_master_pb2.ReplicationInfoBase, _Mapping]] = ..., post_rx_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metadata: _Optional[_Union[_master_pb2.BackupRunReplicationMDProto, _Mapping]] = ..., status: _Optional[_Union[OldBackupRunRxStateProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., local_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., new_entities: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ...) -> None: ...

class BackupTaskRxStateProto(_message.Message):
    __slots__ = ("copy_sub_task", "backup_task", "new_entities")
    COPY_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    copy_sub_task: _master_pb2.CopyBackupSubTaskStateProto
    backup_task: _master_pb2.BackupTaskStateProto
    new_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    def __init__(self, copy_sub_task: _Optional[_Union[_master_pb2.CopyBackupSubTaskStateProto, _Mapping]] = ..., backup_task: _Optional[_Union[_master_pb2.BackupTaskStateProto, _Mapping]] = ..., new_entities: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ...) -> None: ...

class BackupRunRxStateProto(_message.Message):
    __slots__ = ("task_uid", "job_description", "protection_policy", "rx_backup_run_base", "start_time_usecs", "end_time_usecs", "snapshot_expiry_usecs", "data_lock_constraints", "legal_hold_enabled", "view_box_id", "status", "error", "cancellation_requested", "local_job_uid", "rx_backup_tasks", "tx_parent_id", "rx_backup_run", "new_entities", "entity_permission_info_vec", "object_level_copy", "entity_provenance_edge_vec", "cad_archival_copy_run_start_time_usecs", "cascaded_copy_run_start_time_usecs", "is_out_of_band_copy_task", "retention_policy", "app_entity_tx_to_rx_map")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[BackupRunRxStateProto.Status]
        kAssigned: _ClassVar[BackupRunRxStateProto.Status]
        kFinishing: _ClassVar[BackupRunRxStateProto.Status]
        kFinished: _ClassVar[BackupRunRxStateProto.Status]
        kCancelled: _ClassVar[BackupRunRxStateProto.Status]
    kStarted: BackupRunRxStateProto.Status
    kAssigned: BackupRunRxStateProto.Status
    kFinishing: BackupRunRxStateProto.Status
    kFinished: BackupRunRxStateProto.Status
    kCancelled: BackupRunRxStateProto.Status
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    RX_BACKUP_RUN_BASE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RX_BACKUP_TASKS_FIELD_NUMBER: _ClassVar[int]
    TX_PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    RX_BACKUP_RUN_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROVENANCE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    CAD_ARCHIVAL_COPY_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CASCADED_COPY_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_COPY_TASK_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_TX_TO_RX_MAP_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    job_description: _magneto_pb2.BackupJobProto
    protection_policy: _policy_pb2.ProtectionPolicyProto
    rx_backup_run_base: _master_pb2.BackupJobTaskStateBaseProto
    start_time_usecs: int
    end_time_usecs: int
    snapshot_expiry_usecs: int
    data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    legal_hold_enabled: bool
    view_box_id: int
    status: BackupRunRxStateProto.Status
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    local_job_uid: _universal_id_pb2.UniversalIdProto
    rx_backup_tasks: _containers.RepeatedCompositeFieldContainer[BackupTaskRxStateProto]
    tx_parent_id: int
    rx_backup_run: _master_pb2.BackupJobRunStateProto
    new_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    object_level_copy: bool
    entity_provenance_edge_vec: _containers.RepeatedCompositeFieldContainer[_entity_provenance_pb2.EntityProvenanceEdgeProto]
    cad_archival_copy_run_start_time_usecs: int
    cascaded_copy_run_start_time_usecs: int
    is_out_of_band_copy_task: bool
    retention_policy: _policy_pb2.RetentionPolicyProto
    app_entity_tx_to_rx_map: AppEntityIdRxMappingProto
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., rx_backup_run_base: _Optional[_Union[_master_pb2.BackupJobTaskStateBaseProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., snapshot_expiry_usecs: _Optional[int] = ..., data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., legal_hold_enabled: bool = ..., view_box_id: _Optional[int] = ..., status: _Optional[_Union[BackupRunRxStateProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., local_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_backup_tasks: _Optional[_Iterable[_Union[BackupTaskRxStateProto, _Mapping]]] = ..., tx_parent_id: _Optional[int] = ..., rx_backup_run: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., new_entities: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., object_level_copy: bool = ..., entity_provenance_edge_vec: _Optional[_Iterable[_Union[_entity_provenance_pb2.EntityProvenanceEdgeProto, _Mapping]]] = ..., cad_archival_copy_run_start_time_usecs: _Optional[int] = ..., cascaded_copy_run_start_time_usecs: _Optional[int] = ..., is_out_of_band_copy_task: bool = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ..., app_entity_tx_to_rx_map: _Optional[_Union[AppEntityIdRxMappingProto, _Mapping]] = ...) -> None: ...

class AppEntityIdRxMappingProto(_message.Message):
    __slots__ = ("app_entity_mapping",)
    class AppEntityMapping(_message.Message):
        __slots__ = ("tx_entity_id", "rx_entity_id")
        TX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        RX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        tx_entity_id: int
        rx_entity_id: int
        def __init__(self, tx_entity_id: _Optional[int] = ..., rx_entity_id: _Optional[int] = ...) -> None: ...
    APP_ENTITY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    app_entity_mapping: _containers.RepeatedCompositeFieldContainer[AppEntityIdRxMappingProto.AppEntityMapping]
    def __init__(self, app_entity_mapping: _Optional[_Iterable[_Union[AppEntityIdRxMappingProto.AppEntityMapping, _Mapping]]] = ...) -> None: ...

class BackupRunRxWrapperStateProto(_message.Message):
    __slots__ = ("backup_run_rx_state", "backup_task_rx_state")
    BACKUP_RUN_RX_STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_RX_STATE_FIELD_NUMBER: _ClassVar[int]
    backup_run_rx_state: BackupRunRxStateProto
    backup_task_rx_state: BackupTaskRxStateProto
    def __init__(self, backup_run_rx_state: _Optional[_Union[BackupRunRxStateProto, _Mapping]] = ..., backup_task_rx_state: _Optional[_Union[BackupTaskRxStateProto, _Mapping]] = ...) -> None: ...

class FinishedRxReplicationTaskProto(_message.Message):
    __slots__ = ("task_uid", "status", "error", "archival_error")
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    status: BackupRunRxStateProto.Status
    error: _error_pb2_1.ErrorProto
    archival_error: _error_pb2_1.ErrorProto
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., status: _Optional[_Union[BackupRunRxStateProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., archival_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class GarbageCollectionStateProto(_message.Message):
    __slots__ = ("id", "runs_to_gc", "jobs_to_gc", "replication_jobs_to_gc", "finished", "error", "job_counters_to_delete", "azure_resources_to_gc", "aws_resources_to_gc", "archived_snapshots_to_gc_vec", "cdp_resources_to_gc", "files_to_delete")
    class GCBackupRun(_message.Message):
        __slots__ = ("job_uid", "start_time_usecs", "dirs_to_delete", "views_to_delete", "containers_to_delete", "counters_to_delete", "task_ids_to_delete_map", "run_proto")
        class TaskIdsToDeleteMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: bool
            def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        DIRS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        VIEWS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        CONTAINERS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        COUNTERS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        TASK_IDS_TO_DELETE_MAP_FIELD_NUMBER: _ClassVar[int]
        RUN_PROTO_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        start_time_usecs: int
        dirs_to_delete: _containers.RepeatedScalarFieldContainer[str]
        views_to_delete: _containers.RepeatedScalarFieldContainer[str]
        containers_to_delete: _containers.RepeatedScalarFieldContainer[int]
        counters_to_delete: _containers.RepeatedCompositeFieldContainer[_stats_pb2.CounterIdentifier]
        task_ids_to_delete_map: _containers.ScalarMap[int, bool]
        run_proto: _master_pb2.BackupJobRunStateProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., dirs_to_delete: _Optional[_Iterable[str]] = ..., views_to_delete: _Optional[_Iterable[str]] = ..., containers_to_delete: _Optional[_Iterable[int]] = ..., counters_to_delete: _Optional[_Iterable[_Union[_stats_pb2.CounterIdentifier, _Mapping]]] = ..., task_ids_to_delete_map: _Optional[_Mapping[int, bool]] = ..., run_proto: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ...) -> None: ...
    class GCBackupJob(_message.Message):
        __slots__ = ("job_uid",)
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class GCReplicationViews(_message.Message):
        __slots__ = ("job_uid", "replication_views_to_expire")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_VIEWS_TO_EXPIRE_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        replication_views_to_expire: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_views_to_expire: _Optional[_Iterable[str]] = ...) -> None: ...
    class GCAzureResource(_message.Message):
        __slots__ = ("target_entity_id", "blob_info_vec", "managed_snapshot_info_vec")
        class AzureBlobInfo(_message.Message):
            __slots__ = ("blob_name", "resource_group_name", "storage_account_name", "storage_container_name", "snapshot_id")
            BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
            blob_name: str
            resource_group_name: str
            storage_account_name: str
            storage_container_name: str
            snapshot_id: str
            def __init__(self, blob_name: _Optional[str] = ..., resource_group_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ...) -> None: ...
        class ManagedSnapshotInfo(_message.Message):
            __slots__ = ("resource_group_name", "snapshot_name", "subscription_id")
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
            SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
            resource_group_name: str
            snapshot_name: str
            subscription_id: str
            def __init__(self, resource_group_name: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...
        TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        MANAGED_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        target_entity_id: int
        blob_info_vec: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCAzureResource.AzureBlobInfo]
        managed_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCAzureResource.ManagedSnapshotInfo]
        def __init__(self, target_entity_id: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCAzureResource.AzureBlobInfo, _Mapping]]] = ..., managed_snapshot_info_vec: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCAzureResource.ManagedSnapshotInfo, _Mapping]]] = ...) -> None: ...
    class GCAWSResource(_message.Message):
        __slots__ = ("ami_id_vec", "target_entity_id", "region_name", "ebs_snapshot_id_vec", "rds_snapshot_id_vec", "aurora_snapshot_id_vec")
        AMI_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_NAME_FIELD_NUMBER: _ClassVar[int]
        EBS_SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        RDS_SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        AURORA_SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        ami_id_vec: _containers.RepeatedScalarFieldContainer[str]
        target_entity_id: int
        region_name: str
        ebs_snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
        rds_snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
        aurora_snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, ami_id_vec: _Optional[_Iterable[str]] = ..., target_entity_id: _Optional[int] = ..., region_name: _Optional[str] = ..., ebs_snapshot_id_vec: _Optional[_Iterable[str]] = ..., rds_snapshot_id_vec: _Optional[_Iterable[str]] = ..., aurora_snapshot_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class GCDeletedJobArchivedSnapshots(_message.Message):
        __slots__ = ("job_uid", "run_start_time_usecs", "snapshot_target_vec")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        run_start_time_usecs: int
        snapshot_target_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.SnapshotTarget]
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., snapshot_target_vec: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTarget, _Mapping]]] = ...) -> None: ...
    class GCCdpResource(_message.Message):
        __slots__ = ("entity_id", "last_seq_number", "is_journal_sharded", "clear_all")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
        CLEAR_ALL_FIELD_NUMBER: _ClassVar[int]
        entity_id: _entity_pb2.EntityID
        last_seq_number: _event_pb2.Sequencer
        is_journal_sharded: bool
        clear_all: bool
        def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., last_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., is_journal_sharded: bool = ..., clear_all: bool = ...) -> None: ...
    class FilesToDelete(_message.Message):
        __slots__ = ("directory", "files")
        DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        directory: str
        files: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, directory: _Optional[str] = ..., files: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_TO_GC_FIELD_NUMBER: _ClassVar[int]
    JOBS_TO_GC_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_JOBS_TO_GC_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_COUNTERS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    AZURE_RESOURCES_TO_GC_FIELD_NUMBER: _ClassVar[int]
    AWS_RESOURCES_TO_GC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_SNAPSHOTS_TO_GC_VEC_FIELD_NUMBER: _ClassVar[int]
    CDP_RESOURCES_TO_GC_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    id: int
    runs_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCBackupRun]
    jobs_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCBackupJob]
    replication_jobs_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCReplicationViews]
    finished: bool
    error: _error_pb2_1.ErrorProto
    job_counters_to_delete: _containers.RepeatedCompositeFieldContainer[_stats_pb2.CounterIdentifier]
    azure_resources_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCAzureResource]
    aws_resources_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCAWSResource]
    archived_snapshots_to_gc_vec: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCDeletedJobArchivedSnapshots]
    cdp_resources_to_gc: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.GCCdpResource]
    files_to_delete: _containers.RepeatedCompositeFieldContainer[GarbageCollectionStateProto.FilesToDelete]
    def __init__(self, id: _Optional[int] = ..., runs_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCBackupRun, _Mapping]]] = ..., jobs_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCBackupJob, _Mapping]]] = ..., replication_jobs_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCReplicationViews, _Mapping]]] = ..., finished: bool = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., job_counters_to_delete: _Optional[_Iterable[_Union[_stats_pb2.CounterIdentifier, _Mapping]]] = ..., azure_resources_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCAzureResource, _Mapping]]] = ..., aws_resources_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCAWSResource, _Mapping]]] = ..., archived_snapshots_to_gc_vec: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCDeletedJobArchivedSnapshots, _Mapping]]] = ..., cdp_resources_to_gc: _Optional[_Iterable[_Union[GarbageCollectionStateProto.GCCdpResource, _Mapping]]] = ..., files_to_delete: _Optional[_Iterable[_Union[GarbageCollectionStateProto.FilesToDelete, _Mapping]]] = ...) -> None: ...

class EntityIdMapProto(_message.Message):
    __slots__ = ("entity_proto",)
    ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    entity_proto: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    def __init__(self, entity_proto: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ...) -> None: ...

class RunOnceBackupJobProto(_message.Message):
    __slots__ = ("backup_type", "job_id", "additional_param_vec", "copy_snapshot_params_vec", "max_attempts", "user_info", "run_label", "is_failover_run", "is_user_triggered_run", "triggered_during_blackout_window", "oob_uid")
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_RUN_FIELD_NUMBER: _ClassVar[int]
    IS_USER_TRIGGERED_RUN_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_DURING_BLACKOUT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    OOB_UID_FIELD_NUMBER: _ClassVar[int]
    backup_type: _enums_pb2.ScheduledBackupType.Type
    job_id: int
    additional_param_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.BackupTaskAdditionalParams]
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.CopySnapshotParams]
    max_attempts: int
    user_info: _permissions_pb2.UserInformation
    run_label: str
    is_failover_run: bool
    is_user_triggered_run: bool
    triggered_during_blackout_window: bool
    oob_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., job_id: _Optional[int] = ..., additional_param_vec: _Optional[_Iterable[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]]] = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[_master_pb2.CopySnapshotParams, _Mapping]]] = ..., max_attempts: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., run_label: _Optional[str] = ..., is_failover_run: bool = ..., is_user_triggered_run: bool = ..., triggered_during_blackout_window: bool = ..., oob_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ProxyTaskSchedulerStateProto(_message.Message):
    __slots__ = ("proxy_state_vec",)
    PROXY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    proxy_state_vec: _containers.RepeatedCompositeFieldContainer[_proxy_pb2.ProxyStateProto]
    def __init__(self, proxy_state_vec: _Optional[_Iterable[_Union[_proxy_pb2.ProxyStateProto, _Mapping]]] = ...) -> None: ...

class GateKeeperStateProto(_message.Message):
    __slots__ = ("task_records", "aws_task_scheduler_state", "gcp_task_scheduler_state")
    class TaskRecord(_message.Message):
        __slots__ = ("task", "task_state")
        TASK_FIELD_NUMBER: _ClassVar[int]
        TASK_STATE_FIELD_NUMBER: _ClassVar[int]
        task: _gatekeeper_pb2.Task
        task_state: _gatekeeper_pb2.TaskState
        def __init__(self, task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., task_state: _Optional[_Union[_gatekeeper_pb2.TaskState, _Mapping]] = ...) -> None: ...
    TASK_RECORDS_FIELD_NUMBER: _ClassVar[int]
    AWS_TASK_SCHEDULER_STATE_FIELD_NUMBER: _ClassVar[int]
    GCP_TASK_SCHEDULER_STATE_FIELD_NUMBER: _ClassVar[int]
    task_records: _containers.RepeatedCompositeFieldContainer[GateKeeperStateProto.TaskRecord]
    aws_task_scheduler_state: ProxyTaskSchedulerStateProto
    gcp_task_scheduler_state: ProxyTaskSchedulerStateProto
    def __init__(self, task_records: _Optional[_Iterable[_Union[GateKeeperStateProto.TaskRecord, _Mapping]]] = ..., aws_task_scheduler_state: _Optional[_Union[ProxyTaskSchedulerStateProto, _Mapping]] = ..., gcp_task_scheduler_state: _Optional[_Union[ProxyTaskSchedulerStateProto, _Mapping]] = ...) -> None: ...

class RegisterArchivedBackupStateProto(_message.Message):
    __slots__ = ("local_job_uid", "updated_remote_job_description", "backup_run", "new_entity_vec", "updated_entity_vec", "local_job_description_DEPRECATED")
    LOCAL_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_REMOTE_JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCAL_JOB_DESCRIPTION_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    local_job_uid: _universal_id_pb2.UniversalIdProto
    updated_remote_job_description: _magneto_pb2.BackupJobProto
    backup_run: _master_pb2.BackupJobRunStateProto
    new_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    updated_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2_1.EntityProto]
    local_job_description_DEPRECATED: _magneto_pb2.BackupJobProto
    def __init__(self, local_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., updated_remote_job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., backup_run: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., new_entity_vec: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ..., updated_entity_vec: _Optional[_Iterable[_Union[_entity_pb2_1.EntityProto, _Mapping]]] = ..., local_job_description_DEPRECATED: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ...) -> None: ...

class StorageSnapshotsTaskStateProto(_message.Message):
    __slots__ = ("task_id", "job_uid", "job_instance_id", "job_name", "run_start_time_usecs", "attempt_num", "source_info_vec", "parent_source", "parent_source_connection_params", "status", "progress_monitor_task_path", "start_time_usecs", "end_time_usecs", "error", "cancellation_requested", "child_tasks_cancellation_issued", "scheduled_constituent_id", "scheduled_gandalf_session_id", "entities_storage_info", "group_snapshot_task_info_vec", "is_deleted", "leverage_san_transport", "storage_array_snapshot", "view_name", "view_box_id", "backup_type", "qos_principal_name", "additional_params", "action_executor_target_type")
    class SourceInfo(_message.Message):
        __slots__ = ("source_id", "backup_source_params", "backup_task_id", "previous_snapshot_info", "stats_container_id")
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        source_id: int
        backup_source_params: _env_params_pb2.BackupSourceParams
        backup_task_id: int
        previous_snapshot_info: _magneto_pb2.SnapshotInfoProto
        stats_container_id: int
        def __init__(self, source_id: _Optional[int] = ..., backup_source_params: _Optional[_Union[_env_params_pb2.BackupSourceParams, _Mapping]] = ..., backup_task_id: _Optional[int] = ..., previous_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., stats_container_id: _Optional[int] = ...) -> None: ...
    class GroupSnapshotTaskInfo(_message.Message):
        __slots__ = ("group_snapshot_task_id", "source_id_vec")
        GROUP_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        group_snapshot_task_id: int
        source_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, group_snapshot_task_id: _Optional[int] = ..., source_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    CHILD_TASKS_CANCELLATION_ISSUED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_STORAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_SNAPSHOT_TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    job_name: str
    run_start_time_usecs: int
    attempt_num: int
    source_info_vec: _containers.RepeatedCompositeFieldContainer[StorageSnapshotsTaskStateProto.SourceInfo]
    parent_source: _entity_pb2_1.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    status: _enums_pb2_1.StorageSnapshotsTaskStatus.Type
    progress_monitor_task_path: str
    start_time_usecs: int
    end_time_usecs: int
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    child_tasks_cancellation_issued: bool
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    entities_storage_info: _storage_pb2.EntitiesStorageInfoProto
    group_snapshot_task_info_vec: _containers.RepeatedCompositeFieldContainer[StorageSnapshotsTaskStateProto.GroupSnapshotTaskInfo]
    is_deleted: bool
    leverage_san_transport: bool
    storage_array_snapshot: bool
    view_name: str
    view_box_id: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    qos_principal_name: str
    additional_params: _magneto_pb2.BackupTaskAdditionalParams
    action_executor_target_type: _enums_pb2.TargetType.Type
    def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., job_name: _Optional[str] = ..., run_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., source_info_vec: _Optional[_Iterable[_Union[StorageSnapshotsTaskStateProto.SourceInfo, _Mapping]]] = ..., parent_source: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., status: _Optional[_Union[_enums_pb2_1.StorageSnapshotsTaskStatus.Type, str]] = ..., progress_monitor_task_path: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., child_tasks_cancellation_issued: bool = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., entities_storage_info: _Optional[_Union[_storage_pb2.EntitiesStorageInfoProto, _Mapping]] = ..., group_snapshot_task_info_vec: _Optional[_Iterable[_Union[StorageSnapshotsTaskStateProto.GroupSnapshotTaskInfo, _Mapping]]] = ..., is_deleted: bool = ..., leverage_san_transport: bool = ..., storage_array_snapshot: bool = ..., view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., qos_principal_name: _Optional[str] = ..., additional_params: _Optional[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ...) -> None: ...

class GroupSnapshotTaskStateProto(_message.Message):
    __slots__ = ("task_id", "parent_storage_snapshot_task_id", "job_uid", "job_instance_id", "job_name", "run_start_time_usecs", "attempt_num", "source_info_vec", "parent_source", "parent_source_connection_params", "primary_storage_source", "quiesce", "status", "progress_monitor_task_path", "start_time_usecs", "end_time_usecs", "primary_storage_connection_params", "error", "cancellation_requested", "scheduled_constituent_id", "scheduled_gandalf_session_id", "entities_group_snapshot_info", "teardown_group_snapshot_task_id", "is_deleted", "leverage_san_transport", "storage_array_snapshot", "locked_entity_vec", "leverage_san_storage_snapshot_v2", "view_name", "view_box_id", "backup_type", "qos_principal_name", "additional_params", "action_executor_target_type", "san_protocol")
    class SourceInfo(_message.Message):
        __slots__ = ("source_id", "backup_source_params", "backup_task_id", "primary_device_vec", "vmware_source_info", "previous_snapshot_info", "stats_container_id")
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
        VMWARE_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        source_id: int
        backup_source_params: _env_params_pb2.BackupSourceParams
        backup_task_id: int
        primary_device_vec: _containers.RepeatedCompositeFieldContainer[_storage_pb2.StorageDeviceProto]
        vmware_source_info: _magneto_pb2.VMwareSourceInfo
        previous_snapshot_info: _magneto_pb2.SnapshotInfoProto
        stats_container_id: int
        def __init__(self, source_id: _Optional[int] = ..., backup_source_params: _Optional[_Union[_env_params_pb2.BackupSourceParams, _Mapping]] = ..., backup_task_id: _Optional[int] = ..., primary_device_vec: _Optional[_Iterable[_Union[_storage_pb2.StorageDeviceProto, _Mapping]]] = ..., vmware_source_info: _Optional[_Union[_magneto_pb2.VMwareSourceInfo, _Mapping]] = ..., previous_snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., stats_container_id: _Optional[int] = ...) -> None: ...
    class LockedEntityInfoProto(_message.Message):
        __slots__ = ("entity", "num_locks_acquired")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        NUM_LOCKS_ACQUIRED_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2_1.EntityProto
        num_locks_acquired: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., num_locks_acquired: _Optional[int] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_STORAGE_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_GROUP_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    LOCKED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAN_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    parent_storage_snapshot_task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    job_name: str
    run_start_time_usecs: int
    attempt_num: int
    source_info_vec: _containers.RepeatedCompositeFieldContainer[GroupSnapshotTaskStateProto.SourceInfo]
    parent_source: _entity_pb2_1.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    primary_storage_source: _entity_pb2_1.EntityProto
    quiesce: bool
    status: _enums_pb2_1.GroupSnapshotTaskStatus.Type
    progress_monitor_task_path: str
    start_time_usecs: int
    end_time_usecs: int
    primary_storage_connection_params: _magneto_pb2.ConnectorParams
    error: _error_pb2_1.ErrorProto
    cancellation_requested: bool
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    entities_group_snapshot_info: _storage_pb2.EntitiesGroupSnapshotInfoProto
    teardown_group_snapshot_task_id: int
    is_deleted: bool
    leverage_san_transport: bool
    storage_array_snapshot: bool
    locked_entity_vec: _containers.RepeatedCompositeFieldContainer[GroupSnapshotTaskStateProto.LockedEntityInfoProto]
    leverage_san_storage_snapshot_v2: bool
    view_name: str
    view_box_id: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    qos_principal_name: str
    additional_params: _magneto_pb2.BackupTaskAdditionalParams
    action_executor_target_type: _enums_pb2.TargetType.Type
    san_protocol: _storage_pb2.SanProtocol
    def __init__(self, task_id: _Optional[int] = ..., parent_storage_snapshot_task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., job_name: _Optional[str] = ..., run_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., source_info_vec: _Optional[_Iterable[_Union[GroupSnapshotTaskStateProto.SourceInfo, _Mapping]]] = ..., parent_source: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., primary_storage_source: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., quiesce: bool = ..., status: _Optional[_Union[_enums_pb2_1.GroupSnapshotTaskStatus.Type, str]] = ..., progress_monitor_task_path: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., primary_storage_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cancellation_requested: bool = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., entities_group_snapshot_info: _Optional[_Union[_storage_pb2.EntitiesGroupSnapshotInfoProto, _Mapping]] = ..., teardown_group_snapshot_task_id: _Optional[int] = ..., is_deleted: bool = ..., leverage_san_transport: bool = ..., storage_array_snapshot: bool = ..., locked_entity_vec: _Optional[_Iterable[_Union[GroupSnapshotTaskStateProto.LockedEntityInfoProto, _Mapping]]] = ..., leverage_san_storage_snapshot_v2: bool = ..., view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., qos_principal_name: _Optional[str] = ..., additional_params: _Optional[_Union[_magneto_pb2.BackupTaskAdditionalParams, _Mapping]] = ..., action_executor_target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., san_protocol: _Optional[_Union[_storage_pb2.SanProtocol, str]] = ...) -> None: ...

class TeardownGroupSnapshotTaskStateProto(_message.Message):
    __slots__ = ("task_id", "parent_group_snapshot_task_id", "job_uid", "job_instance_id", "run_start_time_usecs", "attempt_num", "parent_source", "parent_source_connection_params", "primary_storage_source", "primary_storage_connection_params", "status", "entities_group_snapshot_info", "progress_monitor_task_path", "start_time_usecs", "end_time_usecs", "error", "scheduled_constituent_id", "scheduled_gandalf_session_id", "teardown_info", "is_deleted", "leverage_san_storage_snapshot_v2")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    parent_group_snapshot_task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    run_start_time_usecs: int
    attempt_num: int
    parent_source: _entity_pb2_1.EntityProto
    parent_source_connection_params: _magneto_pb2.ConnectorParams
    primary_storage_source: _entity_pb2_1.EntityProto
    primary_storage_connection_params: _magneto_pb2.ConnectorParams
    status: _enums_pb2_1.TeardownGroupSnapshotTaskStatus.Type
    entities_group_snapshot_info: _storage_pb2.EntitiesGroupSnapshotInfoProto
    progress_monitor_task_path: str
    start_time_usecs: int
    end_time_usecs: int
    error: _error_pb2_1.ErrorProto
    scheduled_constituent_id: int
    scheduled_gandalf_session_id: int
    teardown_info: _storage_pb2.TeardownGroupSnapshotInfoProto
    is_deleted: bool
    leverage_san_storage_snapshot_v2: bool
    def __init__(self, task_id: _Optional[int] = ..., parent_group_snapshot_task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., parent_source: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., parent_source_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., primary_storage_source: _Optional[_Union[_entity_pb2_1.EntityProto, _Mapping]] = ..., primary_storage_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., status: _Optional[_Union[_enums_pb2_1.TeardownGroupSnapshotTaskStatus.Type, str]] = ..., entities_group_snapshot_info: _Optional[_Union[_storage_pb2.EntitiesGroupSnapshotInfoProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., scheduled_constituent_id: _Optional[int] = ..., scheduled_gandalf_session_id: _Optional[int] = ..., teardown_info: _Optional[_Union[_storage_pb2.TeardownGroupSnapshotInfoProto, _Mapping]] = ..., is_deleted: bool = ..., leverage_san_storage_snapshot_v2: bool = ...) -> None: ...

class CDPTaskStateProto(_message.Message):
    __slots__ = ("task_id", "job_uid")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_uid: int
    def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[int] = ...) -> None: ...

class UpdateBackupObjectsTaskProto(_message.Message):
    __slots__ = ("task_id", "job_uid", "run_start_time_usecs", "copy_snapshot_params_vec", "entity_id_vec", "status", "locking_required", "remote_replica_update_required", "initiated_by_dso_role")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COPY_SNAPSHOT_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCKING_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_REPLICA_UPDATE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    INITIATED_BY_DSO_ROLE_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    copy_snapshot_params_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.CopySnapshotParams]
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    status: _enums_pb2_1.UpdateBackupObjectsTaskStatus.Type
    locking_required: bool
    remote_replica_update_required: bool
    initiated_by_dso_role: bool
    def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., copy_snapshot_params_vec: _Optional[_Iterable[_Union[_master_pb2.CopySnapshotParams, _Mapping]]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., status: _Optional[_Union[_enums_pb2_1.UpdateBackupObjectsTaskStatus.Type, str]] = ..., locking_required: bool = ..., remote_replica_update_required: bool = ..., initiated_by_dso_role: bool = ...) -> None: ...

class ProxyManagerStateProto(_message.Message):
    __slots__ = ("proxy_info_vec", "task_scheduler_checkpointing_enabled")
    PROXY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_SCHEDULER_CHECKPOINTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    proxy_info_vec: _containers.RepeatedCompositeFieldContainer[_proxy_pb2.ProxyInfo]
    task_scheduler_checkpointing_enabled: bool
    def __init__(self, proxy_info_vec: _Optional[_Iterable[_Union[_proxy_pb2.ProxyInfo, _Mapping]]] = ..., task_scheduler_checkpointing_enabled: bool = ...) -> None: ...

class NotificationQueueEntryProto(_message.Message):
    __slots__ = ("notification", "dequeue_notification_id")
    class Notification(_message.Message):
        __slots__ = ("notification_id", "add_snapshot_arg", "update_replicas_arg")
        NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
        ADD_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
        UPDATE_REPLICAS_ARG_FIELD_NUMBER: _ClassVar[int]
        notification_id: int
        add_snapshot_arg: _yoda_pb2.AddSnapshotArg
        update_replicas_arg: _yoda_pb2.UpdateSnapshotReplicasArg
        def __init__(self, notification_id: _Optional[int] = ..., add_snapshot_arg: _Optional[_Union[_yoda_pb2.AddSnapshotArg, _Mapping]] = ..., update_replicas_arg: _Optional[_Union[_yoda_pb2.UpdateSnapshotReplicasArg, _Mapping]] = ...) -> None: ...
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEQUEUE_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification: NotificationQueueEntryProto.Notification
    dequeue_notification_id: int
    def __init__(self, notification: _Optional[_Union[NotificationQueueEntryProto.Notification, _Mapping]] = ..., dequeue_notification_id: _Optional[int] = ...) -> None: ...

class SerializedJobRunStateProto(_message.Message):
    __slots__ = ("job_uid", "shell_proto_vec", "serialized_run_vec", "scribe_keys_vec", "deserialized_run_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SHELL_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    DESERIALIZED_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    shell_proto_vec: _containers.RepeatedCompositeFieldContainer[_backup_job_data_pb2.BackupJobRunMetadataProto]
    serialized_run_vec: _containers.RepeatedScalarFieldContainer[bytes]
    scribe_keys_vec: _containers.RepeatedCompositeFieldContainer[ScribeKeyVec]
    deserialized_run_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.BackupJobRunStateProto]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., shell_proto_vec: _Optional[_Iterable[_Union[_backup_job_data_pb2.BackupJobRunMetadataProto, _Mapping]]] = ..., serialized_run_vec: _Optional[_Iterable[bytes]] = ..., scribe_keys_vec: _Optional[_Iterable[_Union[ScribeKeyVec, _Mapping]]] = ..., deserialized_run_vec: _Optional[_Iterable[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]]] = ...) -> None: ...

class MoveToScribeStateProto(_message.Message):
    __slots__ = ("job_uid", "serialized_backup_run_vec", "shell_backup_run_vec", "garbage_collected_runs")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_BACKUP_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
    SHELL_BACKUP_RUN_VEC_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_COLLECTED_RUNS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    serialized_backup_run_vec: _containers.RepeatedScalarFieldContainer[bytes]
    shell_backup_run_vec: _containers.RepeatedCompositeFieldContainer[_backup_job_data_pb2.BackupJobRunMetadataProto]
    garbage_collected_runs: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., serialized_backup_run_vec: _Optional[_Iterable[bytes]] = ..., shell_backup_run_vec: _Optional[_Iterable[_Union[_backup_job_data_pb2.BackupJobRunMetadataProto, _Mapping]]] = ..., garbage_collected_runs: bool = ...) -> None: ...

class CompactBackupJobProto(_message.Message):
    __slots__ = ("job_uid", "backup_entity_id", "live_view_name", "snapshot_view_name", "task_id", "view_box_name")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    backup_entity_id: int
    live_view_name: str
    snapshot_view_name: str
    task_id: int
    view_box_name: str
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_entity_id: _Optional[int] = ..., live_view_name: _Optional[str] = ..., snapshot_view_name: _Optional[str] = ..., task_id: _Optional[int] = ..., view_box_name: _Optional[str] = ...) -> None: ...

class CompactNosqlStateProto(_message.Message):
    __slots__ = ("compaction_jobs",)
    COMPACTION_JOBS_FIELD_NUMBER: _ClassVar[int]
    compaction_jobs: _containers.RepeatedCompositeFieldContainer[CompactBackupJobProto]
    def __init__(self, compaction_jobs: _Optional[_Iterable[_Union[CompactBackupJobProto, _Mapping]]] = ...) -> None: ...

class NosqlGarbageCollectionStateProto(_message.Message):
    __slots__ = ("task_id", "backup_job_gc_params")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_GC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    backup_job_gc_params: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.BackupJobGCParams]
    def __init__(self, task_id: _Optional[int] = ..., backup_job_gc_params: _Optional[_Iterable[_Union[_nosql_pb2.BackupJobGCParams, _Mapping]]] = ...) -> None: ...

class PauseRequest(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "task_ids", "done")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    done: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., task_ids: _Optional[_Iterable[int]] = ..., done: bool = ...) -> None: ...

class ResumeRequest(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "task_ids", "done")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    done: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., task_ids: _Optional[_Iterable[int]] = ..., done: bool = ...) -> None: ...

class GetRestoreTasksPaginationToken(_message.Message):
    __slots__ = ("finished_restore_tasks_resume_token", "finished_multi_stage_restore_tasks_resume_token")
    FINISHED_RESTORE_TASKS_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FINISHED_MULTI_STAGE_RESTORE_TASKS_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    finished_restore_tasks_resume_token: int
    finished_multi_stage_restore_tasks_resume_token: int
    def __init__(self, finished_restore_tasks_resume_token: _Optional[int] = ..., finished_multi_stage_restore_tasks_resume_token: _Optional[int] = ...) -> None: ...

class RecordBatchInfo(_message.Message):
    __slots__ = ("batch_id", "start_batch_record", "end_batch_record")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    START_BATCH_RECORD_FIELD_NUMBER: _ClassVar[int]
    END_BATCH_RECORD_FIELD_NUMBER: _ClassVar[int]
    batch_id: int
    start_batch_record: bool
    end_batch_record: bool
    def __init__(self, batch_id: _Optional[int] = ..., start_batch_record: bool = ..., end_batch_record: bool = ...) -> None: ...

class UpgradeInformationProto(_message.Message):
    __slots__ = ("bookkeeper_upgrade_proto",)
    class BookkeeperUpgradeProto(_message.Message):
        __slots__ = ("is_bookkeeper_full_sync_done_for_eng_407643", "total_bookkeeper_full_sync_occurrences_DEPRECATED")
        IS_BOOKKEEPER_FULL_SYNC_DONE_FOR_ENG_407643_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BOOKKEEPER_FULL_SYNC_OCCURRENCES_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        is_bookkeeper_full_sync_done_for_eng_407643: bool
        total_bookkeeper_full_sync_occurrences_DEPRECATED: int
        def __init__(self, is_bookkeeper_full_sync_done_for_eng_407643: bool = ..., total_bookkeeper_full_sync_occurrences_DEPRECATED: _Optional[int] = ...) -> None: ...
    BOOKKEEPER_UPGRADE_PROTO_FIELD_NUMBER: _ClassVar[int]
    bookkeeper_upgrade_proto: UpgradeInformationProto.BookkeeperUpgradeProto
    def __init__(self, bookkeeper_upgrade_proto: _Optional[_Union[UpgradeInformationProto.BookkeeperUpgradeProto, _Mapping]] = ...) -> None: ...
