# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/san_entity.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import san_pb2 as magneto_dot_base_dot_san__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/base/entities/san_entity.proto\x12\x14\x63ohesity.magneto.san\x1a\x16magneto/base/san.proto\"\xb6\x07\n\x06\x45ntity\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.cohesity.magneto.san.Entity.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x42\n\nid_version\x18\x13 \x01(\x0e\x32..cohesity.magneto.san.Entity.IdentifierVersion\x12\x10\n\x08\x61rray_id\x18\x03 \x01(\t\x12\x16\n\x0e\x61rray_revision\x18\x04 \x01(\t\x12\x15\n\rarray_version\x18\x05 \x01(\t\x12\x35\n\x0e\x61rray_port_vec\x18\x06 \x03(\x0b\x32\x1d.cohesity.magneto.san.SanPort\x12\x1c\n\x14volume_creation_time\x18\x07 \x01(\t\x12\x15\n\rvolume_serial\x18\x08 \x01(\t\x12\x13\n\x0bvolume_size\x18\t \x01(\x03\x12\x1f\n\x17volume_total_space_used\x18\x0b \x01(\x03\x12\x15\n\rvolume_source\x18\n \x01(\t\x12\x16\n\x0e\x62\x61se_volume_id\x18\x0c \x01(\t\x12\x12\n\nvolume_iqn\x18\r \x01(\t\x12\x17\n\x0fvolume_group_id\x18\x0e \x01(\t\x12\x18\n\x10volume_group_uid\x18\x0f \x01(\t\x12\x17\n\x0fstorage_pool_id\x18\x10 \x01(\t\x12P\n\x13storage_pool_status\x18\x11 \x01(\x0e\x32\x33.cohesity.magneto.san.Entity.StoragePoolStatus.Type\x12\x1d\n\x15\x61vailability_group_id\x18\x12 \x01(\t\x1a\x44\n\x11StoragePoolStatus\"/\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x0b\n\x07kOnline\x10\x01\x12\x0c\n\x08kOffline\x10\x02\"\xa6\x01\n\x04Type\x12\x11\n\rkStorageArray\x10\x00\x12\x0b\n\x07kVolume\x10\x01\x12\x14\n\x10kPureVolumeGroup\x10\x02\x12\x18\n\x14kPureProtectionGroup\x10\x03\x12\x10\n\x0ckVolumeGroup\x10\x04\x12\x10\n\x0ckStoragePool\x10\x05\x12\x16\n\x12kAvailabilityGroup\x10\x06\x12\x12\n\x0ekDummyResource\x10\x07\"M\n\x11IdentifierVersion\x12\t\n\x05kNone\x10\x00\x12\x16\n\x12kNumericIdentifier\x10\x01\x12\x15\n\x11kUniqueIdentifier\x10\x02*\x08\x08\x64\x10\x80\x80\x80\x80\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.san_entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITY']._serialized_start=89
  _globals['_ENTITY']._serialized_end=1039
  _globals['_ENTITY_STORAGEPOOLSTATUS']._serialized_start=713
  _globals['_ENTITY_STORAGEPOOLSTATUS']._serialized_end=781
  _globals['_ENTITY_STORAGEPOOLSTATUS_TYPE']._serialized_start=734
  _globals['_ENTITY_STORAGEPOOLSTATUS_TYPE']._serialized_end=781
  _globals['_ENTITY_TYPE']._serialized_start=784
  _globals['_ENTITY_TYPE']._serialized_end=950
  _globals['_ENTITY_IDENTIFIERVERSION']._serialized_start=952
  _globals['_ENTITY_IDENTIFIERVERSION']._serialized_end=1029
# @@protoc_insertion_point(module_scope)