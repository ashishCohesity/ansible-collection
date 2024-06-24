from magneto.agents.base import error_pb2 as _error_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentInfoProto(_message.Message):
    __slots__ = ("source_entity_id", "host_type", "agent_id", "api_version", "incarnation_id", "cluster_id", "cluster_incarnation_id", "cluster_name", "ip_addr_str_vec", "agent_sw_version_str", "os_version", "os_name", "state", "agent_uid", "agent_type", "hostname", "registered_cluster_vec", "ipaddr_to_subnet_id_vec", "task_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUninstalled: _ClassVar[AgentInfoProto.State]
        kInstalling: _ClassVar[AgentInfoProto.State]
        kInstalled: _ClassVar[AgentInfoProto.State]
        kHealthy: _ClassVar[AgentInfoProto.State]
        kUnhealthy: _ClassVar[AgentInfoProto.State]
    kUninstalled: AgentInfoProto.State
    kInstalling: AgentInfoProto.State
    kInstalled: AgentInfoProto.State
    kHealthy: AgentInfoProto.State
    kUnhealthy: AgentInfoProto.State
    class AgentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCpp: _ClassVar[AgentInfoProto.AgentType]
    kCpp: AgentInfoProto.AgentType
    class RegisteredCluster(_message.Message):
        __slots__ = ("cluster_id", "cluster_incarnation_id", "cluster_name")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_id: int
        cluster_incarnation_id: int
        cluster_name: str
        def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ...) -> None: ...
    class IPAddrToSubnetId(_message.Message):
        __slots__ = ("ip_addr", "subnet_id")
        IP_ADDR_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        ip_addr: str
        subnet_id: str
        def __init__(self, ip_addr: _Optional[str] = ..., subnet_id: _Optional[str] = ...) -> None: ...
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_SW_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    IPADDR_TO_SUBNET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    source_entity_id: int
    host_type: _enums_pb2.HostEnv.Type
    agent_id: int
    api_version: int
    incarnation_id: int
    cluster_id: int
    cluster_incarnation_id: int
    cluster_name: str
    ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    agent_sw_version_str: str
    os_version: str
    os_name: str
    state: AgentInfoProto.State
    agent_uid: _universal_id_pb2.UniversalIdProto
    agent_type: AgentInfoProto.AgentType
    hostname: str
    registered_cluster_vec: _containers.RepeatedCompositeFieldContainer[AgentInfoProto.RegisteredCluster]
    ipaddr_to_subnet_id_vec: _containers.RepeatedCompositeFieldContainer[AgentInfoProto.IPAddrToSubnetId]
    task_id: int
    def __init__(self, source_entity_id: _Optional[int] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., agent_id: _Optional[int] = ..., api_version: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., ip_addr_str_vec: _Optional[_Iterable[str]] = ..., agent_sw_version_str: _Optional[str] = ..., os_version: _Optional[str] = ..., os_name: _Optional[str] = ..., state: _Optional[_Union[AgentInfoProto.State, str]] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., agent_type: _Optional[_Union[AgentInfoProto.AgentType, str]] = ..., hostname: _Optional[str] = ..., registered_cluster_vec: _Optional[_Iterable[_Union[AgentInfoProto.RegisteredCluster, _Mapping]]] = ..., ipaddr_to_subnet_id_vec: _Optional[_Iterable[_Union[AgentInfoProto.IPAddrToSubnetId, _Mapping]]] = ..., task_id: _Optional[int] = ...) -> None: ...

class VolumeInfoProto(_message.Message):
    __slots__ = ("path", "volume_guid", "volume_label", "logical_size_bytes", "used_size_bytes", "mount_point_vec", "mount_type")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    volume_guid: bytes
    volume_label: str
    logical_size_bytes: int
    used_size_bytes: int
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    mount_type: str
    def __init__(self, path: _Optional[bytes] = ..., volume_guid: _Optional[bytes] = ..., volume_label: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., mount_type: _Optional[str] = ...) -> None: ...

class VolumeInfoSummaryProto(_message.Message):
    __slots__ = ("volume_guid", "mount_point_vec", "logical_size_bytes", "used_size_bytes")
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    volume_guid: bytes
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    logical_size_bytes: int
    used_size_bytes: int
    def __init__(self, volume_guid: _Optional[bytes] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., logical_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ...) -> None: ...

class HostInfo(_message.Message):
    __slots__ = ("volume_info_vec", "process_memory_usage_mb", "system_resource_info")
    Extensions: _python_message._ExtensionDict
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MEMORY_USAGE_MB_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfoProto]
    process_memory_usage_mb: int
    system_resource_info: _common_pb2.SystemResourceInfo
    def __init__(self, volume_info_vec: _Optional[_Iterable[_Union[VolumeInfoProto, _Mapping]]] = ..., process_memory_usage_mb: _Optional[int] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ...) -> None: ...

class HostInfoSummary(_message.Message):
    __slots__ = ("volume_info_summary_vec",)
    Extensions: _python_message._ExtensionDict
    VOLUME_INFO_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_info_summary_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfoSummaryProto]
    def __init__(self, volume_info_summary_vec: _Optional[_Iterable[_Union[VolumeInfoSummaryProto, _Mapping]]] = ...) -> None: ...
