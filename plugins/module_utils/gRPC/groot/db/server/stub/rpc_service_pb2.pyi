from open_util.net import protorpc_pb2 as _protorpc_pb2
from groot.base import error_pb2 as _error_pb2
from groot.db.base import reporting_dao_pb2 as _reporting_dao_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteDdlQueryArg(_message.Message):
    __slots__ = ("epoch_id", "query_type", "query")
    class QueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateDb: _ClassVar[ExecuteDdlQueryArg.QueryType]
        kDeleteDb: _ClassVar[ExecuteDdlQueryArg.QueryType]
        kCreateTable: _ClassVar[ExecuteDdlQueryArg.QueryType]
        kDeleteTable: _ClassVar[ExecuteDdlQueryArg.QueryType]
        kAlterTable: _ClassVar[ExecuteDdlQueryArg.QueryType]
    kCreateDb: ExecuteDdlQueryArg.QueryType
    kDeleteDb: ExecuteDdlQueryArg.QueryType
    kCreateTable: ExecuteDdlQueryArg.QueryType
    kDeleteTable: ExecuteDdlQueryArg.QueryType
    kAlterTable: ExecuteDdlQueryArg.QueryType
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    query_type: ExecuteDdlQueryArg.QueryType
    query: bytes
    def __init__(self, epoch_id: _Optional[int] = ..., query_type: _Optional[_Union[ExecuteDdlQueryArg.QueryType, str]] = ..., query: _Optional[bytes] = ...) -> None: ...

class ExecuteDdlQueryResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ExecuteWriteQueryArg(_message.Message):
    __slots__ = ("epoch_id", "query_type", "query")
    class QueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInsert: _ClassVar[ExecuteWriteQueryArg.QueryType]
        kDelete: _ClassVar[ExecuteWriteQueryArg.QueryType]
        kUpdate: _ClassVar[ExecuteWriteQueryArg.QueryType]
    kInsert: ExecuteWriteQueryArg.QueryType
    kDelete: ExecuteWriteQueryArg.QueryType
    kUpdate: ExecuteWriteQueryArg.QueryType
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    query_type: ExecuteWriteQueryArg.QueryType
    query: bytes
    def __init__(self, epoch_id: _Optional[int] = ..., query_type: _Optional[_Union[ExecuteWriteQueryArg.QueryType, str]] = ..., query: _Optional[bytes] = ...) -> None: ...

class ExecuteWriteQueryResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ("upper_limit", "lower_limit")
    UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    upper_limit: int
    lower_limit: int
    def __init__(self, upper_limit: _Optional[int] = ..., lower_limit: _Optional[int] = ...) -> None: ...

