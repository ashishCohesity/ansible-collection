# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/sheltered-harbor/roles/common/proto/grpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4nexus/sheltered-harbor/roles/common/proto/grpc.proto\x12\x1e\x63ohesity.nexus.shelteredharbor\"P\n\x0b\x43ommonError\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0f\n\x07summary\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x04 \x01(\t\"/\n\x0eListParameters\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\"e\n\x0fTLSBootstrapReq\x12\x12\n\njoin_token\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63luster_name\x18\x03 \x01(\t\x12\x14\n\x0ctrust_bundle\x18\x04 \x01(\t\"\x8e\x02\n\x11TLSBootstrapReply\x12:\n\x05\x65rror\x18\x01 \x01(\x0b\x32+.cohesity.nexus.shelteredharbor.CommonError\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63luster_name\x18\x03 \x01(\t\x12S\n\x0c\x63luster_type\x18\x04 \x01(\x0e\x32=.cohesity.nexus.shelteredharbor.TLSBootstrapReply.ClusterType\x12\x14\n\x0ctrust_bundle\x18\x05 \x01(\t\"(\n\x0b\x43lusterType\x12\x0b\n\x07PRIMARY\x10\x00\x12\x0c\n\x08RECOVERY\x10\x01*T\n\x0eOperationState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07WAITING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x0e\n\nCOMPELETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x42\x34Z2cohesity/nexus/sheltered-harbor/roles/common/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.sheltered_harbor.roles.common.proto.grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2cohesity/nexus/sheltered-harbor/roles/common/proto'
  _globals['_OPERATIONSTATE']._serialized_start=595
  _globals['_OPERATIONSTATE']._serialized_end=679
  _globals['_COMMONERROR']._serialized_start=88
  _globals['_COMMONERROR']._serialized_end=168
  _globals['_LISTPARAMETERS']._serialized_start=170
  _globals['_LISTPARAMETERS']._serialized_end=217
  _globals['_TLSBOOTSTRAPREQ']._serialized_start=219
  _globals['_TLSBOOTSTRAPREQ']._serialized_end=320
  _globals['_TLSBOOTSTRAPREPLY']._serialized_start=323
  _globals['_TLSBOOTSTRAPREPLY']._serialized_end=593
  _globals['_TLSBOOTSTRAPREPLY_CLUSTERTYPE']._serialized_start=553
  _globals['_TLSBOOTSTRAPREPLY_CLUSTERTYPE']._serialized_end=593
# @@protoc_insertion_point(module_scope)
