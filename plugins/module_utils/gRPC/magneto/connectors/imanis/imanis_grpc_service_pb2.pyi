from atom.base import event_pb2 as _event_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base.entities import cassandra_pb2 as _cassandra_pb2
from magneto.base.entities import couchbase_pb2 as _couchbase_pb2
from magneto.base.entities import hbase_pb2 as _hbase_pb2
from magneto.base.entities import hdfs_pb2 as _hdfs_pb2
from magneto.base.entities import hive_pb2 as _hive_pb2
from magneto.base.entities import mongodb_pb2 as _mongodb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CassandraClusterPITRSettings(_message.Message):
    __slots__ = ("archive_log_dir_vec", "data_center_vec", "retain_PIT_metadata_days")
    ARCHIVE_LOG_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    RETAIN_PIT_METADATA_DAYS_FIELD_NUMBER: _ClassVar[int]
    archive_log_dir_vec: _containers.RepeatedScalarFieldContainer[str]
    data_center_vec: _containers.RepeatedScalarFieldContainer[str]
    retain_PIT_metadata_days: int
    def __init__(self, archive_log_dir_vec: _Optional[_Iterable[str]] = ..., data_center_vec: _Optional[_Iterable[str]] = ..., retain_PIT_metadata_days: _Optional[int] = ...) -> None: ...

class SourceConnectorParams(_message.Message):
    __slots__ = ("env_type", "credentials", "source_id", "cassandra_connect_params", "mongodb_connect_params", "couchbase_connect_params", "hbase_connect_params", "hdfs_connect_params", "hive_connect_params")
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    credentials: _credentials_pb2.Credentials
    source_id: int
    cassandra_connect_params: _nosql_pb2.CassandraConnectParams
    mongodb_connect_params: _nosql_pb2.MongoDBConnectParams
    couchbase_connect_params: _nosql_pb2.CouchbaseConnectParams
    hbase_connect_params: _nosql_pb2.HBaseConnectParams
    hdfs_connect_params: _nosql_pb2.HdfsConnectParams
    hive_connect_params: _nosql_pb2.HiveConnectParams
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., source_id: _Optional[int] = ..., cassandra_connect_params: _Optional[_Union[_nosql_pb2.CassandraConnectParams, _Mapping]] = ..., mongodb_connect_params: _Optional[_Union[_nosql_pb2.MongoDBConnectParams, _Mapping]] = ..., couchbase_connect_params: _Optional[_Union[_nosql_pb2.CouchbaseConnectParams, _Mapping]] = ..., hbase_connect_params: _Optional[_Union[_nosql_pb2.HBaseConnectParams, _Mapping]] = ..., hdfs_connect_params: _Optional[_Union[_nosql_pb2.HdfsConnectParams, _Mapping]] = ..., hive_connect_params: _Optional[_Union[_nosql_pb2.HiveConnectParams, _Mapping]] = ...) -> None: ...

class DiscoverSourceArg(_message.Message):
    __slots__ = ("source_connector_params", "hbase_discovery_params", "hdfs_discovery_params", "hive_discovery_params")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: SourceConnectorParams
    hbase_discovery_params: _nosql_pb2.HBaseDiscoveryParams
    hdfs_discovery_params: _nosql_pb2.HdfsDiscoveryParams
    hive_discovery_params: _nosql_pb2.HiveDiscoveryParams
    def __init__(self, source_connector_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., hbase_discovery_params: _Optional[_Union[_nosql_pb2.HBaseDiscoveryParams, _Mapping]] = ..., hdfs_discovery_params: _Optional[_Union[_nosql_pb2.HdfsDiscoveryParams, _Mapping]] = ..., hive_discovery_params: _Optional[_Union[_nosql_pb2.HiveDiscoveryParams, _Mapping]] = ...) -> None: ...

