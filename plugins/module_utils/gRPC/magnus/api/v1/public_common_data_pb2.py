# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magnus/api/v1/public_common_data.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magnus.api.protoc_gen_openapiv2.options import annotations_pb2 as magnus_dot_api_dot_protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magnus/api/v1/public_common_data.proto\x12\x16\x63ohesity.magnus.api.v1\x1a\x39magnus/api/protoc-gen-openapiv2/options/annotations.proto\"\xd6\x01\n\x0b\x43redentials\x12:\n\x08username\x18\x01 \x01(\tB(\x92\x41%2#Username to use for authentication.\x12M\n\x08password\x18\x02 \x01(\x0c\x42;\x92\x41\x38\x32\x36Password to use for authentication in base64 encoding.:<\x92\x41\x39\n7*\x0b\x43redentials2(Credentials to authenticate to a system.B\x1fZ\x1d\x63ohesity/magnus/api/v1;magnus')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magnus.api.v1.public_common_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035cohesity/magnus/api/v1;magnus'
  _globals['_CREDENTIALS'].fields_by_name['username']._loaded_options = None
  _globals['_CREDENTIALS'].fields_by_name['username']._serialized_options = b'\222A%2#Username to use for authentication.'
  _globals['_CREDENTIALS'].fields_by_name['password']._loaded_options = None
  _globals['_CREDENTIALS'].fields_by_name['password']._serialized_options = b'\222A826Password to use for authentication in base64 encoding.'
  _globals['_CREDENTIALS']._loaded_options = None
  _globals['_CREDENTIALS']._serialized_options = b'\222A9\n7*\013Credentials2(Credentials to authenticate to a system.'
  _globals['_CREDENTIALS']._serialized_start=126
  _globals['_CREDENTIALS']._serialized_end=340
# @@protoc_insertion_point(module_scope)
