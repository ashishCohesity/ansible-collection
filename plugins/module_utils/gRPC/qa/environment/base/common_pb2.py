# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/environment/base/common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n qa/environment/base/common.proto\x12\x17\x63ohesity.qa.environment\"O\n\x0b\x43redentials\x12\x0b\n\x03oid\x18\x01 \x01(\t\x12\x0f\n\x07oid_ref\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"O\n\nSubnetInfo\x12\x0b\n\x03oid\x18\x01 \x01(\t\x12\x0f\n\x07oid_ref\x18\x02 \x01(\t\x12\x12\n\ngateway_ip\x18\x03 \x01(\t\x12\x0f\n\x07mask_ip\x18\x04 \x01(\tB\x1fZ\x1dqa/environment/base/common.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.environment.base.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035qa/environment/base/common.pb'
  _globals['_CREDENTIALS']._serialized_start=61
  _globals['_CREDENTIALS']._serialized_end=140
  _globals['_SUBNETINFO']._serialized_start=142
  _globals['_SUBNETINFO']._serialized_end=221
# @@protoc_insertion_point(module_scope)
