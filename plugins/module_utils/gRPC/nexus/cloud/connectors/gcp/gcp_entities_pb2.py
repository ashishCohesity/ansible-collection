# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/cloud/connectors/gcp/gcp_entities.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-nexus/cloud/connectors/gcp/gcp_entities.proto\x12\x14\x63ohesity.nexus.cloud\"Z\n\rEncryptionKey\x12\x17\n\x07raw_key\x18\x01 \x01(\tR\x06rawKey\x12 \n\x0ckms_key_name\x18\x02 \x01(\tR\nkmsKeyName\x12\x0e\n\x06sha256\x18\x03 \x01(\t\"\xcf\t\n\x08\x44iskInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\x12\x63reation_timestamp\x18\x02 \x01(\tR\x11\x63reationTimestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x17\n\x07size_gb\x18\x05 \x01(\x03R\x06sizeGb\x12\x0c\n\x04zone\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\'\n\x0fsource_snapshot\x18\x08 \x01(\tR\x0esourceSnapshot\x12,\n\x12source_snapshot_id\x18\t \x01(\tR\x10sourceSnapshotId\x12\x0f\n\x07options\x18\n \x01(\t\x12\x1a\n\x08selflink\x18\x0b \x01(\tR\x08selfLink\x12!\n\x0csource_image\x18\x0c \x01(\tR\x0bsourceImage\x12&\n\x0fsource_image_id\x18\r \x01(\tR\rsourceImageId\x12\x17\n\tdisk_type\x18\x0e \x01(\tR\x04type\x12\x10\n\x08licenses\x18\x0f \x03(\t\x12Z\n\x11guest_os_features\x18\x10 \x03(\x0b\x32..cohesity.nexus.cloud.DiskInfo.GuestOsFeaturesR\x0fguestOsFeatures\x12\x1b\n\x13lastAttachTimestamp\x18\x11 \x01(\t\x12\x1b\n\x13lastDetachTimestamp\x18\x12 \x01(\t\x12\r\n\x05users\x18\x13 \x03(\t\x12S\n\x13\x64isk_encryption_key\x18\x14 \x01(\x0b\x32#.cohesity.nexus.cloud.EncryptionKeyR\x11\x64iskEncryptionKey\x12\x62\n\x1bsource_image_encryption_key\x18\x15 \x01(\x0b\x32#.cohesity.nexus.cloud.EncryptionKeyR\x18sourceImageEncryptionKey\x12h\n\x1esource_snapshot_encryption_key\x18\x16 \x01(\x0b\x32#.cohesity.nexus.cloud.EncryptionKeyR\x1bsourceSnapshotEncryptionKey\x12I\n\nlabels_map\x18\x17 \x03(\x0b\x32-.cohesity.nexus.cloud.DiskInfo.LabelsMapEntryR\x06labels\x12+\n\x11label_fingerprint\x18\x18 \x01(\tR\x10labelFingerprint\x12\x0e\n\x06region\x18\x19 \x01(\t\x12#\n\rreplica_zones\x18\x1a \x03(\tR\x0creplicaZones\x12#\n\rlicense_codes\x18\x1b \x03(\tR\x0clicenseCodes\x12\x39\n\x19physical_block_size_bytes\x18\x1c \x01(\tR\x16physicalBlockSizeBytes\x12\x0c\n\x04kind\x18\x1d \x01(\t\x1a\x1f\n\x0fGuestOsFeatures\x12\x0c\n\x04type\x18\x01 \x01(\t\x1a\x30\n\x0eLabelsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.cloud.connectors.gcp.gcp_entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DISKINFO_LABELSMAPENTRY']._loaded_options = None
  _globals['_DISKINFO_LABELSMAPENTRY']._serialized_options = b'8\001'
  _globals['_ENCRYPTIONKEY']._serialized_start=71
  _globals['_ENCRYPTIONKEY']._serialized_end=161
  _globals['_DISKINFO']._serialized_start=164
  _globals['_DISKINFO']._serialized_end=1395
  _globals['_DISKINFO_GUESTOSFEATURES']._serialized_start=1314
  _globals['_DISKINFO_GUESTOSFEATURES']._serialized_end=1345
  _globals['_DISKINFO_LABELSMAPENTRY']._serialized_start=1347
  _globals['_DISKINFO_LABELSMAPENTRY']._serialized_end=1395
# @@protoc_insertion_point(module_scope)
