# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/apps/insight/base/common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%athena/apps/insight/base/common.proto\x12\x04\x62\x61se\"t\n\x0eHistogramProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x0b\n\x03sum\x18\x03 \x01(\x03\x12\x16\n\x0esum_of_squares\x18\x04 \x01(\x03\x12\x0f\n\x07min_val\x18\x05 \x01(\x03\x12\x0f\n\x07max_val\x18\x06 \x01(\x03\"}\n\x10MinionStatsProto\x12\x1a\n\x12num_subtasks_total\x18\x01 \x01(\x03\x12 \n\x18num_subtask_errors_total\x18\x02 \x01(\x03\x12+\n\rhistogram_vec\x18\x03 \x03(\x0b\x32\x14.base.HistogramProto\"@\n\x16MinionTcpEndpointProto\x12\x13\n\x0bip_addr_str\x18\x01 \x01(\t\x12\x11\n\tgrpc_port\x18\x02 \x01(\x05\"[\n\x0fMinionInfoProto\x12\x13\n\x0buptime_secs\x18\x01 \x01(\x03\x12\x14\n\x0cmemory_bytes\x18\x02 \x01(\x03\x12\x1d\n\x15per_slot_memory_bytes\x18\x03 \x01(\x03\"L\n\x0c\x43ounterProto\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x14\n\x0cnum_entities\x18\x02 \x01(\x03\x12\x11\n\tnum_bytes\x18\x03 \x01(\x03\x42\x1bZ\x19\x63ohesity/insight_app/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.apps.insight.base.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031cohesity/insight_app/base'
  _globals['_HISTOGRAMPROTO']._serialized_start=47
  _globals['_HISTOGRAMPROTO']._serialized_end=163
  _globals['_MINIONSTATSPROTO']._serialized_start=165
  _globals['_MINIONSTATSPROTO']._serialized_end=290
  _globals['_MINIONTCPENDPOINTPROTO']._serialized_start=292
  _globals['_MINIONTCPENDPOINTPROTO']._serialized_end=356
  _globals['_MINIONINFOPROTO']._serialized_start=358
  _globals['_MINIONINFOPROTO']._serialized_end=449
  _globals['_COUNTERPROTO']._serialized_start=451
  _globals['_COUNTERPROTO']._serialized_end=527
# @@protoc_insertion_point(module_scope)
