from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.agents.windows.sql.base import sql_param_pb2 as _sql_param_pb2
from magneto.agents.windows.stub import ad_param_pb2 as _ad_param_pb2
from magneto.agents.windows.stub import exchange_param_pb2 as _exchange_param_pb2
from magneto.agents.windows.stub import o365spo_action_executor_pb2 as _o365spo_action_executor_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import source_throttling_pb2 as _source_throttling_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from util.cert import ssl_certificate_pb2 as _ssl_certificate_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterAgentArg(_message.Message):
    __slots__ = ("header", "agent_id", "cluster_name", "agent_uid", "force", "include_non_lvm_volumes", "discard_persistent_uid", "allow_multiple_cohesity_clusters", "include_shared_volumes", "include_vss_writer_status", "source_throttling_config", "fetch_all_volumes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NON_LVM_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    DISCARD_PERSISTENT_UID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTIPLE_COHESITY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHARED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VSS_WRITER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FETCH_ALL_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    agent_id: int
    cluster_name: str
    agent_uid: _universal_id_pb2.UniversalIdProto
    force: bool
    include_non_lvm_volumes: bool
    discard_persistent_uid: bool
    allow_multiple_cohesity_clusters: bool
    include_shared_volumes: bool
    include_vss_writer_status: bool
    source_throttling_config: _source_throttling_pb2.SourceThrottlingConfiguration
    fetch_all_volumes: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., agent_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., force: bool = ..., include_non_lvm_volumes: bool = ..., discard_persistent_uid: bool = ..., allow_multiple_cohesity_clusters: bool = ..., include_shared_volumes: bool = ..., include_vss_writer_status: bool = ..., source_throttling_config: _Optional[_Union[_source_throttling_pb2.SourceThrottlingConfiguration, _Mapping]] = ..., fetch_all_volumes: bool = ...) -> None: ...

class RegisterAgentResult(_message.Message):
    __slots__ = ("error", "agent_info", "volume_info_vec", "agent_uid", "system_resource_info")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    agent_info: _agent_pb2.AgentInfoProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    agent_uid: _universal_id_pb2.UniversalIdProto
    system_resource_info: _common_pb2.SystemResourceInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ...) -> None: ...

class UnregisterAgentArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetAgentInfoArg(_message.Message):
    __slots__ = ("header", "perform_cluster_detection", "populate_subnet_for_all_cluster_nodes", "vlan_hostname_tag")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PERFORM_CLUSTER_DETECTION_FIELD_NUMBER: _ClassVar[int]
    POPULATE_SUBNET_FOR_ALL_CLUSTER_NODES_FIELD_NUMBER: _ClassVar[int]
    VLAN_HOSTNAME_TAG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    perform_cluster_detection: bool
    populate_subnet_for_all_cluster_nodes: bool
    vlan_hostname_tag: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., perform_cluster_detection: bool = ..., populate_subnet_for_all_cluster_nodes: bool = ..., vlan_hostname_tag: _Optional[str] = ...) -> None: ...

class GetAgentInfoResult(_message.Message):
    __slots__ = ("error", "agent_info", "api_version", "incarnation_id", "cluster_id", "cluster_incarnation_id", "dedup_read_supported")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_READ_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    agent_info: _agent_pb2.AgentInfoProto
    api_version: int
    incarnation_id: int
    cluster_id: int
    cluster_incarnation_id: int
    dedup_read_supported: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., api_version: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., dedup_read_supported: bool = ...) -> None: ...

class RegisteredEndpointInfo(_message.Message):
    __slots__ = ("endpoint_type", "endpoint")
    ENDPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint_type: _agent_pb2.ClusterNetworkingInfo.Resource.Type
    endpoint: str
    def __init__(self, endpoint_type: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource.Type, str]] = ..., endpoint: _Optional[str] = ...) -> None: ...

class FetchVolumeInfoArg(_message.Message):
    __slots__ = ("header", "include_non_lvm_volumes", "include_shared_volumes", "include_smb_mount", "include_ro_volumes", "registered_endpoint_info", "fetch_all_volumes")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NON_LVM_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHARED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SMB_MOUNT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RO_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_ALL_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    include_non_lvm_volumes: bool
    include_shared_volumes: bool
    include_smb_mount: bool
    include_ro_volumes: bool
    registered_endpoint_info: RegisteredEndpointInfo
    fetch_all_volumes: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., include_non_lvm_volumes: bool = ..., include_shared_volumes: bool = ..., include_smb_mount: bool = ..., include_ro_volumes: bool = ..., registered_endpoint_info: _Optional[_Union[RegisteredEndpointInfo, _Mapping]] = ..., fetch_all_volumes: bool = ...) -> None: ...

class FetchVolumeInfoResult(_message.Message):
    __slots__ = ("error", "volume_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ...) -> None: ...

class GetHostInfoArg(_message.Message):
    __slots__ = ("header", "generate_serialized", "include_writer_status", "include_service_state", "include_gflag_settings")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    GENERATE_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_WRITER_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_GFLAG_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    generate_serialized: bool
    include_writer_status: bool
    include_service_state: bool
    include_gflag_settings: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., generate_serialized: bool = ..., include_writer_status: bool = ..., include_service_state: bool = ..., include_gflag_settings: bool = ...) -> None: ...

class JavaAgentInfo(_message.Message):
    __slots__ = ("cache_hit_count", "cache_miss_count", "java_version")
    CACHE_HIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CACHE_MISS_COUNT_FIELD_NUMBER: _ClassVar[int]
    JAVA_VERSION_FIELD_NUMBER: _ClassVar[int]
    cache_hit_count: int
    cache_miss_count: int
    java_version: str
    def __init__(self, cache_hit_count: _Optional[int] = ..., cache_miss_count: _Optional[int] = ..., java_version: _Optional[str] = ...) -> None: ...

class GetHostInfoResult(_message.Message):
    __slots__ = ("error", "host_info", "fetch_id", "host_info_summary", "gflag_setting_vec", "host_env", "java_agent_info")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    GFLAG_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_ENV_FIELD_NUMBER: _ClassVar[int]
    JAVA_AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    host_info: _agent_pb2.HostInfo
    fetch_id: str
    host_info_summary: _agent_pb2.HostInfoSummary
    gflag_setting_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.GFlagSetting]
    host_env: _enums_pb2.HostEnv.Type
    java_agent_info: JavaAgentInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_info: _Optional[_Union[_agent_pb2.HostInfo, _Mapping]] = ..., fetch_id: _Optional[str] = ..., host_info_summary: _Optional[_Union[_agent_pb2.HostInfoSummary, _Mapping]] = ..., gflag_setting_vec: _Optional[_Iterable[_Union[_agent_pb2.GFlagSetting, _Mapping]]] = ..., host_env: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., java_agent_info: _Optional[_Union[JavaAgentInfo, _Mapping]] = ...) -> None: ...

