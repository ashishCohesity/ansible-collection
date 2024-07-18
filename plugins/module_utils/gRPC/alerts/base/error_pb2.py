# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alerts/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61lerts/base/error.proto\x12\x0f\x63ohesity.alerts\"\x8f\x03\n\nErrorProto\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32 .cohesity.alerts.ErrorProto.Type:\x08kNoError\x12\x13\n\terror_msg\x18\x02 \x01(\t:\x00\"\xb1\x02\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kRetry\x10\x03\x12\x15\n\x11kUnknownAlertType\x10\x04\x12\x10\n\x0ckUnavailable\x10\x05\x12\x17\n\x13kNotificationFailed\x10\x06\x12\x0e\n\nkNotMaster\x10\x07\x12\x19\n\x15kAlertAlreadyResolved\x10\x08\x12\x15\n\x11kInvalidArguments\x10\t\x12\x0c\n\x08kDropped\x10\n\x12\x13\n\x0bkErrorCount\x10\x0b\x1a\x02\x08\x01\x12\x12\n\x0ekInternalError\x10\x0c\x12\x16\n\x12kInvalidWebHookUrl\x10\r\x12\x19\n\x15kInvalidWebHookOption\x10\x0e\x42\x16Z\x14\x61lerts/base/error.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'alerts.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024alerts/base/error.pb'
  _globals['_ERRORPROTO_TYPE'].values_by_name["kErrorCount"]._loaded_options = None
  _globals['_ERRORPROTO_TYPE'].values_by_name["kErrorCount"]._serialized_options = b'\010\001'
  _globals['_ERRORPROTO']._serialized_start=45
  _globals['_ERRORPROTO']._serialized_end=444
  _globals['_ERRORPROTO_TYPE']._serialized_start=139
  _globals['_ERRORPROTO_TYPE']._serialized_end=444
# @@protoc_insertion_point(module_scope)