from magneto.base import changelog_pb2 as _changelog_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.master.base import master_pb2 as _master_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisteredSource(_message.Message):
    __slots__ = ("uuid", "entity_proto")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    entity_proto: _entity_pb2.EntityProto
    def __init__(self, uuid: _Optional[str] = ..., entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class EntityUuidEntry(_message.Message):
    __slots__ = ("entity_id", "entity_uuid")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    entity_uuid: str
    def __init__(self, entity_id: _Optional[int] = ..., entity_uuid: _Optional[str] = ...) -> None: ...

class PolicyInfo(_message.Message):
    __slots__ = ("policy_id", "policy_name", "protection_uid")
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_UID_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    policy_name: str
    protection_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, policy_id: _Optional[str] = ..., policy_name: _Optional[str] = ..., protection_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class MagnetoStateObject(_message.Message):
    __slots__ = ("object_id", "magneto_object", "change_id", "deleted")
    class MagnetoObject(_message.Message):
        __slots__ = ("policy_proto", "protection_job_proto", "backup_run_proto", "copy_run_proto", "entity_object", "restore_object", "metric_object", "object_info_proto", "object_snapshot_proto")
        class MagnetoEntityObject(_message.Message):
            __slots__ = ("entity_proto", "is_leaf", "entity_uuid", "registered_source", "logical_size_in_bytes", "tenant_id_vec", "registration_info")
            ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
            IS_LEAF_FIELD_NUMBER: _ClassVar[int]
            ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
            REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
            LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
            entity_proto: _entity_pb2.EntityProto
            is_leaf: bool
            entity_uuid: str
            registered_source: RegisteredSource
            logical_size_in_bytes: int
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            registration_info: _magneto_pb2.RegisteredEntityInfo
            def __init__(self, entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_leaf: bool = ..., entity_uuid: _Optional[str] = ..., registered_source: _Optional[_Union[RegisteredSource, _Mapping]] = ..., logical_size_in_bytes: _Optional[int] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., registration_info: _Optional[_Union[_magneto_pb2.RegisteredEntityInfo, _Mapping]] = ...) -> None: ...
        class RestoreTaskObject(_message.Message):
            __slots__ = ("restore_task", "destroy_clone_task", "job_restore_task", "is_active")
            RESTORE_TASK_FIELD_NUMBER: _ClassVar[int]
            DESTROY_CLONE_TASK_FIELD_NUMBER: _ClassVar[int]
            JOB_RESTORE_TASK_FIELD_NUMBER: _ClassVar[int]
            IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
            restore_task: _master_pb2.PerformRestoreTaskStateProto
            destroy_clone_task: _master_pb2.DestroyClonedTaskStateProto
            job_restore_task: _master_pb2.PerformRestoreJobStateProto.RestoreTask
            is_active: bool
            def __init__(self, restore_task: _Optional[_Union[_master_pb2.PerformRestoreTaskStateProto, _Mapping]] = ..., destroy_clone_task: _Optional[_Union[_master_pb2.DestroyClonedTaskStateProto, _Mapping]] = ..., job_restore_task: _Optional[_Union[_master_pb2.PerformRestoreJobStateProto.RestoreTask, _Mapping]] = ..., is_active: bool = ...) -> None: ...
        class ProtectionJobProto(_message.Message):
            __slots__ = ("entity_uuid_map", "policy_name", "job_proto", "last_protection_run")
            ENTITY_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
            POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
            JOB_PROTO_FIELD_NUMBER: _ClassVar[int]
            LAST_PROTECTION_RUN_FIELD_NUMBER: _ClassVar[int]
            entity_uuid_map: _containers.RepeatedCompositeFieldContainer[EntityUuidEntry]
            policy_name: str
            job_proto: _magneto_pb2.BackupJobProto
            last_protection_run: _master_pb2.ProtectionRunStateProto
            def __init__(self, entity_uuid_map: _Optional[_Iterable[_Union[EntityUuidEntry, _Mapping]]] = ..., policy_name: _Optional[str] = ..., job_proto: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., last_protection_run: _Optional[_Union[_master_pb2.ProtectionRunStateProto, _Mapping]] = ...) -> None: ...
        class ProtectionBackupRunProto(_message.Message):
            __slots__ = ("entity_uuid_map", "backup_run", "tenant_id_vec", "policy_id", "is_cloud_archive_direct", "is_cloud_retrieve", "should_process_run_for_entity_updates", "entity_ids_added_since_last_run", "entity_ids_deleted_since_last_run")
            ENTITY_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
            BACKUP_RUN_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            POLICY_ID_FIELD_NUMBER: _ClassVar[int]
            IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
            IS_CLOUD_RETRIEVE_FIELD_NUMBER: _ClassVar[int]
            SHOULD_PROCESS_RUN_FOR_ENTITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
            ENTITY_IDS_ADDED_SINCE_LAST_RUN_FIELD_NUMBER: _ClassVar[int]
            ENTITY_IDS_DELETED_SINCE_LAST_RUN_FIELD_NUMBER: _ClassVar[int]
            entity_uuid_map: _containers.RepeatedCompositeFieldContainer[EntityUuidEntry]
            backup_run: _master_pb2.BackupJobRunStateProto
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            policy_id: str
            is_cloud_archive_direct: bool
            is_cloud_retrieve: bool
            should_process_run_for_entity_updates: bool
            entity_ids_added_since_last_run: _containers.RepeatedScalarFieldContainer[int]
            entity_ids_deleted_since_last_run: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, entity_uuid_map: _Optional[_Iterable[_Union[EntityUuidEntry, _Mapping]]] = ..., backup_run: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., policy_id: _Optional[str] = ..., is_cloud_archive_direct: bool = ..., is_cloud_retrieve: bool = ..., should_process_run_for_entity_updates: bool = ..., entity_ids_added_since_last_run: _Optional[_Iterable[int]] = ..., entity_ids_deleted_since_last_run: _Optional[_Iterable[int]] = ...) -> None: ...
        class ProtectionCopyRunProto(_message.Message):
            __slots__ = ("entity_uuid_map", "copy_run", "tenant_id_vec", "policy_id", "is_cloud_archive_direct", "is_cloud_retrieve", "copy_entity_backup_stats")
            class CopyEntityBackupStatsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: int
                value: _magneto_external_base_pb2.EntityBackupStats
                def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_magneto_external_base_pb2.EntityBackupStats, _Mapping]] = ...) -> None: ...
            ENTITY_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
            COPY_RUN_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            POLICY_ID_FIELD_NUMBER: _ClassVar[int]
            IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
            IS_CLOUD_RETRIEVE_FIELD_NUMBER: _ClassVar[int]
            COPY_ENTITY_BACKUP_STATS_FIELD_NUMBER: _ClassVar[int]
            entity_uuid_map: _containers.RepeatedCompositeFieldContainer[EntityUuidEntry]
            copy_run: _master_pb2.CopyBackupRunStateProto
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            policy_id: str
            is_cloud_archive_direct: bool
            is_cloud_retrieve: bool
            copy_entity_backup_stats: _containers.MessageMap[int, _magneto_external_base_pb2.EntityBackupStats]
            def __init__(self, entity_uuid_map: _Optional[_Iterable[_Union[EntityUuidEntry, _Mapping]]] = ..., copy_run: _Optional[_Union[_master_pb2.CopyBackupRunStateProto, _Mapping]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., policy_id: _Optional[str] = ..., is_cloud_archive_direct: bool = ..., is_cloud_retrieve: bool = ..., copy_entity_backup_stats: _Optional[_Mapping[int, _magneto_external_base_pb2.EntityBackupStats]] = ...) -> None: ...
        class OptimusProcessingMetric(_message.Message):
            __slots__ = ("prana_completion_timestamp_msecs", "eagle_agent_start_timestamp_msecs")
            PRANA_COMPLETION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
            EAGLE_AGENT_START_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
            prana_completion_timestamp_msecs: int
            eagle_agent_start_timestamp_msecs: int
            def __init__(self, prana_completion_timestamp_msecs: _Optional[int] = ..., eagle_agent_start_timestamp_msecs: _Optional[int] = ...) -> None: ...
        class ObjectInfoProto(_message.Message):
            __slots__ = ("entity_uuid_entry", "object_info", "policy_info_vec")
            ENTITY_UUID_ENTRY_FIELD_NUMBER: _ClassVar[int]
            OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
            POLICY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            entity_uuid_entry: EntityUuidEntry
            object_info: bytes
            policy_info_vec: _containers.RepeatedCompositeFieldContainer[PolicyInfo]
            def __init__(self, entity_uuid_entry: _Optional[_Union[EntityUuidEntry, _Mapping]] = ..., object_info: _Optional[bytes] = ..., policy_info_vec: _Optional[_Iterable[_Union[PolicyInfo, _Mapping]]] = ...) -> None: ...
        class ObjectSnapshotProto(_message.Message):
            __slots__ = ("entity_uuid_entry", "object_summary", "policy_info")
            ENTITY_UUID_ENTRY_FIELD_NUMBER: _ClassVar[int]
            OBJECT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
            POLICY_INFO_FIELD_NUMBER: _ClassVar[int]
            entity_uuid_entry: EntityUuidEntry
            object_summary: bytes
            policy_info: PolicyInfo
            def __init__(self, entity_uuid_entry: _Optional[_Union[EntityUuidEntry, _Mapping]] = ..., object_summary: _Optional[bytes] = ..., policy_info: _Optional[_Union[PolicyInfo, _Mapping]] = ...) -> None: ...
        POLICY_PROTO_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_JOB_PROTO_FIELD_NUMBER: _ClassVar[int]
        BACKUP_RUN_PROTO_FIELD_NUMBER: _ClassVar[int]
        COPY_RUN_PROTO_FIELD_NUMBER: _ClassVar[int]
        ENTITY_OBJECT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_OBJECT_FIELD_NUMBER: _ClassVar[int]
        METRIC_OBJECT_FIELD_NUMBER: _ClassVar[int]
        OBJECT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        OBJECT_SNAPSHOT_PROTO_FIELD_NUMBER: _ClassVar[int]
        policy_proto: _policy_pb2.ProtectionPolicyProto
        protection_job_proto: MagnetoStateObject.MagnetoObject.ProtectionJobProto
        backup_run_proto: MagnetoStateObject.MagnetoObject.ProtectionBackupRunProto
        copy_run_proto: MagnetoStateObject.MagnetoObject.ProtectionCopyRunProto
        entity_object: MagnetoStateObject.MagnetoObject.MagnetoEntityObject
        restore_object: MagnetoStateObject.MagnetoObject.RestoreTaskObject
        metric_object: MagnetoStateObject.MagnetoObject.OptimusProcessingMetric
        object_info_proto: MagnetoStateObject.MagnetoObject.ObjectInfoProto
        object_snapshot_proto: MagnetoStateObject.MagnetoObject.ObjectSnapshotProto
        def __init__(self, policy_proto: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., protection_job_proto: _Optional[_Union[MagnetoStateObject.MagnetoObject.ProtectionJobProto, _Mapping]] = ..., backup_run_proto: _Optional[_Union[MagnetoStateObject.MagnetoObject.ProtectionBackupRunProto, _Mapping]] = ..., copy_run_proto: _Optional[_Union[MagnetoStateObject.MagnetoObject.ProtectionCopyRunProto, _Mapping]] = ..., entity_object: _Optional[_Union[MagnetoStateObject.MagnetoObject.MagnetoEntityObject, _Mapping]] = ..., restore_object: _Optional[_Union[MagnetoStateObject.MagnetoObject.RestoreTaskObject, _Mapping]] = ..., metric_object: _Optional[_Union[MagnetoStateObject.MagnetoObject.OptimusProcessingMetric, _Mapping]] = ..., object_info_proto: _Optional[_Union[MagnetoStateObject.MagnetoObject.ObjectInfoProto, _Mapping]] = ..., object_snapshot_proto: _Optional[_Union[MagnetoStateObject.MagnetoObject.ObjectSnapshotProto, _Mapping]] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    object_id: _changelog_pb2.MagnetoObjectId
    magneto_object: MagnetoStateObject.MagnetoObject
    change_id: int
    deleted: bool
    def __init__(self, object_id: _Optional[_Union[_changelog_pb2.MagnetoObjectId, _Mapping]] = ..., magneto_object: _Optional[_Union[MagnetoStateObject.MagnetoObject, _Mapping]] = ..., change_id: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class MagnetoStateObjectBatch(_message.Message):
    __slots__ = ("state_object_vec",)
    STATE_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    state_object_vec: _containers.RepeatedCompositeFieldContainer[MagnetoStateObject]
    def __init__(self, state_object_vec: _Optional[_Iterable[_Union[MagnetoStateObject, _Mapping]]] = ...) -> None: ...

class MagnetoStateCookie(_message.Message):
    __slots__ = ("change_id", "last_collection_usecs", "change_publish_time_usecs")
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PUBLISH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    change_id: int
    last_collection_usecs: int
    change_publish_time_usecs: int
    def __init__(self, change_id: _Optional[int] = ..., last_collection_usecs: _Optional[int] = ..., change_publish_time_usecs: _Optional[int] = ...) -> None: ...

class GlobalEntity(_message.Message):
    __slots__ = ("uuid", "account_id", "entity_proto", "jobs", "registered_source", "change_event_id", "cluster_id_vec", "logical_size_in_bytes", "is_leaf", "tenant_id_vec", "data_channel_type", "tag_uuid_vec", "snapshot_tag_vec", "deleted_cluster_id_vec", "base_uuid")
    class ProtectionJobInfo(_message.Message):
        __slots__ = ("uuid", "job_name", "policy", "last_run_status", "last_run_uuid", "last_run_status_uuid", "is_rpo_job", "is_latest_run_sla_violated", "latest_archival_run_status", "latest_replication_run_status", "is_object_protection", "latest_archival_run", "latest_replication_run", "storage_domain_uid", "is_autoprotected", "protection_env_type")
        class RunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCancelled: _ClassVar[GlobalEntity.ProtectionJobInfo.RunStatus]
            kSuccess: _ClassVar[GlobalEntity.ProtectionJobInfo.RunStatus]
            kFailure: _ClassVar[GlobalEntity.ProtectionJobInfo.RunStatus]
        kCancelled: GlobalEntity.ProtectionJobInfo.RunStatus
        kSuccess: GlobalEntity.ProtectionJobInfo.RunStatus
        kFailure: GlobalEntity.ProtectionJobInfo.RunStatus
        class PolicyInfo(_message.Message):
            __slots__ = ("policy_id", "policy_name")
            POLICY_ID_FIELD_NUMBER: _ClassVar[int]
            POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
            policy_id: str
            policy_name: str
            def __init__(self, policy_id: _Optional[str] = ..., policy_name: _Optional[str] = ...) -> None: ...
        class LatestArchivalRun(_message.Message):
            __slots__ = ("last_run_uuid", "last_run_status", "is_cad", "is_latest_run_sla_violated")
            LAST_RUN_UUID_FIELD_NUMBER: _ClassVar[int]
            LAST_RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
            IS_CAD_FIELD_NUMBER: _ClassVar[int]
            IS_LATEST_RUN_SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
            last_run_uuid: str
            last_run_status: GlobalEntity.ProtectionJobInfo.RunStatus
            is_cad: bool
            is_latest_run_sla_violated: bool
            def __init__(self, last_run_uuid: _Optional[str] = ..., last_run_status: _Optional[_Union[GlobalEntity.ProtectionJobInfo.RunStatus, str]] = ..., is_cad: bool = ..., is_latest_run_sla_violated: bool = ...) -> None: ...
        class LatestReplicationRun(_message.Message):
            __slots__ = ("last_run_uuid", "last_run_status", "is_latest_run_sla_violated")
            LAST_RUN_UUID_FIELD_NUMBER: _ClassVar[int]
            LAST_RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
            IS_LATEST_RUN_SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
            last_run_uuid: str
            last_run_status: GlobalEntity.ProtectionJobInfo.RunStatus
            is_latest_run_sla_violated: bool
            def __init__(self, last_run_uuid: _Optional[str] = ..., last_run_status: _Optional[_Union[GlobalEntity.ProtectionJobInfo.RunStatus, str]] = ..., is_latest_run_sla_violated: bool = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        JOB_NAME_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_UUID_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_STATUS_UUID_FIELD_NUMBER: _ClassVar[int]
        IS_RPO_JOB_FIELD_NUMBER: _ClassVar[int]
        IS_LATEST_RUN_SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
        LATEST_ARCHIVAL_RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
        LATEST_REPLICATION_RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
        IS_OBJECT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
        LATEST_ARCHIVAL_RUN_FIELD_NUMBER: _ClassVar[int]
        LATEST_REPLICATION_RUN_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_UID_FIELD_NUMBER: _ClassVar[int]
        IS_AUTOPROTECTED_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        job_name: str
        policy: GlobalEntity.ProtectionJobInfo.PolicyInfo
        last_run_status: GlobalEntity.ProtectionJobInfo.RunStatus
        last_run_uuid: str
        last_run_status_uuid: str
        is_rpo_job: bool
        is_latest_run_sla_violated: bool
        latest_archival_run_status: GlobalEntity.ProtectionJobInfo.RunStatus
        latest_replication_run_status: GlobalEntity.ProtectionJobInfo.RunStatus
        is_object_protection: bool
        latest_archival_run: GlobalEntity.ProtectionJobInfo.LatestArchivalRun
        latest_replication_run: GlobalEntity.ProtectionJobInfo.LatestReplicationRun
        storage_domain_uid: str
        is_autoprotected: bool
        protection_env_type: int
        def __init__(self, uuid: _Optional[str] = ..., job_name: _Optional[str] = ..., policy: _Optional[_Union[GlobalEntity.ProtectionJobInfo.PolicyInfo, _Mapping]] = ..., last_run_status: _Optional[_Union[GlobalEntity.ProtectionJobInfo.RunStatus, str]] = ..., last_run_uuid: _Optional[str] = ..., last_run_status_uuid: _Optional[str] = ..., is_rpo_job: bool = ..., is_latest_run_sla_violated: bool = ..., latest_archival_run_status: _Optional[_Union[GlobalEntity.ProtectionJobInfo.RunStatus, str]] = ..., latest_replication_run_status: _Optional[_Union[GlobalEntity.ProtectionJobInfo.RunStatus, str]] = ..., is_object_protection: bool = ..., latest_archival_run: _Optional[_Union[GlobalEntity.ProtectionJobInfo.LatestArchivalRun, _Mapping]] = ..., latest_replication_run: _Optional[_Union[GlobalEntity.ProtectionJobInfo.LatestReplicationRun, _Mapping]] = ..., storage_domain_uid: _Optional[str] = ..., is_autoprotected: bool = ..., protection_env_type: _Optional[int] = ...) -> None: ...
    class SnapshotTag(_message.Message):
        __slots__ = ("tag_uuid", "run_uuid_vec")
        TAG_UUID_FIELD_NUMBER: _ClassVar[int]
        RUN_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
        tag_uuid: str
        run_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, tag_uuid: _Optional[str] = ..., run_uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_LEAF_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETED_CLUSTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    account_id: str
    entity_proto: _entity_pb2.EntityProto
    jobs: _containers.RepeatedCompositeFieldContainer[GlobalEntity.ProtectionJobInfo]
    registered_source: RegisteredSource
    change_event_id: int
    cluster_id_vec: _containers.RepeatedScalarFieldContainer[str]
    logical_size_in_bytes: int
    is_leaf: bool
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    data_channel_type: str
    tag_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_tag_vec: _containers.RepeatedCompositeFieldContainer[GlobalEntity.SnapshotTag]
    deleted_cluster_id_vec: _containers.RepeatedScalarFieldContainer[str]
    base_uuid: str
    def __init__(self, uuid: _Optional[str] = ..., account_id: _Optional[str] = ..., entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., jobs: _Optional[_Iterable[_Union[GlobalEntity.ProtectionJobInfo, _Mapping]]] = ..., registered_source: _Optional[_Union[RegisteredSource, _Mapping]] = ..., change_event_id: _Optional[int] = ..., cluster_id_vec: _Optional[_Iterable[str]] = ..., logical_size_in_bytes: _Optional[int] = ..., is_leaf: bool = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., data_channel_type: _Optional[str] = ..., tag_uuid_vec: _Optional[_Iterable[str]] = ..., snapshot_tag_vec: _Optional[_Iterable[_Union[GlobalEntity.SnapshotTag, _Mapping]]] = ..., deleted_cluster_id_vec: _Optional[_Iterable[str]] = ..., base_uuid: _Optional[str] = ...) -> None: ...

class ProtectionJob(_message.Message):
    __slots__ = ("uuid", "account_id", "entity_uuid_vec", "job_proto", "change_event_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_PROTO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    account_id: str
    entity_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    job_proto: _magneto_pb2.BackupJobProto
    change_event_id: int
    def __init__(self, uuid: _Optional[str] = ..., account_id: _Optional[str] = ..., entity_uuid_vec: _Optional[_Iterable[str]] = ..., job_proto: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., change_event_id: _Optional[int] = ...) -> None: ...

class EntityProtectionRun(_message.Message):
    __slots__ = ("uuid", "backup_run_id", "copy_run_id", "account_id", "entity_uuid", "snapshot_type", "backup_task", "copy_task", "task_status", "run_uuid", "snapshot_target", "change_event_id", "tenant_id_vec")
    class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackup: _ClassVar[EntityProtectionRun.SnapshotType]
        kReplication: _ClassVar[EntityProtectionRun.SnapshotType]
        kArchival: _ClassVar[EntityProtectionRun.SnapshotType]
    kBackup: EntityProtectionRun.SnapshotType
    kReplication: EntityProtectionRun.SnapshotType
    kArchival: EntityProtectionRun.SnapshotType
    class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActive: _ClassVar[EntityProtectionRun.TaskStatus]
        kSuccess: _ClassVar[EntityProtectionRun.TaskStatus]
        kFailed: _ClassVar[EntityProtectionRun.TaskStatus]
        kDeleted: _ClassVar[EntityProtectionRun.TaskStatus]
        kSnapshotExpired: _ClassVar[EntityProtectionRun.TaskStatus]
    kActive: EntityProtectionRun.TaskStatus
    kSuccess: EntityProtectionRun.TaskStatus
    kFailed: EntityProtectionRun.TaskStatus
    kDeleted: EntityProtectionRun.TaskStatus
    kSnapshotExpired: EntityProtectionRun.TaskStatus
    UUID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    RUN_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    backup_run_id: _changelog_pb2.MagnetoObjectId.BackupRunId
    copy_run_id: _changelog_pb2.MagnetoObjectId.CopyRunId
    account_id: str
    entity_uuid: str
    snapshot_type: EntityProtectionRun.SnapshotType
    backup_task: _master_pb2.BackupTaskStateProto
    copy_task: _master_pb2.CopyBackupRunTaskStateProto
    task_status: EntityProtectionRun.TaskStatus
    run_uuid: str
    snapshot_target: str
    change_event_id: int
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., backup_run_id: _Optional[_Union[_changelog_pb2.MagnetoObjectId.BackupRunId, _Mapping]] = ..., copy_run_id: _Optional[_Union[_changelog_pb2.MagnetoObjectId.CopyRunId, _Mapping]] = ..., account_id: _Optional[str] = ..., entity_uuid: _Optional[str] = ..., snapshot_type: _Optional[_Union[EntityProtectionRun.SnapshotType, str]] = ..., backup_task: _Optional[_Union[_master_pb2.BackupTaskStateProto, _Mapping]] = ..., copy_task: _Optional[_Union[_master_pb2.CopyBackupRunTaskStateProto, _Mapping]] = ..., task_status: _Optional[_Union[EntityProtectionRun.TaskStatus, str]] = ..., run_uuid: _Optional[str] = ..., snapshot_target: _Optional[str] = ..., change_event_id: _Optional[int] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ProtectionPolicy(_message.Message):
    __slots__ = ("uuid", "account_id", "policy_proto", "change_event_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_PROTO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    account_id: str
    policy_proto: _policy_pb2.ProtectionPolicyProto
    change_event_id: int
    def __init__(self, uuid: _Optional[str] = ..., account_id: _Optional[str] = ..., policy_proto: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., change_event_id: _Optional[int] = ...) -> None: ...
