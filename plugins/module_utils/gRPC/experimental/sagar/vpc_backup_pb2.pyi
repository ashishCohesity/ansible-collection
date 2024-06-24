from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagInfo(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TagSpecification(_message.Message):
    __slots__ = ("resource_type", "tag_infos")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_INFOS_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    tag_infos: _containers.RepeatedCompositeFieldContainer[TagInfo]
    def __init__(self, resource_type: _Optional[str] = ..., tag_infos: _Optional[_Iterable[_Union[TagInfo, _Mapping]]] = ...) -> None: ...

class TransitGatewayMulticastDomain(_message.Message):
    __slots__ = ("tgw_multicast_domain_name", "transit_gateway_id", "tgw_multicast_domain_id", "tgw_multicast_domain_arn", "tgw_multicast_domain_state", "igmpv2_support_value", "static_sources_support_value", "auto_accept_shared_association_value", "tag_specification")
    TGW_MULTICAST_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_MULTICAST_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_MULTICAST_DOMAIN_ARN_FIELD_NUMBER: _ClassVar[int]
    TGW_MULTICAST_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    IGMPV2_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STATIC_SOURCES_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACCEPT_SHARED_ASSOCIATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    tgw_multicast_domain_name: str
    transit_gateway_id: str
    tgw_multicast_domain_id: str
    tgw_multicast_domain_arn: str
    tgw_multicast_domain_state: str
    igmpv2_support_value: str
    static_sources_support_value: str
    auto_accept_shared_association_value: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, tgw_multicast_domain_name: _Optional[str] = ..., transit_gateway_id: _Optional[str] = ..., tgw_multicast_domain_id: _Optional[str] = ..., tgw_multicast_domain_arn: _Optional[str] = ..., tgw_multicast_domain_state: _Optional[str] = ..., igmpv2_support_value: _Optional[str] = ..., static_sources_support_value: _Optional[str] = ..., auto_accept_shared_association_value: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class TransitGatewayRouteAttachment(_message.Message):
    __slots__ = ("resource_id", "tgw_attachment_id", "tgw_attachment_resource_type")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ATTACHMENT_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    tgw_attachment_id: str
    tgw_attachment_resource_type: str
    def __init__(self, resource_id: _Optional[str] = ..., tgw_attachment_id: _Optional[str] = ..., tgw_attachment_resource_type: _Optional[str] = ...) -> None: ...

class TransitGatewayRoute(_message.Message):
    __slots__ = ("destination_cidr_block", "prefix_list_id", "tgw_route_attachment_vec", "tgw_route_type", "tgw_route_state")
    DESTINATION_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_ATTACHMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    destination_cidr_block: str
    prefix_list_id: str
    tgw_route_attachment_vec: _containers.RepeatedCompositeFieldContainer[TransitGatewayRouteAttachment]
    tgw_route_type: str
    tgw_route_state: str
    def __init__(self, destination_cidr_block: _Optional[str] = ..., prefix_list_id: _Optional[str] = ..., tgw_route_attachment_vec: _Optional[_Iterable[_Union[TransitGatewayRouteAttachment, _Mapping]]] = ..., tgw_route_type: _Optional[str] = ..., tgw_route_state: _Optional[str] = ...) -> None: ...

class TransitGatewayAssociation(_message.Message):
    __slots__ = ("resource_id", "attachment_id", "tgw_association_state", "tgw_attachment_resource_type")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ASSOCIATION_STATE_FIELD_NUMBER: _ClassVar[int]
    TGW_ATTACHMENT_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    attachment_id: str
    tgw_association_state: str
    tgw_attachment_resource_type: str
    def __init__(self, resource_id: _Optional[str] = ..., attachment_id: _Optional[str] = ..., tgw_association_state: _Optional[str] = ..., tgw_attachment_resource_type: _Optional[str] = ...) -> None: ...

class TransitGatewayPropagation(_message.Message):
    __slots__ = ("tgw_attachment_id", "tgw_propagation_state")
    TGW_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_PROPAGATION_STATE_FIELD_NUMBER: _ClassVar[int]
    tgw_attachment_id: str
    tgw_propagation_state: str
    def __init__(self, tgw_attachment_id: _Optional[str] = ..., tgw_propagation_state: _Optional[str] = ...) -> None: ...

class TransitGatewayRouteTable(_message.Message):
    __slots__ = ("transit_gateway_id", "tgw_route_table_name", "default_association_route_table", "default_propagation_route_table", "tgw_route_table_ids", "tgw_route_table_state", "tgw_propagation_info", "tgw_route_info", "tag_specification", "tgw_association_info")
    TRANSIT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ASSOCIATION_ROUTE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROPAGATION_ROUTE_TABLE_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_TABLE_IDS_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_TABLE_STATE_FIELD_NUMBER: _ClassVar[int]
    TGW_PROPAGATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_INFO_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    TGW_ASSOCIATION_INFO_FIELD_NUMBER: _ClassVar[int]
    transit_gateway_id: str
    tgw_route_table_name: str
    default_association_route_table: bool
    default_propagation_route_table: bool
    tgw_route_table_ids: str
    tgw_route_table_state: str
    tgw_propagation_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayPropagation]
    tgw_route_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayRoute]
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    tgw_association_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayAssociation]
    def __init__(self, transit_gateway_id: _Optional[str] = ..., tgw_route_table_name: _Optional[str] = ..., default_association_route_table: bool = ..., default_propagation_route_table: bool = ..., tgw_route_table_ids: _Optional[str] = ..., tgw_route_table_state: _Optional[str] = ..., tgw_propagation_info: _Optional[_Iterable[_Union[TransitGatewayPropagation, _Mapping]]] = ..., tgw_route_info: _Optional[_Iterable[_Union[TransitGatewayRoute, _Mapping]]] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ..., tgw_association_info: _Optional[_Iterable[_Union[TransitGatewayAssociation, _Mapping]]] = ...) -> None: ...

