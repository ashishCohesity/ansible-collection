# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/gcp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base.entities import cloud_pb2 as magneto_dot_base_dot_entities_dot_cloud__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmagneto/base/entities/gcp.proto\x12\x14\x63ohesity.magneto.gcp\x1a!magneto/base/entities/cloud.proto\x1a\x18magneto/base/enums.proto\"\xf0\x01\n\rGCPAttributes\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x39\n\x04type\x18\x06 \x01(\x0e\x32+.cohesity.magneto.gcp.GCPAttributes.TagType\x12\x1a\n\x0ekey_DEPRECATED\x18\x03 \x01(\tB\x02\x18\x01\x12\x1c\n\x10value_DEPRECATED\x18\x04 \x01(\tB\x02\x18\x01\";\n\x07TagType\x12\x0f\n\x0bkNetworkTag\x10\x00\x12\n\n\x06kLabel\x10\x01\x12\x13\n\x0fkCustomMetadata\x10\x02\"\x9f\t\n\x06\x45ntity\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.cohesity.magneto.gcp.Entity.Type\x12\x10\n\x08owner_id\x18\x02 \x01(\t\x12\x36\n\x08iam_info\x18\x03 \x01(\x0b\x32$.cohesity.magneto.gcp.Entity.IAMInfo\x12=\n\x0b\x63ommon_info\x18\x04 \x01(\x0b\x32(.cohesity.magneto.cloud.EntityCommonInfo\x12\x13\n\x0bvpc_network\x18\x05 \x01(\t\x12\x16\n\x0evpc_subnetwork\x18\x06 \x01(\t\x12\x31\n\thost_type\x18\x07 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type\x12\x1a\n\x12private_ip_address\x18\x08 \x01(\t\x12\x0e\n\x06region\x18\t \x01(\t\x12\x12\n\nproject_id\x18\n \x01(\t\x12\x0c\n\x04zone\x18\x0b \x01(\t\x12\x1e\n\x16\x61llowed_project_id_vec\x18\x0c \x03(\t\x12?\n\x12tag_attributes_vec\x18\x0e \x03(\x0b\x32#.cohesity.magneto.gcp.GCPAttributes\x12\x1a\n\x12\x61llowed_region_vec\x18\x11 \x03(\t\x12\x17\n\x0fhost_project_id\x18\x14 \x01(\t\x12>\n\x10gcp_fleet_params\x18\x15 \x01(\x0b\x32$.cohesity.magneto.gcp.GCPFleetParams\x12T\n\x14\x63luster_network_info\x18\x16 \x01(\x0b\x32\x36.cohesity.magneto.gcp.FleetNetworkParams.NetworkParams\x12\x35\n\rdisk_info_vec\x18\x17 \x03(\x0b\x32\x1e.cohesity.magneto.gcp.DiskInfo\x12H\n\x17metadata_vec_DEPRECATED\x18\x0f \x03(\x0b\x32#.cohesity.magneto.gcp.GCPAttributesB\x02\x18\x01\x12K\n\x1anetwork_tag_vec_DEPRECATED\x18\x10 \x03(\x0b\x32#.cohesity.magneto.gcp.GCPAttributesB\x02\x18\x01\x1a\x33\n\x07IAMInfo\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63lient_email\x18\x02 \x01(\t\"\xd8\x01\n\x04Type\x12\x0c\n\x08kIAMUser\x10\x00\x12\x0c\n\x08kProject\x10\x01\x12\x0b\n\x07kRegion\x10\x02\x12\x15\n\x11kAvailabilityZone\x10\x03\x12\x13\n\x0fkVirtualMachine\x10\x04\x12\x08\n\x04kVPC\x10\x05\x12\x0b\n\x07kSubnet\x10\x06\x12\x19\n\x15kNetworkSecurityGroup\x10\x07\x12\x11\n\rkInstanceType\x10\x08\x12\n\n\x06kLabel\x10\t\x12\r\n\tkMetadata\x10\n\x12\x08\n\x04kTag\x10\x0b\x12\x11\n\rkVPCConnector\x10\x0cJ\x04\x08\r\x10\x0eJ\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14R\x11region_subnet_map\"\xb6\x01\n\x0eGCPFleetParams\x12\x14\n\x0ckms_key_name\x18\x03 \x01(\t\x12\x18\n\x10\x66leet_nw_tag_vec\x18\x04 \x03(\t\x12\x1c\n\x14service_account_name\x18\x05 \x01(\t\x12J\n\x18\x66leet_network_params_vec\x18\x06 \x03(\x0b\x32(.cohesity.magneto.gcp.FleetNetworkParamsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\xfb\x03\n\x12\x46leetNetworkParams\x12S\n\x11\x66leet_subnet_type\x18\x01 \x01(\x0e\x32\x38.cohesity.magneto.gcp.FleetNetworkParams.FleetSubnetType\x12R\n\x12network_params_vec\x18\x02 \x03(\x0b\x32\x36.cohesity.magneto.gcp.FleetNetworkParams.NetworkParams\x12[\n\x15\x66leet_subnet_priority\x18\x03 \x01(\x0e\x32<.cohesity.magneto.gcp.FleetNetworkParams.FleetSubnetPriority\x1a^\n\rNetworkParams\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0b\n\x03vpc\x18\x02 \x01(\t\x12\x0e\n\x06subnet\x18\x03 \x01(\t\x12\x0c\n\x04zone\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\";\n\x0f\x46leetSubnetType\x12\x0c\n\x08kCluster\x10\x01\x12\r\n\tkSourceVM\x10\x02\x12\x0b\n\x07kCustom\x10\x03\"B\n\x13\x46leetSubnetPriority\x12\x0c\n\x08kPrimary\x10\x01\x12\x0e\n\nkSecondary\x10\x02\x12\r\n\tkTertiary\x10\x03\"\x90\x02\n\x08\x44iskInfo\x12\x11\n\tdisk_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x04 \x01(\t\x12\x37\n\tlabel_vec\x18\x06 \x03(\x0b\x32$.cohesity.magneto.gcp.DiskInfo.Label\x12\x0f\n\x07size_gb\x18\x07 \x01(\x03\x12\x11\n\tdisk_type\x18\x08 \x01(\t\x12\x1a\n\x0bis_bootable\x18\t \x01(\x08:\x05\x66\x61lse\x12\n\n\x02id\x18\n \x01(\x03\x1a#\n\x05Label\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06R\nsize_bytesR\x04typeR\x0eis_root_device')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.gcp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GCPATTRIBUTES'].fields_by_name['key_DEPRECATED']._loaded_options = None
  _globals['_GCPATTRIBUTES'].fields_by_name['key_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_GCPATTRIBUTES'].fields_by_name['value_DEPRECATED']._loaded_options = None
  _globals['_GCPATTRIBUTES'].fields_by_name['value_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_ENTITY'].fields_by_name['metadata_vec_DEPRECATED']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['metadata_vec_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_ENTITY'].fields_by_name['network_tag_vec_DEPRECATED']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['network_tag_vec_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_GCPATTRIBUTES']._serialized_start=119
  _globals['_GCPATTRIBUTES']._serialized_end=359
  _globals['_GCPATTRIBUTES_TAGTYPE']._serialized_start=300
  _globals['_GCPATTRIBUTES_TAGTYPE']._serialized_end=359
  _globals['_ENTITY']._serialized_start=362
  _globals['_ENTITY']._serialized_end=1545
  _globals['_ENTITY_IAMINFO']._serialized_start=1238
  _globals['_ENTITY_IAMINFO']._serialized_end=1289
  _globals['_ENTITY_TYPE']._serialized_start=1292
  _globals['_ENTITY_TYPE']._serialized_end=1508
  _globals['_GCPFLEETPARAMS']._serialized_start=1548
  _globals['_GCPFLEETPARAMS']._serialized_end=1730
  _globals['_FLEETNETWORKPARAMS']._serialized_start=1733
  _globals['_FLEETNETWORKPARAMS']._serialized_end=2240
  _globals['_FLEETNETWORKPARAMS_NETWORKPARAMS']._serialized_start=2017
  _globals['_FLEETNETWORKPARAMS_NETWORKPARAMS']._serialized_end=2111
  _globals['_FLEETNETWORKPARAMS_FLEETSUBNETTYPE']._serialized_start=2113
  _globals['_FLEETNETWORKPARAMS_FLEETSUBNETTYPE']._serialized_end=2172
  _globals['_FLEETNETWORKPARAMS_FLEETSUBNETPRIORITY']._serialized_start=2174
  _globals['_FLEETNETWORKPARAMS_FLEETSUBNETPRIORITY']._serialized_end=2240
  _globals['_DISKINFO']._serialized_start=2243
  _globals['_DISKINFO']._serialized_end=2515
  _globals['_DISKINFO_LABEL']._serialized_start=2428
  _globals['_DISKINFO_LABEL']._serialized_end=2463
# @@protoc_insertion_point(module_scope)