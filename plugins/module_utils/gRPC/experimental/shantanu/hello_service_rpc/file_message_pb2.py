# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/shantanu/hello_service_rpc/file_message.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:experimental/shantanu/hello_service_rpc/file_message.proto\x12\x1e\x63ohesity.experimental.shantanu\x1a\x1copen_util/net/protorpc.proto\"!\n\x0cHelloRequest\x12\x11\n\x03msg\x18\x01 \x01(\t:\x04Hey!\"!\n\rHelloResponse\x12\x10\n\x08response\x18\x01 \x01(\t2y\n\x0cHelloService\x12i\n\x08SayHello\x12,.cohesity.experimental.shantanu.HelloRequest\x1a-.cohesity.experimental.shantanu.HelloResponse\"\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.shantanu.hello_service_rpc.file_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=124
  _globals['_HELLOREQUEST']._serialized_end=157
  _globals['_HELLORESPONSE']._serialized_start=159
  _globals['_HELLORESPONSE']._serialized_end=192
  _globals['_HELLOSERVICE']._serialized_start=194
  _globals['_HELLOSERVICE']._serialized_end=315
# @@protoc_insertion_point(module_scope)