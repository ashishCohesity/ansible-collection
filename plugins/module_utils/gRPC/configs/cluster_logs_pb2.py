# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/cluster_logs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63onfigs/cluster_logs.proto\"\xc0\x01\n\x10\x43lusterLogsProto\x12&\n\x07log_vec\x18\x01 \x03(\x0b\x32\x15.ClusterLogsProto.Log\x1a\x83\x01\n\x03Log\x12\x17\n\x0ftimestamp_msecs\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12(\n\x04type\x18\x03 \x01(\x0e\x32\x1a.ClusterLogsProto.Log.Type\"(\n\x04Type\x12\x08\n\x04info\x10\x00\x12\x0b\n\x07warning\x10\x01\x12\t\n\x05\x65rror\x10\x02\x42\x19Z\x17\x63onfigs/cluster_logs.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.cluster_logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\027configs/cluster_logs.pb'
  _globals['_CLUSTERLOGSPROTO']._serialized_start=31
  _globals['_CLUSTERLOGSPROTO']._serialized_end=223
  _globals['_CLUSTERLOGSPROTO_LOG']._serialized_start=92
  _globals['_CLUSTERLOGSPROTO_LOG']._serialized_end=223
  _globals['_CLUSTERLOGSPROTO_LOG_TYPE']._serialized_start=183
  _globals['_CLUSTERLOGSPROTO_LOG_TYPE']._serialized_end=223
# @@protoc_insertion_point(module_scope)
