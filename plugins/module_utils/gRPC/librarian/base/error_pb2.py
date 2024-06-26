# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: librarian/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1alibrarian/base/error.proto\x12\x12\x63ohesity.librarian\"\xd7\x07\n\nErrorProto\x12;\n\x04type\x18\x01 \x01(\x0e\x32#.cohesity.librarian.ErrorProto.Type:\x08kNoError\x12\x14\n\x0c\x65rror_detail\x18\x02 \x01(\t\"\xf5\x06\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kStale\x10\x03\x12\x10\n\x0ckNonExistent\x10\x04\x12\n\n\x06kRetry\x10\x05\x12\x0e\n\nkNotLeader\x10\x06\x12\x12\n\x0ekAlreadyExists\x10\x07\x12\x0c\n\x08kInvalid\x10\x08\x12\x15\n\x11kPermissionDenied\x10\t\x12\x0f\n\x0bkOutOfSpace\x10\n\x12\x0e\n\nkBadCookie\x10\x0b\x12\x0c\n\x08kCorrupt\x10\x0c\x12\x0c\n\x08kFsError\x10\r\x12\x11\n\rkNotSupported\x10\x0e\x12\r\n\tkCanceled\x10\x0f\x12\x13\n\x0fkNotEnoughNodes\x10\x10\x12\x0c\n\x08kIOError\x10\x11\x12\x11\n\rkUnknownError\x10\x12\x12\x13\n\x0fkDeleteExisting\x10\x13\x12\r\n\tkReadOnly\x10\x14\x12\x0c\n\x08kPending\x10\x15\x12\x0f\n\x0bkParseError\x10\x16\x12\x17\n\x13kServiceUnavailable\x10\x17\x12\x0f\n\x0bkNotUpdated\x10\x18\x12\n\n\x06kAbort\x10\x19\x12\x13\n\x0fkStaleSessionId\x10\x1a\x12\x1a\n\x16kSlaveConfigNotUpdated\x10\x1b\x12\x0f\n\x0bkForceIndex\x10\x1c\x12\x1b\n\x17kIndexableFieldsChanged\x10\x1d\x12\t\n\x05kBusy\x10\x1e\x12\x1e\n\x1akLuceneserverInternalError\x10\x1f\x12\x10\n\x0ckStaleCookie\x10 \x12\x1e\n\x1akBucketReplicasUnavailable\x10!\x12\x1f\n\x1bkTagOpOnNonExistentDocument\x10\"\x12\x1f\n\x1bkTagOpOnNonExistentSnapshot\x10#\x12\x19\n\x15kTagOpInvalidArgument\x10$\x12\x19\n\x15kLuceneMaxClauseCount\x10+\x12\x1a\n\x16kReassignmentNotNeeded\x10%\x12\r\n\tkReassign\x10&\x12\x18\n\x14kESDocIdSizeExceeded\x10\'\x12\x1e\n\x1akESBulkRequestSizeExceeded\x10(\x12\x11\n\rkDiskNotFound\x10)\x12\x0f\n\x0bkAwsESError\x10*B1\n\x16\x63om.cohesity.librarianZ\x17librarian/base/error.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'librarian.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cohesity.librarianZ\027librarian/base/error.pb'
  _globals['_ERRORPROTO']._serialized_start=51
  _globals['_ERRORPROTO']._serialized_end=1034
  _globals['_ERRORPROTO_TYPE']._serialized_start=149
  _globals['_ERRORPROTO_TYPE']._serialized_end=1034
# @@protoc_insertion_point(module_scope)
