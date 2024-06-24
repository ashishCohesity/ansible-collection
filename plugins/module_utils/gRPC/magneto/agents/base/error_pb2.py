# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.message_catalog import message_catalog_pb2 as util_dot_message__catalog_dot_message__catalog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmagneto/agents/base/error.proto\x12\x17\x63ohesity.magneto.agents\x1a*util/message_catalog/message_catalog.proto\"\xef\x07\n\nErrorProto\x12@\n\x04type\x18\x01 \x01(\x0e\x32(.cohesity.magneto.agents.ErrorProto.Type:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x17\n\tretryable\x18\x03 \x01(\x08:\x04true\x12\x37\n\x12\x64\x65tailed_error_msg\x18\x04 \x01(\x0b\x32\x1b.cohesity.util.MessageProto\"\xb9\x06\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x19\n\x15kClusterMismatchError\x10\x01\x12\x0c\n\x08kFsError\x10\x02\x12\x17\n\x13kWindowsSystemError\x10\x03\x12\x0e\n\nkDuplicate\x10\x04\x12\r\n\tkVDIError\x10\x05\x12\r\n\tkSQLError\x10\x06\x12\x10\n\x0ckStreamError\x10\x07\x12\r\n\tkVSSError\x10\x08\x12\x13\n\x0fkTransportError\x10\t\x12\x0c\n\x08kTimeout\x10\n\x12\n\n\x06kRetry\x10\x0b\x12\x0c\n\x08kInvalid\x10\x0c\x12\x0f\n\x0bkParseError\x10\r\x12\x17\n\x13kServiceUnavailable\x10\x0e\x12\x11\n\rkAccessDenied\x10\x0f\x12\r\n\tkNotFound\x10\x10\x12\x0c\n\x08kIOError\x10\x11\x12\x1f\n\x1bkOperationNotPermittedError\x10\x12\x12\x14\n\x10kUnexpectedState\x10\x13\x12\x16\n\x12kTaskMismatchError\x10\x14\x12\x1a\n\x16kInsufficientResources\x10\x15\x12\x13\n\x0fkHyperVCmdError\x10\x16\x12\x0e\n\nkCancelled\x10\x17\x12\x13\n\x0fkNotImplemented\x10\x18\x12\x1d\n\x19kHyperVCmdExceptionThrown\x10\x19\x12\x13\n\x0fkOracleCmdError\x10\x1a\x12\x11\n\rkSysCallError\x10\x1b\x12\x11\n\rkNotSupported\x10\x1c\x12\x13\n\x0fkScriptNotFound\x10\x1d\x12\x1e\n\x1akPowershellExceptionThrown\x10\x1e\x12\x14\n\x10kPowershellError\x10\x1f\x12\x0b\n\x07kExists\x10 \x12\x08\n\x04kSQL\x10!\x12\x14\n\x10kWindowsCOMError\x10\"\x12\x16\n\x12kRemoteSnapFSError\x10#\x12\x14\n\x10kWindowsSMBError\x10$\x12\x19\n\x15kPstConverterLibError\x10%\x12\x1c\n\x18kPstConverterLibMsgError\x10&\x12\x0f\n\x0bkShellError\x10\'\x12\x0c\n\x08kWarning\x10(B\x1d\n\x1b\x63om.cohesity.magneto.agents')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cohesity.magneto.agents'
  _globals['_ERRORPROTO']._serialized_start=105
  _globals['_ERRORPROTO']._serialized_end=1112
  _globals['_ERRORPROTO_TYPE']._serialized_start=287
  _globals['_ERRORPROTO_TYPE']._serialized_end=1112
# @@protoc_insertion_point(module_scope)
