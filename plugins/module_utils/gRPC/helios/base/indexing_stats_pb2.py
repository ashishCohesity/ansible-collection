# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/base/indexing_stats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n helios/base/indexing_stats.proto\x12\x1d\x63ohesity.helios.indexingstats\"\x97\x01\n\x19IndexingStatsKafkaMessage\x12\x12\n\ncluster_id\x18\x01 \x01(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x02 \x01(\x03\x12\x15\n\rsf_account_id\x18\x03 \x01(\t\x12\x16\n\x0eindexing_stats\x18\x04 \x01(\x0c\x12\x17\n\x0fis_unregistered\x18\x05 \x01(\x08\x42\x1fZ\x1d\x63ohesity/helios/indexingstatsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.base.indexing_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035cohesity/helios/indexingstats'
  _globals['_INDEXINGSTATSKAFKAMESSAGE']._serialized_start=68
  _globals['_INDEXINGSTATSKAFKAMESSAGE']._serialized_end=219
# @@protoc_insertion_point(module_scope)