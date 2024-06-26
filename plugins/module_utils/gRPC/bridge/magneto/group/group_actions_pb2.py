# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/group/group_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base.entities import o365_pb2 as magneto_dot_base_dot_entities_dot_o365__pb2
from magneto.connectors.o365 import o365_pb2 as magneto_dot_connectors_dot_o365_dot_o365__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bridge/magneto/group/group_actions.proto\x12\x1d\x63ohesity.bridge.magneto.group\x1a)bridge/magneto/base/magneto_actions.proto\x1a magneto/base/entities/o365.proto\x1a\"magneto/connectors/o365/o365.proto\"`\n\x16PrepareGroupBackupInfo\x12$\n\x1cshould_recursively_clone_dir\x18\x01 \x01(\x08\x12 \n\x18\x63reate_group_mailbox_dir\x18\x02 \x01(\x08\"\x90\x01\n\rEndBackupInfo\x12\x42\n\x0cgroup_config\x18\x01 \x01(\x0b\x32,.cohesity.magneto.o365.O365GroupSparseConfig\x12\x1f\n\x11write_config_file\x18\x02 \x01(\x08:\x04true\x12\x1a\n\x12\x63leanup_on_failure\x18\x03 \x01(\x08\"\xc8\x03\n\x0e\x42\x61\x63kupGroupArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.cohesity.bridge.magneto.group.BackupGroupArg.Type\x12\x32\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x33\n\x0cgroup_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12X\n\x19prepare_group_backup_info\x18\x05 \x01(\x0b\x32\x35.cohesity.bridge.magneto.group.PrepareGroupBackupInfo\x12\x45\n\x0f\x65nd_backup_info\x18\x06 \x01(\x0b\x32,.cohesity.bridge.magneto.group.EndBackupInfo\"4\n\x04Type\x12\x17\n\x13kPrepareGroupBackup\x10\x01\x12\x13\n\x0fkEndGroupBackup\x10\x02\"%\n\x0eReadConfigInfo\x12\x13\n\x0b\x63onfig_path\x18\x01 \x01(\t\"\xed\x01\n\x0fRestoreGroupArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.cohesity.bridge.magneto.group.RestoreGroupArg.Type\x12G\n\x10read_config_info\x18\x05 \x01(\x0b\x32-.cohesity.bridge.magneto.group.ReadConfigInfo\"\x17\n\x04Type\x12\x0f\n\x0bkReadConfig\x10\x01\"\xc2\x02\n\x0eGroupActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12G\n\x10\x62\x61\x63kup_group_arg\x18\x03 \x01(\x0b\x32-.cohesity.bridge.magneto.group.BackupGroupArg\x12I\n\x11restore_group_arg\x18\x04 \x01(\x0b\x32..cohesity.bridge.magneto.group.RestoreGroupArg2r\n\x10group_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18z \x01(\x0b\x32-.cohesity.bridge.magneto.group.GroupActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.group.group_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREPAREGROUPBACKUPINFO']._serialized_start=188
  _globals['_PREPAREGROUPBACKUPINFO']._serialized_end=284
  _globals['_ENDBACKUPINFO']._serialized_start=287
  _globals['_ENDBACKUPINFO']._serialized_end=431
  _globals['_BACKUPGROUPARG']._serialized_start=434
  _globals['_BACKUPGROUPARG']._serialized_end=890
  _globals['_BACKUPGROUPARG_TYPE']._serialized_start=838
  _globals['_BACKUPGROUPARG_TYPE']._serialized_end=890
  _globals['_READCONFIGINFO']._serialized_start=892
  _globals['_READCONFIGINFO']._serialized_end=929
  _globals['_RESTOREGROUPARG']._serialized_start=932
  _globals['_RESTOREGROUPARG']._serialized_end=1169
  _globals['_RESTOREGROUPARG_TYPE']._serialized_start=1146
  _globals['_RESTOREGROUPARG_TYPE']._serialized_end=1169
  _globals['_GROUPACTIONARG']._serialized_start=1172
  _globals['_GROUPACTIONARG']._serialized_end=1494
# @@protoc_insertion_point(module_scope)
