# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/elastifile/elastifile.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.connectors.file import file_pb2 as magneto_dot_connectors_dot_file_dot_file__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.magneto/connectors/elastifile/elastifile.proto\x12\x1b\x63ohesity.magneto.elastifile\x1a\x1amagneto/base/magneto.proto\x1a\"magneto/connectors/file/file.proto\"\xa7\x01\n\x0cSnapshotInfo\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\x05\x12\x10\n\x08share_id\x18\x02 \x01(\x05\x32p\n\x18\x65lastifile_snapshot_info\x12#.cohesity.magneto.file.SnapshotInfo\x18i \x01(\x0b\x32).cohesity.magneto.elastifile.SnapshotInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.elastifile.elastifile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SNAPSHOTINFO']._serialized_start=144
  _globals['_SNAPSHOTINFO']._serialized_end=311
# @@protoc_insertion_point(module_scope)
