# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/nexus_wal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from nexus.base import nexus_hmac_key_config_pb2 as nexus_dot_base_dot_nexus__hmac__key__config__pb2
from nexus.base import services_gflags_pb2 as nexus_dot_base_dot_services__gflags__pb2
from open_util.base import aes_encryptor_pb2 as open__util_dot_base_dot_aes__encryptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1anexus/base/nexus_wal.proto\x12\x0e\x63ohesity.nexus\x1a\x1c\x63onfigs/cluster_config.proto\x1a&nexus/base/nexus_hmac_key_config.proto\x1a nexus/base/services_gflags.proto\x1a\"open_util/base/aes_encryptor.proto\"\'\n\x08NodeInfo\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0f\n\x07ipmi_ip\x18\x02 \x02(\t\"_\n\x10NodeIpPreference\x12\x19\n\x11node_ip_reachable\x18\x01 \x01(\x08\x12\x17\n\x0fipv4_link_local\x18\x02 \x01(\t\x12\x17\n\x0fipv6_link_local\x18\x03 \x01(\t\"B\n\x08\x44nsGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bnode_ip_vec\x18\x02 \x03(\t\x12\x13\n\x0b\x64ns_servers\x18\x03 \x03(\t\"\x8e\x01\n\x12\x43lusterSubnetGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bnode_ip_vec\x18\x02 \x03(\t\x12\x11\n\tsubnet_ip\x18\x03 \x01(\t\x12\x17\n\x0fsubnet_cidr_len\x18\x04 \x01(\x05\x12\x18\n\x10subnet_ipv4_mask\x18\x05 \x01(\t\x12\x0f\n\x07gateway\x18\x06 \x01(\t\"E\n\x12\x42ringupStatusEvent\x12\x18\n\x10time_stamp_usecs\x18\x01 \x02(\x03\x12\x15\n\rbringup_event\x18\x02 \x02(\t\"\xcd\x15\n\x17\x43lusterBringupWalRecord\x12\x14\n\x0c\x63luster_name\x18\x01 \x02(\t\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x03 \x02(\x03\x12\x13\n\x0bntp_servers\x18\x04 \x03(\t\x12\x13\n\x0b\x64ns_servers\x18\x05 \x03(\t\x12\x14\n\x0c\x64omain_names\x18\x06 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x07 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\t \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\n \x02(\t\x12\x14\n\x0cipmi_gateway\x18\x0b \x01(\t\x12\x16\n\x0eipmi_subnet_ip\x18\x0c \x01(\t\x12\x1c\n\x14ipmi_subnet_cidr_len\x18\r \x01(\x05\x12\x1d\n\x15ipmi_subnet_ipv4_mask\x18\x0e \x01(\t\x12\x15\n\ripmi_username\x18\x0f \x01(\t\x12\x15\n\ripmi_password\x18\x10 \x01(\t\x12;\n\x08node_vec\x18\x11 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\x12\x41\n\x0b\x63hassis_vec\x18\x12 \x03(\x0b\x32,.cohesity.configs.ClusterConfigProto.Chassis\x12 \n\x18\x63luster_software_version\x18\x13 \x02(\t\x12\x16\n\x0erotationPeriod\x18\x14 \x01(\x05\x12\x31\n\x08req_type\x18\x15 \x02(\x0e\x32\x1f.cohesity.nexus.RestRequestType\x12\"\n\x1a\x65nable_software_encryption\x18\x16 \x02(\x08\x12 \n\x14\x63luster_partition_id\x18\x17 \x01(\x03:\x02-1\x12\x13\n\x0b\x61uto_update\x18\x18 \x02(\x08\x12(\n\x19ignore_sw_incompatibility\x18\x19 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x15software_package_urls\x18\x1a \x03(\t\x12 \n\x11\x63lean_logs_needed\x18\x1b \x02(\x08:\x05\x66\x61lse\x12\x1e\n\x16last_updated_time_secs\x18\x1c \x02(\x03\x12\x1f\n\x14percentage_completed\x18\x1d \x01(\x05:\x01\x30\x12/\n\x11\x63urrent_operation\x18\x1e \x01(\t:\x14Nothing in progress.\x12\x17\n\x0ctime_started\x18\x1f \x01(\x03:\x01\x30\x12\x1e\n\x13time_estimated_secs\x18  \x01(\x03:\x01\x30\x12\x1e\n\x13time_remaining_secs\x18! \x01(\x03:\x01\x30\x12-\n\x1ehardware_encryption_capability\x18\" \x01(\x08:\x05\x66\x61lse\x12\x46\n\x0c\x62onding_mode\x18# \x01(\x0e\x32\x30.cohesity.configs.ClusterConfigProto.BondingMode\x12\x1f\n\x17\x63ompatibility_proto_vec\x18$ \x03(\t\x12\x19\n\x11oldscribe_enabled\x18% \x01(\x08\x12\x0b\n\x03mtu\x18& \x01(\x05\x12\x16\n\x0esender_node_ip\x18\' \x01(\t\x12@\n\x16node_ip_preference_vec\x18( \x03(\x0b\x32 .cohesity.nexus.NodeIpPreference\x12\x1c\n\x14rotation_period_secs\x18) \x01(\x03\x12\x18\n\x10\x65nable_fips_mode\x18* \x01(\x08\x12\x13\n\x0bin_progress\x18+ \x01(\x08\x12\x11\n\tlogin_url\x18, \x01(\t\x12\x15\n\rerror_message\x18- \x01(\t\x12=\n\x11\x62ringup_event_vec\x18. \x03(\x0b\x32\".cohesity.nexus.BringupStatusEvent\x12\x16\n\x0ewarnings_found\x18/ \x01(\x08\x12\x33\n\rbringup_state\x18\x30 \x01(\x0e\x32\x1c.cohesity.nexus.BringupState\x12\x31\n\x0bpanic_state\x18\x31 \x01(\x0e\x32\x1c.cohesity.nexus.BringupState\x12\x13\n\x0bpanic_count\x18\x32 \x01(\x05\x12\x45\n\x13ServicesGflagsProto\x18\x33 \x01(\x0b\x32(.cohesity.nexus.base.ServicesGflagsProto\x12S\n\x13proxy_server_config\x18\x34 \x01(\x0b\x32\x36.cohesity.configs.ClusterConfigProto.ProxyServerConfig\x12\x0f\n\x07vip_vec\x18\x35 \x03(\t\x12#\n\x1b\x63luster_partition_host_name\x18\x36 \x01(\t\x12*\n\x1fmetadata_fault_tolerance_factor\x18\x37 \x01(\x05:\x01\x31\x12 \n\x11is_cluster_expand\x18\x38 \x01(\x08:\x05\x66\x61lse\x12Q\n\rip_preference\x18\x39 \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12\x0f\n\x07rack_id\x18; \x01(\x03\x12U\n\x18ntp_server_auth_keys_vec\x18< \x03(\x0b\x32\x33.cohesity.configs.ClusterConfigProto.NTPAuthKeyInfo\x12/\n\rdns_group_vec\x18= \x03(\x0b\x32\x18.cohesity.nexus.DnsGroup\x12\x44\n\x18\x63luster_subnet_group_vec\x18> \x03(\x0b\x32\".cohesity.nexus.ClusterSubnetGroup\x12\"\n\x1antp_authentication_enabled\x18? \x01(\x08\x12,\n$allow_cluster_destroy_on_api_request\x18@ \x01(\x08\x12\x42\n\x17nexus_hmac_config_proto\x18\x41 \x01(\x0b\x32!.cohesity.nexus.NexusHmacKeyProto\x12\"\n\x1a\x65nable_hardware_encryption\x18\x42 \x01(\x08\x12\x1f\n\x17\x65nable_kernel_fips_mode\x18\x43 \x01(\x08\x12%\n\x1dservice_identity_trust_domain\x18\x44 \x01(\t\x12*\n\"service_identity_trust_domain_mode\x18\x45 \x01(\x05\x12\x14\n\x0coperation_id\x18\x46 \x01(\t\x12G\n\x12\x63luster_subnet_vec\x18G \x03(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\x12\x37\n\x13\x61\x65s_encryption_mode\x18H \x01(\x0e\x32\x1a.cohesity.AESEncryptorMode\x12\x17\n\x0fgenerate_rootca\x18I \x01(\x08J\x04\x08:\x10;\"\xfb\x07\n\x1eVirtualRoboClusterCreateRecord\x12\x14\n\x0c\x63luster_name\x18\x01 \x02(\t\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x03 \x02(\x03\x12\x16\n\x0entp_server_vec\x18\x04 \x03(\t\x12\x16\n\x0e\x64ns_server_vec\x18\x05 \x03(\t\x12\x17\n\x0f\x64omain_name_vec\x18\x06 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x07 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\t \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\n \x02(\t\x12\x0f\n\x07node_ip\x18\x0b \x02(\t\x12\x1c\n\x14rotation_period_secs\x18\x0c \x01(\x03\x12\"\n\x1a\x65nable_software_encryption\x18\r \x02(\x08\x12\x18\n\x10\x65nable_fips_mode\x18\x0e \x01(\x08\x12\x0b\n\x03mtu\x18\x0f \x01(\x05\x12\x45\n\x13ServicesGflagsProto\x18\x10 \x01(\x0b\x32(.cohesity.nexus.base.ServicesGflagsProto\x12S\n\x13proxy_server_config\x18\x11 \x01(\x0b\x32\x36.cohesity.configs.ClusterConfigProto.ProxyServerConfig\x12\x10\n\x08hostname\x18\x12 \x01(\t\x12Q\n\rip_preference\x18\x13 \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12U\n\x18ntp_server_auth_keys_vec\x18\x15 \x03(\x0b\x32\x33.cohesity.configs.ClusterConfigProto.NTPAuthKeyInfo\x12\"\n\x1antp_authentication_enabled\x18\x16 \x01(\x08\x12%\n\x1dservice_identity_trust_domain\x18\x17 \x01(\t\x12*\n\"service_identity_trust_domain_mode\x18\x18 \x01(\x05\x12G\n\x12\x63luster_subnet_vec\x18\x19 \x03(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\x12\x37\n\x13\x61\x65s_encryption_mode\x18\x1a \x01(\x0e\x32\x1a.cohesity.AESEncryptorModeJ\x04\x08\x14\x10\x15\"\x9c\x06\n\x18\x43loudClusterCreateRecord\x12\x19\n\x11other_node_ip_vec\x18\x01 \x03(\t\x12\x14\n\x0c\x63luster_name\x18\x02 \x01(\t\x12\x1e\n\x16last_updated_time_secs\x18\x03 \x01(\x03\x12\x16\n\x0entp_server_vec\x18\x04 \x03(\t\x12\x16\n\x0e\x64ns_server_vec\x18\x05 \x03(\t\x12\x17\n\x0f\x64omain_name_vec\x18\x06 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x07 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\t \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\n \x02(\t\x12\x12\n\ncluster_id\x18\x0b \x01(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x0c \x01(\x03\x12\x1c\n\x14rotation_period_secs\x18\r \x01(\x03\x12\"\n\x1a\x65nable_software_encryption\x18\x0e \x02(\x08\x12\x16\n\x0esender_node_ip\x18\x0f \x01(\t\x12 \n\x18metadata_fault_tolerance\x18\x10 \x01(\x05\x12\"\n\x1a\x63luster_partition_hostname\x18\x11 \x01(\t\x12Q\n\rip_preference\x18\x12 \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12\x46\n\x0c\x63luster_size\x18\x13 \x01(\x0e\x32\x30.cohesity.configs.ClusterConfigProto.ClusterSize\x12G\n\x12\x63luster_subnet_vec\x18\x14 \x03(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\x12\x37\n\x13\x61\x65s_encryption_mode\x18\x15 \x01(\x0e\x32\x1a.cohesity.AESEncryptorMode\"\xff\x02\n\x1a\x43loudClusterAddNodesRecord\x12\x13\n\x0bnode_ip_vec\x18\x01 \x03(\t\x12\x1e\n\x16last_updated_time_secs\x18\x02 \x01(\x03\x12\x1c\n\x14\x63luster_partition_id\x18\x03 \x01(\x03\x12\x16\n\x0esender_node_ip\x18\x04 \x01(\t\x12 \n\x18metadata_fault_tolerance\x18\x05 \x01(\x05\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\x06 \x02(\x05\x12Q\n\rip_preference\x18\x07 \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x01(\t\x12\x17\n\x0f\x63luster_gateway\x18\t \x01(\t\x12\x16\n\x0e\x64ns_server_vec\x18\n \x03(\t\x12\x14\n\x0coperation_id\x18\x0b \x01(\t\"\x9c\x03\n\x1a\x43loudNodeJoinClusterRecord\x12\x1e\n\x16last_updated_time_secs\x18\x01 \x01(\x03\x12\x12\n\ncluster_id\x18\x02 \x01(\x03\x12\x16\n\x0eincarnation_id\x18\x03 \x01(\x03\x12\x1c\n\x14\x63luster_partition_id\x18\x04 \x01(\x03\x12\x16\n\x0esender_node_ip\x18\x05 \x01(\t\x12\x19\n\x11num_joining_nodes\x18\x06 \x01(\x05\x12 \n\x18metadata_fault_tolerance\x18\x07 \x01(\x05\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\x08 \x02(\x05\x12\"\n\x18\x63luster_software_version\x18\t \x01(\t:\x00\x12\x1d\n\x15software_package_urls\x18\n \x03(\t\x12\x0f\n\x07node_ip\x18\x0b \x01(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x0c \x01(\t\x12\x17\n\x0f\x63luster_gateway\x18\r \x01(\t\x12\x16\n\x0e\x64ns_server_vec\x18\x0e \x03(\t\"\xd2\x02\n\x14\x43lusterDestroyRecord\x12\x39\n\x05state\x18\x01 \x02(\x0e\x32*.cohesity.nexus.ClusterDestroyRecord.State\x12\x19\n\x11other_node_ip_vec\x18\x02 \x03(\t\x12\"\n\x1ato_cleanup_disk_mount_path\x18\x03 \x01(\t\x12#\n\x1bto_cleanup_disk_device_path\x18\x04 \x01(\t\x12\x1e\n\x16last_updated_time_secs\x18\x05 \x01(\x03\x12\x12\n\ncluster_id\x18\x06 \x01(\x03\"g\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x12\n\x0ekToRemoveNodes\x10\x01\x12\x15\n\x11kToRemoveJsonFile\x10\x02\x12\x11\n\rkToRemoveDirs\x10\x03\x12\x13\n\x0fkToCleanupDisks\x10\x04\"O\n\x17\x43lusterRemoveNodeRecord\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12\x0f\n\x07node_ip\x18\x02 \x02(\t\x12\x12\n\ncluster_id\x18\x03 \x02(\x03\"\x94\x02\n\x18NodeDisjoinClusterRecord\x12=\n\x05state\x18\x01 \x02(\x0e\x32..cohesity.nexus.NodeDisjoinClusterRecord.State\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\"\n\x1ato_cleanup_disk_mount_path\x18\x03 \x01(\t\x12#\n\x1bto_cleanup_disk_device_path\x18\x04 \x01(\t\x12\x1e\n\x16last_updated_time_secs\x18\x05 \x01(\x03\"<\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x11\n\rkToRemoveDirs\x10\x01\x12\x13\n\x0fkToCleanupDisks\x10\x02\"\x8b\x03\n\x11NodeUpgradeRecord\x12\x36\n\x05state\x18\x01 \x02(\x0e\x32\'.cohesity.nexus.NodeUpgradeRecord.State\x12%\n\x1dnode_current_software_version\x18\x02 \x02(\t\x12$\n\x1cnode_target_software_version\x18\x03 \x02(\t\x12\x1e\n\x16last_updated_time_secs\x18\x04 \x01(\x03\x12\x1b\n\x13node_ids_to_upgrade\x18\x06 \x03(\x03\x12\x14\n\x0cupgrade_self\x18\x07 \x01(\x08\x12\x1e\n\x16upgrade_all_free_nodes\x18\x08 \x01(\x08\x12\x1f\n\x17ignoreSwIncompatibility\x18\t \x01(\x08\"W\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x15\n\x11kPackageInstalled\x10\x01\x12\x17\n\x13kToRemoveOldPackage\x10\x02\x12\x11\n\rkToRebootNode\x10\x03J\x04\x08\x05\x10\x06\"\xba\x02\n\x14\x43lusterUpgradeRecord\x12\x39\n\x05state\x18\x01 \x02(\x0e\x32*.cohesity.nexus.ClusterUpgradeRecord.State\x12\x1e\n\x16last_updated_time_secs\x18\x02 \x01(\x03\"\xc0\x01\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x19\n\x15kAcquireUpgradeTicket\x10\x01\x12\x15\n\x11kToInstallPackage\x10\x02\x12\x15\n\x11kPackageInstalled\x10\x03\x12\x17\n\x13kToRemoveOldPackage\x10\x04\x12\x1a\n\x16kToUpdateClusterConfig\x10\x05\x12\x19\n\x15kReleaseUpgradeTicket\x10\x06\x12\x11\n\rkToRebootNode\x10\x07J\x04\x08\x03\x10\x04\"L\n\x14\x43lusterRestartRecord\x12\x1e\n\x16last_updated_time_secs\x18\x01 \x01(\x03\x12\x14\n\x0cnode_boot_id\x18\x02 \x01(\t\"c\n\x13UpgradeChecksRecord\x12\x13\n\x0binstance_id\x18\x01 \x01(\x03\x12\x17\n\x0fstart_time_secs\x18\x02 \x01(\x03\x12\x1e\n\x16last_updated_time_secs\x18\x03 \x01(\x03\"\xa5\x02\n\x10RemoveNodeRecord\x12\x35\n\x05state\x18\x01 \x02(\x0e\x32&.cohesity.nexus.RemoveNodeRecord.State\x12\"\n\x1ato_cleanup_disk_mount_path\x18\x02 \x01(\t\x12#\n\x1bto_cleanup_disk_device_path\x18\x03 \x01(\t\x12\x1e\n\x16last_updated_time_secs\x18\x04 \x01(\x03\x12\x1f\n\x10\x66orceful_removal\x18\x05 \x01(\x08:\x05\x66\x61lse\"P\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x12\n\x0ekToStopGandalf\x10\x01\x12\x11\n\rkToRemoveDirs\x10\x02\x12\x13\n\x0fkToCleanupDisks\x10\x03\"[\n\x14\x44iskAssimilateRecord\x12\x15\n\rdisk_path_vec\x18\x01 \x03(\t\x12\x17\n\x0f\x64isk_serial_vec\x18\x02 \x03(\t\x12\x13\n\x0bis_metadata\x18\x03 \x01(\x08\"\xdd\x01\n\x11\x44iskOfflineRecord\x12\x0f\n\x07\x64isk_id\x18\x01 \x02(\x03\x12\x0f\n\x07offline\x18\x02 \x02(\x08\x12L\n\tdisk_type\x18\x03 \x02(\x0e\x32*.cohesity.nexus.DiskOfflineRecord.DiskType:\rkDiskTypeNone\"X\n\x08\x44iskType\x12\x11\n\rkDiskTypeNone\x10\x00\x12\x13\n\x0fkDiskTypeSystem\x10\x01\x12\x11\n\rkDiskTypeData\x10\x02\x12\x11\n\rkDiskTypeBoth\x10\x03\"S\n\x10\x44iskExtendRecord\x12\x17\n\x0f\x64isk_serial_vec\x18\x01 \x03(\t\x12\x15\n\rdisk_path_vec\x18\x02 \x03(\t\x12\x0f\n\x07\x62oot_id\x18\x03 \x01(\t\"\xab\x05\n\x18RigelClusterCreateRecord\x12\x14\n\x0c\x63luster_name\x18\x01 \x02(\t\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x03 \x02(\x03\x12\x16\n\x0entp_server_vec\x18\x04 \x03(\t\x12\x16\n\x0e\x64ns_server_vec\x18\x05 \x03(\t\x12\x17\n\x0f\x64omain_name_vec\x18\x06 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x07 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\t \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\n \x02(\t\x12\x45\n\x13ServicesGflagsProto\x18\x0b \x01(\x0b\x32(.cohesity.nexus.base.ServicesGflagsProto\x12S\n\x13proxy_server_config\x18\x0c \x01(\x0b\x32\x36.cohesity.configs.ClusterConfigProto.ProxyServerConfig\x12Q\n\rip_preference\x18\r \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12\x10\n\x08hostname\x18\x0e \x01(\t\x12\x0f\n\x07node_ip\x18\x0f \x02(\t\x12\x13\n\x0b\x63laim_token\x18\x10 \x01(\t\x12\x0f\n\x07is_dhcp\x18\x11 \x01(\x08\x12\x1e\n\x16\x65nable_support_channel\x18\x12 \x01(\x08\x12-\n%enable_support_channel_end_time_msecs\x18\x13 \x01(\x03\"\xa2\x03\n\x10ResetStateRecord\x12\x0f\n\x07is_undo\x18\x01 \x01(\x08\x12<\n\ncurrent_op\x18\x02 \x01(\x0e\x32(.cohesity.nexus.ResetStateRecord.ResetOp\"\xbe\x02\n\x07ResetOp\x12\x11\n\rkResetStateOp\x10\x00\x12\x15\n\x11kNetworkScriptsOp\x10\x01\x12\x1c\n\x18kReplaceNetworkScriptsOp\x10\x02\x12\x17\n\x13kSysconfigNetworkOp\x10\x03\x12\x1e\n\x1akReplaceSysconfigNetworkOp\x10\x04\x12\x0f\n\x0bkIproute2Op\x10\x05\x12\x16\n\x12kReplaceIproute2Op\x10\x06\x12\x12\n\x0ekOpenvswitchOp\x10\x07\x12\x19\n\x15kReplaceOpenvswitchOp\x10\x08\x12\x17\n\x13kNetworkingSysctlOp\x10\t\x12\x1e\n\x1akReplaceNetworkingSysctlOp\x10\n\x12\x14\n\x10kNetworkConfigOp\x10\x0b\x12\x0b\n\x07kDoneOp\x10\x0c\"\x9f\x0b\n\x15NetworkingResetRecord\x12:\n\x05state\x18\x01 \x02(\x0e\x32+.cohesity.nexus.NetworkingResetRecord.State\x12\x14\n\x0c\x63luster_name\x18\x02 \x02(\t\x12\x12\n\ncluster_id\x18\x03 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x04 \x02(\x03\x12\x13\n\x0bntp_servers\x18\x05 \x03(\t\x12\x13\n\x0b\x64ns_servers\x18\x06 \x03(\t\x12\x14\n\x0c\x64omain_names\x18\x07 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x08 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\t \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\n \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\x0b \x02(\t\x12\x14\n\x0cipmi_gateway\x18\x0c \x01(\t\x12\x16\n\x0eipmi_subnet_ip\x18\r \x01(\t\x12\x1c\n\x14ipmi_subnet_cidr_len\x18\x0e \x01(\x05\x12\x1d\n\x15ipmi_subnet_ipv4_mask\x18\x0f \x01(\t\x12\x15\n\ripmi_username\x18\x10 \x01(\t\x12\x15\n\ripmi_password\x18\x11 \x01(\t\x12;\n\x08node_vec\x18\x12 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\x12\x31\n\x08req_type\x18\x13 \x02(\x0e\x32\x1f.cohesity.nexus.RestRequestType\x12 \n\x18\x63luster_software_version\x18\x14 \x02(\t\x12\x46\n\x0c\x62onding_mode\x18\x15 \x01(\x0e\x32\x30.cohesity.configs.ClusterConfigProto.BondingMode\x12\x0b\n\x03mtu\x18\x16 \x01(\x05\x12\x16\n\x0esender_node_ip\x18\x17 \x01(\t\x12@\n\x16node_ip_preference_vec\x18\x18 \x03(\x0b\x32 .cohesity.nexus.NodeIpPreference\x12\x13\n\x0bin_progress\x18\x19 \x01(\x08\x12\x0f\n\x07vip_vec\x18\x1a \x03(\t\x12#\n\x1b\x63luster_partition_host_name\x18\x1b \x01(\t\x12Q\n\rip_preference\x18\x1c \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12U\n\x18ntp_server_auth_keys_vec\x18\x1d \x03(\x0b\x32\x33.cohesity.configs.ClusterConfigProto.NTPAuthKeyInfo\x12/\n\rdns_group_vec\x18\x1e \x03(\x0b\x32\x18.cohesity.nexus.DnsGroup\x12\x44\n\x18\x63luster_subnet_group_vec\x18\x1f \x03(\x0b\x32\".cohesity.nexus.ClusterSubnetGroup\x12\"\n\x1antp_authentication_enabled\x18  \x01(\x08\x12@\n\x0b\x61pps_subnet\x18! \x01(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\x12\x43\n\x0e\x61pps_subnet_v6\x18\" \x01(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\"X\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12#\n\x1fkNetworkConfigurationInProgress\x10\x01\x12\x1d\n\x19kNetworkConfigurationDone\x10\x02\"\xf0\x05\n\x1bHeOnpremClusterCreateRecord\x12\x14\n\x0c\x63luster_name\x18\x01 \x02(\t\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x03 \x02(\x03\x12\x16\n\x0entp_server_vec\x18\x04 \x03(\t\x12\x16\n\x0e\x64ns_server_vec\x18\x05 \x03(\t\x12\x17\n\x0f\x64omain_name_vec\x18\x06 \x03(\t\x12\x17\n\x0f\x63luster_gateway\x18\x07 \x02(\t\x12\x19\n\x11\x63luster_subnet_ip\x18\x08 \x02(\t\x12\x1f\n\x17\x63luster_subnet_cidr_len\x18\t \x02(\x05\x12 \n\x18\x63luster_subnet_ipv4_mask\x18\n \x02(\t\x12\x45\n\x13ServicesGflagsProto\x18\x0b \x01(\x0b\x32(.cohesity.nexus.base.ServicesGflagsProto\x12S\n\x13proxy_server_config\x18\x0c \x01(\x0b\x32\x36.cohesity.configs.ClusterConfigProto.ProxyServerConfig\x12Q\n\rip_preference\x18\r \x01(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.IpAddressFamily:\x04IPv4\x12\x10\n\x08hostname\x18\x0e \x01(\t\x12\x0f\n\x07node_ip\x18\x0f \x02(\t\x12\x0f\n\x07is_dhcp\x18\x10 \x01(\x08\x12\x1e\n\x16\x65nable_support_channel\x18\x11 \x01(\x08\x12-\n%enable_support_channel_end_time_msecs\x18\x12 \x01(\x03\x12U\n\x14helios_onprem_config\x18\x13 \x01(\x0b\x32\x37.cohesity.configs.ClusterConfigProto.HeliosOnpremConfig\"<\n\x1aSystemServiceBringupRecord\x12\x1e\n\x16last_updated_time_secs\x18\x01 \x01(\x03\"\xb6\x06\n\x14\x43reateSnapshotRecord\x12\x35\n\x08req_type\x18\x01 \x01(\x0e\x32#.cohesity.nexus.SnapshotRequestType\x12\x12\n\ncluster_id\x18\x02 \x01(\x03\x12\x18\n\x10snapshot_version\x18\x03 \x01(\t\x12;\n\x08node_vec\x18\x04 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\x12\x16\n\x0esender_node_ip\x18\x05 \x01(\t\x12\x18\n\x10software_version\x18\x06 \x01(\t\x12\x17\n\x0fhot_fix_version\x18\x07 \x01(\t\x12\"\n\x1alocal_data_backup_location\x18\x08 \x01(\t\x12/\n\x11\x63urrent_operation\x18\t \x01(\t:\x14Nothing in progress.\x12I\n\x15\x63reate_snapshot_state\x18\n \x01(\x0e\x32*.cohesity.nexus.CreateSnapshotRecord.State\x12\x1e\n\x16last_updated_time_secs\x18\x0b \x01(\x03\"\xf0\x02\n\x05State\x12\x12\n\x0ekNoStateChange\x10\x00\x12\x11\n\rkStartingBgOp\x10\x01\x12\x1b\n\x17kStoppingClusterService\x10\x02\x12!\n\x1dkWaitingForStopClusterService\x10\x03\x12\x14\n\x10kStoppingGandalf\x10\x04\x12\x1f\n\x1bkBackingUpLocalDataToRemote\x10\x05\x12*\n&kWaitingForAllNodesLocalDataBackupDone\x10\x06\x12!\n\x1dkCreatingSnapshotOfRemoteData\x10\x07\x12\x14\n\x10kStartingGandalf\x10\x08\x12\x1b\n\x17kStartingClusterService\x10\t\x12\"\n\x1ekWaitingForStartClusterService\x10\n\x12\x0f\n\x0bkBgOpFailed\x10\x0b\x12\x12\n\x0ekBgOpCompleted\x10\x0c\"\x9d\x07\n\x15RestoreSnapshotRecord\x12\x35\n\x08req_type\x18\x01 \x01(\x0e\x32#.cohesity.nexus.SnapshotRequestType\x12\x12\n\ncluster_id\x18\x02 \x01(\x03\x12\x18\n\x10snapshot_version\x18\x03 \x01(\t\x12\x1e\n\x16restore_to_new_cluster\x18\x04 \x01(\x08\x12;\n\x08node_vec\x18\x05 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\x12\x16\n\x0esender_node_ip\x18\x06 \x01(\t\x12\x1d\n\x15\x66lash_blade_data_vips\x18\x07 \x03(\t\x12\x18\n\x10\x61ll_file_systems\x18\x08 \x03(\t\x12\x1a\n\x12local_file_systems\x18\t \x03(\t\x12/\n\x11\x63urrent_operation\x18\n \x01(\t:\x14Nothing in progress.\x12K\n\x16restore_snapshot_state\x18\x0b \x01(\x0e\x32+.cohesity.nexus.RestoreSnapshotRecord.State\x12\x1e\n\x16last_updated_time_secs\x18\x0c \x01(\x03\"\xb6\x03\n\x05State\x12\x12\n\x0ekNoStateChange\x10\x00\x12\x11\n\rkStartingBgOp\x10\x01\x12\x1b\n\x17kStoppingClusterService\x10\x02\x12!\n\x1dkWaitingForStopClusterService\x10\x03\x12\x14\n\x10kStoppingGandalf\x10\x04\x12\x18\n\x14kUnmountingNfsShares\x10\x05\x12,\n(kWaitingForRestoreRemoteDataSnapshotDone\x10\x06\x12\'\n#kRestoringLocalDataFromRemoteBackup\x10\x07\x12+\n\'kWaitingForAllNodesLocalDataRestoreDone\x10\x08\x12\x14\n\x10kStartingGandalf\x10\t\x12\x16\n\x12kMountingNfsShares\x10\n\x12\x1b\n\x17kStartingClusterService\x10\x0b\x12\"\n\x1ekWaitingForStartClusterService\x10\x0c\x12\x0f\n\x0bkBgOpFailed\x10\r\x12\x12\n\x0ekBgOpCompleted\x10\x0e\"\x91\x02\n\x16NodeDisaggregateRecord\x12;\n\x05state\x18\x01 \x02(\x0e\x32,.cohesity.nexus.NodeDisaggregateRecord.State\x12\x12\n\ncluster_id\x18\x02 \x02(\x03\x12\x0f\n\x07node_id\x18\x03 \x01(\x03\x12\x16\n\x0esender_node_ip\x18\x04 \x01(\t\x12;\n\x08node_vec\x18\x05 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\"@\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x10\n\x0ckBackupFiles\x10\x01\x12\x18\n\x14kStopServicesAndExit\x10\x02\"\xfb\x03\n\x13NodeAggregateRecord\x12\x38\n\x05state\x18\x01 \x02(\x0e\x32).cohesity.nexus.NodeAggregateRecord.State\x12\x14\n\x0c\x63luster_name\x18\x02 \x02(\t\x12\x12\n\ncluster_id\x18\x03 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x04 \x02(\x03\x12 \n\x18\x63luster_software_version\x18\x05 \x02(\t\x12;\n\x08node_vec\x18\x06 \x03(\x0b\x32).cohesity.configs.ClusterConfigProto.Node\x12\x16\n\x0esender_node_ip\x18\x07 \x01(\t\x12\x1a\n\x12primary_iface_name\x18\x08 \x01(\t\x12\x0b\n\x03mtu\x18\t \x01(\x05\x12\x46\n\x0c\x62onding_mode\x18\n \x01(\x0e\x32\x30.cohesity.configs.ClusterConfigProto.BondingMode\x12\x0f\n\x07node_id\x18\x0b \x01(\x03\x12\x0f\n\x07node_ip\x18\x0c \x01(\t\x12\x17\n\x0f\x66orce_aggregate\x18\r \x01(\x08\"=\n\x05State\x12\x0b\n\x07kIntent\x10\x00\x12\x11\n\rkRestoreFiles\x10\x01\x12\x14\n\x10kRestartServices\x10\x02\"\xe9\x01\n\x15\x46irmwareUpgradeRecord\x12\\\n\rfirmware_type\x18\x01 \x01(\x0e\x32\x32.cohesity.nexus.FirmwareUpgradeRecord.FirmwareType:\x11kFirmwareTypeNone\x12\x19\n\x11\x64\x65vice_serial_vec\x18\x02 \x03(\t\"W\n\x0c\x46irmwareType\x12\x15\n\x11kFirmwareTypeNone\x10\x00\x12\x19\n\x15kFirmwareTypePlatform\x10\x01\x12\x15\n\x11kFirmwareTypeDisk\x10\x02\"\xca\x14\n\tWalRecord\x12=\n\toperation\x18\x01 \x01(\x0e\x32#.cohesity.nexus.WalRecord.Operation:\x05kNone\x12!\n\x19operation_start_time_secs\x18\x02 \x01(\x03\x12M\n\x1b\x63loud_cluster_create_record\x18\x03 \x01(\x0b\x32(.cohesity.nexus.CloudClusterCreateRecord\x12R\n\x1e\x63loud_cluster_add_nodes_record\x18\x04 \x01(\x0b\x32*.cohesity.nexus.CloudClusterAddNodesRecord\x12\x44\n\x16\x63luster_destroy_record\x18\x05 \x01(\x0b\x32$.cohesity.nexus.ClusterDestroyRecord\x12R\n\x1e\x63loud_node_join_cluster_record\x18\x06 \x01(\x0b\x32*.cohesity.nexus.CloudNodeJoinClusterRecord\x12M\n\x1bnode_disjoin_cluster_record\x18\x07 \x01(\x0b\x32(.cohesity.nexus.NodeDisjoinClusterRecord\x12>\n\x13node_upgrade_record\x18\x08 \x01(\x0b\x32!.cohesity.nexus.NodeUpgradeRecord\x12\x44\n\x16\x63luster_upgrade_record\x18\t \x01(\x0b\x32$.cohesity.nexus.ClusterUpgradeRecord\x12<\n\x12remove_node_record\x18\n \x01(\x0b\x32 .cohesity.nexus.RemoveNodeRecord\x12K\n\x1a\x63luster_remove_node_record\x18\x0c \x01(\x0b\x32\'.cohesity.nexus.ClusterRemoveNodeRecord\x12\x44\n\x16\x64isk_assimilate_record\x18\r \x01(\x0b\x32$.cohesity.nexus.DiskAssimilateRecord\x12K\n\x1a\x63luster_bringup_wal_record\x18\x0e \x01(\x0b\x32\'.cohesity.nexus.ClusterBringupWalRecord\x12\x44\n\x16\x63luster_restart_record\x18\x0f \x01(\x0b\x32$.cohesity.nexus.ClusterRestartRecord\x12Z\n\"virtual_robo_cluster_create_record\x18\x10 \x01(\x0b\x32..cohesity.nexus.VirtualRoboClusterCreateRecord\x12>\n\x13\x64isk_offline_record\x18\x11 \x01(\x0b\x32!.cohesity.nexus.DiskOfflineRecord\x12<\n\x12\x64isk_extend_record\x18\x12 \x01(\x0b\x32 .cohesity.nexus.DiskExtendRecord\x12M\n\x1brigel_cluster_create_record\x18\x13 \x01(\x0b\x32(.cohesity.nexus.RigelClusterCreateRecord\x12\x46\n\x17networking_reset_record\x18\x14 \x01(\x0b\x32%.cohesity.nexus.NetworkingResetRecord\x12<\n\x12reset_state_record\x18\x15 \x01(\x0b\x32 .cohesity.nexus.ResetStateRecord\x12T\n\x1fhe_onprem_cluster_create_record\x18\x16 \x01(\x0b\x32+.cohesity.nexus.HeOnpremClusterCreateRecord\x12Q\n\x1dsystem_service_bringup_record\x18\x17 \x01(\x0b\x32*.cohesity.nexus.SystemServiceBringupRecord\x12\x44\n\x16\x63reate_snapshot_record\x18\x18 \x01(\x0b\x32$.cohesity.nexus.CreateSnapshotRecord\x12\x46\n\x17restore_snapshot_record\x18\x19 \x01(\x0b\x32%.cohesity.nexus.RestoreSnapshotRecord\x12\x42\n\x15node_aggregate_record\x18\x1a \x01(\x0b\x32#.cohesity.nexus.NodeAggregateRecord\x12H\n\x18node_disaggregate_record\x18\x1b \x01(\x0b\x32&.cohesity.nexus.NodeDisaggregateRecord\x12\x42\n\x15upgrade_checks_record\x18\x1c \x01(\x0b\x32#.cohesity.nexus.UpgradeChecksRecord\x12\x46\n\x17\x66irmware_upgrade_record\x18\x1d \x01(\x0b\x32%.cohesity.nexus.FirmwareUpgradeRecord\"\xde\x04\n\tOperation\x12\t\n\x05kNone\x10\x00\x12\x13\n\x0fkClusterDestroy\x10\x03\x12\x13\n\x0fkClusterUpgrade\x10\x04\x12\x13\n\x0fkClusterRestart\x10\x05\x12\x17\n\x13kNodeDisjoinCluster\x10\x07\x12\x10\n\x0ckNodeUpgrade\x10\x08\x12\x0f\n\x0bkRemoveNode\x10\t\x12\x16\n\x12kClusterRemoveNode\x10\x0b\x12\x13\n\x0fkDiskAssimilate\x10\x0c\x12\x13\n\x0fkClusterBringup\x10\r\x12\x17\n\x13kCloudClusterCreate\x10\x0e\x12\x19\n\x15kCloudClusterAddNodes\x10\x0f\x12\x19\n\x15kCloudNodeJoinCluster\x10\x10\x12\x1d\n\x19kVirtualRoboClusterCreate\x10\x11\x12\x10\n\x0ckDiskOffline\x10\x12\x12\x0f\n\x0bkDiskExtend\x10\x13\x12\x17\n\x13kRigelClusterCreate\x10\x14\x12\x14\n\x10kNetworkingReset\x10\x15\x12\x0f\n\x0bkResetState\x10\x16\x12\x1a\n\x16kHeOnpremClusterCreate\x10\x17\x12\x19\n\x15kSystemServiceBringup\x10\x18\x12\x13\n\x0fkCreateSnapshot\x10\x19\x12\x14\n\x10kRestoreSnapshot\x10\x1a\x12\x15\n\x11kNodeDisaggregate\x10\x1b\x12\x12\n\x0ekNodeAggregate\x10\x1c\x12\x15\n\x11kRunUpgradeChecks\x10\x1d\x12\x14\n\x10kFirmwareUpgrade\x10\x1eJ\x04\x08\x0b\x10\x0c\"i\n\x15UpgraderOpStateRecord\x12\x1e\n\x16last_updated_time_secs\x18\x01 \x01(\x03\x12\x18\n\x10restart_attempts\x18\x02 \x01(\x03\x12\x16\n\x0erestart_reason\x18\x03 \x03(\t*\x83\x01\n\x0fRestRequestType\x12\x13\n\x0fkClusterBringup\x10\x01\x12\x12\n\x0ekClusterExpand\x10\x02\x12\x10\n\x0ckNodeBringup\x10\x03\x12\x1b\n\x17kClusterNetworkingReset\x10\x04\x12\x18\n\x14kNodeNetworkingReset\x10\x05*\xe7\x02\n\x0c\x42ringupState\x12\x12\n\x0ekNoStateChange\x10\x00\x12\x11\n\rkStartingBgOp\x10\x01\x12\x17\n\x13kConfiguringNetwork\x10\x02\x12\x12\n\x0ekUpgradingNode\x10\x03\x12\x14\n\x10kStartingGandalf\x10\x04\x12\x19\n\x15kInitingClusterConfig\x10\x05\x12\x1a\n\x16kAddingChassisAndNodes\x10\x06\x12\x17\n\x13kInitingTimeService\x10\x07\x12\x14\n\x10kFormattingDisks\x10\x08\x12\x13\n\x0fkFormattedDisks\x10\t\x12\x19\n\x15kWaitingForSlavesDone\x10\n\x12\x1d\n\x19kWaitingForHandshakesDone\x10\x0b\x12\x13\n\x0fkHandshakesDone\x10\x0c\x12\x0f\n\x0bkBgOpFailed\x10\r\x12\x12\n\x0ekBgOpCompleted\x10\x0e*\x81\x01\n\x13SnapshotRequestType\x12\x1a\n\x16kClusterCreateSnapshot\x10\x01\x12\x17\n\x13kNodeCreateSnapshot\x10\x02\x12\x1b\n\x17kClusterRestoreSnapshot\x10\x03\x12\x18\n\x14kNodeRestoreSnapshot\x10\x04\x42\x31\n\x16\x63om.cohesity.nexus.walZ\x17nexus/base/nexus_wal.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.nexus_wal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cohesity.nexus.walZ\027nexus/base/nexus_wal.pb'
  _globals['_RESTREQUESTTYPE']._serialized_start=17177
  _globals['_RESTREQUESTTYPE']._serialized_end=17308
  _globals['_BRINGUPSTATE']._serialized_start=17311
  _globals['_BRINGUPSTATE']._serialized_end=17670
  _globals['_SNAPSHOTREQUESTTYPE']._serialized_start=17673
  _globals['_SNAPSHOTREQUESTTYPE']._serialized_end=17802
  _globals['_NODEINFO']._serialized_start=186
  _globals['_NODEINFO']._serialized_end=225
  _globals['_NODEIPPREFERENCE']._serialized_start=227
  _globals['_NODEIPPREFERENCE']._serialized_end=322
  _globals['_DNSGROUP']._serialized_start=324
  _globals['_DNSGROUP']._serialized_end=390
  _globals['_CLUSTERSUBNETGROUP']._serialized_start=393
  _globals['_CLUSTERSUBNETGROUP']._serialized_end=535
  _globals['_BRINGUPSTATUSEVENT']._serialized_start=537
  _globals['_BRINGUPSTATUSEVENT']._serialized_end=606
  _globals['_CLUSTERBRINGUPWALRECORD']._serialized_start=609
  _globals['_CLUSTERBRINGUPWALRECORD']._serialized_end=3374
  _globals['_VIRTUALROBOCLUSTERCREATERECORD']._serialized_start=3377
  _globals['_VIRTUALROBOCLUSTERCREATERECORD']._serialized_end=4396
  _globals['_CLOUDCLUSTERCREATERECORD']._serialized_start=4399
  _globals['_CLOUDCLUSTERCREATERECORD']._serialized_end=5195
  _globals['_CLOUDCLUSTERADDNODESRECORD']._serialized_start=5198
  _globals['_CLOUDCLUSTERADDNODESRECORD']._serialized_end=5581
  _globals['_CLOUDNODEJOINCLUSTERRECORD']._serialized_start=5584
  _globals['_CLOUDNODEJOINCLUSTERRECORD']._serialized_end=5996
  _globals['_CLUSTERDESTROYRECORD']._serialized_start=5999
  _globals['_CLUSTERDESTROYRECORD']._serialized_end=6337
  _globals['_CLUSTERDESTROYRECORD_STATE']._serialized_start=6234
  _globals['_CLUSTERDESTROYRECORD_STATE']._serialized_end=6337
  _globals['_CLUSTERREMOVENODERECORD']._serialized_start=6339
  _globals['_CLUSTERREMOVENODERECORD']._serialized_end=6418
  _globals['_NODEDISJOINCLUSTERRECORD']._serialized_start=6421
  _globals['_NODEDISJOINCLUSTERRECORD']._serialized_end=6697
  _globals['_NODEDISJOINCLUSTERRECORD_STATE']._serialized_start=6637
  _globals['_NODEDISJOINCLUSTERRECORD_STATE']._serialized_end=6697
  _globals['_NODEUPGRADERECORD']._serialized_start=6700
  _globals['_NODEUPGRADERECORD']._serialized_end=7095
  _globals['_NODEUPGRADERECORD_STATE']._serialized_start=7002
  _globals['_NODEUPGRADERECORD_STATE']._serialized_end=7089
  _globals['_CLUSTERUPGRADERECORD']._serialized_start=7098
  _globals['_CLUSTERUPGRADERECORD']._serialized_end=7412
  _globals['_CLUSTERUPGRADERECORD_STATE']._serialized_start=7214
  _globals['_CLUSTERUPGRADERECORD_STATE']._serialized_end=7406
  _globals['_CLUSTERRESTARTRECORD']._serialized_start=7414
  _globals['_CLUSTERRESTARTRECORD']._serialized_end=7490
  _globals['_UPGRADECHECKSRECORD']._serialized_start=7492
  _globals['_UPGRADECHECKSRECORD']._serialized_end=7591
  _globals['_REMOVENODERECORD']._serialized_start=7594
  _globals['_REMOVENODERECORD']._serialized_end=7887
  _globals['_REMOVENODERECORD_STATE']._serialized_start=7807
  _globals['_REMOVENODERECORD_STATE']._serialized_end=7887
  _globals['_DISKASSIMILATERECORD']._serialized_start=7889
  _globals['_DISKASSIMILATERECORD']._serialized_end=7980
  _globals['_DISKOFFLINERECORD']._serialized_start=7983
  _globals['_DISKOFFLINERECORD']._serialized_end=8204
  _globals['_DISKOFFLINERECORD_DISKTYPE']._serialized_start=8116
  _globals['_DISKOFFLINERECORD_DISKTYPE']._serialized_end=8204
  _globals['_DISKEXTENDRECORD']._serialized_start=8206
  _globals['_DISKEXTENDRECORD']._serialized_end=8289
  _globals['_RIGELCLUSTERCREATERECORD']._serialized_start=8292
  _globals['_RIGELCLUSTERCREATERECORD']._serialized_end=8975
  _globals['_RESETSTATERECORD']._serialized_start=8978
  _globals['_RESETSTATERECORD']._serialized_end=9396
  _globals['_RESETSTATERECORD_RESETOP']._serialized_start=9078
  _globals['_RESETSTATERECORD_RESETOP']._serialized_end=9396
  _globals['_NETWORKINGRESETRECORD']._serialized_start=9399
  _globals['_NETWORKINGRESETRECORD']._serialized_end=10838
  _globals['_NETWORKINGRESETRECORD_STATE']._serialized_start=10750
  _globals['_NETWORKINGRESETRECORD_STATE']._serialized_end=10838
  _globals['_HEONPREMCLUSTERCREATERECORD']._serialized_start=10841
  _globals['_HEONPREMCLUSTERCREATERECORD']._serialized_end=11593
  _globals['_SYSTEMSERVICEBRINGUPRECORD']._serialized_start=11595
  _globals['_SYSTEMSERVICEBRINGUPRECORD']._serialized_end=11655
  _globals['_CREATESNAPSHOTRECORD']._serialized_start=11658
  _globals['_CREATESNAPSHOTRECORD']._serialized_end=12480
  _globals['_CREATESNAPSHOTRECORD_STATE']._serialized_start=12112
  _globals['_CREATESNAPSHOTRECORD_STATE']._serialized_end=12480
  _globals['_RESTORESNAPSHOTRECORD']._serialized_start=12483
  _globals['_RESTORESNAPSHOTRECORD']._serialized_end=13408
  _globals['_RESTORESNAPSHOTRECORD_STATE']._serialized_start=12970
  _globals['_RESTORESNAPSHOTRECORD_STATE']._serialized_end=13408
  _globals['_NODEDISAGGREGATERECORD']._serialized_start=13411
  _globals['_NODEDISAGGREGATERECORD']._serialized_end=13684
  _globals['_NODEDISAGGREGATERECORD_STATE']._serialized_start=13620
  _globals['_NODEDISAGGREGATERECORD_STATE']._serialized_end=13684
  _globals['_NODEAGGREGATERECORD']._serialized_start=13687
  _globals['_NODEAGGREGATERECORD']._serialized_end=14194
  _globals['_NODEAGGREGATERECORD_STATE']._serialized_start=14133
  _globals['_NODEAGGREGATERECORD_STATE']._serialized_end=14194
  _globals['_FIRMWAREUPGRADERECORD']._serialized_start=14197
  _globals['_FIRMWAREUPGRADERECORD']._serialized_end=14430
  _globals['_FIRMWAREUPGRADERECORD_FIRMWARETYPE']._serialized_start=14343
  _globals['_FIRMWAREUPGRADERECORD_FIRMWARETYPE']._serialized_end=14430
  _globals['_WALRECORD']._serialized_start=14433
  _globals['_WALRECORD']._serialized_end=17067
  _globals['_WALRECORD_OPERATION']._serialized_start=16455
  _globals['_WALRECORD_OPERATION']._serialized_end=17061
  _globals['_UPGRADEROPSTATERECORD']._serialized_start=17069
  _globals['_UPGRADEROPSTATERECORD']._serialized_end=17174
# @@protoc_insertion_point(module_scope)