# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/failover/failover_WAL.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.failover import failover_state_pb2 as magneto_dot_failover_dot_failover__state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#magneto/failover/failover_WAL.proto\x12\x19\x63ohesity.magneto.failover\x1a%magneto/failover/failover_state.proto\"\xa2\x02\n\x0eWALRecordProto\x12Q\n\x18\x66\x61ilover_service_version\x18\x01 \x01(\x0b\x32/.cohesity.magneto.failover.FailoverVersionProto\x12I\n\x12\x66\x61ilover_state_vec\x18\x02 \x03(\x0b\x32-.cohesity.magneto.failover.FailoverStateProto\x12S\n\x1c\x61\x64\x64_or_update_failover_state\x18\x03 \x01(\x0b\x32-.cohesity.magneto.failover.FailoverStateProto\x12\x1d\n\x15\x64\x65lete_failover_state\x18\x04 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.failover.failover_WAL_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WALRECORDPROTO']._serialized_start=106
  _globals['_WALRECORDPROTO']._serialized_end=396
# @@protoc_insertion_point(module_scope)
