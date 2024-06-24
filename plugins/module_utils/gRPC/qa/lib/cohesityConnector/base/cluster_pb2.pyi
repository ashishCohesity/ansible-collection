from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeInfo(_message.Message):
    __slots__ = ("ip", "ipmi_ip", "id")
    IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ip: str
    ipmi_ip: str
    id: int
    def __init__(self, ip: _Optional[str] = ..., ipmi_ip: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class ClusterPartitionCreateParams(_message.Message):
    __slots__ = ("name", "nodes", "vips", "hostname")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    VIPS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    nodes: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    vips: _containers.RepeatedScalarFieldContainer[str]
    hostname: str
    def __init__(self, name: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., vips: _Optional[_Iterable[str]] = ..., hostname: _Optional[str] = ...) -> None: ...

class PackageInfo(_message.Message):
    __slots__ = ("version", "package_url", "md5sum")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_URL_FIELD_NUMBER: _ClassVar[int]
    MD5SUM_FIELD_NUMBER: _ClassVar[int]
    version: str
    package_url: str
    md5sum: str
    def __init__(self, version: _Optional[str] = ..., package_url: _Optional[str] = ..., md5sum: _Optional[str] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("ip", "mask_ip")
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    mask_ip: str
    def __init__(self, ip: _Optional[str] = ..., mask_ip: _Optional[str] = ...) -> None: ...

class ClusterCreateParams(_message.Message):
    __slots__ = ("cluster_name", "nodes", "host_subnet", "ipmi_subnet", "ipmi_user_name", "ipmi_password", "ntp_servers", "dns_servers", "domain_names", "enable_software_encryption", "enable_hardware_encryption", "rotation_period", "cluster_partitions", "nfs_whitelisted_subnet", "ignore_sw_incompatibility", "package")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    HOST_SUBNET_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_FIELD_NUMBER: _ClassVar[int]
    IPMI_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    IPMI_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SOFTWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    NFS_WHITELISTED_SUBNET_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SW_INCOMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    nodes: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    host_subnet: Subnet
    ipmi_subnet: Subnet
    ipmi_user_name: str
    ipmi_password: str
    ntp_servers: _containers.RepeatedScalarFieldContainer[str]
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    domain_names: _containers.RepeatedScalarFieldContainer[str]
    enable_software_encryption: bool
    enable_hardware_encryption: bool
    rotation_period: int
    cluster_partitions: _containers.RepeatedCompositeFieldContainer[ClusterPartitionCreateParams]
    nfs_whitelisted_subnet: _containers.RepeatedCompositeFieldContainer[Subnet]
    ignore_sw_incompatibility: bool
    package: PackageInfo
    def __init__(self, cluster_name: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., host_subnet: _Optional[_Union[Subnet, _Mapping]] = ..., ipmi_subnet: _Optional[_Union[Subnet, _Mapping]] = ..., ipmi_user_name: _Optional[str] = ..., ipmi_password: _Optional[str] = ..., ntp_servers: _Optional[_Iterable[str]] = ..., dns_servers: _Optional[_Iterable[str]] = ..., domain_names: _Optional[_Iterable[str]] = ..., enable_software_encryption: bool = ..., enable_hardware_encryption: bool = ..., rotation_period: _Optional[int] = ..., cluster_partitions: _Optional[_Iterable[_Union[ClusterPartitionCreateParams, _Mapping]]] = ..., nfs_whitelisted_subnet: _Optional[_Iterable[_Union[Subnet, _Mapping]]] = ..., ignore_sw_incompatibility: bool = ..., package: _Optional[_Union[PackageInfo, _Mapping]] = ...) -> None: ...
