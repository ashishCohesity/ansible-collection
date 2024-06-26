# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/db_utils/db_restore.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(magneto/master/db_utils/db_restore.proto\x12\x17\x63ohesity.magneto.master\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/enums.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1cutil/base/universal_id.proto\"\xfa\x02\n\x15\x44\x62RestoreSnapshotInfo\x12 \n\x14run_start_time_usecs\x18\x01 \x01(\x03:\x02-1\x12+\n\x07job_uid\x18\n \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1b\n\x0fjob_instance_id\x18\x02 \x01(\x03:\x02-1\x12\x17\n\x0b\x61ttempt_num\x18\x03 \x01(\x05:\x02-1\x12\x16\n\ntask_index\x18\x04 \x01(\x05:\x02-1\x12\x13\n\x07task_id\x18\x05 \x01(\x03:\x02-1\x12\x14\n\x08\x64\x62_index\x18\x06 \x01(\x05:\x02-1\x12\x14\n\x0c\x66ull_db_name\x18\t \x01(\t\x12?\n\x0b\x62\x61\x63kup_type\x18\x07 \x01(\x0e\x32*.cohesity.magneto.ScheduledBackupType.Type\x12-\n!db_server_backup_start_time_msecs\x18\x08 \x01(\x03:\x02-1\x12\x13\n\x07node_id\x18\x0b \x01(\x05:\x02-1\"\xe3\x01\n\rDbRestoreNode\x12\x0e\n\x02id\x18\x01 \x01(\x05:\x02-1\x12\x0f\n\x07is_root\x18\x02 \x01(\x08\x12\x45\n\rsnapshot_info\x18\x03 \x01(\x0b\x32..cohesity.magneto.master.DbRestoreSnapshotInfo\x12\x15\n\tparent_id\x18\x04 \x01(\x05:\x02-1\x12\x14\n\x0c\x63hild_id_vec\x18\x05 \x03(\x05\x12\x33\n+max_child_db_server_backup_start_time_msecs\x18\x06 \x01(\x03*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xae\x01\n\rDbRestoreTree\x12\x13\n\x07tree_id\x18\x01 \x01(\x05:\x02-1\x12\x30\n\tdb_entity\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12<\n\x0c\x61ll_node_vec\x18\x03 \x03(\x0b\x32&.cohesity.magneto.master.DbRestoreNode\x12\x18\n\x0croot_node_id\x18\x04 \x01(\x05:\x02-1\"\x82\x01\n\rDbRestorePath\x12\x30\n\tdb_entity\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x1d\n\x15\x66ull_snapshot_node_id\x18\x02 \x01(\x05\x12 \n\x18log_snapshot_node_id_vec\x18\x03 \x03(\x05\"\xc4\x01\n\x0e\x44\x62RecoveryPlan\x12I\n\x0epath_group_vec\x18\x01 \x03(\x0b\x32\x31.cohesity.magneto.master.DbRecoveryPlan.PathGroup\x1ag\n\tPathGroup\x12 \n\x14run_start_time_usecs\x18\x01 \x01(\x03:\x02-1\x12\x38\n\x08path_vec\x18\x02 \x03(\x0b\x32&.cohesity.magneto.master.DbRestorePath')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.db_utils.db_restore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DBRESTORESNAPSHOTINFO']._serialized_start=181
  _globals['_DBRESTORESNAPSHOTINFO']._serialized_end=559
  _globals['_DBRESTORENODE']._serialized_start=562
  _globals['_DBRESTORENODE']._serialized_end=789
  _globals['_DBRESTORETREE']._serialized_start=792
  _globals['_DBRESTORETREE']._serialized_end=966
  _globals['_DBRESTOREPATH']._serialized_start=969
  _globals['_DBRESTOREPATH']._serialized_end=1099
  _globals['_DBRECOVERYPLAN']._serialized_start=1102
  _globals['_DBRECOVERYPLAN']._serialized_end=1298
  _globals['_DBRECOVERYPLAN_PATHGROUP']._serialized_start=1195
  _globals['_DBRECOVERYPLAN_PATHGROUP']._serialized_end=1298
# @@protoc_insertion_point(module_scope)
