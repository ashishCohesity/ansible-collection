# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata_service/application/api/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_service.api import api_pb2 as metadata__service_dot_api_dot_api__pb2
from metadata_service.base import error_pb2 as metadata__service_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*metadata_service/application/api/api.proto\x12)cohesity.metadata_service.application.api\x1a\x1emetadata_service/api/api.proto\x1a!metadata_service/base/error.proto\"c\n\x16NotifyDetachedNodesArg\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12\x37\n\x05nodes\x18\x02 \x03(\x0b\x32(.cohesity.metadata_service.api.NodeProto\"\x8f\x01\n\x19NotifyDetachedNodesResult\x12\x39\n\x05\x65rror\x18\x01 \x01(\x0b\x32*.cohesity.metadata_service.base.ErrorProto\x12\x37\n\x05nodes\x18\x02 \x03(\x0b\x32(.cohesity.metadata_service.api.NodeProtoB+Z)cohesity/metadata_service/application/api')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metadata_service.application.api.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)cohesity/metadata_service/application/api'
  _globals['_NOTIFYDETACHEDNODESARG']._serialized_start=156
  _globals['_NOTIFYDETACHEDNODESARG']._serialized_end=255
  _globals['_NOTIFYDETACHEDNODESRESULT']._serialized_start=258
  _globals['_NOTIFYDETACHEDNODESRESULT']._serialized_end=401
# @@protoc_insertion_point(module_scope)
