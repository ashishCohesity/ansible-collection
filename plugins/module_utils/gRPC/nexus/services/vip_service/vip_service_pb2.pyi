from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VipAssignmentProto(_message.Message):
    __slots__ = ("gandalf_key", "assignment_vec", "cluster_config_version", "vlan_ips_supported")
    class Assignment(_message.Message):
        __slots__ = ("node_id", "vip_vec", "vlan_ip_vec")
        class VlanIp(_message.Message):
            __slots__ = ("ip", "vlan_id", "netmask_bits", "interface_name", "rt_table_id", "gateway_ip", "ecmp_vip")
            IP_FIELD_NUMBER: _ClassVar[int]
            VLAN_ID_FIELD_NUMBER: _ClassVar[int]
            NETMASK_BITS_FIELD_NUMBER: _ClassVar[int]
            INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
            RT_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
            ECMP_VIP_FIELD_NUMBER: _ClassVar[int]
            ip: str
            vlan_id: int
            netmask_bits: int
            interface_name: str
            rt_table_id: int
            gateway_ip: str
            ecmp_vip: bool
            def __init__(self, ip: _Optional[str] = ..., vlan_id: _Optional[int] = ..., netmask_bits: _Optional[int] = ..., interface_name: _Optional[str] = ..., rt_table_id: _Optional[int] = ..., gateway_ip: _Optional[str] = ..., ecmp_vip: bool = ...) -> None: ...
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        VIP_VEC_FIELD_NUMBER: _ClassVar[int]
        VLAN_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        vip_vec: _containers.RepeatedScalarFieldContainer[str]
        vlan_ip_vec: _containers.RepeatedCompositeFieldContainer[VipAssignmentProto.Assignment.VlanIp]
        def __init__(self, node_id: _Optional[int] = ..., vip_vec: _Optional[_Iterable[str]] = ..., vlan_ip_vec: _Optional[_Iterable[_Union[VipAssignmentProto.Assignment.VlanIp, _Mapping]]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    VLAN_IPS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    assignment_vec: _containers.RepeatedCompositeFieldContainer[VipAssignmentProto.Assignment]
    cluster_config_version: int
    vlan_ips_supported: bool
    def __init__(self, gandalf_key: _Optional[str] = ..., assignment_vec: _Optional[_Iterable[_Union[VipAssignmentProto.Assignment, _Mapping]]] = ..., cluster_config_version: _Optional[int] = ..., vlan_ips_supported: bool = ...) -> None: ...
