# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/shyamb/helloworld/hello_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2experimental/shyamb/helloworld/hello_service.proto\x12\'cohesity.experimental.shyamb.helloworld\x1a\x1copen_util/net/protorpc.proto\"&\n\x0cHelloRequest\x12\x16\n\x04name\x18\x01 \x01(\t:\x08\x43ohesity\"\x1d\n\x0bHelloResult\x12\x0e\n\x06req_id\x18\x01 \x01(\x05\x32\x95\x01\n\x0cHelloService\x12v\n\x05Greet\x12\x35.cohesity.experimental.shyamb.helloworld.HelloRequest\x1a\x34.cohesity.experimental.shyamb.helloworld.HelloResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.shyamb.helloworld.hello_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_HELLOSERVICE']._loaded_options = None
  _globals['_HELLOSERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_HELLOREQUEST']._serialized_start=125
  _globals['_HELLOREQUEST']._serialized_end=163
  _globals['_HELLORESULT']._serialized_start=165
  _globals['_HELLORESULT']._serialized_end=194
  _globals['_HELLOSERVICE']._serialized_start=197
  _globals['_HELLOSERVICE']._serialized_end=346
# @@protoc_insertion_point(module_scope)
