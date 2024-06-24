from magneto.base import common_pb2 as _common_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base.entities import agent_pb2 as _agent_pb2_1
from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhysicalUID(_message.Message):
    __slots__ = ("part1", "part2", "part3")
    PART1_FIELD_NUMBER: _ClassVar[int]
    PART2_FIELD_NUMBER: _ClassVar[int]
    PART3_FIELD_NUMBER: _ClassVar[int]
    part1: int
    part2: int
    part3: int
    def __init__(self, part1: _Optional[int] = ..., part2: _Optional[int] = ..., part3: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uid", "name", "host_type", "os_name", "volume_info_vec", "unsupported_path_vec", "vhdx_recovery_supported", "networking_info", "agent_status_vec", "agent_entity_id_DEPRECATED", "system_resource_info", "hostname", "vcs_version", "vlan_params", "vss_writer_info_vec", "is_proxy_machine", "cbmr_version", "proxy_ref_count", "cluster_source_type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGroup: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
        kWindowsCluster: _ClassVar[Entity.Type]
        kOracleRACCluster: _ClassVar[Entity.Type]
        kOracleAPCluster: _ClassVar[Entity.Type]
    kGroup: Entity.Type
    kHost: Entity.Type
    kWindowsCluster: Entity.Type
    kOracleRACCluster: Entity.Type
    kOracleAPCluster: Entity.Type
    class VolumeInfo(_message.Message):
        __slots__ = ("volume_guid", "device_path", "network_path", "logical_size_bytes", "used_size_bytes", "mount_point_vec", "volume_label", "is_protected", "extended_attributes_supported", "is_boot_volume", "mount_type", "is_shared_volume", "is_cohesity_mount_volume", "is_refs_volume", "volume_count")
        VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
        NETWORK_PATH_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
        VOLUME_LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTRIBUTES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        IS_BOOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
        MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_SHARED_VOLUME_FIELD_NUMBER: _ClassVar[int]
        IS_COHESITY_MOUNT_VOLUME_FIELD_NUMBER: _ClassVar[int]
        IS_REFS_VOLUME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
        volume_guid: str
        device_path: str
        network_path: str
        logical_size_bytes: int
        used_size_bytes: int
        mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
        volume_label: str
        is_protected: bool
        extended_attributes_supported: bool
        is_boot_volume: bool
        mount_type: str
        is_shared_volume: bool
        is_cohesity_mount_volume: bool
        is_refs_volume: bool
        volume_count: int
        def __init__(self, volume_guid: _Optional[str] = ..., device_path: _Optional[str] = ..., network_path: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., volume_label: _Optional[str] = ..., is_protected: bool = ..., extended_attributes_supported: bool = ..., is_boot_volume: bool = ..., mount_type: _Optional[str] = ..., is_shared_volume: bool = ..., is_cohesity_mount_volume: bool = ..., is_refs_volume: bool = ..., volume_count: _Optional[int] = ...) -> None: ...
    class VssWriterInfo(_message.Message):
        __slots__ = ("vss_writer_name", "is_default_excluded")
        VSS_WRITER_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        vss_writer_name: str
        is_default_excluded: bool
        def __init__(self, vss_writer_name: _Optional[str] = ..., is_default_excluded: bool = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    UNSUPPORTED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    VHDX_RECOVERY_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENTITY_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    VCS_VERSION_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VSS_WRITER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_PROXY_MACHINE_FIELD_NUMBER: _ClassVar[int]
    CBMR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROXY_REF_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uid: PhysicalUID
    name: str
    host_type: _enums_pb2.HostEnv.Type
    os_name: str
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[Entity.VolumeInfo]
    unsupported_path_vec: _containers.RepeatedScalarFieldContainer[str]
    vhdx_recovery_supported: bool
    networking_info: _agent_pb2.ClusterNetworkingInfo
    agent_status_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2_1.HostAgentStatus]
    agent_entity_id_DEPRECATED: int
    system_resource_info: _common_pb2.SystemResourceInfo
    hostname: str
    vcs_version: str
    vlan_params: _common_pb2.VlanParams
    vss_writer_info_vec: _containers.RepeatedCompositeFieldContainer[Entity.VssWriterInfo]
    is_proxy_machine: bool
    cbmr_version: str
    proxy_ref_count: int
    cluster_source_type: _agent_pb2.ClusterNetworkingInfo.Resource.Type
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uid: _Optional[_Union[PhysicalUID, _Mapping]] = ..., name: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., os_name: _Optional[str] = ..., volume_info_vec: _Optional[_Iterable[_Union[Entity.VolumeInfo, _Mapping]]] = ..., unsupported_path_vec: _Optional[_Iterable[str]] = ..., vhdx_recovery_supported: bool = ..., networking_info: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo, _Mapping]] = ..., agent_status_vec: _Optional[_Iterable[_Union[_agent_pb2_1.HostAgentStatus, _Mapping]]] = ..., agent_entity_id_DEPRECATED: _Optional[int] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ..., hostname: _Optional[str] = ..., vcs_version: _Optional[str] = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., vss_writer_info_vec: _Optional[_Iterable[_Union[Entity.VssWriterInfo, _Mapping]]] = ..., is_proxy_machine: bool = ..., cbmr_version: _Optional[str] = ..., proxy_ref_count: _Optional[int] = ..., cluster_source_type: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource.Type, str]] = ...) -> None: ...
