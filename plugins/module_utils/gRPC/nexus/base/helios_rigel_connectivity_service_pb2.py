# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/helios_rigel_connectivity_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2nexus/base/helios_rigel_connectivity_service.proto\x12\x04pipe\"#\n\x14\x43heckConnectivityArg\x12\x0b\n\x03msg\x18\x01 \x01(\t\"&\n\x17\x43heckConnectivityResult\x12\x0b\n\x03msg\x18\x01 \x01(\t2j\n\x18RigelConnectivityService\x12N\n\x11\x43heckConnectivity\x12\x1a.pipe.CheckConnectivityArg\x1a\x1d.pipe.CheckConnectivityResultB(Z&nexus/base/heliosRigelConnectivityStubb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.helios_rigel_connectivity_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&nexus/base/heliosRigelConnectivityStub'
  _globals['_CHECKCONNECTIVITYARG']._serialized_start=60
  _globals['_CHECKCONNECTIVITYARG']._serialized_end=95
  _globals['_CHECKCONNECTIVITYRESULT']._serialized_start=97
  _globals['_CHECKCONNECTIVITYRESULT']._serialized_end=135
  _globals['_RIGELCONNECTIVITYSERVICE']._serialized_start=137
  _globals['_RIGELCONNECTIVITYSERVICE']._serialized_end=243
# @@protoc_insertion_point(module_scope)