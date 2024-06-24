from configs import cluster_config_pb2 as _cluster_config_pb2
from nexus.base import nexus_hmac_key_config_pb2 as _nexus_hmac_key_config_pb2
from nexus.base import services_gflags_pb2 as _services_gflags_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterBringup: _ClassVar[RestRequestType]
    kClusterExpand: _ClassVar[RestRequestType]
    kNodeBringup: _ClassVar[RestRequestType]
    kClusterNetworkingReset: _ClassVar[RestRequestType]
    kNodeNetworkingReset: _ClassVar[RestRequestType]

class BringupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoStateChange: _ClassVar[BringupState]
    kStartingBgOp: _ClassVar[BringupState]
    kConfiguringNetwork: _ClassVar[BringupState]
    kUpgradingNode: _ClassVar[BringupState]
    kStartingGandalf: _ClassVar[BringupState]
    kInitingClusterConfig: _ClassVar[BringupState]
    kAddingChassisAndNodes: _ClassVar[BringupState]
    kInitingTimeService: _ClassVar[BringupState]
    kFormattingDisks: _ClassVar[BringupState]
    kFormattedDisks: _ClassVar[BringupState]
    kWaitingForSlavesDone: _ClassVar[BringupState]
    kWaitingForHandshakesDone: _ClassVar[BringupState]
    kHandshakesDone: _ClassVar[BringupState]
    kBgOpFailed: _ClassVar[BringupState]
    kBgOpCompleted: _ClassVar[BringupState]

class SnapshotRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterCreateSnapshot: _ClassVar[SnapshotRequestType]
    kNodeCreateSnapshot: _ClassVar[SnapshotRequestType]
    kClusterRestoreSnapshot: _ClassVar[SnapshotRequestType]
    kNodeRestoreSnapshot: _ClassVar[SnapshotRequestType]
kClusterBringup: RestRequestType
kClusterExpand: RestRequestType
kNodeBringup: RestRequestType
kClusterNetworkingReset: RestRequestType
kNodeNetworkingReset: RestRequestType
kNoStateChange: BringupState
kStartingBgOp: BringupState
kConfiguringNetwork: BringupState
kUpgradingNode: BringupState
kStartingGandalf: BringupState
kInitingClusterConfig: BringupState
kAddingChassisAndNodes: BringupState
kInitingTimeService: BringupState
kFormattingDisks: BringupState
kFormattedDisks: BringupState
kWaitingForSlavesDone: BringupState
kWaitingForHandshakesDone: BringupState
kHandshakesDone: BringupState
kBgOpFailed: BringupState
kBgOpCompleted: BringupState
kClusterCreateSnapshot: SnapshotRequestType
kNodeCreateSnapshot: SnapshotRequestType
kClusterRestoreSnapshot: SnapshotRequestType
kNodeRestoreSnapshot: SnapshotRequestType

class NodeInfo(_message.Message):
    __slots__ = ("ip", "ipmi_ip")
    IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    ipmi_ip: str
    def __init__(self, ip: _Optional[str] = ..., ipmi_ip: _Optional[str] = ...) -> None: ...

class NodeIpPreference(_message.Message):
    __slots__ = ("node_ip_reachable", "ipv4_link_local", "ipv6_link_local")
    NODE_IP_REACHABLE_FIELD_NUMBER: _ClassVar[int]
    IPV4_LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
    IPV6_LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
    node_ip_reachable: bool
    ipv4_link_local: str
    ipv6_link_local: str
    def __init__(self, node_ip_reachable: bool = ..., ipv4_link_local: _Optional[str] = ..., ipv6_link_local: _Optional[str] = ...) -> None: ...

class DnsGroup(_message.Message):
    __slots__ = ("name", "node_ip_vec", "dns_servers")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., node_ip_vec: _Optional[_Iterable[str]] = ..., dns_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class ClusterSubnetGroup(_message.Message):
    __slots__ = ("name", "node_ip_vec", "subnet_ip", "subnet_cidr_len", "subnet_ipv4_mask", "gateway")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    subnet_ip: str
    subnet_cidr_len: int
    subnet_ipv4_mask: str
    gateway: str
    def __init__(self, name: _Optional[str] = ..., node_ip_vec: _Optional[_Iterable[str]] = ..., subnet_ip: _Optional[str] = ..., subnet_cidr_len: _Optional[int] = ..., subnet_ipv4_mask: _Optional[str] = ..., gateway: _Optional[str] = ...) -> None: ...

class BringupStatusEvent(_message.Message):
    __slots__ = ("time_stamp_usecs", "bringup_event")
    TIME_STAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    BRINGUP_EVENT_FIELD_NUMBER: _ClassVar[int]
    time_stamp_usecs: int
    bringup_event: str
    def __init__(self, time_stamp_usecs: _Optional[int] = ..., bringup_event: _Optional[str] = ...) -> None: ...

