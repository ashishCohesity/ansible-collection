# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stats/base/stats_types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cstats/base/stats_types.proto\x12\x0e\x63ohesity.stats\"\x89\x02\n\x05Value\x12(\n\x04type\x18\x01 \x02(\x0e\x32\x1a.cohesity.stats.Value.Type\x12(\n\x04\x64\x61ta\x18\x02 \x02(\x0b\x32\x1a.cohesity.stats.Value.Data\x1ar\n\x04\x44\x61ta\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x04 \x01(\x0cH\x00\x42\x0c\n\noneof_data\"8\n\x04Type\x12\n\n\x06kInt64\x10\x00\x12\x0b\n\x07kDouble\x10\x01\x12\x0b\n\x07kString\x10\x02\x12\n\n\x06kBytes\x10\x03\"A\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x02(\t\x12$\n\x05value\x18\x02 \x02(\x0b\x32\x15.cohesity.stats.ValueB\x10Z\x0e\x63ohesity/stats')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats.base.stats_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\016cohesity/stats'
  _globals['_VALUE']._serialized_start=49
  _globals['_VALUE']._serialized_end=314
  _globals['_VALUE_DATA']._serialized_start=142
  _globals['_VALUE_DATA']._serialized_end=256
  _globals['_VALUE_TYPE']._serialized_start=258
  _globals['_VALUE_TYPE']._serialized_end=314
  _globals['_KEYVALUEPAIR']._serialized_start=316
  _globals['_KEYVALUEPAIR']._serialized_end=381
# @@protoc_insertion_point(module_scope)