# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/axon.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15nexus/base/axon.proto\x12\x13\x63ohesity.nexus.base\"v\n\tAxonError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0f\n\x07summary\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x04 \x01(\t\x12\x12\n\ndebug_info\x18\x05 \x01(\x0c\x12\x12\n\nrequest_id\x18\x06 \x01(\t\"\xe7\x0b\n\x07Network\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\r\n\x05ports\x18\x05 \x03(\t\x12\x12\n\nsubnet_ids\x18\x06 \x03(\t\x12\x11\n\ttenant_id\x18\x07 \x01(\t\x12/\n\x04type\x18\t \x01(\x0e\x32!.cohesity.nexus.base.Network.Type\x12\x0b\n\x03mtu\x18\n \x01(\x05\x12<\n\x08metadata\x18\x0b \x03(\x0b\x32*.cohesity.nexus.base.Network.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\x0c \x01(\x08\x12\x37\n\x08provider\x18\r \x01(\x0b\x32%.cohesity.nexus.base.Network.Provider\x12\x1f\n\x17no_l3_host_connectivity\x18\x0e \x01(\x08\x12\x38\n\x11\x64\x65\x66\x61ult_ipam_type\x18\x0f \x01(\x0e\x32\x1d.cohesity.nexus.base.IPAMType\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcb\x01 \x01(\x08\x12\x1a\n\x11is_custom_mtu_set\x18\xcc\x01 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xc4\x03\n\x08Provider\x12?\n\x08segments\x18\x01 \x03(\x0b\x32-.cohesity.nexus.base.Network.Provider.Segment\x1a\xf6\x02\n\x07Segment\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.cohesity.nexus.base.Network.Provider.Segment.Type\x12G\n\x08sub_type\x18\x02 \x01(\x0e\x32\x35.cohesity.nexus.base.Network.Provider.Segment.SubType\x12\x17\n\x0fsegmentation_id\x18\x04 \x01(\x05\x12\x17\n\x0finterface_group\x18\x05 \x01(\t\"N\n\x04Type\x12\x08\n\x04VLAN\x10\x00\x12\x08\n\x04\x46LAT\x10\x01\x12\x07\n\x03GRE\x10\x02\x12\t\n\x05VXLAN\x10\x03\x12\t\n\x05NVGRE\x10\x04\x12\x07\n\x03STT\x10\x05\x12\n\n\x06GENEVE\x10\x06\"X\n\x07SubType\x12\x0f\n\x0bVLAN_NORMAL\x10\x00\x12\x1c\n\x18VLAN_BIFROST_NODE_FACING\x10\x01\x12\x1e\n\x1aVLAN_BIFROST_TENANT_FACING\x10\x02J\x04\x08\x03\x10\x04\"\"\n\x04Type\x12\x0c\n\x08INTERNAL\x10\x00\x12\x0c\n\x08PROVIDER\x10\x01\"\xd0\x02\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x12\n\x0ePORT_ATTACHING\x10\x04\x12\x14\n\x10SUBNET_ATTACHING\x10\x08\x12\x12\n\x0ePORT_DETACHING\x10\x10\x12\x14\n\x10SUBNET_DETACHING\x10 \x12\x11\n\rUPDATING_NAME\x10@\x12\x11\n\x0cUPDATING_MTU\x10\x80\x01\x12\x17\n\x12UPDATING_TENANT_ID\x10\x80\x02\x12\x16\n\x11UPDATING_METADATA\x10\x80\x04\x12\x15\n\x10UPDATING_SEGMENT\x10\x80\x08\x12\x16\n\x11UPDATING_IPAMTYPE\x10\x80\x10\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\x8e\x08\n\x06Subnet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x39\n\nip_version\x18\x05 \x01(\x0e\x32%.cohesity.nexus.base.Subnet.IPVersion\x12\x0c\n\x04\x63idr\x18\x06 \x01(\t\x12\n\n\x02gw\x18\x07 \x01(\t\x12\x12\n\nnetwork_id\x18\x08 \x01(\t\x12\x14\n\x0c\x64hcp_enabled\x18\t \x01(\x08\x12\x34\n\tdhcp_conf\x18\n \x01(\x0b\x32!.cohesity.nexus.base.DhcpSrvrConf\x12\x1c\n\x14\x61llow_service_access\x18\x0b \x01(\x08\x12\x11\n\ttenant_id\x18\r \x01(\t\x12\x19\n\x11\x65xclude_ip_ranges\x18\x0e \x03(\t\x12;\n\x08metadata\x18\x10 \x03(\x0b\x32).cohesity.nexus.base.Subnet.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\x11 \x01(\x08\x12\x18\n\x10static_ip_ranges\x18\x12 \x03(\t\x12G\n\x15service_access_config\x18\x13 \x01(\x0b\x32(.cohesity.nexus.base.ServiceAccessConfig\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x1b\n\x12ovn_dhcp_config_id\x18\xc9\x01 \x01(\t\x12\x10\n\x07version\x18\xca\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xcb\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcc\x01 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\tIPVersion\x12\x06\n\x02V4\x10\x00\x12\x06\n\x02V6\x10\x01\"\xea\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x13\n\x0fUPDATING_SUBNET\x10\x04\x12\x11\n\rUPDATING_DHCP\x10\x08\x12\x1b\n\x17UPDATING_SERVICE_ACCESS\x10\x10\x12\x16\n\x12UPDATING_TENANT_ID\x10 \x12\x15\n\x11UPDATING_METADATA\x10@\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"p\n\x13ServiceAccessConfig\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.cohesity.nexus.base.ServiceAccessConfig.Type\"\x1c\n\x04Type\x12\x07\n\x03\x41PP\x10\x00\x12\x0b\n\x07\x42IFROST\x10\x01\"\x95\x03\n\x0c\x44hcpSrvrConf\x12\x13\n\x0bmac_address\x18\x01 \x01(\t\x12\x11\n\tipaddress\x18\x02 \x01(\t\x12\x13\n\x0bsubnet_cidr\x18\x03 \x01(\t\x12\x12\n\ndns_domain\x18\x04 \x01(\t\x12\x17\n\x0f\x64ns_nameservers\x18\x05 \x03(\t\x12\x19\n\x11\x64ns_searchdomains\x18\x06 \x03(\t\x12J\n\rextra_options\x18\x07 \x03(\x0b\x32\x33.cohesity.nexus.base.DhcpSrvrConf.ExtraOptionsEntry\x12\x0b\n\x03mtu\x18\x08 \x01(\x05\x12\x41\n\x08metadata\x18\x10 \x03(\x0b\x32/.cohesity.nexus.base.DhcpSrvrConf.MetadataEntry\x1a\x33\n\x11\x45xtraOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x85\r\n\x04Port\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x12\n\nnetwork_id\x18\x05 \x01(\t\x12,\n\tpeer_port\x18\x06 \x01(\x0b\x32\x19.cohesity.nexus.base.Port\x12\x13\n\x0bmac_address\x18\x08 \x01(\t\x12K\n\x12\x64hcp_extra_options\x18\t \x03(\x0b\x32/.cohesity.nexus.base.Port.DhcpExtraOptionsEntry\x12,\n\x04type\x18\n \x01(\x0e\x32\x1e.cohesity.nexus.base.Port.Type\x12\x1d\n\x15port_security_enabled\x18\x0b \x01(\x08\x12\x15\n\rport_security\x18\x0c \x03(\t\x12\x17\n\x0fport_profile_id\x18\r \x01(\t\x12\x12\n\nip_address\x18\x0e \x01(\t\x12\x11\n\ttenant_id\x18\x0f \x01(\t\x12\x19\n\x11provider_net_name\x18\x10 \x01(\t\x12\x39\n\x08metadata\x18\x12 \x03(\x0b\x32\'.cohesity.nexus.base.Port.MetadataEntry\x12\x13\n\x0bsubnet_cidr\x18\x13 \x01(\t\x12\x19\n\x11\x61llow_all_tenants\x18\x14 \x01(\x08\x12\x14\n\x0c\x62ind_node_id\x18\x15 \x01(\x03\x12\x45\n\x0e\x62ind_node_type\x18\x16 \x01(\x0e\x32-.cohesity.nexus.base.Port.PortNodeBindingType\x12\x11\n\trouter_id\x18\x17 \x01(\t\x12\x13\n\x0bport_groups\x18\x18 \x03(\t\x12\x1c\n\x14router_attachment_id\x18\x19 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x1c \x01(\t\x12\x30\n\tipam_type\x18\x1d \x01(\x0e\x32\x1d.cohesity.nexus.base.IPAMType\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcb\x01 \x01(\x08\x12\x17\n\x0eis_dynamic_mac\x18\xcc\x01 \x01(\x08\x12\x16\n\ris_dynamic_ip\x18\xcd\x01 \x01(\x08\x1a\x37\n\x15\x44hcpExtraOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"j\n\x04Type\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tLOCALPORT\x10\x01\x12\x0c\n\x08LOCALNET\x10\x02\x12\x0c\n\x08L2GWPORT\x10\x03\x12\n\n\x06ROUTER\x10\x04\x12\x0c\n\x08VTEPPORT\x10\x05\x12\x11\n\rSERVICEACCESS\x10\x64\"M\n\x13PortNodeBindingType\x12\x0b\n\x07UNBOUND\x10\x00\x12\x0c\n\x08INTERNAL\x10\x01\x12\x07\n\x03VIF\x10\x02\x12\x12\n\x0eSERVICE_ACCESS\x10\x03\"\xfc\x02\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x13\n\x0fUPDATING_STATUS\x10\x04\x12\x18\n\x14UPDATING_MAC_ADDRESS\x10\x08\x12\x1f\n\x1bUPDATING_DHCP_EXTRA_OPTIONS\x10\x10\x12\x1a\n\x16UPDATING_PORT_SECURITY\x10 \x12\x19\n\x15UPDATING_PORT_PROFILE\x10@\x12\x18\n\x13UPDATING_NETWORK_ID\x10\x80\x01\x12\x1e\n\x19UPDATING_PROVIDER_NETWORK\x10\x80\x02\x12\x16\n\x11UPDATING_METADATA\x10\x80\x04\x12\x17\n\x12UPDATING_TENANT_ID\x10\x80\x08\x12\x12\n\rUPDATING_NAME\x10\x80\x10\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\xb0\x0b\n\x11SecurityGroupRule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\x12\x10\n\x08port_min\x18\x06 \x01(\x03\x12\x10\n\x08port_max\x18\x07 \x01(\x03\x12\x0f\n\x07ip_cidr\x18\x08 \x01(\t\x12>\n\x05proto\x18\t \x01(\x0e\x32/.cohesity.nexus.base.SecurityGroupRule.Protocol\x12\x43\n\tdirection\x18\n \x01(\x0e\x32\x30.cohesity.nexus.base.SecurityGroupRule.Direction\x12\x11\n\ttenant_id\x18\x0c \x01(\t\x12<\n\x04type\x18\r \x01(\x0e\x32..cohesity.nexus.base.SecurityGroupRule.SgrType\x12\x46\n\x08metadata\x18\x0e \x03(\x0b\x32\x34.cohesity.nexus.base.SecurityGroupRule.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\x0f \x01(\x08\x12\x16\n\x0eip_address_set\x18\x10 \x03(\t\x12\x16\n\x0e\x63luster_ip_set\x18\x11 \x01(\x08\x12\x10\n\x08priority\x18\x12 \x01(\x05\x12@\n\x06\x61\x63tion\x18\x13 \x01(\x0e\x32\x30.cohesity.nexus.base.SecurityGroupRule.ACLAction\x12\x17\n\x0fport_group_name\x18\x14 \x01(\t\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcb\x01 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x08Protocol\x12\x07\n\x03\x41NY\x10\x00\x12\x07\n\x03TCP\x10\x06\x12\x07\n\x03UDP\x10\x11\x12\x08\n\x04ICMP\x10\x01\x12\n\n\x06ICMPV6\x10:\"$\n\tDirection\x12\x0b\n\x07INGRESS\x10\x00\x12\n\n\x06\x45GRESS\x10\x01\"0\n\x07SgrType\x12\n\n\x06NORMAL\x10\x00\x12\x19\n\x15INTERNAL_DEFAULT_DENY\x10\x01\"?\n\tACLAction\x12\t\n\x05\x41LLOW\x10\x00\x12\x11\n\rALLOW_RELATED\x10\x01\x12\x08\n\x04\x44ROP\x10\x02\x12\n\n\x06REJECT\x10\x03\"\xfa\x02\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x15\n\x11UPDATING_PORT_MIN\x10\x04\x12\x15\n\x11UPDATING_PORT_MAX\x10\x08\x12\x11\n\rUPDATING_CIDR\x10\x10\x12\x15\n\x11UPDATING_PROTOCOL\x10 \x12\x16\n\x12UPDATING_DIRECTION\x10@\x12\x14\n\x0fUPDATING_IP_SET\x10\x80\x01\x12\x1c\n\x17UPDATING_CLUSTER_IP_SET\x10\x80\x02\x12\x18\n\x13UPDATING_ACL_ACTION\x10\x80\x04\x12\x17\n\x12UPDATING_TENANT_ID\x10\x80\x08\x12\x12\n\rUPDATING_NAME\x10\x80\x10\x12\x17\n\x11UPDATING_METADATA\x10\x80\x80@\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\xc8\x04\n\rSecurityGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x11\n\ttenant_id\x18\x05 \x01(\t\x12\r\n\x05rules\x18\x06 \x03(\t\x12\x42\n\x08metadata\x18\x08 \x03(\x0b\x32\x30.cohesity.nexus.base.SecurityGroup.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\t \x01(\x08\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcb\x01 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x1a\n\x16UPDATING_SECURITY_RULE\x10\x04\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\xd7\x05\n\x0bPortProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x0f\n\x07vlan_id\x18\x05 \x01(\x05\x12\x11\n\tsecgrp_id\x18\x06 \x01(\t\x12\x11\n\ttenant_id\x18\x08 \x01(\t\x12\r\n\x05ports\x18\t \x03(\t\x12@\n\x08metadata\x18\n \x03(\x0b\x32..cohesity.nexus.base.PortProfile.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\x0b \x01(\x08\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x12\x1c\n\x13try_update_recovery\x18\xcb\x01 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x81\x02\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x11\n\rUPDATING_VLAN\x10\x04\x12\x1b\n\x17UPDATING_SECURITY_GROUP\x10\x08\x12\x16\n\x12UPDATING_PORT_LIST\x10\x10\x12\x16\n\x12UPDATING_TENANT_ID\x10 \x12\x11\n\rUPDATING_NAME\x10@\x12\x16\n\x11UPDATING_METADATA\x10\x80\x01\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\xfc\x05\n\x06Router\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12:\n\x0b\x61ttachments\x18\x05 \x03(\x0b\x32%.cohesity.nexus.base.RouterAttachment\x12>\n\ndeny_rules\x18\x07 \x03(\x0b\x32*.cohesity.nexus.base.Router.DenyRulesEntry\x12\x12\n\ngw_port_id\x18\x08 \x01(\t\x12;\n\x08metadata\x18\t \x03(\x0b\x32).cohesity.nexus.base.Router.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\n \x01(\x08\x12\x11\n\ttenant_id\x18\x0b \x01(\t\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x1a\x30\n\x0e\x44\x65nyRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbf\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x14\n\x10UPDATING_PORT_ID\x10\x04\x12\x1e\n\x1aUPDATING_ROUTER_ATTACHMENT\x10\x08\x12\x11\n\rUPDATING_NAME\x10\x10\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\xee\x02\n\x10RouterAttachment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x17\n\x0fnetwork_port_id\x18\x03 \x01(\t\x12\x17\n\x0fnetwork_address\x18\x04 \x01(\t\x12\x0b\n\x03mac\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\"\x8f\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x17\n\x13UPDATING_ATTACHMENT\x10\x04\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\"\x9d\x04\n\x0cLoadBalancer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x03 \x01(\t\x12\x19\n\x11updated_timestamp\x18\x04 \x01(\t\x12\x0b\n\x03vip\x18\x05 \x01(\t\x12\x13\n\x0bipaddresses\x18\x06 \x03(\t\x12\x41\n\x08metadata\x18\x08 \x03(\x0b\x32/.cohesity.nexus.base.LoadBalancer.MetadataEntry\x12\x19\n\x11\x61llow_all_tenants\x18\t \x01(\x08\x12\r\n\x05state\x18\x65 \x01(\x03\x12-\n\x05\x65rror\x18\x66 \x01(\x0b\x32\x1e.cohesity.nexus.base.AxonError\x12\x17\n\x0flast_request_id\x18g \x01(\t\x12\x10\n\x07version\x18\xc9\x01 \x01(\x03\x12\x19\n\x10\x66orce_set_reason\x18\xca\x01 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x10\n\x0cUPDATING_VIP\x10\x04\x12\x18\n\x14UPDATING_IPADDRESSES\x10\x08\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04*\xb9\x03\n\nStateRange\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x12\n\x0eUPDATING_START\x10\x04\x12\x11\n\x0cUPDATING_END\x10\x80\x10\x12\x14\n\rUPDATING_MASK\x10\xfc\x9f\xc0\x07\x12\x12\n\x0ePROGRESS_START\x10\x01\x12\x11\n\x0cPROGRESS_END\x10\x80\x10\x12\x14\n\rPROGRESS_MASK\x10\xff\x9f\xc0\x07\x12\x0c\n\x07\x43REATED\x10\x80 \x12\x0c\n\x07\x44\x45LETED\x10\x80@\x12\x15\n\x10\x43OMPLETION_START\x10\x80 \x12\x14\n\x0e\x43OMPLETION_END\x10\x80\x80 \x12\x15\n\x0f\x43OMPLETION_MASK\x10\x80\xe0?\x12\x1c\n\x16SPECIAL_UPDATING_START\x10\x80\x80@\x12\x1b\n\x14SPECIAL_UPDATING_END\x10\x80\x80\xc0\x07\x12\r\n\x05\x45RROR\x10\x80\x80\x80\x80\x04\x12\x19\n\x11\x43LEANING_ON_ERROR\x10\x80\x80\x80\x80\x02\x12\x14\n\rSPECIAL_START\x10\x80\x80\x80\x08\x12\x13\n\x0bSPECIAL_END\x10\x80\x80\x80\x80\x04\x12\x14\n\x0cSPECIAL_MASK\x10\x80\x80\x80\xf8\x07\x1a\x02\x10\x01*\x9e\x01\n\x08IPAMType\x12\r\n\tUNDEFINED\x10\x00\x12\x07\n\x03OVN\x10\x01\x12\n\n\x06\x41THENA\x10\x03\x12\x1a\n\x16\x42IFROST_NODEFACING_CNI\x10\x04\x12$\n BIFROST_NODEFACING_SERVICEACCESS\x10\x05\x12\x1c\n\x18\x42IFROST_TENANTFACING_CNI\x10\x06\x12\x08\n\x04TEST\x10\x07\"\x04\x08\x02\x10\x02\x42\x14Z\x12nexus/base/axon.pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.axon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022nexus/base/axon.pb'
  _globals['_STATERANGE']._loaded_options = None
  _globals['_STATERANGE']._serialized_options = b'\020\001'
  _globals['_NETWORK_METADATAENTRY']._loaded_options = None
  _globals['_NETWORK_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SUBNET_METADATAENTRY']._loaded_options = None
  _globals['_SUBNET_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_DHCPSRVRCONF_EXTRAOPTIONSENTRY']._loaded_options = None
  _globals['_DHCPSRVRCONF_EXTRAOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_DHCPSRVRCONF_METADATAENTRY']._loaded_options = None
  _globals['_DHCPSRVRCONF_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_PORT_DHCPEXTRAOPTIONSENTRY']._loaded_options = None
  _globals['_PORT_DHCPEXTRAOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_PORT_METADATAENTRY']._loaded_options = None
  _globals['_PORT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SECURITYGROUPRULE_METADATAENTRY']._loaded_options = None
  _globals['_SECURITYGROUPRULE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SECURITYGROUP_METADATAENTRY']._loaded_options = None
  _globals['_SECURITYGROUP_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_PORTPROFILE_METADATAENTRY']._loaded_options = None
  _globals['_PORTPROFILE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_ROUTER_DENYRULESENTRY']._loaded_options = None
  _globals['_ROUTER_DENYRULESENTRY']._serialized_options = b'8\001'
  _globals['_ROUTER_METADATAENTRY']._loaded_options = None
  _globals['_ROUTER_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_LOADBALANCER_METADATAENTRY']._loaded_options = None
  _globals['_LOADBALANCER_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_STATERANGE']._serialized_start=9372
  _globals['_STATERANGE']._serialized_end=9813
  _globals['_IPAMTYPE']._serialized_start=9816
  _globals['_IPAMTYPE']._serialized_end=9974
  _globals['_AXONERROR']._serialized_start=46
  _globals['_AXONERROR']._serialized_end=164
  _globals['_NETWORK']._serialized_start=167
  _globals['_NETWORK']._serialized_end=1678
  _globals['_NETWORK_METADATAENTRY']._serialized_start=801
  _globals['_NETWORK_METADATAENTRY']._serialized_end=848
  _globals['_NETWORK_PROVIDER']._serialized_start=851
  _globals['_NETWORK_PROVIDER']._serialized_end=1303
  _globals['_NETWORK_PROVIDER_SEGMENT']._serialized_start=929
  _globals['_NETWORK_PROVIDER_SEGMENT']._serialized_end=1303
  _globals['_NETWORK_PROVIDER_SEGMENT_TYPE']._serialized_start=1129
  _globals['_NETWORK_PROVIDER_SEGMENT_TYPE']._serialized_end=1207
  _globals['_NETWORK_PROVIDER_SEGMENT_SUBTYPE']._serialized_start=1209
  _globals['_NETWORK_PROVIDER_SEGMENT_SUBTYPE']._serialized_end=1297
  _globals['_NETWORK_TYPE']._serialized_start=1305
  _globals['_NETWORK_TYPE']._serialized_end=1339
  _globals['_NETWORK_STATE']._serialized_start=1342
  _globals['_NETWORK_STATE']._serialized_end=1678
  _globals['_SUBNET']._serialized_start=1681
  _globals['_SUBNET']._serialized_end=2719
  _globals['_SUBNET_METADATAENTRY']._serialized_start=801
  _globals['_SUBNET_METADATAENTRY']._serialized_end=848
  _globals['_SUBNET_IPVERSION']._serialized_start=2455
  _globals['_SUBNET_IPVERSION']._serialized_end=2482
  _globals['_SUBNET_STATE']._serialized_start=2485
  _globals['_SUBNET_STATE']._serialized_end=2719
  _globals['_SERVICEACCESSCONFIG']._serialized_start=2721
  _globals['_SERVICEACCESSCONFIG']._serialized_end=2833
  _globals['_SERVICEACCESSCONFIG_TYPE']._serialized_start=2805
  _globals['_SERVICEACCESSCONFIG_TYPE']._serialized_end=2833
  _globals['_DHCPSRVRCONF']._serialized_start=2836
  _globals['_DHCPSRVRCONF']._serialized_end=3241
  _globals['_DHCPSRVRCONF_EXTRAOPTIONSENTRY']._serialized_start=3141
  _globals['_DHCPSRVRCONF_EXTRAOPTIONSENTRY']._serialized_end=3192
  _globals['_DHCPSRVRCONF_METADATAENTRY']._serialized_start=801
  _globals['_DHCPSRVRCONF_METADATAENTRY']._serialized_end=848
  _globals['_PORT']._serialized_start=3244
  _globals['_PORT']._serialized_end=4913
  _globals['_PORT_DHCPEXTRAOPTIONSENTRY']._serialized_start=4239
  _globals['_PORT_DHCPEXTRAOPTIONSENTRY']._serialized_end=4294
  _globals['_PORT_METADATAENTRY']._serialized_start=801
  _globals['_PORT_METADATAENTRY']._serialized_end=848
  _globals['_PORT_TYPE']._serialized_start=4345
  _globals['_PORT_TYPE']._serialized_end=4451
  _globals['_PORT_PORTNODEBINDINGTYPE']._serialized_start=4453
  _globals['_PORT_PORTNODEBINDINGTYPE']._serialized_end=4530
  _globals['_PORT_STATE']._serialized_start=4533
  _globals['_PORT_STATE']._serialized_end=4913
  _globals['_SECURITYGROUPRULE']._serialized_start=4916
  _globals['_SECURITYGROUPRULE']._serialized_end=6372
  _globals['_SECURITYGROUPRULE_METADATAENTRY']._serialized_start=801
  _globals['_SECURITYGROUPRULE_METADATAENTRY']._serialized_end=848
  _globals['_SECURITYGROUPRULE_PROTOCOL']._serialized_start=5779
  _globals['_SECURITYGROUPRULE_PROTOCOL']._serialized_end=5838
  _globals['_SECURITYGROUPRULE_DIRECTION']._serialized_start=5840
  _globals['_SECURITYGROUPRULE_DIRECTION']._serialized_end=5876
  _globals['_SECURITYGROUPRULE_SGRTYPE']._serialized_start=5878
  _globals['_SECURITYGROUPRULE_SGRTYPE']._serialized_end=5926
  _globals['_SECURITYGROUPRULE_ACLACTION']._serialized_start=5928
  _globals['_SECURITYGROUPRULE_ACLACTION']._serialized_end=5991
  _globals['_SECURITYGROUPRULE_STATE']._serialized_start=5994
  _globals['_SECURITYGROUPRULE_STATE']._serialized_end=6372
  _globals['_SECURITYGROUP']._serialized_start=6375
  _globals['_SECURITYGROUP']._serialized_end=6959
  _globals['_SECURITYGROUP_METADATAENTRY']._serialized_start=801
  _globals['_SECURITYGROUP_METADATAENTRY']._serialized_end=848
  _globals['_SECURITYGROUP_STATE']._serialized_start=6813
  _globals['_SECURITYGROUP_STATE']._serialized_end=6959
  _globals['_PORTPROFILE']._serialized_start=6962
  _globals['_PORTPROFILE']._serialized_end=7689
  _globals['_PORTPROFILE_METADATAENTRY']._serialized_start=801
  _globals['_PORTPROFILE_METADATAENTRY']._serialized_end=848
  _globals['_PORTPROFILE_STATE']._serialized_start=7432
  _globals['_PORTPROFILE_STATE']._serialized_end=7689
  _globals['_ROUTER']._serialized_start=7692
  _globals['_ROUTER']._serialized_end=8456
  _globals['_ROUTER_DENYRULESENTRY']._serialized_start=8165
  _globals['_ROUTER_DENYRULESENTRY']._serialized_end=8213
  _globals['_ROUTER_METADATAENTRY']._serialized_start=801
  _globals['_ROUTER_METADATAENTRY']._serialized_end=848
  _globals['_ROUTER_STATE']._serialized_start=8265
  _globals['_ROUTER_STATE']._serialized_end=8456
  _globals['_ROUTERATTACHMENT']._serialized_start=8459
  _globals['_ROUTERATTACHMENT']._serialized_end=8825
  _globals['_ROUTERATTACHMENT_STATE']._serialized_start=8682
  _globals['_ROUTERATTACHMENT_STATE']._serialized_end=8825
  _globals['_LOADBALANCER']._serialized_start=8828
  _globals['_LOADBALANCER']._serialized_end=9369
  _globals['_LOADBALANCER_METADATAENTRY']._serialized_start=801
  _globals['_LOADBALANCER_METADATAENTRY']._serialized_end=848
  _globals['_LOADBALANCER_STATE']._serialized_start=9234
  _globals['_LOADBALANCER_STATE']._serialized_end=9369
# @@protoc_insertion_point(module_scope)