class VolumeSelection(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kListed: _ClassVar[VolumeSelection.Type]
        kAll: _ClassVar[VolumeSelection.Type]
        kAllExceptClusterResources: _ClassVar[VolumeSelection.Type]
    kListed: VolumeSelection.Type
    kAll: VolumeSelection.Type
    kAllExceptClusterResources: VolumeSelection.Type
    def __init__(self) -> None: ...

class PrepareVolumeSnapshotArg(_message.Message):
    __slots__ = ("header", "volume_guid_vec", "include_all_volumes", "volume_selection", "registered_endpoint_info")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SELECTION_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[bytes]
    include_all_volumes: bool
    volume_selection: VolumeSelection.Type
    registered_endpoint_info: RegisteredEndpointInfo
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_guid_vec: _Optional[_Iterable[bytes]] = ..., include_all_volumes: bool = ..., volume_selection: _Optional[_Union[VolumeSelection.Type, str]] = ..., registered_endpoint_info: _Optional[_Union[RegisteredEndpointInfo, _Mapping]] = ...) -> None: ...

class PrepareVolumeSnapshotResult(_message.Message):
    __slots__ = ("error", "snapshot_set_id")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    snapshot_set_id: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ...) -> None: ...

class TakeVolumeSnapshotArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "volume_guid_vec", "include_all_volumes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[bytes]
    include_all_volumes: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., volume_guid_vec: _Optional[_Iterable[bytes]] = ..., include_all_volumes: bool = ...) -> None: ...

class TakeVolumeSnapshotResult(_message.Message):
    __slots__ = ("error", "user_messages")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    user_messages: _magneto_pb2.UserMessageProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ...) -> None: ...

class FetchVolumeSnapshotInfoArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "volume_guid_vec", "include_snapshot_set_info", "include_volume_bitmap_info", "prev_volume_snapshot_map", "enable_delta_compression", "generate_serialized_server_snapshot_info", "compress_serialized_server_snapshot_info", "component_name", "include_app_file_info", "clusterid_jobid", "registered_endpoint_info")
    class PrevVolumeSnapshotMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SNAPSHOT_SET_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VOLUME_BITMAP_INFO_FIELD_NUMBER: _ClassVar[int]
    PREV_VOLUME_SNAPSHOT_MAP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DELTA_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    GENERATE_SERIALIZED_SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_SERIALIZED_SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTERID_JOBID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: str
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[str]
    include_snapshot_set_info: bool
    include_volume_bitmap_info: bool
    prev_volume_snapshot_map: _containers.ScalarMap[str, str]
    enable_delta_compression: bool
    generate_serialized_server_snapshot_info: bool
    compress_serialized_server_snapshot_info: bool
    component_name: str
    include_app_file_info: bool
    clusterid_jobid: str
    registered_endpoint_info: RegisteredEndpointInfo
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[str] = ..., volume_guid_vec: _Optional[_Iterable[str]] = ..., include_snapshot_set_info: bool = ..., include_volume_bitmap_info: bool = ..., prev_volume_snapshot_map: _Optional[_Mapping[str, str]] = ..., enable_delta_compression: bool = ..., generate_serialized_server_snapshot_info: bool = ..., compress_serialized_server_snapshot_info: bool = ..., component_name: _Optional[str] = ..., include_app_file_info: bool = ..., clusterid_jobid: _Optional[str] = ..., registered_endpoint_info: _Optional[_Union[RegisteredEndpointInfo, _Mapping]] = ...) -> None: ...

class FetchVolumeSnapshotInfoResult(_message.Message):
    __slots__ = ("error", "server_snapshot_info", "serialized_server_snapshot_info_size", "serialized_server_snapshot_info_compressed")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SERVER_SNAPSHOT_INFO_SIZE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SERVER_SNAPSHOT_INFO_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    serialized_server_snapshot_info_size: int
    serialized_server_snapshot_info_compressed: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., serialized_server_snapshot_info_size: _Optional[int] = ..., serialized_server_snapshot_info_compressed: bool = ...) -> None: ...

class FinalizeVolumeSnapshotMetadataArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "success", "compress_serialized")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    success: bool
    compress_serialized: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., success: bool = ..., compress_serialized: bool = ...) -> None: ...

class FinalizeVolumeSnapshotMetadataResult(_message.Message):
    __slots__ = ("error",)
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchSerializedDataArg(_message.Message):
    __slots__ = ("header", "id", "offset", "length")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    id: bytes
    offset: int
    length: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., id: _Optional[bytes] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FetchSerializedDataResult(_message.Message):
    __slots__ = ("error", "data", "has_more_data", "compressed")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_DATA_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    has_more_data: bool
    compressed: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ..., has_more_data: bool = ..., compressed: bool = ...) -> None: ...

class GCType(_message.Message):
    __slots__ = ()
    class gcAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoGc: _ClassVar[GCType.gcAction]
        kPartialGc: _ClassVar[GCType.gcAction]
        kGc: _ClassVar[GCType.gcAction]
        kDeleteJob: _ClassVar[GCType.gcAction]
    kNoGc: GCType.gcAction
    kPartialGc: GCType.gcAction
    kGc: GCType.gcAction
    kDeleteJob: GCType.gcAction
    def __init__(self) -> None: ...

class NotifyVolumeBackupCompleteArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "success", "gcstate")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    GCSTATE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    success: bool
    gcstate: GCType.gcAction
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., success: bool = ..., gcstate: _Optional[_Union[GCType.gcAction, str]] = ...) -> None: ...

class NotifyVolumeBackupCompleteResult(_message.Message):
    __slots__ = ("error", "user_messages")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    user_messages: _magneto_pb2.UserMessageProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ...) -> None: ...

class DeleteVolumeSnapshotArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ...) -> None: ...

class DeleteVolumeSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteVolumeSnapshotGroupArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class DeleteVolumeSnapshotGroupResult(_message.Message):
    __slots__ = ("error", "deletion_info_vec")
    class DeletionInfo(_message.Message):
        __slots__ = ("snapshot_set_id", "error")
        SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        snapshot_set_id: bytes
        error: _error_pb2.ErrorProto
        def __init__(self, snapshot_set_id: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    deletion_info_vec: _containers.RepeatedCompositeFieldContainer[DeleteVolumeSnapshotGroupResult.DeletionInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., deletion_info_vec: _Optional[_Iterable[_Union[DeleteVolumeSnapshotGroupResult.DeletionInfo, _Mapping]]] = ...) -> None: ...

class RevertVolumeToSnapshotArg(_message.Message):
    __slots__ = ("header", "snapshot_id_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_id_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_id_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RevertVolumeToSnapshotResult(_message.Message):
    __slots__ = ("error", "error_detail_vec")
    class ErrorDetail(_message.Message):
        __slots__ = ("snapshot_id", "error")
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        snapshot_id: bytes
        error: _error_pb2.ErrorProto
        def __init__(self, snapshot_id: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_detail_vec: _containers.RepeatedCompositeFieldContainer[RevertVolumeToSnapshotResult.ErrorDetail]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_detail_vec: _Optional[_Iterable[_Union[RevertVolumeToSnapshotResult.ErrorDetail, _Mapping]]] = ...) -> None: ...

class AbortVolumeSnapshotArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class AbortVolumeSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AcceptVolumeSnapshotMetadataArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "data", "offset", "has_more_data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_DATA_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    data: str
    offset: int
    has_more_data: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., data: _Optional[str] = ..., offset: _Optional[int] = ..., has_more_data: bool = ...) -> None: ...

class AcceptVolumeSnapshotMetadataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AgentRestoreType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFiles: _ClassVar[AgentRestoreType.Type]
        kVolume: _ClassVar[AgentRestoreType.Type]
        kApp: _ClassVar[AgentRestoreType.Type]
    kFiles: AgentRestoreType.Type
    kVolume: AgentRestoreType.Type
    kApp: AgentRestoreType.Type
    def __init__(self) -> None: ...

class RestoreAppFilesArg(_message.Message):
    __slots__ = ("mount_point", "original_to_mounted_path_map", "multi_stage_restore_action", "deleted_file_path_vec", "parallel_restore_info")
    class MultiStageRestoreAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[RestoreAppFilesArg.MultiStageRestoreAction]
        kFileMetadataSync: _ClassVar[RestoreAppFilesArg.MultiStageRestoreAction]
        kFinalizeRestoreOnly: _ClassVar[RestoreAppFilesArg.MultiStageRestoreAction]
    kNone: RestoreAppFilesArg.MultiStageRestoreAction
    kFileMetadataSync: RestoreAppFilesArg.MultiStageRestoreAction
    kFinalizeRestoreOnly: RestoreAppFilesArg.MultiStageRestoreAction
    class OriginalToMountedPathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TO_MOUNTED_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    mount_point: str
    original_to_mounted_path_map: _containers.ScalarMap[str, str]
    multi_stage_restore_action: RestoreAppFilesArg.MultiStageRestoreAction
    deleted_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    parallel_restore_info: ParallelRestoreInfo
    def __init__(self, mount_point: _Optional[str] = ..., original_to_mounted_path_map: _Optional[_Mapping[str, str]] = ..., multi_stage_restore_action: _Optional[_Union[RestoreAppFilesArg.MultiStageRestoreAction, str]] = ..., deleted_file_path_vec: _Optional[_Iterable[str]] = ..., parallel_restore_info: _Optional[_Union[ParallelRestoreInfo, _Mapping]] = ...) -> None: ...

class ParallelRestoreInfo(_message.Message):
    __slots__ = ("restore_step", "data_copy_done", "perform_rename", "cleanup_requested")
    class RestoreStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreDataCopyStep: _ClassVar[ParallelRestoreInfo.RestoreStep]
        kDataCopyStep: _ClassVar[ParallelRestoreInfo.RestoreStep]
        kPostDataCopyStep: _ClassVar[ParallelRestoreInfo.RestoreStep]
    kPreDataCopyStep: ParallelRestoreInfo.RestoreStep
    kDataCopyStep: ParallelRestoreInfo.RestoreStep
    kPostDataCopyStep: ParallelRestoreInfo.RestoreStep
    RESTORE_STEP_FIELD_NUMBER: _ClassVar[int]
    DATA_COPY_DONE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_RENAME_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    restore_step: ParallelRestoreInfo.RestoreStep
    data_copy_done: bool
    perform_rename: bool
    cleanup_requested: bool
    def __init__(self, restore_step: _Optional[_Union[ParallelRestoreInfo.RestoreStep, str]] = ..., data_copy_done: bool = ..., perform_rename: bool = ..., cleanup_requested: bool = ...) -> None: ...

class RestoreFromSnapshotArg(_message.Message):
    __slots__ = ("header", "restore_type", "server_snapshot_info", "credentials", "target_restore_entity", "restore_files_arg", "mount_volume_info_vec", "mounted_volumes_are_crash_consistent", "restore_app_files_arg", "registered_endpoint_info")
    Extensions: _python_message._ExtensionDict
    class RestoreFilesArg(_message.Message):
        __slots__ = ("restore_file_info_vec", "restore_files_preferences", "use_smb_push_for_proxy")
        RESTORE_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILES_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
        USE_SMB_PUSH_FOR_PROXY_FIELD_NUMBER: _ClassVar[int]
        restore_file_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoredFileInfo]
        restore_files_preferences: _magneto_pb2.RestoreFilesPreferences
        use_smb_push_for_proxy: bool
        def __init__(self, restore_file_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoredFileInfo, _Mapping]]] = ..., restore_files_preferences: _Optional[_Union[_magneto_pb2.RestoreFilesPreferences, _Mapping]] = ..., use_smb_push_for_proxy: bool = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESTORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_VOLUMES_ARE_CRASH_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_type: AgentRestoreType.Type
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    credentials: _credentials_pb2.Credentials
    target_restore_entity: _entity_pb2.EntityProto
    restore_files_arg: RestoreFromSnapshotArg.RestoreFilesArg
    mount_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.MountVolumeInfo]
    mounted_volumes_are_crash_consistent: bool
    restore_app_files_arg: RestoreAppFilesArg
    registered_endpoint_info: RegisteredEndpointInfo
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_type: _Optional[_Union[AgentRestoreType.Type, str]] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., target_restore_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., restore_files_arg: _Optional[_Union[RestoreFromSnapshotArg.RestoreFilesArg, _Mapping]] = ..., mount_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.MountVolumeInfo, _Mapping]]] = ..., mounted_volumes_are_crash_consistent: bool = ..., restore_app_files_arg: _Optional[_Union[RestoreAppFilesArg, _Mapping]] = ..., registered_endpoint_info: _Optional[_Union[RegisteredEndpointInfo, _Mapping]] = ...) -> None: ...

class RestoreFromSnapshotResult(_message.Message):
    __slots__ = ("error", "user_messages")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    user_messages: _magneto_pb2.UserMessageProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ...) -> None: ...

class GetRestoreFromSnapshotProgressArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[str] = ...) -> None: ...

class GetRestoreFromSnapshotProgressResult(_message.Message):
    __slots__ = ("error", "restore_type", "finished", "restore_error", "restore_files_result")
    Extensions: _python_message._ExtensionDict
    class RestoreFilesResult(_message.Message):
        __slots__ = ("status", "restore_file_result_info_vec")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_RESULT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        status: _magneto_pb2.RestoreFileStatus.Type
        restore_file_result_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreFileResultInfo]
        def __init__(self, status: _Optional[_Union[_magneto_pb2.RestoreFileStatus.Type, str]] = ..., restore_file_result_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreFileResultInfo, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_type: AgentRestoreType.Type
    finished: bool
    restore_error: _error_pb2.ErrorProto
    restore_files_result: GetRestoreFromSnapshotProgressResult.RestoreFilesResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_type: _Optional[_Union[AgentRestoreType.Type, str]] = ..., finished: bool = ..., restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_files_result: _Optional[_Union[GetRestoreFromSnapshotProgressResult.RestoreFilesResult, _Mapping]] = ...) -> None: ...

class InitApplyChangedAreasArg(_message.Message):
    __slots__ = ("header", "entity_key", "abort_existing_task", "delete_files_after_abort")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    ABORT_EXISTING_TASK_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILES_AFTER_ABORT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    entity_key: str
    abort_existing_task: bool
    delete_files_after_abort: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., entity_key: _Optional[str] = ..., abort_existing_task: bool = ..., delete_files_after_abort: bool = ...) -> None: ...

class InitApplyChangedAreasResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ApplyChangedAreasFileState(_message.Message):
    __slots__ = ("agent_synced_offset", "agent_work_offset", "error_vec")
    AGENT_SYNCED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AGENT_WORK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    agent_synced_offset: int
    agent_work_offset: int
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, agent_synced_offset: _Optional[int] = ..., agent_work_offset: _Optional[int] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class ApplyChangedAreasArg(_message.Message):
    __slots__ = ("header", "entity_key", "batch_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    BATCH_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    entity_key: str
    batch_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.ApplyChangedAreasBatch]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., entity_key: _Optional[str] = ..., batch_vec: _Optional[_Iterable[_Union[_agent_pb2.ApplyChangedAreasBatch, _Mapping]]] = ...) -> None: ...

class ApplyChangedAreasResult(_message.Message):
    __slots__ = ("error", "file_path_to_state_map")
    class FilePathToStateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ApplyChangedAreasFileState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ApplyChangedAreasFileState, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_TO_STATE_MAP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_path_to_state_map: _containers.MessageMap[str, ApplyChangedAreasFileState]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_path_to_state_map: _Optional[_Mapping[str, ApplyChangedAreasFileState]] = ...) -> None: ...

class QueryApplyChangedAreasArg(_message.Message):
    __slots__ = ("header", "entity_key", "file_path_to_magneto_synced_offset_map")
    class FilePathToMagnetoSyncedOffsetMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_TO_MAGNETO_SYNCED_OFFSET_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    entity_key: str
    file_path_to_magneto_synced_offset_map: _containers.ScalarMap[str, int]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., entity_key: _Optional[str] = ..., file_path_to_magneto_synced_offset_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class QueryApplyChangedAreasResult(_message.Message):
    __slots__ = ("error", "file_path_to_state_map")
    class FilePathToStateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ApplyChangedAreasFileState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ApplyChangedAreasFileState, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_TO_STATE_MAP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_path_to_state_map: _containers.MessageMap[str, ApplyChangedAreasFileState]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_path_to_state_map: _Optional[_Mapping[str, ApplyChangedAreasFileState]] = ...) -> None: ...

class NotifyApplyChangedAreasDoneArg(_message.Message):
    __slots__ = ("header", "entity_key", "validate_copied_files", "clear_task_state")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_COPIED_FILES_FIELD_NUMBER: _ClassVar[int]
    CLEAR_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    entity_key: str
    validate_copied_files: bool
    clear_task_state: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., entity_key: _Optional[str] = ..., validate_copied_files: bool = ..., clear_task_state: bool = ...) -> None: ...

class NotifyApplyChangedAreasDoneResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("header", "delete_files")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    delete_files: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., delete_files: bool = ...) -> None: ...

class CancelTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetCancelTaskProgressArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetCancelTaskProgressResult(_message.Message):
    __slots__ = ("error", "cancelled")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cancelled: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cancelled: bool = ...) -> None: ...

class BringDisksOnlineArg(_message.Message):
    __slots__ = ("header", "disk_device_id_vec", "set_disk_ro")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DISK_DEVICE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SET_DISK_RO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    disk_device_id_vec: _containers.RepeatedScalarFieldContainer[int]
    set_disk_ro: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., disk_device_id_vec: _Optional[_Iterable[int]] = ..., set_disk_ro: bool = ...) -> None: ...

class BringDisksOnlineResult(_message.Message):
    __slots__ = ("error", "volume_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ...) -> None: ...

class StopCBTOnVolumesArg(_message.Message):
    __slots__ = ("header", "volume_guid_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_guid_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class StopCBTOnVolumesResult(_message.Message):
    __slots__ = ("error", "stop_cbt_result_vec")
    class StopCBTResult(_message.Message):
        __slots__ = ("volume_guid", "error")
        VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        volume_guid: bytes
        error: _error_pb2.ErrorProto
        def __init__(self, volume_guid: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STOP_CBT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    stop_cbt_result_vec: _containers.RepeatedCompositeFieldContainer[StopCBTOnVolumesResult.StopCBTResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stop_cbt_result_vec: _Optional[_Iterable[_Union[StopCBTOnVolumesResult.StopCBTResult, _Mapping]]] = ...) -> None: ...

class LockVolumeArg(_message.Message):
    __slots__ = ("header", "volume_dev_path", "force_unmount_volume")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    FORCE_UNMOUNT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    force_unmount_volume: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ..., force_unmount_volume: bool = ...) -> None: ...

class UnlockVolumeArg(_message.Message):
    __slots__ = ("header", "volume_dev_path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ...) -> None: ...

class ReadVolumeArg(_message.Message):
    __slots__ = ("header", "volume_dev_path", "offset", "length", "guid", "type", "allow_read_beyond_fs_region", "enable_file_handle_cache", "rpc_stats")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_READ_BEYOND_FS_REGION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FILE_HANDLE_CACHE_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    offset: int
    length: int
    guid: str
    type: _enums_pb2.Environment.Type
    allow_read_beyond_fs_region: bool
    enable_file_handle_cache: bool
    rpc_stats: _agent_pb2.RpcStats
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., guid: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., allow_read_beyond_fs_region: bool = ..., enable_file_handle_cache: bool = ..., rpc_stats: _Optional[_Union[_agent_pb2.RpcStats, _Mapping]] = ...) -> None: ...

class ReadVolumeResult(_message.Message):
    __slots__ = ("error", "data", "eof", "io_latency_usecs", "io_read_time_usecs", "io_handle_open_time_usecs", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    IO_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    IO_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IO_HANDLE_OPEN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    eof: bool
    io_latency_usecs: int
    io_read_time_usecs: int
    io_handle_open_time_usecs: int
    rpc_stats: _agent_pb2.RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ..., eof: bool = ..., io_latency_usecs: _Optional[int] = ..., io_read_time_usecs: _Optional[int] = ..., io_handle_open_time_usecs: _Optional[int] = ..., rpc_stats: _Optional[_Union[_agent_pb2.RpcStats, _Mapping]] = ...) -> None: ...

class WriteVolumeArg(_message.Message):
    __slots__ = ("header", "volume_dev_path", "offset", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    offset: int
    data: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteVolumeResult(_message.Message):
    __slots__ = ("error", "io_latency_usecs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IO_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    io_latency_usecs: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., io_latency_usecs: _Optional[int] = ...) -> None: ...

class MountVirtualVolumeArg(_message.Message):
    __slots__ = ("header", "volume_files_info", "persistent", "ro_persistent", "reboot_persistent")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    RO_PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    REBOOT_PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_files_info: _volume_info_pb2.VolumeInfo
    persistent: bool
    ro_persistent: bool
    reboot_persistent: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_files_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., persistent: bool = ..., ro_persistent: bool = ..., reboot_persistent: bool = ...) -> None: ...

class MountVirtualVolumeResult(_message.Message):
    __slots__ = ("error", "mountpoint")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mountpoint: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mountpoint: _Optional[str] = ...) -> None: ...

class MountNASArg(_message.Message):
    __slots__ = ("header", "remote_name", "username", "password", "persistent", "alternate_remote_name_vec")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_REMOTE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    remote_name: str
    username: str
    password: str
    persistent: bool
    alternate_remote_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., remote_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., persistent: bool = ..., alternate_remote_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class MountNASResult(_message.Message):
    __slots__ = ("error", "mountpoint")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mountpoint: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mountpoint: _Optional[str] = ...) -> None: ...

class UnmountVirtualVolumeArg(_message.Message):
    __slots__ = ("header", "mountpoint", "disk_file_path")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    DISK_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mountpoint: str
    disk_file_path: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mountpoint: _Optional[str] = ..., disk_file_path: _Optional[str] = ...) -> None: ...

