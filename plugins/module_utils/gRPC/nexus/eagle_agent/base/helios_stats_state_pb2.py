# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/eagle_agent/base/helios_stats_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/nexus/eagle_agent/base/helios_stats_state.proto\x12\x1b\x63ohesity.nexus.helios.stats\"\x89\x01\n\x13StatsCollectionInfo\x12\x1e\n\x16start_collection_usecs\x18\x01 \x01(\x03\x12\x1c\n\x14\x65nd_collection_usecs\x18\x02 \x01(\x03\x12\x15\n\rslider_length\x18\x03 \x01(\x03\x12\x1d\n\x15slider_length_minutes\x18\x04 \x01(\x03\"x\n\x10StatsBatchObject\x12\x12\n\nstats_data\x18\x01 \x01(\x0c\x12P\n\x16stats_collection_state\x18\x02 \x01(\x0b\x32\x30.cohesity.nexus.helios.stats.StatsCollectionInfoB.Z,nexus/eagle_agent/base/helios_stats_state.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.eagle_agent.base.helios_stats_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,nexus/eagle_agent/base/helios_stats_state.pb'
  _globals['_STATSCOLLECTIONINFO']._serialized_start=81
  _globals['_STATSCOLLECTIONINFO']._serialized_end=218
  _globals['_STATSBATCHOBJECT']._serialized_start=220
  _globals['_STATSBATCHOBJECT']._serialized_end=340
# @@protoc_insertion_point(module_scope)
