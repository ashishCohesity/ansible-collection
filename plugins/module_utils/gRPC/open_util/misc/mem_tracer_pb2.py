# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/misc/mem_tracer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fopen_util/misc/mem_tracer.proto\x12\rcohesity.misc\"\xf9\x05\n\x0eMemTracerProto\x12Q\n\x13\x63omponent_value_map\x18\x01 \x03(\x0b\x32\x34.cohesity.misc.MemTracerProto.ComponentValueMapEntry\x1a\xaf\x04\n\nValueProto\x12N\n\x0cop_value_map\x18\x01 \x03(\x0b\x32\x38.cohesity.misc.MemTracerProto.ValueProto.OpValueMapEntry\x1a\xeb\x02\n\x07OpProto\x12^\n\x10\x62ucket_value_map\x18\x01 \x03(\x0b\x32\x44.cohesity.misc.MemTracerProto.ValueProto.OpProto.BucketValueMapEntry\x1a\x8a\x01\n\x0b\x42ucketProto\x12\x17\n\x0fnum_data_points\x18\x01 \x02(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x03\x12\x0e\n\x06median\x18\x03 \x01(\x03\x12\x12\n\neighty_ptl\x18\x06 \x01(\x03\x12\x17\n\x0fninety_five_ptl\x18\x04 \x01(\x03\x12\x17\n\x0fninety_nine_ptl\x18\x05 \x01(\x03\x1as\n\x13\x42ucketValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12K\n\x05value\x18\x02 \x01(\x0b\x32<.cohesity.misc.MemTracerProto.ValueProto.OpProto.BucketProto:\x02\x38\x01\x1a\x63\n\x0fOpValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.cohesity.misc.MemTracerProto.ValueProto.OpProto:\x02\x38\x01\x1a\x62\n\x16\x43omponentValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.cohesity.misc.MemTracerProto.ValueProto:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.misc.mem_tracer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETVALUEMAPENTRY']._loaded_options = None
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETVALUEMAPENTRY']._serialized_options = b'8\001'
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPVALUEMAPENTRY']._loaded_options = None
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPVALUEMAPENTRY']._serialized_options = b'8\001'
  _globals['_MEMTRACERPROTO_COMPONENTVALUEMAPENTRY']._loaded_options = None
  _globals['_MEMTRACERPROTO_COMPONENTVALUEMAPENTRY']._serialized_options = b'8\001'
  _globals['_MEMTRACERPROTO']._serialized_start=51
  _globals['_MEMTRACERPROTO']._serialized_end=812
  _globals['_MEMTRACERPROTO_VALUEPROTO']._serialized_start=153
  _globals['_MEMTRACERPROTO_VALUEPROTO']._serialized_end=712
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO']._serialized_start=248
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO']._serialized_end=611
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETPROTO']._serialized_start=356
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETPROTO']._serialized_end=494
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETVALUEMAPENTRY']._serialized_start=496
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPPROTO_BUCKETVALUEMAPENTRY']._serialized_end=611
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPVALUEMAPENTRY']._serialized_start=613
  _globals['_MEMTRACERPROTO_VALUEPROTO_OPVALUEMAPENTRY']._serialized_end=712
  _globals['_MEMTRACERPROTO_COMPONENTVALUEMAPENTRY']._serialized_start=714
  _globals['_MEMTRACERPROTO_COMPONENTVALUEMAPENTRY']._serialized_end=812
# @@protoc_insertion_point(module_scope)
