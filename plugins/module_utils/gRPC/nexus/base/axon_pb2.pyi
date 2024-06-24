from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StateRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[StateRange]
    CREATING: _ClassVar[StateRange]
    DELETING: _ClassVar[StateRange]
    UPDATING_START: _ClassVar[StateRange]
    UPDATING_END: _ClassVar[StateRange]
    UPDATING_MASK: _ClassVar[StateRange]
    PROGRESS_START: _ClassVar[StateRange]
    PROGRESS_END: _ClassVar[StateRange]
    PROGRESS_MASK: _ClassVar[StateRange]
    CREATED: _ClassVar[StateRange]
    DELETED: _ClassVar[StateRange]
    COMPLETION_START: _ClassVar[StateRange]
    COMPLETION_END: _ClassVar[StateRange]
    COMPLETION_MASK: _ClassVar[StateRange]
    SPECIAL_UPDATING_START: _ClassVar[StateRange]
    SPECIAL_UPDATING_END: _ClassVar[StateRange]
    ERROR: _ClassVar[StateRange]
    CLEANING_ON_ERROR: _ClassVar[StateRange]
    SPECIAL_START: _ClassVar[StateRange]
    SPECIAL_END: _ClassVar[StateRange]
    SPECIAL_MASK: _ClassVar[StateRange]

class IPAMType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[IPAMType]
    OVN: _ClassVar[IPAMType]
    ATHENA: _ClassVar[IPAMType]
    BIFROST_NODEFACING_CNI: _ClassVar[IPAMType]
    BIFROST_NODEFACING_SERVICEACCESS: _ClassVar[IPAMType]
    BIFROST_TENANTFACING_CNI: _ClassVar[IPAMType]
    TEST: _ClassVar[IPAMType]
UNKNOWN: StateRange
CREATING: StateRange
DELETING: StateRange
UPDATING_START: StateRange
UPDATING_END: StateRange
UPDATING_MASK: StateRange
PROGRESS_START: StateRange
PROGRESS_END: StateRange
PROGRESS_MASK: StateRange
CREATED: StateRange
DELETED: StateRange
COMPLETION_START: StateRange
COMPLETION_END: StateRange
COMPLETION_MASK: StateRange
SPECIAL_UPDATING_START: StateRange
SPECIAL_UPDATING_END: StateRange
ERROR: StateRange
CLEANING_ON_ERROR: StateRange
SPECIAL_START: StateRange
SPECIAL_END: StateRange
SPECIAL_MASK: StateRange
UNDEFINED: IPAMType
OVN: IPAMType
ATHENA: IPAMType
BIFROST_NODEFACING_CNI: IPAMType
BIFROST_NODEFACING_SERVICEACCESS: IPAMType
BIFROST_TENANTFACING_CNI: IPAMType
TEST: IPAMType

class AxonError(_message.Message):
    __slots__ = ("code", "timestamp", "summary", "details", "debug_info", "request_id")
    CODE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    code: int
    timestamp: int
    summary: str
    details: str
    debug_info: bytes
    request_id: str
    def __init__(self, code: _Optional[int] = ..., timestamp: _Optional[int] = ..., summary: _Optional[str] = ..., details: _Optional[str] = ..., debug_info: _Optional[bytes] = ..., request_id: _Optional[str] = ...) -> None: ...

