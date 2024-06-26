# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/isilon.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"magneto/base/entities/isilon.proto\x12\x17\x63ohesity.magneto.isilon\"0\n\x10NetworkInterface\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08ip_addrs\x18\x02 \x03(\t\"\x81\x01\n\x0b\x43lusterInfo\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x17\n\x0f\x61pi_version_str\x18\x06 \x01(\t\x12\x19\n\x11smb_krb5_hostname\x18\x07 \x01(\tJ\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06\"\xd6\x05\n\x08ZoneInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07zone_id\x18\x02 \x01(\x03\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x10\n\x08groupnet\x18\x04 \x01(\t\x12\x44\n\rnetwork_pools\x18\x05 \x03(\x0b\x32-.cohesity.magneto.isilon.ZoneInfo.NetworkPool\x1a\xc6\x04\n\x0bNetworkPool\x12\x13\n\x0b\x61\x63\x63\x65ss_zone\x18\x01 \x01(\t\x12g\n\x0b\x61\x64\x64r_family\x18\x02 \x01(\x0e\x32;.cohesity.magneto.isilon.ZoneInfo.NetworkPool.AddressFamily:\x15kUnknownAddressFamily\x12\x64\n\x0c\x61lloc_method\x18\x08 \x01(\x0e\x32\x39.cohesity.magneto.isilon.ZoneInfo.NetworkPool.AllocMethod:\x13kUnknownAllocMethod\x12\x10\n\x08groupnet\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x43\n\x06ranges\x18\x05 \x03(\x0b\x32\x33.cohesity.magneto.isilon.ZoneInfo.NetworkPool.Range\x12\x13\n\x0bsc_dns_zone\x18\x06 \x01(\t\x12\x0e\n\x06subnet\x18\x07 \x01(\t\x1a\"\n\x05Range\x12\x0b\n\x03low\x18\x01 \x01(\t\x12\x0c\n\x04high\x18\x02 \x01(\t\"@\n\rAddressFamily\x12\x19\n\x15kUnknownAddressFamily\x10\x00\x12\t\n\x05kIPv4\x10\x01\x12\t\n\x05kIPv6\x10\x02\"W\n\x0b\x41llocMethod\x12\x17\n\x13kUnknownAllocMethod\x10\x00\x12\x16\n\x12kStaticAllocMethod\x10\x01\x12\x17\n\x13kDynamicAllocMethod\x10\x02\"\xaf\x03\n\x0eMountPointInfo\x12L\n\x16supported_protocol_vec\x18\x01 \x03(\x0e\x32,.cohesity.magneto.isilon.MountPointInfo.Type\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x45\n\x0csmb_info_vec\x18\x03 \x03(\x0b\x32/.cohesity.magneto.isilon.MountPointInfo.SmbInfo\x12\x41\n\x08nfs_info\x18\x04 \x01(\x0b\x32/.cohesity.magneto.isilon.MountPointInfo.NfsInfo\x12\x0f\n\x07zone_id\x18\x05 \x01(\t\x12\x10\n\x08groupnet\x18\x06 \x01(\t\x1a;\n\x07SmbInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\x03\x1a;\n\x07NfsInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\"\x1a\n\x04Type\x12\x08\n\x04kNfs\x10\x00\x12\x08\n\x04kSmb\x10\x01\"\xb1\x02\n\x06\x45ntity\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.cohesity.magneto.isilon.Entity.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x0c\x63luster_info\x18\x03 \x01(\x0b\x32$.cohesity.magneto.isilon.ClusterInfo\x12\x34\n\tzone_info\x18\x04 \x01(\x0b\x32!.cohesity.magneto.isilon.ZoneInfo\x12\x41\n\x10mount_point_info\x18\x05 \x01(\x0b\x32\'.cohesity.magneto.isilon.MountPointInfo\"0\n\x04Type\x12\x0c\n\x08kCluster\x10\x00\x12\t\n\x05kZone\x10\x01\x12\x0f\n\x0bkMountPoint\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.isilon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NETWORKINTERFACE']._serialized_start=63
  _globals['_NETWORKINTERFACE']._serialized_end=111
  _globals['_CLUSTERINFO']._serialized_start=114
  _globals['_CLUSTERINFO']._serialized_end=243
  _globals['_ZONEINFO']._serialized_start=246
  _globals['_ZONEINFO']._serialized_end=972
  _globals['_ZONEINFO_NETWORKPOOL']._serialized_start=390
  _globals['_ZONEINFO_NETWORKPOOL']._serialized_end=972
  _globals['_ZONEINFO_NETWORKPOOL_RANGE']._serialized_start=783
  _globals['_ZONEINFO_NETWORKPOOL_RANGE']._serialized_end=817
  _globals['_ZONEINFO_NETWORKPOOL_ADDRESSFAMILY']._serialized_start=819
  _globals['_ZONEINFO_NETWORKPOOL_ADDRESSFAMILY']._serialized_end=883
  _globals['_ZONEINFO_NETWORKPOOL_ALLOCMETHOD']._serialized_start=885
  _globals['_ZONEINFO_NETWORKPOOL_ALLOCMETHOD']._serialized_end=972
  _globals['_MOUNTPOINTINFO']._serialized_start=975
  _globals['_MOUNTPOINTINFO']._serialized_end=1406
  _globals['_MOUNTPOINTINFO_SMBINFO']._serialized_start=1258
  _globals['_MOUNTPOINTINFO_SMBINFO']._serialized_end=1317
  _globals['_MOUNTPOINTINFO_NFSINFO']._serialized_start=1319
  _globals['_MOUNTPOINTINFO_NFSINFO']._serialized_end=1378
  _globals['_MOUNTPOINTINFO_TYPE']._serialized_start=1380
  _globals['_MOUNTPOINTINFO_TYPE']._serialized_end=1406
  _globals['_ENTITY']._serialized_start=1409
  _globals['_ENTITY']._serialized_end=1714
  _globals['_ENTITY_TYPE']._serialized_start=1666
  _globals['_ENTITY_TYPE']._serialized_end=1714
# @@protoc_insertion_point(module_scope)
