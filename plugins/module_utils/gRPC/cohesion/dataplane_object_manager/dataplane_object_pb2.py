# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cohesion/dataplane_object_manager/dataplane_object.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cohesion.base import common_pb2 as cohesion_dot_base_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8cohesion/dataplane_object_manager/dataplane_object.proto\x12\x15\x63ohesity.cohesion.dom\x1a\x1a\x63ohesion/base/common.proto\"\xbc\x02\n\x11ObjectParamsProto\x12>\n\x0estorage_handle\x18\x01 \x01(\x0b\x32&.cohesity.cohesion.BackupStorageHandle\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\x12\x42\n\x04mode\x18\x03 \x01(\x0e\x32-.cohesity.cohesion.dom.ObjectParamsProto.Mode:\x05kNone\x12\x43\n\x13\x62\x61se_storage_handle\x18\x04 \x01(\x0b\x32&.cohesity.cohesion.BackupStorageHandle\x12\x11\n\tupload_id\x18\x05 \x01(\t\"6\n\x04Mode\x12\t\n\x05kNone\x10\x00\x12\x0b\n\x07kCreate\x10\x01\x12\t\n\x05kRead\x10\x02\x12\x0b\n\x07kUpdate\x10\x03\"I\n\x13ObjectMetadataProto\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x01(\x03\x12\x17\n\x0fobject_checksum\x18\x02 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cohesion.dataplane_object_manager.dataplane_object_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OBJECTPARAMSPROTO']._serialized_start=112
  _globals['_OBJECTPARAMSPROTO']._serialized_end=428
  _globals['_OBJECTPARAMSPROTO_MODE']._serialized_start=374
  _globals['_OBJECTPARAMSPROTO_MODE']._serialized_end=428
  _globals['_OBJECTMETADATAPROTO']._serialized_start=430
  _globals['_OBJECTMETADATAPROTO']._serialized_end=503
# @@protoc_insertion_point(module_scope)