from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TenantStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Active: _ClassVar[TenantStatus]
    Inactive: _ClassVar[TenantStatus]
    MarkedForDeletion: _ClassVar[TenantStatus]
    Deleted: _ClassVar[TenantStatus]
    Unregistered: _ClassVar[TenantStatus]

class ClusterScalingRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[ClusterScalingRequestType]
    READ_ONLY_MODE: _ClassVar[ClusterScalingRequestType]
    CLEAR_CACHE: _ClassVar[ClusterScalingRequestType]
    UPDATE_CLUSTER_CONFIG: _ClassVar[ClusterScalingRequestType]
    GET_RSS_MEM: _ClassVar[ClusterScalingRequestType]
    SWITCH_MASTERSHIP: _ClassVar[ClusterScalingRequestType]
Active: TenantStatus
Inactive: TenantStatus
MarkedForDeletion: TenantStatus
Deleted: TenantStatus
Unregistered: TenantStatus
INVALID: ClusterScalingRequestType
READ_ONLY_MODE: ClusterScalingRequestType
CLEAR_CACHE: ClusterScalingRequestType
UPDATE_CLUSTER_CONFIG: ClusterScalingRequestType
GET_RSS_MEM: ClusterScalingRequestType
SWITCH_MASTERSHIP: ClusterScalingRequestType

class ClusterIdentifier(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id", "rigel_guid", "global_tenant_id", "rigel_connector_group_id")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    rigel_guid: int
    global_tenant_id: str
    rigel_connector_group_id: int
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., rigel_guid: _Optional[int] = ..., global_tenant_id: _Optional[str] = ..., rigel_connector_group_id: _Optional[int] = ...) -> None: ...

class ClusterIdentifierList(_message.Message):
    __slots__ = ("cluster_identifiers",)
    CLUSTER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    cluster_identifiers: _containers.RepeatedCompositeFieldContainer[ClusterIdentifier]
    def __init__(self, cluster_identifiers: _Optional[_Iterable[_Union[ClusterIdentifier, _Mapping]]] = ...) -> None: ...

class ControlPlaneApiRequest(_message.Message):
    __slots__ = ("cluster_identifier", "request")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    request: bytes
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., request: _Optional[bytes] = ...) -> None: ...

class ControlPlaneApiResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: bytes
    def __init__(self, response: _Optional[bytes] = ...) -> None: ...

class IrisDataCollectorResponse(_message.Message):
    __slots__ = ("cluster_identifier", "iris_data", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IRIS_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    iris_data: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., iris_data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendIrisCollectorDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendAlertsArg(_message.Message):
    __slots__ = ("cluster_identifier", "alerts_data", "is_compressed", "last_collection_usecs", "is_timeseries")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ALERTS_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    LAST_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    alerts_data: bytes
    is_compressed: bool
    last_collection_usecs: int
    is_timeseries: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., alerts_data: _Optional[bytes] = ..., is_compressed: bool = ..., last_collection_usecs: _Optional[int] = ..., is_timeseries: bool = ...) -> None: ...

class SendAlertsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendClusterConfigArg(_message.Message):
    __slots__ = ("cluster_identifier", "cluster_config_data", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    cluster_config_data: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., cluster_config_data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendClusterConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendStatsArg(_message.Message):
    __slots__ = ("cluster_identifier", "stats_data", "isLastBatch", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STATS_DATA_FIELD_NUMBER: _ClassVar[int]
    ISLASTBATCH_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    stats_data: bytes
    isLastBatch: bool
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., stats_data: _Optional[bytes] = ..., isLastBatch: bool = ..., is_compressed: bool = ...) -> None: ...

class SendStatsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendHealthcheckDataArg(_message.Message):
    __slots__ = ("cluster_identifier", "healthcheck_data", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    HEALTHCHECK_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    healthcheck_data: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., healthcheck_data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendHealthcheckDataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendRunbooksArg(_message.Message):
    __slots__ = ("cluster_identifier", "runbooks_data", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RUNBOOKS_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    runbooks_data: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., runbooks_data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendRunbooksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QuorumRestrictedOpsRequest(_message.Message):
    __slots__ = ("cluster_identifier",)
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ...) -> None: ...

class QuorumRestrictedOpsResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ClusterType(_message.Message):
    __slots__ = ()
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ClusterType.Value]
        kCohesity: _ClassVar[ClusterType.Value]
        kExternal: _ClassVar[ClusterType.Value]
    kUnknown: ClusterType.Value
    kCohesity: ClusterType.Value
    kExternal: ClusterType.Value
    def __init__(self) -> None: ...

class ClusterMetadata(_message.Message):
    __slots__ = ("redirect_url", "cluster_type")
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    redirect_url: str
    cluster_type: ClusterType.Value
    def __init__(self, redirect_url: _Optional[str] = ..., cluster_type: _Optional[_Union[ClusterType.Value, str]] = ...) -> None: ...

class DataplaneMetadata(_message.Message):
    __slots__ = ("cluster_metadata",)
    CLUSTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    cluster_metadata: ClusterMetadata
    def __init__(self, cluster_metadata: _Optional[_Union[ClusterMetadata, _Mapping]] = ...) -> None: ...

class HeliosAgentHeartBeatRequest(_message.Message):
    __slots__ = ("cluster_identifier", "dataplane_metadata")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATAPLANE_METADATA_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    dataplane_metadata: DataplaneMetadata
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., dataplane_metadata: _Optional[_Union[DataplaneMetadata, _Mapping]] = ...) -> None: ...

class HeliosAgentHeartBeatResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeliosServerHeartBeatRequest(_message.Message):
    __slots__ = ("cluster_identifier",)
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ...) -> None: ...

class HeliosServerHeartBeatResponse(_message.Message):
    __slots__ = ("dataplane_connection_status",)
    DATAPLANE_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    dataplane_connection_status: bytes
    def __init__(self, dataplane_connection_status: _Optional[bytes] = ...) -> None: ...

