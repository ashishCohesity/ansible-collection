# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/view.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.view_keeper import view_metadata_pb2 as bridge_dot_view__keeper_dot_view__metadata__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17magneto/base/view.proto\x12\x15\x63ohesity.magneto.view\x1a&bridge/view_keeper/view_metadata.proto\x1a\x1amagneto/base/magneto.proto\"\x9d\x02\n\x0cSnapshotInfo\x12\x1d\n\x15source_inode_id_floor\x18\x03 \x01(\x03\x12\x16\n\x0e\x63loned_view_id\x18\x01 \x01(\x03\x12&\n\x1e\x63loned_view_logical_size_bytes\x18\x02 \x01(\x03\x12H\n\x16source_view_id_mapping\x18\x04 \x01(\x0b\x32(.cohesity.bridge.view.ViewIdMappingProto2d\n\x12view_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18\x66 \x01(\x0b\x32#.cohesity.magneto.view.SnapshotInfoB\x16Z\x14magneto/base/view.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024magneto/base/view.pb'
  _globals['_SNAPSHOTINFO']._serialized_start=119
  _globals['_SNAPSHOTINFO']._serialized_end=404
# @@protoc_insertion_point(module_scope)
