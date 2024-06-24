from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("base", "stats", "task_id", "snapshot_id", "admitted_time_usecs", "stats_container_id", "source_snapshot_creation_time_usecs", "total_file_count", "total_changed_file_count", "file_walk_done")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMITTED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANGED_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILE_WALK_DONE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.TaskBaseProto
    stats: _magneto_external_base_pb2.SnapshotStats
    task_id: int
    snapshot_id: str
    admitted_time_usecs: int
    stats_container_id: int
    source_snapshot_creation_time_usecs: int
    total_file_count: int
    total_changed_file_count: int
    file_walk_done: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.TaskBaseProto, _Mapping]] = ..., stats: _Optional[_Union[_magneto_external_base_pb2.SnapshotStats, _Mapping]] = ..., task_id: _Optional[int] = ..., snapshot_id: _Optional[str] = ..., admitted_time_usecs: _Optional[int] = ..., stats_container_id: _Optional[int] = ..., source_snapshot_creation_time_usecs: _Optional[int] = ..., total_file_count: _Optional[int] = ..., total_changed_file_count: _Optional[int] = ..., file_walk_done: bool = ...) -> None: ...

class ObjectLocalSnapshotInfo(_message.Message):
    __slots__ = ("snapshot_info", "failed_attempts", "storage_domain_id", "snapshot_expiry_info", "indexing_task_path")
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    FAILED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEXING_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: SnapshotInfo
    failed_attempts: _containers.RepeatedCompositeFieldContainer[SnapshotInfo]
    storage_domain_id: int
    snapshot_expiry_info: _magneto_external_base_pb2.SnapshotExpiryInfoProto
    indexing_task_path: str
    def __init__(self, snapshot_info: _Optional[_Union[SnapshotInfo, _Mapping]] = ..., failed_attempts: _Optional[_Iterable[_Union[SnapshotInfo, _Mapping]]] = ..., storage_domain_id: _Optional[int] = ..., snapshot_expiry_info: _Optional[_Union[_magneto_external_base_pb2.SnapshotExpiryInfoProto, _Mapping]] = ..., indexing_task_path: _Optional[str] = ...) -> None: ...

class ObjectRunInfo(_message.Message):
    __slots__ = ("job_uid", "local_snapshot_info", "replication_target_results", "archival_target_results", "cloud_spin_target_results", "onprem_deploy_target_results", "basic_run_info", "additional_protection_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPIN_TARGET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ONPREM_DEPLOY_TARGET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    BASIC_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROTECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    local_snapshot_info: ObjectLocalSnapshotInfo
    replication_target_results: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
    archival_target_results: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ArchivalInfoProto]
    cloud_spin_target_results: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.CloudSpinInfoProto]
    onprem_deploy_target_results: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.OnPremDeployInfoProto]
    basic_run_info: BasicRunInfo
    additional_protection_info: AdditionalProtectionInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., local_snapshot_info: _Optional[_Union[ObjectLocalSnapshotInfo, _Mapping]] = ..., replication_target_results: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ..., archival_target_results: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ArchivalInfoProto, _Mapping]]] = ..., cloud_spin_target_results: _Optional[_Iterable[_Union[_magneto_external_base_pb2.CloudSpinInfoProto, _Mapping]]] = ..., onprem_deploy_target_results: _Optional[_Iterable[_Union[_magneto_external_base_pb2.OnPremDeployInfoProto, _Mapping]]] = ..., basic_run_info: _Optional[_Union[BasicRunInfo, _Mapping]] = ..., additional_protection_info: _Optional[_Union[AdditionalProtectionInfo, _Mapping]] = ...) -> None: ...

class BasicRunInfo(_message.Message):
    __slots__ = ("run_start_time_usecs", "instance_id", "origin_cluster_identifier", "is_incoming_replication", "backup_type", "is_sla_violated", "is_out_of_band_run", "run_label")
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_INCOMING_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SLA_VIOLATED_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_RUN_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    instance_id: int
    origin_cluster_identifier: _magneto_external_base_pb2.ClusterIdentifierProto
    is_incoming_replication: bool
    backup_type: _enum_wrappers_pb2.MagnetoBackupType
    is_sla_violated: bool
    is_out_of_band_run: bool
    run_label: str
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., instance_id: _Optional[int] = ..., origin_cluster_identifier: _Optional[_Union[_magneto_external_base_pb2.ClusterIdentifierProto, _Mapping]] = ..., is_incoming_replication: bool = ..., backup_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., is_sla_violated: bool = ..., is_out_of_band_run: bool = ..., run_label: _Optional[str] = ...) -> None: ...

