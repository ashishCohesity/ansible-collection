# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bifrost/server/bifrost_http_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bifrost.base import error_pb2 as bifrost_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bifrost/server/bifrost_http_service.proto\x12\x10\x63ohesity.bifrost\x1a\x18\x62ifrost/base/error.proto\"\x88\x02\n\x16\x42ifrostHttpConfigProto\x12.\n\x1dupload_configuration_file_url\x18\x01 \x01(\t:\x07/upload\x12\x1a\n\x0fstatus_page_url\x18\x02 \x01(\t:\x01/\x12(\n\x12get_hyx_health_url\x18\x03 \x01(\t:\x0c/hyx_healthz\x12O\n)download_agent_installer_from_cluster_url\x18\x04 \x01(\t:\x1c/download_agent_from_cluster\x12\'\n\x12get_hyx_config_url\x18\x05 \x01(\t:\x0b/hyx_config\"C\n\x1b\x44ownloadAgentFromClusterArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x12\n\nsha512_sum\x18\x02 \x01(\x0c\"y\n\x1e\x44ownloadAgentFromClusterResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.ErrorProto\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x19\n\x11\x64ownload_filepath\x18\x03 \x01(\tB(Z&bifrost/server/bifrost_http_service.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bifrost.server.bifrost_http_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&bifrost/server/bifrost_http_service.pb'
  _globals['_BIFROSTHTTPCONFIGPROTO']._serialized_start=90
  _globals['_BIFROSTHTTPCONFIGPROTO']._serialized_end=354
  _globals['_DOWNLOADAGENTFROMCLUSTERARG']._serialized_start=356
  _globals['_DOWNLOADAGENTFROMCLUSTERARG']._serialized_end=423
  _globals['_DOWNLOADAGENTFROMCLUSTERRESULT']._serialized_start=425
  _globals['_DOWNLOADAGENTFROMCLUSTERRESULT']._serialized_end=546
# @@protoc_insertion_point(module_scope)