class ClusterBringupWalRecord(_message.Message):
    __slots__ = ("cluster_name", "cluster_id", "cluster_incarnation_id", "ntp_servers", "dns_servers", "domain_names", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "ipmi_gateway", "ipmi_subnet_ip", "ipmi_subnet_cidr_len", "ipmi_subnet_ipv4_mask", "ipmi_username", "ipmi_password", "node_vec", "chassis_vec", "cluster_software_version", "rotationPeriod", "req_type", "enable_software_encryption", "cluster_partition_id", "auto_update", "ignore_sw_incompatibility", "software_package_urls", "clean_logs_needed", "last_updated_time_secs", "percentage_completed", "current_operation", "time_started", "time_estimated_secs", "time_remaining_secs", "hardware_encryption_capability", "bonding_mode", "compatibility_proto_vec", "oldscribe_enabled", "mtu", "sender_node_ip", "node_ip_preference_vec", "rotation_period_secs", "enable_fips_mode", "in_progress", "login_url", "error_message", "bringup_event_vec", "warnings_found", "bringup_state", "panic_state", "panic_count", "ServicesGflagsProto", "proxy_server_config", "vip_vec", "cluster_partition_host_name", "metadata_fault_tolerance_factor", "is_cluster_expand", "ip_preference", "rack_id", "ntp_server_auth_keys_vec", "dns_group_vec", "cluster_subnet_group_vec", "ntp_authentication_enabled", "allow_cluster_destroy_on_api_request", "nexus_hmac_config_proto", "enable_hardware_encryption", "enable_kernel_fips_mode", "service_identity_trust_domain", "service_identity_trust_domain_mode", "operation_id", "cluster_subnet_vec", "aes_encryption_mode", "generate_rootca")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    IPMI_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    IPMI_USERNAME_FIELD_NUMBER: _ClassVar[int]
    IPMI_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROTATIONPERIOD_FIELD_NUMBER: _ClassVar[int]
    REQ_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SOFTWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SW_INCOMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_PACKAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    CLEAN_LOGS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIME_STARTED_FIELD_NUMBER: _ClassVar[int]
    TIME_ESTIMATED_SECS_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_SECS_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ENCRYPTION_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    OLDSCRIBE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_PREFERENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    ROTATION_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIPS_MODE_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BRINGUP_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FOUND_FIELD_NUMBER: _ClassVar[int]
    BRINGUP_STATE_FIELD_NUMBER: _ClassVar[int]
    PANIC_STATE_FIELD_NUMBER: _ClassVar[int]
    PANIC_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICESGFLAGSPROTO_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    IS_CLUSTER_EXPAND_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    RACK_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_AUTH_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NTP_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CLUSTER_DESTROY_ON_API_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NEXUS_HMAC_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_KERNEL_FIPS_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IDENTITY_TRUST_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IDENTITY_TRUST_DOMAIN_MODE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    AES_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_ROOTCA_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    ntp_servers: _containers.RepeatedScalarFieldContainer[str]
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    domain_names: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    ipmi_gateway: str
    ipmi_subnet_ip: str
    ipmi_subnet_cidr_len: int
    ipmi_subnet_ipv4_mask: str
    ipmi_username: str
    ipmi_password: str
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    chassis_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Chassis]
    cluster_software_version: str
    rotationPeriod: int
    req_type: RestRequestType
    enable_software_encryption: bool
    cluster_partition_id: int
    auto_update: bool
    ignore_sw_incompatibility: bool
    software_package_urls: _containers.RepeatedScalarFieldContainer[str]
    clean_logs_needed: bool
    last_updated_time_secs: int
    percentage_completed: int
    current_operation: str
    time_started: int
    time_estimated_secs: int
    time_remaining_secs: int
    hardware_encryption_capability: bool
    bonding_mode: _cluster_config_pb2.ClusterConfigProto.BondingMode
    compatibility_proto_vec: _containers.RepeatedScalarFieldContainer[str]
    oldscribe_enabled: bool
    mtu: int
    sender_node_ip: str
    node_ip_preference_vec: _containers.RepeatedCompositeFieldContainer[NodeIpPreference]
    rotation_period_secs: int
    enable_fips_mode: bool
    in_progress: bool
    login_url: str
    error_message: str
    bringup_event_vec: _containers.RepeatedCompositeFieldContainer[BringupStatusEvent]
    warnings_found: bool
    bringup_state: BringupState
    panic_state: BringupState
    panic_count: int
    ServicesGflagsProto: _services_gflags_pb2.ServicesGflagsProto
    proxy_server_config: _cluster_config_pb2.ClusterConfigProto.ProxyServerConfig
    vip_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_partition_host_name: str
    metadata_fault_tolerance_factor: int
    is_cluster_expand: bool
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    rack_id: int
    ntp_server_auth_keys_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo]
    dns_group_vec: _containers.RepeatedCompositeFieldContainer[DnsGroup]
    cluster_subnet_group_vec: _containers.RepeatedCompositeFieldContainer[ClusterSubnetGroup]
    ntp_authentication_enabled: bool
    allow_cluster_destroy_on_api_request: bool
    nexus_hmac_config_proto: _nexus_hmac_key_config_pb2.NexusHmacKeyProto
    enable_hardware_encryption: bool
    enable_kernel_fips_mode: bool
    service_identity_trust_domain: str
    service_identity_trust_domain_mode: int
    operation_id: str
    cluster_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    aes_encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    generate_rootca: bool
    def __init__(self, cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., ntp_servers: _Optional[_Iterable[str]] = ..., dns_servers: _Optional[_Iterable[str]] = ..., domain_names: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., ipmi_gateway: _Optional[str] = ..., ipmi_subnet_ip: _Optional[str] = ..., ipmi_subnet_cidr_len: _Optional[int] = ..., ipmi_subnet_ipv4_mask: _Optional[str] = ..., ipmi_username: _Optional[str] = ..., ipmi_password: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ..., chassis_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Chassis, _Mapping]]] = ..., cluster_software_version: _Optional[str] = ..., rotationPeriod: _Optional[int] = ..., req_type: _Optional[_Union[RestRequestType, str]] = ..., enable_software_encryption: bool = ..., cluster_partition_id: _Optional[int] = ..., auto_update: bool = ..., ignore_sw_incompatibility: bool = ..., software_package_urls: _Optional[_Iterable[str]] = ..., clean_logs_needed: bool = ..., last_updated_time_secs: _Optional[int] = ..., percentage_completed: _Optional[int] = ..., current_operation: _Optional[str] = ..., time_started: _Optional[int] = ..., time_estimated_secs: _Optional[int] = ..., time_remaining_secs: _Optional[int] = ..., hardware_encryption_capability: bool = ..., bonding_mode: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BondingMode, str]] = ..., compatibility_proto_vec: _Optional[_Iterable[str]] = ..., oldscribe_enabled: bool = ..., mtu: _Optional[int] = ..., sender_node_ip: _Optional[str] = ..., node_ip_preference_vec: _Optional[_Iterable[_Union[NodeIpPreference, _Mapping]]] = ..., rotation_period_secs: _Optional[int] = ..., enable_fips_mode: bool = ..., in_progress: bool = ..., login_url: _Optional[str] = ..., error_message: _Optional[str] = ..., bringup_event_vec: _Optional[_Iterable[_Union[BringupStatusEvent, _Mapping]]] = ..., warnings_found: bool = ..., bringup_state: _Optional[_Union[BringupState, str]] = ..., panic_state: _Optional[_Union[BringupState, str]] = ..., panic_count: _Optional[int] = ..., ServicesGflagsProto: _Optional[_Union[_services_gflags_pb2.ServicesGflagsProto, _Mapping]] = ..., proxy_server_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProxyServerConfig, _Mapping]] = ..., vip_vec: _Optional[_Iterable[str]] = ..., cluster_partition_host_name: _Optional[str] = ..., metadata_fault_tolerance_factor: _Optional[int] = ..., is_cluster_expand: bool = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., rack_id: _Optional[int] = ..., ntp_server_auth_keys_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo, _Mapping]]] = ..., dns_group_vec: _Optional[_Iterable[_Union[DnsGroup, _Mapping]]] = ..., cluster_subnet_group_vec: _Optional[_Iterable[_Union[ClusterSubnetGroup, _Mapping]]] = ..., ntp_authentication_enabled: bool = ..., allow_cluster_destroy_on_api_request: bool = ..., nexus_hmac_config_proto: _Optional[_Union[_nexus_hmac_key_config_pb2.NexusHmacKeyProto, _Mapping]] = ..., enable_hardware_encryption: bool = ..., enable_kernel_fips_mode: bool = ..., service_identity_trust_domain: _Optional[str] = ..., service_identity_trust_domain_mode: _Optional[int] = ..., operation_id: _Optional[str] = ..., cluster_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., aes_encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., generate_rootca: bool = ...) -> None: ...

class VirtualRoboClusterCreateRecord(_message.Message):
    __slots__ = ("cluster_name", "cluster_id", "cluster_incarnation_id", "ntp_server_vec", "dns_server_vec", "domain_name_vec", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "node_ip", "rotation_period_secs", "enable_software_encryption", "enable_fips_mode", "mtu", "ServicesGflagsProto", "proxy_server_config", "hostname", "ip_preference", "ntp_server_auth_keys_vec", "ntp_authentication_enabled", "service_identity_trust_domain", "service_identity_trust_domain_mode", "cluster_subnet_vec", "aes_encryption_mode")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    ROTATION_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SOFTWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIPS_MODE_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    SERVICESGFLAGSPROTO_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_AUTH_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    NTP_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IDENTITY_TRUST_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IDENTITY_TRUST_DOMAIN_MODE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    AES_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    ntp_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    node_ip: str
    rotation_period_secs: int
    enable_software_encryption: bool
    enable_fips_mode: bool
    mtu: int
    ServicesGflagsProto: _services_gflags_pb2.ServicesGflagsProto
    proxy_server_config: _cluster_config_pb2.ClusterConfigProto.ProxyServerConfig
    hostname: str
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    ntp_server_auth_keys_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo]
    ntp_authentication_enabled: bool
    service_identity_trust_domain: str
    service_identity_trust_domain_mode: int
    cluster_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    aes_encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., ntp_server_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., node_ip: _Optional[str] = ..., rotation_period_secs: _Optional[int] = ..., enable_software_encryption: bool = ..., enable_fips_mode: bool = ..., mtu: _Optional[int] = ..., ServicesGflagsProto: _Optional[_Union[_services_gflags_pb2.ServicesGflagsProto, _Mapping]] = ..., proxy_server_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProxyServerConfig, _Mapping]] = ..., hostname: _Optional[str] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., ntp_server_auth_keys_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo, _Mapping]]] = ..., ntp_authentication_enabled: bool = ..., service_identity_trust_domain: _Optional[str] = ..., service_identity_trust_domain_mode: _Optional[int] = ..., cluster_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., aes_encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...