class Network(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "ports", "subnet_ids", "tenant_id", "type", "mtu", "metadata", "allow_all_tenants", "provider", "no_l3_host_connectivity", "default_ipam_type", "state", "error", "last_request_id", "version", "force_set_reason", "try_update_recovery", "is_custom_mtu_set")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERNAL: _ClassVar[Network.Type]
        PROVIDER: _ClassVar[Network.Type]
    INTERNAL: Network.Type
    PROVIDER: Network.Type
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Network.State]
        CREATING: _ClassVar[Network.State]
        DELETING: _ClassVar[Network.State]
        PORT_ATTACHING: _ClassVar[Network.State]
        SUBNET_ATTACHING: _ClassVar[Network.State]
        PORT_DETACHING: _ClassVar[Network.State]
        SUBNET_DETACHING: _ClassVar[Network.State]
        UPDATING_NAME: _ClassVar[Network.State]
        UPDATING_MTU: _ClassVar[Network.State]
        UPDATING_TENANT_ID: _ClassVar[Network.State]
        UPDATING_METADATA: _ClassVar[Network.State]
        UPDATING_SEGMENT: _ClassVar[Network.State]
        UPDATING_IPAMTYPE: _ClassVar[Network.State]
        CREATED: _ClassVar[Network.State]
        DELETED: _ClassVar[Network.State]
        ERROR: _ClassVar[Network.State]
        CLEANING_ON_ERROR: _ClassVar[Network.State]
    UNKNOWN: Network.State
    CREATING: Network.State
    DELETING: Network.State
    PORT_ATTACHING: Network.State
    SUBNET_ATTACHING: Network.State
    PORT_DETACHING: Network.State
    SUBNET_DETACHING: Network.State
    UPDATING_NAME: Network.State
    UPDATING_MTU: Network.State
    UPDATING_TENANT_ID: Network.State
    UPDATING_METADATA: Network.State
    UPDATING_SEGMENT: Network.State
    UPDATING_IPAMTYPE: Network.State
    CREATED: Network.State
    DELETED: Network.State
    ERROR: Network.State
    CLEANING_ON_ERROR: Network.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Provider(_message.Message):
        __slots__ = ("segments",)
        class Segment(_message.Message):
            __slots__ = ("type", "sub_type", "segmentation_id", "interface_group")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                VLAN: _ClassVar[Network.Provider.Segment.Type]
                FLAT: _ClassVar[Network.Provider.Segment.Type]
                GRE: _ClassVar[Network.Provider.Segment.Type]
                VXLAN: _ClassVar[Network.Provider.Segment.Type]
                NVGRE: _ClassVar[Network.Provider.Segment.Type]
                STT: _ClassVar[Network.Provider.Segment.Type]
                GENEVE: _ClassVar[Network.Provider.Segment.Type]
            VLAN: Network.Provider.Segment.Type
            FLAT: Network.Provider.Segment.Type
            GRE: Network.Provider.Segment.Type
            VXLAN: Network.Provider.Segment.Type
            NVGRE: Network.Provider.Segment.Type
            STT: Network.Provider.Segment.Type
            GENEVE: Network.Provider.Segment.Type
            class SubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                VLAN_NORMAL: _ClassVar[Network.Provider.Segment.SubType]
                VLAN_BIFROST_NODE_FACING: _ClassVar[Network.Provider.Segment.SubType]
                VLAN_BIFROST_TENANT_FACING: _ClassVar[Network.Provider.Segment.SubType]
            VLAN_NORMAL: Network.Provider.Segment.SubType
            VLAN_BIFROST_NODE_FACING: Network.Provider.Segment.SubType
            VLAN_BIFROST_TENANT_FACING: Network.Provider.Segment.SubType
            TYPE_FIELD_NUMBER: _ClassVar[int]
            SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
            SEGMENTATION_ID_FIELD_NUMBER: _ClassVar[int]
            INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
            type: Network.Provider.Segment.Type
            sub_type: Network.Provider.Segment.SubType
            segmentation_id: int
            interface_group: str
            def __init__(self, type: _Optional[_Union[Network.Provider.Segment.Type, str]] = ..., sub_type: _Optional[_Union[Network.Provider.Segment.SubType, str]] = ..., segmentation_id: _Optional[int] = ..., interface_group: _Optional[str] = ...) -> None: ...
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        segments: _containers.RepeatedCompositeFieldContainer[Network.Provider.Segment]
        def __init__(self, segments: _Optional[_Iterable[_Union[Network.Provider.Segment, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IDS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    NO_L3_HOST_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IPAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    IS_CUSTOM_MTU_SET_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    ports: _containers.RepeatedScalarFieldContainer[str]
    subnet_ids: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    type: Network.Type
    mtu: int
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    provider: Network.Provider
    no_l3_host_connectivity: bool
    default_ipam_type: IPAMType
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    is_custom_mtu_set: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., ports: _Optional[_Iterable[str]] = ..., subnet_ids: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ..., type: _Optional[_Union[Network.Type, str]] = ..., mtu: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., provider: _Optional[_Union[Network.Provider, _Mapping]] = ..., no_l3_host_connectivity: bool = ..., default_ipam_type: _Optional[_Union[IPAMType, str]] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ..., is_custom_mtu_set: bool = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "ip_version", "cidr", "gw", "network_id", "dhcp_enabled", "dhcp_conf", "allow_service_access", "tenant_id", "exclude_ip_ranges", "metadata", "allow_all_tenants", "static_ip_ranges", "service_access_config", "state", "error", "last_request_id", "ovn_dhcp_config_id", "version", "force_set_reason", "try_update_recovery")
    class IPVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        V4: _ClassVar[Subnet.IPVersion]
        V6: _ClassVar[Subnet.IPVersion]
    V4: Subnet.IPVersion
    V6: Subnet.IPVersion
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Subnet.State]
        CREATING: _ClassVar[Subnet.State]
        DELETING: _ClassVar[Subnet.State]
        UPDATING_SUBNET: _ClassVar[Subnet.State]
        UPDATING_DHCP: _ClassVar[Subnet.State]
        UPDATING_SERVICE_ACCESS: _ClassVar[Subnet.State]
        UPDATING_TENANT_ID: _ClassVar[Subnet.State]
        UPDATING_METADATA: _ClassVar[Subnet.State]
        CREATED: _ClassVar[Subnet.State]
        DELETED: _ClassVar[Subnet.State]
        ERROR: _ClassVar[Subnet.State]
        CLEANING_ON_ERROR: _ClassVar[Subnet.State]
    UNKNOWN: Subnet.State
    CREATING: Subnet.State
    DELETING: Subnet.State
    UPDATING_SUBNET: Subnet.State
    UPDATING_DHCP: Subnet.State
    UPDATING_SERVICE_ACCESS: Subnet.State
    UPDATING_TENANT_ID: Subnet.State
    UPDATING_METADATA: Subnet.State
    CREATED: Subnet.State
    DELETED: Subnet.State
    ERROR: Subnet.State
    CLEANING_ON_ERROR: Subnet.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IP_VERSION_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    GW_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DHCP_CONF_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SERVICE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    STATIC_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OVN_DHCP_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    ip_version: Subnet.IPVersion
    cidr: str
    gw: str
    network_id: str
    dhcp_enabled: bool
    dhcp_conf: DhcpSrvrConf
    allow_service_access: bool
    tenant_id: str
    exclude_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    static_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    service_access_config: ServiceAccessConfig
    state: int
    error: AxonError
    last_request_id: str
    ovn_dhcp_config_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., ip_version: _Optional[_Union[Subnet.IPVersion, str]] = ..., cidr: _Optional[str] = ..., gw: _Optional[str] = ..., network_id: _Optional[str] = ..., dhcp_enabled: bool = ..., dhcp_conf: _Optional[_Union[DhcpSrvrConf, _Mapping]] = ..., allow_service_access: bool = ..., tenant_id: _Optional[str] = ..., exclude_ip_ranges: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., static_ip_ranges: _Optional[_Iterable[str]] = ..., service_access_config: _Optional[_Union[ServiceAccessConfig, _Mapping]] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., ovn_dhcp_config_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ...) -> None: ...

class ServiceAccessConfig(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APP: _ClassVar[ServiceAccessConfig.Type]
        BIFROST: _ClassVar[ServiceAccessConfig.Type]
    APP: ServiceAccessConfig.Type
    BIFROST: ServiceAccessConfig.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ServiceAccessConfig.Type
    def __init__(self, type: _Optional[_Union[ServiceAccessConfig.Type, str]] = ...) -> None: ...

class DhcpSrvrConf(_message.Message):
    __slots__ = ("mac_address", "ipaddress", "subnet_cidr", "dns_domain", "dns_nameservers", "dns_searchdomains", "extra_options", "mtu", "metadata")
    class ExtraOptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
    DNS_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DNS_NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SEARCHDOMAINS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    ipaddress: str
    subnet_cidr: str
    dns_domain: str
    dns_nameservers: _containers.RepeatedScalarFieldContainer[str]
    dns_searchdomains: _containers.RepeatedScalarFieldContainer[str]
    extra_options: _containers.ScalarMap[str, str]
    mtu: int
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, mac_address: _Optional[str] = ..., ipaddress: _Optional[str] = ..., subnet_cidr: _Optional[str] = ..., dns_domain: _Optional[str] = ..., dns_nameservers: _Optional[_Iterable[str]] = ..., dns_searchdomains: _Optional[_Iterable[str]] = ..., extra_options: _Optional[_Mapping[str, str]] = ..., mtu: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "network_id", "peer_port", "mac_address", "dhcp_extra_options", "type", "port_security_enabled", "port_security", "port_profile_id", "ip_address", "tenant_id", "provider_net_name", "metadata", "subnet_cidr", "allow_all_tenants", "bind_node_id", "bind_node_type", "router_id", "port_groups", "router_attachment_id", "description", "ipam_type", "state", "error", "last_request_id", "version", "force_set_reason", "try_update_recovery", "is_dynamic_mac", "is_dynamic_ip")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Port.Type]
        LOCALPORT: _ClassVar[Port.Type]
        LOCALNET: _ClassVar[Port.Type]
        L2GWPORT: _ClassVar[Port.Type]
        ROUTER: _ClassVar[Port.Type]
        VTEPPORT: _ClassVar[Port.Type]
        SERVICEACCESS: _ClassVar[Port.Type]
    NORMAL: Port.Type
    LOCALPORT: Port.Type
    LOCALNET: Port.Type
    L2GWPORT: Port.Type
    ROUTER: Port.Type
    VTEPPORT: Port.Type
    SERVICEACCESS: Port.Type
    class PortNodeBindingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNBOUND: _ClassVar[Port.PortNodeBindingType]
        INTERNAL: _ClassVar[Port.PortNodeBindingType]
        VIF: _ClassVar[Port.PortNodeBindingType]
        SERVICE_ACCESS: _ClassVar[Port.PortNodeBindingType]
    UNBOUND: Port.PortNodeBindingType
    INTERNAL: Port.PortNodeBindingType
    VIF: Port.PortNodeBindingType
    SERVICE_ACCESS: Port.PortNodeBindingType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Port.State]
        CREATING: _ClassVar[Port.State]
        DELETING: _ClassVar[Port.State]
        UPDATING_STATUS: _ClassVar[Port.State]
        UPDATING_MAC_ADDRESS: _ClassVar[Port.State]
        UPDATING_DHCP_EXTRA_OPTIONS: _ClassVar[Port.State]
        UPDATING_PORT_SECURITY: _ClassVar[Port.State]
        UPDATING_PORT_PROFILE: _ClassVar[Port.State]
        UPDATING_NETWORK_ID: _ClassVar[Port.State]
        UPDATING_PROVIDER_NETWORK: _ClassVar[Port.State]
        UPDATING_METADATA: _ClassVar[Port.State]
        UPDATING_TENANT_ID: _ClassVar[Port.State]
        UPDATING_NAME: _ClassVar[Port.State]
        CREATED: _ClassVar[Port.State]
        DELETED: _ClassVar[Port.State]
        ERROR: _ClassVar[Port.State]
        CLEANING_ON_ERROR: _ClassVar[Port.State]
    UNKNOWN: Port.State
    CREATING: Port.State
    DELETING: Port.State
    UPDATING_STATUS: Port.State
    UPDATING_MAC_ADDRESS: Port.State
    UPDATING_DHCP_EXTRA_OPTIONS: Port.State
    UPDATING_PORT_SECURITY: Port.State
    UPDATING_PORT_PROFILE: Port.State
    UPDATING_NETWORK_ID: Port.State
    UPDATING_PROVIDER_NETWORK: Port.State
    UPDATING_METADATA: Port.State
    UPDATING_TENANT_ID: Port.State
    UPDATING_NAME: Port.State
    CREATED: Port.State
    DELETED: Port.State
    ERROR: Port.State
    CLEANING_ON_ERROR: Port.State
    class DhcpExtraOptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    PEER_PORT_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DHCP_EXTRA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PORT_SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PORT_SECURITY_FIELD_NUMBER: _ClassVar[int]
    PORT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NET_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    BIND_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BIND_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    PORT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IPAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_MAC_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_IP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    network_id: str
    peer_port: Port
    mac_address: str
    dhcp_extra_options: _containers.ScalarMap[str, str]
    type: Port.Type
    port_security_enabled: bool
    port_security: _containers.RepeatedScalarFieldContainer[str]
    port_profile_id: str
    ip_address: str
    tenant_id: str
    provider_net_name: str
    metadata: _containers.ScalarMap[str, str]
    subnet_cidr: str
    allow_all_tenants: bool
    bind_node_id: int
    bind_node_type: Port.PortNodeBindingType
    router_id: str
    port_groups: _containers.RepeatedScalarFieldContainer[str]
    router_attachment_id: str
    description: str
    ipam_type: IPAMType
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    is_dynamic_mac: bool
    is_dynamic_ip: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., network_id: _Optional[str] = ..., peer_port: _Optional[_Union[Port, _Mapping]] = ..., mac_address: _Optional[str] = ..., dhcp_extra_options: _Optional[_Mapping[str, str]] = ..., type: _Optional[_Union[Port.Type, str]] = ..., port_security_enabled: bool = ..., port_security: _Optional[_Iterable[str]] = ..., port_profile_id: _Optional[str] = ..., ip_address: _Optional[str] = ..., tenant_id: _Optional[str] = ..., provider_net_name: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., subnet_cidr: _Optional[str] = ..., allow_all_tenants: bool = ..., bind_node_id: _Optional[int] = ..., bind_node_type: _Optional[_Union[Port.PortNodeBindingType, str]] = ..., router_id: _Optional[str] = ..., port_groups: _Optional[_Iterable[str]] = ..., router_attachment_id: _Optional[str] = ..., description: _Optional[str] = ..., ipam_type: _Optional[_Union[IPAMType, str]] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ..., is_dynamic_mac: bool = ..., is_dynamic_ip: bool = ...) -> None: ...

