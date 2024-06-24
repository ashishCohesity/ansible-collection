# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/san/san_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$bridge/magneto/san/san_actions.proto\x12\x1b\x63ohesity.bridge.magneto.san\x1a)bridge/magneto/base/magneto_actions.proto\x1a\x17magneto/base/disk.proto\x1a\x1amagneto/base/magneto.proto\"\x84\x03\n\x0c\x42\x61\x63kupSanArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x42\n\x04type\x18\x02 \x01(\x0e\x32\x34.cohesity.bridge.magneto.san.BackupSanArg.ActionType\x12\x30\n\x0bsource_disk\x18\x03 \x01(\x0b\x32\x1b.cohesity.magneto.DiskProto\x12;\n\x0e\x64isk_area_list\x18\x04 \x01(\x0b\x32#.cohesity.magneto.DiskAreaListProto\x12\x18\n\x10sub_file_size_mb\x18\x05 \x01(\x03\"g\n\nActionType\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkSetupFiles\x10\x02\x12\x13\n\x0fkBackupDiskArea\x10\x03\x12\x0f\n\x0bkEndSubTask\x10\x04\x12\x0e\n\nkEndBackup\x10\x05*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xfe\x03\n\rRestoreSanArg\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.cohesity.bridge.magneto.san.RestoreSanArg.ActionType\x12\x18\n\x10source_view_name\x18\x02 \x01(\t\x12\x17\n\x0bview_box_id\x18\x03 \x01(\x03:\x02-1\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\"\n\x1asnapshot_relative_dir_path\x18\x05 \x01(\t\x12+\n#changed_areas_relative_dir_path_vec\x18\x06 \x03(\t\x12\x30\n\x0btarget_disk\x18\x07 \x01(\x0b\x32\x1b.cohesity.magneto.DiskProto\x12;\n\x10\x63onnector_params\x18\x08 \x01(\x0b\x32!.cohesity.magneto.ConnectorParams\x12-\n\x04\x61rea\x18\t \x01(\x0b\x32\x1f.cohesity.magneto.DiskAreaProto\"i\n\nActionType\x12\x0f\n\x0bkCloneFiles\x10\x01\x12\x12\n\x0ekFetchDiskInfo\x10\x02\x12\x14\n\x10kRestoreDiskArea\x10\x03\x12\x0f\n\x0bkEndSubTask\x10\x04\x12\x0f\n\x0bkEndRestore\x10\x05*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xae\x02\n\x0cSanActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12\x41\n\x0e\x62\x61\x63kup_san_arg\x18\x03 \x01(\x0b\x32).cohesity.bridge.magneto.san.BackupSanArg\x12\x43\n\x0frestore_san_arg\x18\x04 \x01(\x0b\x32*.cohesity.bridge.magneto.san.RestoreSanArg2l\n\x0esan_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18h \x01(\x0b\x32).cohesity.bridge.magneto.san.SanActionArg\"\xf1\x02\n\x0eGroupActionArg\x12\x35\n\x0csource_disks\x18\x01 \x03(\x0b\x32\x1b.cohesity.magneto.DiskProtoB\x02\x18\x01\x12S\n\x0evolume_arg_vec\x18\x02 \x03(\x0b\x32;.cohesity.bridge.magneto.san.GroupActionArg.VolumeActionArg\x1aW\n\x0fVolumeActionArg\x12\x44\n\x11volume_action_arg\x18\x01 \x01(\x0b\x32).cohesity.bridge.magneto.ExecuteActionArg*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x32p\n\x10group_action_arg\x12).cohesity.bridge.magneto.san.BackupSanArg\x18\x64 \x01(\x0b\x32+.cohesity.bridge.magneto.san.GroupActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.san.san_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GROUPACTIONARG'].fields_by_name['source_disks']._loaded_options = None
  _globals['_GROUPACTIONARG'].fields_by_name['source_disks']._serialized_options = b'\030\001'
  _globals['_BACKUPSANARG']._serialized_start=166
  _globals['_BACKUPSANARG']._serialized_end=554
  _globals['_BACKUPSANARG_ACTIONTYPE']._serialized_start=441
  _globals['_BACKUPSANARG_ACTIONTYPE']._serialized_end=544
  _globals['_RESTORESANARG']._serialized_start=557
  _globals['_RESTORESANARG']._serialized_end=1067
  _globals['_RESTORESANARG_ACTIONTYPE']._serialized_start=952
  _globals['_RESTORESANARG_ACTIONTYPE']._serialized_end=1057
  _globals['_SANACTIONARG']._serialized_start=1070
  _globals['_SANACTIONARG']._serialized_end=1372
  _globals['_GROUPACTIONARG']._serialized_start=1375
  _globals['_GROUPACTIONARG']._serialized_end=1744
  _globals['_GROUPACTIONARG_VOLUMEACTIONARG']._serialized_start=1533
  _globals['_GROUPACTIONARG_VOLUMEACTIONARG']._serialized_end=1620
# @@protoc_insertion_point(module_scope)