class CloudClusterCreateRecord(_message.Message):
    __slots__ = ("other_node_ip_vec", "cluster_name", "last_updated_time_secs", "ntp_server_vec", "dns_server_vec", "domain_name_vec", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "cluster_id", "cluster_incarnation_id", "rotation_period_secs", "enable_software_encryption", "sender_node_ip", "metadata_fault_tolerance", "cluster_partition_hostname", "ip_preference", "cluster_size", "cluster_subnet_vec", "aes_encryption_mode")
    OTHER_NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROTATION_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SOFTWARE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    AES_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    other_node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_name: str
    last_updated_time_secs: int
    ntp_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    cluster_id: int
    cluster_incarnation_id: int
    rotation_period_secs: int
    enable_software_encryption: bool
    sender_node_ip: str
    metadata_fault_tolerance: int
    cluster_partition_hostname: str
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    cluster_size: _cluster_config_pb2.ClusterConfigProto.ClusterSize
    cluster_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    aes_encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, other_node_ip_vec: _Optional[_Iterable[str]] = ..., cluster_name: _Optional[str] = ..., last_updated_time_secs: _Optional[int] = ..., ntp_server_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., rotation_period_secs: _Optional[int] = ..., enable_software_encryption: bool = ..., sender_node_ip: _Optional[str] = ..., metadata_fault_tolerance: _Optional[int] = ..., cluster_partition_hostname: _Optional[str] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., cluster_size: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ClusterSize, str]] = ..., cluster_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., aes_encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...

class CloudClusterAddNodesRecord(_message.Message):
    __slots__ = ("node_ip_vec", "last_updated_time_secs", "cluster_partition_id", "sender_node_ip", "metadata_fault_tolerance", "cluster_subnet_cidr_len", "ip_preference", "cluster_subnet_ip", "cluster_gateway", "dns_server_vec", "operation_id")
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    last_updated_time_secs: int
    cluster_partition_id: int
    sender_node_ip: str
    metadata_fault_tolerance: int
    cluster_subnet_cidr_len: int
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    cluster_subnet_ip: str
    cluster_gateway: str
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    operation_id: str
    def __init__(self, node_ip_vec: _Optional[_Iterable[str]] = ..., last_updated_time_secs: _Optional[int] = ..., cluster_partition_id: _Optional[int] = ..., sender_node_ip: _Optional[str] = ..., metadata_fault_tolerance: _Optional[int] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_gateway: _Optional[str] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., operation_id: _Optional[str] = ...) -> None: ...

