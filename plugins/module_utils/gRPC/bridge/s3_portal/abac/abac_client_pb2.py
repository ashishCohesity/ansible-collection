# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/s3_portal/abac/abac_client.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'bridge/s3_portal/abac/abac_client.proto\x12\x17\x63ohesity.bridge.s3.abac\"\x1a\n\tClearance\x12\r\n\x05value\x18\x01 \x01(\t\"N\n\x06\x45ntity\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x36\n\nclearances\x18\x02 \x03(\x0b\x32\".cohesity.bridge.s3.abac.Clearance\"G\n\x0cUserResponse\x12\x37\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1f.cohesity.bridge.s3.abac.EntityR\x06\x45ntity\"\x17\n\x06Member\x12\r\n\x05value\x18\x01 \x01(\t\"u\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02\x64n\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12<\n\nmember_vec\x18\x04 \x03(\x0b\x32\x1f.cohesity.bridge.s3.abac.MemberR\x07members\"P\n\x06Groups\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x38\n\tgroup_vec\x18\x02 \x03(\x0b\x32\x1e.cohesity.bridge.s3.abac.GroupR\x05group\"H\n\rGroupResponse\x12\x37\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1f.cohesity.bridge.s3.abac.GroupsR\x06Groups')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.s3_portal.abac.abac_client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLEARANCE']._serialized_start=68
  _globals['_CLEARANCE']._serialized_end=94
  _globals['_ENTITY']._serialized_start=96
  _globals['_ENTITY']._serialized_end=174
  _globals['_USERRESPONSE']._serialized_start=176
  _globals['_USERRESPONSE']._serialized_end=247
  _globals['_MEMBER']._serialized_start=249
  _globals['_MEMBER']._serialized_end=272
  _globals['_GROUP']._serialized_start=274
  _globals['_GROUP']._serialized_end=391
  _globals['_GROUPS']._serialized_start=393
  _globals['_GROUPS']._serialized_end=473
  _globals['_GROUPRESPONSE']._serialized_start=475
  _globals['_GROUPRESPONSE']._serialized_end=547
# @@protoc_insertion_point(module_scope)