class UnmountNASArg(_message.Message):
    __slots__ = ("header", "mountpoint")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mountpoint: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mountpoint: _Optional[str] = ...) -> None: ...

class PrepareForShutdownArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class TerminateArg(_message.Message):
    __slots__ = ("header", "terminate_with_wait")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TERMINATE_WITH_WAIT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    terminate_with_wait: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., terminate_with_wait: bool = ...) -> None: ...

class ExportedFileInfo(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAgentLogs: _ClassVar[ExportedFileInfo.Type]
        kSystemLogs: _ClassVar[ExportedFileInfo.Type]
        kDumps: _ClassVar[ExportedFileInfo.Type]
        kMemTraces: _ClassVar[ExportedFileInfo.Type]
        kTypeLimit: _ClassVar[ExportedFileInfo.Type]
        kOracleRmanLogs: _ClassVar[ExportedFileInfo.Type]
    kAgentLogs: ExportedFileInfo.Type
    kSystemLogs: ExportedFileInfo.Type
    kDumps: ExportedFileInfo.Type
    kMemTraces: ExportedFileInfo.Type
    kTypeLimit: ExportedFileInfo.Type
    kOracleRmanLogs: ExportedFileInfo.Type
    def __init__(self) -> None: ...

class ListFilesArg(_message.Message):
    __slots__ = ("header", "type_vec", "executable_name")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    type_vec: _containers.RepeatedScalarFieldContainer[ExportedFileInfo.Type]
    executable_name: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., type_vec: _Optional[_Iterable[_Union[ExportedFileInfo.Type, str]]] = ..., executable_name: _Optional[bytes] = ...) -> None: ...

class ListFilesResult(_message.Message):
    __slots__ = ("error", "file_vec")
    class File(_message.Message):
        __slots__ = ("original_file_name", "original_size", "original_mtime_usecs", "type")
        ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        original_file_name: bytes
        original_size: int
        original_mtime_usecs: int
        type: ExportedFileInfo.Type
        def __init__(self, original_file_name: _Optional[bytes] = ..., original_size: _Optional[int] = ..., original_mtime_usecs: _Optional[int] = ..., type: _Optional[_Union[ExportedFileInfo.Type, str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_vec: _containers.RepeatedCompositeFieldContainer[ListFilesResult.File]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_vec: _Optional[_Iterable[_Union[ListFilesResult.File, _Mapping]]] = ...) -> None: ...

class FetchFilesArg(_message.Message):
    __slots__ = ("header", "file_name_vec", "offset_bytes", "limit_size_bytes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_name_vec: _containers.RepeatedScalarFieldContainer[bytes]
    offset_bytes: int
    limit_size_bytes: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_name_vec: _Optional[_Iterable[bytes]] = ..., offset_bytes: _Optional[int] = ..., limit_size_bytes: _Optional[int] = ...) -> None: ...

class FetchFilesResult(_message.Message):
    __slots__ = ("error", "file_vec")
    class File(_message.Message):
        __slots__ = ("original_file_name", "data", "compressed")
        ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_FIELD_NUMBER: _ClassVar[int]
        original_file_name: bytes
        data: bytes
        compressed: bool
        def __init__(self, original_file_name: _Optional[bytes] = ..., data: _Optional[bytes] = ..., compressed: bool = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_vec: _containers.RepeatedCompositeFieldContainer[FetchFilesResult.File]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_vec: _Optional[_Iterable[_Union[FetchFilesResult.File, _Mapping]]] = ...) -> None: ...

class ReadFileBurstArg(_message.Message):
    __slots__ = ("header", "file_path", "offset", "chunk_size", "hash_data", "read_limit", "ed_threads", "send_sha1")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    HASH_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ED_THREADS_FIELD_NUMBER: _ClassVar[int]
    SEND_SHA1_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_path: bytes
    offset: int
    chunk_size: int
    hash_data: bool
    read_limit: int
    ed_threads: int
    send_sha1: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_path: _Optional[bytes] = ..., offset: _Optional[int] = ..., chunk_size: _Optional[int] = ..., hash_data: bool = ..., read_limit: _Optional[int] = ..., ed_threads: _Optional[int] = ..., send_sha1: bool = ...) -> None: ...

class ReadFileBurstResult(_message.Message):
    __slots__ = ("error", "chunk_vec")
    class Chunk(_message.Message):
        __slots__ = ("offset", "len", "sha1")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LEN_FIELD_NUMBER: _ClassVar[int]
        SHA1_FIELD_NUMBER: _ClassVar[int]
        offset: int
        len: int
        sha1: str
        def __init__(self, offset: _Optional[int] = ..., len: _Optional[int] = ..., sha1: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    chunk_vec: _containers.RepeatedCompositeFieldContainer[ReadFileBurstResult.Chunk]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., chunk_vec: _Optional[_Iterable[_Union[ReadFileBurstResult.Chunk, _Mapping]]] = ...) -> None: ...

class RunDiagnosticsArg(_message.Message):
    __slots__ = ("header", "offset_bytes", "limit_size_bytes", "create_tarball", "local_alarm_call", "get_all_logs")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TARBALL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ALARM_CALL_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_LOGS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    offset_bytes: int
    limit_size_bytes: int
    create_tarball: bool
    local_alarm_call: bool
    get_all_logs: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., offset_bytes: _Optional[int] = ..., limit_size_bytes: _Optional[int] = ..., create_tarball: bool = ..., local_alarm_call: bool = ..., get_all_logs: bool = ...) -> None: ...

class RunDiagnosticsResult(_message.Message):
    __slots__ = ("error", "diag_file")
    class File(_message.Message):
        __slots__ = ("original_file_name", "data", "original_file_size")
        ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        original_file_name: bytes
        data: bytes
        original_file_size: int
        def __init__(self, original_file_name: _Optional[bytes] = ..., data: _Optional[bytes] = ..., original_file_size: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DIAG_FILE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    diag_file: RunDiagnosticsResult.File
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., diag_file: _Optional[_Union[RunDiagnosticsResult.File, _Mapping]] = ...) -> None: ...

class GetGFlagSettingsArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetGFlagSettingsResult(_message.Message):
    __slots__ = ("error", "gflag_setting_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GFLAG_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    gflag_setting_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.GFlagSetting]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., gflag_setting_vec: _Optional[_Iterable[_Union[_agent_pb2.GFlagSetting, _Mapping]]] = ...) -> None: ...

class UpdateGFlagSettingsArg(_message.Message):
    __slots__ = ("header", "gflag_setting_vec", "clear_current", "effective_now")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    GFLAG_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CURRENT_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_NOW_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    gflag_setting_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.GFlagSetting]
    clear_current: bool
    effective_now: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., gflag_setting_vec: _Optional[_Iterable[_Union[_agent_pb2.GFlagSetting, _Mapping]]] = ..., clear_current: bool = ..., effective_now: bool = ...) -> None: ...

