# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/stats/disk_usage_stats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#bridge/stats/disk_usage_stats.proto\x12\x15\x63ohesity.bridge.stats\"\xa9\x04\n\x13\x44iskUsageStatsProto\x12H\n\x0cview_box_vec\x18\x01 \x03(\x0b\x32\x32.cohesity.bridge.stats.DiskUsageStatsProto.ViewBox\x12\x41\n\x07garbage\x18\x02 \x01(\x0b\x32\x30.cohesity.bridge.stats.DiskUsageStatsProto.Usage\x12?\n\x05total\x18\x03 \x01(\x0b\x32\x30.cohesity.bridge.stats.DiskUsageStatsProto.Usage\x12\x14\n\x0csystem_usage\x18\x04 \x01(\x03\x12\x17\n\x0fsystem_capacity\x18\x05 \x01(\x03\x1a+\n\x05Usage\x12\x11\n\tunmorphed\x18\x01 \x02(\x03\x12\x0f\n\x07morphed\x18\x02 \x02(\x03\x1a\xe7\x01\n\x07ViewBox\x12\x13\n\x0bview_box_id\x18\x01 \x02(\x03\x12?\n\x05\x64\x65\x64up\x18\x02 \x01(\x0b\x32\x30.cohesity.bridge.stats.DiskUsageStatsProto.Usage\x12\x43\n\tnon_dedup\x18\x03 \x01(\x0b\x32\x30.cohesity.bridge.stats.DiskUsageStatsProto.Usage\x12\x41\n\x07garbage\x18\x04 \x01(\x0b\x32\x30.cohesity.bridge.stats.DiskUsageStatsProto.Usage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.stats.disk_usage_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DISKUSAGESTATSPROTO']._serialized_start=63
  _globals['_DISKUSAGESTATSPROTO']._serialized_end=616
  _globals['_DISKUSAGESTATSPROTO_USAGE']._serialized_start=339
  _globals['_DISKUSAGESTATSPROTO_USAGE']._serialized_end=382
  _globals['_DISKUSAGESTATSPROTO_VIEWBOX']._serialized_start=385
  _globals['_DISKUSAGESTATSPROTO_VIEWBOX']._serialized_end=616
# @@protoc_insertion_point(module_scope)
