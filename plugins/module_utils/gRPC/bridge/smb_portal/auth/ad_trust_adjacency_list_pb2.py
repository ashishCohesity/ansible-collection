# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/smb_portal/auth/ad_trust_adjacency_list.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4bridge/smb_portal/auth/ad_trust_adjacency_list.proto\x12\x13\x63ohesity.bridge.smb\"\xfb\x08\n\x19\x41\x64TrustAdjacencyListProto\x12,\n\x0bgandalf_key\x18\x01 \x01(\t:\x17\x61\x64_trust_adjacency_list\x12^\n\x11member_domain_map\x18\x02 \x03(\x0b\x32\x43.cohesity.bridge.smb.AdTrustAdjacencyListProto.MemberDomainMapEntry\x12`\n\x12primary_domain_map\x18\x03 \x03(\x0b\x32\x44.cohesity.bridge.smb.AdTrustAdjacencyListProto.PrimaryDomainMapEntry\x1a\xf6\x01\n\x0cNeighborInfo\x12\x0c\n\x04\x66qdn\x18\x01 \x01(\t\x12\x66\n\x0ftrust_direction\x18\x02 \x01(\x0e\x32=.cohesity.bridge.smb.AdTrustAdjacencyListProto.TrustDirection:\x0ekBidirectional\x12V\n\ntrust_type\x18\x03 \x01(\x0e\x32\x38.cohesity.bridge.smb.AdTrustAdjacencyListProto.TrustType:\x08kUpLevel\x12\x18\n\x10trust_attributes\x18\x04 \x01(\r\x1a\xb5\x01\n\x0cMemberDomain\x12\x0f\n\x07netbios\x18\x01 \x01(\t\x12\x1a\n\x12\x64istinguished_name\x18\x02 \x01(\t\x12\x0b\n\x03sid\x18\x03 \x01(\t\x12\x13\n\x0b\x65rror_count\x18\x04 \x01(\x04\x12V\n\x11neighbor_info_vec\x18\x05 \x03(\x0b\x32;.cohesity.bridge.smb.AdTrustAdjacencyListProto.NeighborInfo\x1as\n\x14MemberDomainMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.cohesity.bridge.smb.AdTrustAdjacencyListProto.MemberDomain:\x02\x38\x01\x1a@\n\rPrimaryDomain\x12\x18\n\x10update_time_secs\x18\x01 \x01(\x03\x12\x15\n\rtenant_id_vec\x18\x02 \x03(\t\x1au\n\x15PrimaryDomainMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12K\n\x05value\x18\x02 \x01(\x0b\x32<.cohesity.bridge.smb.AdTrustAdjacencyListProto.PrimaryDomain:\x02\x38\x01\"P\n\x0eTrustDirection\x12\r\n\tkDisabled\x10\x00\x12\x0c\n\x08kInbound\x10\x01\x12\r\n\tkOutgoing\x10\x02\x12\x12\n\x0ekBidirectional\x10\x03\"=\n\tTrustType\x12\x0e\n\nkDownLevel\x10\x01\x12\x0c\n\x08kUpLevel\x10\x02\x12\x08\n\x04kMIT\x10\x03\x12\x08\n\x04kDCE\x10\x04')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.smb_portal.auth.ad_trust_adjacency_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAINMAPENTRY']._loaded_options = None
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAINMAPENTRY']._serialized_options = b'8\001'
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAINMAPENTRY']._loaded_options = None
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAINMAPENTRY']._serialized_options = b'8\001'
  _globals['_ADTRUSTADJACENCYLISTPROTO']._serialized_start=78
  _globals['_ADTRUSTADJACENCYLISTPROTO']._serialized_end=1225
  _globals['_ADTRUSTADJACENCYLISTPROTO_NEIGHBORINFO']._serialized_start=348
  _globals['_ADTRUSTADJACENCYLISTPROTO_NEIGHBORINFO']._serialized_end=594
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAIN']._serialized_start=597
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAIN']._serialized_end=778
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAINMAPENTRY']._serialized_start=780
  _globals['_ADTRUSTADJACENCYLISTPROTO_MEMBERDOMAINMAPENTRY']._serialized_end=895
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAIN']._serialized_start=897
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAIN']._serialized_end=961
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAINMAPENTRY']._serialized_start=963
  _globals['_ADTRUSTADJACENCYLISTPROTO_PRIMARYDOMAINMAPENTRY']._serialized_end=1080
  _globals['_ADTRUSTADJACENCYLISTPROTO_TRUSTDIRECTION']._serialized_start=1082
  _globals['_ADTRUSTADJACENCYLISTPROTO_TRUSTDIRECTION']._serialized_end=1162
  _globals['_ADTRUSTADJACENCYLISTPROTO_TRUSTTYPE']._serialized_start=1164
  _globals['_ADTRUSTADJACENCYLISTPROTO_TRUSTTYPE']._serialized_end=1225
# @@protoc_insertion_point(module_scope)