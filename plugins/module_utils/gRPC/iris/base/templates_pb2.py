# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/templates.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19iris/base/templates.proto\x12\rcohesity.iris\x1a\x1amagneto/base/magneto.proto\"\x9c\x01\n\rTemplateProto\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12 \n\x18last_modified_time_msecs\x18\x05 \x01(\x03\x12:\n\x10template_details\x18\x03 \x02(\x0b\x32 .cohesity.magneto.BackupJobProtoB\x18Z\x16iris/base/templates.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.templates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\026iris/base/templates.pb'
  _globals['_TEMPLATEPROTO']._serialized_start=73
  _globals['_TEMPLATEPROTO']._serialized_end=229
# @@protoc_insertion_point(module_scope)
