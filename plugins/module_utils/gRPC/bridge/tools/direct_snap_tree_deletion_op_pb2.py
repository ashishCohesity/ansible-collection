# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/tools/direct_snap_tree_deletion_op.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.directory_walker import directory_walker_pb2 as magneto_dot_directory__walker_dot_directory__walker__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bridge/tools/direct_snap_tree_deletion_op.proto\x12\x0f\x63ohesity.bridge\x1a/magneto/directory_walker/directory_walker.proto\"G\n\x10\x44\x65letionEntities\x12\x19\n\x11root_snap_tree_id\x18\x01 \x01(\x03\x12\x18\n\x10snaptree_key_vec\x18\x02 \x03(\x03\"\xab\x02\n\x13\x43heckpointInfoProto\x12H\n\x13last_visited_entity\x18\x01 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12L\n\x0f\x64\x65letion_status\x18\x02 \x01(\x0e\x32\x33.cohesity.bridge.CheckpointInfoProto.DeletionStatus\x12$\n\x1cnext_offset_in_deletion_file\x18\x03 \x01(\x03\"V\n\x0e\x44\x65letionStatus\x12\x15\n\x11kPhase1InProgress\x10\x00\x12\x15\n\x11kPhase2InProgress\x10\x01\x12\x16\n\x12kCleanupInProgress\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.tools.direct_snap_tree_deletion_op_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DELETIONENTITIES']._serialized_start=117
  _globals['_DELETIONENTITIES']._serialized_end=188
  _globals['_CHECKPOINTINFOPROTO']._serialized_start=191
  _globals['_CHECKPOINTINFOPROTO']._serialized_end=490
  _globals['_CHECKPOINTINFOPROTO_DELETIONSTATUS']._serialized_start=404
  _globals['_CHECKPOINTINFOPROTO_DELETIONSTATUS']._serialized_end=490
# @@protoc_insertion_point(module_scope)
