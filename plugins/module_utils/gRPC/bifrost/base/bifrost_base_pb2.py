# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bifrost/base/bifrost_base.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62ifrost/base/bifrost_base.proto\x12\x10\x63ohesity.bifrost\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x18util/base/op_clock.proto\"c\n\x14\x42ifrostServerIdProto\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x1a\n\x0e\x63onstituent_id\x18\x02 \x01(\x03:\x02-1\x12\x16\n\nsession_id\x18\x03 \x01(\x03:\x02-1J\x04\x08\x06\x10\x07\"\xbf\x02\n\x14\x42ifrostRtConfigProto\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x1e\n\x13\x65nd_timestamp_msecs\x18\x02 \x01(\x03:\x01\x30\x12\x19\n\x0ert_remote_port\x18\x03 \x01(\x05:\x01\x30\x12\x18\n\x0crt_host_port\x18\x04 \x01(\x05:\x02\x32\x32\x12\x14\n\x08ssh_port\x18\x05 \x01(\x05:\x02\x32\x32\x12\x1c\n\x0cssh_username\x18\x06 \x01(\t:\x06rtuser\x12\x0f\n\x07ssh_key\x18\x07 \x01(\x0c\x12=\n\x11ssh_key_file_path\x18\x08 \x01(\t:\"/home/cohesity/data/rtclient/rtkey\x12>\n\x0cproxy_server\x18\t \x01(\x0b\x32(.cohesity.bifrost.ProxyServerConfigProto\"n\n\x16ProxyServerConfigProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x02(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x1a\n\x12\x65ncrypted_password\x18\x05 \x01(\x0c\"\'\n\x06Subnet\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x11\n\tmask_bits\x18\x02 \x01(\x05\"Y\n\x0fNetworkConnInfo\x12\x17\n\x0fnetwork_gateway\x18\x01 \x01(\t\x12\x0b\n\x03\x64ns\x18\x02 \x01(\t\x12\x0b\n\x03ntp\x18\x03 \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x04 \x01(\t\"\xec\x0e\n\x0cNetworkRealm\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.cohesity.bifrost.NetworkRealm.Type\x12\x16\n\x07\x64\x65leted\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x08realm_id\x18\x03 \x01(\x03\x12\x12\n\nrealm_name\x18\x04 \x01(\t\x12\x11\n\ttenant_id\x18\x07 \x01(\t\x12.\n\x0crealm_subnet\x18\x05 \x01(\x0b\x32\x18.cohesity.bifrost.Subnet\x12Q\n\x15\x65xternal_bifrost_info\x18\x06 \x01(\x0b\x32\x32.cohesity.bifrost.NetworkRealm.ExternalBifrostInfo\x12\x42\n\rupdate_intent\x18\x08 \x01(\x0b\x32+.cohesity.bifrost.NetworkRealm.UpdateIntent\x12&\n\x0bopclock_vec\x18\t \x03(\x0b\x32\x11.cohesity.OpClock\x12\x1c\n\x14hyx_connector_id_vec\x18\n \x03(\x03\x12W\n\x1a\x63\x61pabilities_at_broker_vec\x18\x0b \x03(\x0b\x32\x33.cohesity.bifrost.NetworkRealm.CapabilitiesAtBroker\x12M\n\x10\x63\x61pabilities_map\x18\x0c \x03(\x0b\x32\x33.cohesity.bifrost.NetworkRealm.CapabilitiesMapEntry\x12\x42\n\x17network_connection_info\x18\r \x01(\x0b\x32!.cohesity.bifrost.NetworkConnInfo\x12G\n\tbw_limits\x18\x0e \x01(\x0b\x32\x34.cohesity.configs.ClusterConfigProto.BandwidthLimits\x12&\n\x1eungrouped_hyx_connector_id_vec\x18\x0f \x03(\x03\x12J\n\x13\x63onnector_group_vec\x18\x10 \x03(\x0b\x32-.cohesity.bifrost.NetworkRealm.ConnectorGroup\x12\x10\n\x08scalable\x18\x11 \x01(\x08\x1a\x36\n\x13\x45xternalBifrostInfo\x12\x1f\n\x17hyx_certificate_version\x18\x01 \x01(\x03\x1a\xb4\x03\n\x0cUpdateIntent\x12\\\n\x14\x61\x64\x64ing_network_realm\x18\x01 \x01(\x0b\x32>.cohesity.bifrost.NetworkRealm.UpdateIntent.AddingNetworkRealm\x12`\n\x16renaming_network_realm\x18\x02 \x01(\x0b\x32@.cohesity.bifrost.NetworkRealm.UpdateIntent.RenamingNetworkRealm\x12`\n\x16\x64\x65leting_network_realm\x18\x03 \x01(\x0b\x32@.cohesity.bifrost.NetworkRealm.UpdateIntent.DeletingNetworkRealm\x1a(\n\x12\x41\x64\x64ingNetworkRealm\x12\x12\n\nrealm_name\x18\x01 \x01(\t\x1a.\n\x14RenamingNetworkRealm\x12\x16\n\x0enew_realm_name\x18\x01 \x01(\t\x1a(\n\x14\x44\x65letingNetworkRealm\x12\x10\n\x08realm_id\x18\x01 \x01(\x03\x1a\xeb\x01\n\x14\x43\x61pabilitiesAtBroker\x12\x1d\n\x15\x62roker_constituent_id\x18\x01 \x01(\x03\x12t\n\x1a\x63\x61pabilities_at_broker_map\x18\x02 \x03(\x0b\x32P.cohesity.bifrost.NetworkRealm.CapabilitiesAtBroker.CapabilitiesAtBrokerMapEntry\x1a>\n\x1c\x43\x61pabilitiesAtBrokerMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x36\n\x14\x43\x61pabilitiesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\xb1\x01\n\x0e\x43onnectorGroup\x12\x1c\n\x14\x63onnector_group_name\x18\x01 \x01(\t\x12\x1a\n\x12\x63onnector_group_id\x18\x02 \x01(\x03\x12\x1c\n\x14hyx_connector_id_vec\x18\x03 \x03(\x03\x12G\n\tbw_limits\x18\x04 \x01(\x0b\x32\x34.cohesity.configs.ClusterConfigProto.BandwidthLimits\"G\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x14\n\x10kExternalBifrost\x10\x01\x12\n\n\x06kRigel\x10\x02\x12\x0f\n\x0bkCohesityCp\x10\x03\"\xa8\x05\n\x17HyxConnectorConfigProto\x12\x18\n\x10hyx_connector_id\x18\x01 \x02(\x03\x12\x1a\n\x12hyx_connector_name\x18\x02 \x01(\t\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32#.cohesity.bifrost.NetworkRealm.Type\x12\x10\n\x08realm_id\x18\x04 \x01(\x03\x12\x1a\n\x12\x63onnector_group_id\x18\x0c \x01(\x03\x12\x1f\n\x17\x63\x65rtificate_version_vec\x18\r \x03(\x03\x12\x1f\n\x13\x63\x65rtificate_version\x18\x05 \x01(\x03\x42\x02\x18\x01\x12U\n\x11\x63onnection_status\x18\x06 \x01(\x0b\x32:.cohesity.bifrost.HyxConnectorConfigProto.ConnectionStatus\x12\x18\n\x10\x63ohesity_side_ip\x18\t \x01(\t\x12\x1d\n\x15tenant_source_side_ip\x18\n \x01(\t\x12\x0f\n\x07version\x18\x0b \x01(\t\x12&\n\x0bopclock_vec\x18\x08 \x03(\x0b\x32\x11.cohesity.OpClock\x12\x43\n\x0e\x63loud_metadata\x18\x0e \x01(\x0b\x32+.cohesity.bifrost.BifrostCloudMetadataProto\x12;\n\x0einitiator_type\x18\x0f \x01(\x0e\x32#.cohesity.bifrost.NetworkRealm.Type\x1a\x63\n\x10\x43onnectionStatus\x12\x14\n\x0cis_connected\x18\x01 \x01(\x08\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12&\n\x1elast_connected_timestamp_usecs\x18\x03 \x01(\x03J\x04\x08\x07\x10\x08\"C\n\x1aNetworkRealmNameMappingKey\x12\x12\n\nrealm_name\x18\x01 \x01(\t\x12\x11\n\ttenant_id\x18\x02 \x01(\t\"X\n\x1cNetworkRealmNameMappingProto\x12\x10\n\x08realm_id\x18\x01 \x01(\x03\x12&\n\x0bopclock_vec\x18\x02 \x03(\x0b\x32\x11.cohesity.OpClock\"]\n\x1c\x42ifrostResourceCapacityProto\x12\x1b\n\x0flegacy_capacity\x18\x01 \x01(\x01:\x02-1\x12 \n\x14max_disks_can_attach\x18\x02 \x01(\x01:\x02-1\"\xa1\x01\n\x19\x42ifrostCloudMetadataProto\x12?\n\x0c\x61ws_metadata\x18\x01 \x01(\x0b\x32).cohesity.bifrost.BifrostAwsMetadataProto\x12\x43\n\x0e\x61zure_metadata\x18\x02 \x01(\x0b\x32+.cohesity.bifrost.BifrostAzureMetadataProto\"2\n\x17\x42ifrostAwsMetadataProto\x12\x17\n\x0f\x61ws_instance_id\x18\x01 \x01(\t\"M\n\x19\x42ifrostAzureMetadataProto\x12\x13\n\x0b\x61zure_vm_id\x18\x01 \x01(\t\x12\x1b\n\x13max_data_disk_count\x18\x02 \x01(\x03*M\n\x16\x42ifrostRtServiceStatus\x12\x0c\n\x08kUnknown\x10\x00\x12\x0c\n\x08kHealthy\x10\x01\x12\x17\n\x13kUnhealthyOrStopped\x10\x02\x42\x1eZ\x1c\x62ifrost/base/bifrost_base.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bifrost.base.bifrost_base_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034bifrost/base/bifrost_base.pb'
  _globals['_NETWORKREALM_CAPABILITIESATBROKER_CAPABILITIESATBROKERMAPENTRY']._loaded_options = None
  _globals['_NETWORKREALM_CAPABILITIESATBROKER_CAPABILITIESATBROKERMAPENTRY']._serialized_options = b'8\001'
  _globals['_NETWORKREALM_CAPABILITIESMAPENTRY']._loaded_options = None
  _globals['_NETWORKREALM_CAPABILITIESMAPENTRY']._serialized_options = b'8\001'
  _globals['_HYXCONNECTORCONFIGPROTO'].fields_by_name['certificate_version']._loaded_options = None
  _globals['_HYXCONNECTORCONFIGPROTO'].fields_by_name['certificate_version']._serialized_options = b'\030\001'
  _globals['_BIFROSTRTSERVICESTATUS']._serialized_start=3911
  _globals['_BIFROSTRTSERVICESTATUS']._serialized_end=3988
  _globals['_BIFROSTSERVERIDPROTO']._serialized_start=109
  _globals['_BIFROSTSERVERIDPROTO']._serialized_end=208
  _globals['_BIFROSTRTCONFIGPROTO']._serialized_start=211
  _globals['_BIFROSTRTCONFIGPROTO']._serialized_end=530
  _globals['_PROXYSERVERCONFIGPROTO']._serialized_start=532
  _globals['_PROXYSERVERCONFIGPROTO']._serialized_end=642
  _globals['_SUBNET']._serialized_start=644
  _globals['_SUBNET']._serialized_end=683
  _globals['_NETWORKCONNINFO']._serialized_start=685
  _globals['_NETWORKCONNINFO']._serialized_end=774
  _globals['_NETWORKREALM']._serialized_start=777
  _globals['_NETWORKREALM']._serialized_end=2677
  _globals['_NETWORKREALM_EXTERNALBIFROSTINFO']._serialized_start=1637
  _globals['_NETWORKREALM_EXTERNALBIFROSTINFO']._serialized_end=1691
  _globals['_NETWORKREALM_UPDATEINTENT']._serialized_start=1694
  _globals['_NETWORKREALM_UPDATEINTENT']._serialized_end=2130
  _globals['_NETWORKREALM_UPDATEINTENT_ADDINGNETWORKREALM']._serialized_start=2000
  _globals['_NETWORKREALM_UPDATEINTENT_ADDINGNETWORKREALM']._serialized_end=2040
  _globals['_NETWORKREALM_UPDATEINTENT_RENAMINGNETWORKREALM']._serialized_start=2042
  _globals['_NETWORKREALM_UPDATEINTENT_RENAMINGNETWORKREALM']._serialized_end=2088
  _globals['_NETWORKREALM_UPDATEINTENT_DELETINGNETWORKREALM']._serialized_start=2090
  _globals['_NETWORKREALM_UPDATEINTENT_DELETINGNETWORKREALM']._serialized_end=2130
  _globals['_NETWORKREALM_CAPABILITIESATBROKER']._serialized_start=2133
  _globals['_NETWORKREALM_CAPABILITIESATBROKER']._serialized_end=2368
  _globals['_NETWORKREALM_CAPABILITIESATBROKER_CAPABILITIESATBROKERMAPENTRY']._serialized_start=2306
  _globals['_NETWORKREALM_CAPABILITIESATBROKER_CAPABILITIESATBROKERMAPENTRY']._serialized_end=2368
  _globals['_NETWORKREALM_CAPABILITIESMAPENTRY']._serialized_start=2370
  _globals['_NETWORKREALM_CAPABILITIESMAPENTRY']._serialized_end=2424
  _globals['_NETWORKREALM_CONNECTORGROUP']._serialized_start=2427
  _globals['_NETWORKREALM_CONNECTORGROUP']._serialized_end=2604
  _globals['_NETWORKREALM_TYPE']._serialized_start=2606
  _globals['_NETWORKREALM_TYPE']._serialized_end=2677
  _globals['_HYXCONNECTORCONFIGPROTO']._serialized_start=2680
  _globals['_HYXCONNECTORCONFIGPROTO']._serialized_end=3360
  _globals['_HYXCONNECTORCONFIGPROTO_CONNECTIONSTATUS']._serialized_start=3255
  _globals['_HYXCONNECTORCONFIGPROTO_CONNECTIONSTATUS']._serialized_end=3354
  _globals['_NETWORKREALMNAMEMAPPINGKEY']._serialized_start=3362
  _globals['_NETWORKREALMNAMEMAPPINGKEY']._serialized_end=3429
  _globals['_NETWORKREALMNAMEMAPPINGPROTO']._serialized_start=3431
  _globals['_NETWORKREALMNAMEMAPPINGPROTO']._serialized_end=3519
  _globals['_BIFROSTRESOURCECAPACITYPROTO']._serialized_start=3521
  _globals['_BIFROSTRESOURCECAPACITYPROTO']._serialized_end=3614
  _globals['_BIFROSTCLOUDMETADATAPROTO']._serialized_start=3617
  _globals['_BIFROSTCLOUDMETADATAPROTO']._serialized_end=3778
  _globals['_BIFROSTAWSMETADATAPROTO']._serialized_start=3780
  _globals['_BIFROSTAWSMETADATAPROTO']._serialized_end=3830
  _globals['_BIFROSTAZUREMETADATAPROTO']._serialized_start=3832
  _globals['_BIFROSTAZUREMETADATAPROTO']._serialized_end=3909
# @@protoc_insertion_point(module_scope)