# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/postgres/postgres.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*magneto/connectors/postgres/postgres.proto\x12\x19\x63ohesity.magneto.postgres\"*\n\x06\x44\x42Info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x03\"S\n\x07\x44\x42sInfo\x12\x10\n\x08\x64\x62_count\x18\x01 \x01(\x05\x12\x36\n\x0b\x64\x62_info_vec\x18\x02 \x03(\x0b\x32!.cohesity.magneto.postgres.DBInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.postgres.postgres_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DBINFO']._serialized_start=73
  _globals['_DBINFO']._serialized_end=115
  _globals['_DBSINFO']._serialized_start=117
  _globals['_DBSINFO']._serialized_end=200
# @@protoc_insertion_point(module_scope)
