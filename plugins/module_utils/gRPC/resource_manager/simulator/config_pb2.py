# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource_manager/simulator/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'resource_manager/simulator/config.proto\x12#cohesity.resource_manager.simulator\"W\n\x0fPolicySpecProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10time_period_secs\x18\x02 \x01(\x05\x12\x1e\n\x16\x62\x61\x63kup_start_time_secs\x18\x03 \x01(\x05\"\xed\x04\n\x0f\x45ntitySpecProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\x04type\x18\x02 \x01(\x0e\x32\x39.cohesity.resource_manager.simulator.EntitySpecProto.Type\x12M\n\x03\x65nv\x18\r \x01(\x0e\x32@.cohesity.resource_manager.simulator.EntitySpecProto.Environment\x12\x1b\n\ttenant_id\x18\x0e \x01(\t:\x08tenant_1\x12\x14\n\x0clogical_size\x18\x03 \x01(\x03\x12\x1f\n\x17\x64\x61ta_source_entity_name\x18\x04 \x01(\t\x12\x11\n\tpolicy_id\x18\x05 \x01(\t\x12\x19\n\x11sla_duration_secs\x18\x06 \x01(\x05\x12\x13\n\x08priority\x18\x07 \x01(\x05:\x01\x31\x12\x1e\n\x16\x64\x61ily_change_rate_mean\x18\x08 \x01(\x01\x12 \n\x18\x64\x61ily_change_rate_stddev\x18\t \x01(\x01\x12\x1f\n\x13num_data_read_slots\x18\n \x01(\x05:\x02\x31\x32\x12*\n\x16max_read_bytes_per_sec\x18\x0b \x01(\x03:\n4294967296\x12+\n\x17max_write_bytes_per_sec\x18\x0c \x01(\x03:\n1073741824\"\"\n\x04Type\x12\t\n\x05kLeaf\x10\x01\x12\x0f\n\x0bkDataSource\x10\x02\"=\n\x0b\x45nvironment\x12\x0c\n\x08kInvalid\x10\x00\x12\x0b\n\x07kVMware\x10\x01\x12\t\n\x05kO365\x10\x02\x12\x08\n\x04kNAS\x10\x03\"\xe5\x01\n\x10\x43lusterSpecProto\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tnum_nodes\x18\x02 \x01(\x05\x12H\n\npolicy_vec\x18\x03 \x03(\x0b\x32\x34.cohesity.resource_manager.simulator.PolicySpecProto\x12H\n\nentity_vec\x18\x04 \x03(\x0b\x32\x34.cohesity.resource_manager.simulator.EntitySpecProto\x12\x16\n\x0bnum_tenants\x18\x05 \x01(\x05:\x01\x31')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resource_manager.simulator.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_POLICYSPECPROTO']._serialized_start=80
  _globals['_POLICYSPECPROTO']._serialized_end=167
  _globals['_ENTITYSPECPROTO']._serialized_start=170
  _globals['_ENTITYSPECPROTO']._serialized_end=791
  _globals['_ENTITYSPECPROTO_TYPE']._serialized_start=694
  _globals['_ENTITYSPECPROTO_TYPE']._serialized_end=728
  _globals['_ENTITYSPECPROTO_ENVIRONMENT']._serialized_start=730
  _globals['_ENTITYSPECPROTO_ENVIRONMENT']._serialized_end=791
  _globals['_CLUSTERSPECPROTO']._serialized_start=794
  _globals['_CLUSTERSPECPROTO']._serialized_end=1023
# @@protoc_insertion_point(module_scope)
