# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/ravi/redact_protobuf/sample.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from experimental.ravi.redact_protobuf import redact_util_pb2 as experimental_dot_ravi_dot_redact__protobuf_dot_redact__util__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.experimental/ravi/redact_protobuf/sample.proto\x12\x10\x63ohesity.configs\x1a\x33\x65xperimental/ravi/redact_protobuf/redact_util.proto\"\xb0\x01\n\x0b\x43redentials\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x38\n\x08provider\x18\x02 \x01(\x0b\x32&.cohesity.configs.Credentials.Provider\x1a[\n\x08Provider\x12\x15\n\raccess_key_id\x18\x01 \x01(\t\x12(\n\x1b\x65ncrypted_secret_access_key\x18\x02 \x01(\x0c\x42\x03\x98M\x01\x12\x0e\n\x06region\x18\x03 \x01(\tB\x16\n\x14\x63om.cohesity.configs')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.ravi.redact_protobuf.sample_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.configs'
  _globals['_CREDENTIALS_PROVIDER'].fields_by_name['encrypted_secret_access_key']._loaded_options = None
  _globals['_CREDENTIALS_PROVIDER'].fields_by_name['encrypted_secret_access_key']._serialized_options = b'\230M\001'
  _globals['_CREDENTIALS']._serialized_start=122
  _globals['_CREDENTIALS']._serialized_end=298
  _globals['_CREDENTIALS_PROVIDER']._serialized_start=207
  _globals['_CREDENTIALS_PROVIDER']._serialized_end=298
# @@protoc_insertion_point(module_scope)
