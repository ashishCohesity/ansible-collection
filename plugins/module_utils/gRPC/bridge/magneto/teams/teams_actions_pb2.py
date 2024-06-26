# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/teams/teams_actions.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bridge/magneto/teams/teams_actions.proto\x12\x1d\x63ohesity.bridge.magneto.teams\x1a)bridge/magneto/base/magneto_actions.proto\x1a magneto/base/entities/o365.proto\x1a\"magneto/connectors/o365/o365.proto\"\xab\x01\n\x16PrepareTeamsBackupInfo\x12\x1c\n\x14view_cloning_enabled\x18\x01 \x01(\x08\x12$\n\x1cshould_recursively_clone_dir\x18\x02 \x01(\x08\x12\"\n\x1askip_channel_site_deletion\x18\x03 \x01(\x08\x12)\n!teams_private_channel_site_id_vec\x18\x04 \x03(\t\"p\n\x12\x45ndTeamsBackupInfo\x12>\n\x0cteams_config\x18\x01 \x01(\x0b\x32(.cohesity.magneto.o365.TeamsSparseConfig\x12\x1a\n\x12\x63leanup_on_failure\x18\x03 \x01(\x08\"\xd3\x03\n\x0e\x42\x61\x63kupTeamsArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.cohesity.bridge.magneto.teams.BackupTeamsArg.Type\x12\x32\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x33\n\x0cteams_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12X\n\x19prepare_teams_backup_info\x18\x05 \x01(\x0b\x32\x35.cohesity.bridge.magneto.teams.PrepareTeamsBackupInfo\x12P\n\x15\x65nd_teams_backup_info\x18\x06 \x01(\x0b\x32\x31.cohesity.bridge.magneto.teams.EndTeamsBackupInfo\"4\n\x04Type\x12\x17\n\x13kPrepareTeamsBackup\x10\x01\x12\x13\n\x0fkEndTeamsBackup\x10\x02\"%\n\x0eGetTeamsConfig\x12\x13\n\x0b\x63onfig_path\x18\x01 \x01(\t\"\xef\x01\n\x0fRestoreTeamsArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.cohesity.bridge.magneto.teams.RestoreTeamsArg.Type\x12G\n\x10get_teams_config\x18\x03 \x01(\x0b\x32-.cohesity.bridge.magneto.teams.GetTeamsConfig\"\x19\n\x04Type\x12\x11\n\rkGetTeamsInfo\x10\x01\"\xc2\x02\n\x0eTeamsActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12G\n\x10\x62\x61\x63kup_teams_arg\x18\x03 \x01(\x0b\x32-.cohesity.bridge.magneto.teams.BackupTeamsArg\x12I\n\x11restore_teams_arg\x18\x04 \x01(\x0b\x32..cohesity.bridge.magneto.teams.RestoreTeamsArg2r\n\x10teams_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18y \x01(\x0b\x32-.cohesity.bridge.magneto.teams.TeamsActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.teams.teams_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREPARETEAMSBACKUPINFO']._serialized_start=189
  _globals['_PREPARETEAMSBACKUPINFO']._serialized_end=360
  _globals['_ENDTEAMSBACKUPINFO']._serialized_start=362
  _globals['_ENDTEAMSBACKUPINFO']._serialized_end=474
  _globals['_BACKUPTEAMSARG']._serialized_start=477
  _globals['_BACKUPTEAMSARG']._serialized_end=944
  _globals['_BACKUPTEAMSARG_TYPE']._serialized_start=892
  _globals['_BACKUPTEAMSARG_TYPE']._serialized_end=944
  _globals['_GETTEAMSCONFIG']._serialized_start=946
  _globals['_GETTEAMSCONFIG']._serialized_end=983
  _globals['_RESTORETEAMSARG']._serialized_start=986
  _globals['_RESTORETEAMSARG']._serialized_end=1225
  _globals['_RESTORETEAMSARG_TYPE']._serialized_start=1200
  _globals['_RESTORETEAMSARG_TYPE']._serialized_end=1225
  _globals['_TEAMSACTIONARG']._serialized_start=1228
  _globals['_TEAMSACTIONARG']._serialized_end=1550
# @@protoc_insertion_point(module_scope)
