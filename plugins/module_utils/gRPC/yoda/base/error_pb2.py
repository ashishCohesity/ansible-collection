# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15yoda/base/error.proto\x12\rcohesity.yoda\"\xdc\x08\n\nErrorProto\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32\x1e.cohesity.yoda.ErrorProto.Type:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\"\x82\x08\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kRetry\x10\x03\x12\x0e\n\nkNotLeader\x10\x04\x12\x0c\n\x08kInvalid\x10\x05\x12\x0c\n\x08kPending\x10\x06\x12\x0f\n\x0bkParseError\x10\x07\x12\x17\n\x13kServiceUnavailable\x10\x08\x12\x11\n\rkAccessDenied\x10\t\x12\x11\n\rkUnknownError\x10\n\x12\x0c\n\x08kCorrupt\x10\x0b\x12\r\n\tkNotFound\x10\x0c\x12\x11\n\rkShardFailure\x10\r\x12\x11\n\rkMountFailure\x10\x0e\x12\x0e\n\nkReadError\x10\x0f\x12\x0c\n\x08kIOError\x10\x10\x12\x1f\n\x1bkOperationNotPermittedError\x10\x11\x12\r\n\tkJVMError\x10\x12\x12\r\n\tkJNIError\x10\x13\x12\x0c\n\x08kFsError\x10\x14\x12\x0e\n\nkCancelled\x10\x15\x12\x0e\n\nkDuplicate\x10\x16\x12\x12\n\x0ekMissingBackup\x10\x17\x12\x19\n\x15kBaseSnapshotNotFound\x10\x18\x12\x14\n\x10kSnapshotExpired\x10\x19\x12\x12\n\x0ekConsumerError\x10\x1a\x12\x0f\n\x0bkNotIndexed\x10\x1b\x12\x18\n\x14kBaseSnapshotExpired\x10\x1c\x12\x0f\n\x0bkOutOfSpace\x10\x1d\x12\x17\n\x13kNoCrackedFileIndex\x10\x1e\x12\x12\n\x0ekNoFsUuidFound\x10\x1f\x12\x1f\n\x1bkSlaveProcessingNotRequired\x10 \x12\n\n\x06kAbort\x10!\x12\x13\n\x0fkStaleSessionId\x10\"\x12\x10\n\x0ckViewDeleted\x10#\x12\r\n\tkReadOnly\x10$\x12\x12\n\x0ekAlreadyExists\x10%\x12\t\n\x05kBusy\x10&\x12\x17\n\x13kParentPathNotFound\x10\'\x12\x15\n\x11kSnapshotNotFound\x10(\x12\x16\n\x12kInvalidDocumentId\x10)\x12\x12\n\x0ekMissingObject\x10*\x12\x10\n\x0ckMissingTags\x10+\x12\x16\n\x12kLibrarianDisabled\x10,\x12\x17\n\x13kNonIndexableEntity\x10-\x12\x1e\n\x1akTenantCloudConfigNotFound\x10.\x12\x18\n\x14kInternalServerError\x10/\x12\x17\n\x13kUnknownBridgeError\x10\x30\x12\x1b\n\x17kSecurityNotInitialized\x10\x31\x12\x0f\n\x0bkAwsESError\x10\x32\x12\x0f\n\x0bkCorruptMFT\x10\x33\x42-\n\x11\x63om.cohesity.yodaZ\x18\x63ohesity/yoda/agent/grpc')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.cohesity.yodaZ\030cohesity/yoda/agent/grpc'
  _globals['_ERRORPROTO']._serialized_start=41
  _globals['_ERRORPROTO']._serialized_end=1157
  _globals['_ERRORPROTO_TYPE']._serialized_start=131
  _globals['_ERRORPROTO_TYPE']._serialized_end=1157
# @@protoc_insertion_point(module_scope)
