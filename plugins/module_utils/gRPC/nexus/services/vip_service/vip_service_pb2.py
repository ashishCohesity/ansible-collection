# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/services/vip_service/vip_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,nexus/services/vip_service/vip_service.proto\x12\x1b\x63ohesity.nexus.services.vip\"\xee\x03\n\x12VipAssignmentProto\x12$\n\x0bgandalf_key\x18\x01 \x01(\t:\x0fvip_assignments\x12R\n\x0e\x61ssignment_vec\x18\x02 \x03(\x0b\x32:.cohesity.nexus.services.vip.VipAssignmentProto.Assignment\x12\"\n\x16\x63luster_config_version\x18\x03 \x01(\x03:\x02-1\x12 \n\x12vlan_ips_supported\x18\x04 \x01(\x08:\x04true\x1a\x97\x02\n\nAssignment\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12\x0f\n\x07vip_vec\x18\x02 \x03(\t\x12V\n\x0bvlan_ip_vec\x18\x03 \x03(\x0b\x32\x41.cohesity.nexus.services.vip.VipAssignmentProto.Assignment.VlanIp\x1a\x8e\x01\n\x06VlanIp\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0f\n\x07vlan_id\x18\x02 \x02(\x03\x12\x14\n\x0cnetmask_bits\x18\x03 \x02(\x05\x12\x16\n\x0einterface_name\x18\x04 \x01(\t\x12\x13\n\x0brt_table_id\x18\x05 \x01(\x03\x12\x12\n\ngateway_ip\x18\x06 \x01(\t\x12\x10\n\x08\x65\x63mp_vip\x18\x07 \x01(\x08\x42+Z)nexus/services/vip_service/vip_service.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.services.vip_service.vip_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)nexus/services/vip_service/vip_service.pb'
  _globals['_VIPASSIGNMENTPROTO']._serialized_start=78
  _globals['_VIPASSIGNMENTPROTO']._serialized_end=572
  _globals['_VIPASSIGNMENTPROTO_ASSIGNMENT']._serialized_start=293
  _globals['_VIPASSIGNMENTPROTO_ASSIGNMENT']._serialized_end=572
  _globals['_VIPASSIGNMENTPROTO_ASSIGNMENT_VLANIP']._serialized_start=430
  _globals['_VIPASSIGNMENTPROTO_ASSIGNMENT_VLANIP']._serialized_end=572
# @@protoc_insertion_point(module_scope)