# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/storage/import_export/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.storage import error_pb2 as util_dot_storage_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$util/storage/import_export/api.proto\x12\x1e\x63ohesity.storage.import_export\x1a\x18util/storage/error.proto*)\n\x0c\x45xportStatus\x12\x0c\n\x08kSuccess\x10\x01\x12\x0b\n\x07kFailed\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.storage.import_export.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EXPORTSTATUS']._serialized_start=98
  _globals['_EXPORTSTATUS']._serialized_end=139
# @@protoc_insertion_point(module_scope)