class CloudNodeJoinClusterRecord(_message.Message):
    __slots__ = ("last_updated_time_secs", "cluster_id", "incarnation_id", "cluster_partition_id", "sender_node_ip", "num_joining_nodes", "metadata_fault_tolerance", "cluster_subnet_cidr_len", "cluster_software_version", "software_package_urls", "node_ip", "cluster_subnet_ip", "cluster_gateway", "dns_server_vec")
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NUM_JOINING_NODES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_PACKAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    last_updated_time_secs: int
    cluster_id: int
    incarnation_id: int
    cluster_partition_id: int
    sender_node_ip: str
    num_joining_nodes: int
    metadata_fault_tolerance: int
    cluster_subnet_cidr_len: int
    cluster_software_version: str
    software_package_urls: _containers.RepeatedScalarFieldContainer[str]
    node_ip: str
    cluster_subnet_ip: str
    cluster_gateway: str
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, last_updated_time_secs: _Optional[int] = ..., cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., cluster_partition_id: _Optional[int] = ..., sender_node_ip: _Optional[str] = ..., num_joining_nodes: _Optional[int] = ..., metadata_fault_tolerance: _Optional[int] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_software_version: _Optional[str] = ..., software_package_urls: _Optional[_Iterable[str]] = ..., node_ip: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_gateway: _Optional[str] = ..., dns_server_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ClusterDestroyRecord(_message.Message):
    __slots__ = ("state", "other_node_ip_vec", "to_cleanup_disk_mount_path", "to_cleanup_disk_device_path", "last_updated_time_secs", "cluster_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[ClusterDestroyRecord.State]
        kToRemoveNodes: _ClassVar[ClusterDestroyRecord.State]
        kToRemoveJsonFile: _ClassVar[ClusterDestroyRecord.State]
        kToRemoveDirs: _ClassVar[ClusterDestroyRecord.State]
        kToCleanupDisks: _ClassVar[ClusterDestroyRecord.State]
    kIntent: ClusterDestroyRecord.State
    kToRemoveNodes: ClusterDestroyRecord.State
    kToRemoveJsonFile: ClusterDestroyRecord.State
    kToRemoveDirs: ClusterDestroyRecord.State
    kToCleanupDisks: ClusterDestroyRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    OTHER_NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    state: ClusterDestroyRecord.State
    other_node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    to_cleanup_disk_mount_path: str
    to_cleanup_disk_device_path: str
    last_updated_time_secs: int
    cluster_id: int
    def __init__(self, state: _Optional[_Union[ClusterDestroyRecord.State, str]] = ..., other_node_ip_vec: _Optional[_Iterable[str]] = ..., to_cleanup_disk_mount_path: _Optional[str] = ..., to_cleanup_disk_device_path: _Optional[str] = ..., last_updated_time_secs: _Optional[int] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class ClusterRemoveNodeRecord(_message.Message):
    __slots__ = ("node_id", "node_ip", "cluster_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    node_ip: str
    cluster_id: int
    def __init__(self, node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class NodeDisjoinClusterRecord(_message.Message):
    __slots__ = ("state", "cluster_id", "to_cleanup_disk_mount_path", "to_cleanup_disk_device_path", "last_updated_time_secs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[NodeDisjoinClusterRecord.State]
        kToRemoveDirs: _ClassVar[NodeDisjoinClusterRecord.State]
        kToCleanupDisks: _ClassVar[NodeDisjoinClusterRecord.State]
    kIntent: NodeDisjoinClusterRecord.State
    kToRemoveDirs: NodeDisjoinClusterRecord.State
    kToCleanupDisks: NodeDisjoinClusterRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    state: NodeDisjoinClusterRecord.State
    cluster_id: int
    to_cleanup_disk_mount_path: str
    to_cleanup_disk_device_path: str
    last_updated_time_secs: int
    def __init__(self, state: _Optional[_Union[NodeDisjoinClusterRecord.State, str]] = ..., cluster_id: _Optional[int] = ..., to_cleanup_disk_mount_path: _Optional[str] = ..., to_cleanup_disk_device_path: _Optional[str] = ..., last_updated_time_secs: _Optional[int] = ...) -> None: ...

class NodeUpgradeRecord(_message.Message):
    __slots__ = ("state", "node_current_software_version", "node_target_software_version", "last_updated_time_secs", "node_ids_to_upgrade", "upgrade_self", "upgrade_all_free_nodes", "ignoreSwIncompatibility")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[NodeUpgradeRecord.State]
        kPackageInstalled: _ClassVar[NodeUpgradeRecord.State]
        kToRemoveOldPackage: _ClassVar[NodeUpgradeRecord.State]
        kToRebootNode: _ClassVar[NodeUpgradeRecord.State]
    kIntent: NodeUpgradeRecord.State
    kPackageInstalled: NodeUpgradeRecord.State
    kToRemoveOldPackage: NodeUpgradeRecord.State
    kToRebootNode: NodeUpgradeRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    NODE_CURRENT_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_TARGET_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_TO_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SELF_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_ALL_FREE_NODES_FIELD_NUMBER: _ClassVar[int]
    IGNORESWINCOMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    state: NodeUpgradeRecord.State
    node_current_software_version: str
    node_target_software_version: str
    last_updated_time_secs: int
    node_ids_to_upgrade: _containers.RepeatedScalarFieldContainer[int]
    upgrade_self: bool
    upgrade_all_free_nodes: bool
    ignoreSwIncompatibility: bool
    def __init__(self, state: _Optional[_Union[NodeUpgradeRecord.State, str]] = ..., node_current_software_version: _Optional[str] = ..., node_target_software_version: _Optional[str] = ..., last_updated_time_secs: _Optional[int] = ..., node_ids_to_upgrade: _Optional[_Iterable[int]] = ..., upgrade_self: bool = ..., upgrade_all_free_nodes: bool = ..., ignoreSwIncompatibility: bool = ...) -> None: ...

class ClusterUpgradeRecord(_message.Message):
    __slots__ = ("state", "last_updated_time_secs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[ClusterUpgradeRecord.State]
        kAcquireUpgradeTicket: _ClassVar[ClusterUpgradeRecord.State]
        kToInstallPackage: _ClassVar[ClusterUpgradeRecord.State]
        kPackageInstalled: _ClassVar[ClusterUpgradeRecord.State]
        kToRemoveOldPackage: _ClassVar[ClusterUpgradeRecord.State]
        kToUpdateClusterConfig: _ClassVar[ClusterUpgradeRecord.State]
        kReleaseUpgradeTicket: _ClassVar[ClusterUpgradeRecord.State]
        kToRebootNode: _ClassVar[ClusterUpgradeRecord.State]
    kIntent: ClusterUpgradeRecord.State
    kAcquireUpgradeTicket: ClusterUpgradeRecord.State
    kToInstallPackage: ClusterUpgradeRecord.State
    kPackageInstalled: ClusterUpgradeRecord.State
    kToRemoveOldPackage: ClusterUpgradeRecord.State
    kToUpdateClusterConfig: ClusterUpgradeRecord.State
    kReleaseUpgradeTicket: ClusterUpgradeRecord.State
    kToRebootNode: ClusterUpgradeRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    state: ClusterUpgradeRecord.State
    last_updated_time_secs: int
    def __init__(self, state: _Optional[_Union[ClusterUpgradeRecord.State, str]] = ..., last_updated_time_secs: _Optional[int] = ...) -> None: ...

class ClusterRestartRecord(_message.Message):
    __slots__ = ("last_updated_time_secs", "node_boot_id")
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    NODE_BOOT_ID_FIELD_NUMBER: _ClassVar[int]
    last_updated_time_secs: int
    node_boot_id: str
    def __init__(self, last_updated_time_secs: _Optional[int] = ..., node_boot_id: _Optional[str] = ...) -> None: ...

class UpgradeChecksRecord(_message.Message):
    __slots__ = ("instance_id", "start_time_secs", "last_updated_time_secs")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    instance_id: int
    start_time_secs: int
    last_updated_time_secs: int
    def __init__(self, instance_id: _Optional[int] = ..., start_time_secs: _Optional[int] = ..., last_updated_time_secs: _Optional[int] = ...) -> None: ...

class RemoveNodeRecord(_message.Message):
    __slots__ = ("state", "to_cleanup_disk_mount_path", "to_cleanup_disk_device_path", "last_updated_time_secs", "forceful_removal")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[RemoveNodeRecord.State]
        kToStopGandalf: _ClassVar[RemoveNodeRecord.State]
        kToRemoveDirs: _ClassVar[RemoveNodeRecord.State]
        kToCleanupDisks: _ClassVar[RemoveNodeRecord.State]
    kIntent: RemoveNodeRecord.State
    kToStopGandalf: RemoveNodeRecord.State
    kToRemoveDirs: RemoveNodeRecord.State
    kToCleanupDisks: RemoveNodeRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    TO_CLEANUP_DISK_DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    FORCEFUL_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    state: RemoveNodeRecord.State
    to_cleanup_disk_mount_path: str
    to_cleanup_disk_device_path: str
    last_updated_time_secs: int
    forceful_removal: bool
    def __init__(self, state: _Optional[_Union[RemoveNodeRecord.State, str]] = ..., to_cleanup_disk_mount_path: _Optional[str] = ..., to_cleanup_disk_device_path: _Optional[str] = ..., last_updated_time_secs: _Optional[int] = ..., forceful_removal: bool = ...) -> None: ...

class DiskAssimilateRecord(_message.Message):
    __slots__ = ("disk_path_vec", "disk_serial_vec", "is_metadata")
    DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_SERIAL_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_METADATA_FIELD_NUMBER: _ClassVar[int]
    disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    disk_serial_vec: _containers.RepeatedScalarFieldContainer[str]
    is_metadata: bool
    def __init__(self, disk_path_vec: _Optional[_Iterable[str]] = ..., disk_serial_vec: _Optional[_Iterable[str]] = ..., is_metadata: bool = ...) -> None: ...

class DiskOfflineRecord(_message.Message):
    __slots__ = ("disk_id", "offline", "disk_type")
    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDiskTypeNone: _ClassVar[DiskOfflineRecord.DiskType]
        kDiskTypeSystem: _ClassVar[DiskOfflineRecord.DiskType]
        kDiskTypeData: _ClassVar[DiskOfflineRecord.DiskType]
        kDiskTypeBoth: _ClassVar[DiskOfflineRecord.DiskType]
    kDiskTypeNone: DiskOfflineRecord.DiskType
    kDiskTypeSystem: DiskOfflineRecord.DiskType
    kDiskTypeData: DiskOfflineRecord.DiskType
    kDiskTypeBoth: DiskOfflineRecord.DiskType
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    offline: bool
    disk_type: DiskOfflineRecord.DiskType
    def __init__(self, disk_id: _Optional[int] = ..., offline: bool = ..., disk_type: _Optional[_Union[DiskOfflineRecord.DiskType, str]] = ...) -> None: ...

class DiskExtendRecord(_message.Message):
    __slots__ = ("disk_serial_vec", "disk_path_vec", "boot_id")
    DISK_SERIAL_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    BOOT_ID_FIELD_NUMBER: _ClassVar[int]
    disk_serial_vec: _containers.RepeatedScalarFieldContainer[str]
    disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    boot_id: str
    def __init__(self, disk_serial_vec: _Optional[_Iterable[str]] = ..., disk_path_vec: _Optional[_Iterable[str]] = ..., boot_id: _Optional[str] = ...) -> None: ...

class RigelClusterCreateRecord(_message.Message):
    __slots__ = ("cluster_name", "cluster_id", "cluster_incarnation_id", "ntp_server_vec", "dns_server_vec", "domain_name_vec", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "ServicesGflagsProto", "proxy_server_config", "ip_preference", "hostname", "node_ip", "claim_token", "is_dhcp", "enable_support_channel", "enable_support_channel_end_time_msecs")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICESGFLAGSPROTO_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    CLAIM_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_DHCP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SUPPORT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SUPPORT_CHANNEL_END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    ntp_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    ServicesGflagsProto: _services_gflags_pb2.ServicesGflagsProto
    proxy_server_config: _cluster_config_pb2.ClusterConfigProto.ProxyServerConfig
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    hostname: str
    node_ip: str
    claim_token: str
    is_dhcp: bool
    enable_support_channel: bool
    enable_support_channel_end_time_msecs: int
    def __init__(self, cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., ntp_server_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., ServicesGflagsProto: _Optional[_Union[_services_gflags_pb2.ServicesGflagsProto, _Mapping]] = ..., proxy_server_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProxyServerConfig, _Mapping]] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., hostname: _Optional[str] = ..., node_ip: _Optional[str] = ..., claim_token: _Optional[str] = ..., is_dhcp: bool = ..., enable_support_channel: bool = ..., enable_support_channel_end_time_msecs: _Optional[int] = ...) -> None: ...

class ResetStateRecord(_message.Message):
    __slots__ = ("is_undo", "current_op")
    class ResetOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kResetStateOp: _ClassVar[ResetStateRecord.ResetOp]
        kNetworkScriptsOp: _ClassVar[ResetStateRecord.ResetOp]
        kReplaceNetworkScriptsOp: _ClassVar[ResetStateRecord.ResetOp]
        kSysconfigNetworkOp: _ClassVar[ResetStateRecord.ResetOp]
        kReplaceSysconfigNetworkOp: _ClassVar[ResetStateRecord.ResetOp]
        kIproute2Op: _ClassVar[ResetStateRecord.ResetOp]
        kReplaceIproute2Op: _ClassVar[ResetStateRecord.ResetOp]
        kOpenvswitchOp: _ClassVar[ResetStateRecord.ResetOp]
        kReplaceOpenvswitchOp: _ClassVar[ResetStateRecord.ResetOp]
        kNetworkingSysctlOp: _ClassVar[ResetStateRecord.ResetOp]
        kReplaceNetworkingSysctlOp: _ClassVar[ResetStateRecord.ResetOp]
        kNetworkConfigOp: _ClassVar[ResetStateRecord.ResetOp]
        kDoneOp: _ClassVar[ResetStateRecord.ResetOp]
    kResetStateOp: ResetStateRecord.ResetOp
    kNetworkScriptsOp: ResetStateRecord.ResetOp
    kReplaceNetworkScriptsOp: ResetStateRecord.ResetOp
    kSysconfigNetworkOp: ResetStateRecord.ResetOp
    kReplaceSysconfigNetworkOp: ResetStateRecord.ResetOp
    kIproute2Op: ResetStateRecord.ResetOp
    kReplaceIproute2Op: ResetStateRecord.ResetOp
    kOpenvswitchOp: ResetStateRecord.ResetOp
    kReplaceOpenvswitchOp: ResetStateRecord.ResetOp
    kNetworkingSysctlOp: ResetStateRecord.ResetOp
    kReplaceNetworkingSysctlOp: ResetStateRecord.ResetOp
    kNetworkConfigOp: ResetStateRecord.ResetOp
    kDoneOp: ResetStateRecord.ResetOp
    IS_UNDO_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OP_FIELD_NUMBER: _ClassVar[int]
    is_undo: bool
    current_op: ResetStateRecord.ResetOp
    def __init__(self, is_undo: bool = ..., current_op: _Optional[_Union[ResetStateRecord.ResetOp, str]] = ...) -> None: ...

class NetworkingResetRecord(_message.Message):
    __slots__ = ("state", "cluster_name", "cluster_id", "cluster_incarnation_id", "ntp_servers", "dns_servers", "domain_names", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "ipmi_gateway", "ipmi_subnet_ip", "ipmi_subnet_cidr_len", "ipmi_subnet_ipv4_mask", "ipmi_username", "ipmi_password", "node_vec", "req_type", "cluster_software_version", "bonding_mode", "mtu", "sender_node_ip", "node_ip_preference_vec", "in_progress", "vip_vec", "cluster_partition_host_name", "ip_preference", "ntp_server_auth_keys_vec", "dns_group_vec", "cluster_subnet_group_vec", "ntp_authentication_enabled", "apps_subnet", "apps_subnet_v6")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[NetworkingResetRecord.State]
        kNetworkConfigurationInProgress: _ClassVar[NetworkingResetRecord.State]
        kNetworkConfigurationDone: _ClassVar[NetworkingResetRecord.State]
    kIntent: NetworkingResetRecord.State
    kNetworkConfigurationInProgress: NetworkingResetRecord.State
    kNetworkConfigurationDone: NetworkingResetRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    IPMI_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    IPMI_USERNAME_FIELD_NUMBER: _ClassVar[int]
    IPMI_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    REQ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_PREFERENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_AUTH_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NTP_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    APPS_SUBNET_FIELD_NUMBER: _ClassVar[int]
    APPS_SUBNET_V6_FIELD_NUMBER: _ClassVar[int]
    state: NetworkingResetRecord.State
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    ntp_servers: _containers.RepeatedScalarFieldContainer[str]
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    domain_names: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    ipmi_gateway: str
    ipmi_subnet_ip: str
    ipmi_subnet_cidr_len: int
    ipmi_subnet_ipv4_mask: str
    ipmi_username: str
    ipmi_password: str
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    req_type: RestRequestType
    cluster_software_version: str
    bonding_mode: _cluster_config_pb2.ClusterConfigProto.BondingMode
    mtu: int
    sender_node_ip: str
    node_ip_preference_vec: _containers.RepeatedCompositeFieldContainer[NodeIpPreference]
    in_progress: bool
    vip_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_partition_host_name: str
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    ntp_server_auth_keys_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo]
    dns_group_vec: _containers.RepeatedCompositeFieldContainer[DnsGroup]
    cluster_subnet_group_vec: _containers.RepeatedCompositeFieldContainer[ClusterSubnetGroup]
    ntp_authentication_enabled: bool
    apps_subnet: _cluster_config_pb2.ClusterConfigProto.Subnet
    apps_subnet_v6: _cluster_config_pb2.ClusterConfigProto.Subnet
    def __init__(self, state: _Optional[_Union[NetworkingResetRecord.State, str]] = ..., cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., ntp_servers: _Optional[_Iterable[str]] = ..., dns_servers: _Optional[_Iterable[str]] = ..., domain_names: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., ipmi_gateway: _Optional[str] = ..., ipmi_subnet_ip: _Optional[str] = ..., ipmi_subnet_cidr_len: _Optional[int] = ..., ipmi_subnet_ipv4_mask: _Optional[str] = ..., ipmi_username: _Optional[str] = ..., ipmi_password: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ..., req_type: _Optional[_Union[RestRequestType, str]] = ..., cluster_software_version: _Optional[str] = ..., bonding_mode: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BondingMode, str]] = ..., mtu: _Optional[int] = ..., sender_node_ip: _Optional[str] = ..., node_ip_preference_vec: _Optional[_Iterable[_Union[NodeIpPreference, _Mapping]]] = ..., in_progress: bool = ..., vip_vec: _Optional[_Iterable[str]] = ..., cluster_partition_host_name: _Optional[str] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., ntp_server_auth_keys_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NTPAuthKeyInfo, _Mapping]]] = ..., dns_group_vec: _Optional[_Iterable[_Union[DnsGroup, _Mapping]]] = ..., cluster_subnet_group_vec: _Optional[_Iterable[_Union[ClusterSubnetGroup, _Mapping]]] = ..., ntp_authentication_enabled: bool = ..., apps_subnet: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]] = ..., apps_subnet_v6: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]] = ...) -> None: ...