class BulletinBoardArg(_message.Message):
    __slots__ = ("user_account_id", "cluster_identifier", "tenant_ids", "data_keys")
    USER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
    DATA_KEYS_FIELD_NUMBER: _ClassVar[int]
    user_account_id: str
    cluster_identifier: ClusterIdentifier
    tenant_ids: _containers.RepeatedScalarFieldContainer[str]
    data_keys: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_account_id: _Optional[str] = ..., cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., tenant_ids: _Optional[_Iterable[str]] = ..., data_keys: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateBulletinBoardArg(_message.Message):
    __slots__ = ("bulletin_board_arg", "data")
    BULLETIN_BOARD_ARG_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    bulletin_board_arg: BulletinBoardArg
    data: bytes
    def __init__(self, bulletin_board_arg: _Optional[_Union[BulletinBoardArg, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulletinBoardResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class AppMetadataRequest(_message.Message):
    __slots__ = ("app_id", "version")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    version: int
    def __init__(self, app_id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class AppMetadataResponse(_message.Message):
    __slots__ = ("size", "md5")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    size: int
    md5: str
    def __init__(self, size: _Optional[int] = ..., md5: _Optional[str] = ...) -> None: ...

class AppChunkRequest(_message.Message):
    __slots__ = ("app_id", "version", "offset", "chunkSize")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    version: int
    offset: int
    chunkSize: int
    def __init__(self, app_id: _Optional[int] = ..., version: _Optional[int] = ..., offset: _Optional[int] = ..., chunkSize: _Optional[int] = ...) -> None: ...

class AppChunkResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class SnapshotDiffRequest(_message.Message):
    __slots__ = ("cluster_identifier", "prepareArg")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PREPAREARG_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    prepareArg: bytes
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., prepareArg: _Optional[bytes] = ...) -> None: ...

class SnapshotDiffResponse(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class SnapshotDiffStatusRequest(_message.Message):
    __slots__ = ("cluster_identifier", "key")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    key: str
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class SnapshotDiffStatusResponse(_message.Message):
    __slots__ = ("key", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUNNING: _ClassVar[SnapshotDiffStatusResponse.Status]
        COMPLETED: _ClassVar[SnapshotDiffStatusResponse.Status]
        FAILED: _ClassVar[SnapshotDiffStatusResponse.Status]
    RUNNING: SnapshotDiffStatusResponse.Status
    COMPLETED: SnapshotDiffStatusResponse.Status
    FAILED: SnapshotDiffStatusResponse.Status
    KEY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    key: str
    status: SnapshotDiffStatusResponse.Status
    def __init__(self, key: _Optional[str] = ..., status: _Optional[_Union[SnapshotDiffStatusResponse.Status, str]] = ...) -> None: ...

class TenantInfo(_message.Message):
    __slots__ = ("name", "description", "tenantId", "lastUpdatedTimeStampUsecs", "status", "connectorEnabled", "clusterHostname", "clusterIps", "isManagedOnHelios")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATEDTIMESTAMPUSECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTORENABLED_FIELD_NUMBER: _ClassVar[int]
    CLUSTERHOSTNAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTERIPS_FIELD_NUMBER: _ClassVar[int]
    ISMANAGEDONHELIOS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    tenantId: str
    lastUpdatedTimeStampUsecs: int
    status: TenantStatus
    connectorEnabled: bool
    clusterHostname: str
    clusterIps: _containers.RepeatedScalarFieldContainer[str]
    isManagedOnHelios: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., tenantId: _Optional[str] = ..., lastUpdatedTimeStampUsecs: _Optional[int] = ..., status: _Optional[_Union[TenantStatus, str]] = ..., connectorEnabled: bool = ..., clusterHostname: _Optional[str] = ..., clusterIps: _Optional[_Iterable[str]] = ..., isManagedOnHelios: bool = ...) -> None: ...

class SendRigelHealthCheckArg(_message.Message):
    __slots__ = ("cluster_identifier", "connectivity_data", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    connectivity_data: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., connectivity_data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendRigelHealthCheckResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClusterKeyRequest(_message.Message):
    __slots__ = ("cluster_identifier",)
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ...) -> None: ...

class GetClusterKeyResponse(_message.Message):
    __slots__ = ("cluster_key", "err_msg")
    CLUSTER_KEY_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    cluster_key: bytes
    err_msg: str
    def __init__(self, cluster_key: _Optional[bytes] = ..., err_msg: _Optional[str] = ...) -> None: ...

class SendAuditLogDataArg(_message.Message):
    __slots__ = ("cluster_identifier", "audit_log", "is_compressed")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    audit_log: bytes
    is_compressed: bool
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., audit_log: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendAuditLogDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendNodesConfigDataArg(_message.Message):
    __slots__ = ("cluster_identifier", "nodes_config_data")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NODES_CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    nodes_config_data: bytes
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., nodes_config_data: _Optional[bytes] = ...) -> None: ...

class SendNodesConfigDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClusterPairingArg(_message.Message):
    __slots__ = ("cluster_identifier", "aws_role")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    AWS_ROLE_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    aws_role: str
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., aws_role: _Optional[str] = ...) -> None: ...

class ClusterPairingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMagnetoUpcomingJobsStatsRequest(_message.Message):
    __slots__ = ("cluster_identifier", "time_period_secs")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    time_period_secs: int
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., time_period_secs: _Optional[int] = ...) -> None: ...

class GetMagnetoUpcomingJobsStatsResponse(_message.Message):
    __slots__ = ("upcoming_job_count", "time_period_secs", "err_msg")
    UPCOMING_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    upcoming_job_count: int
    time_period_secs: int
    err_msg: str
    def __init__(self, upcoming_job_count: _Optional[int] = ..., time_period_secs: _Optional[int] = ..., err_msg: _Optional[str] = ...) -> None: ...

class UpdateClusterConfigMap(_message.Message):
    __slots__ = ("field", "storage_type_name", "int32_value")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    field: str
    storage_type_name: str
    int32_value: int
    def __init__(self, field: _Optional[str] = ..., storage_type_name: _Optional[str] = ..., int32_value: _Optional[int] = ...) -> None: ...

class SetupClusterForScalingRequest(_message.Message):
    __slots__ = ("cluster_identifier", "type", "update_cluster_config_map_vec")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLUSTER_CONFIG_MAP_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    type: ClusterScalingRequestType
    update_cluster_config_map_vec: _containers.RepeatedCompositeFieldContainer[UpdateClusterConfigMap]
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., type: _Optional[_Union[ClusterScalingRequestType, str]] = ..., update_cluster_config_map_vec: _Optional[_Iterable[_Union[UpdateClusterConfigMap, _Mapping]]] = ...) -> None: ...

