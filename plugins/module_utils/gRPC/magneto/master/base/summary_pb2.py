# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/summary.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!magneto/master/base/summary.proto\x12\x1f\x63ohesity.magneto.master.summary\"\x89\x04\n\rBackupJobRuns\x12\x12\n\ntotal_runs\x18\x01 \x01(\x05\x12\x16\n\x0esla_violations\x18\x02 \x01(\x05\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\x05\x12\x0f\n\x07running\x18\x04 \x01(\x05\x12I\n\npolicy_vec\x18\x05 \x03(\x0b\x32\x35.cohesity.magneto.master.summary.BackupJobRuns.Policy\x12\x16\n\x0e\x63\x61ncelled_runs\x18\x06 \x01(\x05\x12\x17\n\x0fsuccessful_runs\x18\x07 \x01(\x05\x1a=\n\rObjectDetails\x12\x16\n\x0eprotected_size\x18\x02 \x01(\x03\x12\x14\n\x0cobject_count\x18\x03 \x01(\x05\x1a\xef\x01\n\x06Policy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12Z\n\x0b\x64\x65tails_map\x18\x03 \x03(\x0b\x32\x45.cohesity.magneto.master.summary.BackupJobRuns.Policy.DetailsMapEntry\x1ao\n\x0f\x44\x65tailsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12K\n\x05value\x18\x02 \x01(\x0b\x32<.cohesity.magneto.master.summary.BackupJobRuns.ObjectDetails:\x02\x38\x01\"\x83\x03\n\nProtection\x12\x43\n\x06\x62\x61\x63kup\x18\x01 \x01(\x0b\x32\x33.cohesity.magneto.master.summary.Protection.Details\x12K\n\x0ereplication_rx\x18\x02 \x01(\x0b\x32\x33.cohesity.magneto.master.summary.Protection.Details\x12K\n\x0ereplication_tx\x18\x03 \x01(\x0b\x32\x33.cohesity.magneto.master.summary.Protection.Details\x12\x45\n\x08\x61rchival\x18\x04 \x01(\x0b\x32\x33.cohesity.magneto.master.summary.Protection.Details\x1aO\n\x07\x44\x65tails\x12\x14\n\x0cobject_count\x18\x01 \x01(\x05\x12\x13\n\x0b\x65rror_count\x18\x02 \x01(\x05\x12\x19\n\x11\x62ytes_transferred\x18\x03 \x01(\x03\"\xea\x02\n\x10ProtectedObjects\x12\x63\n\x12object_details_map\x18\x01 \x03(\x0b\x32G.cohesity.magneto.master.summary.ProtectedObjects.ObjectDetailsMapEntry\x1a}\n\x07\x44\x65tails\x12\x1e\n\x16protected_object_count\x18\x01 \x01(\x05\x12\x16\n\x0eprotected_size\x18\x02 \x01(\x03\x12 \n\x18unprotected_object_count\x18\x03 \x01(\x05\x12\x18\n\x10unprotected_size\x18\x04 \x01(\x03\x1ar\n\x15ObjectDetailsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12H\n\x05value\x18\x02 \x01(\x0b\x32\x39.cohesity.magneto.master.summary.ProtectedObjects.Details:\x02\x38\x01\"\xde\x01\n\x0eRestoreObjects\x12_\n\x11object_counts_map\x18\x01 \x03(\x0b\x32\x44.cohesity.magneto.master.summary.RestoreObjects.ObjectCountsMapEntry\x12\x19\n\x11tasks_in_progress\x18\x02 \x01(\x05\x12\x18\n\x10total_size_bytes\x18\x03 \x01(\x03\x1a\x36\n\x14ObjectCountsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKUPJOBRUNS_POLICY_DETAILSMAPENTRY']._loaded_options = None
  _globals['_BACKUPJOBRUNS_POLICY_DETAILSMAPENTRY']._serialized_options = b'8\001'
  _globals['_PROTECTEDOBJECTS_OBJECTDETAILSMAPENTRY']._loaded_options = None
  _globals['_PROTECTEDOBJECTS_OBJECTDETAILSMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREOBJECTS_OBJECTCOUNTSMAPENTRY']._loaded_options = None
  _globals['_RESTOREOBJECTS_OBJECTCOUNTSMAPENTRY']._serialized_options = b'8\001'
  _globals['_BACKUPJOBRUNS']._serialized_start=71
  _globals['_BACKUPJOBRUNS']._serialized_end=592
  _globals['_BACKUPJOBRUNS_OBJECTDETAILS']._serialized_start=289
  _globals['_BACKUPJOBRUNS_OBJECTDETAILS']._serialized_end=350
  _globals['_BACKUPJOBRUNS_POLICY']._serialized_start=353
  _globals['_BACKUPJOBRUNS_POLICY']._serialized_end=592
  _globals['_BACKUPJOBRUNS_POLICY_DETAILSMAPENTRY']._serialized_start=481
  _globals['_BACKUPJOBRUNS_POLICY_DETAILSMAPENTRY']._serialized_end=592
  _globals['_PROTECTION']._serialized_start=595
  _globals['_PROTECTION']._serialized_end=982
  _globals['_PROTECTION_DETAILS']._serialized_start=903
  _globals['_PROTECTION_DETAILS']._serialized_end=982
  _globals['_PROTECTEDOBJECTS']._serialized_start=985
  _globals['_PROTECTEDOBJECTS']._serialized_end=1347
  _globals['_PROTECTEDOBJECTS_DETAILS']._serialized_start=1106
  _globals['_PROTECTEDOBJECTS_DETAILS']._serialized_end=1231
  _globals['_PROTECTEDOBJECTS_OBJECTDETAILSMAPENTRY']._serialized_start=1233
  _globals['_PROTECTEDOBJECTS_OBJECTDETAILSMAPENTRY']._serialized_end=1347
  _globals['_RESTOREOBJECTS']._serialized_start=1350
  _globals['_RESTOREOBJECTS']._serialized_end=1572
  _globals['_RESTOREOBJECTS_OBJECTCOUNTSMAPENTRY']._serialized_start=1518
  _globals['_RESTOREOBJECTS_OBJECTCOUNTSMAPENTRY']._serialized_end=1572
# @@protoc_insertion_point(module_scope)