class HeOnpremClusterCreateRecord(_message.Message):
    __slots__ = ("cluster_name", "cluster_id", "cluster_incarnation_id", "ntp_server_vec", "dns_server_vec", "domain_name_vec", "cluster_gateway", "cluster_subnet_ip", "cluster_subnet_cidr_len", "cluster_subnet_ipv4_mask", "ServicesGflagsProto", "proxy_server_config", "ip_preference", "hostname", "node_ip", "is_dhcp", "enable_support_channel", "enable_support_channel_end_time_msecs", "helios_onprem_config")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_CIDR_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_IPV4_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICESGFLAGSPROTO_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    IS_DHCP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SUPPORT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SUPPORT_CHANNEL_END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    HELIOS_ONPREM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    ntp_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_gateway: str
    cluster_subnet_ip: str
    cluster_subnet_cidr_len: int
    cluster_subnet_ipv4_mask: str
    ServicesGflagsProto: _services_gflags_pb2.ServicesGflagsProto
    proxy_server_config: _cluster_config_pb2.ClusterConfigProto.ProxyServerConfig
    ip_preference: _cluster_config_pb2.ClusterConfigProto.IpAddressFamily
    hostname: str
    node_ip: str
    is_dhcp: bool
    enable_support_channel: bool
    enable_support_channel_end_time_msecs: int
    helios_onprem_config: _cluster_config_pb2.ClusterConfigProto.HeliosOnpremConfig
    def __init__(self, cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., ntp_server_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., cluster_gateway: _Optional[str] = ..., cluster_subnet_ip: _Optional[str] = ..., cluster_subnet_cidr_len: _Optional[int] = ..., cluster_subnet_ipv4_mask: _Optional[str] = ..., ServicesGflagsProto: _Optional[_Union[_services_gflags_pb2.ServicesGflagsProto, _Mapping]] = ..., proxy_server_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProxyServerConfig, _Mapping]] = ..., ip_preference: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IpAddressFamily, str]] = ..., hostname: _Optional[str] = ..., node_ip: _Optional[str] = ..., is_dhcp: bool = ..., enable_support_channel: bool = ..., enable_support_channel_end_time_msecs: _Optional[int] = ..., helios_onprem_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.HeliosOnpremConfig, _Mapping]] = ...) -> None: ...