class InstallUpdateArg(_message.Message):
    __slots__ = ("header", "uri", "command_line_args", "uri_vec", "wget_retry_count", "sleep_duration_between_wget_retries_secs", "retry_http_upon_https_failure")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINE_ARGS_FIELD_NUMBER: _ClassVar[int]
    URI_VEC_FIELD_NUMBER: _ClassVar[int]
    WGET_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLEEP_DURATION_BETWEEN_WGET_RETRIES_SECS_FIELD_NUMBER: _ClassVar[int]
    RETRY_HTTP_UPON_HTTPS_FAILURE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    uri: str
    command_line_args: str
    uri_vec: _containers.RepeatedScalarFieldContainer[str]
    wget_retry_count: int
    sleep_duration_between_wget_retries_secs: int
    retry_http_upon_https_failure: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., uri: _Optional[str] = ..., command_line_args: _Optional[str] = ..., uri_vec: _Optional[_Iterable[str]] = ..., wget_retry_count: _Optional[int] = ..., sleep_duration_between_wget_retries_secs: _Optional[int] = ..., retry_http_upon_https_failure: bool = ...) -> None: ...

class GetInstallUpdateProgressArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetInstallUpdateProgressResult(_message.Message):
    __slots__ = ("error", "finished", "update_error")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    finished: bool
    update_error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., finished: bool = ..., update_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetServiceStateArg(_message.Message):
    __slots__ = ("header", "service_name_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    service_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., service_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetServiceStateResult(_message.Message):
    __slots__ = ("error", "state_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    state_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.ServiceState]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., state_vec: _Optional[_Iterable[_Union[_agent_pb2.ServiceState, _Mapping]]] = ...) -> None: ...

class ControlServiceArg(_message.Message):
    __slots__ = ("header", "info")
    class ServiceInfo(_message.Message):
        __slots__ = ("name", "action", "start_service_args_vec", "display_name")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStart: _ClassVar[ControlServiceArg.ServiceInfo.Action]
            kStop: _ClassVar[ControlServiceArg.ServiceInfo.Action]
        kStart: ControlServiceArg.ServiceInfo.Action
        kStop: ControlServiceArg.ServiceInfo.Action
        NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        START_SERVICE_ARGS_VEC_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        action: ControlServiceArg.ServiceInfo.Action
        start_service_args_vec: _containers.RepeatedScalarFieldContainer[str]
        display_name: str
        def __init__(self, name: _Optional[str] = ..., action: _Optional[_Union[ControlServiceArg.ServiceInfo.Action, str]] = ..., start_service_args_vec: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    info: ControlServiceArg.ServiceInfo
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., info: _Optional[_Union[ControlServiceArg.ServiceInfo, _Mapping]] = ...) -> None: ...

class StartCBMRArg(_message.Message):
    __slots__ = ("header", "destination_path", "local_path", "excluded_dirs_vec", "cbmr_config")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DIRS_VEC_FIELD_NUMBER: _ClassVar[int]
    CBMR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    destination_path: str
    local_path: str
    excluded_dirs_vec: _containers.RepeatedScalarFieldContainer[str]
    cbmr_config: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., destination_path: _Optional[str] = ..., local_path: _Optional[str] = ..., excluded_dirs_vec: _Optional[_Iterable[str]] = ..., cbmr_config: _Optional[str] = ...) -> None: ...

class GetCBMRProgressArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetCBMRProgressResult(_message.Message):
    __slots__ = ("error", "cbmr_error", "finished", "total_dir_count", "completed_dir_count")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CBMR_ERROR_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIR_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_DIR_COUNT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cbmr_error: _error_pb2.ErrorProto
    finished: bool
    total_dir_count: int
    completed_dir_count: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cbmr_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., finished: bool = ..., total_dir_count: _Optional[int] = ..., completed_dir_count: _Optional[int] = ...) -> None: ...

class CancelCBMRArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetFileChangeAreasArg(_message.Message):
    __slots__ = ("header", "file_full_path", "offset", "length", "snapshot_set_id", "previous_snapshot_set_id", "previous_file_path", "type", "clusterid_jobid", "fail_for_qcow2_compression_enabled")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTERID_JOBID_FIELD_NUMBER: _ClassVar[int]
    FAIL_FOR_QCOW2_COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_full_path: str
    offset: int
    length: int
    snapshot_set_id: bytes
    previous_snapshot_set_id: bytes
    previous_file_path: str
    type: _enums_pb2.Environment.Type
    clusterid_jobid: str
    fail_for_qcow2_compression_enabled: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_full_path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., snapshot_set_id: _Optional[bytes] = ..., previous_snapshot_set_id: _Optional[bytes] = ..., previous_file_path: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., clusterid_jobid: _Optional[str] = ..., fail_for_qcow2_compression_enabled: bool = ...) -> None: ...

class GetFileChangeAreasResult(_message.Message):
    __slots__ = ("error", "delta_type", "delta_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ...) -> None: ...

class RemountDisksArg(_message.Message):
    __slots__ = ("header", "mount_vec")
    class Mount(_message.Message):
        __slots__ = ("guid", "mountpoint")
        GUID_FIELD_NUMBER: _ClassVar[int]
        MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
        guid: str
        mountpoint: str
        def __init__(self, guid: _Optional[str] = ..., mountpoint: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mount_vec: _containers.RepeatedCompositeFieldContainer[RemountDisksArg.Mount]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mount_vec: _Optional[_Iterable[_Union[RemountDisksArg.Mount, _Mapping]]] = ...) -> None: ...

class RemountDisksResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloseDiskArg(_message.Message):
    __slots__ = ("header", "volume_dev_path", "type", "use_volume_reader")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_VOLUME_READER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    type: _enums_pb2.Environment.Type
    use_volume_reader: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., use_volume_reader: bool = ...) -> None: ...

class StartScriptExecutionArg(_message.Message):
    __slots__ = ("header", "script", "env_vec", "should_return_output")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETURN_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    script: _magneto_pb2.RemoteScriptProto
    env_vec: _containers.RepeatedScalarFieldContainer[str]
    should_return_output: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., script: _Optional[_Union[_magneto_pb2.RemoteScriptProto, _Mapping]] = ..., env_vec: _Optional[_Iterable[str]] = ..., should_return_output: bool = ...) -> None: ...

class StartScriptExecutionResult(_message.Message):
    __slots__ = ("error", "script_start_time_usecs", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    script_start_time_usecs: int
    status: _magneto_pb2.ScriptExecutionStatus
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., script_start_time_usecs: _Optional[int] = ..., status: _Optional[_Union[_magneto_pb2.ScriptExecutionStatus, _Mapping]] = ...) -> None: ...

class GetScriptExecutionStatusArg(_message.Message):
    __slots__ = ("header", "send_stdout_log", "send_stderr_log")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SEND_STDOUT_LOG_FIELD_NUMBER: _ClassVar[int]
    SEND_STDERR_LOG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    send_stdout_log: int
    send_stderr_log: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., send_stdout_log: _Optional[int] = ..., send_stderr_log: _Optional[int] = ...) -> None: ...

class GetScriptExecutionStatusResult(_message.Message):
    __slots__ = ("error", "status", "script_log")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_LOG_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: _magneto_pb2.ScriptExecutionStatus
    script_log: _magneto_pb2.ScriptLogMessage
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[_magneto_pb2.ScriptExecutionStatus, _Mapping]] = ..., script_log: _Optional[_Union[_magneto_pb2.ScriptLogMessage, _Mapping]] = ...) -> None: ...

class CancelScriptExecutionArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class CancelScriptExecutionResult(_message.Message):
    __slots__ = ("error", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: _magneto_pb2.ScriptExecutionStatus
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[_magneto_pb2.ScriptExecutionStatus, _Mapping]] = ...) -> None: ...

class CleanupScriptExecutionStateArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class CleanupScriptExecutionStateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AgentActionAdapterServiceType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEnvironment: _ClassVar[AgentActionAdapterServiceType.Type]
        kO365SPO: _ClassVar[AgentActionAdapterServiceType.Type]
    kEnvironment: AgentActionAdapterServiceType.Type
    kO365SPO: AgentActionAdapterServiceType.Type
    def __init__(self) -> None: ...

class ExecuteAgentActionArg(_message.Message):
    __slots__ = ("env_type", "header", "ad_action_arg", "exchange_action_arg", "get_app_topology_arg", "service_type", "o365spo_action_arg", "sql_action_arg", "glob_arg")
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AD_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_APP_TOPOLOGY_ARG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    O365SPO_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    SQL_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    GLOB_ARG_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    header: _agent_base_pb2.AgentBaseArg
    ad_action_arg: _ad_param_pb2.ExecuteADActionArg
    exchange_action_arg: _exchange_param_pb2.ExecuteExchangeActionArg
    get_app_topology_arg: GetAppTopologyArg
    service_type: AgentActionAdapterServiceType.Type
    o365spo_action_arg: _o365spo_action_executor_pb2.ExecuteO365SPOActionArg
    sql_action_arg: _sql_param_pb2.ExecuteSQLActionArg
    glob_arg: GlobArg
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., ad_action_arg: _Optional[_Union[_ad_param_pb2.ExecuteADActionArg, _Mapping]] = ..., exchange_action_arg: _Optional[_Union[_exchange_param_pb2.ExecuteExchangeActionArg, _Mapping]] = ..., get_app_topology_arg: _Optional[_Union[GetAppTopologyArg, _Mapping]] = ..., service_type: _Optional[_Union[AgentActionAdapterServiceType.Type, str]] = ..., o365spo_action_arg: _Optional[_Union[_o365spo_action_executor_pb2.ExecuteO365SPOActionArg, _Mapping]] = ..., sql_action_arg: _Optional[_Union[_sql_param_pb2.ExecuteSQLActionArg, _Mapping]] = ..., glob_arg: _Optional[_Union[GlobArg, _Mapping]] = ...) -> None: ...

class ExecuteAgentActionResult(_message.Message):
    __slots__ = ("error", "env_type", "ad_action_result", "exchange_action_result", "get_app_topology_result", "service_type", "o365spo_action_result", "sql_action_result", "glob_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_APP_TOPOLOGY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    O365SPO_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    SQL_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    GLOB_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    env_type: _enums_pb2.Environment.Type
    ad_action_result: _ad_param_pb2.ExecuteADActionResult
    exchange_action_result: _exchange_param_pb2.ExecuteExchangeActionResult
    get_app_topology_result: GetAppTopologyResult
    service_type: AgentActionAdapterServiceType.Type
    o365spo_action_result: _o365spo_action_executor_pb2.ExecuteO365SPOActionResult
    sql_action_result: _sql_param_pb2.ExecuteSQLActionResult
    glob_result: GlobResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., ad_action_result: _Optional[_Union[_ad_param_pb2.ExecuteADActionResult, _Mapping]] = ..., exchange_action_result: _Optional[_Union[_exchange_param_pb2.ExecuteExchangeActionResult, _Mapping]] = ..., get_app_topology_result: _Optional[_Union[GetAppTopologyResult, _Mapping]] = ..., service_type: _Optional[_Union[AgentActionAdapterServiceType.Type, str]] = ..., o365spo_action_result: _Optional[_Union[_o365spo_action_executor_pb2.ExecuteO365SPOActionResult, _Mapping]] = ..., sql_action_result: _Optional[_Union[_sql_param_pb2.ExecuteSQLActionResult, _Mapping]] = ..., glob_result: _Optional[_Union[GlobResult, _Mapping]] = ...) -> None: ...

class RunHostSettingsCheckArg(_message.Message):
    __slots__ = ("header", "run_all_checks", "host_settings_check_vec", "env_type", "skip_cache", "credentials")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_ALL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    HOST_SETTINGS_CHECK_VEC_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    run_all_checks: bool
    host_settings_check_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostSettingsCheck]
    env_type: _enums_pb2.Environment.Type
    skip_cache: bool
    credentials: _credentials_pb2.Credentials
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., run_all_checks: bool = ..., host_settings_check_vec: _Optional[_Iterable[_Union[_agent_pb2.HostSettingsCheck, _Mapping]]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., skip_cache: bool = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class RunHostSettingsCheckResult(_message.Message):
    __slots__ = ("error", "last_run_end_time_usec", "result_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_END_TIME_USEC_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    last_run_end_time_usec: int
    result_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostSettingsCheckResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., last_run_end_time_usec: _Optional[int] = ..., result_vec: _Optional[_Iterable[_Union[_agent_pb2.HostSettingsCheckResult, _Mapping]]] = ...) -> None: ...

class UploadCertToHostArg(_message.Message):
    __slots__ = ("header", "agent_cert")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AGENT_CERT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    agent_cert: _ssl_certificate_pb2.AgentCertificate
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., agent_cert: _Optional[_Union[_ssl_certificate_pb2.AgentCertificate, _Mapping]] = ...) -> None: ...

class TopologyNode(_message.Message):
    __slots__ = ("node_id", "cluster_resource", "is_root", "child_id_vec", "display_messages")
    Extensions: _python_message._ExtensionDict
    class NodeID(_message.Message):
        __slots__ = ("wsfc_node_id", "node_name", "node_ip")
        WSFC_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        wsfc_node_id: str
        node_name: str
        node_ip: str
        def __init__(self, wsfc_node_id: _Optional[str] = ..., node_name: _Optional[str] = ..., node_ip: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    CHILD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    node_id: TopologyNode.NodeID
    cluster_resource: _agent_pb2.ClusterNetworkingInfo.Resource
    is_root: bool
    child_id_vec: _containers.RepeatedCompositeFieldContainer[TopologyNode.NodeID]
    display_messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node_id: _Optional[_Union[TopologyNode.NodeID, _Mapping]] = ..., cluster_resource: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource, _Mapping]] = ..., is_root: bool = ..., child_id_vec: _Optional[_Iterable[_Union[TopologyNode.NodeID, _Mapping]]] = ..., display_messages: _Optional[_Iterable[str]] = ...) -> None: ...

class AppTopology(_message.Message):
    __slots__ = ("error", "env_type", "last_cache_update_usecs", "requested_endpoint_matches_wsfc_address", "node_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_CACHE_UPDATE_USECS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ENDPOINT_MATCHES_WSFC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    env_type: _enums_pb2.Environment.Type
    last_cache_update_usecs: int
    requested_endpoint_matches_wsfc_address: bool
    node_vec: _containers.RepeatedCompositeFieldContainer[TopologyNode]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., last_cache_update_usecs: _Optional[int] = ..., requested_endpoint_matches_wsfc_address: bool = ..., node_vec: _Optional[_Iterable[_Union[TopologyNode, _Mapping]]] = ...) -> None: ...

