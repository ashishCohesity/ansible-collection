# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/amandeep/grpc/stub/grpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2experimental/amandeep/grpc/stub/grpc_service.proto\x12\x1e\x63ohesity.experimental.amandeep\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2u\n\x0bGrpcService\x12\x66\n\x08SayHello\x12,.cohesity.experimental.amandeep.HelloRequest\x1a*.cohesity.experimental.amandeep.HelloReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.amandeep.grpc.stub.grpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=86
  _globals['_HELLOREQUEST']._serialized_end=114
  _globals['_HELLOREPLY']._serialized_start=116
  _globals['_HELLOREPLY']._serialized_end=145
  _globals['_GRPCSERVICE']._serialized_start=147
  _globals['_GRPCSERVICE']._serialized_end=264
# @@protoc_insertion_point(module_scope)