class TransitGatewayCidrBlock(_message.Message):
    __slots__ = ("cidr_block_id",)
    CIDR_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    cidr_block_id: str
    def __init__(self, cidr_block_id: _Optional[str] = ...) -> None: ...

class TransitGateway(_message.Message):
    __slots__ = ("transit_gateway_name", "transit_gateway_id", "transit_gateway_arn", "transit_gateway_description", "amazon_side_asn", "auto_accept_shared_attachment", "default_route_table_association", "association_default_route_table_id", "default_route_table_propagation", "propagation_default_route_table_id", "vpn_ecmp_support_value", "dns_support_value", "multicast_support_value", "transit_gateway_cidr_blocks", "transit_gateway_state", "tag_specification")
    TRANSIT_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_ARN_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMAZON_SIDE_ASN_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACCEPT_SHARED_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUTE_TABLE_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_DEFAULT_ROUTE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUTE_TABLE_PROPAGATION_FIELD_NUMBER: _ClassVar[int]
    PROPAGATION_DEFAULT_ROUTE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    VPN_ECMP_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DNS_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_STATE_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    transit_gateway_name: str
    transit_gateway_id: str
    transit_gateway_arn: str
    transit_gateway_description: str
    amazon_side_asn: int
    auto_accept_shared_attachment: str
    default_route_table_association: str
    association_default_route_table_id: str
    default_route_table_propagation: str
    propagation_default_route_table_id: str
    vpn_ecmp_support_value: str
    dns_support_value: str
    multicast_support_value: str
    transit_gateway_cidr_blocks: _containers.RepeatedCompositeFieldContainer[TransitGatewayCidrBlock]
    transit_gateway_state: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, transit_gateway_name: _Optional[str] = ..., transit_gateway_id: _Optional[str] = ..., transit_gateway_arn: _Optional[str] = ..., transit_gateway_description: _Optional[str] = ..., amazon_side_asn: _Optional[int] = ..., auto_accept_shared_attachment: _Optional[str] = ..., default_route_table_association: _Optional[str] = ..., association_default_route_table_id: _Optional[str] = ..., default_route_table_propagation: _Optional[str] = ..., propagation_default_route_table_id: _Optional[str] = ..., vpn_ecmp_support_value: _Optional[str] = ..., dns_support_value: _Optional[str] = ..., multicast_support_value: _Optional[str] = ..., transit_gateway_cidr_blocks: _Optional[_Iterable[_Union[TransitGatewayCidrBlock, _Mapping]]] = ..., transit_gateway_state: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class TransitGatewaySubnet(_message.Message):
    __slots__ = ("subnet_ids",)
    SUBNET_IDS_FIELD_NUMBER: _ClassVar[int]
    subnet_ids: str
    def __init__(self, subnet_ids: _Optional[str] = ...) -> None: ...

