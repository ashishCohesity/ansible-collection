# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/physical.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import common_pb2 as magneto_dot_base_dot_common__pb2
from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base.entities import agent_pb2 as magneto_dot_base_dot_entities_dot_agent__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$magneto/base/entities/physical.proto\x12\x19\x63ohesity.magneto.physical\x1a\x19magneto/base/common.proto\x1a\x1fmagneto/agents/base/agent.proto\x1a!magneto/base/entities/agent.proto\x1a\x18magneto/base/enums.proto\":\n\x0bPhysicalUID\x12\r\n\x05part1\x18\x01 \x01(\x03\x12\r\n\x05part2\x18\x02 \x01(\x03\x12\r\n\x05part3\x18\x03 \x01(\x03\"\xf7\x0b\n\x06\x45ntity\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.cohesity.magneto.physical.Entity.Type\x12\x33\n\x03uid\x18\x02 \x01(\x0b\x32&.cohesity.magneto.physical.PhysicalUID\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x31\n\thost_type\x18\x04 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type\x12\x0f\n\x07os_name\x18\x10 \x01(\t\x12\x45\n\x0fvolume_info_vec\x18\x05 \x03(\x0b\x32,.cohesity.magneto.physical.Entity.VolumeInfo\x12\x1c\n\x14unsupported_path_vec\x18\x0b \x03(\t\x12%\n\x17vhdx_recovery_supported\x18\n \x01(\x08:\x04true\x12G\n\x0fnetworking_info\x18\x0c \x01(\x0b\x32..cohesity.magneto.agents.ClusterNetworkingInfo\x12\x41\n\x10\x61gent_status_vec\x18\r \x03(\x0b\x32\'.cohesity.magneto.agent.HostAgentStatus\x12&\n\x1a\x61gent_entity_id_DEPRECATED\x18\x08 \x01(\x03\x42\x02\x18\x01\x12\x42\n\x14system_resource_info\x18\x11 \x01(\x0b\x32$.cohesity.magneto.SystemResourceInfo\x12\x10\n\x08hostname\x18\x12 \x01(\t\x12\x13\n\x0bvcs_version\x18\x13 \x01(\t\x12\x31\n\x0bvlan_params\x18\x14 \x01(\x0b\x32\x1c.cohesity.magneto.VlanParams\x12L\n\x13vss_writer_info_vec\x18\x15 \x03(\x0b\x32/.cohesity.magneto.physical.Entity.VssWriterInfo\x12\x18\n\x10is_proxy_machine\x18\x16 \x01(\x08\x12\x14\n\x0c\x63\x62mr_version\x18\x17 \x01(\t\x12\x17\n\x0fproxy_ref_count\x18\x18 \x01(\x04\x12Y\n\x13\x63luster_source_type\x18\x19 \x01(\x0e\x32<.cohesity.magneto.agents.ClusterNetworkingInfo.Resource.Type\x1a\x98\x03\n\nVolumeInfo\x12\x13\n\x0bvolume_guid\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_path\x18\x07 \x01(\t\x12\x14\n\x0cnetwork_path\x18\x08 \x01(\t\x12\x1a\n\x12logical_size_bytes\x18\x02 \x01(\x04\x12\x17\n\x0fused_size_bytes\x18\x03 \x01(\x04\x12\x17\n\x0fmount_point_vec\x18\x04 \x03(\t\x12\x14\n\x0cvolume_label\x18\x05 \x01(\t\x12\x14\n\x0cis_protected\x18\x06 \x01(\x08\x12%\n\x1d\x65xtended_attributes_supported\x18\t \x01(\x08\x12\x1d\n\x0eis_boot_volume\x18\n \x01(\x08:\x05\x66\x61lse\x12\x12\n\nmount_type\x18\x0b \x01(\t\x12\x18\n\x10is_shared_volume\x18\x0c \x01(\x08\x12\'\n\x18is_cohesity_mount_volume\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0eis_refs_volume\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0cvolume_count\x18\x16 \x01(\x03\x1aL\n\rVssWriterInfo\x12\x17\n\x0fvss_writer_name\x18\x01 \x01(\t\x12\"\n\x13is_default_excluded\x18\x02 \x01(\x08:\x05\x66\x61lse\"_\n\x04Type\x12\n\n\x06kGroup\x10\x00\x12\t\n\x05kHost\x10\x01\x12\x13\n\x0fkWindowsCluster\x10\x02\x12\x15\n\x11kOracleRACCluster\x10\x03\x12\x14\n\x10kOracleAPCluster\x10\x04J\x04\x08\x0e\x10\x0fJ\x04\x08\x06\x10\x07J\x04\x08\t\x10\nJ\x04\x08\x0f\x10\x10')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.physical_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITY'].fields_by_name['agent_entity_id_DEPRECATED']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['agent_entity_id_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_PHYSICALUID']._serialized_start=188
  _globals['_PHYSICALUID']._serialized_end=246
  _globals['_ENTITY']._serialized_start=249
  _globals['_ENTITY']._serialized_end=1776
  _globals['_ENTITY_VOLUMEINFO']._serialized_start=1169
  _globals['_ENTITY_VOLUMEINFO']._serialized_end=1577
  _globals['_ENTITY_VSSWRITERINFO']._serialized_start=1579
  _globals['_ENTITY_VSSWRITERINFO']._serialized_end=1655
  _globals['_ENTITY_TYPE']._serialized_start=1657
  _globals['_ENTITY_TYPE']._serialized_end=1752
# @@protoc_insertion_point(module_scope)
