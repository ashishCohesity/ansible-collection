# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/tenant/snapshots/metadata_internal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0magneto/tenant/snapshots/metadata_internal.proto\x12\x17\x63ohesity.magneto.tenant\x1a\x1cutil/base/universal_id.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/error.proto\"X\n\x06\x43ookie\x12.\n\nobject_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1e\n\x16runs_pagination_cookie\x18\x02 \x01(\x0c\"q\n\x13ReconciliationState\"Z\n\x05State\x12\x0c\n\x08kInvalid\x10\x00\x12\x18\n\x14kGetMissingSnapshots\x10\x01\x12\x1a\n\x16kApplyMissingSnapshots\x10\x02\x12\r\n\tkFinished\x10\x03\"\xd0\x02\n\x14PersistentStateProto\x12W\n\x05state\x18\x01 \x01(\x0e\x32\x32.cohesity.magneto.tenant.ReconciliationState.State:\x14kGetMissingSnapshots\x12 \n\x18source_pagination_cookie\x18\x02 \x01(\x0c\x12\x1e\n\x16last_snapshot_notified\x18\x03 \x01(\x0c\x12\x1f\n\x17next_snapshot_to_notify\x18\x04 \x01(\x0c\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12.\n#missing_snapshots_record_counter_id\x18\x06 \x01(\x05:\x01\x31\x12\x1f\n\x17total_missing_snapshots\x18\x07 \x01(\x03\"\xa7\x02\n\x15MissingSnapshotsProto\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x16\n\x0emigration_uuid\x18\x02 \x01(\t\x12W\n\x11missing_snapshots\x18\x03 \x03(\x0b\x32<.cohesity.magneto.tenant.MissingSnapshotsProto.SnapshotProto\x1a\x89\x01\n\rSnapshotProto\x12+\n\x07job_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1c\n\x14run_start_time_usecs\x18\x02 \x01(\x03\x12-\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.tenant.snapshots.metadata_internal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COOKIE']._serialized_start=160
  _globals['_COOKIE']._serialized_end=248
  _globals['_RECONCILIATIONSTATE']._serialized_start=250
  _globals['_RECONCILIATIONSTATE']._serialized_end=363
  _globals['_RECONCILIATIONSTATE_STATE']._serialized_start=273
  _globals['_RECONCILIATIONSTATE_STATE']._serialized_end=363
  _globals['_PERSISTENTSTATEPROTO']._serialized_start=366
  _globals['_PERSISTENTSTATEPROTO']._serialized_end=702
  _globals['_MISSINGSNAPSHOTSPROTO']._serialized_start=705
  _globals['_MISSINGSNAPSHOTSPROTO']._serialized_end=1000
  _globals['_MISSINGSNAPSHOTSPROTO_SNAPSHOTPROTO']._serialized_start=863
  _globals['_MISSINGSNAPSHOTSPROTO_SNAPSHOTPROTO']._serialized_end=1000
# @@protoc_insertion_point(module_scope)