class DiscoverSourceResult(_message.Message):
    __slots__ = ("error", "cassandra_connect_params", "cassandra_additional_params", "hbase_connect_params", "hdfs_connect_params", "hive_connect_params")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cassandra_connect_params: _nosql_pb2.CassandraConnectParams
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    hbase_connect_params: _nosql_pb2.HBaseConnectParams
    hdfs_connect_params: _nosql_pb2.HdfsConnectParams
    hive_connect_params: _nosql_pb2.HiveConnectParams
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cassandra_connect_params: _Optional[_Union[_nosql_pb2.CassandraConnectParams, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ..., hbase_connect_params: _Optional[_Union[_nosql_pb2.HBaseConnectParams, _Mapping]] = ..., hdfs_connect_params: _Optional[_Union[_nosql_pb2.HdfsConnectParams, _Mapping]] = ..., hive_connect_params: _Optional[_Union[_nosql_pb2.HiveConnectParams, _Mapping]] = ...) -> None: ...

class VerifySourceArg(_message.Message):
    __slots__ = ("source_connector_params", "cassandra_additional_params", "mongodb_additional_params", "additional_request_params")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: SourceConnectorParams
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    mongodb_additional_params: _nosql_pb2.MongoDBAdditionalParams
    additional_request_params: AdditionalRequestParams
    def __init__(self, source_connector_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ..., mongodb_additional_params: _Optional[_Union[_nosql_pb2.MongoDBAdditionalParams, _Mapping]] = ..., additional_request_params: _Optional[_Union[AdditionalRequestParams, _Mapping]] = ...) -> None: ...

class VerifySourceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class EntityProto(_message.Message):
    __slots__ = ("type", "cassandra_entity", "mongodb_entity", "couchbase_entity", "hbase_entity", "hdfs_entity", "hive_entity", "magneto_entity_id", "magneto_immediate_ancestor_entity_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HBASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HDFS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HIVE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_IMMEDIATE_ANCESTOR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    cassandra_entity: _cassandra_pb2.Entity
    mongodb_entity: _mongodb_pb2.Entity
    couchbase_entity: _couchbase_pb2.Entity
    hbase_entity: _hbase_pb2.Entity
    hdfs_entity: _hdfs_pb2.Entity
    hive_entity: _hive_pb2.Entity
    magneto_entity_id: int
    magneto_immediate_ancestor_entity_id: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., cassandra_entity: _Optional[_Union[_cassandra_pb2.Entity, _Mapping]] = ..., mongodb_entity: _Optional[_Union[_mongodb_pb2.Entity, _Mapping]] = ..., couchbase_entity: _Optional[_Union[_couchbase_pb2.Entity, _Mapping]] = ..., hbase_entity: _Optional[_Union[_hbase_pb2.Entity, _Mapping]] = ..., hdfs_entity: _Optional[_Union[_hdfs_pb2.Entity, _Mapping]] = ..., hive_entity: _Optional[_Union[_hive_pb2.Entity, _Mapping]] = ..., magneto_entity_id: _Optional[int] = ..., magneto_immediate_ancestor_entity_id: _Optional[int] = ...) -> None: ...

class PageInfo(_message.Message):
    __slots__ = ("offset", "size")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetConnectorInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConnectorInfoResult(_message.Message):
    __slots__ = ("error", "imanis_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IMANIS_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    imanis_version: ImanisVersion
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., imanis_version: _Optional[_Union[ImanisVersion, _Mapping]] = ...) -> None: ...

class GetImanisVersionArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetImanisVersionResult(_message.Message):
    __slots__ = ("error", "imanis_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IMANIS_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    imanis_version: ImanisVersion
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., imanis_version: _Optional[_Union[ImanisVersion, _Mapping]] = ...) -> None: ...

class ImanisVersion(_message.Message):
    __slots__ = ("major_version", "minor_version", "patch_version", "tag")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    patch_version: int
    tag: str
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., patch_version: _Optional[int] = ..., tag: _Optional[str] = ...) -> None: ...