class TransitGatewayVpcAttachment(_message.Message):
    __slots__ = ("tgw_vpc_attachment_name", "transit_gateway_id", "tgw_vpc_attachment_id", "vpc_id", "tgw_attachment_state", "ipv6_support_value", "dns_support_value", "appliance_mode_support_value", "tag_specification", "tgw_subnet_id")
    TGW_VPC_ATTACHMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_VPC_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    TGW_ATTACHMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    IPV6_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DNS_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_MODE_SUPPORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    TGW_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    tgw_vpc_attachment_name: str
    transit_gateway_id: str
    tgw_vpc_attachment_id: str
    vpc_id: str
    tgw_attachment_state: str
    ipv6_support_value: str
    dns_support_value: str
    appliance_mode_support_value: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    tgw_subnet_id: _containers.RepeatedCompositeFieldContainer[TransitGatewaySubnet]
    def __init__(self, tgw_vpc_attachment_name: _Optional[str] = ..., transit_gateway_id: _Optional[str] = ..., tgw_vpc_attachment_id: _Optional[str] = ..., vpc_id: _Optional[str] = ..., tgw_attachment_state: _Optional[str] = ..., ipv6_support_value: _Optional[str] = ..., dns_support_value: _Optional[str] = ..., appliance_mode_support_value: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ..., tgw_subnet_id: _Optional[_Iterable[_Union[TransitGatewaySubnet, _Mapping]]] = ...) -> None: ...

class FlowLogs(_message.Message):
    __slots__ = ("flow_log_id", "deliver_logs_error_message", "deliver_logs_permission_arn", "deliver_logs_status", "flow_log_status", "log_group_name", "resource_id", "log_destination", "log_format", "max_aggregation_interval", "tag_info", "traffic_type", "log_destination_type")
    FLOW_LOG_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVER_LOGS_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELIVER_LOGS_PERMISSION_ARN_FIELD_NUMBER: _ClassVar[int]
    DELIVER_LOGS_STATUS_FIELD_NUMBER: _ClassVar[int]
    FLOW_LOG_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_AGGREGATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TAG_INFO_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_DESTINATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    flow_log_id: str
    deliver_logs_error_message: str
    deliver_logs_permission_arn: str
    deliver_logs_status: str
    flow_log_status: str
    log_group_name: str
    resource_id: str
    log_destination: str
    log_format: str
    max_aggregation_interval: int
    tag_info: _containers.RepeatedCompositeFieldContainer[TagInfo]
    traffic_type: str
    log_destination_type: str
    def __init__(self, flow_log_id: _Optional[str] = ..., deliver_logs_error_message: _Optional[str] = ..., deliver_logs_permission_arn: _Optional[str] = ..., deliver_logs_status: _Optional[str] = ..., flow_log_status: _Optional[str] = ..., log_group_name: _Optional[str] = ..., resource_id: _Optional[str] = ..., log_destination: _Optional[str] = ..., log_format: _Optional[str] = ..., max_aggregation_interval: _Optional[int] = ..., tag_info: _Optional[_Iterable[_Union[TagInfo, _Mapping]]] = ..., traffic_type: _Optional[str] = ..., log_destination_type: _Optional[str] = ...) -> None: ...

class SecurityGroupIdentifier(_message.Message):
    __slots__ = ("security_group_name", "security_group_id")
    SECURITY_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    security_group_name: str
    security_group_id: str
    def __init__(self, security_group_name: _Optional[str] = ..., security_group_id: _Optional[str] = ...) -> None: ...

class DnsEntry(_message.Message):
    __slots__ = ("dns_name", "hosted_zone_id")
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTED_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    dns_name: str
    hosted_zone_id: str
    def __init__(self, dns_name: _Optional[str] = ..., hosted_zone_id: _Optional[str] = ...) -> None: ...

