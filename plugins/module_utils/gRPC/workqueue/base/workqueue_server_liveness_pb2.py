# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workqueue/base/workqueue_server_liveness.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.workqueue/base/workqueue_server_liveness.proto\x12\x19\x63ohesity.workqueue.server\"\x83\x01\n\rLivenessProto\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x11\n\thttp_port\x18\x03 \x01(\x05\x12\x0f\n\x07node_id\x18\x04 \x01(\x03\x12\x34\n\x1aworkqueue_server_namespace\x18\x05 \x01(\t:\x10workqueue_serverB\x1f\n\x1d\x63om.cohesity.workqueue.server')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workqueue.base.workqueue_server_liveness_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.cohesity.workqueue.server'
  _globals['_LIVENESSPROTO']._serialized_start=78
  _globals['_LIVENESSPROTO']._serialized_end=209
# @@protoc_insertion_point(module_scope)