class GetEntitiesArg(_message.Message):
    __slots__ = ("source_connector_params", "parent_entity", "page", "task_id", "cassandra_additional_params", "additional_request_params")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: SourceConnectorParams
    parent_entity: EntityProto
    page: PageInfo
    task_id: int
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    additional_request_params: AdditionalRequestParams
    def __init__(self, source_connector_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., parent_entity: _Optional[_Union[EntityProto, _Mapping]] = ..., page: _Optional[_Union[PageInfo, _Mapping]] = ..., task_id: _Optional[int] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ..., additional_request_params: _Optional[_Union[AdditionalRequestParams, _Mapping]] = ...) -> None: ...

class GetEntitiesResult(_message.Message):
    __slots__ = ("error", "entities", "more", "in_progress")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    MORE_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[EntityProto]
    more: bool
    in_progress: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[EntityProto, _Mapping]]] = ..., more: bool = ..., in_progress: bool = ...) -> None: ...

class AdditionalRequestParams(_message.Message):
    __slots__ = ("priority", "timeout")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    priority: _magneto_pb2.Priority
    timeout: int
    def __init__(self, priority: _Optional[_Union[_magneto_pb2.Priority, str]] = ..., timeout: _Optional[int] = ...) -> None: ...

class LogBackupJobParams(_message.Message):
    __slots__ = ("source_params", "nosql_backup_job_params", "source_id")
    SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    source_params: SourceConnectorParams
    nosql_backup_job_params: _nosql_pb2.NoSqlBackupJobParams
    source_id: int
    def __init__(self, source_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., nosql_backup_job_params: _Optional[_Union[_nosql_pb2.NoSqlBackupJobParams, _Mapping]] = ..., source_id: _Optional[int] = ...) -> None: ...

class BackupJobParams(_message.Message):
    __slots__ = ("source_params", "nosql_backup_job_params", "source_id")
    SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    source_params: SourceConnectorParams
    nosql_backup_job_params: _nosql_pb2.NoSqlBackupJobParams
    source_id: int
    def __init__(self, source_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., nosql_backup_job_params: _Optional[_Union[_nosql_pb2.NoSqlBackupJobParams, _Mapping]] = ..., source_id: _Optional[int] = ...) -> None: ...

class RecoverJobParams(_message.Message):
    __slots__ = ("source_params", "nosql_recover_job_params", "source_id", "destination_id")
    SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    source_params: SourceConnectorParams
    nosql_recover_job_params: _nosql_pb2.NoSqlRecoverJobParams
    source_id: int
    destination_id: int
    def __init__(self, source_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., nosql_recover_job_params: _Optional[_Union[_nosql_pb2.NoSqlRecoverJobParams, _Mapping]] = ..., source_id: _Optional[int] = ..., destination_id: _Optional[int] = ...) -> None: ...

class CompactJobParams(_message.Message):
    __slots__ = ("env_type",)
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class GCJobParams(_message.Message):
    __slots__ = ("backup_job_gc_params",)
    BACKUP_JOB_GC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    backup_job_gc_params: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.BackupJobGCParams]
    def __init__(self, backup_job_gc_params: _Optional[_Iterable[_Union[_nosql_pb2.BackupJobGCParams, _Mapping]]] = ...) -> None: ...

class UpdateNosqlCdpServiceParams(_message.Message):
    __slots__ = ("source_params", "additional_params")
    SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_params: SourceConnectorParams
    additional_params: _nosql_pb2.MongoDBAdditionalParams
    def __init__(self, source_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., additional_params: _Optional[_Union[_nosql_pb2.MongoDBAdditionalParams, _Mapping]] = ...) -> None: ...

class RunId(_message.Message):
    __slots__ = ("job_id", "task_id", "job_instance_id", "attempt_num", "backup_entity_id", "source_id", "mirror_restore_parent_task_id", "run_type")
    class RunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[RunId.RunType]
        kCancel: _ClassVar[RunId.RunType]
    kRegular: RunId.RunType
    kCancel: RunId.RunType
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    MIRROR_RESTORE_PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    task_id: int
    job_instance_id: int
    attempt_num: int
    backup_entity_id: int
    source_id: int
    mirror_restore_parent_task_id: int
    run_type: RunId.RunType
    def __init__(self, job_id: _Optional[int] = ..., task_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., backup_entity_id: _Optional[int] = ..., source_id: _Optional[int] = ..., mirror_restore_parent_task_id: _Optional[int] = ..., run_type: _Optional[_Union[RunId.RunType, str]] = ...) -> None: ...

