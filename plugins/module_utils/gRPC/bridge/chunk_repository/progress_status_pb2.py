# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/chunk_repository/progress_status.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-bridge/chunk_repository/progress_status.proto\x12\x1a\x63ohesity.bridge.chunk_repo\x1a\x1c\x63onfigs/cluster_config.proto\"\x82\x03\n\x10MigrateWALStatus\x12\x0f\n\x07\x64isk_id\x18\x01 \x02(\x03\x12W\n\x0fsource_location\x18\x02 \x01(\x0e\x32>.cohesity.configs.ClusterConfigProto.Disk.ChunkRepoWALLocation\x12\x1a\n\x12source_incarnation\x18\x03 \x01(\x03\x12W\n\x0ftarget_location\x18\x04 \x01(\x0e\x32>.cohesity.configs.ClusterConfigProto.Disk.ChunkRepoWALLocation\x12\x1a\n\x12target_incarnation\x18\x05 \x01(\x03\x12 \n\x18\x61ll_chunk_files_migrated\x18\x06 \x01(\x08\x12\x1a\n\x12resume_from_cookie\x18\x07 \x01(\t\x12 \n\x18num_chunk_files_migrated\x18\x08 \x01(\x03\x12\x13\n\x0bstart_usecs\x18\t \x01(\x03\"B\n\x08GCStatus\x12\x0f\n\x07\x64isk_id\x18\x01 \x02(\x03\x12%\n\x1dgc_complete_until_incarnation\x18\x02 \x02(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.chunk_repository.progress_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MIGRATEWALSTATUS']._serialized_start=108
  _globals['_MIGRATEWALSTATUS']._serialized_end=494
  _globals['_GCSTATUS']._serialized_start=496
  _globals['_GCSTATUS']._serialized_end=562
# @@protoc_insertion_point(module_scope)