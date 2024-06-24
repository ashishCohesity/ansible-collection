from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kZone: _ClassVar[GroupType]
    kBgpConfig: _ClassVar[GroupType]
    kOspfConfig: _ClassVar[GroupType]
    kDns: _ClassVar[GroupType]
kZone: GroupType
kBgpConfig: GroupType
kOspfConfig: GroupType
kDns: GroupType

class Subnet(_message.Message):
    __slots__ = ("ip", "netmask_bits", "netmask_ip4", "gateway")
    IP_FIELD_NUMBER: _ClassVar[int]
    NETMASK_BITS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_IP4_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    ip: str
    netmask_bits: int
    netmask_ip4: str
    gateway: str
    def __init__(self, ip: _Optional[str] = ..., netmask_bits: _Optional[int] = ..., netmask_ip4: _Optional[str] = ..., gateway: _Optional[str] = ...) -> None: ...

class OspfConfig(_message.Message):
    __slots__ = ("instances", "shutdown")
    class Authentication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        None: _ClassVar[OspfConfig.Authentication]
        AuthenticationSimple: _ClassVar[OspfConfig.Authentication]
        AuthenticationMessageDigest: _ClassVar[OspfConfig.Authentication]
    None: OspfConfig.Authentication
    AuthenticationSimple: OspfConfig.Authentication
    AuthenticationMessageDigest: OspfConfig.Authentication
    class Area(_message.Message):
        __slots__ = ("id", "default_cost", "authentication_type")
        ID_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_COST_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: int
        default_cost: int
        authentication_type: OspfConfig.Authentication
        def __init__(self, id: _Optional[int] = ..., default_cost: _Optional[int] = ..., authentication_type: _Optional[_Union[OspfConfig.Authentication, str]] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("destination", "area_id")
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        AREA_ID_FIELD_NUMBER: _ClassVar[int]
        destination: Subnet
        area_id: int
        def __init__(self, destination: _Optional[_Union[Subnet, _Mapping]] = ..., area_id: _Optional[int] = ...) -> None: ...
    class Interface(_message.Message):
        __slots__ = ("node_id", "interface_name", "area_id", "cost", "priority", "hello_interval", "dead_interval", "retransmit_interval", "transmit_delay", "authentication_type", "authentication_key", "authenticaion_message_digest", "md_key", "md_key_id")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        AREA_ID_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        HELLO_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        DEAD_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        RETRANSMIT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        TRANSMIT_DELAY_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_KEY_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICAION_MESSAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
        MD_KEY_FIELD_NUMBER: _ClassVar[int]
        MD_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        interface_name: str
        area_id: int
        cost: int
        priority: int
        hello_interval: int
        dead_interval: int
        retransmit_interval: int
        transmit_delay: int
        authentication_type: OspfConfig.Authentication
        authentication_key: str
        authenticaion_message_digest: bool
        md_key: str
        md_key_id: str
        def __init__(self, node_id: _Optional[int] = ..., interface_name: _Optional[str] = ..., area_id: _Optional[int] = ..., cost: _Optional[int] = ..., priority: _Optional[int] = ..., hello_interval: _Optional[int] = ..., dead_interval: _Optional[int] = ..., retransmit_interval: _Optional[int] = ..., transmit_delay: _Optional[int] = ..., authentication_type: _Optional[_Union[OspfConfig.Authentication, str]] = ..., authentication_key: _Optional[str] = ..., authenticaion_message_digest: bool = ..., md_key: _Optional[str] = ..., md_key_id: _Optional[str] = ...) -> None: ...
    class Instance(_message.Message):
        __slots__ = ("id", "router_id", "areas", "networks", "interfaces", "shutdown")
        ID_FIELD_NUMBER: _ClassVar[int]
        ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
        AREAS_FIELD_NUMBER: _ClassVar[int]
        NETWORKS_FIELD_NUMBER: _ClassVar[int]
        INTERFACES_FIELD_NUMBER: _ClassVar[int]
        SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        id: int
        router_id: str
        areas: _containers.RepeatedCompositeFieldContainer[OspfConfig.Area]
        networks: _containers.RepeatedCompositeFieldContainer[OspfConfig.Network]
        interfaces: _containers.RepeatedCompositeFieldContainer[OspfConfig.Interface]
        shutdown: bool
        def __init__(self, id: _Optional[int] = ..., router_id: _Optional[str] = ..., areas: _Optional[_Iterable[_Union[OspfConfig.Area, _Mapping]]] = ..., networks: _Optional[_Iterable[_Union[OspfConfig.Network, _Mapping]]] = ..., interfaces: _Optional[_Iterable[_Union[OspfConfig.Interface, _Mapping]]] = ..., shutdown: bool = ...) -> None: ...
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[OspfConfig.Instance]
    shutdown: bool
    def __init__(self, instances: _Optional[_Iterable[_Union[OspfConfig.Instance, _Mapping]]] = ..., shutdown: bool = ...) -> None: ...

class BgpConfig(_message.Message):
    __slots__ = ("instances", "shutdown")
    class Network(_message.Message):
        __slots__ = ("destination",)
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        destination: Subnet
        def __init__(self, destination: _Optional[_Union[Subnet, _Mapping]] = ...) -> None: ...
    class Peer(_message.Message):
        __slots__ = ("address_or_tag", "bgp_multihop", "description", "remote_as", "peer_group", "keepalive_interval", "hold_timer", "shutdown", "export_match_interfaces")
        ADDRESS_OR_TAG_FIELD_NUMBER: _ClassVar[int]
        BGP_MULTIHOP_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        REMOTE_AS_FIELD_NUMBER: _ClassVar[int]
        PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
        KEEPALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        HOLD_TIMER_FIELD_NUMBER: _ClassVar[int]
        SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        EXPORT_MATCH_INTERFACES_FIELD_NUMBER: _ClassVar[int]
        address_or_tag: str
        bgp_multihop: bool
        description: str
        remote_as: int
        peer_group: str
        keepalive_interval: int
        hold_timer: int
        shutdown: bool
        export_match_interfaces: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, address_or_tag: _Optional[str] = ..., bgp_multihop: bool = ..., description: _Optional[str] = ..., remote_as: _Optional[int] = ..., peer_group: _Optional[str] = ..., keepalive_interval: _Optional[int] = ..., hold_timer: _Optional[int] = ..., shutdown: bool = ..., export_match_interfaces: _Optional[_Iterable[str]] = ...) -> None: ...
    class Instance(_message.Message):
        __slots__ = ("local_as", "router_id", "networks", "peers", "keepalive_interval", "hold_timer", "shutdown", "redistribute_connected")
        LOCAL_AS_FIELD_NUMBER: _ClassVar[int]
        ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORKS_FIELD_NUMBER: _ClassVar[int]
        PEERS_FIELD_NUMBER: _ClassVar[int]
        KEEPALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        HOLD_TIMER_FIELD_NUMBER: _ClassVar[int]
        SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        REDISTRIBUTE_CONNECTED_FIELD_NUMBER: _ClassVar[int]
        local_as: int
        router_id: str
        networks: _containers.RepeatedCompositeFieldContainer[BgpConfig.Network]
        peers: _containers.RepeatedCompositeFieldContainer[BgpConfig.Peer]
        keepalive_interval: int
        hold_timer: int
        shutdown: bool
        redistribute_connected: bool
        def __init__(self, local_as: _Optional[int] = ..., router_id: _Optional[str] = ..., networks: _Optional[_Iterable[_Union[BgpConfig.Network, _Mapping]]] = ..., peers: _Optional[_Iterable[_Union[BgpConfig.Peer, _Mapping]]] = ..., keepalive_interval: _Optional[int] = ..., hold_timer: _Optional[int] = ..., shutdown: bool = ..., redistribute_connected: bool = ...) -> None: ...
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[BgpConfig.Instance]
    shutdown: bool
    def __init__(self, instances: _Optional[_Iterable[_Union[BgpConfig.Instance, _Mapping]]] = ..., shutdown: bool = ...) -> None: ...

