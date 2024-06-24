from google.protobuf import descriptor_pb2 as _descriptor_pb2
from atom.base import atom_pb2 as _atom_pb2
from atom.base import event_pb2 as _event_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.api.common import aws_rds_pb2 as _aws_rds_pb2
from magneto.api.common import oracle_pb2 as _oracle_pb2
from magneto.api.common import azure_sql_pb2 as _azure_sql_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.agents.windows.o365spo import o365spo_pb2 as _o365spo_pb2
from magneto.agents.windows.stub import ad_param_pb2 as _ad_param_pb2
from magneto.agents.windows.stub import exchange_param_pb2 as _exchange_param_pb2
from magneto.api.common import entity_operations_pb2 as _entity_operations_pb2
from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base.entities import azure_pb2 as _azure_pb2
from magneto.base.entities import kubernetes_pb2 as _kubernetes_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.base.entities import oracle_pb2 as _oracle_pb2_1
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base import uda_pb2 as _uda_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import schedule_pb2 as _schedule_pb2
from magneto.base import source_throttling_pb2 as _source_throttling_pb2
from magneto.connectors.kubernetes import kubernetes_api_pb2 as _kubernetes_api_pb2
from magneto.connectors.ms_graph import graph_enums_pb2 as _graph_enums_pb2
from magneto.connectors.o365 import o365_additional_pb2 as _o365_additional_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from magneto.base.env_params_pb2 import AlertingPolicyProto as AlertingPolicyProto
from magneto.base.env_params_pb2 import IndexingPolicyProto as IndexingPolicyProto
from magneto.base.env_params_pb2 import AWSSnapshotManagerParams as AWSSnapshotManagerParams
from magneto.base.env_params_pb2 import SnapshotManagerParams as SnapshotManagerParams
from magneto.base.env_params_pb2 import AcropolisDiskFilterProto as AcropolisDiskFilterProto
from magneto.base.env_params_pb2 import VMwareDiskExclusionProto as VMwareDiskExclusionProto
from magneto.base.env_params_pb2 import HyperVDiskFilterProto as HyperVDiskFilterProto
from magneto.base.env_params_pb2 import MSExchangeParams as MSExchangeParams
from magneto.base.env_params_pb2 import SourceAppParams as SourceAppParams
from magneto.base.env_params_pb2 import PhysicalSnapshotParams as PhysicalSnapshotParams
from magneto.base.env_params_pb2 import PhysicalFileBackupParams as PhysicalFileBackupParams
from magneto.base.env_params_pb2 import PhysicalBackupSourceParams as PhysicalBackupSourceParams
from magneto.base.env_params_pb2 import VMwareBackupSourceParams as VMwareBackupSourceParams
from magneto.base.env_params_pb2 import HyperVBackupSourceParams as HyperVBackupSourceParams
from magneto.base.env_params_pb2 import AcropolisBackupSourceParams as AcropolisBackupSourceParams
from magneto.base.env_params_pb2 import UdaBackupSourceParams as UdaBackupSourceParams
from magneto.base.env_params_pb2 import KubernetesBackupSourceParams as KubernetesBackupSourceParams
from magneto.base.env_params_pb2 import OracleRmanBackupType as OracleRmanBackupType
from magneto.base.env_params_pb2 import OracleArchiveLogRetentionType as OracleArchiveLogRetentionType
from magneto.base.env_params_pb2 import OracleVlanInfo as OracleVlanInfo
from magneto.base.env_params_pb2 import OracleSbtHostParams as OracleSbtHostParams
from magneto.base.env_params_pb2 import OracleDBChannelInfo as OracleDBChannelInfo
from magneto.base.env_params_pb2 import AdditionalOracleDBParams as AdditionalOracleDBParams
from magneto.base.env_params_pb2 import OracleSourceParams as OracleSourceParams
from magneto.base.env_params_pb2 import NasThrottlingParams as NasThrottlingParams
from magneto.base.env_params_pb2 import UdaThrottlingParams as UdaThrottlingParams
from magneto.base.env_params_pb2 import AWSNativeBackupSourceParams as AWSNativeBackupSourceParams
from magneto.base.env_params_pb2 import AWSSnapshotManagerBackupSourceParams as AWSSnapshotManagerBackupSourceParams
from magneto.base.env_params_pb2 import GCPNativeObjectParams as GCPNativeObjectParams
from magneto.base.env_params_pb2 import SharepointBackupSourceParams as SharepointBackupSourceParams
from magneto.base.env_params_pb2 import S3BucketParamsProto as S3BucketParamsProto
from magneto.base.env_params_pb2 import BackupSourceParams as BackupSourceParams
from magneto.base.env_params_pb2 import FilteringPolicyProto as FilteringPolicyProto
from magneto.base.env_params_pb2 import NasBackupParams as NasBackupParams
from magneto.base.env_params_pb2 import S3ViewBackupProperties as S3ViewBackupProperties
from magneto.base.env_params_pb2 import PhysicalBackupEnvParams as PhysicalBackupEnvParams
from magneto.base.env_params_pb2 import VMwareBackupEnvParams as VMwareBackupEnvParams
from magneto.base.env_params_pb2 import SqlBackupJobParams as SqlBackupJobParams
from magneto.base.env_params_pb2 import OracleBackupJobParams as OracleBackupJobParams
from magneto.base.env_params_pb2 import AcropolisBackupJobParams as AcropolisBackupJobParams
from magneto.base.env_params_pb2 import SanBackupJobParams as SanBackupJobParams
from magneto.base.env_params_pb2 import ExternallyTriggeredJobParams as ExternallyTriggeredJobParams
from magneto.base.env_params_pb2 import HyperVBackupEnvParams as HyperVBackupEnvParams
from magneto.base.env_params_pb2 import AttributeFilterParams as AttributeFilterParams
from magneto.base.env_params_pb2 import AttributeFilterPolicy as AttributeFilterPolicy
from magneto.base.env_params_pb2 import OutlookBackupEnvParams as OutlookBackupEnvParams
from magneto.base.env_params_pb2 import OneDriveBackupEnvParams as OneDriveBackupEnvParams
from magneto.base.env_params_pb2 import SharepPointSiteBackupEnvParams as SharepPointSiteBackupEnvParams
from magneto.base.env_params_pb2 import GroupBackupEnvParams as GroupBackupEnvParams
from magneto.base.env_params_pb2 import TeamsBackupEnvParams as TeamsBackupEnvParams
from magneto.base.env_params_pb2 import PublicFoldersBackupEnvParams as PublicFoldersBackupEnvParams
from magneto.base.env_params_pb2 import O365BackupEnvParams as O365BackupEnvParams
from magneto.base.env_params_pb2 import FileUptieringParams as FileUptieringParams
from magneto.base.env_params_pb2 import ExchangeBackupJobParams as ExchangeBackupJobParams
from magneto.base.env_params_pb2 import NasAnalysisJobParams as NasAnalysisJobParams
from magneto.base.env_params_pb2 import FileStubbingParams as FileStubbingParams
from magneto.base.env_params_pb2 import IsilonEnvParams as IsilonEnvParams
from magneto.base.env_params_pb2 import AWSNativeEnvParams as AWSNativeEnvParams
from magneto.base.env_params_pb2 import GCPNativeJobParams as GCPNativeJobParams
from magneto.base.env_params_pb2 import KubernetesEnvParams as KubernetesEnvParams
from magneto.base.env_params_pb2 import S3BackupJobParams as S3BackupJobParams
from magneto.base.env_params_pb2 import EnvBackupParams as EnvBackupParams
from magneto.base.env_params_pb2 import GCPDiskExclusionObjectParams as GCPDiskExclusionObjectParams
from magneto.base.env_params_pb2 import GCPJobDiskExclusionRule as GCPJobDiskExclusionRule
from magneto.base.env_params_pb2 import EBSVolumeExclusionParams as EBSVolumeExclusionParams
from magneto.base.env_params_pb2 import K8sFilterParams as K8sFilterParams
from magneto.base.env_params_pb2 import DataTransferInfo as DataTransferInfo

DESCRIPTOR: _descriptor.FileDescriptor

class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLow: _ClassVar[Priority]
    kMedium: _ClassVar[Priority]
    kHigh: _ClassVar[Priority]
    kNumPriorities: _ClassVar[Priority]
kLow: Priority
kMedium: Priority
kHigh: Priority
kNumPriorities: Priority
SKIP_OUTGOING_REWRITE_FIELD_NUMBER: _ClassVar[int]
skip_outgoing_rewrite: _descriptor.FieldDescriptor
SKIP_INCOMING_REWRITE_FIELD_NUMBER: _ClassVar[int]
skip_incoming_rewrite: _descriptor.FieldDescriptor

class AdditionalConnectorParams(_message.Message):
    __slots__ = ("o365_region", "use_outlook_ews_oauth", "use_get_searchable_mailboxes_api", "o365_emulator_entity_info", "registered_entity_sfdc_params", "max_vmware_http_sessions", "outlook_skip_creating_autodiscover_proxy", "graph_token_endpoint", "msgraph_host")
    O365_REGION_FIELD_NUMBER: _ClassVar[int]
    USE_OUTLOOK_EWS_OAUTH_FIELD_NUMBER: _ClassVar[int]
    USE_GET_SEARCHABLE_MAILBOXES_API_FIELD_NUMBER: _ClassVar[int]
    O365_EMULATOR_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_SFDC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_VMWARE_HTTP_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_SKIP_CREATING_AUTODISCOVER_PROXY_FIELD_NUMBER: _ClassVar[int]
    GRAPH_TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MSGRAPH_HOST_FIELD_NUMBER: _ClassVar[int]
    o365_region: _o365_additional_pb2.O365RegionProto
    use_outlook_ews_oauth: bool
    use_get_searchable_mailboxes_api: bool
    o365_emulator_entity_info: str
    registered_entity_sfdc_params: _sfdc_pb2.RegisteredEntitySfdcParams
    max_vmware_http_sessions: int
    outlook_skip_creating_autodiscover_proxy: bool
    graph_token_endpoint: str
    msgraph_host: str
    def __init__(self, o365_region: _Optional[_Union[_o365_additional_pb2.O365RegionProto, _Mapping]] = ..., use_outlook_ews_oauth: bool = ..., use_get_searchable_mailboxes_api: bool = ..., o365_emulator_entity_info: _Optional[str] = ..., registered_entity_sfdc_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., max_vmware_http_sessions: _Optional[int] = ..., outlook_skip_creating_autodiscover_proxy: bool = ..., graph_token_endpoint: _Optional[str] = ..., msgraph_host: _Optional[str] = ...) -> None: ...

class ConnectorParams(_message.Message):
    __slots__ = ("id", "version", "type", "host_type", "endpoint", "port", "agent_endpoint", "agent_port", "credentials", "entity", "tenant_id", "network_realm_id", "connector_group_id", "network_realm_info_vec", "populate_subnet_for_all_cluster_nodes", "additional_params")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    POPULATE_SUBNET_FOR_ALL_CLUSTER_NODES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    id: int
    version: int
    type: _enums_pb2.Environment.Type
    host_type: _enums_pb2.HostEnv.Type
    endpoint: str
    port: int
    agent_endpoint: str
    agent_port: int
    credentials: _credentials_pb2.Credentials
    entity: _entity_pb2.EntityProto
    tenant_id: str
    network_realm_id: int
    connector_group_id: int
    network_realm_info_vec: _containers.RepeatedCompositeFieldContainer[NetworkRealmInfo]
    populate_subnet_for_all_cluster_nodes: bool
    additional_params: AdditionalConnectorParams
    def __init__(self, id: _Optional[int] = ..., version: _Optional[int] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., endpoint: _Optional[str] = ..., port: _Optional[int] = ..., agent_endpoint: _Optional[str] = ..., agent_port: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., network_realm_info_vec: _Optional[_Iterable[_Union[NetworkRealmInfo, _Mapping]]] = ..., populate_subnet_for_all_cluster_nodes: bool = ..., additional_params: _Optional[_Union[AdditionalConnectorParams, _Mapping]] = ...) -> None: ...

class ConnectorParamsListProto(_message.Message):
    __slots__ = ("connector_params",)
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    connector_params: _containers.RepeatedCompositeFieldContainer[ConnectorParams]
    def __init__(self, connector_params: _Optional[_Iterable[_Union[ConnectorParams, _Mapping]]] = ...) -> None: ...

