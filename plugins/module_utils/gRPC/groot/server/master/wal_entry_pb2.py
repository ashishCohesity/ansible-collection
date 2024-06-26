# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groot/server/master/wal_entry.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from groot.base import groot_pb2 as groot_dot_base_dot_groot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#groot/server/master/wal_entry.proto\x12\x1c\x63ohesity.groot.server.master\x1a\x16groot/base/groot.proto\"\x84\x03\n\rMigrationTask\x12\x0f\n\x07task_id\x18\x01 \x02(\x03\x12\x12\n\nservice_id\x18\x08 \x02(\x03\x12\x16\n\x0esource_node_id\x18\x02 \x01(\x03\x12\x16\n\x0esource_disk_id\x18\x06 \x01(\x03\x12\x1b\n\x13\x64\x65stination_node_id\x18\x03 \x01(\x03\x12\x1b\n\x13\x64\x65stination_disk_id\x18\x07 \x01(\x03\x12G\n\ttask_type\x18\x04 \x01(\x0e\x32\x34.cohesity.groot.server.master.MigrationTask.TaskType\x12\x42\n\x06status\x18\x05 \x01(\x0e\x32\x32.cohesity.groot.server.master.MigrationTask.Status\"!\n\x08TaskType\x12\x08\n\x04kAdd\x10\x01\x12\x0b\n\x07kDelete\x10\x02\"4\n\x06Status\x12\x0f\n\x0bkIncomplete\x10\x02\x12\t\n\x05kDone\x10\x03\x12\x0e\n\nkCancelled\x10\x04\"\xd3\x07\n\x08WALEntry\x12N\n\x11service_state_vec\x18\x01 \x03(\x0b\x32\x33.cohesity.groot.server.master.WALEntry.ServiceState\x12P\n\x12service_update_vec\x18\x02 \x03(\x0b\x32\x34.cohesity.groot.server.master.WALEntry.ServiceUpdate\x1a\xce\x01\n\x0cServiceState\x12\x36\n\x0cservice_info\x18\x01 \x02(\x0b\x32 .cohesity.groot.base.ServiceInfo\x12G\n\x12migration_task_vec\x18\x02 \x03(\x0b\x32+.cohesity.groot.server.master.MigrationTask\x12=\n\x06status\x18\x03 \x02(\x0e\x32-.cohesity.groot.server.master.WALEntry.Status\x1a\xeb\x03\n\rServiceUpdate\x12\x12\n\nservice_id\x18\x01 \x02(\x03\x12\x63\n\x13\x65poch_update_intent\x18\x02 \x01(\x0b\x32\x46.cohesity.groot.server.master.WALEntry.ServiceUpdate.EpochUpdateIntent\x12G\n\x12migration_task_vec\x18\x03 \x03(\x0b\x32+.cohesity.groot.server.master.MigrationTask\x12\x46\n\x10replica_info_vec\x18\x04 \x03(\x0b\x32,.cohesity.groot.base.ServiceInfo.ReplicaInfo\x12L\n\x16older_replica_info_vec\x18\x06 \x03(\x0b\x32,.cohesity.groot.base.ServiceInfo.ReplicaInfo\x12=\n\x06status\x18\x05 \x02(\x0e\x32-.cohesity.groot.server.master.WALEntry.Status\x1a\x43\n\x11\x45pochUpdateIntent\x12\x18\n\x10\x63urrent_epoch_id\x18\x02 \x02(\x03\x12\x14\n\x0cnew_epoch_id\x18\x03 \x02(\x03\"f\n\x06Status\x12\x17\n\x13kUpdateIntentLogged\x10\x01\x12\x16\n\x12kSlaveEpochUpdated\x10\x02\x12\x16\n\x12kMigrationComplete\x10\x03\x12\x13\n\x0fkServiceEnabled\x10\x04')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'groot.server.master.wal_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MIGRATIONTASK']._serialized_start=94
  _globals['_MIGRATIONTASK']._serialized_end=482
  _globals['_MIGRATIONTASK_TASKTYPE']._serialized_start=395
  _globals['_MIGRATIONTASK_TASKTYPE']._serialized_end=428
  _globals['_MIGRATIONTASK_STATUS']._serialized_start=430
  _globals['_MIGRATIONTASK_STATUS']._serialized_end=482
  _globals['_WALENTRY']._serialized_start=485
  _globals['_WALENTRY']._serialized_end=1464
  _globals['_WALENTRY_SERVICESTATE']._serialized_start=660
  _globals['_WALENTRY_SERVICESTATE']._serialized_end=866
  _globals['_WALENTRY_SERVICEUPDATE']._serialized_start=869
  _globals['_WALENTRY_SERVICEUPDATE']._serialized_end=1360
  _globals['_WALENTRY_SERVICEUPDATE_EPOCHUPDATEINTENT']._serialized_start=1293
  _globals['_WALENTRY_SERVICEUPDATE_EPOCHUPDATEINTENT']._serialized_end=1360
  _globals['_WALENTRY_STATUS']._serialized_start=1362
  _globals['_WALENTRY_STATUS']._serialized_end=1464
# @@protoc_insertion_point(module_scope)
