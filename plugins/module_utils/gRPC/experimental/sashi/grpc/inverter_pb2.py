# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/sashi/grpc/inverter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&experimental/sashi/grpc/inverter.proto\x12\x19\x63ohesity.util.net.grpclib\"\x1d\n\x0bInverterArg\x12\x0e\n\x06number\x18\x01 \x01(\x05\" \n\x0eInverterResult\x12\x0e\n\x06number\x18\x01 \x01(\x05\x32\xb8\x02\n\x0fInverterService\x12\x61\n\x06RpcOne\x12&.cohesity.util.net.grpclib.InverterArg\x1a).cohesity.util.net.grpclib.InverterResult\"\x00(\x01\x30\x01\x12\x61\n\x06RpcTwo\x12&.cohesity.util.net.grpclib.InverterArg\x1a).cohesity.util.net.grpclib.InverterResult\"\x00(\x01\x30\x01\x12_\n\x08RpcThree\x12&.cohesity.util.net.grpclib.InverterArg\x1a).cohesity.util.net.grpclib.InverterResult\"\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.sashi.grpc.inverter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INVERTERARG']._serialized_start=69
  _globals['_INVERTERARG']._serialized_end=98
  _globals['_INVERTERRESULT']._serialized_start=100
  _globals['_INVERTERRESULT']._serialized_end=132
  _globals['_INVERTERSERVICE']._serialized_start=135
  _globals['_INVERTERSERVICE']._serialized_end=447
# @@protoc_insertion_point(module_scope)
