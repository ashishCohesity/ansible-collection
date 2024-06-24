# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/mcmetl/base/mcmetl_rest_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from helios.base import helios_cluster_base_pb2 as helios_dot_base_dot_helios__cluster__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,helios/mcmetl/base/mcmetl_rest_service.proto\x12#cohesity.helios.mcmetl_rest_service\x1a%helios/base/helios_cluster_base.proto\"\xbe\x01\n\x0f\x43\x61\x63heRequestArg\x12V\n\x0brequest_vec\x18\x01 \x03(\x0b\x32\x41.cohesity.helios.mcmetl_rest_service.CacheRequestArg.CacheRequest\x1aS\n\x0c\x43\x61\x63heRequest\x12\x43\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\'.cohesity.helios.base.ClusterIdentifier\"\xe1\x02\n\rCacheResponse\x12R\n\nresult_vec\x18\x01 \x03(\x0b\x32>.cohesity.helios.mcmetl_rest_service.CacheResponse.CacheResult\x1a\xfb\x01\n\x0b\x43\x61\x63heResult\x12\x43\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\'.cohesity.helios.base.ClusterIdentifier\x12U\n\x06status\x18\x02 \x01(\x0e\x32\x45.cohesity.helios.mcmetl_rest_service.CacheResponse.CacheResult.Status\x12\x0e\n\x06output\x18\x03 \x01(\t\x12\x1a\n\x12total_object_count\x18\x04 \x01(\x03\"$\n\x06Status\x12\x0c\n\x08kSuccess\x10\x00\x12\x0c\n\x08kFailure\x10\x01\"\xc7\x01\n\x13McmEtlRestUrisProto\x12\x1f\n\x10mcmetl_rest_port\x18\x01 \x01(\x05:\x05\x32\x33\x34\x36\x32\x12\x18\n\x0b\x61pi_version\x18\x02 \x01(\t:\x03/v1\x12\x19\n\tcache_uri\x18\x03 \x01(\t:\x06/cache\x12-\n\x13mcm_tag_updates_uri\x18\x04 \x01(\t:\x10/mcm_tag_updates\x12+\n\x12gc_tag_updates_uri\x18\x05 \x01(\t:\x0f/gc_tag_updatesB+Z)helios/mcmetl/base/mcmetl_rest_service.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.mcmetl.base.mcmetl_rest_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)helios/mcmetl/base/mcmetl_rest_service.pb'
  _globals['_CACHEREQUESTARG']._serialized_start=125
  _globals['_CACHEREQUESTARG']._serialized_end=315
  _globals['_CACHEREQUESTARG_CACHEREQUEST']._serialized_start=232
  _globals['_CACHEREQUESTARG_CACHEREQUEST']._serialized_end=315
  _globals['_CACHERESPONSE']._serialized_start=318
  _globals['_CACHERESPONSE']._serialized_end=671
  _globals['_CACHERESPONSE_CACHERESULT']._serialized_start=420
  _globals['_CACHERESPONSE_CACHERESULT']._serialized_end=671
  _globals['_CACHERESPONSE_CACHERESULT_STATUS']._serialized_start=635
  _globals['_CACHERESPONSE_CACHERESULT_STATUS']._serialized_end=671
  _globals['_MCMETLRESTURISPROTO']._serialized_start=674
  _globals['_MCMETLRESTURISPROTO']._serialized_end=873
# @@protoc_insertion_point(module_scope)