class RipConfig(_message.Message):
    __slots__ = ("networks", "shutdown")
    class Network(_message.Message):
        __slots__ = ("destination",)
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        destination: Subnet
        def __init__(self, destination: _Optional[_Union[Subnet, _Mapping]] = ...) -> None: ...
    class Interface(_message.Message):
        __slots__ = ("node_id", "interface_name", "shutdown")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        interface_name: str
        shutdown: bool
        def __init__(self, node_id: _Optional[int] = ..., interface_name: _Optional[str] = ..., shutdown: bool = ...) -> None: ...
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[RipConfig.Network]
    shutdown: bool
    def __init__(self, networks: _Optional[_Iterable[_Union[RipConfig.Network, _Mapping]]] = ..., shutdown: bool = ...) -> None: ...

class ZoneProperties(_message.Message):
    __slots__ = ("primary_subnet", "route_vec")
    PRIMARY_SUBNET_FIELD_NUMBER: _ClassVar[int]
    ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    primary_subnet: Subnet
    route_vec: _containers.RepeatedCompositeFieldContainer[RouteConfig]
    def __init__(self, primary_subnet: _Optional[_Union[Subnet, _Mapping]] = ..., route_vec: _Optional[_Iterable[_Union[RouteConfig, _Mapping]]] = ...) -> None: ...

class DnsProperties(_message.Message):
    __slots__ = ("dns_server_vec",)
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dns_server_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RouteConfig(_message.Message):
    __slots__ = ("dest_network", "next_hop", "interface_group", "source_ip", "mtu", "description", "adv_mss")
    DEST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADV_MSS_FIELD_NUMBER: _ClassVar[int]
    dest_network: Subnet
    next_hop: str
    interface_group: str
    source_ip: str
    mtu: int
    description: str
    adv_mss: int
    def __init__(self, dest_network: _Optional[_Union[Subnet, _Mapping]] = ..., next_hop: _Optional[str] = ..., interface_group: _Optional[str] = ..., source_ip: _Optional[str] = ..., mtu: _Optional[int] = ..., description: _Optional[str] = ..., adv_mss: _Optional[int] = ...) -> None: ...

class NodeGroup(_message.Message):
    __slots__ = ("id", "name", "type", "node_ids", "zone", "dns", "bgp_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    BGP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: GroupType
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    zone: ZoneProperties
    dns: DnsProperties
    bgp_config: BgpConfig
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[GroupType, str]] = ..., node_ids: _Optional[_Iterable[int]] = ..., zone: _Optional[_Union[ZoneProperties, _Mapping]] = ..., dns: _Optional[_Union[DnsProperties, _Mapping]] = ..., bgp_config: _Optional[_Union[BgpConfig, _Mapping]] = ...) -> None: ...

class NodeNetworkProto(_message.Message):
    __slots__ = ("id", "bgp_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    BGP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: int
    bgp_config: BgpConfig
    def __init__(self, id: _Optional[int] = ..., bgp_config: _Optional[_Union[BgpConfig, _Mapping]] = ...) -> None: ...