class SecurityGroupRule(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "security_group_ids", "port_min", "port_max", "ip_cidr", "proto", "direction", "tenant_id", "type", "metadata", "allow_all_tenants", "ip_address_set", "cluster_ip_set", "priority", "action", "port_group_name", "state", "error", "last_request_id", "version", "force_set_reason", "try_update_recovery")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[SecurityGroupRule.Protocol]
        TCP: _ClassVar[SecurityGroupRule.Protocol]
        UDP: _ClassVar[SecurityGroupRule.Protocol]
        ICMP: _ClassVar[SecurityGroupRule.Protocol]
        ICMPV6: _ClassVar[SecurityGroupRule.Protocol]
    ANY: SecurityGroupRule.Protocol
    TCP: SecurityGroupRule.Protocol
    UDP: SecurityGroupRule.Protocol
    ICMP: SecurityGroupRule.Protocol
    ICMPV6: SecurityGroupRule.Protocol
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INGRESS: _ClassVar[SecurityGroupRule.Direction]
        EGRESS: _ClassVar[SecurityGroupRule.Direction]
    INGRESS: SecurityGroupRule.Direction
    EGRESS: SecurityGroupRule.Direction
    class SgrType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[SecurityGroupRule.SgrType]
        INTERNAL_DEFAULT_DENY: _ClassVar[SecurityGroupRule.SgrType]
    NORMAL: SecurityGroupRule.SgrType
    INTERNAL_DEFAULT_DENY: SecurityGroupRule.SgrType
    class ACLAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOW: _ClassVar[SecurityGroupRule.ACLAction]
        ALLOW_RELATED: _ClassVar[SecurityGroupRule.ACLAction]
        DROP: _ClassVar[SecurityGroupRule.ACLAction]
        REJECT: _ClassVar[SecurityGroupRule.ACLAction]
    ALLOW: SecurityGroupRule.ACLAction
    ALLOW_RELATED: SecurityGroupRule.ACLAction
    DROP: SecurityGroupRule.ACLAction
    REJECT: SecurityGroupRule.ACLAction
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SecurityGroupRule.State]
        CREATING: _ClassVar[SecurityGroupRule.State]
        DELETING: _ClassVar[SecurityGroupRule.State]
        UPDATING_PORT_MIN: _ClassVar[SecurityGroupRule.State]
        UPDATING_PORT_MAX: _ClassVar[SecurityGroupRule.State]
        UPDATING_CIDR: _ClassVar[SecurityGroupRule.State]
        UPDATING_PROTOCOL: _ClassVar[SecurityGroupRule.State]
        UPDATING_DIRECTION: _ClassVar[SecurityGroupRule.State]
        UPDATING_IP_SET: _ClassVar[SecurityGroupRule.State]
        UPDATING_CLUSTER_IP_SET: _ClassVar[SecurityGroupRule.State]
        UPDATING_ACL_ACTION: _ClassVar[SecurityGroupRule.State]
        UPDATING_TENANT_ID: _ClassVar[SecurityGroupRule.State]
        UPDATING_NAME: _ClassVar[SecurityGroupRule.State]
        UPDATING_METADATA: _ClassVar[SecurityGroupRule.State]
        CREATED: _ClassVar[SecurityGroupRule.State]
        DELETED: _ClassVar[SecurityGroupRule.State]
        ERROR: _ClassVar[SecurityGroupRule.State]
        CLEANING_ON_ERROR: _ClassVar[SecurityGroupRule.State]
    UNKNOWN: SecurityGroupRule.State
    CREATING: SecurityGroupRule.State
    DELETING: SecurityGroupRule.State
    UPDATING_PORT_MIN: SecurityGroupRule.State
    UPDATING_PORT_MAX: SecurityGroupRule.State
    UPDATING_CIDR: SecurityGroupRule.State
    UPDATING_PROTOCOL: SecurityGroupRule.State
    UPDATING_DIRECTION: SecurityGroupRule.State
    UPDATING_IP_SET: SecurityGroupRule.State
    UPDATING_CLUSTER_IP_SET: SecurityGroupRule.State
    UPDATING_ACL_ACTION: SecurityGroupRule.State
    UPDATING_TENANT_ID: SecurityGroupRule.State
    UPDATING_NAME: SecurityGroupRule.State
    UPDATING_METADATA: SecurityGroupRule.State
    CREATED: SecurityGroupRule.State
    DELETED: SecurityGroupRule.State
    ERROR: SecurityGroupRule.State
    CLEANING_ON_ERROR: SecurityGroupRule.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    PORT_MIN_FIELD_NUMBER: _ClassVar[int]
    PORT_MAX_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_FIELD_NUMBER: _ClassVar[int]
    PROTO_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_SET_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IP_SET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PORT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    security_group_ids: _containers.RepeatedScalarFieldContainer[str]
    port_min: int
    port_max: int
    ip_cidr: str
    proto: SecurityGroupRule.Protocol
    direction: SecurityGroupRule.Direction
    tenant_id: str
    type: SecurityGroupRule.SgrType
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    ip_address_set: _containers.RepeatedScalarFieldContainer[str]
    cluster_ip_set: bool
    priority: int
    action: SecurityGroupRule.ACLAction
    port_group_name: str
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., security_group_ids: _Optional[_Iterable[str]] = ..., port_min: _Optional[int] = ..., port_max: _Optional[int] = ..., ip_cidr: _Optional[str] = ..., proto: _Optional[_Union[SecurityGroupRule.Protocol, str]] = ..., direction: _Optional[_Union[SecurityGroupRule.Direction, str]] = ..., tenant_id: _Optional[str] = ..., type: _Optional[_Union[SecurityGroupRule.SgrType, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., ip_address_set: _Optional[_Iterable[str]] = ..., cluster_ip_set: bool = ..., priority: _Optional[int] = ..., action: _Optional[_Union[SecurityGroupRule.ACLAction, str]] = ..., port_group_name: _Optional[str] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ...) -> None: ...

class SecurityGroup(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "tenant_id", "rules", "metadata", "allow_all_tenants", "state", "error", "last_request_id", "version", "force_set_reason", "try_update_recovery")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SecurityGroup.State]
        CREATING: _ClassVar[SecurityGroup.State]
        DELETING: _ClassVar[SecurityGroup.State]
        UPDATING_SECURITY_RULE: _ClassVar[SecurityGroup.State]
        CREATED: _ClassVar[SecurityGroup.State]
        DELETED: _ClassVar[SecurityGroup.State]
        ERROR: _ClassVar[SecurityGroup.State]
        CLEANING_ON_ERROR: _ClassVar[SecurityGroup.State]
    UNKNOWN: SecurityGroup.State
    CREATING: SecurityGroup.State
    DELETING: SecurityGroup.State
    UPDATING_SECURITY_RULE: SecurityGroup.State
    CREATED: SecurityGroup.State
    DELETED: SecurityGroup.State
    ERROR: SecurityGroup.State
    CLEANING_ON_ERROR: SecurityGroup.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    tenant_id: str
    rules: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., tenant_id: _Optional[str] = ..., rules: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ...) -> None: ...

