# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/storage/import_export/metadata_internal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.storage import error_pb2 as util_dot_storage_dot_error__pb2
from util.storage.import_export import api_pb2 as util_dot_storage_dot_import__export_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2util/storage/import_export/metadata_internal.proto\x12\x1e\x63ohesity.storage.import_export\x1a\x18util/storage/error.proto\x1a$util/storage/import_export/api.proto\"v\n\x10\x45xportIdentifier\x12\x1a\n\x12service_identifier\x18\x01 \x01(\t\x12\x13\n\x0b\x65xport_usec\x18\x02 \x01(\x03\x12\x1e\n\x16\x65xport_sequence_number\x18\x03 \x01(\x05\x12\x11\n\texport_id\x18\x04 \x01(\t\"\x84\x02\n\x14ImportExportMetadata\x12K\n\x11\x65xport_identifier\x18\x01 \x01(\x0b\x32\x30.cohesity.storage.import_export.ExportIdentifier\x12\x16\n\x0enum_data_files\x18\x02 \x01(\x03\x12\x43\n\rexport_status\x18\x03 \x01(\x0e\x32,.cohesity.storage.import_export.ExportStatus\x12+\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1c.cohesity.storage.ErrorProto\x12\x15\n\rmarked_for_gc\x18\x05 \x01(\x08\"X\n\x06\x43ookie\x12\x18\n\x10import_export_id\x18\x01 \x01(\t\x12\x16\n\x0elast_data_file\x18\x02 \x01(\t\x12\x1c\n\x14last_sequence_number\x18\x03 \x01(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.storage.import_export.metadata_internal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EXPORTIDENTIFIER']._serialized_start=150
  _globals['_EXPORTIDENTIFIER']._serialized_end=268
  _globals['_IMPORTEXPORTMETADATA']._serialized_start=271
  _globals['_IMPORTEXPORTMETADATA']._serialized_end=531
  _globals['_COOKIE']._serialized_start=533
  _globals['_COOKIE']._serialized_end=621
# @@protoc_insertion_point(module_scope)
