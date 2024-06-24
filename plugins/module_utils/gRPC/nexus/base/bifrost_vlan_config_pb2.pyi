from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostVlanVec(_message.Message):
    __slots__ = ("vlan_conf_vec",)
    class VlanConf(_message.Message):
        __slots__ = ("interface_group", "vlan_tag", "tenant_id", "type", "vlan_name", "subnet", "description", "mtu", "state")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INTERNAL: _ClassVar[BifrostVlanVec.VlanConf.Type]
            EXTERNAL: _ClassVar[BifrostVlanVec.VlanConf.Type]
        INTERNAL: BifrostVlanVec.VlanConf.Type
        EXTERNAL: BifrostVlanVec.VlanConf.Type
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[BifrostVlanVec.VlanConf.State]
            ACTIVE: _ClassVar[BifrostVlanVec.VlanConf.State]
            DISABLED: _ClassVar[BifrostVlanVec.VlanConf.State]
            DELETING: _ClassVar[BifrostVlanVec.VlanConf.State]
        UNKNOWN: BifrostVlanVec.VlanConf.State
        ACTIVE: BifrostVlanVec.VlanConf.State
        DISABLED: BifrostVlanVec.VlanConf.State
        DELETING: BifrostVlanVec.VlanConf.State
        class Subnet(_message.Message):
            __slots__ = ("ip_cidr", "netmask_bits", "netmask_ip4", "gateway", "ip_addresses")
            IP_CIDR_FIELD_NUMBER: _ClassVar[int]
            NETMASK_BITS_FIELD_NUMBER: _ClassVar[int]
            NETMASK_IP4_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            ip_cidr: str
            netmask_bits: int
            netmask_ip4: str
            gateway: str
            ip_addresses: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, ip_cidr: _Optional[str] = ..., netmask_bits: _Optional[int] = ..., netmask_ip4: _Optional[str] = ..., gateway: _Optional[str] = ..., ip_addresses: _Optional[_Iterable[str]] = ...) -> None: ...
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        VLAN_TAG_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VLAN_NAME_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MTU_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        interface_group: str
        vlan_tag: int
        tenant_id: str
        type: BifrostVlanVec.VlanConf.Type
        vlan_name: str
        subnet: _containers.RepeatedCompositeFieldContainer[BifrostVlanVec.VlanConf.Subnet]
        description: str
        mtu: int
        state: BifrostVlanVec.VlanConf.State
        def __init__(self, interface_group: _Optional[str] = ..., vlan_tag: _Optional[int] = ..., tenant_id: _Optional[str] = ..., type: _Optional[_Union[BifrostVlanVec.VlanConf.Type, str]] = ..., vlan_name: _Optional[str] = ..., subnet: _Optional[_Iterable[_Union[BifrostVlanVec.VlanConf.Subnet, _Mapping]]] = ..., description: _Optional[str] = ..., mtu: _Optional[int] = ..., state: _Optional[_Union[BifrostVlanVec.VlanConf.State, str]] = ...) -> None: ...
    VLAN_CONF_VEC_FIELD_NUMBER: _ClassVar[int]
    vlan_conf_vec: _containers.RepeatedCompositeFieldContainer[BifrostVlanVec.VlanConf]
    def __init__(self, vlan_conf_vec: _Optional[_Iterable[_Union[BifrostVlanVec.VlanConf, _Mapping]]] = ...) -> None: ...
