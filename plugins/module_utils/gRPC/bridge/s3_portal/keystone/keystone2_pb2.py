# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/s3_portal/keystone/keystone2.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bridge/s3_portal/keystone/keystone2.proto\x12\x1b\x63ohesity.bridge.s3.keystone\"5\n\x05Links\x12\x0c\n\x04self\x18\x01 \x01(\t\x12\x10\n\x08previous\x18\x02 \x01(\t\x12\x0c\n\x04next\x18\x03 \x01(\t\"{\n\x06\x44omain\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x31\n\x05links\x18\x05 \x01(\x0b\x32\".cohesity.bridge.s3.keystone.Links\"k\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\x06\x64omain\x18\x03 \x01(\x0b\x32#.cohesity.bridge.s3.keystone.Domain\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"\x97\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x1b\n\x13password_expires_at\x18\x04 \x01(\t\x12\x33\n\x06\x64omain\x18\x05 \x01(\x0b\x32#.cohesity.bridge.s3.keystone.Domain\x12\x11\n\tdomain_id\x18\x06 \x01(\t\"v\n\x06Region\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x31\n\x05links\x18\x03 \x01(\x0b\x32\".cohesity.bridge.s3.keystone.Links\x12\x18\n\x10parent_region_id\x18\x04 \x01(\tB!\n\x1f\x63om.cohesity.bridge.s3.keystone')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.s3_portal.keystone.keystone2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.cohesity.bridge.s3.keystone'
  _globals['_LINKS']._serialized_start=74
  _globals['_LINKS']._serialized_end=127
  _globals['_DOMAIN']._serialized_start=129
  _globals['_DOMAIN']._serialized_end=252
  _globals['_PROJECT']._serialized_start=254
  _globals['_PROJECT']._serialized_end=361
  _globals['_USER']._serialized_start=364
  _globals['_USER']._serialized_end=515
  _globals['_REGION']._serialized_start=517
  _globals['_REGION']._serialized_end=635
# @@protoc_insertion_point(module_scope)