class PortProfile(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "vlan_id", "secgrp_id", "tenant_id", "ports", "metadata", "allow_all_tenants", "state", "error", "last_request_id", "version", "force_set_reason", "try_update_recovery")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[PortProfile.State]
        CREATING: _ClassVar[PortProfile.State]
        DELETING: _ClassVar[PortProfile.State]
        UPDATING_VLAN: _ClassVar[PortProfile.State]
        UPDATING_SECURITY_GROUP: _ClassVar[PortProfile.State]
        UPDATING_PORT_LIST: _ClassVar[PortProfile.State]
        UPDATING_TENANT_ID: _ClassVar[PortProfile.State]
        UPDATING_NAME: _ClassVar[PortProfile.State]
        UPDATING_METADATA: _ClassVar[PortProfile.State]
        CREATED: _ClassVar[PortProfile.State]
        DELETED: _ClassVar[PortProfile.State]
        ERROR: _ClassVar[PortProfile.State]
        CLEANING_ON_ERROR: _ClassVar[PortProfile.State]
    UNKNOWN: PortProfile.State
    CREATING: PortProfile.State
    DELETING: PortProfile.State
    UPDATING_VLAN: PortProfile.State
    UPDATING_SECURITY_GROUP: PortProfile.State
    UPDATING_PORT_LIST: PortProfile.State
    UPDATING_TENANT_ID: PortProfile.State
    UPDATING_NAME: PortProfile.State
    UPDATING_METADATA: PortProfile.State
    CREATED: PortProfile.State
    DELETED: PortProfile.State
    ERROR: PortProfile.State
    CLEANING_ON_ERROR: PortProfile.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SECGRP_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    TRY_UPDATE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    vlan_id: int
    secgrp_id: str
    tenant_id: str
    ports: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    try_update_recovery: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., vlan_id: _Optional[int] = ..., secgrp_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., ports: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ..., try_update_recovery: bool = ...) -> None: ...

