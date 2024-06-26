# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/agent.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import credentials_pb2 as magneto_dot_base_dot_credentials__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from yoda.base import volume_info_pb2 as yoda_dot_base_dot_volume__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18magneto/base/agent.proto\x12\x10\x63ohesity.magneto\x1a\x1emagneto/base/credentials.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1byoda/base/volume_info.proto\"\xa9\x0b\n\x1d\x41gentSetupRestoreDiskTaskInfo\x12O\n\x0bsetup_state\x18\x01 \x01(\x0e\x32:.cohesity.magneto.AgentSetupRestoreDiskTaskInfo.SetupState\x12\x31\n\x0bsetup_error\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12U\n\x0eteardown_state\x18\x03 \x01(\x0e\x32=.cohesity.magneto.AgentSetupRestoreDiskTaskInfo.TeardownState\x12\x34\n\x0eteardown_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x30\n$relative_restore_path_vec_DEPRECATED\x18\x05 \x03(\tB\x02\x18\x01\x12\x42\n\x14volume_file_info_vec\x18\x06 \x03(\x0b\x32$.cohesity.yoda.volumeutil.VolumeInfo\x12M\n\nmount_info\x18\x07 \x01(\x0b\x32\x39.cohesity.magneto.AgentSetupRestoreDiskTaskInfo.MountInfo\x12m\n\x19\x66ile_to_relative_path_map\x18\x08 \x03(\x0b\x32J.cohesity.magneto.AgentSetupRestoreDiskTaskInfo.FileToRelativePathMapEntry\x12\x1d\n\x15snapshot_files_cloned\x18\t \x01(\x08\x12\x15\n\rfull_nas_path\x18\n \x01(\t\x12\"\n\x13restore_view_cloned\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x18\n\x10\x61gent_ip_address\x18\x0c \x01(\t\x12<\n\x15target_vm_credentials\x18\r \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x1a\xe1\x01\n\tMountInfo\x12\x13\n\x0bremote_host\x18\x01 \x01(\t\x12\x13\n\x0bremote_path\x18\x02 \x01(\t\x12\x17\n\x0fnas_mount_point\x18\x03 \x01(\t\x12\x1a\n\x12volume_fs_uuid_vec\x18\x04 \x03(\t\x12\x17\n\x0fvolume_guid_vec\x18\x07 \x03(\t\x12$\n\x1cvirtual_disk_mount_point_vec\x18\x05 \x03(\t\x12\x1d\n\x15virtual_disk_path_vec\x18\x06 \x03(\t\x12\x17\n\x0fremote_host_vec\x18\x08 \x03(\t\x1a<\n\x1a\x46ileToRelativePathMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"s\n\nSetupState\x12\x11\n\rkSetupStarted\x10\x00\x12\x18\n\x14kCloneFilesCompleted\x10\x01\x12\x0f\n\x0bkMountedNAS\x10\x02\x12\x12\n\x0ekSetupFinished\x10\x03\x12\x13\n\x0fkSetupCancelled\x10\x04\"k\n\rTeardownState\x12\x14\n\x10kTeardownStarted\x10\x00\x12\x1a\n\x16kUnmountedVirtualDisks\x10\x01\x12\x11\n\rkUnmountedNAS\x10\x02\x12\x15\n\x11kTeardownFinished\x10\x03\x32\x8c\x01\n\"agent_setup_restore_disk_task_info\x12/.cohesity.magneto.SetupRestoreDiskTaskInfoProto\x18\x65 \x01(\x0b\x32/.cohesity.magneto.AgentSetupRestoreDiskTaskInfo\"\x9b\x04\n\x15\x41gentRestoreFilesInfo\x12Q\n\ntask_state\x18\x01 \x01(\x0e\x32=.cohesity.magneto.AgentRestoreFilesInfo.RestoreFilesTaskState\x12P\n\x17restore_disks_task_info\x18\x02 \x01(\x0b\x32/.cohesity.magneto.AgentSetupRestoreDiskTaskInfo\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x35\n\x0ftear_down_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\x84\x01\n\x15RestoreFilesTaskState\x12\x0c\n\x08kStarted\x10\x00\x12\x13\n\x0fkSetupCompleted\x10\x01\x12\x17\n\x13kCopyFilesInitiated\x10\x02\x12\x17\n\x13kCopyFilesCompleted\x10\x03\x12\x16\n\x12kTeardownCompleted\x10\x04\x32r\n\x18\x61gent_restore_files_info\x12\'.cohesity.magneto.RestoreFilesInfoProto\x18\x65 \x01(\x0b\x32\'.cohesity.magneto.AgentRestoreFilesInfoB\x17Z\x15magneto/base/agent.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025magneto/base/agent.pb'
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_FILETORELATIVEPATHMAPENTRY']._loaded_options = None
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_FILETORELATIVEPATHMAPENTRY']._serialized_options = b'8\001'
  _globals['_AGENTSETUPRESTOREDISKTASKINFO'].fields_by_name['relative_restore_path_vec_DEPRECATED']._loaded_options = None
  _globals['_AGENTSETUPRESTOREDISKTASKINFO'].fields_by_name['relative_restore_path_vec_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_AGENTSETUPRESTOREDISKTASKINFO']._serialized_start=162
  _globals['_AGENTSETUPRESTOREDISKTASKINFO']._serialized_end=1611
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_MOUNTINFO']._serialized_start=955
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_MOUNTINFO']._serialized_end=1180
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_FILETORELATIVEPATHMAPENTRY']._serialized_start=1182
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_FILETORELATIVEPATHMAPENTRY']._serialized_end=1242
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_SETUPSTATE']._serialized_start=1244
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_SETUPSTATE']._serialized_end=1359
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_TEARDOWNSTATE']._serialized_start=1361
  _globals['_AGENTSETUPRESTOREDISKTASKINFO_TEARDOWNSTATE']._serialized_end=1468
  _globals['_AGENTRESTOREFILESINFO']._serialized_start=1614
  _globals['_AGENTRESTOREFILESINFO']._serialized_end=2153
  _globals['_AGENTRESTOREFILESINFO_RESTOREFILESTASKSTATE']._serialized_start=1905
  _globals['_AGENTRESTOREFILESINFO_RESTOREFILESTASKSTATE']._serialized_end=2037
# @@protoc_insertion_point(module_scope)
