# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/storage/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.message_catalog import message_catalog_pb2 as util_dot_message__catalog_dot_message__catalog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18util/storage/error.proto\x12\x10\x63ohesity.storage\x1a*util/message_catalog/message_catalog.proto\"\xfd\x05\n\nErrorProto\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32!.cohesity.storage.ErrorProto.Type:\x08kNoError\x12\x14\n\x0c\x65rror_detail\x18\x02 \x01(\t\x12\x37\n\x12\x64\x65tailed_error_msg\x18\x03 \x01(\x0b\x32\x1b.cohesity.util.MessageProto\"\xe4\x04\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x12\n\x0ekExpectedError\x10\x1b\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kRetry\x10\x03\x12\x0e\n\nkCancelled\x10\x04\x12\x10\n\x0ckNonExistent\x10\x05\x12\x11\n\rkNotDirectory\x10\x06\x12\x10\n\x0ckNameTooLong\x10\x07\x12\x15\n\x11kPermissionDenied\x10\x08\x12\x0c\n\x08kInvalid\x10\t\x12\x11\n\rkNotSupported\x10\n\x12\x13\n\x0fkBufferTooSmall\x10\x0b\x12\x1c\n\x18kSizeExceededSystemLimit\x10\x0c\x12\x14\n\x10kAttrNonExistent\x10\r\x12\x17\n\x13kWindowsSystemError\x10\x0e\x12\n\n\x06kStale\x10\x0f\x12\x12\n\x0ekAlreadyExists\x10\x10\x12\x19\n\x15kClusterMismatchError\x10\x11\x12\x0c\n\x08kFsError\x10\x12\x12\x13\n\x0fkPathNotCovered\x10\x13\x12\x17\n\x13kFetchChildrenError\x10\x14\x12\x0c\n\x08kSkipped\x10\x15\x12\x12\n\x0ekVMwareFsError\x10\x16\x12\x11\n\rkResourceBusy\x10\x17\x12\x15\n\x11kStoppedOnSymlink\x10\x18\x12\x08\n\x04kEOF\x10\x1a\x12\x15\n\x11kSharingViolation\x10\x1c\x12\x0b\n\x07kVosEOF\x10\x1d\x12\x0f\n\x0bkVosFailure\x10\x1e\x12\x14\n\x10kVosIgnoreOffset\x10\x1f\x12\x12\n\x0ekInternalError\x10 B\x16\n\x14\x63om.cohesity.storage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.storage.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.storage'
  _globals['_ERRORPROTO']._serialized_start=91
  _globals['_ERRORPROTO']._serialized_end=856
  _globals['_ERRORPROTO_TYPE']._serialized_start=244
  _globals['_ERRORPROTO_TYPE']._serialized_end=856
# @@protoc_insertion_point(module_scope)