class Router(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "attachments", "deny_rules", "gw_port_id", "metadata", "allow_all_tenants", "tenant_id", "state", "error", "last_request_id", "version", "force_set_reason")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Router.State]
        CREATING: _ClassVar[Router.State]
        DELETING: _ClassVar[Router.State]
        UPDATING_PORT_ID: _ClassVar[Router.State]
        UPDATING_ROUTER_ATTACHMENT: _ClassVar[Router.State]
        UPDATING_NAME: _ClassVar[Router.State]
        CREATED: _ClassVar[Router.State]
        DELETED: _ClassVar[Router.State]
        ERROR: _ClassVar[Router.State]
        CLEANING_ON_ERROR: _ClassVar[Router.State]
    UNKNOWN: Router.State
    CREATING: Router.State
    DELETING: Router.State
    UPDATING_PORT_ID: Router.State
    UPDATING_ROUTER_ATTACHMENT: Router.State
    UPDATING_NAME: Router.State
    CREATED: Router.State
    DELETED: Router.State
    ERROR: Router.State
    CLEANING_ON_ERROR: Router.State
    class DenyRulesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    DENY_RULES_FIELD_NUMBER: _ClassVar[int]
    GW_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    attachments: _containers.RepeatedCompositeFieldContainer[RouterAttachment]
    deny_rules: _containers.ScalarMap[str, str]
    gw_port_id: str
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    tenant_id: str
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[RouterAttachment, _Mapping]]] = ..., deny_rules: _Optional[_Mapping[str, str]] = ..., gw_port_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., tenant_id: _Optional[str] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ...) -> None: ...