class ConfigurationParams(_message.Message):
    __slots__ = ("key", "value", "reason")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    reason: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class MagnetoObjectId(_message.Message):
    __slots__ = ("job_id", "job_uid", "entity")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    entity: _entity_pb2.EntityProto
    def __init__(self, job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class BackupRunId(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...

class ObjectSnapshotType(_message.Message):
    __slots__ = ("type", "msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ObjectSnapshotType.Type]
        kCrashConsistent: _ClassVar[ObjectSnapshotType.Type]
        kAppConsistent: _ClassVar[ObjectSnapshotType.Type]
        kNotPoweredOn: _ClassVar[ObjectSnapshotType.Type]
    kUnknown: ObjectSnapshotType.Type
    kCrashConsistent: ObjectSnapshotType.Type
    kAppConsistent: ObjectSnapshotType.Type
    kNotPoweredOn: ObjectSnapshotType.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    type: ObjectSnapshotType.Type
    msg: str
    def __init__(self, type: _Optional[_Union[ObjectSnapshotType.Type, str]] = ..., msg: _Optional[str] = ...) -> None: ...

class SnapshotInfoProto(_message.Message):
    __slots__ = ("type", "view_name", "metadata_view_name", "view_name_to_gc", "root_path", "relative_snapshot_dir", "total_bytes_read_from_source", "total_bytes_to_read_from_source", "total_bytes_tiered", "total_primary_physical_size_bytes", "total_logical_backup_size_bytes", "front_end_size_info", "num_app_instances", "num_app_objects", "slave_task_start_time_usecs", "snapshot_type", "scribe_table_row", "scribe_table_column", "total_entity_count", "total_changed_entity_count", "target_type", "file_walk_done", "source_snapshot_status", "source_snapshot_name", "snapshot_expiry_time", "source_snapshot_create_time_usecs", "storage_snapshot_provider", "pre_backup_script_status", "post_snapshot_script_status", "post_backup_script_status", "view_case_insensitivity_altered", "error_rocksdb_name", "change_rocksdb_name", "warnings", "reacquire_permit", "total_zero_fill_bytes", "zero_fill_task_weight_scale_down_factor")
    Extensions: _python_message._ExtensionDict
    class SourceSnapshotState(_message.Message):
        __slots__ = ()
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNotSupported: _ClassVar[SnapshotInfoProto.SourceSnapshotState.Status]
            kNotStarted: _ClassVar[SnapshotInfoProto.SourceSnapshotState.Status]
            kSnapshotCreated: _ClassVar[SnapshotInfoProto.SourceSnapshotState.Status]
            kSnapshotMarkedForDeletion: _ClassVar[SnapshotInfoProto.SourceSnapshotState.Status]
        kNotSupported: SnapshotInfoProto.SourceSnapshotState.Status
        kNotStarted: SnapshotInfoProto.SourceSnapshotState.Status
        kSnapshotCreated: SnapshotInfoProto.SourceSnapshotState.Status
        kSnapshotMarkedForDeletion: SnapshotInfoProto.SourceSnapshotState.Status
        def __init__(self) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_TO_GC_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TIERED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRIMARY_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_ROW_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANGED_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_WALK_DONE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PRE_BACKUP_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    POST_SNAPSHOT_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    POST_BACKUP_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_CASE_INSENSITIVITY_ALTERED_FIELD_NUMBER: _ClassVar[int]
    ERROR_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANGE_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    REACQUIRE_PERMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ZERO_FILL_BYTES_FIELD_NUMBER: _ClassVar[int]
    ZERO_FILL_TASK_WEIGHT_SCALE_DOWN_FACTOR_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    view_name: str
    metadata_view_name: str
    view_name_to_gc: str
    root_path: str
    relative_snapshot_dir: str
    total_bytes_read_from_source: int
    total_bytes_to_read_from_source: int
    total_bytes_tiered: int
    total_primary_physical_size_bytes: int
    total_logical_backup_size_bytes: int
    front_end_size_info: _stats_pb2.SizeInfo
    num_app_instances: int
    num_app_objects: int
    slave_task_start_time_usecs: int
    snapshot_type: ObjectSnapshotType
    scribe_table_row: str
    scribe_table_column: str
    total_entity_count: int
    total_changed_entity_count: int
    target_type: _enums_pb2.TargetType.Type
    file_walk_done: bool
    source_snapshot_status: SnapshotInfoProto.SourceSnapshotState.Status
    source_snapshot_name: str
    snapshot_expiry_time: int
    source_snapshot_create_time_usecs: int
    storage_snapshot_provider: StorageSnapshotProviderParams
    pre_backup_script_status: ScriptExecutionStatus
    post_snapshot_script_status: ScriptExecutionStatus
    post_backup_script_status: ScriptExecutionStatus
    view_case_insensitivity_altered: bool
    error_rocksdb_name: str
    change_rocksdb_name: str
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    reacquire_permit: bool
    total_zero_fill_bytes: int
    zero_fill_task_weight_scale_down_factor: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., view_name: _Optional[str] = ..., metadata_view_name: _Optional[str] = ..., view_name_to_gc: _Optional[str] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., total_bytes_read_from_source: _Optional[int] = ..., total_bytes_to_read_from_source: _Optional[int] = ..., total_bytes_tiered: _Optional[int] = ..., total_primary_physical_size_bytes: _Optional[int] = ..., total_logical_backup_size_bytes: _Optional[int] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., num_app_instances: _Optional[int] = ..., num_app_objects: _Optional[int] = ..., slave_task_start_time_usecs: _Optional[int] = ..., snapshot_type: _Optional[_Union[ObjectSnapshotType, _Mapping]] = ..., scribe_table_row: _Optional[str] = ..., scribe_table_column: _Optional[str] = ..., total_entity_count: _Optional[int] = ..., total_changed_entity_count: _Optional[int] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., file_walk_done: bool = ..., source_snapshot_status: _Optional[_Union[SnapshotInfoProto.SourceSnapshotState.Status, str]] = ..., source_snapshot_name: _Optional[str] = ..., snapshot_expiry_time: _Optional[int] = ..., source_snapshot_create_time_usecs: _Optional[int] = ..., storage_snapshot_provider: _Optional[_Union[StorageSnapshotProviderParams, _Mapping]] = ..., pre_backup_script_status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ..., post_snapshot_script_status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ..., post_backup_script_status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ..., view_case_insensitivity_altered: bool = ..., error_rocksdb_name: _Optional[str] = ..., change_rocksdb_name: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., reacquire_permit: bool = ..., total_zero_fill_bytes: _Optional[int] = ..., zero_fill_task_weight_scale_down_factor: _Optional[int] = ...) -> None: ...

class SnapshotDeltaProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class SnapshotScribeInfoProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class AdapterSpecificFlagsProto(_message.Message):
    __slots__ = ("env_type",)
    Extensions: _python_message._ExtensionDict
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class RestoreScribeInfoProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class VerificationInfoProto(_message.Message):
    __slots__ = ("app_env_vec", "num_app_instances", "num_app_objects", "agent_endpoint", "agent_info", "host_settings_check_result_vec")
    Extensions: _python_message._ExtensionDict
    APP_ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_SETTINGS_CHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    app_env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    num_app_instances: int
    num_app_objects: int
    agent_endpoint: str
    agent_info: _agent_pb2.AgentInfoProto
    host_settings_check_result_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostSettingsCheckResult]
    def __init__(self, app_env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., num_app_instances: _Optional[int] = ..., num_app_objects: _Optional[int] = ..., agent_endpoint: _Optional[str] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., host_settings_check_result_vec: _Optional[_Iterable[_Union[_agent_pb2.HostSettingsCheckResult, _Mapping]]] = ...) -> None: ...

class UserMessageProto(_message.Message):
    __slots__ = ("info_vec", "warning_vec")
    INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    info_vec: _containers.RepeatedScalarFieldContainer[str]
    warning_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, info_vec: _Optional[_Iterable[str]] = ..., warning_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class BackupTaskAdditionalParams(_message.Message):
    __slots__ = ("pre_backup_task_script", "post_snapshot_script", "post_backup_task_script", "sql_params", "physical_params", "vmware_params", "source_entity", "app_entity_id_vec", "cloud_vm_params", "kubernetes_params", "o365_params", "acropolis_params", "outlook_params", "oracle_params", "cdp_hydration_params", "nosql_connect_params", "uptier_params", "cdp_log_run_params", "analysis_params", "uda_backup_params", "externally_triggered_backup_params", "san_backup_params", "sfdc_backup_params", "cdp_params", "config_vec", "cassandra_backup_params")
    PRE_BACKUP_TASK_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SNAPSHOT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_BACKUP_TASK_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SQL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    O365_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CDP_HYDRATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPTIER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CDP_LOG_RUN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_TRIGGERED_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SAN_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CDP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    pre_backup_task_script: RemoteScriptProto
    post_snapshot_script: RemoteScriptProto
    post_backup_task_script: RemoteScriptProto
    sql_params: SqlBackupParams
    physical_params: PhysicalBackupParams
    vmware_params: VMwareBackupParams
    source_entity: _entity_pb2.EntityProto
    app_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    cloud_vm_params: CloudVMBackupParams
    kubernetes_params: KubernetesBackupParams
    o365_params: O365BackupParams
    acropolis_params: AcropolisBackupParams
    outlook_params: OutlookBackupParams
    oracle_params: OracleBackupParams
    cdp_hydration_params: CdpHydrationParams
    nosql_connect_params: NoSqlConnectParams
    uptier_params: UptieringRunOnceParams
    cdp_log_run_params: CdpLogRunParams
    analysis_params: AnalysisRunOnceParams
    uda_backup_params: UdaBackupParams
    externally_triggered_backup_params: ExternallyTriggeredBackupParams
    san_backup_params: SANBackupParams
    sfdc_backup_params: _sfdc_pb2.SfdcBackupJobParams
    cdp_params: CdpCommonBackupParams
    config_vec: _containers.RepeatedCompositeFieldContainer[ConfigurationParams]
    cassandra_backup_params: CassandraBackupParams
    def __init__(self, pre_backup_task_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., post_snapshot_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., post_backup_task_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., sql_params: _Optional[_Union[SqlBackupParams, _Mapping]] = ..., physical_params: _Optional[_Union[PhysicalBackupParams, _Mapping]] = ..., vmware_params: _Optional[_Union[VMwareBackupParams, _Mapping]] = ..., source_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., app_entity_id_vec: _Optional[_Iterable[int]] = ..., cloud_vm_params: _Optional[_Union[CloudVMBackupParams, _Mapping]] = ..., kubernetes_params: _Optional[_Union[KubernetesBackupParams, _Mapping]] = ..., o365_params: _Optional[_Union[O365BackupParams, _Mapping]] = ..., acropolis_params: _Optional[_Union[AcropolisBackupParams, _Mapping]] = ..., outlook_params: _Optional[_Union[OutlookBackupParams, _Mapping]] = ..., oracle_params: _Optional[_Union[OracleBackupParams, _Mapping]] = ..., cdp_hydration_params: _Optional[_Union[CdpHydrationParams, _Mapping]] = ..., nosql_connect_params: _Optional[_Union[NoSqlConnectParams, _Mapping]] = ..., uptier_params: _Optional[_Union[UptieringRunOnceParams, _Mapping]] = ..., cdp_log_run_params: _Optional[_Union[CdpLogRunParams, _Mapping]] = ..., analysis_params: _Optional[_Union[AnalysisRunOnceParams, _Mapping]] = ..., uda_backup_params: _Optional[_Union[UdaBackupParams, _Mapping]] = ..., externally_triggered_backup_params: _Optional[_Union[ExternallyTriggeredBackupParams, _Mapping]] = ..., san_backup_params: _Optional[_Union[SANBackupParams, _Mapping]] = ..., sfdc_backup_params: _Optional[_Union[_sfdc_pb2.SfdcBackupJobParams, _Mapping]] = ..., cdp_params: _Optional[_Union[CdpCommonBackupParams, _Mapping]] = ..., config_vec: _Optional[_Iterable[_Union[ConfigurationParams, _Mapping]]] = ..., cassandra_backup_params: _Optional[_Union[CassandraBackupParams, _Mapping]] = ...) -> None: ...

class RestoreTaskAdditionalParams(_message.Message):
    __slots__ = ("pre_script", "post_script", "uptier_params")
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    UPTIER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    pre_script: RemoteScriptProto
    post_script: RemoteScriptProto
    uptier_params: UptieringRunOnceParams
    def __init__(self, pre_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., post_script: _Optional[_Union[RemoteScriptProto, _Mapping]] = ..., uptier_params: _Optional[_Union[UptieringRunOnceParams, _Mapping]] = ...) -> None: ...

class VMwareSourceInfo(_message.Message):
    __slots__ = ("resource_pool_entity", "host_system_entity")
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HOST_SYSTEM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    resource_pool_entity: _entity_pb2.EntityProto
    host_system_entity: _entity_pb2.EntityProto
    def __init__(self, resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., host_system_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class ScriptExecutionStatus(_message.Message):
    __slots__ = ("state", "exit_code", "error", "executing", "output")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[ScriptExecutionStatus.State]
        kRunning: _ClassVar[ScriptExecutionStatus.State]
        kExited: _ClassVar[ScriptExecutionStatus.State]
        kCancelled: _ClassVar[ScriptExecutionStatus.State]
        kKilled: _ClassVar[ScriptExecutionStatus.State]
    kNotStarted: ScriptExecutionStatus.State
    kRunning: ScriptExecutionStatus.State
    kExited: ScriptExecutionStatus.State
    kCancelled: ScriptExecutionStatus.State
    kKilled: ScriptExecutionStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTING_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    state: ScriptExecutionStatus.State
    exit_code: int
    error: _error_pb2.ErrorProto
    executing: bool
    output: str
    def __init__(self, state: _Optional[_Union[ScriptExecutionStatus.State, str]] = ..., exit_code: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., executing: bool = ..., output: _Optional[str] = ...) -> None: ...

class ScriptLogMessage(_message.Message):
    __slots__ = ("stdout_log", "stderr_log")
    STDOUT_LOG_FIELD_NUMBER: _ClassVar[int]
    STDERR_LOG_FIELD_NUMBER: _ClassVar[int]
    stdout_log: str
    stderr_log: str
    def __init__(self, stdout_log: _Optional[str] = ..., stderr_log: _Optional[str] = ...) -> None: ...

class RemoteScriptProto(_message.Message):
    __slots__ = ("remote_host_params", "script", "windows_script", "status")
    REMOTE_HOST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    remote_host_params: RemoteHostConnectorParams
    script: ScriptPathAndParams
    windows_script: ScriptPathAndParams
    status: ScriptExecutionStatus
    def __init__(self, remote_host_params: _Optional[_Union[RemoteHostConnectorParams, _Mapping]] = ..., script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ..., windows_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ..., status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ...) -> None: ...

class SqlBackupParams(_message.Message):
    __slots__ = ("is_sql_tail_log_backup", "related_restore_task_id", "progress_monitor_root_path_prefix", "app_entity_vec")
    IS_SQL_TAIL_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RELATED_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_ROOT_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    is_sql_tail_log_backup: bool
    related_restore_task_id: int
    progress_monitor_root_path_prefix: str
    app_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, is_sql_tail_log_backup: bool = ..., related_restore_task_id: _Optional[int] = ..., progress_monitor_root_path_prefix: _Optional[str] = ..., app_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class PhysicalBackupParams(_message.Message):
    __slots__ = ("volume_guid_device_key_map", "disk_area_align_end_offset_enabled", "disk_area_alignment_for_inc_backup_enabled", "include_system_backup", "metadata_file_path")
    class VolumeGuidDeviceKeyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VOLUME_GUID_DEVICE_KEY_MAP_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_ALIGN_END_OFFSET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_ALIGNMENT_FOR_INC_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    volume_guid_device_key_map: _containers.ScalarMap[str, int]
    disk_area_align_end_offset_enabled: bool
    disk_area_alignment_for_inc_backup_enabled: bool
    include_system_backup: bool
    metadata_file_path: str
    def __init__(self, volume_guid_device_key_map: _Optional[_Mapping[str, int]] = ..., disk_area_align_end_offset_enabled: bool = ..., disk_area_alignment_for_inc_backup_enabled: bool = ..., include_system_backup: bool = ..., metadata_file_path: _Optional[str] = ...) -> None: ...

class StorageSnapshotProviderParams(_message.Message):
    __slots__ = ("entity", "connector_params", "root_entity")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    connector_params: ConnectorParams
    root_entity: _entity_pb2.EntityProto
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., connector_params: _Optional[_Union[ConnectorParams, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class CdpCommonBackupParams(_message.Message):
    __slots__ = ("is_journal_sharded",)
    IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
    is_journal_sharded: bool
    def __init__(self, is_journal_sharded: bool = ...) -> None: ...

class VMwareBackupParams(_message.Message):
    __slots__ = ("disk_area_alignment_size_kb", "storage_snapshot_provider_params", "vcd_backup_params", "use_san_transport", "preserve_cbt_info_enabled", "vm_entity_id_to_progress_monitor_path")
    class VmEntityIdToProgressMonitorPathEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    DISK_AREA_ALIGNMENT_SIZE_KB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_PROVIDER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VCD_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_CBT_INFO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_ID_TO_PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    disk_area_alignment_size_kb: int
    storage_snapshot_provider_params: _containers.RepeatedCompositeFieldContainer[StorageSnapshotProviderParams]
    vcd_backup_params: VCDBackupParams
    use_san_transport: bool
    preserve_cbt_info_enabled: bool
    vm_entity_id_to_progress_monitor_path: _containers.ScalarMap[int, str]
    def __init__(self, disk_area_alignment_size_kb: _Optional[int] = ..., storage_snapshot_provider_params: _Optional[_Iterable[_Union[StorageSnapshotProviderParams, _Mapping]]] = ..., vcd_backup_params: _Optional[_Union[VCDBackupParams, _Mapping]] = ..., use_san_transport: bool = ..., preserve_cbt_info_enabled: bool = ..., vm_entity_id_to_progress_monitor_path: _Optional[_Mapping[int, str]] = ...) -> None: ...

class KubernetesBackupParams(_message.Message):
    __slots__ = ("management_namespace", "cluster_software_version", "is_protection_using_datamover_enabled", "is_volume_exclusion_enabled", "s3_account_id", "init_container_image", "use_annotated_vsc", "datamover_service_type", "vlan_params")
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_PROTECTION_USING_DATAMOVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_VOLUME_EXCLUSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    S3_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    USE_ANNOTATED_VSC_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    cluster_software_version: str
    is_protection_using_datamover_enabled: bool
    is_volume_exclusion_enabled: bool
    s3_account_id: str
    init_container_image: str
    use_annotated_vsc: bool
    datamover_service_type: _kubernetes_pb2.ServiceType
    vlan_params: _common_pb2.VlanParams
    def __init__(self, management_namespace: _Optional[str] = ..., cluster_software_version: _Optional[str] = ..., is_protection_using_datamover_enabled: bool = ..., is_volume_exclusion_enabled: bool = ..., s3_account_id: _Optional[str] = ..., init_container_image: _Optional[str] = ..., use_annotated_vsc: bool = ..., datamover_service_type: _Optional[_Union[_kubernetes_pb2.ServiceType, str]] = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ...) -> None: ...

class VCDBackupParams(_message.Message):
    __slots__ = ("vm_to_vapp_map",)
    class VmToVappMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BackupTaskStateVappInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BackupTaskStateVappInfoProto, _Mapping]] = ...) -> None: ...
    VM_TO_VAPP_MAP_FIELD_NUMBER: _ClassVar[int]
    vm_to_vapp_map: _containers.MessageMap[int, BackupTaskStateVappInfoProto]
    def __init__(self, vm_to_vapp_map: _Optional[_Mapping[int, BackupTaskStateVappInfoProto]] = ...) -> None: ...

class AcropolisBackupParams(_message.Message):
    __slots__ = ("include_root_entity_for_backup_task_lock",)
    INCLUDE_ROOT_ENTITY_FOR_BACKUP_TASK_LOCK_FIELD_NUMBER: _ClassVar[int]
    include_root_entity_for_backup_task_lock: bool
    def __init__(self, include_root_entity_for_backup_task_lock: bool = ...) -> None: ...

class SanExternalResource(_message.Message):
    __slots__ = ("availability_group_entity_vec",)
    AVAILABILITY_GROUP_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    availability_group_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, availability_group_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class SANBackupParams(_message.Message):
    __slots__ = ("pure_sequential_vol_diff_query", "nimble_sequential_vol_diff_query", "preserve_changed_areas_enabled", "transport_mode", "use_secured_snapshot", "snapshot_retention_time_usecs", "san_external_resource")
    class TransportMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreferFc: _ClassVar[SANBackupParams.TransportMode]
        kIscsiOnly: _ClassVar[SANBackupParams.TransportMode]
    kPreferFc: SANBackupParams.TransportMode
    kIscsiOnly: SANBackupParams.TransportMode
    PURE_SEQUENTIAL_VOL_DIFF_QUERY_FIELD_NUMBER: _ClassVar[int]
    NIMBLE_SEQUENTIAL_VOL_DIFF_QUERY_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_CHANGED_AREAS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_SECURED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RETENTION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SAN_EXTERNAL_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    pure_sequential_vol_diff_query: bool
    nimble_sequential_vol_diff_query: bool
    preserve_changed_areas_enabled: bool
    transport_mode: SANBackupParams.TransportMode
    use_secured_snapshot: bool
    snapshot_retention_time_usecs: int
    san_external_resource: SanExternalResource
    def __init__(self, pure_sequential_vol_diff_query: bool = ..., nimble_sequential_vol_diff_query: bool = ..., preserve_changed_areas_enabled: bool = ..., transport_mode: _Optional[_Union[SANBackupParams.TransportMode, str]] = ..., use_secured_snapshot: bool = ..., snapshot_retention_time_usecs: _Optional[int] = ..., san_external_resource: _Optional[_Union[SanExternalResource, _Mapping]] = ...) -> None: ...

class SANGroupEntityRecoverParams(_message.Message):
    __slots__ = ("volume_recover_params_vec",)
    class SANVolumeRecoverParams(_message.Message):
        __slots__ = ("volume_entity",)
        VOLUME_ENTITY_FIELD_NUMBER: _ClassVar[int]
        volume_entity: _entity_pb2.EntityProto
        def __init__(self, volume_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    VOLUME_RECOVER_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_recover_params_vec: _containers.RepeatedCompositeFieldContainer[SANGroupEntityRecoverParams.SANVolumeRecoverParams]
    def __init__(self, volume_recover_params_vec: _Optional[_Iterable[_Union[SANGroupEntityRecoverParams.SANVolumeRecoverParams, _Mapping]]] = ...) -> None: ...

class SANStorageArraySnapshotRecoverParams(_message.Message):
    __slots__ = ("storage_array_snapshot_id", "storage_array_snapshot_name")
    STORAGE_ARRAY_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    storage_array_snapshot_id: str
    storage_array_snapshot_name: str
    def __init__(self, storage_array_snapshot_id: _Optional[str] = ..., storage_array_snapshot_name: _Optional[str] = ...) -> None: ...

class SANRecoverParams(_message.Message):
    __slots__ = ("san_group_recover_params", "san_storage_array_snap_params")
    SAN_GROUP_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SAN_STORAGE_ARRAY_SNAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    san_group_recover_params: SANGroupEntityRecoverParams
    san_storage_array_snap_params: SANStorageArraySnapshotRecoverParams
    def __init__(self, san_group_recover_params: _Optional[_Union[SANGroupEntityRecoverParams, _Mapping]] = ..., san_storage_array_snap_params: _Optional[_Union[SANStorageArraySnapshotRecoverParams, _Mapping]] = ...) -> None: ...

class BackupTaskStateVappInfoProto(_message.Message):
    __slots__ = ("vapp_id", "vapp_name", "vapp_href", "vapp_in_maintenance_mode", "vapp_deployed", "vapp_info_xml", "vapp_entity", "vdc_id", "is_vapp_template_backup", "catalog_uuid", "vapp_network_xml")
    VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    VAPP_HREF_FIELD_NUMBER: _ClassVar[int]
    VAPP_IN_MAINTENANCE_MODE_FIELD_NUMBER: _ClassVar[int]
    VAPP_DEPLOYED_FIELD_NUMBER: _ClassVar[int]
    VAPP_INFO_XML_FIELD_NUMBER: _ClassVar[int]
    VAPP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VAPP_TEMPLATE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    CATALOG_UUID_FIELD_NUMBER: _ClassVar[int]
    VAPP_NETWORK_XML_FIELD_NUMBER: _ClassVar[int]
    vapp_id: str
    vapp_name: str
    vapp_href: str
    vapp_in_maintenance_mode: bool
    vapp_deployed: bool
    vapp_info_xml: str
    vapp_entity: int
    vdc_id: str
    is_vapp_template_backup: bool
    catalog_uuid: str
    vapp_network_xml: str
    def __init__(self, vapp_id: _Optional[str] = ..., vapp_name: _Optional[str] = ..., vapp_href: _Optional[str] = ..., vapp_in_maintenance_mode: bool = ..., vapp_deployed: bool = ..., vapp_info_xml: _Optional[str] = ..., vapp_entity: _Optional[int] = ..., vdc_id: _Optional[str] = ..., is_vapp_template_backup: bool = ..., catalog_uuid: _Optional[str] = ..., vapp_network_xml: _Optional[str] = ...) -> None: ...

class CloudVMBackupParams(_message.Message):
    __slots__ = ("restore_entity", "view_name")
    RESTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    restore_entity: RestoreInfoProto.RestoreEntity
    view_name: str
    def __init__(self, restore_entity: _Optional[_Union[RestoreInfoProto.RestoreEntity, _Mapping]] = ..., view_name: _Optional[str] = ...) -> None: ...

class OutlookBackupParams(_message.Message):
    __slots__ = ("previous_run_view_name", "view_cloning_enabled", "first_time_view_clone", "sla_deadline_time_usecs", "delete_cloned_directory")
    PREVIOUS_RUN_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_VIEW_CLONE_FIELD_NUMBER: _ClassVar[int]
    SLA_DEADLINE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLONED_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    previous_run_view_name: str
    view_cloning_enabled: bool
    first_time_view_clone: bool
    sla_deadline_time_usecs: int
    delete_cloned_directory: bool
    def __init__(self, previous_run_view_name: _Optional[str] = ..., view_cloning_enabled: bool = ..., first_time_view_clone: bool = ..., sla_deadline_time_usecs: _Optional[int] = ..., delete_cloned_directory: bool = ...) -> None: ...

class OracleBackupParams(_message.Message):
    __slots__ = ("parallel_op_enabled", "parallel_log_backup_enabled")
    PARALLEL_OP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    parallel_op_enabled: bool
    parallel_log_backup_enabled: bool
    def __init__(self, parallel_op_enabled: bool = ..., parallel_log_backup_enabled: bool = ...) -> None: ...

class O365BackupParams(_message.Message):
    __slots__ = ("should_backup_onedrive", "previous_run_view_name", "view_cloning_enabled", "first_time_view_clone", "should_backup_sharepoint", "total_entity_logical_size", "sla_deadline_time_usecs", "site_relative_path", "should_use_flat_file_structure", "report_lookup_error", "delete_cloned_directory", "should_recursively_clone_sharepoint_dir", "is_automatic_full_backup", "child_site_vec", "parent_site", "dir_to_be_renamed", "application_ids_permit_scaling_enabled", "maybe_skip_sharepoint_template_backup")
    class SiteInfo(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    SHOULD_BACKUP_ONEDRIVE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RUN_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_VIEW_CLONE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BACKUP_SHAREPOINT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENTITY_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    SLA_DEADLINE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SITE_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHOULD_USE_FLAT_FILE_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOOKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLONED_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_SHAREPOINT_DIR_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOMATIC_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    CHILD_SITE_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_SITE_FIELD_NUMBER: _ClassVar[int]
    DIR_TO_BE_RENAMED_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_PERMIT_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAYBE_SKIP_SHAREPOINT_TEMPLATE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    should_backup_onedrive: bool
    previous_run_view_name: str
    view_cloning_enabled: bool
    first_time_view_clone: bool
    should_backup_sharepoint: bool
    total_entity_logical_size: int
    sla_deadline_time_usecs: int
    site_relative_path: str
    should_use_flat_file_structure: bool
    report_lookup_error: bool
    delete_cloned_directory: bool
    should_recursively_clone_sharepoint_dir: bool
    is_automatic_full_backup: bool
    child_site_vec: _containers.RepeatedCompositeFieldContainer[O365BackupParams.SiteInfo]
    parent_site: O365BackupParams.SiteInfo
    dir_to_be_renamed: str
    application_ids_permit_scaling_enabled: bool
    maybe_skip_sharepoint_template_backup: bool
    def __init__(self, should_backup_onedrive: bool = ..., previous_run_view_name: _Optional[str] = ..., view_cloning_enabled: bool = ..., first_time_view_clone: bool = ..., should_backup_sharepoint: bool = ..., total_entity_logical_size: _Optional[int] = ..., sla_deadline_time_usecs: _Optional[int] = ..., site_relative_path: _Optional[str] = ..., should_use_flat_file_structure: bool = ..., report_lookup_error: bool = ..., delete_cloned_directory: bool = ..., should_recursively_clone_sharepoint_dir: bool = ..., is_automatic_full_backup: bool = ..., child_site_vec: _Optional[_Iterable[_Union[O365BackupParams.SiteInfo, _Mapping]]] = ..., parent_site: _Optional[_Union[O365BackupParams.SiteInfo, _Mapping]] = ..., dir_to_be_renamed: _Optional[str] = ..., application_ids_permit_scaling_enabled: bool = ..., maybe_skip_sharepoint_template_backup: bool = ...) -> None: ...

class CdpHydrationParams(_message.Message):
    __slots__ = ("log_view_dir", "disk_logs_vec", "hydration_time_usecs", "hydration_needed", "cdp_version", "cdp_hydration_task_id", "hydration_version")
    class VirtualDiskInfo(_message.Message):
        __slots__ = ("uuid", "file_name", "base_seq_number")
        UUID_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        file_name: str
        base_seq_number: _event_pb2.Sequencer
        def __init__(self, uuid: _Optional[str] = ..., file_name: _Optional[str] = ..., base_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ...) -> None: ...
    class LogData(_message.Message):
        __slots__ = ("log_file_name", "removal_needed", "start_seq_number", "end_seq_number", "is_journal_sharded")
        LOG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_NEEDED_FIELD_NUMBER: _ClassVar[int]
        START_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        END_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
        log_file_name: str
        removal_needed: bool
        start_seq_number: _event_pb2.Sequencer
        end_seq_number: _event_pb2.Sequencer
        is_journal_sharded: bool
        def __init__(self, log_file_name: _Optional[str] = ..., removal_needed: bool = ..., start_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., is_journal_sharded: bool = ...) -> None: ...
    class DiskLog(_message.Message):
        __slots__ = ("disk_info", "log_data_vec")
        DISK_INFO_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_info: CdpHydrationParams.VirtualDiskInfo
        log_data_vec: _containers.RepeatedCompositeFieldContainer[CdpHydrationParams.LogData]
        def __init__(self, disk_info: _Optional[_Union[CdpHydrationParams.VirtualDiskInfo, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[CdpHydrationParams.LogData, _Mapping]]] = ...) -> None: ...
    LOG_VIEW_DIR_FIELD_NUMBER: _ClassVar[int]
    DISK_LOGS_VEC_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_NEEDED_FIELD_NUMBER: _ClassVar[int]
    CDP_VERSION_FIELD_NUMBER: _ClassVar[int]
    CDP_HYDRATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    log_view_dir: str
    disk_logs_vec: _containers.RepeatedCompositeFieldContainer[CdpHydrationParams.DiskLog]
    hydration_time_usecs: int
    hydration_needed: bool
    cdp_version: _common_pb2.CDPVersion
    cdp_hydration_task_id: int
    hydration_version: _common_pb2.CDPHydrationVersion
    def __init__(self, log_view_dir: _Optional[str] = ..., disk_logs_vec: _Optional[_Iterable[_Union[CdpHydrationParams.DiskLog, _Mapping]]] = ..., hydration_time_usecs: _Optional[int] = ..., hydration_needed: bool = ..., cdp_version: _Optional[_Union[_common_pb2.CDPVersion, str]] = ..., cdp_hydration_task_id: _Optional[int] = ..., hydration_version: _Optional[_Union[_common_pb2.CDPHydrationVersion, str]] = ...) -> None: ...

class CdpPostProcessParams(_message.Message):
    __slots__ = ("log_view_dir", "disk_logs_vec")
    class VirtualDiskInfo(_message.Message):
        __slots__ = ("uuid", "file_name", "last_seq_number", "is_deleted")
        UUID_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        file_name: str
        last_seq_number: _event_pb2.Sequencer
        is_deleted: bool
        def __init__(self, uuid: _Optional[str] = ..., file_name: _Optional[str] = ..., last_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., is_deleted: bool = ...) -> None: ...
    class LogData(_message.Message):
        __slots__ = ("log_file_name", "removal_needed")
        LOG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_NEEDED_FIELD_NUMBER: _ClassVar[int]
        log_file_name: str
        removal_needed: bool
        def __init__(self, log_file_name: _Optional[str] = ..., removal_needed: bool = ...) -> None: ...
    class DiskLog(_message.Message):
        __slots__ = ("disk_info", "log_data_vec")
        DISK_INFO_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_info: CdpPostProcessParams.VirtualDiskInfo
        log_data_vec: _containers.RepeatedCompositeFieldContainer[CdpPostProcessParams.LogData]
        def __init__(self, disk_info: _Optional[_Union[CdpPostProcessParams.VirtualDiskInfo, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[CdpPostProcessParams.LogData, _Mapping]]] = ...) -> None: ...
    LOG_VIEW_DIR_FIELD_NUMBER: _ClassVar[int]
    DISK_LOGS_VEC_FIELD_NUMBER: _ClassVar[int]
    log_view_dir: str
    disk_logs_vec: _containers.RepeatedCompositeFieldContainer[CdpPostProcessParams.DiskLog]
    def __init__(self, log_view_dir: _Optional[str] = ..., disk_logs_vec: _Optional[_Iterable[_Union[CdpPostProcessParams.DiskLog, _Mapping]]] = ...) -> None: ...

class CdpLogRunParams(_message.Message):
    __slots__ = ("disk_logs_vec", "log_run_time_usecs", "epoch_data_vec")
    class VirtualDiskInfo(_message.Message):
        __slots__ = ("uuid", "file_name")
        UUID_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        file_name: str
        def __init__(self, uuid: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...
    class LogData(_message.Message):
        __slots__ = ("log_file_path", "remove")
        LOG_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        REMOVE_FIELD_NUMBER: _ClassVar[int]
        log_file_path: str
        remove: bool
        def __init__(self, log_file_path: _Optional[str] = ..., remove: bool = ...) -> None: ...
    class DiskLog(_message.Message):
        __slots__ = ("disk_info", "log_data_vec", "data_events_vec")
        DISK_INFO_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        DATA_EVENTS_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_info: CdpLogRunParams.VirtualDiskInfo
        log_data_vec: _containers.RepeatedCompositeFieldContainer[CdpLogRunParams.LogData]
        data_events_vec: _containers.RepeatedCompositeFieldContainer[_event_pb2.DataEvent]
        def __init__(self, disk_info: _Optional[_Union[CdpLogRunParams.VirtualDiskInfo, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[CdpLogRunParams.LogData, _Mapping]]] = ..., data_events_vec: _Optional[_Iterable[_Union[_event_pb2.DataEvent, _Mapping]]] = ...) -> None: ...
    class EpochData(_message.Message):
        __slots__ = ("epoch", "removed")
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        REMOVED_FIELD_NUMBER: _ClassVar[int]
        epoch: _atom_pb2.EpochProto
        removed: bool
        def __init__(self, epoch: _Optional[_Union[_atom_pb2.EpochProto, _Mapping]] = ..., removed: bool = ...) -> None: ...
    DISK_LOGS_VEC_FIELD_NUMBER: _ClassVar[int]
    LOG_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EPOCH_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_logs_vec: _containers.RepeatedCompositeFieldContainer[CdpLogRunParams.DiskLog]
    log_run_time_usecs: int
    epoch_data_vec: _containers.RepeatedCompositeFieldContainer[CdpLogRunParams.EpochData]
    def __init__(self, disk_logs_vec: _Optional[_Iterable[_Union[CdpLogRunParams.DiskLog, _Mapping]]] = ..., log_run_time_usecs: _Optional[int] = ..., epoch_data_vec: _Optional[_Iterable[_Union[CdpLogRunParams.EpochData, _Mapping]]] = ...) -> None: ...

class DiskDiffParams(_message.Message):
    __slots__ = ("disk_info_vec", "view_box_id", "current_view_name", "previous_view_name", "error")
    class VirtualDiskInfo(_message.Message):
        __slots__ = ("disk_key", "current_file_path", "previous_file_path", "start_offset", "disk_diff_list", "all_diffs_fetched")
        DISK_KEY_FIELD_NUMBER: _ClassVar[int]
        CURRENT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DISK_DIFF_LIST_FIELD_NUMBER: _ClassVar[int]
        ALL_DIFFS_FETCHED_FIELD_NUMBER: _ClassVar[int]
        disk_key: int
        current_file_path: str
        previous_file_path: str
        start_offset: int
        disk_diff_list: _disk_pb2.DiskAreaListProto
        all_diffs_fetched: bool
        def __init__(self, disk_key: _Optional[int] = ..., current_file_path: _Optional[str] = ..., previous_file_path: _Optional[str] = ..., start_offset: _Optional[int] = ..., disk_diff_list: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ..., all_diffs_fetched: bool = ...) -> None: ...
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[DiskDiffParams.VirtualDiskInfo]
    view_box_id: int
    current_view_name: str
    previous_view_name: str
    error: _error_pb2.ErrorProto
    def __init__(self, disk_info_vec: _Optional[_Iterable[_Union[DiskDiffParams.VirtualDiskInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., current_view_name: _Optional[str] = ..., previous_view_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class NoSqlConnectParams(_message.Message):
    __slots__ = ("cassandra_connect_params", "cassandra_additional_params", "mongodb_connect_params", "mongodb_additional_params", "couchbase_connect_params", "hbase_connect_params", "hdfs_connect_params", "hive_connect_params")
    CASSANDRA_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    cassandra_connect_params: _nosql_pb2.CassandraConnectParams
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    mongodb_connect_params: _nosql_pb2.MongoDBConnectParams
    mongodb_additional_params: _nosql_pb2.MongoDBAdditionalParams
    couchbase_connect_params: _nosql_pb2.CouchbaseConnectParams
    hbase_connect_params: _nosql_pb2.HBaseConnectParams
    hdfs_connect_params: _nosql_pb2.HdfsConnectParams
    hive_connect_params: _nosql_pb2.HiveConnectParams
    def __init__(self, cassandra_connect_params: _Optional[_Union[_nosql_pb2.CassandraConnectParams, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ..., mongodb_connect_params: _Optional[_Union[_nosql_pb2.MongoDBConnectParams, _Mapping]] = ..., mongodb_additional_params: _Optional[_Union[_nosql_pb2.MongoDBAdditionalParams, _Mapping]] = ..., couchbase_connect_params: _Optional[_Union[_nosql_pb2.CouchbaseConnectParams, _Mapping]] = ..., hbase_connect_params: _Optional[_Union[_nosql_pb2.HBaseConnectParams, _Mapping]] = ..., hdfs_connect_params: _Optional[_Union[_nosql_pb2.HdfsConnectParams, _Mapping]] = ..., hive_connect_params: _Optional[_Union[_nosql_pb2.HiveConnectParams, _Mapping]] = ...) -> None: ...

class UptieringRunOnceParams(_message.Message):
    __slots__ = ("uptier_path", "use_entity_id_for_uptier_range")
    UPTIER_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_ENTITY_ID_FOR_UPTIER_RANGE_FIELD_NUMBER: _ClassVar[int]
    uptier_path: str
    use_entity_id_for_uptier_range: bool
    def __init__(self, uptier_path: _Optional[str] = ..., use_entity_id_for_uptier_range: bool = ...) -> None: ...

class NoSqlRecoverParams(_message.Message):
    __slots__ = ("restore_objects", "entity_logs", "start_sequencer", "end_sequencer", "job_end_time_usecs")
    class EntityLog(_message.Message):
        __slots__ = ("entity", "log_data_vec")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        log_data_vec: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.NoSqlLogData]
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[_nosql_pb2.NoSqlLogData, _Mapping]]] = ...) -> None: ...
    RESTORE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LOGS_FIELD_NUMBER: _ClassVar[int]
    START_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    END_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    JOB_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    restore_objects: _containers.RepeatedCompositeFieldContainer[_nosql_pb2.NoSqlRestoreObject]
    entity_logs: _containers.RepeatedCompositeFieldContainer[NoSqlRecoverParams.EntityLog]
    start_sequencer: _event_pb2.Sequencer
    end_sequencer: _event_pb2.Sequencer
    job_end_time_usecs: int
    def __init__(self, restore_objects: _Optional[_Iterable[_Union[_nosql_pb2.NoSqlRestoreObject, _Mapping]]] = ..., entity_logs: _Optional[_Iterable[_Union[NoSqlRecoverParams.EntityLog, _Mapping]]] = ..., start_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., job_end_time_usecs: _Optional[int] = ...) -> None: ...

class UdaRecoverParams(_message.Message):
    __slots__ = ("restore_objects", "log_view_name", "view_box_id", "throttling_policy")
    RESTORE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    LOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_POLICY_FIELD_NUMBER: _ClassVar[int]
    restore_objects: _containers.RepeatedCompositeFieldContainer[_uda_pb2.UdaRestoreObject]
    log_view_name: str
    view_box_id: int
    throttling_policy: ThrottlingPolicy
    def __init__(self, restore_objects: _Optional[_Iterable[_Union[_uda_pb2.UdaRestoreObject, _Mapping]]] = ..., log_view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., throttling_policy: _Optional[_Union[ThrottlingPolicy, _Mapping]] = ...) -> None: ...

class SfdcRecoverParams(_message.Message):
    __slots__ = ("restore_objects",)
    RESTORE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    restore_objects: _containers.RepeatedCompositeFieldContainer[_sfdc_pb2.SfdcRestoreObject]
    def __init__(self, restore_objects: _Optional[_Iterable[_Union[_sfdc_pb2.SfdcRestoreObject, _Mapping]]] = ...) -> None: ...

class AnalysisRunOnceParams(_message.Message):
    __slots__ = ("only_walk_checkpoint",)
    ONLY_WALK_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    only_walk_checkpoint: bool
    def __init__(self, only_walk_checkpoint: bool = ...) -> None: ...

class RestoreEntityStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFilesCloned: _ClassVar[RestoreEntityStatus.Type]
        kFetchedEntityInfo: _ClassVar[RestoreEntityStatus.Type]
        kDataCopyStarted: _ClassVar[RestoreEntityStatus.Type]
        kVMCreated: _ClassVar[RestoreEntityStatus.Type]
        kRelocationStarted: _ClassVar[RestoreEntityStatus.Type]
        kFinished: _ClassVar[RestoreEntityStatus.Type]
        kAborted: _ClassVar[RestoreEntityStatus.Type]
        kInProgress: _ClassVar[RestoreEntityStatus.Type]
        kCancelled: _ClassVar[RestoreEntityStatus.Type]
        kVMDeleted: _ClassVar[RestoreEntityStatus.Type]
    kFilesCloned: RestoreEntityStatus.Type
    kFetchedEntityInfo: RestoreEntityStatus.Type
    kDataCopyStarted: RestoreEntityStatus.Type
    kVMCreated: RestoreEntityStatus.Type
    kRelocationStarted: RestoreEntityStatus.Type
    kFinished: RestoreEntityStatus.Type
    kAborted: RestoreEntityStatus.Type
    kInProgress: RestoreEntityStatus.Type
    kCancelled: RestoreEntityStatus.Type
    kVMDeleted: RestoreEntityStatus.Type
    def __init__(self) -> None: ...

class RestoreInfoProto(_message.Message):
    __slots__ = ("type", "restore_entity_vec", "target_type", "pre_script_status", "post_script_status")
    Extensions: _python_message._ExtensionDict
    class RestoreEntity(_message.Message):
        __slots__ = ("entity", "status", "public_status", "restored_entity", "relative_restore_paths", "error", "resource_pool_entity", "progress_monitor_task_path", "warnings", "restored_view_name", "total_bytes_restored")
        Extensions: _python_message._ExtensionDict
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
        RESTORED_ENTITY_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_RESTORE_PATHS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        RESTORED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        status: RestoreEntityStatus.Type
        public_status: _enums_pb2.PublicTaskStatus.Type
        restored_entity: _entity_pb2.EntityProto
        relative_restore_paths: _containers.RepeatedScalarFieldContainer[str]
        error: _error_pb2.ErrorProto
        resource_pool_entity: _entity_pb2.EntityProto
        progress_monitor_task_path: str
        warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
        restored_view_name: str
        total_bytes_restored: int
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., status: _Optional[_Union[RestoreEntityStatus.Type, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., restored_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., relative_restore_paths: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., restored_view_name: _Optional[str] = ..., total_bytes_restored: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRE_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    POST_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    restore_entity_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfoProto.RestoreEntity]
    target_type: _enums_pb2.TargetType.Type
    pre_script_status: ScriptExecutionStatus
    post_script_status: ScriptExecutionStatus
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_entity_vec: _Optional[_Iterable[_Union[RestoreInfoProto.RestoreEntity, _Mapping]]] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., pre_script_status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ..., post_script_status: _Optional[_Union[ScriptExecutionStatus, _Mapping]] = ...) -> None: ...

class DestroyClonedEntityInfoProto(_message.Message):
    __slots__ = ("type", "cloned_entity", "cloned_entity_status", "destroy_cloned_entity_state", "error", "full_view_name")
    class DestroyClonedEntityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[DestroyClonedEntityInfoProto.DestroyClonedEntityState]
        kFinished: _ClassVar[DestroyClonedEntityInfoProto.DestroyClonedEntityState]
    kNotStarted: DestroyClonedEntityInfoProto.DestroyClonedEntityState
    kFinished: DestroyClonedEntityInfoProto.DestroyClonedEntityState
    class ClonedEntity(_message.Message):
        __slots__ = ("entity", "relative_restore_path_vec")
        Extensions: _python_message._ExtensionDict
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_RESTORE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        relative_restore_path_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., relative_restore_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLONED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CLONED_ENTITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONED_ENTITY_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FULL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    cloned_entity: DestroyClonedEntityInfoProto.ClonedEntity
    cloned_entity_status: RestoreEntityStatus.Type
    destroy_cloned_entity_state: DestroyClonedEntityInfoProto.DestroyClonedEntityState
    error: _error_pb2.ErrorProto
    full_view_name: str
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., cloned_entity: _Optional[_Union[DestroyClonedEntityInfoProto.ClonedEntity, _Mapping]] = ..., cloned_entity_status: _Optional[_Union[RestoreEntityStatus.Type, str]] = ..., destroy_cloned_entity_state: _Optional[_Union[DestroyClonedEntityInfoProto.DestroyClonedEntityState, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., full_view_name: _Optional[str] = ...) -> None: ...

class DestroyClonedVMTaskInfoProto(_message.Message):
    __slots__ = ("type", "destroy_cloned_entity_info_vec", "datastore_unmounted", "datastore_not_unmounted_reason", "view_deleted")
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONED_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_UNMOUNTED_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NOT_UNMOUNTED_REASON_FIELD_NUMBER: _ClassVar[int]
    VIEW_DELETED_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    destroy_cloned_entity_info_vec: _containers.RepeatedCompositeFieldContainer[DestroyClonedEntityInfoProto]
    datastore_unmounted: bool
    datastore_not_unmounted_reason: str
    view_deleted: bool
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., destroy_cloned_entity_info_vec: _Optional[_Iterable[_Union[DestroyClonedEntityInfoProto, _Mapping]]] = ..., datastore_unmounted: bool = ..., datastore_not_unmounted_reason: _Optional[str] = ..., view_deleted: bool = ...) -> None: ...

class SetupRestoreDiskTaskInfoProto(_message.Message):
    __slots__ = ("entity", "root_entity", "view_box_id", "source_view_name", "view_name", "task_id", "progress_monitor_root_task_path")
    Extensions: _python_message._ExtensionDict
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_ROOT_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    root_entity: _entity_pb2.EntityProto
    view_box_id: int
    source_view_name: str
    view_name: str
    task_id: int
    progress_monitor_root_task_path: str
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., view_box_id: _Optional[int] = ..., source_view_name: _Optional[str] = ..., view_name: _Optional[str] = ..., task_id: _Optional[int] = ..., progress_monitor_root_task_path: _Optional[str] = ...) -> None: ...

class RestoreFileStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[RestoreFileStatus.Type]
        kEstimationInProgress: _ClassVar[RestoreFileStatus.Type]
        kEstimationDone: _ClassVar[RestoreFileStatus.Type]
        kCopyInProgress: _ClassVar[RestoreFileStatus.Type]
        kFinished: _ClassVar[RestoreFileStatus.Type]
    kNotStarted: RestoreFileStatus.Type
    kEstimationInProgress: RestoreFileStatus.Type
    kEstimationDone: RestoreFileStatus.Type
    kCopyInProgress: RestoreFileStatus.Type
    kFinished: RestoreFileStatus.Type
    def __init__(self) -> None: ...

class RestoreFileCopyStats(_message.Message):
    __slots__ = ("estimation_skipped", "total_files_to_copy", "total_directories_to_copy", "total_bytes_to_copy", "num_files_copied", "num_directories_copied", "num_bytes_copied", "num_errors")
    ESTIMATION_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIRECTORIES_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_COPIED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_COPIED_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_COPIED_FIELD_NUMBER: _ClassVar[int]
    NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    estimation_skipped: bool
    total_files_to_copy: int
    total_directories_to_copy: int
    total_bytes_to_copy: int
    num_files_copied: int
    num_directories_copied: int
    num_bytes_copied: int
    num_errors: int
    def __init__(self, estimation_skipped: bool = ..., total_files_to_copy: _Optional[int] = ..., total_directories_to_copy: _Optional[int] = ..., total_bytes_to_copy: _Optional[int] = ..., num_files_copied: _Optional[int] = ..., num_directories_copied: _Optional[int] = ..., num_bytes_copied: _Optional[int] = ..., num_errors: _Optional[int] = ...) -> None: ...

class RestoreFileResultInfo(_message.Message):
    __slots__ = ("restored_file_info", "status", "error", "copy_stats", "destination_dir")
    RESTORED_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COPY_STATS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DIR_FIELD_NUMBER: _ClassVar[int]
    restored_file_info: RestoredFileInfo
    status: RestoreFileStatus.Type
    error: _error_pb2.ErrorProto
    copy_stats: RestoreFileCopyStats
    destination_dir: str
    def __init__(self, restored_file_info: _Optional[_Union[RestoredFileInfo, _Mapping]] = ..., status: _Optional[_Union[RestoreFileStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., copy_stats: _Optional[_Union[RestoreFileCopyStats, _Mapping]] = ..., destination_dir: _Optional[str] = ...) -> None: ...

class RestoreFilesInfoProto(_message.Message):
    __slots__ = ("type", "error", "teardown_error", "restore_files_result_vec", "slave_task_start_time_usecs", "download_files_path", "target_type", "proxy_entity_connector_params", "expiry_time_usecs")
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILES_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROXY_ENTITY_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    error: _error_pb2.ErrorProto
    teardown_error: _error_pb2.ErrorProto
    restore_files_result_vec: _containers.RepeatedCompositeFieldContainer[RestoreFileResultInfo]
    slave_task_start_time_usecs: int
    download_files_path: str
    target_type: _enums_pb2.TargetType.Type
    proxy_entity_connector_params: ConnectorParams
    expiry_time_usecs: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., teardown_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_files_result_vec: _Optional[_Iterable[_Union[RestoreFileResultInfo, _Mapping]]] = ..., slave_task_start_time_usecs: _Optional[int] = ..., download_files_path: _Optional[str] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., proxy_entity_connector_params: _Optional[_Union[ConnectorParams, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ...) -> None: ...

class MountVolumeResult(_message.Message):
    __slots__ = ("error", "original_volume_name", "mount_point", "filesystem_type")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    original_volume_name: str
    mount_point: str
    filesystem_type: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., original_volume_name: _Optional[str] = ..., mount_point: _Optional[str] = ..., filesystem_type: _Optional[str] = ...) -> None: ...

class MountVolumesInfoProto(_message.Message):
    __slots__ = ("type", "error", "cleanup_error", "vm_online_disks_error", "mount_volume_result_vec", "finished", "restore_disks_task_info_proto", "slave_task_start_time_usecs")
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_ONLINE_DISKS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUME_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    error: _error_pb2.ErrorProto
    cleanup_error: _error_pb2.ErrorProto
    vm_online_disks_error: _error_pb2.ErrorProto
    mount_volume_result_vec: _containers.RepeatedCompositeFieldContainer[MountVolumeResult]
    finished: bool
    restore_disks_task_info_proto: SetupRestoreDiskTaskInfoProto
    slave_task_start_time_usecs: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cleanup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_online_disks_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mount_volume_result_vec: _Optional[_Iterable[_Union[MountVolumeResult, _Mapping]]] = ..., finished: bool = ..., restore_disks_task_info_proto: _Optional[_Union[SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., slave_task_start_time_usecs: _Optional[int] = ...) -> None: ...

class RecoverVirtualDiskInfoProto(_message.Message):
    __slots__ = ("type", "error", "cleanup_error", "data_migration_error", "instant_recovery_finished", "finished", "restore_disks_task_info_proto", "slave_task_start_time_usecs", "task_state", "migrate_task_moref")
    Extensions: _python_message._ExtensionDict
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDetachDisksDone: _ClassVar[RecoverVirtualDiskInfoProto.State]
        kSetupDisksDone: _ClassVar[RecoverVirtualDiskInfoProto.State]
        kMigrateDisksStarted: _ClassVar[RecoverVirtualDiskInfoProto.State]
        kMigrateDisksDone: _ClassVar[RecoverVirtualDiskInfoProto.State]
        kUnMountDatastoreDone: _ClassVar[RecoverVirtualDiskInfoProto.State]
    kDetachDisksDone: RecoverVirtualDiskInfoProto.State
    kSetupDisksDone: RecoverVirtualDiskInfoProto.State
    kMigrateDisksStarted: RecoverVirtualDiskInfoProto.State
    kMigrateDisksDone: RecoverVirtualDiskInfoProto.State
    kUnMountDatastoreDone: RecoverVirtualDiskInfoProto.State
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_MIGRATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTANT_RECOVERY_FINISHED_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    error: _error_pb2.ErrorProto
    cleanup_error: _error_pb2.ErrorProto
    data_migration_error: _error_pb2.ErrorProto
    instant_recovery_finished: bool
    finished: bool
    restore_disks_task_info_proto: SetupRestoreDiskTaskInfoProto
    slave_task_start_time_usecs: int
    task_state: RecoverVirtualDiskInfoProto.State
    migrate_task_moref: _vmware_common_pb2.MORef
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cleanup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data_migration_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., instant_recovery_finished: bool = ..., finished: bool = ..., restore_disks_task_info_proto: _Optional[_Union[SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., slave_task_start_time_usecs: _Optional[int] = ..., task_state: _Optional[_Union[RecoverVirtualDiskInfoProto.State, str]] = ..., migrate_task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class DestroyMountVolumesTaskInfoProto(_message.Message):
    __slots__ = ("target_entity", "mount_volumes_info_proto", "error", "finished", "slave_task_start_time_usecs", "host_name", "use_existing_agent", "vmware_params")
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_AGENT_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    target_entity: _entity_pb2.EntityProto
    mount_volumes_info_proto: MountVolumesInfoProto
    error: _error_pb2.ErrorProto
    finished: bool
    slave_task_start_time_usecs: int
    host_name: str
    use_existing_agent: bool
    vmware_params: MountVolumesVMwareParams
    def __init__(self, target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., mount_volumes_info_proto: _Optional[_Union[MountVolumesInfoProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., finished: bool = ..., slave_task_start_time_usecs: _Optional[int] = ..., host_name: _Optional[str] = ..., use_existing_agent: bool = ..., vmware_params: _Optional[_Union[MountVolumesVMwareParams, _Mapping]] = ...) -> None: ...

class DestroyCloneAppTaskInfoProto(_message.Message):
    __slots__ = ("app_env", "target_entity", "target_entity_credentials", "error", "finished")
    Extensions: _python_message._ExtensionDict
    APP_ENV_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    app_env: _enums_pb2.Environment.Type
    target_entity: _entity_pb2.EntityProto
    target_entity_credentials: _credentials_pb2.Credentials
    error: _error_pb2.ErrorProto
    finished: bool
    def __init__(self, app_env: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., finished: bool = ...) -> None: ...

class DeactivateEntityStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[DeactivateEntityStatus.Type]
        kFinished: _ClassVar[DeactivateEntityStatus.Type]
    kNotStarted: DeactivateEntityStatus.Type
    kFinished: DeactivateEntityStatus.Type
    def __init__(self) -> None: ...

class DeactivateJobEntitiesInfoProto(_message.Message):
    __slots__ = ("type", "deactivated_entity_vec")
    class DeactivatedEntity(_message.Message):
        __slots__ = ("entity", "status", "error")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        status: DeactivateEntityStatus.Type
        error: _error_pb2.ErrorProto
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., status: _Optional[_Union[DeactivateEntityStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    deactivated_entity_vec: _containers.RepeatedCompositeFieldContainer[DeactivateJobEntitiesInfoProto.DeactivatedEntity]
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., deactivated_entity_vec: _Optional[_Iterable[_Union[DeactivateJobEntitiesInfoProto.DeactivatedEntity, _Mapping]]] = ...) -> None: ...

class ThrottlingPolicy(_message.Message):
    __slots__ = ("entity", "is_registered_source_throttling_config_enabled", "registered_source_throttling_config", "is_throttling_enabled", "latency_thresholds", "is_datastore_streams_config_enabled", "datastore_streams_config", "datastore_throttling_policies", "is_max_snapshots_config_enabled", "is_max_space_config_enabled", "storage_array_snapshot_max_snapshot_config", "storage_array_snapshot_max_space_config", "storage_array_snapshot_throttling_policies")
    class RegisteredSourceThrottlingConfig(_message.Message):
        __slots__ = ("max_concurrent_backups", "nas_throttling_params", "uda_throttling_params")
        MAX_CONCURRENT_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        NAS_THROTTLING_PARAMS_FIELD_NUMBER: _ClassVar[int]
        UDA_THROTTLING_PARAMS_FIELD_NUMBER: _ClassVar[int]
        max_concurrent_backups: int
        nas_throttling_params: _env_params_pb2.NasThrottlingParams
        uda_throttling_params: _env_params_pb2.UdaThrottlingParams
        def __init__(self, max_concurrent_backups: _Optional[int] = ..., nas_throttling_params: _Optional[_Union[_env_params_pb2.NasThrottlingParams, _Mapping]] = ..., uda_throttling_params: _Optional[_Union[_env_params_pb2.UdaThrottlingParams, _Mapping]] = ...) -> None: ...
    class LatencyThresholds(_message.Message):
        __slots__ = ("new_task_latency_threshold_msecs", "active_task_latency_threshold_msecs")
        NEW_TASK_LATENCY_THRESHOLD_MSECS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_TASK_LATENCY_THRESHOLD_MSECS_FIELD_NUMBER: _ClassVar[int]
        new_task_latency_threshold_msecs: int
        active_task_latency_threshold_msecs: int
        def __init__(self, new_task_latency_threshold_msecs: _Optional[int] = ..., active_task_latency_threshold_msecs: _Optional[int] = ...) -> None: ...
    class DatastoreStreamsConfig(_message.Message):
        __slots__ = ("max_concurrent_streams",)
        MAX_CONCURRENT_STREAMS_FIELD_NUMBER: _ClassVar[int]
        max_concurrent_streams: int
        def __init__(self, max_concurrent_streams: _Optional[int] = ...) -> None: ...
    class DatastoreThrottlingPolicy(_message.Message):
        __slots__ = ("datastore_entity", "is_throttling_enabled", "latency_thresholds", "is_datastore_streams_config_enabled", "datastore_streams_config")
        DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
        IS_THROTTLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LATENCY_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        IS_DATASTORE_STREAMS_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_STREAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
        datastore_entity: _entity_pb2.EntityProto
        is_throttling_enabled: bool
        latency_thresholds: ThrottlingPolicy.LatencyThresholds
        is_datastore_streams_config_enabled: bool
        datastore_streams_config: ThrottlingPolicy.DatastoreStreamsConfig
        def __init__(self, datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_throttling_enabled: bool = ..., latency_thresholds: _Optional[_Union[ThrottlingPolicy.LatencyThresholds, _Mapping]] = ..., is_datastore_streams_config_enabled: bool = ..., datastore_streams_config: _Optional[_Union[ThrottlingPolicy.DatastoreStreamsConfig, _Mapping]] = ...) -> None: ...
    class StorageArraySnapshotMaxSnapshotConfig(_message.Message):
        __slots__ = ("max_snapshots",)
        MAX_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        max_snapshots: int
        def __init__(self, max_snapshots: _Optional[int] = ...) -> None: ...
    class StorageArraySnapshotMaxSpaceConfig(_message.Message):
        __slots__ = ("max_snapshot_space_percentage",)
        MAX_SNAPSHOT_SPACE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        max_snapshot_space_percentage: int
        def __init__(self, max_snapshot_space_percentage: _Optional[int] = ...) -> None: ...
    class StorageArraySnapshotThrottlingPolicy(_message.Message):
        __slots__ = ("storage_entity", "is_max_snapshots_config_enabled", "is_max_space_config_enabled", "max_snapshot_config", "max_space_config")
        STORAGE_ENTITY_FIELD_NUMBER: _ClassVar[int]
        IS_MAX_SNAPSHOTS_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
        IS_MAX_SPACE_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MAX_SNAPSHOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        MAX_SPACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        storage_entity: _entity_pb2.EntityProto
        is_max_snapshots_config_enabled: bool
        is_max_space_config_enabled: bool
        max_snapshot_config: ThrottlingPolicy.StorageArraySnapshotMaxSnapshotConfig
        max_space_config: ThrottlingPolicy.StorageArraySnapshotMaxSpaceConfig
        def __init__(self, storage_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_max_snapshots_config_enabled: bool = ..., is_max_space_config_enabled: bool = ..., max_snapshot_config: _Optional[_Union[ThrottlingPolicy.StorageArraySnapshotMaxSnapshotConfig, _Mapping]] = ..., max_space_config: _Optional[_Union[ThrottlingPolicy.StorageArraySnapshotMaxSpaceConfig, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_SOURCE_THROTTLING_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_THROTTLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LATENCY_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    IS_DATASTORE_STREAMS_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_STREAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_THROTTLING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    IS_MAX_SNAPSHOTS_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_MAX_SPACE_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_MAX_SNAPSHOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_MAX_SPACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_THROTTLING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    is_registered_source_throttling_config_enabled: bool
    registered_source_throttling_config: ThrottlingPolicy.RegisteredSourceThrottlingConfig
    is_throttling_enabled: bool
    latency_thresholds: ThrottlingPolicy.LatencyThresholds
    is_datastore_streams_config_enabled: bool
    datastore_streams_config: ThrottlingPolicy.DatastoreStreamsConfig
    datastore_throttling_policies: _containers.RepeatedCompositeFieldContainer[ThrottlingPolicy.DatastoreThrottlingPolicy]
    is_max_snapshots_config_enabled: bool
    is_max_space_config_enabled: bool
    storage_array_snapshot_max_snapshot_config: ThrottlingPolicy.StorageArraySnapshotMaxSnapshotConfig
    storage_array_snapshot_max_space_config: ThrottlingPolicy.StorageArraySnapshotMaxSpaceConfig
    storage_array_snapshot_throttling_policies: _containers.RepeatedCompositeFieldContainer[ThrottlingPolicy.StorageArraySnapshotThrottlingPolicy]
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_registered_source_throttling_config_enabled: bool = ..., registered_source_throttling_config: _Optional[_Union[ThrottlingPolicy.RegisteredSourceThrottlingConfig, _Mapping]] = ..., is_throttling_enabled: bool = ..., latency_thresholds: _Optional[_Union[ThrottlingPolicy.LatencyThresholds, _Mapping]] = ..., is_datastore_streams_config_enabled: bool = ..., datastore_streams_config: _Optional[_Union[ThrottlingPolicy.DatastoreStreamsConfig, _Mapping]] = ..., datastore_throttling_policies: _Optional[_Iterable[_Union[ThrottlingPolicy.DatastoreThrottlingPolicy, _Mapping]]] = ..., is_max_snapshots_config_enabled: bool = ..., is_max_space_config_enabled: bool = ..., storage_array_snapshot_max_snapshot_config: _Optional[_Union[ThrottlingPolicy.StorageArraySnapshotMaxSnapshotConfig, _Mapping]] = ..., storage_array_snapshot_max_space_config: _Optional[_Union[ThrottlingPolicy.StorageArraySnapshotMaxSpaceConfig, _Mapping]] = ..., storage_array_snapshot_throttling_policies: _Optional[_Iterable[_Union[ThrottlingPolicy.StorageArraySnapshotThrottlingPolicy, _Mapping]]] = ...) -> None: ...

class ThrottlingPolicies(_message.Message):
    __slots__ = ("throttling_policies",)
    THROTTLING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    throttling_policies: _containers.RepeatedCompositeFieldContainer[ThrottlingPolicy]
    def __init__(self, throttling_policies: _Optional[_Iterable[_Union[ThrottlingPolicy, _Mapping]]] = ...) -> None: ...

class DatastoreLatencies(_message.Message):
    __slots__ = ("datastore_latencies",)
    class DatastoreLatency(_message.Message):
        __slots__ = ("datastore_entity", "latency_msecs")
        DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
        LATENCY_MSECS_FIELD_NUMBER: _ClassVar[int]
        datastore_entity: _entity_pb2.EntityProto
        latency_msecs: int
        def __init__(self, datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., latency_msecs: _Optional[int] = ...) -> None: ...
    DATASTORE_LATENCIES_FIELD_NUMBER: _ClassVar[int]
    datastore_latencies: _containers.RepeatedCompositeFieldContainer[DatastoreLatencies.DatastoreLatency]
    def __init__(self, datastore_latencies: _Optional[_Iterable[_Union[DatastoreLatencies.DatastoreLatency, _Mapping]]] = ...) -> None: ...

class RegisteredAppInfo(_message.Message):
    __slots__ = ("env", "verification_status", "verification_error", "refresh_error", "host_settings_check_result_vec")
    ENV_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_SETTINGS_CHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    env: _enums_pb2.Environment.Type
    verification_status: _enums_pb2.VerificationStatus.Type
    verification_error: _error_pb2.ErrorProto
    refresh_error: _error_pb2.ErrorProto
    host_settings_check_result_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostSettingsCheckResult]
    def __init__(self, env: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., verification_status: _Optional[_Union[_enums_pb2.VerificationStatus.Type, str]] = ..., verification_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., refresh_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_settings_check_result_vec: _Optional[_Iterable[_Union[_agent_pb2.HostSettingsCheckResult, _Mapping]]] = ...) -> None: ...

class RegisteredEntityInfo(_message.Message):
    __slots__ = ("connector_params", "is_storage_snapshot_provider", "throttling_policy", "registration_time_usecs", "last_refresh_time_usecs", "refresh_error", "verification_status", "verification_error", "verification_warning_vec", "progress_monitor_path", "source_side_dedup_enabled", "app_env_vec", "app_credentials_vec", "registered_app_info_vec", "user_messages", "registered_entity_params", "is_registered_by_user", "cluster_software_version_during_last_refresh", "restricted_object_id_map")
    class RestrictedObjectIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_STORAGE_SNAPSHOT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_POLICY_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ERROR_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    APP_ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_APP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_DURING_LAST_REFRESH_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_OBJECT_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    connector_params: ConnectorParams
    is_storage_snapshot_provider: bool
    throttling_policy: ThrottlingPolicy
    registration_time_usecs: int
    last_refresh_time_usecs: int
    refresh_error: _error_pb2.ErrorProto
    verification_status: _enums_pb2.VerificationStatus.Type
    verification_error: _error_pb2.ErrorProto
    verification_warning_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    progress_monitor_path: str
    source_side_dedup_enabled: bool
    app_env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.AppCredentials]
    registered_app_info_vec: _containers.RepeatedCompositeFieldContainer[RegisteredAppInfo]
    user_messages: _containers.RepeatedScalarFieldContainer[str]
    registered_entity_params: RegisteredEntityParams
    is_registered_by_user: bool
    cluster_software_version_during_last_refresh: str
    restricted_object_id_map: _containers.ScalarMap[str, bool]
    def __init__(self, connector_params: _Optional[_Union[ConnectorParams, _Mapping]] = ..., is_storage_snapshot_provider: bool = ..., throttling_policy: _Optional[_Union[ThrottlingPolicy, _Mapping]] = ..., registration_time_usecs: _Optional[int] = ..., last_refresh_time_usecs: _Optional[int] = ..., refresh_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., verification_status: _Optional[_Union[_enums_pb2.VerificationStatus.Type, str]] = ..., verification_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., verification_warning_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., progress_monitor_path: _Optional[str] = ..., source_side_dedup_enabled: bool = ..., app_env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.AppCredentials, _Mapping]]] = ..., registered_app_info_vec: _Optional[_Iterable[_Union[RegisteredAppInfo, _Mapping]]] = ..., user_messages: _Optional[_Iterable[str]] = ..., registered_entity_params: _Optional[_Union[RegisteredEntityParams, _Mapping]] = ..., is_registered_by_user: bool = ..., cluster_software_version_during_last_refresh: _Optional[str] = ..., restricted_object_id_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class VCDVCenterInfo(_message.Message):
    __slots__ = ("name", "endpoint", "credentials", "register_as_standalone_source", "id", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    REGISTER_AS_STANDALONE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    endpoint: str
    credentials: _credentials_pb2.Credentials
    register_as_standalone_source: bool
    id: int
    version: int
    def __init__(self, name: _Optional[str] = ..., endpoint: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., register_as_standalone_source: bool = ..., id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class RegisteredEntityVCDParams(_message.Message):
    __slots__ = ("vcenter_info_list",)
    VCENTER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    vcenter_info_list: _containers.RepeatedCompositeFieldContainer[VCDVCenterInfo]
    def __init__(self, vcenter_info_list: _Optional[_Iterable[_Union[VCDVCenterInfo, _Mapping]]] = ...) -> None: ...

class RegisteredEntityVMwareParams(_message.Message):
    __slots__ = ("use_vm_bios_uuid", "vcd_params", "storage_snapshot_providers", "preferred_subnet_vec", "link_vms_across_vcenter")
    USE_VM_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    VCD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    LINK_VMS_ACROSS_VCENTER_FIELD_NUMBER: _ClassVar[int]
    use_vm_bios_uuid: bool
    vcd_params: RegisteredEntityVCDParams
    storage_snapshot_providers: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    preferred_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    link_vms_across_vcenter: bool
    def __init__(self, use_vm_bios_uuid: bool = ..., vcd_params: _Optional[_Union[RegisteredEntityVCDParams, _Mapping]] = ..., storage_snapshot_providers: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., preferred_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., link_vms_across_vcenter: bool = ...) -> None: ...

class RegisteredEntityGenericNasParams(_message.Message):
    __slots__ = ("skip_validation",)
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    skip_validation: bool
    def __init__(self, skip_validation: bool = ...) -> None: ...

class RegisteredEntityCassandraParams(_message.Message):
    __slots__ = ("is_discovery_request", "cassandra_connect_params", "cassandra_additional_params")
    IS_DISCOVERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    is_discovery_request: bool
    cassandra_connect_params: _nosql_pb2.CassandraConnectParams
    cassandra_additional_params: _nosql_pb2.CassandraAdditionalParams
    def __init__(self, is_discovery_request: bool = ..., cassandra_connect_params: _Optional[_Union[_nosql_pb2.CassandraConnectParams, _Mapping]] = ..., cassandra_additional_params: _Optional[_Union[_nosql_pb2.CassandraAdditionalParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityMongoDBParams(_message.Message):
    __slots__ = ("mongodb_connect_params", "mongodb_additional_params")
    MONGODB_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    mongodb_connect_params: _nosql_pb2.MongoDBConnectParams
    mongodb_additional_params: _nosql_pb2.MongoDBAdditionalParams
    def __init__(self, mongodb_connect_params: _Optional[_Union[_nosql_pb2.MongoDBConnectParams, _Mapping]] = ..., mongodb_additional_params: _Optional[_Union[_nosql_pb2.MongoDBAdditionalParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityCouchbaseParams(_message.Message):
    __slots__ = ("couchbase_connect_params",)
    COUCHBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    couchbase_connect_params: _nosql_pb2.CouchbaseConnectParams
    def __init__(self, couchbase_connect_params: _Optional[_Union[_nosql_pb2.CouchbaseConnectParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityHBaseParams(_message.Message):
    __slots__ = ("is_discovery_request", "hbase_connect_params", "hbase_discovery_params")
    IS_DISCOVERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HBASE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    is_discovery_request: bool
    hbase_connect_params: _nosql_pb2.HBaseConnectParams
    hbase_discovery_params: _nosql_pb2.HBaseDiscoveryParams
    def __init__(self, is_discovery_request: bool = ..., hbase_connect_params: _Optional[_Union[_nosql_pb2.HBaseConnectParams, _Mapping]] = ..., hbase_discovery_params: _Optional[_Union[_nosql_pb2.HBaseDiscoveryParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityHdfsParams(_message.Message):
    __slots__ = ("is_discovery_request", "hdfs_connect_params", "hdfs_discovery_params")
    IS_DISCOVERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    is_discovery_request: bool
    hdfs_connect_params: _nosql_pb2.HdfsConnectParams
    hdfs_discovery_params: _nosql_pb2.HdfsDiscoveryParams
    def __init__(self, is_discovery_request: bool = ..., hdfs_connect_params: _Optional[_Union[_nosql_pb2.HdfsConnectParams, _Mapping]] = ..., hdfs_discovery_params: _Optional[_Union[_nosql_pb2.HdfsDiscoveryParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityHiveParams(_message.Message):
    __slots__ = ("is_discovery_request", "hive_connect_params", "hive_discovery_params")
    IS_DISCOVERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HIVE_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    is_discovery_request: bool
    hive_connect_params: _nosql_pb2.HiveConnectParams
    hive_discovery_params: _nosql_pb2.HiveDiscoveryParams
    def __init__(self, is_discovery_request: bool = ..., hive_connect_params: _Optional[_Union[_nosql_pb2.HiveConnectParams, _Mapping]] = ..., hive_discovery_params: _Optional[_Union[_nosql_pb2.HiveDiscoveryParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityIsilonParams(_message.Message):
    __slots__ = ("isilon_env_params",)
    ISILON_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    isilon_env_params: _env_params_pb2.IsilonEnvParams
    def __init__(self, isilon_env_params: _Optional[_Union[_env_params_pb2.IsilonEnvParams, _Mapping]] = ...) -> None: ...

class RegisteredEntityPhysicalParams(_message.Message):
    __slots__ = ("app_env_vec", "credentials", "app_credentials_vec", "source_throttling_config")
    APP_ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    app_env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    credentials: _credentials_pb2.Credentials
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.AppCredentials]
    source_throttling_config: _source_throttling_pb2.SourceThrottlingConfiguration
    def __init__(self, app_env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.AppCredentials, _Mapping]]] = ..., source_throttling_config: _Optional[_Union[_source_throttling_pb2.SourceThrottlingConfiguration, _Mapping]] = ...) -> None: ...

class RegisteredEntityUdaParams(_message.Message):
    __slots__ = ("hosts", "credentials", "mount_view", "mount_dir", "script_dir", "source_args", "source_type", "host_type", "fresh_full_backup_view", "capabilities", "preferred_control_nodes", "live_data_view", "use_s3_view", "live_log_view", "object_types", "static_live_log_view", "source_arguments_map", "restrict_parallel_data_log_backups", "parallel_log_backups", "et_enable_log_backup_policy", "et_enable_run_now", "deployment_type", "pre_backup_job_script_failure_tolerance")
    class SourceArgumentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _uda_pb2.UdaCustomArgument
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_uda_pb2.UdaCustomArgument, _Mapping]] = ...) -> None: ...
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VIEW_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DIR_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    FRESH_FULL_BACKUP_VIEW_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_CONTROL_NODES_FIELD_NUMBER: _ClassVar[int]
    LIVE_DATA_VIEW_FIELD_NUMBER: _ClassVar[int]
    USE_S3_VIEW_FIELD_NUMBER: _ClassVar[int]
    LIVE_LOG_VIEW_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    STATIC_LIVE_LOG_VIEW_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARGUMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_PARALLEL_DATA_LOG_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_LOG_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    ET_ENABLE_LOG_BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ET_ENABLE_RUN_NOW_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRE_BACKUP_JOB_SCRIPT_FAILURE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    credentials: _credentials_pb2.Credentials
    mount_view: bool
    mount_dir: str
    script_dir: str
    source_args: str
    source_type: str
    host_type: _enums_pb2.HostEnv.Type
    fresh_full_backup_view: bool
    capabilities: _uda_pb2.UdaSourceCapabilities
    preferred_control_nodes: _containers.RepeatedScalarFieldContainer[str]
    live_data_view: bool
    use_s3_view: bool
    live_log_view: bool
    object_types: _containers.RepeatedScalarFieldContainer[str]
    static_live_log_view: bool
    source_arguments_map: _containers.MessageMap[str, _uda_pb2.UdaCustomArgument]
    restrict_parallel_data_log_backups: bool
    parallel_log_backups: bool
    et_enable_log_backup_policy: bool
    et_enable_run_now: bool
    deployment_type: _uda_pb2.UdaAgentDeployment.Type
    pre_backup_job_script_failure_tolerance: _uda_pb2.PreJobScriptFailureTolerance
    def __init__(self, hosts: _Optional[_Iterable[str]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., mount_view: bool = ..., mount_dir: _Optional[str] = ..., script_dir: _Optional[str] = ..., source_args: _Optional[str] = ..., source_type: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., fresh_full_backup_view: bool = ..., capabilities: _Optional[_Union[_uda_pb2.UdaSourceCapabilities, _Mapping]] = ..., preferred_control_nodes: _Optional[_Iterable[str]] = ..., live_data_view: bool = ..., use_s3_view: bool = ..., live_log_view: bool = ..., object_types: _Optional[_Iterable[str]] = ..., static_live_log_view: bool = ..., source_arguments_map: _Optional[_Mapping[str, _uda_pb2.UdaCustomArgument]] = ..., restrict_parallel_data_log_backups: bool = ..., parallel_log_backups: bool = ..., et_enable_log_backup_policy: bool = ..., et_enable_run_now: bool = ..., deployment_type: _Optional[_Union[_uda_pb2.UdaAgentDeployment.Type, str]] = ..., pre_backup_job_script_failure_tolerance: _Optional[_Union[_uda_pb2.PreJobScriptFailureTolerance, str]] = ...) -> None: ...

class RegisteredEntityO365Params(_message.Message):
    __slots__ = ("discoverable_entity_type_vec", "user_entity_discovery_params", "use_existing_credentials", "enable_site_tagging", "pending_background_entity_fetch", "team_entity_additional_params")
    class UserEntityDiscoveryParams(_message.Message):
        __slots__ = ("discover_users_with_mailbox", "fetch_users_mailbox_info", "discover_users_with_onedrive", "fetch_users_onedrive_info", "skip_users_with_missing_onedrive_mysite", "allow_chats_backup")
        DISCOVER_USERS_WITH_MAILBOX_FIELD_NUMBER: _ClassVar[int]
        FETCH_USERS_MAILBOX_INFO_FIELD_NUMBER: _ClassVar[int]
        DISCOVER_USERS_WITH_ONEDRIVE_FIELD_NUMBER: _ClassVar[int]
        FETCH_USERS_ONEDRIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        SKIP_USERS_WITH_MISSING_ONEDRIVE_MYSITE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CHATS_BACKUP_FIELD_NUMBER: _ClassVar[int]
        discover_users_with_mailbox: bool
        fetch_users_mailbox_info: bool
        discover_users_with_onedrive: bool
        fetch_users_onedrive_info: bool
        skip_users_with_missing_onedrive_mysite: bool
        allow_chats_backup: bool
        def __init__(self, discover_users_with_mailbox: bool = ..., fetch_users_mailbox_info: bool = ..., discover_users_with_onedrive: bool = ..., fetch_users_onedrive_info: bool = ..., skip_users_with_missing_onedrive_mysite: bool = ..., allow_chats_backup: bool = ...) -> None: ...
    class TeamEntityAdditionalParams(_message.Message):
        __slots__ = ("allow_posts_backup",)
        ALLOW_POSTS_BACKUP_FIELD_NUMBER: _ClassVar[int]
        allow_posts_backup: bool
        def __init__(self, allow_posts_backup: bool = ...) -> None: ...
    DISCOVERABLE_ENTITY_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_ENTITY_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SITE_TAGGING_FIELD_NUMBER: _ClassVar[int]
    PENDING_BACKGROUND_ENTITY_FETCH_FIELD_NUMBER: _ClassVar[int]
    TEAM_ENTITY_ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    discoverable_entity_type_vec: _containers.RepeatedScalarFieldContainer[_o365_pb2.Entity.Type]
    user_entity_discovery_params: RegisteredEntityO365Params.UserEntityDiscoveryParams
    use_existing_credentials: bool
    enable_site_tagging: bool
    pending_background_entity_fetch: bool
    team_entity_additional_params: RegisteredEntityO365Params.TeamEntityAdditionalParams
    def __init__(self, discoverable_entity_type_vec: _Optional[_Iterable[_Union[_o365_pb2.Entity.Type, str]]] = ..., user_entity_discovery_params: _Optional[_Union[RegisteredEntityO365Params.UserEntityDiscoveryParams, _Mapping]] = ..., use_existing_credentials: bool = ..., enable_site_tagging: bool = ..., pending_background_entity_fetch: bool = ..., team_entity_additional_params: _Optional[_Union[RegisteredEntityO365Params.TeamEntityAdditionalParams, _Mapping]] = ...) -> None: ...

class NetworkRealmInfo(_message.Message):
    __slots__ = ("network_realm_id", "entity_id", "connector_group_id")
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    network_realm_id: int
    entity_id: int
    connector_group_id: int
    def __init__(self, network_realm_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ...) -> None: ...

class RegisteredEntityAzureParams(_message.Message):
    __slots__ = ("registration_level", "registration_workflow", "use_cases")
    class RegistrationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTenant: _ClassVar[RegisteredEntityAzureParams.RegistrationLevel]
        kSubscription: _ClassVar[RegisteredEntityAzureParams.RegistrationLevel]
    kTenant: RegisteredEntityAzureParams.RegistrationLevel
    kSubscription: RegisteredEntityAzureParams.RegistrationLevel
    class RegistrationWorkflow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kExpress: _ClassVar[RegisteredEntityAzureParams.RegistrationWorkflow]
        kManual: _ClassVar[RegisteredEntityAzureParams.RegistrationWorkflow]
    kExpress: RegisteredEntityAzureParams.RegistrationWorkflow
    kManual: RegisteredEntityAzureParams.RegistrationWorkflow
    class UseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVirtualMachine: _ClassVar[RegisteredEntityAzureParams.UseCase]
        kSQL: _ClassVar[RegisteredEntityAzureParams.UseCase]
    kVirtualMachine: RegisteredEntityAzureParams.UseCase
    kSQL: RegisteredEntityAzureParams.UseCase
    REGISTRATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    USE_CASES_FIELD_NUMBER: _ClassVar[int]
    registration_level: RegisteredEntityAzureParams.RegistrationLevel
    registration_workflow: RegisteredEntityAzureParams.RegistrationWorkflow
    use_cases: _containers.RepeatedScalarFieldContainer[RegisteredEntityAzureParams.UseCase]
    def __init__(self, registration_level: _Optional[_Union[RegisteredEntityAzureParams.RegistrationLevel, str]] = ..., registration_workflow: _Optional[_Union[RegisteredEntityAzureParams.RegistrationWorkflow, str]] = ..., use_cases: _Optional[_Iterable[_Union[RegisteredEntityAzureParams.UseCase, str]]] = ...) -> None: ...

class RegisteredEntityParams(_message.Message):
    __slots__ = ("description", "space_usage_policy", "throttling_policy", "vlan_params", "network_realm_id", "connector_group_id", "network_realm_info_vec", "vmware_params", "generic_nas_params", "cassandra_params", "mongodb_params", "couchbase_params", "hbase_params", "hdfs_params", "hive_params", "isilon_params", "physical_params", "uda_params", "o365_params", "sfdc_params", "kubernetes_params", "blacklisted_ip_addrs", "whitelisted_ip_addrs", "is_storage_array_snapshot_enabled", "config_vec", "azure_params")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPACE_USAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_POLICY_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GENERIC_NAS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ISILON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    O365_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    IS_STORAGE_ARRAY_SNAPSHOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    AZURE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    description: str
    space_usage_policy: SpaceUsagePolicy
    throttling_policy: ThrottlingPolicy
    vlan_params: _common_pb2.VlanParams
    network_realm_id: int
    connector_group_id: int
    network_realm_info_vec: _containers.RepeatedCompositeFieldContainer[NetworkRealmInfo]
    vmware_params: RegisteredEntityVMwareParams
    generic_nas_params: RegisteredEntityGenericNasParams
    cassandra_params: RegisteredEntityCassandraParams
    mongodb_params: RegisteredEntityMongoDBParams
    couchbase_params: RegisteredEntityCouchbaseParams
    hbase_params: RegisteredEntityHBaseParams
    hdfs_params: RegisteredEntityHdfsParams
    hive_params: RegisteredEntityHiveParams
    isilon_params: RegisteredEntityIsilonParams
    physical_params: RegisteredEntityPhysicalParams
    uda_params: RegisteredEntityUdaParams
    o365_params: RegisteredEntityO365Params
    sfdc_params: _sfdc_pb2.RegisteredEntitySfdcParams
    kubernetes_params: RegisteredEntityKubernetesParams
    blacklisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    whitelisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    is_storage_array_snapshot_enabled: bool
    config_vec: _containers.RepeatedCompositeFieldContainer[ConfigurationParams]
    azure_params: RegisteredEntityAzureParams
    def __init__(self, description: _Optional[str] = ..., space_usage_policy: _Optional[_Union[SpaceUsagePolicy, _Mapping]] = ..., throttling_policy: _Optional[_Union[ThrottlingPolicy, _Mapping]] = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., network_realm_info_vec: _Optional[_Iterable[_Union[NetworkRealmInfo, _Mapping]]] = ..., vmware_params: _Optional[_Union[RegisteredEntityVMwareParams, _Mapping]] = ..., generic_nas_params: _Optional[_Union[RegisteredEntityGenericNasParams, _Mapping]] = ..., cassandra_params: _Optional[_Union[RegisteredEntityCassandraParams, _Mapping]] = ..., mongodb_params: _Optional[_Union[RegisteredEntityMongoDBParams, _Mapping]] = ..., couchbase_params: _Optional[_Union[RegisteredEntityCouchbaseParams, _Mapping]] = ..., hbase_params: _Optional[_Union[RegisteredEntityHBaseParams, _Mapping]] = ..., hdfs_params: _Optional[_Union[RegisteredEntityHdfsParams, _Mapping]] = ..., hive_params: _Optional[_Union[RegisteredEntityHiveParams, _Mapping]] = ..., isilon_params: _Optional[_Union[RegisteredEntityIsilonParams, _Mapping]] = ..., physical_params: _Optional[_Union[RegisteredEntityPhysicalParams, _Mapping]] = ..., uda_params: _Optional[_Union[RegisteredEntityUdaParams, _Mapping]] = ..., o365_params: _Optional[_Union[RegisteredEntityO365Params, _Mapping]] = ..., sfdc_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., kubernetes_params: _Optional[_Union[RegisteredEntityKubernetesParams, _Mapping]] = ..., blacklisted_ip_addrs: _Optional[_Iterable[str]] = ..., whitelisted_ip_addrs: _Optional[_Iterable[str]] = ..., is_storage_array_snapshot_enabled: bool = ..., config_vec: _Optional[_Iterable[_Union[ConfigurationParams, _Mapping]]] = ..., azure_params: _Optional[_Union[RegisteredEntityAzureParams, _Mapping]] = ...) -> None: ...

class SpaceUsagePolicy(_message.Message):
    __slots__ = ("min_free_datastore_space_for_backup_gb", "min_free_datastore_space_for_backup_percentage")
    MIN_FREE_DATASTORE_SPACE_FOR_BACKUP_GB_FIELD_NUMBER: _ClassVar[int]
    MIN_FREE_DATASTORE_SPACE_FOR_BACKUP_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    min_free_datastore_space_for_backup_gb: int
    min_free_datastore_space_for_backup_percentage: int
    def __init__(self, min_free_datastore_space_for_backup_gb: _Optional[int] = ..., min_free_datastore_space_for_backup_percentage: _Optional[int] = ...) -> None: ...

class EntityHierarchyProto(_message.Message):
    __slots__ = ("is_super_root_entity", "children", "aux_children", "entity", "aggregated_protected_info_vec", "aggregated_cdp_protected_info_vec", "aggregated_unprotected_info_vec", "registered_entity_info", "entity_operation_info", "logical_size_in_bytes", "physical_size_in_bytes", "total_downtiered_size_in_bytes", "total_uptiered_size_in_bytes", "last_modification_time_usecs", "parent", "external_metadata")
    class AggregatedEntityInfo(_message.Message):
        __slots__ = ("type", "num_entities", "total_logical_size_in_bytes", "logical_replicated_size_in_bytes", "logical_archived_size_in_bytes")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_REPLICATED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_ARCHIVED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        type: _enums_pb2.Environment.Type
        num_entities: int
        total_logical_size_in_bytes: int
        logical_replicated_size_in_bytes: int
        logical_archived_size_in_bytes: int
        def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., num_entities: _Optional[int] = ..., total_logical_size_in_bytes: _Optional[int] = ..., logical_replicated_size_in_bytes: _Optional[int] = ..., logical_archived_size_in_bytes: _Optional[int] = ...) -> None: ...
    IS_SUPER_ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    AUX_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_PROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_CDP_PROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_UNPROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_OPERATION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DOWNTIERED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UPTIERED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    is_super_root_entity: bool
    children: _containers.RepeatedCompositeFieldContainer[EntityHierarchyProto]
    aux_children: _containers.RepeatedCompositeFieldContainer[EntityHierarchyProto]
    entity: _entity_pb2.EntityProto
    aggregated_protected_info_vec: _containers.RepeatedCompositeFieldContainer[EntityHierarchyProto.AggregatedEntityInfo]
    aggregated_cdp_protected_info_vec: EntityHierarchyProto.AggregatedEntityInfo
    aggregated_unprotected_info_vec: _containers.RepeatedCompositeFieldContainer[EntityHierarchyProto.AggregatedEntityInfo]
    registered_entity_info: RegisteredEntityInfo
    entity_operation_info: _entity_operations_pb2.EntityOperationInfoProto
    logical_size_in_bytes: int
    physical_size_in_bytes: int
    total_downtiered_size_in_bytes: int
    total_uptiered_size_in_bytes: int
    last_modification_time_usecs: int
    parent: EntityHierarchyProto
    external_metadata: EntityExternalMetadataProto
    def __init__(self, is_super_root_entity: bool = ..., children: _Optional[_Iterable[_Union[EntityHierarchyProto, _Mapping]]] = ..., aux_children: _Optional[_Iterable[_Union[EntityHierarchyProto, _Mapping]]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., aggregated_protected_info_vec: _Optional[_Iterable[_Union[EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ..., aggregated_cdp_protected_info_vec: _Optional[_Union[EntityHierarchyProto.AggregatedEntityInfo, _Mapping]] = ..., aggregated_unprotected_info_vec: _Optional[_Iterable[_Union[EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ..., registered_entity_info: _Optional[_Union[RegisteredEntityInfo, _Mapping]] = ..., entity_operation_info: _Optional[_Union[_entity_operations_pb2.EntityOperationInfoProto, _Mapping]] = ..., logical_size_in_bytes: _Optional[int] = ..., physical_size_in_bytes: _Optional[int] = ..., total_downtiered_size_in_bytes: _Optional[int] = ..., total_uptiered_size_in_bytes: _Optional[int] = ..., last_modification_time_usecs: _Optional[int] = ..., parent: _Optional[_Union[EntityHierarchyProto, _Mapping]] = ..., external_metadata: _Optional[_Union[EntityExternalMetadataProto, _Mapping]] = ...) -> None: ...

class EntityExternalMetadataProto(_message.Message):
    __slots__ = ("credentials", "uda_params", "maintenance_mode_config")
    Extensions: _python_message._ExtensionDict
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    UDA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    credentials: _credentials_pb2.Credentials
    uda_params: RegisteredEntityUdaParams
    maintenance_mode_config: MaintenanceModeConfigProto
    def __init__(self, credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., uda_params: _Optional[_Union[RegisteredEntityUdaParams, _Mapping]] = ..., maintenance_mode_config: _Optional[_Union[MaintenanceModeConfigProto, _Mapping]] = ...) -> None: ...

class HierarchyNode(_message.Message):
    __slots__ = ("entity_id", "child_entity_id_vec", "aux_child_entity_id_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    AUX_CHILD_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    child_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    aux_child_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, entity_id: _Optional[int] = ..., child_entity_id_vec: _Optional[_Iterable[int]] = ..., aux_child_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class EntityConnectivityProto(_message.Message):
    __slots__ = ("entity_id", "last_connectivity_check_time_usecs", "connection_state", "status_msg")
    Extensions: _python_message._ExtensionDict
    class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[EntityConnectivityProto.ConnectionState]
        kDisconnected: _ClassVar[EntityConnectivityProto.ConnectionState]
        kConnected: _ClassVar[EntityConnectivityProto.ConnectionState]
    kUnknown: EntityConnectivityProto.ConnectionState
    kDisconnected: EntityConnectivityProto.ConnectionState
    kConnected: EntityConnectivityProto.ConnectionState
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTIVITY_CHECK_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MSG_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    last_connectivity_check_time_usecs: int
    connection_state: EntityConnectivityProto.ConnectionState
    status_msg: str
    def __init__(self, entity_id: _Optional[int] = ..., last_connectivity_check_time_usecs: _Optional[int] = ..., connection_state: _Optional[_Union[EntityConnectivityProto.ConnectionState, str]] = ..., status_msg: _Optional[str] = ...) -> None: ...

class BackupPolicyProto(_message.Message):
    __slots__ = ("name", "periodicity", "continuous_schedule", "daily_schedule", "monthly_schedule", "one_off_schedule", "schedule_end", "start_window_interval_mins", "num_retries", "retry_delay_mins", "num_days_to_keep", "truncate_logs")
    class Periodicity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kContinuous: _ClassVar[BackupPolicyProto.Periodicity]
        kDaily: _ClassVar[BackupPolicyProto.Periodicity]
        kMonthly: _ClassVar[BackupPolicyProto.Periodicity]
        kOneOff: _ClassVar[BackupPolicyProto.Periodicity]
    kContinuous: BackupPolicyProto.Periodicity
    kDaily: BackupPolicyProto.Periodicity
    kMonthly: BackupPolicyProto.Periodicity
    kOneOff: BackupPolicyProto.Periodicity
    class Day(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSunday: _ClassVar[BackupPolicyProto.Day]
        kMonday: _ClassVar[BackupPolicyProto.Day]
        kTuesday: _ClassVar[BackupPolicyProto.Day]
        kWednesday: _ClassVar[BackupPolicyProto.Day]
        kThursday: _ClassVar[BackupPolicyProto.Day]
        kFriday: _ClassVar[BackupPolicyProto.Day]
        kSaturday: _ClassVar[BackupPolicyProto.Day]
    kSunday: BackupPolicyProto.Day
    kMonday: BackupPolicyProto.Day
    kTuesday: BackupPolicyProto.Day
    kWednesday: BackupPolicyProto.Day
    kThursday: BackupPolicyProto.Day
    kFriday: BackupPolicyProto.Day
    kSaturday: BackupPolicyProto.Day
    class ExclusionTimeRange(_message.Message):
        __slots__ = ("day", "start_time", "end_time")
        DAY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        day: BackupPolicyProto.Day
        start_time: _policy_pb2.Time
        end_time: _policy_pb2.Time
        def __init__(self, day: _Optional[_Union[BackupPolicyProto.Day, str]] = ..., start_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ..., end_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ...) -> None: ...
    class ContinuousSchedule(_message.Message):
        __slots__ = ("backup_interval_mins", "exclusion_ranges")
        BACKUP_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
        EXCLUSION_RANGES_FIELD_NUMBER: _ClassVar[int]
        backup_interval_mins: int
        exclusion_ranges: _containers.RepeatedCompositeFieldContainer[BackupPolicyProto.ExclusionTimeRange]
        def __init__(self, backup_interval_mins: _Optional[int] = ..., exclusion_ranges: _Optional[_Iterable[_Union[BackupPolicyProto.ExclusionTimeRange, _Mapping]]] = ...) -> None: ...
    class DailySchedule(_message.Message):
        __slots__ = ("time", "days")
        TIME_FIELD_NUMBER: _ClassVar[int]
        DAYS_FIELD_NUMBER: _ClassVar[int]
        time: _policy_pb2.Time
        days: _containers.RepeatedScalarFieldContainer[BackupPolicyProto.Day]
        def __init__(self, time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ..., days: _Optional[_Iterable[_Union[BackupPolicyProto.Day, str]]] = ...) -> None: ...
    class MonthlySchedule(_message.Message):
        __slots__ = ("day", "count", "time")
        class DayCountInMonth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFirst: _ClassVar[BackupPolicyProto.MonthlySchedule.DayCountInMonth]
            kSecond: _ClassVar[BackupPolicyProto.MonthlySchedule.DayCountInMonth]
            kThird: _ClassVar[BackupPolicyProto.MonthlySchedule.DayCountInMonth]
            kFourth: _ClassVar[BackupPolicyProto.MonthlySchedule.DayCountInMonth]
            kLast: _ClassVar[BackupPolicyProto.MonthlySchedule.DayCountInMonth]
        kFirst: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        kSecond: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        kThird: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        kFourth: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        kLast: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        DAY_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        day: BackupPolicyProto.Day
        count: BackupPolicyProto.MonthlySchedule.DayCountInMonth
        time: _policy_pb2.Time
        def __init__(self, day: _Optional[_Union[BackupPolicyProto.Day, str]] = ..., count: _Optional[_Union[BackupPolicyProto.MonthlySchedule.DayCountInMonth, str]] = ..., time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ...) -> None: ...
    class OneOffSchedule(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: _policy_pb2.Time
        def __init__(self, time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ...) -> None: ...
    class ScheduleEnd(_message.Message):
        __slots__ = ("end_time_usecs", "end_after_num_backups")
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_AFTER_NUM_BACKUPS_FIELD_NUMBER: _ClassVar[int]
        end_time_usecs: int
        end_after_num_backups: int
        def __init__(self, end_time_usecs: _Optional[int] = ..., end_after_num_backups: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DAILY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ONE_OFF_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_END_FIELD_NUMBER: _ClassVar[int]
    START_WINDOW_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_MINS_FIELD_NUMBER: _ClassVar[int]
    NUM_DAYS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_LOGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    periodicity: BackupPolicyProto.Periodicity
    continuous_schedule: BackupPolicyProto.ContinuousSchedule
    daily_schedule: BackupPolicyProto.DailySchedule
    monthly_schedule: BackupPolicyProto.MonthlySchedule
    one_off_schedule: BackupPolicyProto.OneOffSchedule
    schedule_end: BackupPolicyProto.ScheduleEnd
    start_window_interval_mins: int
    num_retries: int
    retry_delay_mins: int
    num_days_to_keep: int
    truncate_logs: bool
    def __init__(self, name: _Optional[str] = ..., periodicity: _Optional[_Union[BackupPolicyProto.Periodicity, str]] = ..., continuous_schedule: _Optional[_Union[BackupPolicyProto.ContinuousSchedule, _Mapping]] = ..., daily_schedule: _Optional[_Union[BackupPolicyProto.DailySchedule, _Mapping]] = ..., monthly_schedule: _Optional[_Union[BackupPolicyProto.MonthlySchedule, _Mapping]] = ..., one_off_schedule: _Optional[_Union[BackupPolicyProto.OneOffSchedule, _Mapping]] = ..., schedule_end: _Optional[_Union[BackupPolicyProto.ScheduleEnd, _Mapping]] = ..., start_window_interval_mins: _Optional[int] = ..., num_retries: _Optional[int] = ..., retry_delay_mins: _Optional[int] = ..., num_days_to_keep: _Optional[int] = ..., truncate_logs: bool = ...) -> None: ...

class JobPolicyProto(_message.Message):
    __slots__ = ("backup_policy", "snapshot_target_policy_vec")
    BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_policy: BackupPolicyProto
    snapshot_target_policy_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.SnapshotTargetPolicyProto]
    def __init__(self, backup_policy: _Optional[_Union[BackupPolicyProto, _Mapping]] = ..., snapshot_target_policy_vec: _Optional[_Iterable[_Union[_policy_pb2.SnapshotTargetPolicyProto, _Mapping]]] = ...) -> None: ...

class ScriptPathAndParams(_message.Message):
    __slots__ = ("script_path", "script_params", "timeout_secs", "continue_on_error", "is_active")
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    script_path: str
    script_params: str
    timeout_secs: int
    continue_on_error: bool
    is_active: bool
    def __init__(self, script_path: _Optional[str] = ..., script_params: _Optional[str] = ..., timeout_secs: _Optional[int] = ..., continue_on_error: bool = ..., is_active: bool = ...) -> None: ...

class RemoteHostConnectorParams(_message.Message):
    __slots__ = ("host_type", "host_address", "credentials")
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host_type: _enums_pb2.HostEnv.Type
    host_address: str
    credentials: _credentials_pb2.Credentials
    def __init__(self, host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., host_address: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class BackupJobPreOrPostScript(_message.Message):
    __slots__ = ("remote_host_params", "full_backup_script", "backup_script", "log_backup_script")
    REMOTE_HOST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    remote_host_params: RemoteHostConnectorParams
    full_backup_script: ScriptPathAndParams
    backup_script: ScriptPathAndParams
    log_backup_script: ScriptPathAndParams
    def __init__(self, remote_host_params: _Optional[_Union[RemoteHostConnectorParams, _Mapping]] = ..., full_backup_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ..., backup_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ..., log_backup_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ...) -> None: ...

class CloudBackupJobPreOrPostScript(_message.Message):
    __slots__ = ("linux_script", "windows_script")
    LINUX_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    linux_script: ScriptPathAndParams
    windows_script: ScriptPathAndParams
    def __init__(self, linux_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ..., windows_script: _Optional[_Union[ScriptPathAndParams, _Mapping]] = ...) -> None: ...

class StubbingPolicyProto(_message.Message):
    __slots__ = ("scheduling_policy", "retention_policy")
    SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    scheduling_policy: _policy_pb2.SchedulingPolicyProto
    retention_policy: _policy_pb2.RetentionPolicyProto
    def __init__(self, scheduling_policy: _Optional[_Union[_policy_pb2.SchedulingPolicyProto, _Mapping]] = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ...) -> None: ...

class BackupJobProto(_message.Message):
    __slots__ = ("type", "name", "description", "tag_vec", "job_id", "job_uid", "primary_job_uid", "remote_job_uids", "priority", "perform_source_side_dedup", "dedup_disabled_source_id_vec", "policy_id", "policy_applied_time_msecs", "policy_name", "start_time", "end_time_usecs", "pre_script", "post_snapshot_script", "post_backup_script", "cloud_pre_backup_script", "cloud_post_backup_script", "cloud_post_snapshot_script", "view_box_id", "backup_source_params", "parent_source", "eh_parent_source", "sources", "exclude_sources_DEPRECATED", "exclude_sources", "indexing_policy", "alerting_policy", "last_modification_time_usecs", "job_creation_time_usecs", "sla_time_mins", "full_backup_sla_time_mins", "log_backup_sla_time_mins", "deletion_status", "is_deleted", "last_updated_username", "ignorable_errors_in_error_db", "quiesce", "continue_on_quiesce_failure", "is_active", "is_paused", "last_pause_modification_time_usecs", "last_pause_reason", "is_rpo_job", "is_internal", "timezone", "abort_in_exclusion_window", "pause_in_blackout_window", "num_snapshots_to_keep_on_primary", "backup_qos_principal", "env_backup_params", "required_feature_vec", "truncate_logs", "leverage_storage_snapshots", "leverage_storage_snapshots_for_hyperflex", "leverage_san_transport", "leverage_nutanix_snapshots", "storage_array_snapshot", "dr_to_cloud_params", "user_info", "stubbing_policy", "remote_view_params", "remote_view_name", "create_remote_view", "is_direct_archive_enabled", "is_direct_archive_native_format_enabled", "source_filters", "is_continuous_snapshotting_enabled", "max_allowed_source_snapshots", "all_archival_snapshots_expired", "all_internal_replication_views_deleted", "is_cloud_archive_direct", "standby_resource_vec", "is_cdp_sync_replication_enabled", "skip_tenant_validations", "global_include_exclude", "object_backup_spec_uid", "is_source_paused_map", "allow_parallel_runs", "skip_rigel_for_backup", "data_transfer_info", "perform_brick_based_dedup", "task_timeout_vec", "last_start_time_modification_time_usecs", "config_vec", "job_policy", "full_backup_job_policy", "log_backup_job_policy", "exclusion_ranges")
    class DeletionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kValid: _ClassVar[BackupJobProto.DeletionStatus]
        kDeleteJob: _ClassVar[BackupJobProto.DeletionStatus]
        kDeleteJobAndBackups: _ClassVar[BackupJobProto.DeletionStatus]
    kValid: BackupJobProto.DeletionStatus
    kDeleteJob: BackupJobProto.DeletionStatus
    kDeleteJobAndBackups: BackupJobProto.DeletionStatus
    class BackupSource(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        def __init__(self, entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
    class ExcludeSource(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        def __init__(self, entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
    class DRToCloudParams(_message.Message):
        __slots__ = ("need_to_fail_over",)
        NEED_TO_FAIL_OVER_FIELD_NUMBER: _ClassVar[int]
        need_to_fail_over: bool
        def __init__(self, need_to_fail_over: bool = ...) -> None: ...
    class RemoteViewParams(_message.Message):
        __slots__ = ("remote_view_map",)
        class RemoteViewParamsPerView(_message.Message):
            __slots__ = ("use_same_name_as_source_view", "remote_view_name")
            USE_SAME_NAME_AS_SOURCE_VIEW_FIELD_NUMBER: _ClassVar[int]
            REMOTE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
            use_same_name_as_source_view: bool
            remote_view_name: str
            def __init__(self, use_same_name_as_source_view: bool = ..., remote_view_name: _Optional[str] = ...) -> None: ...
        class RemoteViewMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: BackupJobProto.RemoteViewParams.RemoteViewParamsPerView
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BackupJobProto.RemoteViewParams.RemoteViewParamsPerView, _Mapping]] = ...) -> None: ...
        REMOTE_VIEW_MAP_FIELD_NUMBER: _ClassVar[int]
        remote_view_map: _containers.MessageMap[int, BackupJobProto.RemoteViewParams.RemoteViewParamsPerView]
        def __init__(self, remote_view_map: _Optional[_Mapping[int, BackupJobProto.RemoteViewParams.RemoteViewParamsPerView]] = ...) -> None: ...
    class IsSourcePausedMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ExclusionTimeRange(_message.Message):
        __slots__ = ("day", "start_time", "end_time")
        DAY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        day: _enums_pb2.Day.Type
        start_time: _policy_pb2.Time
        end_time: _policy_pb2.Time
        def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., start_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ..., end_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PERFORM_SOURCE_SIDE_DEDUP_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DISABLED_SOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_APPLIED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SNAPSHOT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PRE_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_POST_BACKUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_POST_SNAPSHOT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EH_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOURCES_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALERTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    DELETION_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_USERNAME_FIELD_NUMBER: _ClassVar[int]
    IGNORABLE_ERRORS_IN_ERROR_DB_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_QUIESCE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSE_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSE_REASON_FIELD_NUMBER: _ClassVar[int]
    IS_RPO_JOB_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ABORT_IN_EXCLUSION_WINDOW_FIELD_NUMBER: _ClassVar[int]
    PAUSE_IN_BLACKOUT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAPSHOTS_TO_KEEP_ON_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ENV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_LOGS_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_STORAGE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_STORAGE_SNAPSHOTS_FOR_HYPERFLEX_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_NUTANIX_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DR_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    STUBBING_POLICY_FIELD_NUMBER: _ClassVar[int]
    REMOTE_VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_REMOTE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_NATIVE_FORMAT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    IS_CONTINUOUS_SNAPSHOTTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_SOURCE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    ALL_ARCHIVAL_SNAPSHOTS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    ALL_INTERNAL_REPLICATION_VIEWS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_ARCHIVE_DIRECT_FIELD_NUMBER: _ClassVar[int]
    STANDBY_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CDP_SYNC_REPLICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SKIP_TENANT_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INCLUDE_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_BACKUP_SPEC_UID_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_PAUSED_MAP_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PARALLEL_RUNS_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    PERFORM_BRICK_BASED_DEDUP_FIELD_NUMBER: _ClassVar[int]
    TASK_TIMEOUT_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_START_TIME_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_POLICY_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_JOB_POLICY_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_JOB_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_RANGES_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    name: str
    description: str
    tag_vec: _containers.RepeatedScalarFieldContainer[str]
    job_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    primary_job_uid: _universal_id_pb2.UniversalIdProto
    remote_job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    priority: Priority
    perform_source_side_dedup: bool
    dedup_disabled_source_id_vec: _containers.RepeatedScalarFieldContainer[int]
    policy_id: str
    policy_applied_time_msecs: int
    policy_name: str
    start_time: _policy_pb2.Time
    end_time_usecs: int
    pre_script: BackupJobPreOrPostScript
    post_snapshot_script: BackupJobPreOrPostScript
    post_backup_script: BackupJobPreOrPostScript
    cloud_pre_backup_script: CloudBackupJobPreOrPostScript
    cloud_post_backup_script: CloudBackupJobPreOrPostScript
    cloud_post_snapshot_script: CloudBackupJobPreOrPostScript
    view_box_id: int
    backup_source_params: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.BackupSourceParams]
    parent_source: _entity_pb2.EntityProto
    eh_parent_source: _entity_pb2.EntityProto
    sources: _containers.RepeatedCompositeFieldContainer[BackupJobProto.BackupSource]
    exclude_sources_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    exclude_sources: _containers.RepeatedCompositeFieldContainer[BackupJobProto.ExcludeSource]
    indexing_policy: _env_params_pb2.IndexingPolicyProto
    alerting_policy: _env_params_pb2.AlertingPolicyProto
    last_modification_time_usecs: int
    job_creation_time_usecs: int
    sla_time_mins: int
    full_backup_sla_time_mins: int
    log_backup_sla_time_mins: int
    deletion_status: BackupJobProto.DeletionStatus
    is_deleted: bool
    last_updated_username: str
    ignorable_errors_in_error_db: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    quiesce: bool
    continue_on_quiesce_failure: bool
    is_active: bool
    is_paused: bool
    last_pause_modification_time_usecs: int
    last_pause_reason: _enums_pb2.JobPauseReason.Type
    is_rpo_job: bool
    is_internal: bool
    timezone: str
    abort_in_exclusion_window: bool
    pause_in_blackout_window: bool
    num_snapshots_to_keep_on_primary: int
    backup_qos_principal: _enums_pb2.BackupQoSPrincipal.Type
    env_backup_params: _env_params_pb2.EnvBackupParams
    required_feature_vec: _containers.RepeatedScalarFieldContainer[str]
    truncate_logs: bool
    leverage_storage_snapshots: bool
    leverage_storage_snapshots_for_hyperflex: bool
    leverage_san_transport: bool
    leverage_nutanix_snapshots: bool
    storage_array_snapshot: bool
    dr_to_cloud_params: BackupJobProto.DRToCloudParams
    user_info: _permissions_pb2.UserInformation
    stubbing_policy: StubbingPolicyProto
    remote_view_params: BackupJobProto.RemoteViewParams
    remote_view_name: str
    create_remote_view: bool
    is_direct_archive_enabled: bool
    is_direct_archive_native_format_enabled: bool
    source_filters: SourceFilters
    is_continuous_snapshotting_enabled: bool
    max_allowed_source_snapshots: int
    all_archival_snapshots_expired: bool
    all_internal_replication_views_deleted: bool
    is_cloud_archive_direct: bool
    standby_resource_vec: _containers.RepeatedCompositeFieldContainer[StandbyResource]
    is_cdp_sync_replication_enabled: bool
    skip_tenant_validations: bool
    global_include_exclude: _env_params_pb2.PhysicalFileBackupParams.GlobalIncludeExclude
    object_backup_spec_uid: _universal_id_pb2.UniversalIdProto
    is_source_paused_map: _containers.ScalarMap[int, bool]
    allow_parallel_runs: bool
    skip_rigel_for_backup: bool
    data_transfer_info: _env_params_pb2.DataTransferInfo
    perform_brick_based_dedup: bool
    task_timeout_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.CancellationTimeout]
    last_start_time_modification_time_usecs: int
    config_vec: _containers.RepeatedCompositeFieldContainer[ConfigurationParams]
    job_policy: JobPolicyProto
    full_backup_job_policy: JobPolicyProto
    log_backup_job_policy: JobPolicyProto
    exclusion_ranges: _containers.RepeatedCompositeFieldContainer[BackupJobProto.ExclusionTimeRange]
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tag_vec: _Optional[_Iterable[str]] = ..., job_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., primary_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., remote_job_uids: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., priority: _Optional[_Union[Priority, str]] = ..., perform_source_side_dedup: bool = ..., dedup_disabled_source_id_vec: _Optional[_Iterable[int]] = ..., policy_id: _Optional[str] = ..., policy_applied_time_msecs: _Optional[int] = ..., policy_name: _Optional[str] = ..., start_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ..., end_time_usecs: _Optional[int] = ..., pre_script: _Optional[_Union[BackupJobPreOrPostScript, _Mapping]] = ..., post_snapshot_script: _Optional[_Union[BackupJobPreOrPostScript, _Mapping]] = ..., post_backup_script: _Optional[_Union[BackupJobPreOrPostScript, _Mapping]] = ..., cloud_pre_backup_script: _Optional[_Union[CloudBackupJobPreOrPostScript, _Mapping]] = ..., cloud_post_backup_script: _Optional[_Union[CloudBackupJobPreOrPostScript, _Mapping]] = ..., cloud_post_snapshot_script: _Optional[_Union[CloudBackupJobPreOrPostScript, _Mapping]] = ..., view_box_id: _Optional[int] = ..., backup_source_params: _Optional[_Iterable[_Union[_env_params_pb2.BackupSourceParams, _Mapping]]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., eh_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., sources: _Optional[_Iterable[_Union[BackupJobProto.BackupSource, _Mapping]]] = ..., exclude_sources_DEPRECATED: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., exclude_sources: _Optional[_Iterable[_Union[BackupJobProto.ExcludeSource, _Mapping]]] = ..., indexing_policy: _Optional[_Union[_env_params_pb2.IndexingPolicyProto, _Mapping]] = ..., alerting_policy: _Optional[_Union[_env_params_pb2.AlertingPolicyProto, _Mapping]] = ..., last_modification_time_usecs: _Optional[int] = ..., job_creation_time_usecs: _Optional[int] = ..., sla_time_mins: _Optional[int] = ..., full_backup_sla_time_mins: _Optional[int] = ..., log_backup_sla_time_mins: _Optional[int] = ..., deletion_status: _Optional[_Union[BackupJobProto.DeletionStatus, str]] = ..., is_deleted: bool = ..., last_updated_username: _Optional[str] = ..., ignorable_errors_in_error_db: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., quiesce: bool = ..., continue_on_quiesce_failure: bool = ..., is_active: bool = ..., is_paused: bool = ..., last_pause_modification_time_usecs: _Optional[int] = ..., last_pause_reason: _Optional[_Union[_enums_pb2.JobPauseReason.Type, str]] = ..., is_rpo_job: bool = ..., is_internal: bool = ..., timezone: _Optional[str] = ..., abort_in_exclusion_window: bool = ..., pause_in_blackout_window: bool = ..., num_snapshots_to_keep_on_primary: _Optional[int] = ..., backup_qos_principal: _Optional[_Union[_enums_pb2.BackupQoSPrincipal.Type, str]] = ..., env_backup_params: _Optional[_Union[_env_params_pb2.EnvBackupParams, _Mapping]] = ..., required_feature_vec: _Optional[_Iterable[str]] = ..., truncate_logs: bool = ..., leverage_storage_snapshots: bool = ..., leverage_storage_snapshots_for_hyperflex: bool = ..., leverage_san_transport: bool = ..., leverage_nutanix_snapshots: bool = ..., storage_array_snapshot: bool = ..., dr_to_cloud_params: _Optional[_Union[BackupJobProto.DRToCloudParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., stubbing_policy: _Optional[_Union[StubbingPolicyProto, _Mapping]] = ..., remote_view_params: _Optional[_Union[BackupJobProto.RemoteViewParams, _Mapping]] = ..., remote_view_name: _Optional[str] = ..., create_remote_view: bool = ..., is_direct_archive_enabled: bool = ..., is_direct_archive_native_format_enabled: bool = ..., source_filters: _Optional[_Union[SourceFilters, _Mapping]] = ..., is_continuous_snapshotting_enabled: bool = ..., max_allowed_source_snapshots: _Optional[int] = ..., all_archival_snapshots_expired: bool = ..., all_internal_replication_views_deleted: bool = ..., is_cloud_archive_direct: bool = ..., standby_resource_vec: _Optional[_Iterable[_Union[StandbyResource, _Mapping]]] = ..., is_cdp_sync_replication_enabled: bool = ..., skip_tenant_validations: bool = ..., global_include_exclude: _Optional[_Union[_env_params_pb2.PhysicalFileBackupParams.GlobalIncludeExclude, _Mapping]] = ..., object_backup_spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_source_paused_map: _Optional[_Mapping[int, bool]] = ..., allow_parallel_runs: bool = ..., skip_rigel_for_backup: bool = ..., data_transfer_info: _Optional[_Union[_env_params_pb2.DataTransferInfo, _Mapping]] = ..., perform_brick_based_dedup: bool = ..., task_timeout_vec: _Optional[_Iterable[_Union[_policy_pb2.CancellationTimeout, _Mapping]]] = ..., last_start_time_modification_time_usecs: _Optional[int] = ..., config_vec: _Optional[_Iterable[_Union[ConfigurationParams, _Mapping]]] = ..., job_policy: _Optional[_Union[JobPolicyProto, _Mapping]] = ..., full_backup_job_policy: _Optional[_Union[JobPolicyProto, _Mapping]] = ..., log_backup_job_policy: _Optional[_Union[JobPolicyProto, _Mapping]] = ..., exclusion_ranges: _Optional[_Iterable[_Union[BackupJobProto.ExclusionTimeRange, _Mapping]]] = ...) -> None: ...

class EntityUpgradeStatus(_message.Message):
    __slots__ = ("previous_agent_sw_version_str", "upgrade_status", "error", "start_time", "end_time", "display_name")
    class UpgradeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kStarted: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kSuccessful: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kFailed: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kCancelled: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kSkipped: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
        kNoAutoUpgrade: _ClassVar[EntityUpgradeStatus.UpgradeStatus]
    kNotStarted: EntityUpgradeStatus.UpgradeStatus
    kStarted: EntityUpgradeStatus.UpgradeStatus
    kSuccessful: EntityUpgradeStatus.UpgradeStatus
    kFailed: EntityUpgradeStatus.UpgradeStatus
    kCancelled: EntityUpgradeStatus.UpgradeStatus
    kSkipped: EntityUpgradeStatus.UpgradeStatus
    kNoAutoUpgrade: EntityUpgradeStatus.UpgradeStatus
    PREVIOUS_AGENT_SW_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    previous_agent_sw_version_str: str
    upgrade_status: EntityUpgradeStatus.UpgradeStatus
    error: _error_pb2.ErrorProto
    start_time: int
    end_time: int
    display_name: str
    def __init__(self, previous_agent_sw_version_str: _Optional[str] = ..., upgrade_status: _Optional[_Union[EntityUpgradeStatus.UpgradeStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., display_name: _Optional[str] = ...) -> None: ...

class ScheduleInfo(_message.Message):
    __slots__ = ("schedule_time_usecs", "schedule_end_time_usecs")
    SCHEDULE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    schedule_time_usecs: int
    schedule_end_time_usecs: int
    def __init__(self, schedule_time_usecs: _Optional[int] = ..., schedule_end_time_usecs: _Optional[int] = ...) -> None: ...

class UpgradeTaskStateProto(_message.Message):
    __slots__ = ("name", "description", "id", "start_time", "end_time", "status", "current_batch_entity_id_vec", "cluster_version", "entity_upgrade_status_map", "is_selective_upgrade", "schedule_info", "retryable", "original_task_id", "upgrade_now", "error", "user_info", "progress_monitor_task_path")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[UpgradeTaskStateProto.Status]
        kRunning: _ClassVar[UpgradeTaskStateProto.Status]
        kFinished: _ClassVar[UpgradeTaskStateProto.Status]
        kSuccessful: _ClassVar[UpgradeTaskStateProto.Status]
        kFailed: _ClassVar[UpgradeTaskStateProto.Status]
        kPartialFailure: _ClassVar[UpgradeTaskStateProto.Status]
        kCancelled: _ClassVar[UpgradeTaskStateProto.Status]
    kNotStarted: UpgradeTaskStateProto.Status
    kRunning: UpgradeTaskStateProto.Status
    kFinished: UpgradeTaskStateProto.Status
    kSuccessful: UpgradeTaskStateProto.Status
    kFailed: UpgradeTaskStateProto.Status
    kPartialFailure: UpgradeTaskStateProto.Status
    kCancelled: UpgradeTaskStateProto.Status
    class EntityUpgradeStatusMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EntityUpgradeStatus
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EntityUpgradeStatus, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BATCH_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UPGRADE_STATUS_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTIVE_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_INFO_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_NOW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    id: int
    start_time: int
    end_time: int
    status: UpgradeTaskStateProto.Status
    current_batch_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    cluster_version: str
    entity_upgrade_status_map: _containers.MessageMap[int, EntityUpgradeStatus]
    is_selective_upgrade: bool
    schedule_info: ScheduleInfo
    retryable: bool
    original_task_id: int
    upgrade_now: bool
    error: _error_pb2.ErrorProto
    user_info: _permissions_pb2.UserInformation
    progress_monitor_task_path: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., id: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., status: _Optional[_Union[UpgradeTaskStateProto.Status, str]] = ..., current_batch_entity_id_vec: _Optional[_Iterable[int]] = ..., cluster_version: _Optional[str] = ..., entity_upgrade_status_map: _Optional[_Mapping[int, EntityUpgradeStatus]] = ..., is_selective_upgrade: bool = ..., schedule_info: _Optional[_Union[ScheduleInfo, _Mapping]] = ..., retryable: bool = ..., original_task_id: _Optional[int] = ..., upgrade_now: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ...) -> None: ...

class AgentConfigScribeStateProto(_message.Message):
    __slots__ = ("type", "data", "is_compressed", "config_format")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kConfigData: _ClassVar[AgentConfigScribeStateProto.Type]
    kConfigData: AgentConfigScribeStateProto.Type
    class ConfigFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kJson: _ClassVar[AgentConfigScribeStateProto.ConfigFileFormat]
        kLinuxConfigFile: _ClassVar[AgentConfigScribeStateProto.ConfigFileFormat]
    kJson: AgentConfigScribeStateProto.ConfigFileFormat
    kLinuxConfigFile: AgentConfigScribeStateProto.ConfigFileFormat
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    type: AgentConfigScribeStateProto.Type
    data: bytes
    is_compressed: bool
    config_format: AgentConfigScribeStateProto.ConfigFileFormat
    def __init__(self, type: _Optional[_Union[AgentConfigScribeStateProto.Type, str]] = ..., data: _Optional[bytes] = ..., is_compressed: bool = ..., config_format: _Optional[_Union[AgentConfigScribeStateProto.ConfigFileFormat, str]] = ...) -> None: ...

class RenameObjectParamProto(_message.Message):
    __slots__ = ("prefix", "suffix")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    suffix: str
    def __init__(self, prefix: _Optional[str] = ..., suffix: _Optional[str] = ...) -> None: ...

class RestoreAcropolisVMParam(_message.Message):
    __slots__ = ("base_cbt_snapshot_info_proto", "network_config")
    class NetworkConfigInfo(_message.Message):
        __slots__ = ("network_state_change", "nic_vec")
        class NetworkStateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kKeepOriginal: _ClassVar[RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange]
            kAttachNewNetwork: _ClassVar[RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange]
            kRemoveNetwork: _ClassVar[RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange]
        kKeepOriginal: RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange
        kAttachNewNetwork: RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange
        kRemoveNetwork: RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange
        class NICSpec(_message.Message):
            __slots__ = ("network_uuid", "ip_address")
            NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            network_uuid: str
            ip_address: str
            def __init__(self, network_uuid: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...
        NETWORK_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        NIC_VEC_FIELD_NUMBER: _ClassVar[int]
        network_state_change: RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange
        nic_vec: _containers.RepeatedCompositeFieldContainer[RestoreAcropolisVMParam.NetworkConfigInfo.NICSpec]
        def __init__(self, network_state_change: _Optional[_Union[RestoreAcropolisVMParam.NetworkConfigInfo.NetworkStateChange, str]] = ..., nic_vec: _Optional[_Iterable[_Union[RestoreAcropolisVMParam.NetworkConfigInfo.NICSpec, _Mapping]]] = ...) -> None: ...
    BASE_CBT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base_cbt_snapshot_info_proto: SnapshotInfoProto
    network_config: RestoreAcropolisVMParam.NetworkConfigInfo
    def __init__(self, base_cbt_snapshot_info_proto: _Optional[_Union[SnapshotInfoProto, _Mapping]] = ..., network_config: _Optional[_Union[RestoreAcropolisVMParam.NetworkConfigInfo, _Mapping]] = ...) -> None: ...

class RestoreKVMVMParam(_message.Message):
    __slots__ = ("base_cbt_snapshot_info_proto", "network_config")
    class NetworkConfigInfo(_message.Message):
        __slots__ = ("network_state_change", "nic_vec")
        class NetworkStateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kKeepOriginal: _ClassVar[RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange]
            kAttachNewNetwork: _ClassVar[RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange]
            kRemoveNetwork: _ClassVar[RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange]
        kKeepOriginal: RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange
        kAttachNewNetwork: RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange
        kRemoveNetwork: RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange
        class NICSpec(_message.Message):
            __slots__ = ("network_uuid", "ip_address", "vnic_id")
            NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            VNIC_ID_FIELD_NUMBER: _ClassVar[int]
            network_uuid: str
            ip_address: str
            vnic_id: str
            def __init__(self, network_uuid: _Optional[str] = ..., ip_address: _Optional[str] = ..., vnic_id: _Optional[str] = ...) -> None: ...
        NETWORK_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        NIC_VEC_FIELD_NUMBER: _ClassVar[int]
        network_state_change: RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange
        nic_vec: _containers.RepeatedCompositeFieldContainer[RestoreKVMVMParam.NetworkConfigInfo.NICSpec]
        def __init__(self, network_state_change: _Optional[_Union[RestoreKVMVMParam.NetworkConfigInfo.NetworkStateChange, str]] = ..., nic_vec: _Optional[_Iterable[_Union[RestoreKVMVMParam.NetworkConfigInfo.NICSpec, _Mapping]]] = ...) -> None: ...
    BASE_CBT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base_cbt_snapshot_info_proto: SnapshotInfoProto
    network_config: RestoreKVMVMParam.NetworkConfigInfo
    def __init__(self, base_cbt_snapshot_info_proto: _Optional[_Union[SnapshotInfoProto, _Mapping]] = ..., network_config: _Optional[_Union[RestoreKVMVMParam.NetworkConfigInfo, _Mapping]] = ...) -> None: ...

class RestoreVappInfo(_message.Message):
    __slots__ = ("vapp_id", "vapp_name")
    VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    vapp_id: str
    vapp_name: str
    def __init__(self, vapp_id: _Optional[str] = ..., vapp_name: _Optional[str] = ...) -> None: ...

class RestoreObject(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "start_time_usecs", "point_in_time_restore_time_usecs", "hydration_time_usecs", "entity", "archival_target", "cloud_deploy_target", "cloud_replication_target", "recover_from_standby", "parent_source", "attempt_num", "snapshot_relative_dir_path", "vm_had_independent_disks", "view_name", "restore_acropolis_vm_param", "nosql_recover_params", "uda_recover_params", "sfdc_recover_params", "restore_vapp_info", "backup_type", "restore_exchange_params", "pit_preferred_archival_target", "san_recover_params", "config_vec", "one_drive_restore_entity_params", "restore_azure_sql_params", "restore_rds_postgres_params", "job_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_RESTORE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_TARGET_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    RECOVER_FROM_STANDBY_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    VM_HAD_INDEPENDENT_DISKS_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ACROPOLIS_VM_PARAM_FIELD_NUMBER: _ClassVar[int]
    NOSQL_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_EXCHANGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PIT_PREFERRED_ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    SAN_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_RESTORE_ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_AZURE_SQL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RDS_POSTGRES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    start_time_usecs: int
    point_in_time_restore_time_usecs: int
    hydration_time_usecs: int
    entity: _entity_pb2.EntityProto
    archival_target: _policy_pb2.ArchivalTarget
    cloud_deploy_target: _policy_pb2.CloudDeployTarget
    cloud_replication_target: _policy_pb2.CloudDeployTarget
    recover_from_standby: bool
    parent_source: _entity_pb2.EntityProto
    attempt_num: int
    snapshot_relative_dir_path: str
    vm_had_independent_disks: bool
    view_name: str
    restore_acropolis_vm_param: RestoreAcropolisVMParam
    nosql_recover_params: NoSqlRecoverParams
    uda_recover_params: UdaRecoverParams
    sfdc_recover_params: SfdcRecoverParams
    restore_vapp_info: RestoreVappInfo
    backup_type: _enums_pb2.ScheduledBackupType.Type
    restore_exchange_params: RestoreExchangeParams
    pit_preferred_archival_target: _policy_pb2.ArchivalTarget
    san_recover_params: SANRecoverParams
    config_vec: _containers.RepeatedCompositeFieldContainer[ConfigurationParams]
    one_drive_restore_entity_params: O365OneDriveRestoreEntityParams
    restore_azure_sql_params: _azure_sql_pb2.RestoreAzureSQLParams
    restore_rds_postgres_params: _aws_rds_pb2.RestoreRDSPostgresParams
    job_id: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., point_in_time_restore_time_usecs: _Optional[int] = ..., hydration_time_usecs: _Optional[int] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., archival_target: _Optional[_Union[_policy_pb2.ArchivalTarget, _Mapping]] = ..., cloud_deploy_target: _Optional[_Union[_policy_pb2.CloudDeployTarget, _Mapping]] = ..., cloud_replication_target: _Optional[_Union[_policy_pb2.CloudDeployTarget, _Mapping]] = ..., recover_from_standby: bool = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., attempt_num: _Optional[int] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_had_independent_disks: bool = ..., view_name: _Optional[str] = ..., restore_acropolis_vm_param: _Optional[_Union[RestoreAcropolisVMParam, _Mapping]] = ..., nosql_recover_params: _Optional[_Union[NoSqlRecoverParams, _Mapping]] = ..., uda_recover_params: _Optional[_Union[UdaRecoverParams, _Mapping]] = ..., sfdc_recover_params: _Optional[_Union[SfdcRecoverParams, _Mapping]] = ..., restore_vapp_info: _Optional[_Union[RestoreVappInfo, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., restore_exchange_params: _Optional[_Union[RestoreExchangeParams, _Mapping]] = ..., pit_preferred_archival_target: _Optional[_Union[_policy_pb2.ArchivalTarget, _Mapping]] = ..., san_recover_params: _Optional[_Union[SANRecoverParams, _Mapping]] = ..., config_vec: _Optional[_Iterable[_Union[ConfigurationParams, _Mapping]]] = ..., one_drive_restore_entity_params: _Optional[_Union[O365OneDriveRestoreEntityParams, _Mapping]] = ..., restore_azure_sql_params: _Optional[_Union[_azure_sql_pb2.RestoreAzureSQLParams, _Mapping]] = ..., restore_rds_postgres_params: _Optional[_Union[_aws_rds_pb2.RestoreRDSPostgresParams, _Mapping]] = ..., job_id: _Optional[int] = ...) -> None: ...

class VMOrgVDCNetwork(_message.Message):
    __slots__ = ("network_name", "is_connected", "network_adapter_type", "ip_address_allocation_mode", "network_connection_index", "mac_address", "ip_address", "external_ip_address")
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_ALLOCATION_MODE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONNECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    network_name: str
    is_connected: bool
    network_adapter_type: str
    ip_address_allocation_mode: str
    network_connection_index: int
    mac_address: str
    ip_address: _common_pb2.IPAddress
    external_ip_address: _common_pb2.IPAddress
    def __init__(self, network_name: _Optional[str] = ..., is_connected: bool = ..., network_adapter_type: _Optional[str] = ..., ip_address_allocation_mode: _Optional[str] = ..., network_connection_index: _Optional[int] = ..., mac_address: _Optional[str] = ..., ip_address: _Optional[_Union[_common_pb2.IPAddress, _Mapping]] = ..., external_ip_address: _Optional[_Union[_common_pb2.IPAddress, _Mapping]] = ...) -> None: ...

class RestoreType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRecoverVMs: _ClassVar[RestoreType.Type]
        kCloneVMs: _ClassVar[RestoreType.Type]
        kRestoreFiles: _ClassVar[RestoreType.Type]
        kRecoverApp: _ClassVar[RestoreType.Type]
        kCloneApp: _ClassVar[RestoreType.Type]
        kCloneView: _ClassVar[RestoreType.Type]
        kMountVolumes: _ClassVar[RestoreType.Type]
        kRecoverSanVolume: _ClassVar[RestoreType.Type]
        kConvertAndDeployVMs: _ClassVar[RestoreType.Type]
        kMountFileVolume: _ClassVar[RestoreType.Type]
        kSystem: _ClassVar[RestoreType.Type]
        kRecoverVolumes: _ClassVar[RestoreType.Type]
        kDeployVMs: _ClassVar[RestoreType.Type]
        kDownloadFiles: _ClassVar[RestoreType.Type]
        kRecoverEmails: _ClassVar[RestoreType.Type]
        kRecoverDisks: _ClassVar[RestoreType.Type]
        kCloneRefreshApp: _ClassVar[RestoreType.Type]
        kCloneAppView: _ClassVar[RestoreType.Type]
        kRecoverNamespaces: _ClassVar[RestoreType.Type]
        kRecoverO365Drive: _ClassVar[RestoreType.Type]
        kCloneVMsToView: _ClassVar[RestoreType.Type]
        kRecoverNoSql: _ClassVar[RestoreType.Type]
        kRecoverSites: _ClassVar[RestoreType.Type]
        kRecoverO365PublicFolders: _ClassVar[RestoreType.Type]
        kConvertToPst: _ClassVar[RestoreType.Type]
        kRecoverUda: _ClassVar[RestoreType.Type]
        kRecoverO365Teams: _ClassVar[RestoreType.Type]
        kRecoverO365Groups: _ClassVar[RestoreType.Type]
        kLogApply: _ClassVar[RestoreType.Type]
        kReHydrateVMs: _ClassVar[RestoreType.Type]
        kUptiering: _ClassVar[RestoreType.Type]
        kRecoverRDS: _ClassVar[RestoreType.Type]
        kRecoverAurora: _ClassVar[RestoreType.Type]
        kRecoverSfdc: _ClassVar[RestoreType.Type]
        kCloneProtectionJobView: _ClassVar[RestoreType.Type]
        kRecoverExchangeDbs: _ClassVar[RestoreType.Type]
        kRecoverS3Buckets: _ClassVar[RestoreType.Type]
        kRecoverS3Objects: _ClassVar[RestoreType.Type]
        kRecoverSanGroup: _ClassVar[RestoreType.Type]
        kRecoverAzureSQL: _ClassVar[RestoreType.Type]
        kDownloadChats: _ClassVar[RestoreType.Type]
        kRecoverRDSPostgres: _ClassVar[RestoreType.Type]
    kRecoverVMs: RestoreType.Type
    kCloneVMs: RestoreType.Type
    kRestoreFiles: RestoreType.Type
    kRecoverApp: RestoreType.Type
    kCloneApp: RestoreType.Type
    kCloneView: RestoreType.Type
    kMountVolumes: RestoreType.Type
    kRecoverSanVolume: RestoreType.Type
    kConvertAndDeployVMs: RestoreType.Type
    kMountFileVolume: RestoreType.Type
    kSystem: RestoreType.Type
    kRecoverVolumes: RestoreType.Type
    kDeployVMs: RestoreType.Type
    kDownloadFiles: RestoreType.Type
    kRecoverEmails: RestoreType.Type
    kRecoverDisks: RestoreType.Type
    kCloneRefreshApp: RestoreType.Type
    kCloneAppView: RestoreType.Type
    kRecoverNamespaces: RestoreType.Type
    kRecoverO365Drive: RestoreType.Type
    kCloneVMsToView: RestoreType.Type
    kRecoverNoSql: RestoreType.Type
    kRecoverSites: RestoreType.Type
    kRecoverO365PublicFolders: RestoreType.Type
    kConvertToPst: RestoreType.Type
    kRecoverUda: RestoreType.Type
    kRecoverO365Teams: RestoreType.Type
    kRecoverO365Groups: RestoreType.Type
    kLogApply: RestoreType.Type
    kReHydrateVMs: RestoreType.Type
    kUptiering: RestoreType.Type
    kRecoverRDS: RestoreType.Type
    kRecoverAurora: RestoreType.Type
    kRecoverSfdc: RestoreType.Type
    kCloneProtectionJobView: RestoreType.Type
    kRecoverExchangeDbs: RestoreType.Type
    kRecoverS3Buckets: RestoreType.Type
    kRecoverS3Objects: RestoreType.Type
    kRecoverSanGroup: RestoreType.Type
    kRecoverAzureSQL: RestoreType.Type
    kDownloadChats: RestoreType.Type
    kRecoverRDSPostgres: RestoreType.Type
    def __init__(self) -> None: ...

class NetworkMappingProto(_message.Message):
    __slots__ = ("source_network_entity", "target_network_entity", "disable_network", "preserve_mac_address_on_new_network")
    SOURCE_NETWORK_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_NETWORK_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_MAC_ADDRESS_ON_NEW_NETWORK_FIELD_NUMBER: _ClassVar[int]
    source_network_entity: _entity_pb2.EntityProto
    target_network_entity: _entity_pb2.EntityProto
    disable_network: bool
    preserve_mac_address_on_new_network: bool
    def __init__(self, source_network_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_network_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., disable_network: bool = ..., preserve_mac_address_on_new_network: bool = ...) -> None: ...

class RestoredObjectNetworkConfigProto(_message.Message):
    __slots__ = ("detach_network", "mappings", "disable_network", "network_entity", "vnic_entity", "preserve_mac_address_on_new_network", "vcd_network")
    DETACH_NETWORK_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VNIC_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_MAC_ADDRESS_ON_NEW_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VCD_NETWORK_FIELD_NUMBER: _ClassVar[int]
    detach_network: bool
    mappings: _containers.RepeatedCompositeFieldContainer[NetworkMappingProto]
    disable_network: bool
    network_entity: _entity_pb2.EntityProto
    vnic_entity: _entity_pb2.EntityProto
    preserve_mac_address_on_new_network: bool
    vcd_network: _common_pb2.OrgVDCNetwork
    def __init__(self, detach_network: bool = ..., mappings: _Optional[_Iterable[_Union[NetworkMappingProto, _Mapping]]] = ..., disable_network: bool = ..., network_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., vnic_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., preserve_mac_address_on_new_network: bool = ..., vcd_network: _Optional[_Union[_common_pb2.OrgVDCNetwork, _Mapping]] = ...) -> None: ...

class PowerStateConfigProto(_message.Message):
    __slots__ = ("power_on",)
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    power_on: bool
    def __init__(self, power_on: bool = ...) -> None: ...

class UuidConfigProto(_message.Message):
    __slots__ = ("preserve_uuid",)
    PRESERVE_UUID_FIELD_NUMBER: _ClassVar[int]
    preserve_uuid: bool
    def __init__(self, preserve_uuid: bool = ...) -> None: ...

class RestoreObjectParams(_message.Message):
    __slots__ = ("action", "restore_parent_source", "rename_restored_object_param", "resource_pool_entity", "restored_objects_network_config", "power_state_config", "datastore_entity", "view_name")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    action: RestoreType.Type
    restore_parent_source: _entity_pb2.EntityProto
    rename_restored_object_param: RenameObjectParamProto
    resource_pool_entity: _entity_pb2.EntityProto
    restored_objects_network_config: RestoredObjectNetworkConfigProto
    power_state_config: PowerStateConfigProto
    datastore_entity: _entity_pb2.EntityProto
    view_name: str
    def __init__(self, action: _Optional[_Union[RestoreType.Type, str]] = ..., restore_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., rename_restored_object_param: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ..., datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., view_name: _Optional[str] = ...) -> None: ...

class RestoreAppObject(_message.Message):
    __slots__ = ("app_entity", "restore_params", "display_name", "additional_params", "task_node_uid", "entity_node_uid")
    APP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TASK_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    app_entity: _entity_pb2.EntityProto
    restore_params: RestoreAppObjectParams
    display_name: str
    additional_params: RestoreTaskAdditionalParams
    task_node_uid: _universal_id_pb2.UniversalIdProto
    entity_node_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, app_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_params: _Optional[_Union[RestoreAppObjectParams, _Mapping]] = ..., display_name: _Optional[str] = ..., additional_params: _Optional[_Union[RestoreTaskAdditionalParams, _Mapping]] = ..., task_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class RestoreAppObjectParams(_message.Message):
    __slots__ = ("sql_restore_params", "oracle_restore_params", "ad_restore_params", "exchange_restore_params", "target_host", "clone_task_id", "target_host_parent_source")
    SQL_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AD_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_FIELD_NUMBER: _ClassVar[int]
    CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    sql_restore_params: RestoreSqlAppObjectParams
    oracle_restore_params: RestoreOracleAppObjectParams
    ad_restore_params: RestoreADAppObjectParams
    exchange_restore_params: RestoreExchangeParams
    target_host: _entity_pb2.EntityProto
    clone_task_id: int
    target_host_parent_source: _entity_pb2.EntityProto
    def __init__(self, sql_restore_params: _Optional[_Union[RestoreSqlAppObjectParams, _Mapping]] = ..., oracle_restore_params: _Optional[_Union[RestoreOracleAppObjectParams, _Mapping]] = ..., ad_restore_params: _Optional[_Union[RestoreADAppObjectParams, _Mapping]] = ..., exchange_restore_params: _Optional[_Union[RestoreExchangeParams, _Mapping]] = ..., target_host: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., clone_task_id: _Optional[int] = ..., target_host_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class CloneAppViewParams(_message.Message):
    __slots__ = ("mount_path_identifier", "read_only_view_expose")
    MOUNT_PATH_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_VIEW_EXPOSE_FIELD_NUMBER: _ClassVar[int]
    mount_path_identifier: str
    read_only_view_expose: bool
    def __init__(self, mount_path_identifier: _Optional[str] = ..., read_only_view_expose: bool = ...) -> None: ...

class CloneAppViewInfoOracle(_message.Message):
    __slots__ = ("mount_path_info_vec",)
    MOUNT_PATH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    mount_path_info_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mount_path_info_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CloneAppViewInfoProto(_message.Message):
    __slots__ = ("oracle_app_view_restore_info",)
    ORACLE_APP_VIEW_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_app_view_restore_info: CloneAppViewInfoOracle
    def __init__(self, oracle_app_view_restore_info: _Optional[_Union[CloneAppViewInfoOracle, _Mapping]] = ...) -> None: ...

class MigrateOracleCloneParams(_message.Message):
    __slots__ = ("delay_secs", "target_path_vec")
    DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    delay_secs: int
    target_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, delay_secs: _Optional[int] = ..., target_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class OracleUpdateRestoreTaskOptions(_message.Message):
    __slots__ = ("migrate_clone_params",)
    MIGRATE_CLONE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    migrate_clone_params: MigrateOracleCloneParams
    def __init__(self, migrate_clone_params: _Optional[_Union[MigrateOracleCloneParams, _Mapping]] = ...) -> None: ...

class SqlMultiStageRestoreAction(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[SqlMultiStageRestoreAction.Type]
        kCreate: _ClassVar[SqlMultiStageRestoreAction.Type]
        kUpdate: _ClassVar[SqlMultiStageRestoreAction.Type]
        kFinalize: _ClassVar[SqlMultiStageRestoreAction.Type]
    kNone: SqlMultiStageRestoreAction.Type
    kCreate: SqlMultiStageRestoreAction.Type
    kUpdate: SqlMultiStageRestoreAction.Type
    kFinalize: SqlMultiStageRestoreAction.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SqlMultiStageRestoreAction.Type
    def __init__(self, type: _Optional[_Union[SqlMultiStageRestoreAction.Type, str]] = ...) -> None: ...

class SqlUpdateRestoreTaskOptions(_message.Message):
    __slots__ = ("multi_stage_restore_action", "enable_auto_sync")
    MULTI_STAGE_RESTORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTO_SYNC_FIELD_NUMBER: _ClassVar[int]
    multi_stage_restore_action: SqlMultiStageRestoreAction.Type
    enable_auto_sync: bool
    def __init__(self, multi_stage_restore_action: _Optional[_Union[SqlMultiStageRestoreAction.Type, str]] = ..., enable_auto_sync: bool = ...) -> None: ...

class RestoreSqlAppObjectParams(_message.Message):
    __slots__ = ("restore_time_secs", "capture_tail_logs", "instance_name", "data_file_destination", "log_file_destination", "secondary_data_file_destination", "secondary_data_file_destination_vec", "new_database_name", "with_no_recovery", "db_restore_overwrite_policy", "is_multi_stage_restore", "is_auto_sync_enabled", "multi_stage_restore_options", "keep_cdc", "enable_checksum", "continue_after_error", "with_clause", "resume_restore", "replay_entire_last_log")
    RESTORE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_TAIL_LOGS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_DATA_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_DATA_FILE_DESTINATION_VEC_FIELD_NUMBER: _ClassVar[int]
    NEW_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    WITH_NO_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    DB_RESTORE_OVERWRITE_POLICY_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_STAGE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_SYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    RESUME_RESTORE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_ENTIRE_LAST_LOG_FIELD_NUMBER: _ClassVar[int]
    restore_time_secs: int
    capture_tail_logs: bool
    instance_name: str
    data_file_destination: str
    log_file_destination: str
    secondary_data_file_destination: str
    secondary_data_file_destination_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.FilesToDirectoryMapping]
    new_database_name: str
    with_no_recovery: bool
    db_restore_overwrite_policy: _sql_pb2.DBRestoreOverwritePolicy.Type
    is_multi_stage_restore: bool
    is_auto_sync_enabled: bool
    multi_stage_restore_options: SqlUpdateRestoreTaskOptions
    keep_cdc: bool
    enable_checksum: bool
    continue_after_error: bool
    with_clause: str
    resume_restore: bool
    replay_entire_last_log: bool
    def __init__(self, restore_time_secs: _Optional[int] = ..., capture_tail_logs: bool = ..., instance_name: _Optional[str] = ..., data_file_destination: _Optional[str] = ..., log_file_destination: _Optional[str] = ..., secondary_data_file_destination: _Optional[str] = ..., secondary_data_file_destination_vec: _Optional[_Iterable[_Union[_common_pb2.FilesToDirectoryMapping, _Mapping]]] = ..., new_database_name: _Optional[str] = ..., with_no_recovery: bool = ..., db_restore_overwrite_policy: _Optional[_Union[_sql_pb2.DBRestoreOverwritePolicy.Type, str]] = ..., is_multi_stage_restore: bool = ..., is_auto_sync_enabled: bool = ..., multi_stage_restore_options: _Optional[_Union[SqlUpdateRestoreTaskOptions, _Mapping]] = ..., keep_cdc: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., with_clause: _Optional[str] = ..., resume_restore: bool = ..., replay_entire_last_log: bool = ...) -> None: ...

class OracleDBConfig(_message.Message):
    __slots__ = ("num_tempfiles", "bct_file_path", "control_file_path_vec", "redo_log_conf", "audit_log_dest", "diag_dest", "fra_dest", "fra_size_mb", "db_config_file_path", "enable_archive_log_mode", "sga_target_size", "shared_pool_size", "pfile_parameter_map")
    class RedoLogGroupConf(_message.Message):
        __slots__ = ("num_groups", "group_member_vec", "member_prefix", "size_mb")
        NUM_GROUPS_FIELD_NUMBER: _ClassVar[int]
        GROUP_MEMBER_VEC_FIELD_NUMBER: _ClassVar[int]
        MEMBER_PREFIX_FIELD_NUMBER: _ClassVar[int]
        SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        num_groups: int
        group_member_vec: _containers.RepeatedScalarFieldContainer[str]
        member_prefix: str
        size_mb: int
        def __init__(self, num_groups: _Optional[int] = ..., group_member_vec: _Optional[_Iterable[str]] = ..., member_prefix: _Optional[str] = ..., size_mb: _Optional[int] = ...) -> None: ...
    class PfileParameterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NUM_TEMPFILES_FIELD_NUMBER: _ClassVar[int]
    BCT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REDO_LOG_CONF_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOG_DEST_FIELD_NUMBER: _ClassVar[int]
    DIAG_DEST_FIELD_NUMBER: _ClassVar[int]
    FRA_DEST_FIELD_NUMBER: _ClassVar[int]
    FRA_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    DB_CONFIG_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ARCHIVE_LOG_MODE_FIELD_NUMBER: _ClassVar[int]
    SGA_TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHARED_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    PFILE_PARAMETER_MAP_FIELD_NUMBER: _ClassVar[int]
    num_tempfiles: int
    bct_file_path: str
    control_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    redo_log_conf: OracleDBConfig.RedoLogGroupConf
    audit_log_dest: str
    diag_dest: str
    fra_dest: str
    fra_size_mb: int
    db_config_file_path: str
    enable_archive_log_mode: bool
    sga_target_size: str
    shared_pool_size: str
    pfile_parameter_map: _containers.ScalarMap[str, str]
    def __init__(self, num_tempfiles: _Optional[int] = ..., bct_file_path: _Optional[str] = ..., control_file_path_vec: _Optional[_Iterable[str]] = ..., redo_log_conf: _Optional[_Union[OracleDBConfig.RedoLogGroupConf, _Mapping]] = ..., audit_log_dest: _Optional[str] = ..., diag_dest: _Optional[str] = ..., fra_dest: _Optional[str] = ..., fra_size_mb: _Optional[int] = ..., db_config_file_path: _Optional[str] = ..., enable_archive_log_mode: bool = ..., sga_target_size: _Optional[str] = ..., shared_pool_size: _Optional[str] = ..., pfile_parameter_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PDBRestoreParam(_message.Message):
    __slots__ = ("existing_cdb", "pdb_entity_info_vec", "drop_pdbs_if_exists", "rename_pdb_map", "include_in_restore")
    class RenamePdbMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EXISTING_CDB_FIELD_NUMBER: _ClassVar[int]
    PDB_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DROP_PDBS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RENAME_PDB_MAP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IN_RESTORE_FIELD_NUMBER: _ClassVar[int]
    existing_cdb: bool
    pdb_entity_info_vec: _oracle_pb2_1.CDBEntityInfo
    drop_pdbs_if_exists: bool
    rename_pdb_map: _containers.ScalarMap[str, str]
    include_in_restore: bool
    def __init__(self, existing_cdb: bool = ..., pdb_entity_info_vec: _Optional[_Union[_oracle_pb2_1.CDBEntityInfo, _Mapping]] = ..., drop_pdbs_if_exists: bool = ..., rename_pdb_map: _Optional[_Mapping[str, str]] = ..., include_in_restore: bool = ...) -> None: ...

class GranularRestoreInfo(_message.Message):
    __slots__ = ("granularity_type", "pdb_restore_params")
    class GranularityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPDB: _ClassVar[GranularRestoreInfo.GranularityType]
        kTable: _ClassVar[GranularRestoreInfo.GranularityType]
    kPDB: GranularRestoreInfo.GranularityType
    kTable: GranularRestoreInfo.GranularityType
    GRANULARITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PDB_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    granularity_type: GranularRestoreInfo.GranularityType
    pdb_restore_params: PDBRestoreParam
    def __init__(self, granularity_type: _Optional[_Union[GranularRestoreInfo.GranularityType, str]] = ..., pdb_restore_params: _Optional[_Union[PDBRestoreParam, _Mapping]] = ...) -> None: ...

class RestoreSpfileOrPfileInfo(_message.Message):
    __slots__ = ("should_restore_spfile_or_pfile", "file_location")
    SHOULD_RESTORE_SPFILE_OR_PFILE_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    should_restore_spfile_or_pfile: bool
    file_location: str
    def __init__(self, should_restore_spfile_or_pfile: bool = ..., file_location: _Optional[str] = ...) -> None: ...

class OracleArchiveLogInfo(_message.Message):
    __slots__ = ("oracle_archive_log_range_vec", "oracle_archive_log_restore_dest")
    class OracleArchiveLogRange(_message.Message):
        __slots__ = ("range_type", "start_of_range", "end_of_range", "attributes")
        class RangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kTime: _ClassVar[OracleArchiveLogInfo.OracleArchiveLogRange.RangeType]
            kScn: _ClassVar[OracleArchiveLogInfo.OracleArchiveLogRange.RangeType]
            kSequence: _ClassVar[OracleArchiveLogInfo.OracleArchiveLogRange.RangeType]
        kTime: OracleArchiveLogInfo.OracleArchiveLogRange.RangeType
        kScn: OracleArchiveLogInfo.OracleArchiveLogRange.RangeType
        kSequence: OracleArchiveLogInfo.OracleArchiveLogRange.RangeType
        class RangeAttributes(_message.Message):
            __slots__ = ("job_uid", "reset_logs_id", "incarnation_id", "thread_id")
            JOB_UID_FIELD_NUMBER: _ClassVar[int]
            RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
            INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
            THREAD_ID_FIELD_NUMBER: _ClassVar[int]
            job_uid: _universal_id_pb2.UniversalIdProto
            reset_logs_id: int
            incarnation_id: int
            thread_id: int
            def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reset_logs_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., thread_id: _Optional[int] = ...) -> None: ...
        RANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        START_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
        END_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        range_type: OracleArchiveLogInfo.OracleArchiveLogRange.RangeType
        start_of_range: int
        end_of_range: int
        attributes: OracleArchiveLogInfo.OracleArchiveLogRange.RangeAttributes
        def __init__(self, range_type: _Optional[_Union[OracleArchiveLogInfo.OracleArchiveLogRange.RangeType, str]] = ..., start_of_range: _Optional[int] = ..., end_of_range: _Optional[int] = ..., attributes: _Optional[_Union[OracleArchiveLogInfo.OracleArchiveLogRange.RangeAttributes, _Mapping]] = ...) -> None: ...
    ORACLE_ARCHIVE_LOG_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_DEST_FIELD_NUMBER: _ClassVar[int]
    oracle_archive_log_range_vec: _containers.RepeatedCompositeFieldContainer[OracleArchiveLogInfo.OracleArchiveLogRange]
    oracle_archive_log_restore_dest: str
    def __init__(self, oracle_archive_log_range_vec: _Optional[_Iterable[_Union[OracleArchiveLogInfo.OracleArchiveLogRange, _Mapping]]] = ..., oracle_archive_log_restore_dest: _Optional[str] = ...) -> None: ...

class OracleRecoveryValidationInfo(_message.Message):
    __slots__ = ("create_dummy_instance",)
    CREATE_DUMMY_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    create_dummy_instance: bool
    def __init__(self, create_dummy_instance: bool = ...) -> None: ...

class RestoreOracleAppObjectParams(_message.Message):
    __slots__ = ("restore_time_secs", "alternate_location_params", "no_open_mode", "oracle_target_params", "oracle_clone_app_view_params_vec", "parallel_op_enabled", "shell_environment_vec", "granular_restore_info", "is_multi_stage_restore", "oracle_update_restore_options", "oracle_archive_log_restore_info", "skip_clone_nid", "roll_forward_log_path_vec", "attempt_complete_recovery", "roll_forward_time_msecs", "oracle_recovery_validation_info", "restore_spfile_or_pfile_info", "use_scn_for_restore", "stop_active_passive", "same_config_ir_recovery_options", "restore_as_rac")
    class AlternateLocationParams(_message.Message):
        __slots__ = ("new_database_name", "base_dir", "home_dir", "database_file_destination", "oracle_db_config", "newname_clause", "nofilenamecheck", "new_sid_deprecated")
        NEW_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_DIR_FIELD_NUMBER: _ClassVar[int]
        HOME_DIR_FIELD_NUMBER: _ClassVar[int]
        DATABASE_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        ORACLE_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NEWNAME_CLAUSE_FIELD_NUMBER: _ClassVar[int]
        NOFILENAMECHECK_FIELD_NUMBER: _ClassVar[int]
        NEW_SID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        new_database_name: str
        base_dir: str
        home_dir: str
        database_file_destination: str
        oracle_db_config: OracleDBConfig
        newname_clause: str
        nofilenamecheck: bool
        new_sid_deprecated: str
        def __init__(self, new_database_name: _Optional[str] = ..., base_dir: _Optional[str] = ..., home_dir: _Optional[str] = ..., database_file_destination: _Optional[str] = ..., oracle_db_config: _Optional[_Union[OracleDBConfig, _Mapping]] = ..., newname_clause: _Optional[str] = ..., nofilenamecheck: bool = ..., new_sid_deprecated: _Optional[str] = ...) -> None: ...
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    RESTORE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    ORACLE_TARGET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_CLONE_APP_VIEW_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_OP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_STAGE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ORACLE_UPDATE_RESTORE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_NID_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_LOG_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COMPLETE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RECOVERY_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SPFILE_OR_PFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_SCN_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    STOP_ACTIVE_PASSIVE_FIELD_NUMBER: _ClassVar[int]
    SAME_CONFIG_IR_RECOVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_AS_RAC_FIELD_NUMBER: _ClassVar[int]
    restore_time_secs: int
    alternate_location_params: RestoreOracleAppObjectParams.AlternateLocationParams
    no_open_mode: bool
    oracle_target_params: _env_params_pb2.OracleSourceParams
    oracle_clone_app_view_params_vec: _containers.RepeatedCompositeFieldContainer[CloneAppViewParams]
    parallel_op_enabled: bool
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[RestoreOracleAppObjectParams.KeyValuePair]
    granular_restore_info: GranularRestoreInfo
    is_multi_stage_restore: bool
    oracle_update_restore_options: OracleUpdateRestoreTaskOptions
    oracle_archive_log_restore_info: OracleArchiveLogInfo
    skip_clone_nid: bool
    roll_forward_log_path_vec: _containers.RepeatedScalarFieldContainer[str]
    attempt_complete_recovery: bool
    roll_forward_time_msecs: int
    oracle_recovery_validation_info: OracleRecoveryValidationInfo
    restore_spfile_or_pfile_info: RestoreSpfileOrPfileInfo
    use_scn_for_restore: bool
    stop_active_passive: bool
    same_config_ir_recovery_options: _oracle_pb2.SameConfigIrRecoveryOptions
    restore_as_rac: bool
    def __init__(self, restore_time_secs: _Optional[int] = ..., alternate_location_params: _Optional[_Union[RestoreOracleAppObjectParams.AlternateLocationParams, _Mapping]] = ..., no_open_mode: bool = ..., oracle_target_params: _Optional[_Union[_env_params_pb2.OracleSourceParams, _Mapping]] = ..., oracle_clone_app_view_params_vec: _Optional[_Iterable[_Union[CloneAppViewParams, _Mapping]]] = ..., parallel_op_enabled: bool = ..., shell_environment_vec: _Optional[_Iterable[_Union[RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ..., granular_restore_info: _Optional[_Union[GranularRestoreInfo, _Mapping]] = ..., is_multi_stage_restore: bool = ..., oracle_update_restore_options: _Optional[_Union[OracleUpdateRestoreTaskOptions, _Mapping]] = ..., oracle_archive_log_restore_info: _Optional[_Union[OracleArchiveLogInfo, _Mapping]] = ..., skip_clone_nid: bool = ..., roll_forward_log_path_vec: _Optional[_Iterable[str]] = ..., attempt_complete_recovery: bool = ..., roll_forward_time_msecs: _Optional[int] = ..., oracle_recovery_validation_info: _Optional[_Union[OracleRecoveryValidationInfo, _Mapping]] = ..., restore_spfile_or_pfile_info: _Optional[_Union[RestoreSpfileOrPfileInfo, _Mapping]] = ..., use_scn_for_restore: bool = ..., stop_active_passive: bool = ..., same_config_ir_recovery_options: _Optional[_Union[_oracle_pb2.SameConfigIrRecoveryOptions, _Mapping]] = ..., restore_as_rac: bool = ...) -> None: ...

class RestoreADAppObjectParams(_message.Message):
    __slots__ = ("ldap_port", "credentials", "ad_update_options", "ad_restore_status_vec", "num_successfull", "num_failed", "num_running", "should_mount_and_restore")
    LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AD_UPDATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AD_RESTORE_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFULL_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_FIELD_NUMBER: _ClassVar[int]
    NUM_RUNNING_FIELD_NUMBER: _ClassVar[int]
    SHOULD_MOUNT_AND_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ldap_port: int
    credentials: _credentials_pb2.Credentials
    ad_update_options: ADUpdateRestoreTaskOptions
    ad_restore_status_vec: _containers.RepeatedCompositeFieldContainer[ADRestoreStatus]
    num_successfull: int
    num_failed: int
    num_running: int
    should_mount_and_restore: bool
    def __init__(self, ldap_port: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., ad_update_options: _Optional[_Union[ADUpdateRestoreTaskOptions, _Mapping]] = ..., ad_restore_status_vec: _Optional[_Iterable[_Union[ADRestoreStatus, _Mapping]]] = ..., num_successfull: _Optional[int] = ..., num_failed: _Optional[int] = ..., num_running: _Optional[int] = ..., should_mount_and_restore: bool = ...) -> None: ...

class ADUpdateRestoreAction(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ADUpdateRestoreAction.Type]
        kObjects: _ClassVar[ADUpdateRestoreAction.Type]
        kObjectAttributes: _ClassVar[ADUpdateRestoreAction.Type]
    kNone: ADUpdateRestoreAction.Type
    kObjects: ADUpdateRestoreAction.Type
    kObjectAttributes: ADUpdateRestoreAction.Type
    def __init__(self) -> None: ...

class ADUpdateRestoreTaskOptions(_message.Message):
    __slots__ = ("type", "object_param", "object_attributes_param")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ATTRIBUTES_PARAM_FIELD_NUMBER: _ClassVar[int]
    type: ADUpdateRestoreAction.Type
    object_param: _ad_param_pb2.ADObjectRestoreParam
    object_attributes_param: _ad_param_pb2.ADAttributeRestoreParam
    def __init__(self, type: _Optional[_Union[ADUpdateRestoreAction.Type, str]] = ..., object_param: _Optional[_Union[_ad_param_pb2.ADObjectRestoreParam, _Mapping]] = ..., object_attributes_param: _Optional[_Union[_ad_param_pb2.ADAttributeRestoreParam, _Mapping]] = ...) -> None: ...

class ADRestoreStatus(_message.Message):
    __slots__ = ("object_info", "status")
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    object_info: _ad_param_pb2.CompareADObjectsResult.ADObject
    status: _ad_param_pb2.ADObjectRestoreStatus
    def __init__(self, object_info: _Optional[_Union[_ad_param_pb2.CompareADObjectsResult.ADObject, _Mapping]] = ..., status: _Optional[_Union[_ad_param_pb2.ADObjectRestoreStatus, _Mapping]] = ...) -> None: ...

class ExchangeRestoreType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ExchangeRestoreType.Type]
        kView: _ClassVar[ExchangeRestoreType.Type]
        kDatabase: _ClassVar[ExchangeRestoreType.Type]
    kNone: ExchangeRestoreType.Type
    kView: ExchangeRestoreType.Type
    kDatabase: ExchangeRestoreType.Type
    def __init__(self) -> None: ...

class RestoreExchangeParams(_message.Message):
    __slots__ = ("type", "view_options", "database_options")
    class ViewOptions(_message.Message):
        __slots__ = ("whitelist_restore_view_for_all", "view_name", "mount_point")
        WHITELIST_RESTORE_VIEW_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        whitelist_restore_view_for_all: bool
        view_name: str
        mount_point: str
        def __init__(self, whitelist_restore_view_for_all: bool = ..., view_name: _Optional[str] = ..., mount_point: _Optional[str] = ...) -> None: ...
    class DatabaseOptions(_message.Message):
        __slots__ = ("entity_id", "target_host_entity", "use_latest_logs", "restore_as_recovery_db", "mount_db", "dest_db_name", "dest_edb_filepath", "dest_log_dirpath", "progress_monitor_path")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
        USE_LATEST_LOGS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_AS_RECOVERY_DB_FIELD_NUMBER: _ClassVar[int]
        MOUNT_DB_FIELD_NUMBER: _ClassVar[int]
        DEST_DB_NAME_FIELD_NUMBER: _ClassVar[int]
        DEST_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
        DEST_LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        target_host_entity: _entity_pb2.EntityProto
        use_latest_logs: bool
        restore_as_recovery_db: bool
        mount_db: bool
        dest_db_name: str
        dest_edb_filepath: str
        dest_log_dirpath: str
        progress_monitor_path: str
        def __init__(self, entity_id: _Optional[int] = ..., target_host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., use_latest_logs: bool = ..., restore_as_recovery_db: bool = ..., mount_db: bool = ..., dest_db_name: _Optional[str] = ..., dest_edb_filepath: _Optional[str] = ..., dest_log_dirpath: _Optional[str] = ..., progress_monitor_path: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    type: ExchangeRestoreType.Type
    view_options: RestoreExchangeParams.ViewOptions
    database_options: RestoreExchangeParams.DatabaseOptions
    def __init__(self, type: _Optional[_Union[ExchangeRestoreType.Type, str]] = ..., view_options: _Optional[_Union[RestoreExchangeParams.ViewOptions, _Mapping]] = ..., database_options: _Optional[_Union[RestoreExchangeParams.DatabaseOptions, _Mapping]] = ...) -> None: ...

class AppOwnerRestoreInfo(_message.Message):
    __slots__ = ("owner_object", "perform_restore", "owner_restore_params")
    OWNER_OBJECT_FIELD_NUMBER: _ClassVar[int]
    PERFORM_RESTORE_FIELD_NUMBER: _ClassVar[int]
    OWNER_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    owner_object: RestoreObject
    perform_restore: bool
    owner_restore_params: RestoreObjectParams
    def __init__(self, owner_object: _Optional[_Union[RestoreObject, _Mapping]] = ..., perform_restore: bool = ..., owner_restore_params: _Optional[_Union[RestoreObjectParams, _Mapping]] = ...) -> None: ...

class RestoreAppParams(_message.Message):
    __slots__ = ("type", "owner_restore_info", "restore_app_object_vec", "credentials")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    owner_restore_info: AppOwnerRestoreInfo
    restore_app_object_vec: _containers.RepeatedCompositeFieldContainer[RestoreAppObject]
    credentials: _credentials_pb2.Credentials
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., owner_restore_info: _Optional[_Union[AppOwnerRestoreInfo, _Mapping]] = ..., restore_app_object_vec: _Optional[_Iterable[_Union[RestoreAppObject, _Mapping]]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class RestoredFileInfo(_message.Message):
    __slots__ = ("absolute_path", "inode_number", "is_directory", "is_non_simple_ldm_vol", "virtual_disk_file", "disk_partition_id", "volume_id", "volume_path", "attached_disk_id", "restore_mount_point", "size_bytes", "fs_uuid", "restore_base_directory")
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    INODE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    IS_NON_SIMPLE_LDM_VOL_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FILE_FIELD_NUMBER: _ClassVar[int]
    DISK_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FS_UUID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    inode_number: int
    is_directory: bool
    is_non_simple_ldm_vol: bool
    virtual_disk_file: str
    disk_partition_id: int
    volume_id: str
    volume_path: str
    attached_disk_id: int
    restore_mount_point: str
    size_bytes: int
    fs_uuid: str
    restore_base_directory: str
    def __init__(self, absolute_path: _Optional[str] = ..., inode_number: _Optional[int] = ..., is_directory: bool = ..., is_non_simple_ldm_vol: bool = ..., virtual_disk_file: _Optional[str] = ..., disk_partition_id: _Optional[int] = ..., volume_id: _Optional[str] = ..., volume_path: _Optional[str] = ..., attached_disk_id: _Optional[int] = ..., restore_mount_point: _Optional[str] = ..., size_bytes: _Optional[int] = ..., fs_uuid: _Optional[str] = ..., restore_base_directory: _Optional[str] = ...) -> None: ...

class RestoreFilesPreferences(_message.Message):
    __slots__ = ("restore_to_original_paths", "override_originals", "alternate_restore_base_directory", "preserve_attributes", "preserve_timestamps", "preserve_acls", "continue_on_error", "skip_estimation", "generate_ssh_keys", "encryption_enabled", "save_success_files", "restore_entities")
    class RestoreEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[RestoreFilesPreferences.RestoreEntityType]
        kACLOnly: _ClassVar[RestoreFilesPreferences.RestoreEntityType]
    kRegular: RestoreFilesPreferences.RestoreEntityType
    kACLOnly: RestoreFilesPreferences.RestoreEntityType
    RESTORE_TO_ORIGINAL_PATHS_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_ORIGINALS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_RESTORE_BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ACLS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    SKIP_ESTIMATION_FIELD_NUMBER: _ClassVar[int]
    GENERATE_SSH_KEYS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SAVE_SUCCESS_FILES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    restore_to_original_paths: bool
    override_originals: bool
    alternate_restore_base_directory: str
    preserve_attributes: bool
    preserve_timestamps: bool
    preserve_acls: bool
    continue_on_error: bool
    skip_estimation: bool
    generate_ssh_keys: bool
    encryption_enabled: bool
    save_success_files: bool
    restore_entities: RestoreFilesPreferences.RestoreEntityType
    def __init__(self, restore_to_original_paths: bool = ..., override_originals: bool = ..., alternate_restore_base_directory: _Optional[str] = ..., preserve_attributes: bool = ..., preserve_timestamps: bool = ..., preserve_acls: bool = ..., continue_on_error: bool = ..., skip_estimation: bool = ..., generate_ssh_keys: bool = ..., encryption_enabled: bool = ..., save_success_files: bool = ..., restore_entities: _Optional[_Union[RestoreFilesPreferences.RestoreEntityType, str]] = ...) -> None: ...

class RestoreFilesParams(_message.Message):
    __slots__ = ("restored_file_info_vec", "target_entity", "target_entity_parent_source", "target_host_entity", "proxy_entity", "proxy_entity_parent_source", "target_entity_credentials", "target_host_type", "nas_protocol_type_vec", "directory_name_security_style_map", "restore_files_preferences", "is_file_volume_restore", "is_mount_based_flr", "vpc_connector_entity", "is_archive_flr", "uptier_params", "use_existing_agent", "mount_disks_on_vm", "restore_method", "nas_backup_params", "physical_flr_parallel_restore", "blacklisted_ip_addrs", "whitelisted_ip_addrs", "isilon_env_params", "is_source_initiated_restore", "objectstore_config_name", "destination_ep_uuid", "source_snapshot_name", "s3viewbackupproperties", "view_name", "view_id", "glacier_flr_restore_option")
    class RestoreMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAutoDeploy: _ClassVar[RestoreFilesParams.RestoreMethod]
        kUseExistingAgent: _ClassVar[RestoreFilesParams.RestoreMethod]
        kUseHypervisorAPIs: _ClassVar[RestoreFilesParams.RestoreMethod]
    kAutoDeploy: RestoreFilesParams.RestoreMethod
    kUseExistingAgent: RestoreFilesParams.RestoreMethod
    kUseHypervisorAPIs: RestoreFilesParams.RestoreMethod
    class GlacierFLRRestoreOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStandard: _ClassVar[RestoreFilesParams.GlacierFLRRestoreOption]
        kExpeditedNoPCU: _ClassVar[RestoreFilesParams.GlacierFLRRestoreOption]
        kExpeditedWithPCU: _ClassVar[RestoreFilesParams.GlacierFLRRestoreOption]
    kStandard: RestoreFilesParams.GlacierFLRRestoreOption
    kExpeditedNoPCU: RestoreFilesParams.GlacierFLRRestoreOption
    kExpeditedWithPCU: RestoreFilesParams.GlacierFLRRestoreOption
    class DirectoryNameSecurityStyleMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORED_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PROXY_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PROXY_ENTITY_PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAS_PROTOCOL_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_NAME_SECURITY_STYLE_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_VOLUME_RESTORE_FIELD_NUMBER: _ClassVar[int]
    IS_MOUNT_BASED_FLR_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVE_FLR_FIELD_NUMBER: _ClassVar[int]
    UPTIER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_AGENT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DISKS_ON_VM_FIELD_NUMBER: _ClassVar[int]
    RESTORE_METHOD_FIELD_NUMBER: _ClassVar[int]
    NAS_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_FLR_PARALLEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    ISILON_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_INITIATED_RESTORE_FIELD_NUMBER: _ClassVar[int]
    OBJECTSTORE_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_EP_UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    S3VIEWBACKUPPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    GLACIER_FLR_RESTORE_OPTION_FIELD_NUMBER: _ClassVar[int]
    restored_file_info_vec: _containers.RepeatedCompositeFieldContainer[RestoredFileInfo]
    target_entity: _entity_pb2.EntityProto
    target_entity_parent_source: _entity_pb2.EntityProto
    target_host_entity: _entity_pb2.EntityProto
    proxy_entity: _entity_pb2.EntityProto
    proxy_entity_parent_source: _entity_pb2.EntityProto
    target_entity_credentials: _credentials_pb2.Credentials
    target_host_type: _enums_pb2.HostEnv.Type
    nas_protocol_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
    directory_name_security_style_map: _containers.ScalarMap[str, str]
    restore_files_preferences: RestoreFilesPreferences
    is_file_volume_restore: bool
    is_mount_based_flr: bool
    vpc_connector_entity: _entity_pb2.EntityProto
    is_archive_flr: bool
    uptier_params: _env_params_pb2.FileUptieringParams
    use_existing_agent: bool
    mount_disks_on_vm: bool
    restore_method: RestoreFilesParams.RestoreMethod
    nas_backup_params: _env_params_pb2.NasBackupParams
    physical_flr_parallel_restore: bool
    blacklisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    whitelisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    isilon_env_params: _env_params_pb2.IsilonEnvParams
    is_source_initiated_restore: bool
    objectstore_config_name: str
    destination_ep_uuid: str
    source_snapshot_name: str
    s3viewbackupproperties: _env_params_pb2.S3ViewBackupProperties
    view_name: str
    view_id: int
    glacier_flr_restore_option: RestoreFilesParams.GlacierFLRRestoreOption
    def __init__(self, restored_file_info_vec: _Optional[_Iterable[_Union[RestoredFileInfo, _Mapping]]] = ..., target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_entity_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., proxy_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., proxy_entity_parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., target_host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., nas_protocol_type_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ..., directory_name_security_style_map: _Optional[_Mapping[str, str]] = ..., restore_files_preferences: _Optional[_Union[RestoreFilesPreferences, _Mapping]] = ..., is_file_volume_restore: bool = ..., is_mount_based_flr: bool = ..., vpc_connector_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_archive_flr: bool = ..., uptier_params: _Optional[_Union[_env_params_pb2.FileUptieringParams, _Mapping]] = ..., use_existing_agent: bool = ..., mount_disks_on_vm: bool = ..., restore_method: _Optional[_Union[RestoreFilesParams.RestoreMethod, str]] = ..., nas_backup_params: _Optional[_Union[_env_params_pb2.NasBackupParams, _Mapping]] = ..., physical_flr_parallel_restore: bool = ..., blacklisted_ip_addrs: _Optional[_Iterable[str]] = ..., whitelisted_ip_addrs: _Optional[_Iterable[str]] = ..., isilon_env_params: _Optional[_Union[_env_params_pb2.IsilonEnvParams, _Mapping]] = ..., is_source_initiated_restore: bool = ..., objectstore_config_name: _Optional[str] = ..., destination_ep_uuid: _Optional[str] = ..., source_snapshot_name: _Optional[str] = ..., s3viewbackupproperties: _Optional[_Union[_env_params_pb2.S3ViewBackupProperties, _Mapping]] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., glacier_flr_restore_option: _Optional[_Union[RestoreFilesParams.GlacierFLRRestoreOption, str]] = ...) -> None: ...

class MountVolumesVMwareParams(_message.Message):
    __slots__ = ("target_entity_credentials", "bring_disks_online")
    TARGET_ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BRING_DISKS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    target_entity_credentials: _credentials_pb2.Credentials
    bring_disks_online: bool
    def __init__(self, target_entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., bring_disks_online: bool = ...) -> None: ...

class MountVolumesHyperVParams(_message.Message):
    __slots__ = ("target_entity_credentials", "bring_disks_online")
    TARGET_ENTITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BRING_DISKS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    target_entity_credentials: _credentials_pb2.Credentials
    bring_disks_online: bool
    def __init__(self, target_entity_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., bring_disks_online: bool = ...) -> None: ...

class MountVolumesParams(_message.Message):
    __slots__ = ("target_entity", "volume_name_vec", "vmware_params", "readonly_mount", "hyperv_params", "use_existing_agent")
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    READONLY_MOUNT_FIELD_NUMBER: _ClassVar[int]
    HYPERV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_AGENT_FIELD_NUMBER: _ClassVar[int]
    target_entity: _entity_pb2.EntityProto
    volume_name_vec: _containers.RepeatedScalarFieldContainer[str]
    vmware_params: MountVolumesVMwareParams
    readonly_mount: bool
    hyperv_params: MountVolumesHyperVParams
    use_existing_agent: bool
    def __init__(self, target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., volume_name_vec: _Optional[_Iterable[str]] = ..., vmware_params: _Optional[_Union[MountVolumesVMwareParams, _Mapping]] = ..., readonly_mount: bool = ..., hyperv_params: _Optional[_Union[MountVolumesHyperVParams, _Mapping]] = ..., use_existing_agent: bool = ...) -> None: ...

class VirtualDiskId(_message.Message):
    __slots__ = ("disk_id", "unit_number", "controller_bus_number", "controller_type")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_id: str
    unit_number: int
    controller_bus_number: int
    controller_type: str
    def __init__(self, disk_id: _Optional[str] = ..., unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ...) -> None: ...

class VirtualDiskInfo(_message.Message):
    __slots__ = ("virtual_disk_id", "file_path", "volume_info_vec", "capacity", "location", "claim_name", "volume_name", "storage_class", "labels")
    class VolumeInfo(_message.Message):
        __slots__ = ("mount_point",)
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        mount_point: str
        def __init__(self, mount_point: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VIRTUAL_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLAIM_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_id: VirtualDiskId
    file_path: str
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo.VolumeInfo]
    capacity: int
    location: _entity_pb2.EntityProto
    claim_name: str
    volume_name: str
    storage_class: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, virtual_disk_id: _Optional[_Union[VirtualDiskId, _Mapping]] = ..., file_path: _Optional[str] = ..., volume_info_vec: _Optional[_Iterable[_Union[VirtualDiskInfo.VolumeInfo, _Mapping]]] = ..., capacity: _Optional[int] = ..., location: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., claim_name: _Optional[str] = ..., volume_name: _Optional[str] = ..., storage_class: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RecoverVirtualDiskParams(_message.Message):
    __slots__ = ("target_entity", "virtual_disk_mappings", "power_off_vm_before_recovery", "power_on_vm_after_recovery")
    class VirtualDiskMapping(_message.Message):
        __slots__ = ("src_disk", "disk_to_overwrite", "target_location")
        SRC_DISK_FIELD_NUMBER: _ClassVar[int]
        DISK_TO_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
        TARGET_LOCATION_FIELD_NUMBER: _ClassVar[int]
        src_disk: VirtualDiskId
        disk_to_overwrite: VirtualDiskId
        target_location: _entity_pb2.EntityProto
        def __init__(self, src_disk: _Optional[_Union[VirtualDiskId, _Mapping]] = ..., disk_to_overwrite: _Optional[_Union[VirtualDiskId, _Mapping]] = ..., target_location: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    POWER_OFF_VM_BEFORE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_VM_AFTER_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    target_entity: _entity_pb2.EntityProto
    virtual_disk_mappings: _containers.RepeatedCompositeFieldContainer[RecoverVirtualDiskParams.VirtualDiskMapping]
    power_off_vm_before_recovery: bool
    power_on_vm_after_recovery: bool
    def __init__(self, target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., virtual_disk_mappings: _Optional[_Iterable[_Union[RecoverVirtualDiskParams.VirtualDiskMapping, _Mapping]]] = ..., power_off_vm_before_recovery: bool = ..., power_on_vm_after_recovery: bool = ...) -> None: ...

class RecoverVolumesParams(_message.Message):
    __slots__ = ("target_entity", "mapping_vec", "force_unmount_volume")
    class Mapping(_message.Message):
        __slots__ = ("src_guid", "dst_guid")
        SRC_GUID_FIELD_NUMBER: _ClassVar[int]
        DST_GUID_FIELD_NUMBER: _ClassVar[int]
        src_guid: str
        dst_guid: str
        def __init__(self, src_guid: _Optional[str] = ..., dst_guid: _Optional[str] = ...) -> None: ...
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_UNMOUNT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    target_entity: _entity_pb2.EntityProto
    mapping_vec: _containers.RepeatedCompositeFieldContainer[RecoverVolumesParams.Mapping]
    force_unmount_volume: bool
    def __init__(self, target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., mapping_vec: _Optional[_Iterable[_Union[RecoverVolumesParams.Mapping, _Mapping]]] = ..., force_unmount_volume: bool = ...) -> None: ...

class RestoreAcropolisVMsParams(_message.Message):
    __slots__ = ("rename_restored_object_param", "restored_objects_network_config", "power_state_config", "storage_container", "uuid_config", "recover_excluded_disks_as_blank_disks", "copy_recovery")
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    UUID_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RECOVER_EXCLUDED_DISKS_AS_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    COPY_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    rename_restored_object_param: RenameObjectParamProto
    restored_objects_network_config: RestoredObjectNetworkConfigProto
    power_state_config: PowerStateConfigProto
    storage_container: _entity_pb2.EntityProto
    uuid_config: UuidConfigProto
    recover_excluded_disks_as_blank_disks: bool
    copy_recovery: bool
    def __init__(self, rename_restored_object_param: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ..., storage_container: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., uuid_config: _Optional[_Union[UuidConfigProto, _Mapping]] = ..., recover_excluded_disks_as_blank_disks: bool = ..., copy_recovery: bool = ...) -> None: ...

class RestoreHyperVVMParams(_message.Message):
    __slots__ = ("rename_restored_object_param", "restored_objects_network_config", "power_state_config", "resource_entity", "datastore_entity", "copy_recovery", "recover_excluded_disks_as_blank_disks", "use_smb_service", "uuid_config")
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    COPY_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    RECOVER_EXCLUDED_DISKS_AS_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    USE_SMB_SERVICE_FIELD_NUMBER: _ClassVar[int]
    UUID_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rename_restored_object_param: RenameObjectParamProto
    restored_objects_network_config: RestoredObjectNetworkConfigProto
    power_state_config: PowerStateConfigProto
    resource_entity: _entity_pb2.EntityProto
    datastore_entity: _entity_pb2.EntityProto
    copy_recovery: bool
    recover_excluded_disks_as_blank_disks: bool
    use_smb_service: bool
    uuid_config: UuidConfigProto
    def __init__(self, rename_restored_object_param: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ..., resource_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datastore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., copy_recovery: bool = ..., recover_excluded_disks_as_blank_disks: bool = ..., use_smb_service: bool = ..., uuid_config: _Optional[_Union[UuidConfigProto, _Mapping]] = ...) -> None: ...

class RestoreOutlookParams(_message.Message):
    __slots__ = ("mailbox_vec", "target_mailbox", "target_folder_path", "pst_params", "skip_mbx_permit_for_pst", "skip_recover_archive_mailbox", "skip_recover_recoverable_items", "recoverable_items_prefix", "skip_recover_archive_recoverable_items", "archive_recoverable_items_prefix")
    class Folder(_message.Message):
        __slots__ = ("folder_id", "folder_key", "is_entire_folder_required", "item_id_vec")
        FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        IS_ENTIRE_FOLDER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        folder_id: str
        folder_key: int
        is_entire_folder_required: bool
        item_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, folder_id: _Optional[str] = ..., folder_key: _Optional[int] = ..., is_entire_folder_required: bool = ..., item_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class Mailbox(_message.Message):
        __slots__ = ("object", "is_entire_mailbox_required", "folder_vec")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        IS_ENTIRE_MAILBOX_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        is_entire_mailbox_required: bool
        folder_vec: _containers.RepeatedCompositeFieldContainer[RestoreOutlookParams.Folder]
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., is_entire_mailbox_required: bool = ..., folder_vec: _Optional[_Iterable[_Union[RestoreOutlookParams.Folder, _Mapping]]] = ...) -> None: ...
    MAILBOX_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    PST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_MBX_PERMIT_FOR_PST_FIELD_NUMBER: _ClassVar[int]
    SKIP_RECOVER_ARCHIVE_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    SKIP_RECOVER_RECOVERABLE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    RECOVERABLE_ITEMS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SKIP_RECOVER_ARCHIVE_RECOVERABLE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_RECOVERABLE_ITEMS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    mailbox_vec: _containers.RepeatedCompositeFieldContainer[RestoreOutlookParams.Mailbox]
    target_mailbox: _entity_pb2.EntityProto
    target_folder_path: str
    pst_params: _exchange_param_pb2.EwsToPstConversionParams
    skip_mbx_permit_for_pst: bool
    skip_recover_archive_mailbox: bool
    skip_recover_recoverable_items: bool
    recoverable_items_prefix: str
    skip_recover_archive_recoverable_items: bool
    archive_recoverable_items_prefix: str
    def __init__(self, mailbox_vec: _Optional[_Iterable[_Union[RestoreOutlookParams.Mailbox, _Mapping]]] = ..., target_mailbox: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_folder_path: _Optional[str] = ..., pst_params: _Optional[_Union[_exchange_param_pb2.EwsToPstConversionParams, _Mapping]] = ..., skip_mbx_permit_for_pst: bool = ..., skip_recover_archive_mailbox: bool = ..., skip_recover_recoverable_items: bool = ..., recoverable_items_prefix: _Optional[str] = ..., skip_recover_archive_recoverable_items: bool = ..., archive_recoverable_items_prefix: _Optional[str] = ...) -> None: ...

class O365OneDriveRestoreEntityParams(_message.Message):
    __slots__ = ("drive_vec",)
    class DriveItem(_message.Message):
        __slots__ = ("drive_item_id", "drive_item_path", "is_file_item")
        DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ITEM_PATH_FIELD_NUMBER: _ClassVar[int]
        IS_FILE_ITEM_FIELD_NUMBER: _ClassVar[int]
        drive_item_id: str
        drive_item_path: str
        is_file_item: bool
        def __init__(self, drive_item_id: _Optional[str] = ..., drive_item_path: _Optional[str] = ..., is_file_item: bool = ...) -> None: ...
    class Drive(_message.Message):
        __slots__ = ("restore_item_vec", "restore_drive_id", "is_entire_drive_required", "drive_type")
        RESTORE_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
        RESTORE_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_ENTIRE_DRIVE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        restore_item_vec: _containers.RepeatedCompositeFieldContainer[O365OneDriveRestoreEntityParams.DriveItem]
        restore_drive_id: str
        is_entire_drive_required: bool
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, restore_item_vec: _Optional[_Iterable[_Union[O365OneDriveRestoreEntityParams.DriveItem, _Mapping]]] = ..., restore_drive_id: _Optional[str] = ..., is_entire_drive_required: bool = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_vec: _containers.RepeatedCompositeFieldContainer[O365OneDriveRestoreEntityParams.Drive]
    def __init__(self, drive_vec: _Optional[_Iterable[_Union[O365OneDriveRestoreEntityParams.Drive, _Mapping]]] = ...) -> None: ...

class RestoreOneDriveParams(_message.Message):
    __slots__ = ("drive_owner_vec", "restore_to_original", "target_user", "target_drive_id", "target_folder_path", "phl_folder_prefix")
    class DriveItem(_message.Message):
        __slots__ = ("id", "drive_item_path", "is_file_item")
        ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ITEM_PATH_FIELD_NUMBER: _ClassVar[int]
        IS_FILE_ITEM_FIELD_NUMBER: _ClassVar[int]
        id: str
        drive_item_path: str
        is_file_item: bool
        def __init__(self, id: _Optional[str] = ..., drive_item_path: _Optional[str] = ..., is_file_item: bool = ...) -> None: ...
    class DriveOwner(_message.Message):
        __slots__ = ("object", "drive_vec")
        class Drive(_message.Message):
            __slots__ = ("restore_item_vec", "restore_drive_id", "is_entire_drive_required")
            RESTORE_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
            RESTORE_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
            IS_ENTIRE_DRIVE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
            restore_item_vec: _containers.RepeatedCompositeFieldContainer[RestoreOneDriveParams.DriveItem]
            restore_drive_id: str
            is_entire_drive_required: bool
            def __init__(self, restore_item_vec: _Optional[_Iterable[_Union[RestoreOneDriveParams.DriveItem, _Mapping]]] = ..., restore_drive_id: _Optional[str] = ..., is_entire_drive_required: bool = ...) -> None: ...
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        drive_vec: _containers.RepeatedCompositeFieldContainer[RestoreOneDriveParams.DriveOwner.Drive]
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., drive_vec: _Optional[_Iterable[_Union[RestoreOneDriveParams.DriveOwner.Drive, _Mapping]]] = ...) -> None: ...
    DRIVE_OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_FIELD_NUMBER: _ClassVar[int]
    TARGET_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    PHL_FOLDER_PREFIX_FIELD_NUMBER: _ClassVar[int]
    drive_owner_vec: _containers.RepeatedCompositeFieldContainer[RestoreOneDriveParams.DriveOwner]
    restore_to_original: bool
    target_user: _entity_pb2.EntityProto
    target_drive_id: str
    target_folder_path: str
    phl_folder_prefix: str
    def __init__(self, drive_owner_vec: _Optional[_Iterable[_Union[RestoreOneDriveParams.DriveOwner, _Mapping]]] = ..., restore_to_original: bool = ..., target_user: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_drive_id: _Optional[str] = ..., target_folder_path: _Optional[str] = ..., phl_folder_prefix: _Optional[str] = ...) -> None: ...

class RestoreSiteParams(_message.Message):
    __slots__ = ("site_owner_vec", "restore_to_original", "target_site", "target_doc_lib_prefix", "target_doc_lib_name", "site_result", "snap_fs_relative_template_path", "restore_template", "snap_fs_relative_site_backup_result_path", "parent_source_sharepoint_domain_name", "site_version", "source_site_uuid", "source_site_name", "source_web_url", "dst_site_uuid", "dst_site_name", "dst_site_web_url", "target_folder_path_prefix", "restore_phl_drive", "phl_restore_prefix", "should_restore_lists")
    class SiteRestoreVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSiteVersionV1: _ClassVar[RestoreSiteParams.SiteRestoreVersion]
        kSiteVersionV2: _ClassVar[RestoreSiteParams.SiteRestoreVersion]
    kSiteVersionV1: RestoreSiteParams.SiteRestoreVersion
    kSiteVersionV2: RestoreSiteParams.SiteRestoreVersion
    class DriveItem(_message.Message):
        __slots__ = ("id", "drive_item_path", "is_file_item")
        ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ITEM_PATH_FIELD_NUMBER: _ClassVar[int]
        IS_FILE_ITEM_FIELD_NUMBER: _ClassVar[int]
        id: str
        drive_item_path: str
        is_file_item: bool
        def __init__(self, id: _Optional[str] = ..., drive_item_path: _Optional[str] = ..., is_file_item: bool = ...) -> None: ...
    class SiteOwner(_message.Message):
        __slots__ = ("object", "parent_site", "drive_vec")
        class Drive(_message.Message):
            __slots__ = ("restore_path_vec", "restore_drive_id", "restore_drive_name", "is_entire_drive_required")
            RESTORE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
            RESTORE_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
            RESTORE_DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
            IS_ENTIRE_DRIVE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
            restore_path_vec: _containers.RepeatedCompositeFieldContainer[RestoreSiteParams.DriveItem]
            restore_drive_id: str
            restore_drive_name: str
            is_entire_drive_required: bool
            def __init__(self, restore_path_vec: _Optional[_Iterable[_Union[RestoreSiteParams.DriveItem, _Mapping]]] = ..., restore_drive_id: _Optional[str] = ..., restore_drive_name: _Optional[str] = ..., is_entire_drive_required: bool = ...) -> None: ...
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        PARENT_SITE_FIELD_NUMBER: _ClassVar[int]
        DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        parent_site: _entity_pb2.EntityProto
        drive_vec: _containers.RepeatedCompositeFieldContainer[RestoreSiteParams.SiteOwner.Drive]
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., parent_site: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., drive_vec: _Optional[_Iterable[_Union[RestoreSiteParams.SiteOwner.Drive, _Mapping]]] = ...) -> None: ...
    SITE_OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_SITE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOC_LIB_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOC_LIB_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_RELATIVE_TEMPLATE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_RELATIVE_SITE_BACKUP_RESULT_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SITE_UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DST_SITE_UUID_FIELD_NUMBER: _ClassVar[int]
    DST_SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    DST_SITE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PHL_DRIVE_FIELD_NUMBER: _ClassVar[int]
    PHL_RESTORE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RESTORE_LISTS_FIELD_NUMBER: _ClassVar[int]
    site_owner_vec: _containers.RepeatedCompositeFieldContainer[RestoreSiteParams.SiteOwner]
    restore_to_original: bool
    target_site: _entity_pb2.EntityProto
    target_doc_lib_prefix: str
    target_doc_lib_name: str
    site_result: _o365spo_pb2.SiteBackupStatus
    snap_fs_relative_template_path: str
    restore_template: bool
    snap_fs_relative_site_backup_result_path: str
    parent_source_sharepoint_domain_name: str
    site_version: RestoreSiteParams.SiteRestoreVersion
    source_site_uuid: str
    source_site_name: str
    source_web_url: str
    dst_site_uuid: str
    dst_site_name: str
    dst_site_web_url: str
    target_folder_path_prefix: str
    restore_phl_drive: bool
    phl_restore_prefix: str
    should_restore_lists: bool
    def __init__(self, site_owner_vec: _Optional[_Iterable[_Union[RestoreSiteParams.SiteOwner, _Mapping]]] = ..., restore_to_original: bool = ..., target_site: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_doc_lib_prefix: _Optional[str] = ..., target_doc_lib_name: _Optional[str] = ..., site_result: _Optional[_Union[_o365spo_pb2.SiteBackupStatus, _Mapping]] = ..., snap_fs_relative_template_path: _Optional[str] = ..., restore_template: bool = ..., snap_fs_relative_site_backup_result_path: _Optional[str] = ..., parent_source_sharepoint_domain_name: _Optional[str] = ..., site_version: _Optional[_Union[RestoreSiteParams.SiteRestoreVersion, str]] = ..., source_site_uuid: _Optional[str] = ..., source_site_name: _Optional[str] = ..., source_web_url: _Optional[str] = ..., dst_site_uuid: _Optional[str] = ..., dst_site_name: _Optional[str] = ..., dst_site_web_url: _Optional[str] = ..., target_folder_path_prefix: _Optional[str] = ..., restore_phl_drive: bool = ..., phl_restore_prefix: _Optional[str] = ..., should_restore_lists: bool = ...) -> None: ...

class RestoreO365PublicFoldersParams(_message.Message):
    __slots__ = ("root_public_folder_vec", "target_root_public_folder", "target_folder_path")
    class PublicFolder(_message.Message):
        __slots__ = ("folder_id", "is_entire_folder_required", "item_id_vec", "absolute_folder_path")
        FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        IS_ENTIRE_FOLDER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
        folder_id: str
        is_entire_folder_required: bool
        item_id_vec: _containers.RepeatedScalarFieldContainer[str]
        absolute_folder_path: str
        def __init__(self, folder_id: _Optional[str] = ..., is_entire_folder_required: bool = ..., item_id_vec: _Optional[_Iterable[str]] = ..., absolute_folder_path: _Optional[str] = ...) -> None: ...
    class RootPublicFolder(_message.Message):
        __slots__ = ("object", "is_entire_root_folder_required", "folder_vec")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        IS_ENTIRE_ROOT_FOLDER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        is_entire_root_folder_required: bool
        folder_vec: _containers.RepeatedCompositeFieldContainer[RestoreO365PublicFoldersParams.PublicFolder]
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., is_entire_root_folder_required: bool = ..., folder_vec: _Optional[_Iterable[_Union[RestoreO365PublicFoldersParams.PublicFolder, _Mapping]]] = ...) -> None: ...
    ROOT_PUBLIC_FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROOT_PUBLIC_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    root_public_folder_vec: _containers.RepeatedCompositeFieldContainer[RestoreO365PublicFoldersParams.RootPublicFolder]
    target_root_public_folder: _entity_pb2.EntityProto
    target_folder_path: str
    def __init__(self, root_public_folder_vec: _Optional[_Iterable[_Union[RestoreO365PublicFoldersParams.RootPublicFolder, _Mapping]]] = ..., target_root_public_folder: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_folder_path: _Optional[str] = ...) -> None: ...

class RestoreO365TeamsParams(_message.Message):
    __slots__ = ("ms_teams_vec", "restore_to_original", "target_team", "target_team_name", "target_team_owner", "create_new_team", "restore_original_owners_members", "target_ms_team_entity", "target_team_owner_entity", "target_channel")
    class TeamInfo(_message.Message):
        __slots__ = ("team_id",)
        TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        team_id: str
        def __init__(self, team_id: _Optional[str] = ...) -> None: ...
    class SourceChannel(_message.Message):
        __slots__ = ("drive_vec", "id", "name", "is_full_channel_restore")
        DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_CHANNEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
        drive_vec: _containers.RepeatedCompositeFieldContainer[RestoreSiteParams.SiteOwner.Drive]
        id: str
        name: str
        is_full_channel_restore: bool
        def __init__(self, drive_vec: _Optional[_Iterable[_Union[RestoreSiteParams.SiteOwner.Drive, _Mapping]]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., is_full_channel_restore: bool = ...) -> None: ...
    class MSTeamInfo(_message.Message):
        __slots__ = ("object", "is_full_team_required", "source_channel_vec")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_TEAM_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CHANNEL_VEC_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        is_full_team_required: bool
        source_channel_vec: _containers.RepeatedCompositeFieldContainer[RestoreO365TeamsParams.SourceChannel]
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., is_full_team_required: bool = ..., source_channel_vec: _Optional[_Iterable[_Union[RestoreO365TeamsParams.SourceChannel, _Mapping]]] = ...) -> None: ...
    class TargetChannel(_message.Message):
        __slots__ = ("id", "name", "create_new_channel", "channel_type", "channel_owner_vec")
        class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kPublic: _ClassVar[RestoreO365TeamsParams.TargetChannel.ChannelType]
            kPrivate: _ClassVar[RestoreO365TeamsParams.TargetChannel.ChannelType]
        kPublic: RestoreO365TeamsParams.TargetChannel.ChannelType
        kPrivate: RestoreO365TeamsParams.TargetChannel.ChannelType
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CREATE_NEW_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        create_new_channel: bool
        channel_type: RestoreO365TeamsParams.TargetChannel.ChannelType
        channel_owner_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., create_new_channel: bool = ..., channel_type: _Optional[_Union[RestoreO365TeamsParams.TargetChannel.ChannelType, str]] = ..., channel_owner_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
    MS_TEAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEAM_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEAM_OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_TEAM_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ORIGINAL_OWNERS_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TARGET_MS_TEAM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEAM_OWNER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ms_teams_vec: _containers.RepeatedCompositeFieldContainer[RestoreO365TeamsParams.MSTeamInfo]
    restore_to_original: bool
    target_team: str
    target_team_name: str
    target_team_owner: str
    create_new_team: bool
    restore_original_owners_members: bool
    target_ms_team_entity: _entity_pb2.EntityProto
    target_team_owner_entity: _entity_pb2.EntityProto
    target_channel: RestoreO365TeamsParams.TargetChannel
    def __init__(self, ms_teams_vec: _Optional[_Iterable[_Union[RestoreO365TeamsParams.MSTeamInfo, _Mapping]]] = ..., restore_to_original: bool = ..., target_team: _Optional[str] = ..., target_team_name: _Optional[str] = ..., target_team_owner: _Optional[str] = ..., create_new_team: bool = ..., restore_original_owners_members: bool = ..., target_ms_team_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_team_owner_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_channel: _Optional[_Union[RestoreO365TeamsParams.TargetChannel, _Mapping]] = ...) -> None: ...

class RestoreO365GroupsParams(_message.Message):
    __slots__ = ("ms_groups_vec", "restore_to_original", "target_group", "target_group_name", "target_group_owner", "create_new_group", "restore_original_owners_members")
    class GroupGranularParams(_message.Message):
        __slots__ = ("group_id", "group_mbx_params", "restore_site_params")
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_MBX_PARAMS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        group_mbx_params: RestoreOutlookParams
        restore_site_params: RestoreSiteParams
        def __init__(self, group_id: _Optional[str] = ..., group_mbx_params: _Optional[_Union[RestoreOutlookParams, _Mapping]] = ..., restore_site_params: _Optional[_Union[RestoreSiteParams, _Mapping]] = ...) -> None: ...
    class MSGroupInfo(_message.Message):
        __slots__ = ("object", "is_full_group_required", "mailbox_restore_type", "site_restore_type", "group_granular_params")
        class RestoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFull: _ClassVar[RestoreO365GroupsParams.MSGroupInfo.RestoreType]
            kPartial: _ClassVar[RestoreO365GroupsParams.MSGroupInfo.RestoreType]
        kFull: RestoreO365GroupsParams.MSGroupInfo.RestoreType
        kPartial: RestoreO365GroupsParams.MSGroupInfo.RestoreType
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_GROUP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        MAILBOX_RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SITE_RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
        GROUP_GRANULAR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        object: RestoreObject
        is_full_group_required: bool
        mailbox_restore_type: RestoreO365GroupsParams.MSGroupInfo.RestoreType
        site_restore_type: RestoreO365GroupsParams.MSGroupInfo.RestoreType
        group_granular_params: RestoreO365GroupsParams.GroupGranularParams
        def __init__(self, object: _Optional[_Union[RestoreObject, _Mapping]] = ..., is_full_group_required: bool = ..., mailbox_restore_type: _Optional[_Union[RestoreO365GroupsParams.MSGroupInfo.RestoreType, str]] = ..., site_restore_type: _Optional[_Union[RestoreO365GroupsParams.MSGroupInfo.RestoreType, str]] = ..., group_granular_params: _Optional[_Union[RestoreO365GroupsParams.GroupGranularParams, _Mapping]] = ...) -> None: ...
    MS_GROUPS_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ORIGINAL_OWNERS_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ms_groups_vec: _containers.RepeatedCompositeFieldContainer[RestoreO365GroupsParams.MSGroupInfo]
    restore_to_original: bool
    target_group: str
    target_group_name: str
    target_group_owner: str
    create_new_group: bool
    restore_original_owners_members: bool
    def __init__(self, ms_groups_vec: _Optional[_Iterable[_Union[RestoreO365GroupsParams.MSGroupInfo, _Mapping]]] = ..., restore_to_original: bool = ..., target_group: _Optional[str] = ..., target_group_name: _Optional[str] = ..., target_group_owner: _Optional[str] = ..., create_new_group: bool = ..., restore_original_owners_members: bool = ...) -> None: ...

class RestoreKVMVMsParams(_message.Message):
    __slots__ = ("rename_restored_object_param", "restored_objects_network_config", "power_state_config", "cluster_entity", "datacenter_entity", "storagedomain_entity")
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECTS_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    STORAGEDOMAIN_ENTITY_FIELD_NUMBER: _ClassVar[int]
    rename_restored_object_param: RenameObjectParamProto
    restored_objects_network_config: RestoredObjectNetworkConfigProto
    power_state_config: PowerStateConfigProto
    cluster_entity: _entity_pb2.EntityProto
    datacenter_entity: _entity_pb2.EntityProto
    storagedomain_entity: _entity_pb2.EntityProto
    def __init__(self, rename_restored_object_param: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., restored_objects_network_config: _Optional[_Union[RestoredObjectNetworkConfigProto, _Mapping]] = ..., power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ..., cluster_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datacenter_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storagedomain_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class RestoreKubernetesNamespacesParams(_message.Message):
    __slots__ = ("rename_restored_object_param", "cluster_entity", "management_namespace", "backup_job_name", "backup_cluster_id", "pod_metadata_vec", "cluster_software_version", "is_protection_using_datamover_enabled", "s3_account_id", "init_container_image", "datamover_service_type", "vlan_params", "excluded_pvc_vec")
    RENAME_RESTORED_OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    POD_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_PROTECTION_USING_DATAMOVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    S3_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PVC_VEC_FIELD_NUMBER: _ClassVar[int]
    rename_restored_object_param: RenameObjectParamProto
    cluster_entity: _entity_pb2.EntityProto
    management_namespace: str
    backup_job_name: str
    backup_cluster_id: int
    pod_metadata_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_pb2.PodMetadata]
    cluster_software_version: str
    is_protection_using_datamover_enabled: bool
    s3_account_id: str
    init_container_image: str
    datamover_service_type: _kubernetes_pb2.ServiceType
    vlan_params: _common_pb2.VlanParams
    excluded_pvc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rename_restored_object_param: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., cluster_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., management_namespace: _Optional[str] = ..., backup_job_name: _Optional[str] = ..., backup_cluster_id: _Optional[int] = ..., pod_metadata_vec: _Optional[_Iterable[_Union[_kubernetes_pb2.PodMetadata, _Mapping]]] = ..., cluster_software_version: _Optional[str] = ..., is_protection_using_datamover_enabled: bool = ..., s3_account_id: _Optional[str] = ..., init_container_image: _Optional[str] = ..., datamover_service_type: _Optional[_Union[_kubernetes_pb2.ServiceType, str]] = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., excluded_pvc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ExternalSnapshotSource(_message.Message):
    __slots__ = ("entity_id", "job_id", "deletion_type")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DELETION_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    job_id: int
    deletion_type: _enums_pb2.ExternalSnapshotDeletionType.Type
    def __init__(self, entity_id: _Optional[int] = ..., job_id: _Optional[int] = ..., deletion_type: _Optional[_Union[_enums_pb2.ExternalSnapshotDeletionType.Type, str]] = ...) -> None: ...

class ExternalSnapshotInfo(_message.Message):
    __slots__ = ("entity_id", "snapshot_id_vec", "snapshot_time_usecs", "snapshot_removed", "job_id", "job_instance_id", "attempt_num", "task_id", "deletion_type", "expiry_time_usecs", "is_cloned_volume")
    Extensions: _python_message._ExtensionDict
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_REMOVED_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DELETION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_CLONED_VOLUME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_time_usecs: int
    snapshot_removed: bool
    job_id: int
    job_instance_id: int
    attempt_num: int
    task_id: int
    deletion_type: _enums_pb2.ExternalSnapshotDeletionType.Type
    expiry_time_usecs: int
    is_cloned_volume: bool
    def __init__(self, entity_id: _Optional[int] = ..., snapshot_id_vec: _Optional[_Iterable[str]] = ..., snapshot_time_usecs: _Optional[int] = ..., snapshot_removed: bool = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., task_id: _Optional[int] = ..., deletion_type: _Optional[_Union[_enums_pb2.ExternalSnapshotDeletionType.Type, str]] = ..., expiry_time_usecs: _Optional[int] = ..., is_cloned_volume: bool = ...) -> None: ...

class ConversionInfoProto(_message.Message):
    __slots__ = ("snapshot_info",)
    Extensions: _python_message._ExtensionDict
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: SnapshotInfoProto
    def __init__(self, snapshot_info: _Optional[_Union[SnapshotInfoProto, _Mapping]] = ...) -> None: ...

class DatastoreSpaceCheckProto(_message.Message):
    __slots__ = ("ds_space_check_state", "error")
    class DatastoreSpaceCheckState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPeriodicCheckInitialState: _ClassVar[DatastoreSpaceCheckProto.DatastoreSpaceCheckState]
        kReadyForPeriodicChecks: _ClassVar[DatastoreSpaceCheckProto.DatastoreSpaceCheckState]
        kPeriodicSpaceCheckFailed: _ClassVar[DatastoreSpaceCheckProto.DatastoreSpaceCheckState]
    kPeriodicCheckInitialState: DatastoreSpaceCheckProto.DatastoreSpaceCheckState
    kReadyForPeriodicChecks: DatastoreSpaceCheckProto.DatastoreSpaceCheckState
    kPeriodicSpaceCheckFailed: DatastoreSpaceCheckProto.DatastoreSpaceCheckState
    DS_SPACE_CHECK_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ds_space_check_state: DatastoreSpaceCheckProto.DatastoreSpaceCheckState
    error: _error_pb2.ErrorProto
    def __init__(self, ds_space_check_state: _Optional[_Union[DatastoreSpaceCheckProto.DatastoreSpaceCheckState, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AdditionalRunInfo(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class CloudDeployInfoProto(_message.Message):
    __slots__ = ("type", "cloud_deploy_entity_vec", "target_type", "restore_info", "total_bytes_transferred_to_source", "is_incremental", "warnings")
    Extensions: _python_message._ExtensionDict
    class CloudDeployEntity(_message.Message):
        __slots__ = ("entity", "status", "public_status", "relative_clone_paths", "previous_relative_clone_paths", "previous_relative_clone_dir_path", "error", "progress_monitor_task_path", "deployed_vm_name")
        Extensions: _python_message._ExtensionDict
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFilesCloned: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kFetchedEntityInfo: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kDataCopyStarted: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kInProgress: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kFinished: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kAborted: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
            kCancelled: _ClassVar[CloudDeployInfoProto.CloudDeployEntity.Status]
        kFilesCloned: CloudDeployInfoProto.CloudDeployEntity.Status
        kFetchedEntityInfo: CloudDeployInfoProto.CloudDeployEntity.Status
        kDataCopyStarted: CloudDeployInfoProto.CloudDeployEntity.Status
        kInProgress: CloudDeployInfoProto.CloudDeployEntity.Status
        kFinished: CloudDeployInfoProto.CloudDeployEntity.Status
        kAborted: CloudDeployInfoProto.CloudDeployEntity.Status
        kCancelled: CloudDeployInfoProto.CloudDeployEntity.Status
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONE_PATHS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_RELATIVE_CLONE_PATHS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_RELATIVE_CLONE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        DEPLOYED_VM_NAME_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        status: CloudDeployInfoProto.CloudDeployEntity.Status
        public_status: _enums_pb2.PublicTaskStatus.Type
        relative_clone_paths: _containers.RepeatedScalarFieldContainer[str]
        previous_relative_clone_paths: _containers.RepeatedScalarFieldContainer[str]
        previous_relative_clone_dir_path: str
        error: _error_pb2.ErrorProto
        progress_monitor_task_path: str
        deployed_vm_name: str
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., status: _Optional[_Union[CloudDeployInfoProto.CloudDeployEntity.Status, str]] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., relative_clone_paths: _Optional[_Iterable[str]] = ..., previous_relative_clone_paths: _Optional[_Iterable[str]] = ..., previous_relative_clone_dir_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., deployed_vm_name: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TRANSFERRED_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    cloud_deploy_entity_vec: _containers.RepeatedCompositeFieldContainer[CloudDeployInfoProto.CloudDeployEntity]
    target_type: _enums_pb2.TargetType.Type
    restore_info: RestoreInfoProto
    total_bytes_transferred_to_source: int
    is_incremental: bool
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., cloud_deploy_entity_vec: _Optional[_Iterable[_Union[CloudDeployInfoProto.CloudDeployEntity, _Mapping]]] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., restore_info: _Optional[_Union[RestoreInfoProto, _Mapping]] = ..., total_bytes_transferred_to_source: _Optional[int] = ..., is_incremental: bool = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class VirtualDiskHydrationInfo(_message.Message):
    __slots__ = ("uuid", "key", "file_name", "capacity", "start_sequence_number", "last_applied_sequence_number", "delete_disk", "update_disk_info", "log_data_vec")
    class UpdateDiskInfo(_message.Message):
        __slots__ = ("capacity",)
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        capacity: int
        def __init__(self, capacity: _Optional[int] = ...) -> None: ...
    class LogData(_message.Message):
        __slots__ = ("full_path", "start_seq_number", "end_seq_number", "logical_size_bytes", "is_journal_sharded")
        FULL_PATH_FIELD_NUMBER: _ClassVar[int]
        START_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        END_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
        full_path: str
        start_seq_number: _event_pb2.Sequencer
        end_seq_number: _event_pb2.Sequencer
        logical_size_bytes: int
        is_journal_sharded: bool
        def __init__(self, full_path: _Optional[str] = ..., start_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., is_journal_sharded: bool = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    START_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LAST_APPLIED_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DELETE_DISK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    key: int
    file_name: str
    capacity: int
    start_sequence_number: _event_pb2.Sequencer
    last_applied_sequence_number: _event_pb2.Sequencer
    delete_disk: bool
    update_disk_info: VirtualDiskHydrationInfo.UpdateDiskInfo
    log_data_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskHydrationInfo.LogData]
    def __init__(self, uuid: _Optional[str] = ..., key: _Optional[int] = ..., file_name: _Optional[str] = ..., capacity: _Optional[int] = ..., start_sequence_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., last_applied_sequence_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., delete_disk: bool = ..., update_disk_info: _Optional[_Union[VirtualDiskHydrationInfo.UpdateDiskInfo, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[VirtualDiskHydrationInfo.LogData, _Mapping]]] = ...) -> None: ...

class CDPRestoreParams(_message.Message):
    __slots__ = ("restore_time_usecs", "virtual_disk_vec", "backup_view_dir", "relative_snapshot_dir", "base_backup_run_start_time_usecs", "cdp_hydration_task_id", "hydration_version", "restore_type")
    RESTORE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_DIR_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CDP_HYDRATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    restore_time_usecs: int
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskHydrationInfo]
    backup_view_dir: str
    relative_snapshot_dir: str
    base_backup_run_start_time_usecs: int
    cdp_hydration_task_id: int
    hydration_version: _common_pb2.CDPHydrationVersion
    restore_type: RestoreType.Type
    def __init__(self, restore_time_usecs: _Optional[int] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDiskHydrationInfo, _Mapping]]] = ..., backup_view_dir: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., base_backup_run_start_time_usecs: _Optional[int] = ..., cdp_hydration_task_id: _Optional[int] = ..., hydration_version: _Optional[_Union[_common_pb2.CDPHydrationVersion, str]] = ..., restore_type: _Optional[_Union[RestoreType.Type, str]] = ...) -> None: ...

class DataProtectionEventProto(_message.Message):
    __slots__ = ("timestamp_usecs", "event_type", "backup_job_proto_DEPRECATED", "env_type", "registered_source", "restore_target", "entities", "error", "task_id", "replication_target", "archival_target", "attribute_map")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackup: _ClassVar[DataProtectionEventProto.EventType]
        kRestore: _ClassVar[DataProtectionEventProto.EventType]
        kArchival: _ClassVar[DataProtectionEventProto.EventType]
        kReplication: _ClassVar[DataProtectionEventProto.EventType]
    kBackup: DataProtectionEventProto.EventType
    kRestore: DataProtectionEventProto.EventType
    kArchival: DataProtectionEventProto.EventType
    kReplication: DataProtectionEventProto.EventType
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_PROTO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    event_type: DataProtectionEventProto.EventType
    backup_job_proto_DEPRECATED: BackupJobProto
    env_type: _enums_pb2.Environment.Type
    registered_source: _entity_pb2.EntityProto
    restore_target: _entity_pb2.EntityProto
    entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    error: _error_pb2.ErrorProto
    task_id: int
    replication_target: _policy_pb2.ReplicationTarget
    archival_target: _policy_pb2.ArchivalTarget
    attribute_map: _containers.RepeatedCompositeFieldContainer[DataProtectionEventProto.KeyValuePair]
    def __init__(self, timestamp_usecs: _Optional[int] = ..., event_type: _Optional[_Union[DataProtectionEventProto.EventType, str]] = ..., backup_job_proto_DEPRECATED: _Optional[_Union[BackupJobProto, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_target: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_id: _Optional[int] = ..., replication_target: _Optional[_Union[_policy_pb2.ReplicationTarget, _Mapping]] = ..., archival_target: _Optional[_Union[_policy_pb2.ArchivalTarget, _Mapping]] = ..., attribute_map: _Optional[_Iterable[_Union[DataProtectionEventProto.KeyValuePair, _Mapping]]] = ...) -> None: ...

class SyslogFormattedDataProtectionEventProto(_message.Message):
    __slots__ = ("event_message", "timestamp", "cluster_info", "event_type", "env_type", "registered_source", "restore_target", "backup_job_name", "backup_job_id", "entities", "error", "task_id", "replication_target", "archival_target", "attribute_map")
    class ClusterInfo(_message.Message):
        __slots__ = ("cluster_id", "cluster_name")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_id: str
        cluster_name: str
        def __init__(self, cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ...) -> None: ...
    class Entity(_message.Message):
        __slots__ = ("entity_type", "entity_id", "entity_name")
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        entity_type: str
        entity_id: str
        entity_name: str
        def __init__(self, entity_type: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...
    class Error(_message.Message):
        __slots__ = ("error_code", "error_message")
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_code: str
        error_message: str
        def __init__(self, error_code: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...
    class ArchivalTargetInfo(_message.Message):
        __slots__ = ("type", "name")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        type: str
        name: str
        def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TARGET_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    event_message: str
    timestamp: str
    cluster_info: SyslogFormattedDataProtectionEventProto.ClusterInfo
    event_type: str
    env_type: str
    registered_source: SyslogFormattedDataProtectionEventProto.Entity
    restore_target: SyslogFormattedDataProtectionEventProto.Entity
    backup_job_name: str
    backup_job_id: str
    entities: _containers.RepeatedCompositeFieldContainer[SyslogFormattedDataProtectionEventProto.Entity]
    error: SyslogFormattedDataProtectionEventProto.Error
    task_id: str
    replication_target: SyslogFormattedDataProtectionEventProto.ClusterInfo
    archival_target: SyslogFormattedDataProtectionEventProto.ArchivalTargetInfo
    attribute_map: _containers.RepeatedCompositeFieldContainer[SyslogFormattedDataProtectionEventProto.KeyValuePair]
    def __init__(self, event_message: _Optional[str] = ..., timestamp: _Optional[str] = ..., cluster_info: _Optional[_Union[SyslogFormattedDataProtectionEventProto.ClusterInfo, _Mapping]] = ..., event_type: _Optional[str] = ..., env_type: _Optional[str] = ..., registered_source: _Optional[_Union[SyslogFormattedDataProtectionEventProto.Entity, _Mapping]] = ..., restore_target: _Optional[_Union[SyslogFormattedDataProtectionEventProto.Entity, _Mapping]] = ..., backup_job_name: _Optional[str] = ..., backup_job_id: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[SyslogFormattedDataProtectionEventProto.Entity, _Mapping]]] = ..., error: _Optional[_Union[SyslogFormattedDataProtectionEventProto.Error, _Mapping]] = ..., task_id: _Optional[str] = ..., replication_target: _Optional[_Union[SyslogFormattedDataProtectionEventProto.ClusterInfo, _Mapping]] = ..., archival_target: _Optional[_Union[SyslogFormattedDataProtectionEventProto.ArchivalTargetInfo, _Mapping]] = ..., attribute_map: _Optional[_Iterable[_Union[SyslogFormattedDataProtectionEventProto.KeyValuePair, _Mapping]]] = ...) -> None: ...

class SourceFilters(_message.Message):
    __slots__ = ("exclude_source_filter_vec",)
    class SourceFilter(_message.Message):
        __slots__ = ("source_filter", "is_regex", "case_sensitive")
        SOURCE_FILTER_FIELD_NUMBER: _ClassVar[int]
        IS_REGEX_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        source_filter: str
        is_regex: bool
        case_sensitive: bool
        def __init__(self, source_filter: _Optional[str] = ..., is_regex: bool = ..., case_sensitive: bool = ...) -> None: ...
    EXCLUDE_SOURCE_FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
    exclude_source_filter_vec: _containers.RepeatedCompositeFieldContainer[SourceFilters.SourceFilter]
    def __init__(self, exclude_source_filter_vec: _Optional[_Iterable[_Union[SourceFilters.SourceFilter, _Mapping]]] = ...) -> None: ...

class SourceFiltersResult(_message.Message):
    __slots__ = ("excluded_entity_id_vec",)
    EXCLUDED_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    excluded_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, excluded_entity_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class VMwareStandbyResource(_message.Message):
    __slots__ = ("rename_object_params", "parent_source", "target_vm_folder", "resource_pool_entity", "datastore_entity_vec", "network_config", "target_datastore_folder")
    RENAME_OBJECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_VM_FOLDER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATASTORE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    rename_object_params: RenameObjectParamProto
    parent_source: _entity_pb2.EntityProto
    target_vm_folder: _entity_pb2.EntityProto
    resource_pool_entity: _entity_pb2.EntityProto
    datastore_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    network_config: RestoredObjectNetworkConfigProto
    target_datastore_folder: _entity_pb2.EntityProto
    def __init__(self, rename_object_params: _Optional[_Union[RenameObjectParamProto, _Mapping]] = ..., parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_vm_folder: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datastore_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., network_config: _Optional[_Union[RestoredObjectNetworkConfigProto, _Mapping]] = ..., target_datastore_folder: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class StandbyResource(_message.Message):
    __slots__ = ("recovery_point_objective_secs", "vmware_standby_resource")
    RECOVERY_POINT_OBJECTIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_STANDBY_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    recovery_point_objective_secs: int
    vmware_standby_resource: VMwareStandbyResource
    def __init__(self, recovery_point_objective_secs: _Optional[int] = ..., vmware_standby_resource: _Optional[_Union[VMwareStandbyResource, _Mapping]] = ...) -> None: ...

class MultiStageRestoreAction(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[MultiStageRestoreAction.Type]
        kCreate: _ClassVar[MultiStageRestoreAction.Type]
        kUpdate: _ClassVar[MultiStageRestoreAction.Type]
        kFinalize: _ClassVar[MultiStageRestoreAction.Type]
    kNone: MultiStageRestoreAction.Type
    kCreate: MultiStageRestoreAction.Type
    kUpdate: MultiStageRestoreAction.Type
    kFinalize: MultiStageRestoreAction.Type
    class FinalizeParams(_message.Message):
        __slots__ = ("target_power_state_config", "source_power_state_config")
        TARGET_POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SOURCE_POWER_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        target_power_state_config: PowerStateConfigProto
        source_power_state_config: PowerStateConfigProto
        def __init__(self, target_power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ..., source_power_state_config: _Optional[_Union[PowerStateConfigProto, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: MultiStageRestoreAction.Type
    def __init__(self, type: _Optional[_Union[MultiStageRestoreAction.Type, str]] = ...) -> None: ...

class UpdateRestoreTaskOptions(_message.Message):
    __slots__ = ("multi_stage_restore_action", "multi_stage_restore_finalize_action_params")
    MULTI_STAGE_RESTORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_FINALIZE_ACTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    multi_stage_restore_action: MultiStageRestoreAction.Type
    multi_stage_restore_finalize_action_params: MultiStageRestoreAction.FinalizeParams
    def __init__(self, multi_stage_restore_action: _Optional[_Union[MultiStageRestoreAction.Type, str]] = ..., multi_stage_restore_finalize_action_params: _Optional[_Union[MultiStageRestoreAction.FinalizeParams, _Mapping]] = ...) -> None: ...

class MagnetoConfigProto(_message.Message):
    __slots__ = ("gandalf_master_key", "gandalf_throttling_policies_key", "lookup_master_url", "create_or_update_protection_policy_url", "get_protection_policies_url", "get_protection_policy_summary_url", "create_backup_job_url", "update_backup_job_url", "cancel_protection_job_run_url", "run_backup_job_once_url", "get_backup_job_summary_url", "get_backup_job_run_errors_url", "get_backup_job_runs_url", "get_backup_job_leaf_sources_url", "register_entity_url", "update_entity_url", "register_app_owner_url", "update_app_owner_url", "update_backup_run_url", "get_entity_hierarchy_url", "get_entities_url", "collect_source_diagnostics_url", "get_entity_ids_url", "get_backup_runs_for_source_url", "create_restore_task_url", "create_restore_app_task_url", "create_restore_multi_app_task_url", "modify_restore_task_url", "check_restore_app_task_url", "get_restore_app_time_ranges_url", "get_restore_points_for_time_range_url", "get_sql_aag_host_cluster_url", "get_restore_tasks_url", "destroy_clone_task_url", "get_restore_views_url", "get_job_audit_trail_url", "write_blob_url", "read_blob_url", "create_restore_files_task_url", "create_download_files_task_url", "upgrade_agent_url", "update_cdp_components_url", "get_permission_info_for_entities_url", "update_permission_info_for_entities_url", "get_entity_permission_infos_for_sids_url", "get_protection_info_for_entities_url", "resolve_entities_url", "cancel_restore_task_url", "get_summary_url", "get_virtual_disk_info_url", "get_cdp_info_url", "expand_sources_url", "get_standby_info_url", "internal_viewname_prefix", "download_target_viewname_prefix", "cdp_restore_target_viewname_prefix", "retrieve_archive_viewname_prefix", "get_gatekeeper_info_url", "execute_agent_action_url", "execute_runbook_action_url", "create_upgrade_task_url", "validate_entities_access_url", "get_upgrade_task_status_url", "cancel_upgrade_task_url", "master_status_page_url", "backup_job_status_page_url", "restore_task_status_page_url", "destroy_task_status_page_url", "sql_status_page_url", "entity_hierarchy_status_page_url", "restore_job_status_page_url", "windows_agent_flags_status_page_url", "storage_snapshot_tasks_status_page_url", "oracle_status_page_url", "backup_job_locks_status_page_url", "permissions_status_page_url", "gatekeeper_status_page_url", "app_clone_status_page_url", "replication_status_page_url", "archival_status_page_url", "cdp_status_page_url", "entity_range_status_page_url", "agent_status_page_url", "entity_provenance_status_page_url", "policy_status_page_url", "get_source_debug_logs_url", "failover_status_page_url", "o365_status_page_url", "get_oracle_restore_meta_info_url", "get_magneto_http_rpc_encryption_capability_url", "cloud_status_page_url", "scribe_runs_status_page_url", "yoda_reindex_url", "dump_checkpoint_state_url", "get_task_debug_logs_url", "standby_status_page_url", "object_protection_url", "copy_backup_run_url", "backup_job_task_status_page_url", "backup_job_run_status_page_url", "bridge_proxy_constituents_status_page_url", "copy_task_url", "get_file_restore_errors_url", "live_magneto_slaves_page_url", "verification_tasks_page_url", "conversion_tasks_page_url", "physical_backup_sources_page_url", "registered_agents_page_url", "get_restore_meta_data_ranges_url", "list_contents_url", "resource_manager_status_page_url", "admctl_status_page_url", "tenant_status_page_url", "get_restore_success_files_url", "get_backup_job_success_files_url", "source_status_page_url", "get_teams_channels_list_url", "gandalf_read_replica_master_key", "get_sfdc_records_url", "get_sfdc_dependent_objects_url", "get_sfdc_fields_list_url", "patch_entity_url", "get_scheduler_stats_url", "enable_cdp_url", "get_dataprotect_ssh_public_key_url", "oob_requests_status_page_url")
    GANDALF_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    GANDALF_THROTTLING_POLICIES_KEY_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_OR_UPDATE_PROTECTION_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_PROTECTION_POLICIES_URL_FIELD_NUMBER: _ClassVar[int]
    GET_PROTECTION_POLICY_SUMMARY_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_BACKUP_JOB_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BACKUP_JOB_URL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PROTECTION_JOB_RUN_URL_FIELD_NUMBER: _ClassVar[int]
    RUN_BACKUP_JOB_ONCE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_JOB_SUMMARY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_JOB_RUN_ERRORS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_JOB_RUNS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_JOB_LEAF_SOURCES_URL_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    REGISTER_APP_OWNER_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_APP_OWNER_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BACKUP_RUN_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_HIERARCHY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITIES_URL_FIELD_NUMBER: _ClassVar[int]
    COLLECT_SOURCE_DIAGNOSTICS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_IDS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_RUNS_FOR_SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_APP_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_MULTI_APP_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    MODIFY_RESTORE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESTORE_APP_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_APP_TIME_RANGES_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_POINTS_FOR_TIME_RANGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SQL_AAG_HOST_CLUSTER_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_TASKS_URL_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_VIEWS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_JOB_AUDIT_TRAIL_URL_FIELD_NUMBER: _ClassVar[int]
    WRITE_BLOB_URL_FIELD_NUMBER: _ClassVar[int]
    READ_BLOB_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_DOWNLOAD_FILES_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_AGENT_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CDP_COMPONENTS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_PERMISSION_INFO_FOR_ENTITIES_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PERMISSION_INFO_FOR_ENTITIES_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_PERMISSION_INFOS_FOR_SIDS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_PROTECTION_INFO_FOR_ENTITIES_URL_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_ENTITIES_URL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_RESTORE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SUMMARY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_VIRTUAL_DISK_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    GET_CDP_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    EXPAND_SOURCES_URL_FIELD_NUMBER: _ClassVar[int]
    GET_STANDBY_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEWNAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_TARGET_VIEWNAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_TARGET_VIEWNAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ARCHIVE_VIEWNAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_GATEKEEPER_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_AGENT_ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_RUNBOOK_ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_UPGRADE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ENTITIES_ACCESS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_UPGRADE_TASK_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_UPGRADE_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DESTROY_TASK_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SQL_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_AGENT_FLAGS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SNAPSHOT_TASKS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ORACLE_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_LOCKS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GATEKEEPER_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    APP_CLONE_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CDP_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RANGE_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROVENANCE_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    POLICY_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SOURCE_DEBUG_LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    O365_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ORACLE_RESTORE_META_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MAGNETO_HTTP_RPC_ENCRYPTION_CAPABILITY_URL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_RUNS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    YODA_REINDEX_URL_FIELD_NUMBER: _ClassVar[int]
    DUMP_CHECKPOINT_STATE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_TASK_DEBUG_LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROTECTION_URL_FIELD_NUMBER: _ClassVar[int]
    COPY_BACKUP_RUN_URL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_TASK_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_RUN_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_PROXY_CONSTITUENTS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    COPY_TASK_URL_FIELD_NUMBER: _ClassVar[int]
    GET_FILE_RESTORE_ERRORS_URL_FIELD_NUMBER: _ClassVar[int]
    LIVE_MAGNETO_SLAVES_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TASKS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TASKS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BACKUP_SOURCES_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AGENTS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_META_DATA_RANGES_URL_FIELD_NUMBER: _ClassVar[int]
    LIST_CONTENTS_URL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MANAGER_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ADMCTL_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    TENANT_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_SUCCESS_FILES_URL_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_JOB_SUCCESS_FILES_URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_TEAMS_CHANNELS_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    GANDALF_READ_REPLICA_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    GET_SFDC_RECORDS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SFDC_DEPENDENT_OBJECTS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SFDC_FIELDS_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    PATCH_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_SCHEDULER_STATS_URL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CDP_URL_FIELD_NUMBER: _ClassVar[int]
    GET_DATAPROTECT_SSH_PUBLIC_KEY_URL_FIELD_NUMBER: _ClassVar[int]
    OOB_REQUESTS_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_key: str
    gandalf_throttling_policies_key: str
    lookup_master_url: str
    create_or_update_protection_policy_url: str
    get_protection_policies_url: str
    get_protection_policy_summary_url: str
    create_backup_job_url: str
    update_backup_job_url: str
    cancel_protection_job_run_url: str
    run_backup_job_once_url: str
    get_backup_job_summary_url: str
    get_backup_job_run_errors_url: str
    get_backup_job_runs_url: str
    get_backup_job_leaf_sources_url: str
    register_entity_url: str
    update_entity_url: str
    register_app_owner_url: str
    update_app_owner_url: str
    update_backup_run_url: str
    get_entity_hierarchy_url: str
    get_entities_url: str
    collect_source_diagnostics_url: str
    get_entity_ids_url: str
    get_backup_runs_for_source_url: str
    create_restore_task_url: str
    create_restore_app_task_url: str
    create_restore_multi_app_task_url: str
    modify_restore_task_url: str
    check_restore_app_task_url: str
    get_restore_app_time_ranges_url: str
    get_restore_points_for_time_range_url: str
    get_sql_aag_host_cluster_url: str
    get_restore_tasks_url: str
    destroy_clone_task_url: str
    get_restore_views_url: str
    get_job_audit_trail_url: str
    write_blob_url: str
    read_blob_url: str
    create_restore_files_task_url: str
    create_download_files_task_url: str
    upgrade_agent_url: str
    update_cdp_components_url: str
    get_permission_info_for_entities_url: str
    update_permission_info_for_entities_url: str
    get_entity_permission_infos_for_sids_url: str
    get_protection_info_for_entities_url: str
    resolve_entities_url: str
    cancel_restore_task_url: str
    get_summary_url: str
    get_virtual_disk_info_url: str
    get_cdp_info_url: str
    expand_sources_url: str
    get_standby_info_url: str
    internal_viewname_prefix: str
    download_target_viewname_prefix: str
    cdp_restore_target_viewname_prefix: str
    retrieve_archive_viewname_prefix: str
    get_gatekeeper_info_url: str
    execute_agent_action_url: str
    execute_runbook_action_url: str
    create_upgrade_task_url: str
    validate_entities_access_url: str
    get_upgrade_task_status_url: str
    cancel_upgrade_task_url: str
    master_status_page_url: str
    backup_job_status_page_url: str
    restore_task_status_page_url: str
    destroy_task_status_page_url: str
    sql_status_page_url: str
    entity_hierarchy_status_page_url: str
    restore_job_status_page_url: str
    windows_agent_flags_status_page_url: str
    storage_snapshot_tasks_status_page_url: str
    oracle_status_page_url: str
    backup_job_locks_status_page_url: str
    permissions_status_page_url: str
    gatekeeper_status_page_url: str
    app_clone_status_page_url: str
    replication_status_page_url: str
    archival_status_page_url: str
    cdp_status_page_url: str
    entity_range_status_page_url: str
    agent_status_page_url: str
    entity_provenance_status_page_url: str
    policy_status_page_url: str
    get_source_debug_logs_url: str
    failover_status_page_url: str
    o365_status_page_url: str
    get_oracle_restore_meta_info_url: str
    get_magneto_http_rpc_encryption_capability_url: str
    cloud_status_page_url: str
    scribe_runs_status_page_url: str
    yoda_reindex_url: str
    dump_checkpoint_state_url: str
    get_task_debug_logs_url: str
    standby_status_page_url: str
    object_protection_url: str
    copy_backup_run_url: str
    backup_job_task_status_page_url: str
    backup_job_run_status_page_url: str
    bridge_proxy_constituents_status_page_url: str
    copy_task_url: str
    get_file_restore_errors_url: str
    live_magneto_slaves_page_url: str
    verification_tasks_page_url: str
    conversion_tasks_page_url: str
    physical_backup_sources_page_url: str
    registered_agents_page_url: str
    get_restore_meta_data_ranges_url: str
    list_contents_url: str
    resource_manager_status_page_url: str
    admctl_status_page_url: str
    tenant_status_page_url: str
    get_restore_success_files_url: str
    get_backup_job_success_files_url: str
    source_status_page_url: str
    get_teams_channels_list_url: str
    gandalf_read_replica_master_key: str
    get_sfdc_records_url: str
    get_sfdc_dependent_objects_url: str
    get_sfdc_fields_list_url: str
    patch_entity_url: str
    get_scheduler_stats_url: str
    enable_cdp_url: str
    get_dataprotect_ssh_public_key_url: str
    oob_requests_status_page_url: str
    def __init__(self, gandalf_master_key: _Optional[str] = ..., gandalf_throttling_policies_key: _Optional[str] = ..., lookup_master_url: _Optional[str] = ..., create_or_update_protection_policy_url: _Optional[str] = ..., get_protection_policies_url: _Optional[str] = ..., get_protection_policy_summary_url: _Optional[str] = ..., create_backup_job_url: _Optional[str] = ..., update_backup_job_url: _Optional[str] = ..., cancel_protection_job_run_url: _Optional[str] = ..., run_backup_job_once_url: _Optional[str] = ..., get_backup_job_summary_url: _Optional[str] = ..., get_backup_job_run_errors_url: _Optional[str] = ..., get_backup_job_runs_url: _Optional[str] = ..., get_backup_job_leaf_sources_url: _Optional[str] = ..., register_entity_url: _Optional[str] = ..., update_entity_url: _Optional[str] = ..., register_app_owner_url: _Optional[str] = ..., update_app_owner_url: _Optional[str] = ..., update_backup_run_url: _Optional[str] = ..., get_entity_hierarchy_url: _Optional[str] = ..., get_entities_url: _Optional[str] = ..., collect_source_diagnostics_url: _Optional[str] = ..., get_entity_ids_url: _Optional[str] = ..., get_backup_runs_for_source_url: _Optional[str] = ..., create_restore_task_url: _Optional[str] = ..., create_restore_app_task_url: _Optional[str] = ..., create_restore_multi_app_task_url: _Optional[str] = ..., modify_restore_task_url: _Optional[str] = ..., check_restore_app_task_url: _Optional[str] = ..., get_restore_app_time_ranges_url: _Optional[str] = ..., get_restore_points_for_time_range_url: _Optional[str] = ..., get_sql_aag_host_cluster_url: _Optional[str] = ..., get_restore_tasks_url: _Optional[str] = ..., destroy_clone_task_url: _Optional[str] = ..., get_restore_views_url: _Optional[str] = ..., get_job_audit_trail_url: _Optional[str] = ..., write_blob_url: _Optional[str] = ..., read_blob_url: _Optional[str] = ..., create_restore_files_task_url: _Optional[str] = ..., create_download_files_task_url: _Optional[str] = ..., upgrade_agent_url: _Optional[str] = ..., update_cdp_components_url: _Optional[str] = ..., get_permission_info_for_entities_url: _Optional[str] = ..., update_permission_info_for_entities_url: _Optional[str] = ..., get_entity_permission_infos_for_sids_url: _Optional[str] = ..., get_protection_info_for_entities_url: _Optional[str] = ..., resolve_entities_url: _Optional[str] = ..., cancel_restore_task_url: _Optional[str] = ..., get_summary_url: _Optional[str] = ..., get_virtual_disk_info_url: _Optional[str] = ..., get_cdp_info_url: _Optional[str] = ..., expand_sources_url: _Optional[str] = ..., get_standby_info_url: _Optional[str] = ..., internal_viewname_prefix: _Optional[str] = ..., download_target_viewname_prefix: _Optional[str] = ..., cdp_restore_target_viewname_prefix: _Optional[str] = ..., retrieve_archive_viewname_prefix: _Optional[str] = ..., get_gatekeeper_info_url: _Optional[str] = ..., execute_agent_action_url: _Optional[str] = ..., execute_runbook_action_url: _Optional[str] = ..., create_upgrade_task_url: _Optional[str] = ..., validate_entities_access_url: _Optional[str] = ..., get_upgrade_task_status_url: _Optional[str] = ..., cancel_upgrade_task_url: _Optional[str] = ..., master_status_page_url: _Optional[str] = ..., backup_job_status_page_url: _Optional[str] = ..., restore_task_status_page_url: _Optional[str] = ..., destroy_task_status_page_url: _Optional[str] = ..., sql_status_page_url: _Optional[str] = ..., entity_hierarchy_status_page_url: _Optional[str] = ..., restore_job_status_page_url: _Optional[str] = ..., windows_agent_flags_status_page_url: _Optional[str] = ..., storage_snapshot_tasks_status_page_url: _Optional[str] = ..., oracle_status_page_url: _Optional[str] = ..., backup_job_locks_status_page_url: _Optional[str] = ..., permissions_status_page_url: _Optional[str] = ..., gatekeeper_status_page_url: _Optional[str] = ..., app_clone_status_page_url: _Optional[str] = ..., replication_status_page_url: _Optional[str] = ..., archival_status_page_url: _Optional[str] = ..., cdp_status_page_url: _Optional[str] = ..., entity_range_status_page_url: _Optional[str] = ..., agent_status_page_url: _Optional[str] = ..., entity_provenance_status_page_url: _Optional[str] = ..., policy_status_page_url: _Optional[str] = ..., get_source_debug_logs_url: _Optional[str] = ..., failover_status_page_url: _Optional[str] = ..., o365_status_page_url: _Optional[str] = ..., get_oracle_restore_meta_info_url: _Optional[str] = ..., get_magneto_http_rpc_encryption_capability_url: _Optional[str] = ..., cloud_status_page_url: _Optional[str] = ..., scribe_runs_status_page_url: _Optional[str] = ..., yoda_reindex_url: _Optional[str] = ..., dump_checkpoint_state_url: _Optional[str] = ..., get_task_debug_logs_url: _Optional[str] = ..., standby_status_page_url: _Optional[str] = ..., object_protection_url: _Optional[str] = ..., copy_backup_run_url: _Optional[str] = ..., backup_job_task_status_page_url: _Optional[str] = ..., backup_job_run_status_page_url: _Optional[str] = ..., bridge_proxy_constituents_status_page_url: _Optional[str] = ..., copy_task_url: _Optional[str] = ..., get_file_restore_errors_url: _Optional[str] = ..., live_magneto_slaves_page_url: _Optional[str] = ..., verification_tasks_page_url: _Optional[str] = ..., conversion_tasks_page_url: _Optional[str] = ..., physical_backup_sources_page_url: _Optional[str] = ..., registered_agents_page_url: _Optional[str] = ..., get_restore_meta_data_ranges_url: _Optional[str] = ..., list_contents_url: _Optional[str] = ..., resource_manager_status_page_url: _Optional[str] = ..., admctl_status_page_url: _Optional[str] = ..., tenant_status_page_url: _Optional[str] = ..., get_restore_success_files_url: _Optional[str] = ..., get_backup_job_success_files_url: _Optional[str] = ..., source_status_page_url: _Optional[str] = ..., get_teams_channels_list_url: _Optional[str] = ..., gandalf_read_replica_master_key: _Optional[str] = ..., get_sfdc_records_url: _Optional[str] = ..., get_sfdc_dependent_objects_url: _Optional[str] = ..., get_sfdc_fields_list_url: _Optional[str] = ..., patch_entity_url: _Optional[str] = ..., get_scheduler_stats_url: _Optional[str] = ..., enable_cdp_url: _Optional[str] = ..., get_dataprotect_ssh_public_key_url: _Optional[str] = ..., oob_requests_status_page_url: _Optional[str] = ...) -> None: ...

class UdaBackupParams(_message.Message):
    __slots__ = ("registered_entity_uda_params", "is_full_backup", "retention_mins", "parent_entities", "run_params", "disk_attach_params")
    REGISTERED_ENTITY_UDA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MINS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    RUN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DISK_ATTACH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    registered_entity_uda_params: RegisteredEntityUdaParams
    is_full_backup: bool
    retention_mins: int
    parent_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    run_params: UdaBackupRunParams
    disk_attach_params: DiskAttachParams
    def __init__(self, registered_entity_uda_params: _Optional[_Union[RegisteredEntityUdaParams, _Mapping]] = ..., is_full_backup: bool = ..., retention_mins: _Optional[int] = ..., parent_entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., run_params: _Optional[_Union[UdaBackupRunParams, _Mapping]] = ..., disk_attach_params: _Optional[_Union[DiskAttachParams, _Mapping]] = ...) -> None: ...

class UdaBackupRunParams(_message.Message):
    __slots__ = ("et_run_params",)
    class UdaExternallyTriggeredRunParams(_message.Message):
        __slots__ = ("et_run_id", "control_node", "args_map")
        class ArgsMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _uda_pb2.UdaCustomArgument
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_uda_pb2.UdaCustomArgument, _Mapping]] = ...) -> None: ...
        ET_RUN_ID_FIELD_NUMBER: _ClassVar[int]
        CONTROL_NODE_FIELD_NUMBER: _ClassVar[int]
        ARGS_MAP_FIELD_NUMBER: _ClassVar[int]
        et_run_id: str
        control_node: str
        args_map: _containers.MessageMap[str, _uda_pb2.UdaCustomArgument]
        def __init__(self, et_run_id: _Optional[str] = ..., control_node: _Optional[str] = ..., args_map: _Optional[_Mapping[str, _uda_pb2.UdaCustomArgument]] = ...) -> None: ...
    ET_RUN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    et_run_params: UdaBackupRunParams.UdaExternallyTriggeredRunParams
    def __init__(self, et_run_params: _Optional[_Union[UdaBackupRunParams.UdaExternallyTriggeredRunParams, _Mapping]] = ...) -> None: ...

class ExternallyTriggeredBackupParams(_message.Message):
    __slots__ = ("tag", "job_instance_start_time")
    TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    tag: str
    job_instance_start_time: int
    def __init__(self, tag: _Optional[str] = ..., job_instance_start_time: _Optional[int] = ...) -> None: ...

class CassandraBackupParams(_message.Message):
    __slots__ = ("run_params",)
    RUN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    run_params: CassandraBackupRunParams
    def __init__(self, run_params: _Optional[_Union[CassandraBackupRunParams, _Mapping]] = ...) -> None: ...

class CassandraBackupRunParams(_message.Message):
    __slots__ = ("set_primary_for_log",)
    SET_PRIMARY_FOR_LOG_FIELD_NUMBER: _ClassVar[int]
    set_primary_for_log: bool
    def __init__(self, set_primary_for_log: bool = ...) -> None: ...

class DiskAttachParams(_message.Message):
    __slots__ = ("azure_disk", "vm_instance_id_str", "size")
    AZURE_DISK_FIELD_NUMBER: _ClassVar[int]
    VM_INSTANCE_ID_STR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    azure_disk: _azure_pb2.AzureDisk.Type
    vm_instance_id_str: str
    size: int
    def __init__(self, azure_disk: _Optional[_Union[_azure_pb2.AzureDisk.Type, str]] = ..., vm_instance_id_str: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class PersistError(_message.Message):
    __slots__ = ("error", "timestamp", "action_item")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    timestamp: int
    action_item: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., action_item: _Optional[str] = ...) -> None: ...

class RegisteredEntityKubernetesParams(_message.Message):
    __slots__ = ("datamover_image_location", "velero_image_location", "velero_aws_plugin_image_location", "init_container_image_location", "s3_account_id", "velero_openshift_plugin_image_location", "distribution", "datamover_service_type", "default_vlan_params", "vlan_info_vec", "service_annotations", "tolerations_vec")
    class ServiceAnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATAMOVER_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_AWS_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INIT_CONTAINER_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    S3_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VELERO_OPENSHIFT_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    datamover_image_location: str
    velero_image_location: str
    velero_aws_plugin_image_location: str
    init_container_image_location: str
    s3_account_id: str
    velero_openshift_plugin_image_location: str
    distribution: _kubernetes_pb2.Entity.Distribution
    datamover_service_type: _kubernetes_pb2.ServiceType
    default_vlan_params: _common_pb2.VlanParams
    vlan_info_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_pb2.VlanInfo]
    service_annotations: _containers.ScalarMap[str, str]
    tolerations_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration]
    def __init__(self, datamover_image_location: _Optional[str] = ..., velero_image_location: _Optional[str] = ..., velero_aws_plugin_image_location: _Optional[str] = ..., init_container_image_location: _Optional[str] = ..., s3_account_id: _Optional[str] = ..., velero_openshift_plugin_image_location: _Optional[str] = ..., distribution: _Optional[_Union[_kubernetes_pb2.Entity.Distribution, str]] = ..., datamover_service_type: _Optional[_Union[_kubernetes_pb2.ServiceType, str]] = ..., default_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., vlan_info_vec: _Optional[_Iterable[_Union[_kubernetes_pb2.VlanInfo, _Mapping]]] = ..., service_annotations: _Optional[_Mapping[str, str]] = ..., tolerations_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration, _Mapping]]] = ...) -> None: ...

class O365TeamsChannel(_message.Message):
    __slots__ = ("name", "is_private")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_private: bool
    def __init__(self, name: _Optional[str] = ..., is_private: bool = ...) -> None: ...

class O365TeamsChannelsList(_message.Message):
    __slots__ = ("id", "channels_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_LIST_FIELD_NUMBER: _ClassVar[int]
    id: str
    channels_list: _containers.RepeatedCompositeFieldContainer[O365TeamsChannel]
    def __init__(self, id: _Optional[str] = ..., channels_list: _Optional[_Iterable[_Union[O365TeamsChannel, _Mapping]]] = ...) -> None: ...

class RestoreS3Params(_message.Message):
    __slots__ = ("is_original_location", "overwrite_objects_in_bucket", "preserve_object_attributes", "object_prefix", "new_location_params", "prefixes_to_recover")
    class NewLocationParams(_message.Message):
        __slots__ = ("region", "s3_bucket")
        REGION_FIELD_NUMBER: _ClassVar[int]
        S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
        region: _entity_pb2.EntityProto
        s3_bucket: _entity_pb2.EntityProto
        def __init__(self, region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., s3_bucket: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    IS_ORIGINAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_OBJECTS_IN_BUCKET_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_OBJECT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NEW_LOCATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_TO_RECOVER_FIELD_NUMBER: _ClassVar[int]
    is_original_location: bool
    overwrite_objects_in_bucket: bool
    preserve_object_attributes: bool
    object_prefix: str
    new_location_params: RestoreS3Params.NewLocationParams
    prefixes_to_recover: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_original_location: bool = ..., overwrite_objects_in_bucket: bool = ..., preserve_object_attributes: bool = ..., object_prefix: _Optional[str] = ..., new_location_params: _Optional[_Union[RestoreS3Params.NewLocationParams, _Mapping]] = ..., prefixes_to_recover: _Optional[_Iterable[str]] = ...) -> None: ...

class DownloadChatsParams(_message.Message):
    __slots__ = ("html_template", "channel_ids_vec", "download_file_type")
    class DownloadFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHTML: _ClassVar[DownloadChatsParams.DownloadFileType]
        kJSON: _ClassVar[DownloadChatsParams.DownloadFileType]
    kHTML: DownloadChatsParams.DownloadFileType
    kJSON: DownloadChatsParams.DownloadFileType
    HTML_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    html_template: str
    channel_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    download_file_type: DownloadChatsParams.DownloadFileType
    def __init__(self, html_template: _Optional[str] = ..., channel_ids_vec: _Optional[_Iterable[str]] = ..., download_file_type: _Optional[_Union[DownloadChatsParams.DownloadFileType, str]] = ...) -> None: ...

class UpdateConnectionParams(_message.Message):
    __slots__ = ("min_connections_requested", "max_connections_requested", "connections_to_release")
    MIN_CONNECTIONS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    MAX_CONNECTIONS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_TO_RELEASE_FIELD_NUMBER: _ClassVar[int]
    min_connections_requested: int
    max_connections_requested: int
    connections_to_release: int
    def __init__(self, min_connections_requested: _Optional[int] = ..., max_connections_requested: _Optional[int] = ..., connections_to_release: _Optional[int] = ...) -> None: ...

class RestoreSanParams(_message.Message):
    __slots__ = ("storage_pool", "transport_mode", "use_thin_clone")
    class TransportMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreferFc: _ClassVar[RestoreSanParams.TransportMode]
        kIscsiOnly: _ClassVar[RestoreSanParams.TransportMode]
    kPreferFc: RestoreSanParams.TransportMode
    kIscsiOnly: RestoreSanParams.TransportMode
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_THIN_CLONE_FIELD_NUMBER: _ClassVar[int]
    storage_pool: _entity_pb2.EntityProto
    transport_mode: RestoreSanParams.TransportMode
    use_thin_clone: bool
    def __init__(self, storage_pool: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., transport_mode: _Optional[_Union[RestoreSanParams.TransportMode, str]] = ..., use_thin_clone: bool = ...) -> None: ...

class MaintenanceModeConfigProto(_message.Message):
    __slots__ = ("workflow_intervention_spec_vec", "activation_time_intervals", "maintenance_schedule", "user_message")
    class Intervention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownIntervention: _ClassVar[MaintenanceModeConfigProto.Intervention]
        kNoIntervention: _ClassVar[MaintenanceModeConfigProto.Intervention]
        kCancel: _ClassVar[MaintenanceModeConfigProto.Intervention]
    kUnknownIntervention: MaintenanceModeConfigProto.Intervention
    kNoIntervention: MaintenanceModeConfigProto.Intervention
    kCancel: MaintenanceModeConfigProto.Intervention
    class WorkflowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownType: _ClassVar[MaintenanceModeConfigProto.WorkflowType]
        kBackupRun: _ClassVar[MaintenanceModeConfigProto.WorkflowType]
    kUnknownType: MaintenanceModeConfigProto.WorkflowType
    kBackupRun: MaintenanceModeConfigProto.WorkflowType
    class WorkflowInterventionSpec(_message.Message):
        __slots__ = ("workflow_type", "intervention")
        WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
        INTERVENTION_FIELD_NUMBER: _ClassVar[int]
        workflow_type: MaintenanceModeConfigProto.WorkflowType
        intervention: MaintenanceModeConfigProto.Intervention
        def __init__(self, workflow_type: _Optional[_Union[MaintenanceModeConfigProto.WorkflowType, str]] = ..., intervention: _Optional[_Union[MaintenanceModeConfigProto.Intervention, str]] = ...) -> None: ...
    WORKFLOW_INTERVENTION_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TIME_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    workflow_intervention_spec_vec: _containers.RepeatedCompositeFieldContainer[MaintenanceModeConfigProto.WorkflowInterventionSpec]
    activation_time_intervals: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.TimeRangeUsecs]
    maintenance_schedule: _schedule_pb2.ScheduleProto
    user_message: str
    def __init__(self, workflow_intervention_spec_vec: _Optional[_Iterable[_Union[MaintenanceModeConfigProto.WorkflowInterventionSpec, _Mapping]]] = ..., activation_time_intervals: _Optional[_Iterable[_Union[_schedule_pb2.TimeRangeUsecs, _Mapping]]] = ..., maintenance_schedule: _Optional[_Union[_schedule_pb2.ScheduleProto, _Mapping]] = ..., user_message: _Optional[str] = ...) -> None: ...