class EndpointRouteTableId(_message.Message):
    __slots__ = ("endpoint_route_table_id",)
    ENDPOINT_ROUTE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_route_table_id: str
    def __init__(self, endpoint_route_table_id: _Optional[str] = ...) -> None: ...

class EndpointSubnetId(_message.Message):
    __slots__ = ("endpoint_subnet_id",)
    ENDPOINT_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_subnet_id: str
    def __init__(self, endpoint_subnet_id: _Optional[str] = ...) -> None: ...

class VpcEndpoint(_message.Message):
    __slots__ = ("vpc_endpoint_id", "vpc_endpoint_name", "vpc_endpoint_type", "endpoint_service_name", "endpoint_policy_document", "endpoint_subnet_id_vec", "endpoint_route_table_id_vec", "security_group_vec", "dns_entries_vec", "tag_specification")
    VPC_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_ENDPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_ENDPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_POLICY_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_SUBNET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ROUTE_TABLE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    vpc_endpoint_id: str
    vpc_endpoint_name: str
    vpc_endpoint_type: str
    endpoint_service_name: str
    endpoint_policy_document: str
    endpoint_subnet_id_vec: _containers.RepeatedCompositeFieldContainer[EndpointSubnetId]
    endpoint_route_table_id_vec: _containers.RepeatedCompositeFieldContainer[EndpointRouteTableId]
    security_group_vec: _containers.RepeatedCompositeFieldContainer[SecurityGroupIdentifier]
    dns_entries_vec: _containers.RepeatedCompositeFieldContainer[DnsEntry]
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, vpc_endpoint_id: _Optional[str] = ..., vpc_endpoint_name: _Optional[str] = ..., vpc_endpoint_type: _Optional[str] = ..., endpoint_service_name: _Optional[str] = ..., endpoint_policy_document: _Optional[str] = ..., endpoint_subnet_id_vec: _Optional[_Iterable[_Union[EndpointSubnetId, _Mapping]]] = ..., endpoint_route_table_id_vec: _Optional[_Iterable[_Union[EndpointRouteTableId, _Mapping]]] = ..., security_group_vec: _Optional[_Iterable[_Union[SecurityGroupIdentifier, _Mapping]]] = ..., dns_entries_vec: _Optional[_Iterable[_Union[DnsEntry, _Mapping]]] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class PortRange(_message.Message):
    __slots__ = ("first_port", "last_port")
    FIRST_PORT_FIELD_NUMBER: _ClassVar[int]
    LAST_PORT_FIELD_NUMBER: _ClassVar[int]
    first_port: int
    last_port: int
    def __init__(self, first_port: _Optional[int] = ..., last_port: _Optional[int] = ...) -> None: ...

