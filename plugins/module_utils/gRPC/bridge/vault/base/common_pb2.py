# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/vault/base/common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x62ridge/vault/base/common.proto\x12\x15\x63ohesity.bridge.vault\"\'\n\x10MonitoringCookie\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\"Q\n\x0e\x43oldTierCookie\x12!\n\x19last_object_creation_secs\x18\x01 \x01(\x03\x12\x1c\n\x14is_restore_initiated\x18\x02 \x01(\x08\"F\n\nWormCookie\x12\x19\n\x11object_version_id\x18\x01 \x01(\t\x12\x1d\n\x15retention_period_secs\x18\x02 \x01(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.vault.base.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MONITORINGCOOKIE']._serialized_start=57
  _globals['_MONITORINGCOOKIE']._serialized_end=96
  _globals['_COLDTIERCOOKIE']._serialized_start=98
  _globals['_COLDTIERCOOKIE']._serialized_end=179
  _globals['_WORMCOOKIE']._serialized_start=181
  _globals['_WORMCOOKIE']._serialized_end=251
# @@protoc_insertion_point(module_scope)
