from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkInterface(_message.Message):
    __slots__ = ("id", "ip_addrs")
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., ip_addrs: _Optional[_Iterable[str]] = ...) -> None: ...

class ClusterInfo(_message.Message):
    __slots__ = ("guid", "description", "version", "api_version_str", "smb_krb5_hostname")
    GUID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    SMB_KRB5_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    guid: str
    description: str
    version: str
    api_version_str: str
    smb_krb5_hostname: str
    def __init__(self, guid: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., api_version_str: _Optional[str] = ..., smb_krb5_hostname: _Optional[str] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("id", "zone_id", "path", "groupnet", "network_pools")
    class NetworkPool(_message.Message):
        __slots__ = ("access_zone", "addr_family", "alloc_method", "groupnet", "id", "name", "ranges", "sc_dns_zone", "subnet")
        class AddressFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknownAddressFamily: _ClassVar[ZoneInfo.NetworkPool.AddressFamily]
            kIPv4: _ClassVar[ZoneInfo.NetworkPool.AddressFamily]
            kIPv6: _ClassVar[ZoneInfo.NetworkPool.AddressFamily]
        kUnknownAddressFamily: ZoneInfo.NetworkPool.AddressFamily
        kIPv4: ZoneInfo.NetworkPool.AddressFamily
        kIPv6: ZoneInfo.NetworkPool.AddressFamily
        class AllocMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknownAllocMethod: _ClassVar[ZoneInfo.NetworkPool.AllocMethod]
            kStaticAllocMethod: _ClassVar[ZoneInfo.NetworkPool.AllocMethod]
            kDynamicAllocMethod: _ClassVar[ZoneInfo.NetworkPool.AllocMethod]
        kUnknownAllocMethod: ZoneInfo.NetworkPool.AllocMethod
        kStaticAllocMethod: ZoneInfo.NetworkPool.AllocMethod
        kDynamicAllocMethod: ZoneInfo.NetworkPool.AllocMethod
        class Range(_message.Message):
            __slots__ = ("low", "high")
            LOW_FIELD_NUMBER: _ClassVar[int]
            HIGH_FIELD_NUMBER: _ClassVar[int]
            low: str
            high: str
            def __init__(self, low: _Optional[str] = ..., high: _Optional[str] = ...) -> None: ...
        ACCESS_ZONE_FIELD_NUMBER: _ClassVar[int]
        ADDR_FAMILY_FIELD_NUMBER: _ClassVar[int]
        ALLOC_METHOD_FIELD_NUMBER: _ClassVar[int]
        GROUPNET_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RANGES_FIELD_NUMBER: _ClassVar[int]
        SC_DNS_ZONE_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        access_zone: str
        addr_family: ZoneInfo.NetworkPool.AddressFamily
        alloc_method: ZoneInfo.NetworkPool.AllocMethod
        groupnet: str
        id: str
        name: str
        ranges: _containers.RepeatedCompositeFieldContainer[ZoneInfo.NetworkPool.Range]
        sc_dns_zone: str
        subnet: str
        def __init__(self, access_zone: _Optional[str] = ..., addr_family: _Optional[_Union[ZoneInfo.NetworkPool.AddressFamily, str]] = ..., alloc_method: _Optional[_Union[ZoneInfo.NetworkPool.AllocMethod, str]] = ..., groupnet: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., ranges: _Optional[_Iterable[_Union[ZoneInfo.NetworkPool.Range, _Mapping]]] = ..., sc_dns_zone: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    GROUPNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POOLS_FIELD_NUMBER: _ClassVar[int]
    id: str
    zone_id: int
    path: str
    groupnet: str
    network_pools: _containers.RepeatedCompositeFieldContainer[ZoneInfo.NetworkPool]
    def __init__(self, id: _Optional[str] = ..., zone_id: _Optional[int] = ..., path: _Optional[str] = ..., groupnet: _Optional[str] = ..., network_pools: _Optional[_Iterable[_Union[ZoneInfo.NetworkPool, _Mapping]]] = ...) -> None: ...

class MountPointInfo(_message.Message):
    __slots__ = ("supported_protocol_vec", "path", "smb_info_vec", "nfs_info", "zone_id", "groupnet")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfs: _ClassVar[MountPointInfo.Type]
        kSmb: _ClassVar[MountPointInfo.Type]
    kNfs: MountPointInfo.Type
    kSmb: MountPointInfo.Type
    class SmbInfo(_message.Message):
        __slots__ = ("id", "description", "zone_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        description: str
        zone_id: int
        def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., zone_id: _Optional[int] = ...) -> None: ...
    class NfsInfo(_message.Message):
        __slots__ = ("id", "description", "zone_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        id: int
        description: str
        zone_id: str
        def __init__(self, id: _Optional[int] = ..., description: _Optional[str] = ..., zone_id: _Optional[str] = ...) -> None: ...
    SUPPORTED_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NFS_INFO_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPNET_FIELD_NUMBER: _ClassVar[int]
    supported_protocol_vec: _containers.RepeatedScalarFieldContainer[MountPointInfo.Type]
    path: str
    smb_info_vec: _containers.RepeatedCompositeFieldContainer[MountPointInfo.SmbInfo]
    nfs_info: MountPointInfo.NfsInfo
    zone_id: str
    groupnet: str
    def __init__(self, supported_protocol_vec: _Optional[_Iterable[_Union[MountPointInfo.Type, str]]] = ..., path: _Optional[str] = ..., smb_info_vec: _Optional[_Iterable[_Union[MountPointInfo.SmbInfo, _Mapping]]] = ..., nfs_info: _Optional[_Union[MountPointInfo.NfsInfo, _Mapping]] = ..., zone_id: _Optional[str] = ..., groupnet: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "cluster_info", "zone_info", "mount_point_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kZone: _ClassVar[Entity.Type]
        kMountPoint: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kZone: Entity.Type
    kMountPoint: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    cluster_info: ClusterInfo
    zone_info: ZoneInfo
    mount_point_info: MountPointInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., zone_info: _Optional[_Union[ZoneInfo, _Mapping]] = ..., mount_point_info: _Optional[_Union[MountPointInfo, _Mapping]] = ...) -> None: ...
