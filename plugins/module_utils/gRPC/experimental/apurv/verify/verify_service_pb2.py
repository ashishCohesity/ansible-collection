# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/apurv/verify/verify_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.experimental/apurv/verify/verify_service.proto\x12\"cohesity.experimental.apurv.verify\x1a\x1copen_util/net/protorpc.proto\"E\n\rVerifyRequest\x12\x10\n\x08\x66ilepath\x18\x01 \x02(\t\x12\x0e\n\x06length\x18\x02 \x02(\x03\x12\x12\n\npage_seeds\x18\x03 \x03(\x05\"\x1f\n\x0cVerifyResult\x12\x0f\n\x07\x63orrupt\x18\x01 \x01(\x08\x32\x90\x01\n\rVerifyService\x12o\n\x06Verify\x12\x31.cohesity.experimental.apurv.verify.VerifyRequest\x1a\x30.cohesity.experimental.apurv.verify.VerifyResult\"\x00\x1a\x0e\x80\xf1\x04\xc0\xcf$\x88\xf1\x04\x01\x90\xf1\x04\x01\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.apurv.verify.verify_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_VERIFYSERVICE']._loaded_options = None
  _globals['_VERIFYSERVICE']._serialized_options = b'\200\361\004\300\317$\210\361\004\001\220\361\004\001'
  _globals['_VERIFYREQUEST']._serialized_start=116
  _globals['_VERIFYREQUEST']._serialized_end=185
  _globals['_VERIFYRESULT']._serialized_start=187
  _globals['_VERIFYRESULT']._serialized_end=218
  _globals['_VERIFYSERVICE']._serialized_start=221
  _globals['_VERIFYSERVICE']._serialized_end=365
# @@protoc_insertion_point(module_scope)
