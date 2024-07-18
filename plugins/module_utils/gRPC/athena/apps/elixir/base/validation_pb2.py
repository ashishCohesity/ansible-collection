# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/apps/elixir/base/validation.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.appspec import appspec_pb2 as util_dot_appspec_dot_appspec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(athena/apps/elixir/base/validation.proto\x12\x04\x62\x61se\x1a\x1autil/appspec/appspec.proto\"\xce\x01\n\x13ValidationInfoProto\x12\x31\n\x0bresource_id\x18\x01 \x01(\x0b\x32\x1c.cohesity.appspec.Identifier\x12\x34\n\x08severity\x18\x02 \x01(\x0e\x32\".base.ValidationInfoProto.Severity\x12\x0f\n\x07summary\x18\x03 \x01(\t\"=\n\x08Severity\x12\x0c\n\x08kUnknown\x10\x00\x12\t\n\x05kInfo\x10\x01\x12\x0c\n\x08kWarning\x10\x02\x12\n\n\x06kError\x10\x03\"\xd0\x02\n\x15ValidationResultProto\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0brunbook_uid\x18\x02 \x01(\t\x12\x36\n\x13validation_info_vec\x18\x03 \x03(\x0b\x32\x19.base.ValidationInfoProto\x12\x32\n\x06result\x18\x04 \x01(\x0e\x32\".base.ValidationResultProto.Result\x12\x14\n\x0c\x61ppspec_json\x18\x05 \x01(\t\x12\x18\n\x10start_time_usecs\x18\x06 \x01(\x03\x12\x16\n\x0e\x65nd_time_usecs\x18\x07 \x01(\x03\"b\n\x06Result\x12\x0f\n\x0bkInProgress\x10\x00\x12\x0c\n\x08kSuccess\x10\x01\x12\x0c\n\x08kFailure\x10\x02\x12\x0c\n\x08kWarning\x10\x03\x12\r\n\tkCanceled\x10\x04\x12\x0e\n\nkCanceling\x10\x05\x42\x1aZ\x18\x63ohesity/elixir_app/base')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.apps.elixir.base.validation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/elixir_app/base'
  _globals['_VALIDATIONINFOPROTO']._serialized_start=79
  _globals['_VALIDATIONINFOPROTO']._serialized_end=285
  _globals['_VALIDATIONINFOPROTO_SEVERITY']._serialized_start=224
  _globals['_VALIDATIONINFOPROTO_SEVERITY']._serialized_end=285
  _globals['_VALIDATIONRESULTPROTO']._serialized_start=288
  _globals['_VALIDATIONRESULTPROTO']._serialized_end=624
  _globals['_VALIDATIONRESULTPROTO_RESULT']._serialized_start=526
  _globals['_VALIDATIONRESULTPROTO_RESULT']._serialized_end=624
# @@protoc_insertion_point(module_scope)