# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/api/common/physical.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api.common import filters_pb2 as magneto_dot_api_dot_common_dot_filters__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!magneto/api/common/physical.proto\x12\x1d\x63ohesity.magneto.api.physical\x1a magneto/api/common/filters.proto\"\x94\x01\n\x14\x45nvBackupParamsProto\x12/\n\'enable_incremental_backup_after_restart\x18\x01 \x01(\x08\x12K\n\x10\x66iltering_policy\x18\x02 \x01(\x0b\x32\x31.cohesity.magneto.api.common.FilteringPolicyProto\"\x91\x04\n\x18PhysicalFileBackupParams\x12\x64\n\x14\x62\x61\x63kup_path_info_vec\x18\x01 \x03(\x0b\x32\x46.cohesity.magneto.api.physical.PhysicalFileBackupParams.BackupPathInfo\x12+\n\x1cuses_skip_nested_volumes_vec\x18\x03 \x01(\x08:\x05\x66\x61lse\x12(\n\x19symlink_follow_nas_target\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x17skip_nested_volumes_vec\x18\x02 \x03(\t\x12\x1a\n\x12metadata_file_path\x18\x05 \x01(\t\x12l\n\x16global_include_exclude\x18\x06 \x01(\x0b\x32L.cohesity.magneto.api.physical.PhysicalFileBackupParams.GlobalIncludeExclude\x1a+\n\x14GlobalIncludeExclude\x12\x13\n\x0b\x65xclude_vec\x18\x01 \x03(\t\x1a`\n\x0e\x42\x61\x63kupPathInfo\x12\x14\n\x0cinclude_path\x18\x01 \x01(\t\x12\x15\n\rexclude_paths\x18\x02 \x03(\t\x12!\n\x13skip_nested_volumes\x18\x03 \x01(\x08:\x04true\"\xa7\x01\n\x16PhysicalSnapshotParams\x12\x1c\n\x14vss_excluded_writers\x18\x01 \x03(\t\x12\x1c\n\x14vss_copy_only_backup\x18\x02 \x01(\x08\x12(\n fetch_snapshot_metadata_disabled\x18\x03 \x01(\x08\x12\'\n\x1fnotify_backup_complete_disabled\x18\x04 \x01(\x08\"\x9c\x03\n\x1fPhysicalBackupSourceParamsProto\x12\x17\n\x0fvolume_guid_vec\x18\x01 \x03(\t\x12S\n\x12\x66ile_backup_params\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.api.physical.PhysicalFileBackupParams\x12N\n\x0fsnapshot_params\x18\x03 \x01(\x0b\x32\x35.cohesity.magneto.api.physical.PhysicalSnapshotParams\x12#\n\x14\x65nable_system_backup\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07quiesce\x18\x05 \x01(\x08:\x05\x66\x61lse\x12*\n\x1b\x63ontinue_on_quiesce_failure\x18\x06 \x01(\x08:\x05\x66\x61lse\x12(\n\x19perform_source_side_dedup\x18\x07 \x01(\x08:\x05\x66\x61lse\x12(\n\x19perform_brick_based_dedup\x18\x08 \x01(\x08:\x05\x66\x61lseB\x1fZ\x1d\x63ohesity/magneto/api/physical')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.api.common.physical_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035cohesity/magneto/api/physical'
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_start=103
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_end=251
  _globals['_PHYSICALFILEBACKUPPARAMS']._serialized_start=254
  _globals['_PHYSICALFILEBACKUPPARAMS']._serialized_end=783
  _globals['_PHYSICALFILEBACKUPPARAMS_GLOBALINCLUDEEXCLUDE']._serialized_start=642
  _globals['_PHYSICALFILEBACKUPPARAMS_GLOBALINCLUDEEXCLUDE']._serialized_end=685
  _globals['_PHYSICALFILEBACKUPPARAMS_BACKUPPATHINFO']._serialized_start=687
  _globals['_PHYSICALFILEBACKUPPARAMS_BACKUPPATHINFO']._serialized_end=783
  _globals['_PHYSICALSNAPSHOTPARAMS']._serialized_start=786
  _globals['_PHYSICALSNAPSHOTPARAMS']._serialized_end=953
  _globals['_PHYSICALBACKUPSOURCEPARAMSPROTO']._serialized_start=956
  _globals['_PHYSICALBACKUPSOURCEPARAMSPROTO']._serialized_end=1368
# @@protoc_insertion_point(module_scope)