class SetupClusterForScalingResponse(_message.Message):
    __slots__ = ("err_msg", "eagle_master_node_ip", "rss_usage")
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    EAGLE_MASTER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    RSS_USAGE_FIELD_NUMBER: _ClassVar[int]
    err_msg: str
    eagle_master_node_ip: str
    rss_usage: int
    def __init__(self, err_msg: _Optional[str] = ..., eagle_master_node_ip: _Optional[str] = ..., rss_usage: _Optional[int] = ...) -> None: ...

class MinSelector(_message.Message):
    __slots__ = ("min_ruleset_id",)
    MIN_RULESET_ID_FIELD_NUMBER: _ClassVar[int]
    min_ruleset_id: int
    def __init__(self, min_ruleset_id: _Optional[int] = ...) -> None: ...

class ListSelector(_message.Message):
    __slots__ = ("ruleset_ids",)
    RULESET_IDS_FIELD_NUMBER: _ClassVar[int]
    ruleset_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ruleset_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class Specification(_message.Message):
    __slots__ = ("vendor_id", "min_selector", "list_selector")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    LIST_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    vendor_id: int
    min_selector: MinSelector
    list_selector: ListSelector
    def __init__(self, vendor_id: _Optional[int] = ..., min_selector: _Optional[_Union[MinSelector, _Mapping]] = ..., list_selector: _Optional[_Union[ListSelector, _Mapping]] = ...) -> None: ...

class TriggerSnapshotSecurityScanRequest(_message.Message):
    __slots__ = ("cluster_identifier", "protection_group_id", "protection_group_instance_id", "snapshot_id", "scan_id", "specifications", "latest_ruleset_updated_timestamp_usecs")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    LATEST_RULESET_UPDATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    protection_group_id: str
    protection_group_instance_id: int
    snapshot_id: str
    scan_id: str
    specifications: _containers.RepeatedCompositeFieldContainer[Specification]
    latest_ruleset_updated_timestamp_usecs: int
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., protection_group_id: _Optional[str] = ..., protection_group_instance_id: _Optional[int] = ..., snapshot_id: _Optional[str] = ..., scan_id: _Optional[str] = ..., specifications: _Optional[_Iterable[_Union[Specification, _Mapping]]] = ..., latest_ruleset_updated_timestamp_usecs: _Optional[int] = ...) -> None: ...

class TriggerSnapshotSecurityScanResponse(_message.Message):
    __slots__ = ("protection_group_id", "protection_group_instance_id", "snapshot_id", "scan_id", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALIDATION_ERROR: _ClassVar[TriggerSnapshotSecurityScanResponse.Status]
        INTERNAL_ERROR: _ClassVar[TriggerSnapshotSecurityScanResponse.Status]
        ACCEPTED: _ClassVar[TriggerSnapshotSecurityScanResponse.Status]
    VALIDATION_ERROR: TriggerSnapshotSecurityScanResponse.Status
    INTERNAL_ERROR: TriggerSnapshotSecurityScanResponse.Status
    ACCEPTED: TriggerSnapshotSecurityScanResponse.Status
    PROTECTION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    protection_group_id: str
    protection_group_instance_id: int
    snapshot_id: str
    scan_id: str
    status: TriggerSnapshotSecurityScanResponse.Status
    def __init__(self, protection_group_id: _Optional[str] = ..., protection_group_instance_id: _Optional[int] = ..., snapshot_id: _Optional[str] = ..., scan_id: _Optional[str] = ..., status: _Optional[_Union[TriggerSnapshotSecurityScanResponse.Status, str]] = ...) -> None: ...
