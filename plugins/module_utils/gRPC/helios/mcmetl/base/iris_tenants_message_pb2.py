# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/mcmetl/base/iris_tenants_message.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from helios.base import helios_cluster_base_pb2 as helios_dot_base_dot_helios__cluster__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-helios/mcmetl/base/iris_tenants_message.proto\x12\x1e\x63ohesity.helios.mcmetl_tenants\x1a%helios/base/helios_cluster_base.proto\"\x8c\x03\n\x11\x43lusterTenantInfo\x12\x43\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\'.cohesity.helios.base.ClusterIdentifier\x12P\n\ntenantInfo\x18\x02 \x03(\x0b\x32<.cohesity.helios.mcmetl_tenants.ClusterTenantInfo.TenantInfo\x1a\xdf\x01\n\nTenantInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08tenantId\x18\x03 \x01(\t\x12\x18\n\x10\x63reatedTimeMsecs\x18\x04 \x01(\x03\x12\x1c\n\x14lastUpdatedTimeMsecs\x18\x05 \x01(\x03\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\x12\x0f\n\x07\x64\x65leted\x18\x07 \x01(\x08\x12\x16\n\x0e\x62ifrostEnabled\x18\x08 \x01(\x08\x12\x17\n\x0f\x63lusterHostname\x18\t \x01(\t\x12\x12\n\nclusterIps\x18\n \x03(\tB,Z*helios/mcmetl/base/iris_tenants_message.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.mcmetl.base.iris_tenants_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*helios/mcmetl/base/iris_tenants_message.pb'
  _globals['_CLUSTERTENANTINFO']._serialized_start=121
  _globals['_CLUSTERTENANTINFO']._serialized_end=517
  _globals['_CLUSTERTENANTINFO_TENANTINFO']._serialized_start=294
  _globals['_CLUSTERTENANTINFO_TENANTINFO']._serialized_end=517
# @@protoc_insertion_point(module_scope)