class RunJobArg(_message.Message):
    __slots__ = ("id", "job_name", "job_type", "view_box_name", "view_name", "previous_snapshot_view_name", "qos_principal_name", "progress_monitor_task_path", "backup_job_params", "recover_job_params", "compact_job_params", "gc_job_params", "virtual_ip_vec", "priority", "io_unit_size", "update_nosql_cdp_service_params", "log_backup_job_params", "prev_view_user_view_tree_id_ceiling", "curr_view_user_view_tree_id_ceiling", "cohesity_cluster_id")
    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackup: _ClassVar[RunJobArg.JobType]
        kRecover: _ClassVar[RunJobArg.JobType]
        kCompaction: _ClassVar[RunJobArg.JobType]
        kGC: _ClassVar[RunJobArg.JobType]
        kFlushCdpLogs: _ClassVar[RunJobArg.JobType]
        kUpdateCdpService: _ClassVar[RunJobArg.JobType]
        kStopCdpService: _ClassVar[RunJobArg.JobType]
        kHydrationBackup: _ClassVar[RunJobArg.JobType]
        kLogBackup: _ClassVar[RunJobArg.JobType]
        kIncrementalRecover: _ClassVar[RunJobArg.JobType]
        kFinaliseRestore: _ClassVar[RunJobArg.JobType]
    kBackup: RunJobArg.JobType
    kRecover: RunJobArg.JobType
    kCompaction: RunJobArg.JobType
    kGC: RunJobArg.JobType
    kFlushCdpLogs: RunJobArg.JobType
    kUpdateCdpService: RunJobArg.JobType
    kStopCdpService: RunJobArg.JobType
    kHydrationBackup: RunJobArg.JobType
    kLogBackup: RunJobArg.JobType
    kIncrementalRecover: RunJobArg.JobType
    kFinaliseRestore: RunJobArg.JobType
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMPACT_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GC_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IO_UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_NOSQL_CDP_SERVICE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PREV_VIEW_USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    CURR_VIEW_USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    id: RunId
    job_name: str
    job_type: RunJobArg.JobType
    view_box_name: str
    view_name: str
    previous_snapshot_view_name: str
    qos_principal_name: str
    progress_monitor_task_path: str
    backup_job_params: BackupJobParams
    recover_job_params: RecoverJobParams
    compact_job_params: CompactJobParams
    gc_job_params: GCJobParams
    virtual_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    priority: _magneto_pb2.Priority
    io_unit_size: int
    update_nosql_cdp_service_params: UpdateNosqlCdpServiceParams
    log_backup_job_params: LogBackupJobParams
    prev_view_user_view_tree_id_ceiling: int
    curr_view_user_view_tree_id_ceiling: int
    cohesity_cluster_id: int
    def __init__(self, id: _Optional[_Union[RunId, _Mapping]] = ..., job_name: _Optional[str] = ..., job_type: _Optional[_Union[RunJobArg.JobType, str]] = ..., view_box_name: _Optional[str] = ..., view_name: _Optional[str] = ..., previous_snapshot_view_name: _Optional[str] = ..., qos_principal_name: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., backup_job_params: _Optional[_Union[BackupJobParams, _Mapping]] = ..., recover_job_params: _Optional[_Union[RecoverJobParams, _Mapping]] = ..., compact_job_params: _Optional[_Union[CompactJobParams, _Mapping]] = ..., gc_job_params: _Optional[_Union[GCJobParams, _Mapping]] = ..., virtual_ip_vec: _Optional[_Iterable[str]] = ..., priority: _Optional[_Union[_magneto_pb2.Priority, str]] = ..., io_unit_size: _Optional[int] = ..., update_nosql_cdp_service_params: _Optional[_Union[UpdateNosqlCdpServiceParams, _Mapping]] = ..., log_backup_job_params: _Optional[_Union[LogBackupJobParams, _Mapping]] = ..., prev_view_user_view_tree_id_ceiling: _Optional[int] = ..., curr_view_user_view_tree_id_ceiling: _Optional[int] = ..., cohesity_cluster_id: _Optional[int] = ...) -> None: ...

class RunJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelJobArg(_message.Message):
    __slots__ = ("id", "job_type", "cancellation_reason")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[CancelJobArg.Reason]
        kCancellingPreviousRun: _ClassVar[CancelJobArg.Reason]
        kErrorsOccurredInCurrentRun: _ClassVar[CancelJobArg.Reason]
        kCancellationRequested: _ClassVar[CancelJobArg.Reason]
    kUnknown: CancelJobArg.Reason
    kCancellingPreviousRun: CancelJobArg.Reason
    kErrorsOccurredInCurrentRun: CancelJobArg.Reason
    kCancellationRequested: CancelJobArg.Reason
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    id: RunId
    job_type: RunJobArg.JobType
    cancellation_reason: CancelJobArg.Reason
    def __init__(self, id: _Optional[_Union[RunId, _Mapping]] = ..., job_type: _Optional[_Union[RunJobArg.JobType, str]] = ..., cancellation_reason: _Optional[_Union[CancelJobArg.Reason, str]] = ...) -> None: ...

class CancelJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetJobStatusArg(_message.Message):
    __slots__ = ("id", "job_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: RunId
    job_type: RunJobArg.JobType
    def __init__(self, id: _Optional[_Union[RunId, _Mapping]] = ..., job_type: _Optional[_Union[RunJobArg.JobType, str]] = ...) -> None: ...

class GetJobStatusResult(_message.Message):
    __slots__ = ("status", "progress_percent", "error", "stats")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[GetJobStatusResult.Status]
        kCompleted: _ClassVar[GetJobStatusResult.Status]
    kRunning: GetJobStatusResult.Status
    kCompleted: GetJobStatusResult.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    status: GetJobStatusResult.Status
    progress_percent: int
    error: _error_pb2.ErrorProto
    stats: _nosql_pb2.NoSqlStats
    def __init__(self, status: _Optional[_Union[GetJobStatusResult.Status, str]] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[_nosql_pb2.NoSqlStats, _Mapping]] = ...) -> None: ...

class GetCompletedJobDetailsArg(_message.Message):
    __slots__ = ("id", "job_type", "populate_successfull_objects")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    POPULATE_SUCCESSFULL_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    id: RunId
    job_type: RunJobArg.JobType
    populate_successfull_objects: bool
    def __init__(self, id: _Optional[_Union[RunId, _Mapping]] = ..., job_type: _Optional[_Union[RunJobArg.JobType, str]] = ..., populate_successfull_objects: bool = ...) -> None: ...

