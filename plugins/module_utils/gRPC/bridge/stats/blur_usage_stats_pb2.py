# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/stats/blur_usage_stats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#bridge/stats/blur_usage_stats.proto\x12\x15\x63ohesity.bridge.stats\"\xd9\x04\n\x13\x42lurUsageStatsProto\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12\x11\n\tnum_blobs\x18\x02 \x01(\x05\x12Z\n\x0eview_usage_vec\x18\x03 \x03(\x0b\x32\x42.cohesity.bridge.stats.BlurUsageStatsProto.BlurViewUsageStatsProto\x12\x61\n\x12view_box_usage_vec\x18\x04 \x03(\x0b\x32\x45.cohesity.bridge.stats.BlurUsageStatsProto.BlurViewBoxUsageStatsProto\x12Z\n\x0e\x64isk_usage_vec\x18\x05 \x03(\x0b\x32\x42.cohesity.bridge.stats.BlurUsageStatsProto.BlurDiskUsageStatsProto\x1aS\n\x17\x42lurViewUsageStatsProto\x12\x0f\n\x07view_id\x18\x01 \x01(\x03\x12\x13\n\x0busage_bytes\x18\x02 \x01(\x03\x12\x12\n\nnum_epochs\x18\x03 \x01(\x05\x1aY\n\x1a\x42lurViewBoxUsageStatsProto\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x12\n\nused_bytes\x18\x02 \x01(\x03\x12\x12\n\nnum_epochs\x18\x03 \x01(\x05\x1aS\n\x17\x42lurDiskUsageStatsProto\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\x03\x12\x13\n\x0busage_bytes\x18\x02 \x01(\x03\x12\x12\n\nnum_epochs\x18\x03 \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.stats.blur_usage_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BLURUSAGESTATSPROTO']._serialized_start=63
  _globals['_BLURUSAGESTATSPROTO']._serialized_end=664
  _globals['_BLURUSAGESTATSPROTO_BLURVIEWUSAGESTATSPROTO']._serialized_start=405
  _globals['_BLURUSAGESTATSPROTO_BLURVIEWUSAGESTATSPROTO']._serialized_end=488
  _globals['_BLURUSAGESTATSPROTO_BLURVIEWBOXUSAGESTATSPROTO']._serialized_start=490
  _globals['_BLURUSAGESTATSPROTO_BLURVIEWBOXUSAGESTATSPROTO']._serialized_end=579
  _globals['_BLURUSAGESTATSPROTO_BLURDISKUSAGESTATSPROTO']._serialized_start=581
  _globals['_BLURUSAGESTATSPROTO_BLURDISKUSAGESTATSPROTO']._serialized_end=664
# @@protoc_insertion_point(module_scope)