class SystemServiceBringupRecord(_message.Message):
    __slots__ = ("last_updated_time_secs",)
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    last_updated_time_secs: int
    def __init__(self, last_updated_time_secs: _Optional[int] = ...) -> None: ...

class CreateSnapshotRecord(_message.Message):
    __slots__ = ("req_type", "cluster_id", "snapshot_version", "node_vec", "sender_node_ip", "software_version", "hot_fix_version", "local_data_backup_location", "current_operation", "create_snapshot_state", "last_updated_time_secs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoStateChange: _ClassVar[CreateSnapshotRecord.State]
        kStartingBgOp: _ClassVar[CreateSnapshotRecord.State]
        kStoppingClusterService: _ClassVar[CreateSnapshotRecord.State]
        kWaitingForStopClusterService: _ClassVar[CreateSnapshotRecord.State]
        kStoppingGandalf: _ClassVar[CreateSnapshotRecord.State]
        kBackingUpLocalDataToRemote: _ClassVar[CreateSnapshotRecord.State]
        kWaitingForAllNodesLocalDataBackupDone: _ClassVar[CreateSnapshotRecord.State]
        kCreatingSnapshotOfRemoteData: _ClassVar[CreateSnapshotRecord.State]
        kStartingGandalf: _ClassVar[CreateSnapshotRecord.State]
        kStartingClusterService: _ClassVar[CreateSnapshotRecord.State]
        kWaitingForStartClusterService: _ClassVar[CreateSnapshotRecord.State]
        kBgOpFailed: _ClassVar[CreateSnapshotRecord.State]
        kBgOpCompleted: _ClassVar[CreateSnapshotRecord.State]
    kNoStateChange: CreateSnapshotRecord.State
    kStartingBgOp: CreateSnapshotRecord.State
    kStoppingClusterService: CreateSnapshotRecord.State
    kWaitingForStopClusterService: CreateSnapshotRecord.State
    kStoppingGandalf: CreateSnapshotRecord.State
    kBackingUpLocalDataToRemote: CreateSnapshotRecord.State
    kWaitingForAllNodesLocalDataBackupDone: CreateSnapshotRecord.State
    kCreatingSnapshotOfRemoteData: CreateSnapshotRecord.State
    kStartingGandalf: CreateSnapshotRecord.State
    kStartingClusterService: CreateSnapshotRecord.State
    kWaitingForStartClusterService: CreateSnapshotRecord.State
    kBgOpFailed: CreateSnapshotRecord.State
    kBgOpCompleted: CreateSnapshotRecord.State
    REQ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOT_FIX_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA_BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    req_type: SnapshotRequestType
    cluster_id: int
    snapshot_version: str
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    sender_node_ip: str
    software_version: str
    hot_fix_version: str
    local_data_backup_location: str
    current_operation: str
    create_snapshot_state: CreateSnapshotRecord.State
    last_updated_time_secs: int
    def __init__(self, req_type: _Optional[_Union[SnapshotRequestType, str]] = ..., cluster_id: _Optional[int] = ..., snapshot_version: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ..., sender_node_ip: _Optional[str] = ..., software_version: _Optional[str] = ..., hot_fix_version: _Optional[str] = ..., local_data_backup_location: _Optional[str] = ..., current_operation: _Optional[str] = ..., create_snapshot_state: _Optional[_Union[CreateSnapshotRecord.State, str]] = ..., last_updated_time_secs: _Optional[int] = ...) -> None: ...

class RestoreSnapshotRecord(_message.Message):
    __slots__ = ("req_type", "cluster_id", "snapshot_version", "restore_to_new_cluster", "node_vec", "sender_node_ip", "flash_blade_data_vips", "all_file_systems", "local_file_systems", "current_operation", "restore_snapshot_state", "last_updated_time_secs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoStateChange: _ClassVar[RestoreSnapshotRecord.State]
        kStartingBgOp: _ClassVar[RestoreSnapshotRecord.State]
        kStoppingClusterService: _ClassVar[RestoreSnapshotRecord.State]
        kWaitingForStopClusterService: _ClassVar[RestoreSnapshotRecord.State]
        kStoppingGandalf: _ClassVar[RestoreSnapshotRecord.State]
        kUnmountingNfsShares: _ClassVar[RestoreSnapshotRecord.State]
        kWaitingForRestoreRemoteDataSnapshotDone: _ClassVar[RestoreSnapshotRecord.State]
        kRestoringLocalDataFromRemoteBackup: _ClassVar[RestoreSnapshotRecord.State]
        kWaitingForAllNodesLocalDataRestoreDone: _ClassVar[RestoreSnapshotRecord.State]
        kStartingGandalf: _ClassVar[RestoreSnapshotRecord.State]
        kMountingNfsShares: _ClassVar[RestoreSnapshotRecord.State]
        kStartingClusterService: _ClassVar[RestoreSnapshotRecord.State]
        kWaitingForStartClusterService: _ClassVar[RestoreSnapshotRecord.State]
        kBgOpFailed: _ClassVar[RestoreSnapshotRecord.State]
        kBgOpCompleted: _ClassVar[RestoreSnapshotRecord.State]
    kNoStateChange: RestoreSnapshotRecord.State
    kStartingBgOp: RestoreSnapshotRecord.State
    kStoppingClusterService: RestoreSnapshotRecord.State
    kWaitingForStopClusterService: RestoreSnapshotRecord.State
    kStoppingGandalf: RestoreSnapshotRecord.State
    kUnmountingNfsShares: RestoreSnapshotRecord.State
    kWaitingForRestoreRemoteDataSnapshotDone: RestoreSnapshotRecord.State
    kRestoringLocalDataFromRemoteBackup: RestoreSnapshotRecord.State
    kWaitingForAllNodesLocalDataRestoreDone: RestoreSnapshotRecord.State
    kStartingGandalf: RestoreSnapshotRecord.State
    kMountingNfsShares: RestoreSnapshotRecord.State
    kStartingClusterService: RestoreSnapshotRecord.State
    kWaitingForStartClusterService: RestoreSnapshotRecord.State
    kBgOpFailed: RestoreSnapshotRecord.State
    kBgOpCompleted: RestoreSnapshotRecord.State
    REQ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_NEW_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    FLASH_BLADE_DATA_VIPS_FIELD_NUMBER: _ClassVar[int]
    ALL_FILE_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILE_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    req_type: SnapshotRequestType
    cluster_id: int
    snapshot_version: str
    restore_to_new_cluster: bool
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    sender_node_ip: str
    flash_blade_data_vips: _containers.RepeatedScalarFieldContainer[str]
    all_file_systems: _containers.RepeatedScalarFieldContainer[str]
    local_file_systems: _containers.RepeatedScalarFieldContainer[str]
    current_operation: str
    restore_snapshot_state: RestoreSnapshotRecord.State
    last_updated_time_secs: int
    def __init__(self, req_type: _Optional[_Union[SnapshotRequestType, str]] = ..., cluster_id: _Optional[int] = ..., snapshot_version: _Optional[str] = ..., restore_to_new_cluster: bool = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ..., sender_node_ip: _Optional[str] = ..., flash_blade_data_vips: _Optional[_Iterable[str]] = ..., all_file_systems: _Optional[_Iterable[str]] = ..., local_file_systems: _Optional[_Iterable[str]] = ..., current_operation: _Optional[str] = ..., restore_snapshot_state: _Optional[_Union[RestoreSnapshotRecord.State, str]] = ..., last_updated_time_secs: _Optional[int] = ...) -> None: ...

class NodeDisaggregateRecord(_message.Message):
    __slots__ = ("state", "cluster_id", "node_id", "sender_node_ip", "node_vec")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[NodeDisaggregateRecord.State]
        kBackupFiles: _ClassVar[NodeDisaggregateRecord.State]
        kStopServicesAndExit: _ClassVar[NodeDisaggregateRecord.State]
    kIntent: NodeDisaggregateRecord.State
    kBackupFiles: NodeDisaggregateRecord.State
    kStopServicesAndExit: NodeDisaggregateRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    state: NodeDisaggregateRecord.State
    cluster_id: int
    node_id: int
    sender_node_ip: str
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    def __init__(self, state: _Optional[_Union[NodeDisaggregateRecord.State, str]] = ..., cluster_id: _Optional[int] = ..., node_id: _Optional[int] = ..., sender_node_ip: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ...) -> None: ...

class NodeAggregateRecord(_message.Message):
    __slots__ = ("state", "cluster_name", "cluster_id", "cluster_incarnation_id", "cluster_software_version", "node_vec", "sender_node_ip", "primary_iface_name", "mtu", "bonding_mode", "node_id", "node_ip", "force_aggregate")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIntent: _ClassVar[NodeAggregateRecord.State]
        kRestoreFiles: _ClassVar[NodeAggregateRecord.State]
        kRestartServices: _ClassVar[NodeAggregateRecord.State]
    kIntent: NodeAggregateRecord.State
    kRestoreFiles: NodeAggregateRecord.State
    kRestartServices: NodeAggregateRecord.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    FORCE_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    state: NodeAggregateRecord.State
    cluster_name: str
    cluster_id: int
    cluster_incarnation_id: int
    cluster_software_version: str
    node_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Node]
    sender_node_ip: str
    primary_iface_name: str
    mtu: int
    bonding_mode: _cluster_config_pb2.ClusterConfigProto.BondingMode
    node_id: int
    node_ip: str
    force_aggregate: bool
    def __init__(self, state: _Optional[_Union[NodeAggregateRecord.State, str]] = ..., cluster_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_software_version: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Node, _Mapping]]] = ..., sender_node_ip: _Optional[str] = ..., primary_iface_name: _Optional[str] = ..., mtu: _Optional[int] = ..., bonding_mode: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BondingMode, str]] = ..., node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., force_aggregate: bool = ...) -> None: ...

