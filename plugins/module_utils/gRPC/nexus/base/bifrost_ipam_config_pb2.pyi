from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostIpamVec(_message.Message):
    __slots__ = ("ipam_conf_vec", "node_facing_vlan_ips_bitset", "node_facing_vlan_start_ip", "mac_bitset", "bifrost_config_start_mac")
    class IpamConf(_message.Message):
        __slots__ = ("interface_group", "vlan_tag", "tenant_id", "node_facing_ip_mac_vec", "tenant_facing_ip_mac_vec")
        class IpMacMapping(_message.Message):
            __slots__ = ("ip", "mac", "container_id", "if_name", "network_id", "pod_namespace", "pod_name", "node_id")
            IP_FIELD_NUMBER: _ClassVar[int]
            MAC_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
            IF_NAME_FIELD_NUMBER: _ClassVar[int]
            NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
            POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
            POD_NAME_FIELD_NUMBER: _ClassVar[int]
            NODE_ID_FIELD_NUMBER: _ClassVar[int]
            ip: str
            mac: str
            container_id: str
            if_name: str
            network_id: str
            pod_namespace: str
            pod_name: str
            node_id: str
            def __init__(self, ip: _Optional[str] = ..., mac: _Optional[str] = ..., container_id: _Optional[str] = ..., if_name: _Optional[str] = ..., network_id: _Optional[str] = ..., pod_namespace: _Optional[str] = ..., pod_name: _Optional[str] = ..., node_id: _Optional[str] = ...) -> None: ...
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        VLAN_TAG_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_FACING_IP_MAC_VEC_FIELD_NUMBER: _ClassVar[int]
        TENANT_FACING_IP_MAC_VEC_FIELD_NUMBER: _ClassVar[int]
        interface_group: str
        vlan_tag: int
        tenant_id: str
        node_facing_ip_mac_vec: _containers.RepeatedCompositeFieldContainer[BifrostIpamVec.IpamConf.IpMacMapping]
        tenant_facing_ip_mac_vec: _containers.RepeatedCompositeFieldContainer[BifrostIpamVec.IpamConf.IpMacMapping]
        def __init__(self, interface_group: _Optional[str] = ..., vlan_tag: _Optional[int] = ..., tenant_id: _Optional[str] = ..., node_facing_ip_mac_vec: _Optional[_Iterable[_Union[BifrostIpamVec.IpamConf.IpMacMapping, _Mapping]]] = ..., tenant_facing_ip_mac_vec: _Optional[_Iterable[_Union[BifrostIpamVec.IpamConf.IpMacMapping, _Mapping]]] = ...) -> None: ...
    IPAM_CONF_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_FACING_VLAN_IPS_BITSET_FIELD_NUMBER: _ClassVar[int]
    NODE_FACING_VLAN_START_IP_FIELD_NUMBER: _ClassVar[int]
    MAC_BITSET_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONFIG_START_MAC_FIELD_NUMBER: _ClassVar[int]
    ipam_conf_vec: _containers.RepeatedCompositeFieldContainer[BifrostIpamVec.IpamConf]
    node_facing_vlan_ips_bitset: _containers.RepeatedScalarFieldContainer[int]
    node_facing_vlan_start_ip: str
    mac_bitset: _containers.RepeatedScalarFieldContainer[int]
    bifrost_config_start_mac: str
    def __init__(self, ipam_conf_vec: _Optional[_Iterable[_Union[BifrostIpamVec.IpamConf, _Mapping]]] = ..., node_facing_vlan_ips_bitset: _Optional[_Iterable[int]] = ..., node_facing_vlan_start_ip: _Optional[str] = ..., mac_bitset: _Optional[_Iterable[int]] = ..., bifrost_config_start_mac: _Optional[str] = ...) -> None: ...
