# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/apps/insight/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$athena/apps/insight/base/error.proto\x12\x04\x62\x61se\"\xd9\x02\n\nErrorProto\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.base.ErrorProto.Type\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"\x95\x02\n\x04Type\x12\x15\n\x11kInvalidEnumValue\x10\x00\x12\x0c\n\x08kNoError\x10\x01\x12\x13\n\x0fkDirWalkerError\x10\x02\x12\x18\n\x14kDirWalkerFatalError\x10\x03\x12\x19\n\x15kDirectoryDifferError\x10\x04\x12\x14\n\x10kTaskRunnerError\x10\x05\x12\x10\n\x0ckMinionError\x10\x06\x12\x0f\n\x0bkMountError\x10\x07\x12\x0c\n\x08kIOError\x10\x08\x12\x11\n\rkElasticError\x10\t\x12\r\n\tkCanceled\x10\n\x12\x14\n\x10kValidationError\x10\x0b\x12\x10\n\x0ckNonExistent\x10\x0c\x12\r\n\tkApiError\x10\rB\x1bZ\x19\x63ohesity/insight_app/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.apps.insight.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031cohesity/insight_app/base'
  _globals['_ERRORPROTO']._serialized_start=47
  _globals['_ERRORPROTO']._serialized_end=392
  _globals['_ERRORPROTO_TYPE']._serialized_start=115
  _globals['_ERRORPROTO_TYPE']._serialized_end=392
# @@protoc_insertion_point(module_scope)