class ImanisError(_message.Message):
    __slots__ = ("object_name", "cause", "action")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    cause: str
    action: str
    def __init__(self, object_name: _Optional[str] = ..., cause: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class CassandraAdditionalCompletedJobDetails(_message.Message):
    __slots__ = ("source_claim_overwritten",)
    SOURCE_CLAIM_OVERWRITTEN_FIELD_NUMBER: _ClassVar[int]
    source_claim_overwritten: bool
    def __init__(self, source_claim_overwritten: bool = ...) -> None: ...

class AdditionalCompletedJobDetails(_message.Message):
    __slots__ = ("cassandra_details",)
    CASSANDRA_DETAILS_FIELD_NUMBER: _ClassVar[int]
    cassandra_details: CassandraAdditionalCompletedJobDetails
    def __init__(self, cassandra_details: _Optional[_Union[CassandraAdditionalCompletedJobDetails, _Mapping]] = ...) -> None: ...

class GetCompletedJobDetailsResult(_message.Message):
    __slots__ = ("status", "yoda_entities_path", "stats", "error", "fatal", "warnings", "successful_objects", "additional_job_details")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFailure: _ClassVar[GetCompletedJobDetailsResult.Status]
        kPartialSuccess: _ClassVar[GetCompletedJobDetailsResult.Status]
        kSuccess: _ClassVar[GetCompletedJobDetailsResult.Status]
    kFailure: GetCompletedJobDetailsResult.Status
    kPartialSuccess: GetCompletedJobDetailsResult.Status
    kSuccess: GetCompletedJobDetailsResult.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    YODA_ENTITIES_PATH_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FATAL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: GetCompletedJobDetailsResult.Status
    yoda_entities_path: str
    stats: _nosql_pb2.NoSqlStats
    error: _error_pb2.ErrorProto
    fatal: ImanisError
    warnings: _containers.RepeatedCompositeFieldContainer[ImanisError]
    successful_objects: _containers.RepeatedScalarFieldContainer[str]
    additional_job_details: AdditionalCompletedJobDetails
    def __init__(self, status: _Optional[_Union[GetCompletedJobDetailsResult.Status, str]] = ..., yoda_entities_path: _Optional[str] = ..., stats: _Optional[_Union[_nosql_pb2.NoSqlStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fatal: _Optional[_Union[ImanisError, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[ImanisError, _Mapping]]] = ..., successful_objects: _Optional[_Iterable[str]] = ..., additional_job_details: _Optional[_Union[AdditionalCompletedJobDetails, _Mapping]] = ...) -> None: ...

class GetEntitySizeArg(_message.Message):
    __slots__ = ("source_connector_params", "entity", "cassandra_additional_params")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: SourceConnectorParams
    entity: EntityProto
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    def __init__(self, source_connector_params: _Optional[_Union[SourceConnectorParams, _Mapping]] = ..., entity: _Optional[_Union[EntityProto, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ...) -> None: ...

class GetEntitySizeResult(_message.Message):
    __slots__ = ("error", "size")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    size: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., size: _Optional[int] = ...) -> None: ...

class SendEntitiesArg(_message.Message):
    __slots__ = ("id", "job_type", "backup_entities", "restore_objects", "page_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: RunId
    job_type: RunJobArg.JobType
    backup_entities: _containers.RepeatedCompositeFieldContainer[EntityProto]
    restore_objects: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.NoSqlRestoreObject]
    page_number: int
    def __init__(self, id: _Optional[_Union[RunId, _Mapping]] = ..., job_type: _Optional[_Union[RunJobArg.JobType, str]] = ..., backup_entities: _Optional[_Iterable[_Union[EntityProto, _Mapping]]] = ..., restore_objects: _Optional[_Iterable[_Union[_nosql_pb2.NoSqlRestoreObject, _Mapping]]] = ..., page_number: _Optional[int] = ...) -> None: ...

class SendEntitiesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotLogsMetadata(_message.Message):
    __slots__ = ("entity_log_vec", "start_sequencer", "end_sequencer", "atom_view_name", "atom_view_box_name")
    class EntityLog(_message.Message):
        __slots__ = ("entity", "log_data_vec", "entity_id")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        entity: EntityProto
        log_data_vec: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.NoSqlLogData]
        entity_id: int
        def __init__(self, entity: _Optional[_Union[EntityProto, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[_nosql_pb2.NoSqlLogData, _Mapping]]] = ..., entity_id: _Optional[int] = ...) -> None: ...
    ENTITY_LOG_VEC_FIELD_NUMBER: _ClassVar[int]
    START_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    END_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    ATOM_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ATOM_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_log_vec: _containers.RepeatedCompositeFieldContainer[SnapshotLogsMetadata.EntityLog]
    start_sequencer: _event_pb2.Sequencer
    end_sequencer: _event_pb2.Sequencer
    atom_view_name: str
    atom_view_box_name: str
    def __init__(self, entity_log_vec: _Optional[_Iterable[_Union[SnapshotLogsMetadata.EntityLog, _Mapping]]] = ..., start_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., atom_view_name: _Optional[str] = ..., atom_view_box_name: _Optional[str] = ...) -> None: ...