class RouterAttachment(_message.Message):
    __slots__ = ("id", "subnet_id", "network_port_id", "network_address", "mac", "description", "state", "error", "last_request_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[RouterAttachment.State]
        CREATING: _ClassVar[RouterAttachment.State]
        DELETING: _ClassVar[RouterAttachment.State]
        UPDATING_ATTACHMENT: _ClassVar[RouterAttachment.State]
        CREATED: _ClassVar[RouterAttachment.State]
        DELETED: _ClassVar[RouterAttachment.State]
        ERROR: _ClassVar[RouterAttachment.State]
        CLEANING_ON_ERROR: _ClassVar[RouterAttachment.State]
    UNKNOWN: RouterAttachment.State
    CREATING: RouterAttachment.State
    DELETING: RouterAttachment.State
    UPDATING_ATTACHMENT: RouterAttachment.State
    CREATED: RouterAttachment.State
    DELETED: RouterAttachment.State
    ERROR: RouterAttachment.State
    CLEANING_ON_ERROR: RouterAttachment.State
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    subnet_id: str
    network_port_id: str
    network_address: str
    mac: str
    description: str
    state: int
    error: AxonError
    last_request_id: str
    def __init__(self, id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., network_port_id: _Optional[str] = ..., network_address: _Optional[str] = ..., mac: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ...) -> None: ...

class LoadBalancer(_message.Message):
    __slots__ = ("id", "name", "created_timestamp", "updated_timestamp", "vip", "ipaddresses", "metadata", "allow_all_tenants", "state", "error", "last_request_id", "version", "force_set_reason")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[LoadBalancer.State]
        CREATING: _ClassVar[LoadBalancer.State]
        DELETING: _ClassVar[LoadBalancer.State]
        UPDATING_VIP: _ClassVar[LoadBalancer.State]
        UPDATING_IPADDRESSES: _ClassVar[LoadBalancer.State]
        CREATED: _ClassVar[LoadBalancer.State]
        DELETED: _ClassVar[LoadBalancer.State]
        ERROR: _ClassVar[LoadBalancer.State]
    UNKNOWN: LoadBalancer.State
    CREATING: LoadBalancer.State
    DELETING: LoadBalancer.State
    UPDATING_VIP: LoadBalancer.State
    UPDATING_IPADDRESSES: LoadBalancer.State
    CREATED: LoadBalancer.State
    DELETED: LoadBalancer.State
    ERROR: LoadBalancer.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VIP_FIELD_NUMBER: _ClassVar[int]
    IPADDRESSES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TENANTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_SET_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_timestamp: str
    updated_timestamp: str
    vip: str
    ipaddresses: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    allow_all_tenants: bool
    state: int
    error: AxonError
    last_request_id: str
    version: int
    force_set_reason: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_timestamp: _Optional[str] = ..., updated_timestamp: _Optional[str] = ..., vip: _Optional[str] = ..., ipaddresses: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., allow_all_tenants: bool = ..., state: _Optional[int] = ..., error: _Optional[_Union[AxonError, _Mapping]] = ..., last_request_id: _Optional[str] = ..., version: _Optional[int] = ..., force_set_reason: _Optional[str] = ...) -> None: ...
