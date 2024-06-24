# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.message_catalog import message_catalog_pb2 as util_dot_message__catalog_dot_message__catalog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18magneto/base/error.proto\x12\x10\x63ohesity.magneto\x1a*util/message_catalog/message_catalog.proto\"\x84\x18\n\nErrorProto\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32!.cohesity.magneto.ErrorProto.Type:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x37\n\x12\x64\x65tailed_error_msg\x18\x03 \x01(\x0b\x32\x1b.cohesity.util.MessageProto\"\xee\x16\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kStale\x10\x03\x12\x0b\n\x07kExists\x10\x04\x12\x10\n\x0ckNonExistent\x10\x05\x12\n\n\x06kRetry\x10\x06\x12\x0e\n\nkNotMaster\x10\x07\x12\x11\n\rkInvalidLogin\x10\x08\x12\x13\n\x0fkInvalidRequest\x10\t\x12\x10\n\x0ckUnsupported\x10\n\x12\x11\n\rkVSphereError\x10\x0b\x12\r\n\tkVixError\x10\x0c\x12\x10\n\x0ckBridgeError\x10\r\x12\r\n\tkRejected\x10\x0e\x12\x0e\n\nkDuplicate\x10\x0f\x12\x13\n\x0fkVMHostMismatch\x10\x10\x12\x19\n\x15kGuestOperationsError\x10\x11\x12\x0f\n\x0bkAgentError\x10\x12\x12\x1b\n\x17kAgentErrorNotRetryable\x10\x1e\x12\x1b\n\x17kDatabaseBackupMismatch\x10\x13\x12\x14\n\x10kVolumeUtilError\x10\x14\x12\x12\n\x0ekCopyUtilError\x10\x15\x12\x14\n\x10kSqlRestoreError\x10\x16\x12\x0e\n\nkGrpcError\x10\x17\x12\x0e\n\nkYodaError\x10\x18\x12\r\n\tkDisabled\x10\x19\x12\x10\n\x0ckScriptError\x10\x1a\x12\x10\n\x0ckMethodError\x10\x1b\x12\x11\n\rkUnknownError\x10\x1c\x12\x0e\n\nkCancelled\x10\x1d\x12\x0f\n\x0bkIneligible\x10\x1f\x12\x0e\n\nkPureError\x10 \x12\x0f\n\x0bkCloudError\x10!\x12\x0f\n\x0bkNexusError\x10\"\x12\x10\n\x0ckNetappError\x10#\x12\x19\n\x15kDirectoryWalkerError\x10$\x12\x10\n\x0ckScribeError\x10%\x12\x13\n\x0fkAcropolisError\x10&\x12\x0c\n\x08kFsError\x10\'\x12\x14\n\x10kVixTimeoutError\x10(\x12\x10\n\x0ckIsilonError\x10)\x12\r\n\tkKvmError\x10*\x12\x14\n\x10kSchedulingError\x10+\x12\x10\n\x0ckAccessError\x10,\x12\x0c\n\x08kInvalid\x10-\x12\x0e\n\nkNotLeader\x10.\x12\x0c\n\x08kPending\x10/\x12\x0f\n\x0bkParseError\x10\x30\x12\x17\n\x13kServiceUnavailable\x10\x31\x12\x17\n\x13kOracleRestoreError\x10\x32\x12\x14\n\x10kFlashbladeError\x10\x33\x12\x13\n\x0fkDbRestoreError\x10\x34\x12\x1f\n\x1bkCloudResourceLimitExceeded\x10\x35\x12\r\n\tkVCDError\x10\x36\x12\x14\n\x10kOutlookEwsError\x10\x37\x12\x13\n\x0fkHyperFlexError\x10\x38\x12\x18\n\x14kCloudProxyDiskError\x10\x39\x12\x1a\n\x16kCloudProxyLaunchError\x10:\x12\x1d\n\x19kCloudResourceUnsupported\x10;\x12\x19\n\x15kSQLLogChainHoleFound\x10<\x12\x1d\n\x19kSQLEntityLockingConflict\x10=\x12\x1c\n\x18kIncompleteHardlinkGroup\x10>\x12 \n\x1ckCloudNetworkConnectionError\x10?\x12\x11\n\rkBifrostError\x10@\x12\x0c\n\x08kWarning\x10\x41\x12\x13\n\x0fkADRestoreError\x10\x42\x12\x11\n\rkMSGraphError\x10\x43\x12\x0e\n\nkGPFSError\x10\x44\x12\x13\n\x0fkNotImplemented\x10\x45\x12\r\n\tkCimError\x10\x46\x12\x14\n\x10kKubernetesError\x10G\x12\x12\n\x0ekIoFilterError\x10H\x12\x0e\n\nkTagsError\x10I\x12\x14\n\x10kNotSynchronized\x10J\x12\x10\n\x0ckNimbleError\x10K\x12\r\n\tkSANError\x10L\x12\x14\n\x10kElastifileError\x10M\x12\x0f\n\x0bkOutOfSpace\x10N\x12\x1f\n\x1bkSQLMissingDifferentialBase\x10O\x12\x11\n\rkUnauthorized\x10P\x12\x0e\n\nkAtomError\x10Q\x12\x12\n\x0ekExchangeError\x10R\x12\x1a\n\x16kCustomAttributesError\x10S\x12\x19\n\x15kMissingBackupsetRows\x10T\x12\x10\n\x0ckImanisError\x10U\x12\x13\n\x0fkInvalidEndTime\x10V\x12\x12\n\x0ekInternalError\x10W\x12\x1b\n\x17kSQLMissingFCIInstances\x10X\x12\x1b\n\x17kVolumeAttachmentFailed\x10Z\x12\x1e\n\x1akCloudResourceNotAvailable\x10[\x12\x1a\n\x16kEncryptionKeyNotFound\x10\\\x12\x08\n\x04kEOF\x10]\x12\x16\n\x12kAutodiscoverError\x10^\x12\x1b\n\x17kSourceEntityNotPresent\x10_\x12\x1c\n\x18kSQLAAGRelationshipError\x10`\x12\x14\n\x10kNoDbsDiscovered\x10\x61\x12\x14\n\x10kSharepointError\x10\x62\x12\x17\n\x13kHeimdallFleetError\x10\x63\x12\x14\n\x10kViewKeeperError\x10\x64\x12\x16\n\x12kAlreadyTerminated\x10\x65\x12\x14\n\x10kUdaRestoreError\x10\x66\x12\x13\n\x0fkUdaBackupError\x10g\x12\r\n\tkMDSError\x10h\x12\x14\n\x10kMissingProvider\x10i\x12\x11\n\rkMountFailure\x10j\x12\x14\n\x10kSFDCBackupError\x10k\x12\x18\n\x14kSSLCertificateError\x10l\x12\x16\n\x12kSSLHandshakeError\x10m\x12\x18\n\x14kHostResolutionError\x10n\x12\x0e\n\nkSfdcError\x10o\x12\x17\n\x13kLogFileNonExistent\x10p\x12\x1a\n\x16kVMListPaginationError\x10q\x12\x1b\n\x17kFullRecoveryInProgress\x10r\x12\x0e\n\nkEmptyFile\x10s\x12\x0c\n\x08kSkipped\x10t\x12\x1e\n\x1akMSGraphEmptyResponseError\x10u\x12\x14\n\x10kViewBoxNotFound\x10v\x12\x16\n\x12kSfdcCycleDetected\x10w\x12\x19\n\x15kGCPSubnetIPExhausted\x10x\x12\x11\n\rkSfdcAwsError\x10y\x12\x16\n\x12kResponseMalformed\x10z\x12\x1a\n\x16kNoConnectionAvailable\x10{\x12\x19\n\x15kNonProtectableEntity\x10|\x12\x17\n\x13kInvalidApiResponse\x10}\x12\x15\n\x11kInvalidParameter\x10~\x12\x0c\n\x08kIOError\x10\x7f\x12!\n\x1ckOracleRestoreV2NotSupported\x10\x80\x01\x12\x0c\n\x07kVosEOF\x10\x82\x01\x12\x10\n\x0bkVosFailure\x10\x83\x01\x12\x15\n\x10kVosIgnoreOffset\x10\x84\x01\x12\x19\n\x14kIbmFlashSystemError\x10\x85\x01\x12\x1b\n\x16kRequestEntityTooLarge\x10\x86\x01\x12\r\n\x08kCorrupt\x10\x87\x01\x12\x13\n\x0ekSnapshotError\x10\x88\x01\x12#\n\x1ekQueryDiskExtentSessionExpired\x10\x8a\x01\"\x06\x08\x81\x01\x10\x81\x01*\x12kBucketNonExistentB\x0eZ\x0cmagneto/base')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014magneto/base'
  _globals['_ERRORPROTO']._serialized_start=91
  _globals['_ERRORPROTO']._serialized_end=3167
  _globals['_ERRORPROTO_TYPE']._serialized_start=241
  _globals['_ERRORPROTO_TYPE']._serialized_end=3167
# @@protoc_insertion_point(module_scope)
