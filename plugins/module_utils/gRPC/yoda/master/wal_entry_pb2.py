# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/master/wal_entry.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yoda.base import reports_pb2 as yoda_dot_base_dot_reports__pb2
from yoda.master import librarian_migration_pb2 as yoda_dot_master_dot_librarian__migration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1byoda/master/wal_entry.proto\x12\x14\x63ohesity.yoda.master\x1a\x17yoda/base/reports.proto\x1a%yoda/master/librarian_migration.proto\"}\n\x0bTaskDetails\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x1f\n\x17pending_sub_task_id_vec\x18\x02 \x03(\x03\x12)\n\x06report\x18\x03 \x01(\x0b\x32\x19.cohesity.yoda.YodaReport\x12\x11\n\tcompleted\x18\x04 \x01(\x08\"\x92\x01\n\tWalRecord\x12P\n\x19librarian_migration_stats\x18\x01 \x01(\x0b\x32-.cohesity.yoda.master.LibrarianMigrationStats\x12\x33\n\x08task_vec\x18\x02 \x03(\x0b\x32!.cohesity.yoda.master.TaskDetails')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.master.wal_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKDETAILS']._serialized_start=117
  _globals['_TASKDETAILS']._serialized_end=242
  _globals['_WALRECORD']._serialized_start=245
  _globals['_WALRECORD']._serialized_end=391
# @@protoc_insertion_point(module_scope)