class FirmwareUpgradeRecord(_message.Message):
    __slots__ = ("firmware_type", "device_serial_vec")
    class FirmwareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFirmwareTypeNone: _ClassVar[FirmwareUpgradeRecord.FirmwareType]
        kFirmwareTypePlatform: _ClassVar[FirmwareUpgradeRecord.FirmwareType]
        kFirmwareTypeDisk: _ClassVar[FirmwareUpgradeRecord.FirmwareType]
    kFirmwareTypeNone: FirmwareUpgradeRecord.FirmwareType
    kFirmwareTypePlatform: FirmwareUpgradeRecord.FirmwareType
    kFirmwareTypeDisk: FirmwareUpgradeRecord.FirmwareType
    FIRMWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SERIAL_VEC_FIELD_NUMBER: _ClassVar[int]
    firmware_type: FirmwareUpgradeRecord.FirmwareType
    device_serial_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, firmware_type: _Optional[_Union[FirmwareUpgradeRecord.FirmwareType, str]] = ..., device_serial_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class WalRecord(_message.Message):
    __slots__ = ("operation", "operation_start_time_secs", "cloud_cluster_create_record", "cloud_cluster_add_nodes_record", "cluster_destroy_record", "cloud_node_join_cluster_record", "node_disjoin_cluster_record", "node_upgrade_record", "cluster_upgrade_record", "remove_node_record", "cluster_remove_node_record", "disk_assimilate_record", "cluster_bringup_wal_record", "cluster_restart_record", "virtual_robo_cluster_create_record", "disk_offline_record", "disk_extend_record", "rigel_cluster_create_record", "networking_reset_record", "reset_state_record", "he_onprem_cluster_create_record", "system_service_bringup_record", "create_snapshot_record", "restore_snapshot_record", "node_aggregate_record", "node_disaggregate_record", "upgrade_checks_record", "firmware_upgrade_record")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[WalRecord.Operation]
        kClusterDestroy: _ClassVar[WalRecord.Operation]
        kClusterUpgrade: _ClassVar[WalRecord.Operation]
        kClusterRestart: _ClassVar[WalRecord.Operation]
        kNodeDisjoinCluster: _ClassVar[WalRecord.Operation]
        kNodeUpgrade: _ClassVar[WalRecord.Operation]
        kRemoveNode: _ClassVar[WalRecord.Operation]
        kClusterRemoveNode: _ClassVar[WalRecord.Operation]
        kDiskAssimilate: _ClassVar[WalRecord.Operation]
        kClusterBringup: _ClassVar[WalRecord.Operation]
        kCloudClusterCreate: _ClassVar[WalRecord.Operation]
        kCloudClusterAddNodes: _ClassVar[WalRecord.Operation]
        kCloudNodeJoinCluster: _ClassVar[WalRecord.Operation]
        kVirtualRoboClusterCreate: _ClassVar[WalRecord.Operation]
        kDiskOffline: _ClassVar[WalRecord.Operation]
        kDiskExtend: _ClassVar[WalRecord.Operation]
        kRigelClusterCreate: _ClassVar[WalRecord.Operation]
        kNetworkingReset: _ClassVar[WalRecord.Operation]
        kResetState: _ClassVar[WalRecord.Operation]
        kHeOnpremClusterCreate: _ClassVar[WalRecord.Operation]
        kSystemServiceBringup: _ClassVar[WalRecord.Operation]
        kCreateSnapshot: _ClassVar[WalRecord.Operation]
        kRestoreSnapshot: _ClassVar[WalRecord.Operation]
        kNodeDisaggregate: _ClassVar[WalRecord.Operation]
        kNodeAggregate: _ClassVar[WalRecord.Operation]
        kRunUpgradeChecks: _ClassVar[WalRecord.Operation]
        kFirmwareUpgrade: _ClassVar[WalRecord.Operation]
    kNone: WalRecord.Operation
    kClusterDestroy: WalRecord.Operation
    kClusterUpgrade: WalRecord.Operation
    kClusterRestart: WalRecord.Operation
    kNodeDisjoinCluster: WalRecord.Operation
    kNodeUpgrade: WalRecord.Operation
    kRemoveNode: WalRecord.Operation
    kClusterRemoveNode: WalRecord.Operation
    kDiskAssimilate: WalRecord.Operation
    kClusterBringup: WalRecord.Operation
    kCloudClusterCreate: WalRecord.Operation
    kCloudClusterAddNodes: WalRecord.Operation
    kCloudNodeJoinCluster: WalRecord.Operation
    kVirtualRoboClusterCreate: WalRecord.Operation
    kDiskOffline: WalRecord.Operation
    kDiskExtend: WalRecord.Operation
    kRigelClusterCreate: WalRecord.Operation
    kNetworkingReset: WalRecord.Operation
    kResetState: WalRecord.Operation
    kHeOnpremClusterCreate: WalRecord.Operation
    kSystemServiceBringup: WalRecord.Operation
    kCreateSnapshot: WalRecord.Operation
    kRestoreSnapshot: WalRecord.Operation
    kNodeDisaggregate: WalRecord.Operation
    kNodeAggregate: WalRecord.Operation
    kRunUpgradeChecks: WalRecord.Operation
    kFirmwareUpgrade: WalRecord.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CLUSTER_CREATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CLUSTER_ADD_NODES_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DESTROY_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NODE_JOIN_CLUSTER_RECORD_FIELD_NUMBER: _ClassVar[int]
    NODE_DISJOIN_CLUSTER_RECORD_FIELD_NUMBER: _ClassVar[int]
    NODE_UPGRADE_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UPGRADE_RECORD_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NODE_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_REMOVE_NODE_RECORD_FIELD_NUMBER: _ClassVar[int]
    DISK_ASSIMILATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BRINGUP_WAL_RECORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESTART_RECORD_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_ROBO_CLUSTER_CREATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    DISK_OFFLINE_RECORD_FIELD_NUMBER: _ClassVar[int]
    DISK_EXTEND_RECORD_FIELD_NUMBER: _ClassVar[int]
    RIGEL_CLUSTER_CREATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_RESET_RECORD_FIELD_NUMBER: _ClassVar[int]
    RESET_STATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    HE_ONPREM_CLUSTER_CREATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SERVICE_BRINGUP_RECORD_FIELD_NUMBER: _ClassVar[int]
    CREATE_SNAPSHOT_RECORD_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_RECORD_FIELD_NUMBER: _ClassVar[int]
    NODE_AGGREGATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    NODE_DISAGGREGATE_RECORD_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_CHECKS_RECORD_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPGRADE_RECORD_FIELD_NUMBER: _ClassVar[int]
    operation: WalRecord.Operation
    operation_start_time_secs: int
    cloud_cluster_create_record: CloudClusterCreateRecord
    cloud_cluster_add_nodes_record: CloudClusterAddNodesRecord
    cluster_destroy_record: ClusterDestroyRecord
    cloud_node_join_cluster_record: CloudNodeJoinClusterRecord
    node_disjoin_cluster_record: NodeDisjoinClusterRecord
    node_upgrade_record: NodeUpgradeRecord
    cluster_upgrade_record: ClusterUpgradeRecord
    remove_node_record: RemoveNodeRecord
    cluster_remove_node_record: ClusterRemoveNodeRecord
    disk_assimilate_record: DiskAssimilateRecord
    cluster_bringup_wal_record: ClusterBringupWalRecord
    cluster_restart_record: ClusterRestartRecord
    virtual_robo_cluster_create_record: VirtualRoboClusterCreateRecord
    disk_offline_record: DiskOfflineRecord
    disk_extend_record: DiskExtendRecord
    rigel_cluster_create_record: RigelClusterCreateRecord
    networking_reset_record: NetworkingResetRecord
    reset_state_record: ResetStateRecord
    he_onprem_cluster_create_record: HeOnpremClusterCreateRecord
    system_service_bringup_record: SystemServiceBringupRecord
    create_snapshot_record: CreateSnapshotRecord
    restore_snapshot_record: RestoreSnapshotRecord
    node_aggregate_record: NodeAggregateRecord
    node_disaggregate_record: NodeDisaggregateRecord
    upgrade_checks_record: UpgradeChecksRecord
    firmware_upgrade_record: FirmwareUpgradeRecord
    def __init__(self, operation: _Optional[_Union[WalRecord.Operation, str]] = ..., operation_start_time_secs: _Optional[int] = ..., cloud_cluster_create_record: _Optional[_Union[CloudClusterCreateRecord, _Mapping]] = ..., cloud_cluster_add_nodes_record: _Optional[_Union[CloudClusterAddNodesRecord, _Mapping]] = ..., cluster_destroy_record: _Optional[_Union[ClusterDestroyRecord, _Mapping]] = ..., cloud_node_join_cluster_record: _Optional[_Union[CloudNodeJoinClusterRecord, _Mapping]] = ..., node_disjoin_cluster_record: _Optional[_Union[NodeDisjoinClusterRecord, _Mapping]] = ..., node_upgrade_record: _Optional[_Union[NodeUpgradeRecord, _Mapping]] = ..., cluster_upgrade_record: _Optional[_Union[ClusterUpgradeRecord, _Mapping]] = ..., remove_node_record: _Optional[_Union[RemoveNodeRecord, _Mapping]] = ..., cluster_remove_node_record: _Optional[_Union[ClusterRemoveNodeRecord, _Mapping]] = ..., disk_assimilate_record: _Optional[_Union[DiskAssimilateRecord, _Mapping]] = ..., cluster_bringup_wal_record: _Optional[_Union[ClusterBringupWalRecord, _Mapping]] = ..., cluster_restart_record: _Optional[_Union[ClusterRestartRecord, _Mapping]] = ..., virtual_robo_cluster_create_record: _Optional[_Union[VirtualRoboClusterCreateRecord, _Mapping]] = ..., disk_offline_record: _Optional[_Union[DiskOfflineRecord, _Mapping]] = ..., disk_extend_record: _Optional[_Union[DiskExtendRecord, _Mapping]] = ..., rigel_cluster_create_record: _Optional[_Union[RigelClusterCreateRecord, _Mapping]] = ..., networking_reset_record: _Optional[_Union[NetworkingResetRecord, _Mapping]] = ..., reset_state_record: _Optional[_Union[ResetStateRecord, _Mapping]] = ..., he_onprem_cluster_create_record: _Optional[_Union[HeOnpremClusterCreateRecord, _Mapping]] = ..., system_service_bringup_record: _Optional[_Union[SystemServiceBringupRecord, _Mapping]] = ..., create_snapshot_record: _Optional[_Union[CreateSnapshotRecord, _Mapping]] = ..., restore_snapshot_record: _Optional[_Union[RestoreSnapshotRecord, _Mapping]] = ..., node_aggregate_record: _Optional[_Union[NodeAggregateRecord, _Mapping]] = ..., node_disaggregate_record: _Optional[_Union[NodeDisaggregateRecord, _Mapping]] = ..., upgrade_checks_record: _Optional[_Union[UpgradeChecksRecord, _Mapping]] = ..., firmware_upgrade_record: _Optional[_Union[FirmwareUpgradeRecord, _Mapping]] = ...) -> None: ...

class UpgraderOpStateRecord(_message.Message):
    __slots__ = ("last_updated_time_secs", "restart_attempts", "restart_reason")
    LAST_UPDATED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    RESTART_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RESTART_REASON_FIELD_NUMBER: _ClassVar[int]
    last_updated_time_secs: int
    restart_attempts: int
    restart_reason: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, last_updated_time_secs: _Optional[int] = ..., restart_attempts: _Optional[int] = ..., restart_reason: _Optional[_Iterable[str]] = ...) -> None: ...