class IcpmTypeCode(_message.Message):
    __slots__ = ("code", "type")
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    code: int
    type: int
    def __init__(self, code: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class NetworkAclEntry(_message.Message):
    __slots__ = ("cidr_block", "is_egress", "ipv6_cidr_block", "port_range", "icpm_type_code", "protocol_number", "rule_action", "rule_number")
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    IS_EGRESS_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    ICPM_TYPE_CODE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RULE_ACTION_FIELD_NUMBER: _ClassVar[int]
    RULE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    cidr_block: str
    is_egress: bool
    ipv6_cidr_block: str
    port_range: _containers.RepeatedCompositeFieldContainer[PortRange]
    icpm_type_code: _containers.RepeatedCompositeFieldContainer[IcpmTypeCode]
    protocol_number: str
    rule_action: str
    rule_number: int
    def __init__(self, cidr_block: _Optional[str] = ..., is_egress: bool = ..., ipv6_cidr_block: _Optional[str] = ..., port_range: _Optional[_Iterable[_Union[PortRange, _Mapping]]] = ..., icpm_type_code: _Optional[_Iterable[_Union[IcpmTypeCode, _Mapping]]] = ..., protocol_number: _Optional[str] = ..., rule_action: _Optional[str] = ..., rule_number: _Optional[int] = ...) -> None: ...

class NetworkAclAssociation(_message.Message):
    __slots__ = ("network_acl_association_id", "associated_subnet_id")
    NETWORK_ACL_ASSOCIATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    network_acl_association_id: str
    associated_subnet_id: str
    def __init__(self, network_acl_association_id: _Optional[str] = ..., associated_subnet_id: _Optional[str] = ...) -> None: ...

class NetworkAcl(_message.Message):
    __slots__ = ("network_acl_id", "network_acl_name", "entries_vec", "association_vec", "tag_specification")
    NETWORK_ACL_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ACL_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    network_acl_id: str
    network_acl_name: str
    entries_vec: _containers.RepeatedCompositeFieldContainer[NetworkAclEntry]
    association_vec: _containers.RepeatedCompositeFieldContainer[NetworkAclAssociation]
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, network_acl_id: _Optional[str] = ..., network_acl_name: _Optional[str] = ..., entries_vec: _Optional[_Iterable[_Union[NetworkAclEntry, _Mapping]]] = ..., association_vec: _Optional[_Iterable[_Union[NetworkAclAssociation, _Mapping]]] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class VpnGateway(_message.Message):
    __slots__ = ("vpn_gateway_id", "vpn_gateway_name", "vpn_gateway_availability_zone", "amazon_side_asn", "vpn_gateway_type", "tag_specification")
    VPN_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    VPN_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VPN_GATEWAY_AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    AMAZON_SIDE_ASN_FIELD_NUMBER: _ClassVar[int]
    VPN_GATEWAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    vpn_gateway_id: str
    vpn_gateway_name: str
    vpn_gateway_availability_zone: str
    amazon_side_asn: int
    vpn_gateway_type: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, vpn_gateway_id: _Optional[str] = ..., vpn_gateway_name: _Optional[str] = ..., vpn_gateway_availability_zone: _Optional[str] = ..., amazon_side_asn: _Optional[int] = ..., vpn_gateway_type: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class EgressOnlyInternetGateway(_message.Message):
    __slots__ = ("egress_only_internet_gateway_id", "egress_only_internet_gateway_name", "tag_specification")
    EGRESS_ONLY_INTERNET_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    EGRESS_ONLY_INTERNET_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    egress_only_internet_gateway_id: str
    egress_only_internet_gateway_name: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, egress_only_internet_gateway_id: _Optional[str] = ..., egress_only_internet_gateway_name: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class NatGateway(_message.Message):
    __slots__ = ("nat_gateway_id", "nat_subnet_id", "nat_gateway_name", "tag_specification")
    NAT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    NAT_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    NAT_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    nat_gateway_id: str
    nat_subnet_id: str
    nat_gateway_name: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, nat_gateway_id: _Optional[str] = ..., nat_subnet_id: _Optional[str] = ..., nat_gateway_name: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class AttributeValue(_message.Message):
    __slots__ = ("attribute_value",)
    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    attribute_value: str
    def __init__(self, attribute_value: _Optional[str] = ...) -> None: ...

class DhcpConfiguration(_message.Message):
    __slots__ = ("dhcp_config_key", "attribute_value_vec")
    DHCP_CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
    dhcp_config_key: str
    attribute_value_vec: _containers.RepeatedCompositeFieldContainer[AttributeValue]
    def __init__(self, dhcp_config_key: _Optional[str] = ..., attribute_value_vec: _Optional[_Iterable[_Union[AttributeValue, _Mapping]]] = ...) -> None: ...

class DhcpOption(_message.Message):
    __slots__ = ("dhcp_option_id", "dhcp_option_name", "dhcp_config_vec", "tag_specification")
    DHCP_OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    DHCP_OPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DHCP_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    dhcp_option_id: str
    dhcp_option_name: str
    dhcp_config_vec: _containers.RepeatedCompositeFieldContainer[DhcpConfiguration]
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, dhcp_option_id: _Optional[str] = ..., dhcp_option_name: _Optional[str] = ..., dhcp_config_vec: _Optional[_Iterable[_Union[DhcpConfiguration, _Mapping]]] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class CarrierGateway(_message.Message):
    __slots__ = ("carrier_gateway_id", "carrier_gateway_name", "tag_specification")
    CARRIER_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    carrier_gateway_id: str
    carrier_gateway_name: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, carrier_gateway_id: _Optional[str] = ..., carrier_gateway_name: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class InternetGateway(_message.Message):
    __slots__ = ("internet_gateway_id", "internet_gateway_name", "tag_specification")
    INTERNET_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNET_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    internet_gateway_id: str
    internet_gateway_name: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    def __init__(self, internet_gateway_id: _Optional[str] = ..., internet_gateway_name: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ("route_destination_cidr_block", "route_destination_ipv6_cidr_block", "route_destination_prefix_list_id", "route_egress_only_internet_gateway_id", "route_gateway_id", "route_nat_gateway_id", "route_transit_gateway_id", "route_carrier_gateway_id", "route_local_gateway_id", "route_vpc_peering_connection_id")
    ROUTE_DESTINATION_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ROUTE_DESTINATION_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ROUTE_DESTINATION_PREFIX_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_EGRESS_ONLY_INTERNET_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_NAT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TRANSIT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_CARRIER_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_LOCAL_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_VPC_PEERING_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    route_destination_cidr_block: str
    route_destination_ipv6_cidr_block: str
    route_destination_prefix_list_id: str
    route_egress_only_internet_gateway_id: str
    route_gateway_id: str
    route_nat_gateway_id: str
    route_transit_gateway_id: str
    route_carrier_gateway_id: str
    route_local_gateway_id: str
    route_vpc_peering_connection_id: str
    def __init__(self, route_destination_cidr_block: _Optional[str] = ..., route_destination_ipv6_cidr_block: _Optional[str] = ..., route_destination_prefix_list_id: _Optional[str] = ..., route_egress_only_internet_gateway_id: _Optional[str] = ..., route_gateway_id: _Optional[str] = ..., route_nat_gateway_id: _Optional[str] = ..., route_transit_gateway_id: _Optional[str] = ..., route_carrier_gateway_id: _Optional[str] = ..., route_local_gateway_id: _Optional[str] = ..., route_vpc_peering_connection_id: _Optional[str] = ...) -> None: ...

class Association(_message.Message):
    __slots__ = ("associated_subnet_id", "route_table_association_id", "associated_gateway_id")
    ASSOCIATED_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLE_ASSOCIATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    associated_subnet_id: str
    route_table_association_id: str
    associated_gateway_id: str
    def __init__(self, associated_subnet_id: _Optional[str] = ..., route_table_association_id: _Optional[str] = ..., associated_gateway_id: _Optional[str] = ...) -> None: ...

class PropagatingVgw(_message.Message):
    __slots__ = ("vgw_gateway_id",)
    VGW_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    vgw_gateway_id: str
    def __init__(self, vgw_gateway_id: _Optional[str] = ...) -> None: ...

class RouteTableInfo(_message.Message):
    __slots__ = ("route_table_id", "route_vec", "association_vec", "route_table_name", "tag_specification", "propagating_vgw_vec")
    ROUTE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_VEC_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    PROPAGATING_VGW_VEC_FIELD_NUMBER: _ClassVar[int]
    route_table_id: str
    route_vec: _containers.RepeatedCompositeFieldContainer[Route]
    association_vec: _containers.RepeatedCompositeFieldContainer[Association]
    route_table_name: str
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    propagating_vgw_vec: _containers.RepeatedCompositeFieldContainer[PropagatingVgw]
    def __init__(self, route_table_id: _Optional[str] = ..., route_vec: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., association_vec: _Optional[_Iterable[_Union[Association, _Mapping]]] = ..., route_table_name: _Optional[str] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ..., propagating_vgw_vec: _Optional[_Iterable[_Union[PropagatingVgw, _Mapping]]] = ...) -> None: ...

class SubnetIpv6CidrBlockAssociation(_message.Message):
    __slots__ = ("subnet_ipv6_association_id", "ipv6_cidr_block")
    SUBNET_IPV6_ASSOCIATION_ID_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    subnet_ipv6_association_id: str
    ipv6_cidr_block: str
    def __init__(self, subnet_ipv6_association_id: _Optional[str] = ..., ipv6_cidr_block: _Optional[str] = ...) -> None: ...

class SubnetInfo(_message.Message):
    __slots__ = ("subnet_id", "availability_zone", "cidr_block", "availability_zone_id", "subnet_is_default", "customer_owned_ipv4_pool", "subnet_arn", "subnet_outpost_arn", "subnet_name", "subnet_ipv6_cidr_block", "tag_specification", "map_public_ip_on_launch", "map_customer_owner_ip_on_launch", "assign_ipv6_address_on_creation", "subnet_flow_log_info")
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_OWNED_IPV4_POOL_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ARN_FIELD_NUMBER: _ClassVar[int]
    SUBNET_OUTPOST_ARN_FIELD_NUMBER: _ClassVar[int]
    SUBNET_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    MAP_PUBLIC_IP_ON_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    MAP_CUSTOMER_OWNER_IP_ON_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_IPV6_ADDRESS_ON_CREATION_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FLOW_LOG_INFO_FIELD_NUMBER: _ClassVar[int]
    subnet_id: str
    availability_zone: str
    cidr_block: str
    availability_zone_id: str
    subnet_is_default: bool
    customer_owned_ipv4_pool: str
    subnet_arn: str
    subnet_outpost_arn: str
    subnet_name: str
    subnet_ipv6_cidr_block: _containers.RepeatedCompositeFieldContainer[SubnetIpv6CidrBlockAssociation]
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    map_public_ip_on_launch: bool
    map_customer_owner_ip_on_launch: bool
    assign_ipv6_address_on_creation: bool
    subnet_flow_log_info: _containers.RepeatedCompositeFieldContainer[FlowLogs]
    def __init__(self, subnet_id: _Optional[str] = ..., availability_zone: _Optional[str] = ..., cidr_block: _Optional[str] = ..., availability_zone_id: _Optional[str] = ..., subnet_is_default: bool = ..., customer_owned_ipv4_pool: _Optional[str] = ..., subnet_arn: _Optional[str] = ..., subnet_outpost_arn: _Optional[str] = ..., subnet_name: _Optional[str] = ..., subnet_ipv6_cidr_block: _Optional[_Iterable[_Union[SubnetIpv6CidrBlockAssociation, _Mapping]]] = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ..., map_public_ip_on_launch: bool = ..., map_customer_owner_ip_on_launch: bool = ..., assign_ipv6_address_on_creation: bool = ..., subnet_flow_log_info: _Optional[_Iterable[_Union[FlowLogs, _Mapping]]] = ...) -> None: ...

class VPCInfo(_message.Message):
    __slots__ = ("vpc_id", "vpc_name", "vpc_primary_cidr_block", "vpc_dhcp_options_id", "vpc_owner_id", "instance_tenancy", "vpc_associated_ipv6_id", "vpc_ipv6_cidr_block", "network_border_group", "ipv6_pool", "vpc_is_default", "tag_specification", "subnet_vec", "route_table_vec", "internet_gateway_vec", "carrier_gateway_vec", "nat_gateway_vec", "eigw_vec", "vpn_gateway_vec", "network_acl_vec", "vpc_endpoint_vec", "vpc_hostname", "vpc_resolution", "dhcp_option_vec", "flow_logs_info", "transit_gateway_info", "tgw_route_table_info", "tgw_multicast_domain_info", "tgw_vpc_attachment_info")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_PRIMARY_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    VPC_DHCP_OPTIONS_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TENANCY_FIELD_NUMBER: _ClassVar[int]
    VPC_ASSOCIATED_IPV6_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BORDER_GROUP_FIELD_NUMBER: _ClassVar[int]
    IPV6_POOL_FIELD_NUMBER: _ClassVar[int]
    VPC_IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLE_VEC_FIELD_NUMBER: _ClassVar[int]
    INTERNET_GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
    CARRIER_GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
    NAT_GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
    EIGW_VEC_FIELD_NUMBER: _ClassVar[int]
    VPN_GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ACL_VEC_FIELD_NUMBER: _ClassVar[int]
    VPC_ENDPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    VPC_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    VPC_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    DHCP_OPTION_VEC_FIELD_NUMBER: _ClassVar[int]
    FLOW_LOGS_INFO_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_GATEWAY_INFO_FIELD_NUMBER: _ClassVar[int]
    TGW_ROUTE_TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    TGW_MULTICAST_DOMAIN_INFO_FIELD_NUMBER: _ClassVar[int]
    TGW_VPC_ATTACHMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    vpc_name: str
    vpc_primary_cidr_block: str
    vpc_dhcp_options_id: str
    vpc_owner_id: str
    instance_tenancy: str
    vpc_associated_ipv6_id: str
    vpc_ipv6_cidr_block: str
    network_border_group: str
    ipv6_pool: str
    vpc_is_default: bool
    tag_specification: _containers.RepeatedCompositeFieldContainer[TagSpecification]
    subnet_vec: _containers.RepeatedCompositeFieldContainer[SubnetInfo]
    route_table_vec: _containers.RepeatedCompositeFieldContainer[RouteTableInfo]
    internet_gateway_vec: _containers.RepeatedCompositeFieldContainer[InternetGateway]
    carrier_gateway_vec: _containers.RepeatedCompositeFieldContainer[CarrierGateway]
    nat_gateway_vec: _containers.RepeatedCompositeFieldContainer[NatGateway]
    eigw_vec: _containers.RepeatedCompositeFieldContainer[EgressOnlyInternetGateway]
    vpn_gateway_vec: _containers.RepeatedCompositeFieldContainer[VpnGateway]
    network_acl_vec: _containers.RepeatedCompositeFieldContainer[NetworkAcl]
    vpc_endpoint_vec: _containers.RepeatedCompositeFieldContainer[VpcEndpoint]
    vpc_hostname: bool
    vpc_resolution: bool
    dhcp_option_vec: _containers.RepeatedCompositeFieldContainer[DhcpOption]
    flow_logs_info: _containers.RepeatedCompositeFieldContainer[FlowLogs]
    transit_gateway_info: _containers.RepeatedCompositeFieldContainer[TransitGateway]
    tgw_route_table_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayRouteTable]
    tgw_multicast_domain_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayMulticastDomain]
    tgw_vpc_attachment_info: _containers.RepeatedCompositeFieldContainer[TransitGatewayVpcAttachment]
    def __init__(self, vpc_id: _Optional[str] = ..., vpc_name: _Optional[str] = ..., vpc_primary_cidr_block: _Optional[str] = ..., vpc_dhcp_options_id: _Optional[str] = ..., vpc_owner_id: _Optional[str] = ..., instance_tenancy: _Optional[str] = ..., vpc_associated_ipv6_id: _Optional[str] = ..., vpc_ipv6_cidr_block: _Optional[str] = ..., network_border_group: _Optional[str] = ..., ipv6_pool: _Optional[str] = ..., vpc_is_default: bool = ..., tag_specification: _Optional[_Iterable[_Union[TagSpecification, _Mapping]]] = ..., subnet_vec: _Optional[_Iterable[_Union[SubnetInfo, _Mapping]]] = ..., route_table_vec: _Optional[_Iterable[_Union[RouteTableInfo, _Mapping]]] = ..., internet_gateway_vec: _Optional[_Iterable[_Union[InternetGateway, _Mapping]]] = ..., carrier_gateway_vec: _Optional[_Iterable[_Union[CarrierGateway, _Mapping]]] = ..., nat_gateway_vec: _Optional[_Iterable[_Union[NatGateway, _Mapping]]] = ..., eigw_vec: _Optional[_Iterable[_Union[EgressOnlyInternetGateway, _Mapping]]] = ..., vpn_gateway_vec: _Optional[_Iterable[_Union[VpnGateway, _Mapping]]] = ..., network_acl_vec: _Optional[_Iterable[_Union[NetworkAcl, _Mapping]]] = ..., vpc_endpoint_vec: _Optional[_Iterable[_Union[VpcEndpoint, _Mapping]]] = ..., vpc_hostname: bool = ..., vpc_resolution: bool = ..., dhcp_option_vec: _Optional[_Iterable[_Union[DhcpOption, _Mapping]]] = ..., flow_logs_info: _Optional[_Iterable[_Union[FlowLogs, _Mapping]]] = ..., transit_gateway_info: _Optional[_Iterable[_Union[TransitGateway, _Mapping]]] = ..., tgw_route_table_info: _Optional[_Iterable[_Union[TransitGatewayRouteTable, _Mapping]]] = ..., tgw_multicast_domain_info: _Optional[_Iterable[_Union[TransitGatewayMulticastDomain, _Mapping]]] = ..., tgw_vpc_attachment_info: _Optional[_Iterable[_Union[TransitGatewayVpcAttachment, _Mapping]]] = ...) -> None: ...
