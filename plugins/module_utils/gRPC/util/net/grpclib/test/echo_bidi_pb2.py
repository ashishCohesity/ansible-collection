# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/net/grpclib/test/echo_bidi.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%util/net/grpclib/test/echo_bidi.proto\x12\x14\x63ohesity.echoservice\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1copen_util/net/protorpc.proto\"%\n\x13\x45\x63hoNumberStreamArg\x12\x0e\n\x06number\x18\x01 \x01(\x03\"(\n\x16\x45\x63hoNumberStreamResult\x12\x0e\n\x06number\x18\x02 \x01(\x03\x32}\n\x08\x45\x63hoBidi\x12q\n\x10\x45\x63hoNumberStream\x12).cohesity.echoservice.EchoNumberStreamArg\x1a,.cohesity.echoservice.EchoNumberStreamResult\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.net.grpclib.test.echo_bidi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ECHONUMBERSTREAMARG']._serialized_start=125
  _globals['_ECHONUMBERSTREAMARG']._serialized_end=162
  _globals['_ECHONUMBERSTREAMRESULT']._serialized_start=164
  _globals['_ECHONUMBERSTREAMRESULT']._serialized_end=204
  _globals['_ECHOBIDI']._serialized_start=206
  _globals['_ECHOBIDI']._serialized_end=331
# @@protoc_insertion_point(module_scope)