class AdditionalProtectionInfo(_message.Message):
    __slots__ = ("is_cloud_archive_direct", "job_uid", "job_name", "spec_uid", "action_key", "network_realm_id", "connector_group_id")
    IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_UID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    is_cloud_archive_direct: bool
    job_uid: _universal_id_pb2.UniversalIdProto
    job_name: str
    spec_uid: _universal_id_pb2.UniversalIdProto
    action_key: _magneto_external_base_pb2.ObjectActionKey
    network_realm_id: int
    connector_group_id: int
    def __init__(self, is_cloud_archive_direct: bool = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_name: _Optional[str] = ..., spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ...) -> None: ...

class ObjectSummary(_message.Message):
    __slots__ = ("object", "runs_info")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
    object: _magneto_external_base_pb2.ObjectProto
    runs_info: _containers.RepeatedCompositeFieldContainer[ObjectRunInfo]
    def __init__(self, object: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., runs_info: _Optional[_Iterable[_Union[ObjectRunInfo, _Mapping]]] = ...) -> None: ...

class ProtectionGroupRunInfo(_message.Message):
    __slots__ = ("run_start_time_usecs", "instance_id", "basic_run_info", "uid", "name", "backup_type", "is_replication_run", "origin_cluster_identifier", "objects", "local_backup_info", "replication_info_vec", "archival_info_vec", "cloud_spin_info_vec", "onprem_deploy_info_vec")
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASIC_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_REPLICATION_RUN_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ONPREM_DEPLOY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    instance_id: int
    basic_run_info: BasicRunInfo
    uid: _universal_id_pb2.UniversalIdProto
    name: str
    backup_type: _enum_wrappers_pb2.MagnetoBackupType
    is_replication_run: bool
    origin_cluster_identifier: _magneto_external_base_pb2.ClusterIdentifierProto
    objects: _containers.RepeatedCompositeFieldContainer[ObjectSummary]
    local_backup_info: _magneto_external_base_pb2.LocalBackupRunInfo
    replication_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
    archival_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ArchivalInfoProto]
    cloud_spin_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.CloudSpinInfoProto]
    onprem_deploy_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.OnPremDeployInfoProto]
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., instance_id: _Optional[int] = ..., basic_run_info: _Optional[_Union[BasicRunInfo, _Mapping]] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., backup_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., is_replication_run: bool = ..., origin_cluster_identifier: _Optional[_Union[_magneto_external_base_pb2.ClusterIdentifierProto, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[ObjectSummary, _Mapping]]] = ..., local_backup_info: _Optional[_Union[_magneto_external_base_pb2.LocalBackupRunInfo, _Mapping]] = ..., replication_info_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ..., archival_info_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ArchivalInfoProto, _Mapping]]] = ..., cloud_spin_info_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.CloudSpinInfoProto, _Mapping]]] = ..., onprem_deploy_info_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.OnPremDeployInfoProto, _Mapping]]] = ...) -> None: ...

class EntityExternalMetadata(_message.Message):
    __slots__ = ("environment", "parent_source_uuid", "entity_uuid", "vmware_metadata")
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_METADATA_FIELD_NUMBER: _ClassVar[int]
    environment: _enum_wrappers_pb2.EnvironmentProto
    parent_source_uuid: str
    entity_uuid: str
    vmware_metadata: VMwareEntityExternalMetadata
    def __init__(self, environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., parent_source_uuid: _Optional[str] = ..., entity_uuid: _Optional[str] = ..., vmware_metadata: _Optional[_Union[VMwareEntityExternalMetadata, _Mapping]] = ...) -> None: ...

class VMwareEntityExternalMetadata(_message.Message):
    __slots__ = ("vcenter_static_id",)
    VCENTER_STATIC_ID_FIELD_NUMBER: _ClassVar[int]
    vcenter_static_id: int
    def __init__(self, vcenter_static_id: _Optional[int] = ...) -> None: ...
