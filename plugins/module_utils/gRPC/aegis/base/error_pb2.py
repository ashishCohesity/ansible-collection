# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aegis/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61\x65gis/base/error.proto\x12\x0e\x63ohesity.aegis\"\x9d\x02\n\nErrorProto\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32\x1f.cohesity.aegis.ErrorProto.Type:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\"\xc2\x01\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x11\n\rkRequestError\x10\x01\x12\x10\n\x0ckNonExistent\x10\x02\x12\x0e\n\nkNotMaster\x10\x03\x12\x13\n\x0fkTransportError\x10\x04\x12\x0c\n\x08kTimeout\x10\x05\x12\n\n\x06kRetry\x10\x06\x12\x12\n\x0ekInternalError\x10\x07\x12\x10\n\x0ckMethodError\x10\x08\x12\x11\n\rkServiceError\x10\t\x12\x0f\n\x0bkErrorCount\x10\x10\x42\x15Z\x13\x61\x65gis/base/error.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aegis.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023aegis/base/error.pb'
  _globals['_ERRORPROTO']._serialized_start=43
  _globals['_ERRORPROTO']._serialized_end=328
  _globals['_ERRORPROTO_TYPE']._serialized_start=134
  _globals['_ERRORPROTO_TYPE']._serialized_end=328
# @@protoc_insertion_point(module_scope)