class GetAppTopologyArg(_message.Message):
    __slots__ = ("env_vec", "endpoint", "timeout_sec", "num_retries", "use_cached_topology")
    Extensions: _python_message._ExtensionDict
    ENV_VEC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    USE_CACHED_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    env_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    endpoint: str
    timeout_sec: int
    num_retries: int
    use_cached_topology: bool
    def __init__(self, env_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., endpoint: _Optional[str] = ..., timeout_sec: _Optional[int] = ..., num_retries: _Optional[int] = ..., use_cached_topology: bool = ...) -> None: ...

class GetAppTopologyResult(_message.Message):
    __slots__ = ("error", "app_topology_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_TOPOLOGY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    app_topology_vec: _containers.RepeatedCompositeFieldContainer[AppTopology]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_topology_vec: _Optional[_Iterable[_Union[AppTopology, _Mapping]]] = ...) -> None: ...

class GlobArg(_message.Message):
    __slots__ = ("path_patterns",)
    PATH_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    path_patterns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, path_patterns: _Optional[_Iterable[str]] = ...) -> None: ...

class GlobResult(_message.Message):
    __slots__ = ("resolved_paths_vec",)
    RESOLVED_PATHS_VEC_FIELD_NUMBER: _ClassVar[int]
    resolved_paths_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resolved_paths_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateSourceThrottlingConfigArg(_message.Message):
    __slots__ = ("header", "throttling_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    throttling_info: _source_throttling_pb2.SourceThrottlingConfiguration
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., throttling_info: _Optional[_Union[_source_throttling_pb2.SourceThrottlingConfiguration, _Mapping]] = ...) -> None: ...

class UpdateSourceThrottlingConfigResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchSourceThrottlingConfigArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class FetchSourceThrottlingConfigResult(_message.Message):
    __slots__ = ("error", "throttling_info", "cpu_effective_throttling_data", "network_effective_throttling_data")
    class EffectiveThrottlingData(_message.Message):
        __slots__ = ("effective_threshold", "timestamp_usecs")
        EFFECTIVE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        effective_threshold: int
        timestamp_usecs: int
        def __init__(self, effective_threshold: _Optional[int] = ..., timestamp_usecs: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_INFO_FIELD_NUMBER: _ClassVar[int]
    CPU_EFFECTIVE_THROTTLING_DATA_FIELD_NUMBER: _ClassVar[int]
    NETWORK_EFFECTIVE_THROTTLING_DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    throttling_info: _source_throttling_pb2.SourceThrottlingConfiguration
    cpu_effective_throttling_data: _containers.RepeatedCompositeFieldContainer[FetchSourceThrottlingConfigResult.EffectiveThrottlingData]
    network_effective_throttling_data: _containers.RepeatedCompositeFieldContainer[FetchSourceThrottlingConfigResult.EffectiveThrottlingData]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., throttling_info: _Optional[_Union[_source_throttling_pb2.SourceThrottlingConfiguration, _Mapping]] = ..., cpu_effective_throttling_data: _Optional[_Iterable[_Union[FetchSourceThrottlingConfigResult.EffectiveThrottlingData, _Mapping]]] = ..., network_effective_throttling_data: _Optional[_Iterable[_Union[FetchSourceThrottlingConfigResult.EffectiveThrottlingData, _Mapping]]] = ...) -> None: ...

class SaveAgentConfigToDiskArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class SaveAgentConfigToDiskResult(_message.Message):
    __slots__ = ("error", "config_file_name", "config_file_size", "is_compressed", "config_file_timestamp", "config_format")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    config_file_name: bytes
    config_file_size: int
    is_compressed: bool
    config_file_timestamp: int
    config_format: _magneto_pb2.AgentConfigScribeStateProto.ConfigFileFormat
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., config_file_name: _Optional[bytes] = ..., config_file_size: _Optional[int] = ..., is_compressed: bool = ..., config_file_timestamp: _Optional[int] = ..., config_format: _Optional[_Union[_magneto_pb2.AgentConfigScribeStateProto.ConfigFileFormat, str]] = ...) -> None: ...

class LoadAgentConfigFromDiskArg(_message.Message):
    __slots__ = ("header", "config_file_name", "config_file_timestamp", "is_compressed", "config_format")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    config_file_name: str
    config_file_timestamp: int
    is_compressed: bool
    config_format: _magneto_pb2.AgentConfigScribeStateProto.ConfigFileFormat
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., config_file_name: _Optional[str] = ..., config_file_timestamp: _Optional[int] = ..., is_compressed: bool = ..., config_format: _Optional[_Union[_magneto_pb2.AgentConfigScribeStateProto.ConfigFileFormat, str]] = ...) -> None: ...

class LoadAgentConfigFromDiskResult(_message.Message):
    __slots__ = ("error", "invalid_config_param_count", "merge_failure_vec", "merge_conflict_vec")
    class LoadConfigFailure(_message.Message):
        __slots__ = ("config_parameter", "error")
        CONFIG_PARAMETER_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        config_parameter: str
        error: _error_pb2.ErrorProto
        def __init__(self, config_parameter: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INVALID_CONFIG_PARAM_COUNT_FIELD_NUMBER: _ClassVar[int]
    MERGE_FAILURE_VEC_FIELD_NUMBER: _ClassVar[int]
    MERGE_CONFLICT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    invalid_config_param_count: int
    merge_failure_vec: _containers.RepeatedCompositeFieldContainer[LoadAgentConfigFromDiskResult.LoadConfigFailure]
    merge_conflict_vec: _containers.RepeatedCompositeFieldContainer[LoadAgentConfigFromDiskResult.LoadConfigFailure]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., invalid_config_param_count: _Optional[int] = ..., merge_failure_vec: _Optional[_Iterable[_Union[LoadAgentConfigFromDiskResult.LoadConfigFailure, _Mapping]]] = ..., merge_conflict_vec: _Optional[_Iterable[_Union[LoadAgentConfigFromDiskResult.LoadConfigFailure, _Mapping]]] = ...) -> None: ...

class WriteFileArg(_message.Message):
    __slots__ = ("header", "file_path", "offset", "size", "data", "is_compressed")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_path: str
    offset: int
    size: int
    data: bytes
    is_compressed: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_path: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., data: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class PerformCoBMRActionArg(_message.Message):
    __slots__ = ("header", "action_type")
    class CoBMRActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStartCoBMRCfg: _ClassVar[PerformCoBMRActionArg.CoBMRActionType]
        kGetCoBMRProgress: _ClassVar[PerformCoBMRActionArg.CoBMRActionType]
    kStartCoBMRCfg: PerformCoBMRActionArg.CoBMRActionType
    kGetCoBMRProgress: PerformCoBMRActionArg.CoBMRActionType
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    action_type: PerformCoBMRActionArg.CoBMRActionType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., action_type: _Optional[_Union[PerformCoBMRActionArg.CoBMRActionType, str]] = ...) -> None: ...

class PerformCoBMRActionResult(_message.Message):
    __slots__ = ("error", "finished")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    finished: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., finished: bool = ...) -> None: ...