class UpdateTableArg(_message.Message):
    __slots__ = ("epoch_id", "table_name", "backup_job_dao_vec", "registered_source_dao_vec", "leaf_entity_dao_vec", "job_entity_dao_vec", "cluster_dao_vec", "partition_dao_vec", "rack_dao_vec", "chassis_dao_vec", "node_dao_vec", "view_box_dao_vec", "view_dao_vec", "view_alias_dao_vec", "archival_target_dao_vec", "job_run_dao_vec", "job_run_entity_dao_vec", "job_run_replication_dao_vec", "job_run_replication_entity_dao_vec", "job_run_archival_dao_vec", "io_performance_stats_dao_vec", "resource_usage_stats_dao_vec", "storage_usage_stats_dao_vec", "remote_cluster_dao_vec", "remote_cluster_view_box_dao_vec", "protection_policy_dao_vec", "back_up_schedule_dao_vec", "policy_replication_schedule_dao_vec", "policy_archival_schedule_dao_vec", "restored_object_dao_vec", "restore_task_dao_vec", "tenant_dao_vec", "tenant_view_box_map_dao_vec", "tenant_protection_policy_map_dao_vec", "apollo_pipeline_run_dao_vec", "yoda_index_run_dao_vec", "tenant_storage_stats_dao_vec", "view_storage_stats_dao_vec", "job_storage_stats_dao_vec", "parent_id", "view_id_range", "using_pubsub", "leaf_entity_id_vec", "mark_as_deleted", "registered_source_id_vec")
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    LEAF_ENTITY_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ENTITY_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    RACK_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALIAS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ENTITY_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_REPLICATION_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_REPLICATION_ENTITY_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ARCHIVAL_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    IO_PERFORMANCE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_USAGE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_VIEW_BOX_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    BACK_UP_SCHEDULE_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    POLICY_REPLICATION_SCHEDULE_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    POLICY_ARCHIVAL_SCHEDULE_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECT_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_VIEW_BOX_MAP_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_PROTECTION_POLICY_MAP_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    APOLLO_PIPELINE_RUN_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    YODA_INDEX_RUN_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_STORAGE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_STORAGE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_STORAGE_STATS_DAO_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_RANGE_FIELD_NUMBER: _ClassVar[int]
    USING_PUBSUB_FIELD_NUMBER: _ClassVar[int]
    LEAF_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MARK_AS_DELETED_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    table_name: str
    backup_job_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.BackupJobDao]
    registered_source_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RegisteredSourceDao]
    leaf_entity_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.LeafEntityDao]
    job_entity_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobEntityDao]
    cluster_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ClusterDao]
    partition_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.PartitionDao]
    rack_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RackDao]
    chassis_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ChassisDao]
    node_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.NodeDao]
    view_box_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ViewBoxDao]
    view_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ViewDao]
    view_alias_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ViewAliasDao]
    archival_target_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ArchivalTargetDao]
    job_run_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobRunDao]
    job_run_entity_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobRunEntityDao]
    job_run_replication_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobRunReplicationDao]
    job_run_replication_entity_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobRunReplicationEntityDao]
    job_run_archival_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobRunArchivalDao]
    io_performance_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.IOPerformanceStatsDao]
    resource_usage_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ResourceUsageStatsDao]
    storage_usage_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.StorageUsageStatsDao]
    remote_cluster_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RemoteClusterDao]
    remote_cluster_view_box_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RemoteClusterViewBoxDao]
    protection_policy_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ProtectionPolicyDao]
    back_up_schedule_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.BackUpScheduleDao]
    policy_replication_schedule_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.PolicyReplicationScheduleDao]
    policy_archival_schedule_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.PolicyArchivalScheduleDao]
    restored_object_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RestoredObjectDao]
    restore_task_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.RestoreTaskDao]
    tenant_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.TenantDao]
    tenant_view_box_map_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.TenantViewBoxMapDao]
    tenant_protection_policy_map_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.TenantProtectionPolicyMapDao]
    apollo_pipeline_run_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ApolloPipelineRunDao]
    yoda_index_run_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.YodaIndexRunDao]
    tenant_storage_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.TenantStorageStatsDao]
    view_storage_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.ViewStorageStatsDao]
    job_storage_stats_dao_vec: _containers.RepeatedCompositeFieldContainer[_reporting_dao_pb2.JobStorageStatsDao]
    parent_id: int
    view_id_range: Range
    using_pubsub: bool
    leaf_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    mark_as_deleted: bool
    registered_source_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, epoch_id: _Optional[int] = ..., table_name: _Optional[str] = ..., backup_job_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.BackupJobDao, _Mapping]]] = ..., registered_source_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RegisteredSourceDao, _Mapping]]] = ..., leaf_entity_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.LeafEntityDao, _Mapping]]] = ..., job_entity_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobEntityDao, _Mapping]]] = ..., cluster_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ClusterDao, _Mapping]]] = ..., partition_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.PartitionDao, _Mapping]]] = ..., rack_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RackDao, _Mapping]]] = ..., chassis_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ChassisDao, _Mapping]]] = ..., node_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.NodeDao, _Mapping]]] = ..., view_box_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ViewBoxDao, _Mapping]]] = ..., view_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ViewDao, _Mapping]]] = ..., view_alias_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ViewAliasDao, _Mapping]]] = ..., archival_target_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ArchivalTargetDao, _Mapping]]] = ..., job_run_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobRunDao, _Mapping]]] = ..., job_run_entity_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobRunEntityDao, _Mapping]]] = ..., job_run_replication_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobRunReplicationDao, _Mapping]]] = ..., job_run_replication_entity_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobRunReplicationEntityDao, _Mapping]]] = ..., job_run_archival_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobRunArchivalDao, _Mapping]]] = ..., io_performance_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.IOPerformanceStatsDao, _Mapping]]] = ..., resource_usage_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ResourceUsageStatsDao, _Mapping]]] = ..., storage_usage_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.StorageUsageStatsDao, _Mapping]]] = ..., remote_cluster_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RemoteClusterDao, _Mapping]]] = ..., remote_cluster_view_box_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RemoteClusterViewBoxDao, _Mapping]]] = ..., protection_policy_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ProtectionPolicyDao, _Mapping]]] = ..., back_up_schedule_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.BackUpScheduleDao, _Mapping]]] = ..., policy_replication_schedule_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.PolicyReplicationScheduleDao, _Mapping]]] = ..., policy_archival_schedule_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.PolicyArchivalScheduleDao, _Mapping]]] = ..., restored_object_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RestoredObjectDao, _Mapping]]] = ..., restore_task_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.RestoreTaskDao, _Mapping]]] = ..., tenant_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.TenantDao, _Mapping]]] = ..., tenant_view_box_map_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.TenantViewBoxMapDao, _Mapping]]] = ..., tenant_protection_policy_map_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.TenantProtectionPolicyMapDao, _Mapping]]] = ..., apollo_pipeline_run_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ApolloPipelineRunDao, _Mapping]]] = ..., yoda_index_run_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.YodaIndexRunDao, _Mapping]]] = ..., tenant_storage_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.TenantStorageStatsDao, _Mapping]]] = ..., view_storage_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.ViewStorageStatsDao, _Mapping]]] = ..., job_storage_stats_dao_vec: _Optional[_Iterable[_Union[_reporting_dao_pb2.JobStorageStatsDao, _Mapping]]] = ..., parent_id: _Optional[int] = ..., view_id_range: _Optional[_Union[Range, _Mapping]] = ..., using_pubsub: bool = ..., leaf_entity_id_vec: _Optional[_Iterable[int]] = ..., mark_as_deleted: bool = ..., registered_source_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateTableResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
