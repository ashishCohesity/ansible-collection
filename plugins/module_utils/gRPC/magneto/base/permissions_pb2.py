# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/permissions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from stats.base import stats_types_pb2 as stats_dot_base_dot_stats__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emagneto/base/permissions.proto\x12\x10\x63ohesity.magneto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x1cstats/base/stats_types.proto\"\xc0\x02\n\x14\x45ntityPermissionInfo\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12\x46\n\x0bpermissions\x18\x02 \x03(\x0b\x32\x31.cohesity.magneto.EntityPermissionInfo.Permission\x12\x11\n\ttenant_id\x18\x03 \x01(\t\x12\x13\n\x0bis_inferred\x18\x04 \x01(\x08\x12\x1d\n\x15registering_tenant_id\x18\x05 \x01(\t\x12\x1b\n\x13is_registered_by_sp\x18\x06 \x01(\x08\x12$\n\x1clast_modification_time_usecs\x18\x07 \x01(\x03\x1a\x43\n\nPermission\x12\x35\n\x03sid\x18\x01 \x01(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\"\xc7\x01\n\x0fUserInformation\x12\x39\n\x13pulse_attribute_vec\x18\x01 \x03(\x0b\x32\x1c.cohesity.stats.KeyValuePair\x12\x39\n\x07sid_vec\x18\x02 \x03(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\x12\x15\n\rtenant_id_vec\x18\x03 \x03(\t\x12\'\n\x19include_subtenant_objects\x18\x04 \x01(\x08:\x04true')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.permissions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITYPERMISSIONINFO']._serialized_start=113
  _globals['_ENTITYPERMISSIONINFO']._serialized_end=433
  _globals['_ENTITYPERMISSIONINFO_PERMISSION']._serialized_start=366
  _globals['_ENTITYPERMISSIONINFO_PERMISSION']._serialized_end=433
  _globals['_USERINFORMATION']._serialized_start=436
  _globals['_USERINFORMATION']._serialized_end=635
# @@protoc_insertion_point(module_scope)
