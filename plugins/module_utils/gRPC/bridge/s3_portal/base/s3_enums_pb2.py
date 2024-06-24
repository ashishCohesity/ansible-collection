# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/s3_portal/base/s3_enums.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$bridge/s3_portal/base/s3_enums.proto\x12\x12\x63ohesity.bridge.s3\"\xdb\r\n\x07Request\"\xcf\r\n\x04Type\x12\x0c\n\x08kUnKnown\x10\x00\x12\x11\n\rkS3GetBuckets\x10\x01\x12\x13\n\x0fkS3GetBucketACL\x10\x02\x12\x16\n\x12kS3UpdateBucketACL\x10\x03\x12\x1c\n\x18kS3MultipleDeleteObjects\x10\x04\x12\x17\n\x13kS3GetBucketTagging\x10\x05\x12\x1a\n\x16kS3UpdateBucketTagging\x10\x06\x12\x1a\n\x16kS3DeleteBucketTagging\x10\x07\x12\x19\n\x15kS3ListObjectVersions\x10\x08\x12\x1a\n\x16kS3GetBucketVersioning\x10\t\x12\x1d\n\x19kS3UpdateBucketVersioning\x10\n\x12\x1b\n\x17kS3ListMultiPartUploads\x10\x0b\x12\x12\n\x0ekS3ListObjects\x10\x0c\x12\x11\n\rkS3HeadBucket\x10\r\x12\x13\n\x0fkS3CreateBucket\x10\x0e\x12\x13\n\x0fkS3DeleteBucket\x10\x0f\x12\x18\n\x14kS3GetBucketLocation\x10\x1b\x12!\n\x1dkS3GetObjectLockConfiguration\x10!\x12$\n kS3UpdateObjectLockConfiguration\x10\"\x12&\n\"kS3GetBucketLifecycleConfiguration\x10#\x12)\n%kS3UpdateBucketLifecycleConfiguration\x10$\x12)\n%kS3DeleteBucketLifecycleConfiguration\x10%\x12\x16\n\x12kS3GetBucketPolicy\x10&\x12\x19\n\x15kS3UpdateBucketPolicy\x10\'\x12\x19\n\x15kS3DeleteBucketPolicy\x10(\x12!\n\x1dkS3GetBucketOwnershipControls\x10\x42\x12$\n kS3UpdateBucketOwnershipControls\x10\x43\x12$\n kS3DeleteBucketOwnershipControls\x10\x44\x12\x1a\n\x16kS3InitMultiPartUpload\x10\x10\x12\x16\n\x12kS3ListObjectParts\x10\x11\x12\x17\n\x13kS3UploadObjectPart\x10\x12\x12\x1e\n\x1akS3CompleteMultiPartUpload\x10\x13\x12\x1b\n\x17kS3AbortMultiPartUpload\x10\x14\x12\x10\n\x0ckS3GetObject\x10\x15\x12\x18\n\x14kS3GetObjectMetadata\x10\x16\x12\x13\n\x0fkS3CreateObject\x10\x17\x12\x13\n\x0fkS3DeleteObject\x10\x18\x12\x13\n\x0fkS3GetObjectACL\x10\x19\x12\x16\n\x12kS3UpdateObjectACL\x10\x1a\x12\x11\n\rkS3CopyObject\x10\x1c\x12\x19\n\x15kS3GetObjectRetention\x10\x1d\x12\x1c\n\x18kS3UpdateObjectRetention\x10\x1e\x12\x19\n\x15kS3GetObjectLegalHold\x10\x1f\x12\x1c\n\x18kS3UpdateObjectLegalHold\x10 \x12\x17\n\x13kS3GetObjectTagging\x10)\x12\x1a\n\x16kS3UpdateObjectTagging\x10*\x12\x1a\n\x16kS3DeleteObjectTagging\x10+\x12\x15\n\x11kS3UploadPartCopy\x10,\x12\x18\n\x14kSwiftGetServiceInfo\x10\x32\x12\x14\n\x10kSwiftGetAccount\x10\x33\x12\x1c\n\x18kSwiftGetAccountMetadata\x10\x34\x12\x1f\n\x1bkSwiftUpdateAccountMetadata\x10\x35\x12\x16\n\x12kSwiftGetContainer\x10\x36\x12\x19\n\x15kSwiftCreateContainer\x10\x37\x12!\n\x1dkSwiftUpdateContainerMetadata\x10\x38\x12\x1e\n\x1akSwiftGetContainerMetadata\x10\x39\x12\x19\n\x15kSwiftDeleteContainer\x10:\x12\x13\n\x0fkSwiftGetObject\x10;\x12\x16\n\x12kSwiftCreateObject\x10<\x12\x14\n\x10kSwiftCopyObject\x10=\x12\x16\n\x12kSwiftDeleteObject\x10>\x12\x1b\n\x17kSwiftGetObjectMetadata\x10?\x12\x1e\n\x1akSwiftUpdateObjectMetadata\x10@\x12\x16\n\x12kSwiftGetEndpoints\x10\x41\"\xb7\x02\n\x11\x42ucketSubresource\"\xa1\x02\n\x04Type\x12\x12\n\x0ekNoSubresource\x10\x01\x12\x0f\n\x0bkAccelerate\x10\x02\x12\x08\n\x04kAcl\x10\x03\x12\t\n\x05kCors\x10\x04\x12\x0b\n\x07kDelete\x10\x05\x12\x0e\n\nkLifecycle\x10\x06\x12\r\n\tkLocation\x10\x07\x12\x0c\n\x08kLogging\x10\x08\x12\x0b\n\x07kPolicy\x10\t\x12\x10\n\x0ckReplication\x10\n\x12\x13\n\x0fkRequestPayment\x10\x0b\x12\x0c\n\x08kTagging\x10\x0c\x12\r\n\tkVersions\x10\r\x12\x0f\n\x0bkVersioning\x10\x0e\x12\x0c\n\x08kWebsite\x10\x0f\x12\x0c\n\x08kUploads\x10\x10\x12\x0f\n\x0bkObjectLock\x10\x11\x12\x16\n\x12kOwnershipControls\x10\x12\"\xa1\x01\n\x11ObjectSubresource\"\x8b\x01\n\x04Type\x12\x12\n\x0ekNoSubresource\x10\x01\x12\x08\n\x04kAcl\x10\x02\x12\x0c\n\x08kTorrent\x10\x03\x12\x0c\n\x08kRestore\x10\x04\x12\x0c\n\x08kUploads\x10\x05\x12\r\n\tkUploadId\x10\x06\x12\x0e\n\nkRetention\x10\x07\x12\x0e\n\nkLegalHold\x10\x08\x12\x0c\n\x08kTagging\x10\tB#Z!bridge/s3_portal/base/s3_enums.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.s3_portal.base.s3_enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z!bridge/s3_portal/base/s3_enums.pb'
  _globals['_REQUEST']._serialized_start=61
  _globals['_REQUEST']._serialized_end=1816
  _globals['_REQUEST_TYPE']._serialized_start=73
  _globals['_REQUEST_TYPE']._serialized_end=1816
  _globals['_BUCKETSUBRESOURCE']._serialized_start=1819
  _globals['_BUCKETSUBRESOURCE']._serialized_end=2130
  _globals['_BUCKETSUBRESOURCE_TYPE']._serialized_start=1841
  _globals['_BUCKETSUBRESOURCE_TYPE']._serialized_end=2130
  _globals['_OBJECTSUBRESOURCE']._serialized_start=2133
  _globals['_OBJECTSUBRESOURCE']._serialized_end=2294
  _globals['_OBJECTSUBRESOURCE_TYPE']._serialized_start=2155
  _globals['_OBJECTSUBRESOURCE_TYPE']._serialized_end=2294
# @@protoc_insertion_point(module_scope)
