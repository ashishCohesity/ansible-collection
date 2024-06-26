# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/physical.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2
from util import cbt_delta_pb2 as util_dot_cbt__delta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmagneto/base/physical.proto\x12\x19\x63ohesity.magneto.physical\x1a\x1fmagneto/agents/base/agent.proto\x1a\x17magneto/base/disk.proto\x1a\x18magneto/base/enums.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1bmagneto/base/sub_task.proto\x1a\x14util/cbt_delta.proto\"\xfd\x03\n\x0bVirtualDisk\x12\x13\n\x0bvolume_guid\x18\x01 \x01(\x0c\x12\x15\n\rsnapshot_guid\x18\x02 \x01(\x0c\x12\x1c\n\x14snapshot_device_path\x18\x03 \x01(\t\x12\x16\n\x0e\x63\x61pacity_bytes\x18\x04 \x01(\x03\x12&\n\x19logical_sector_size_bytes\x18\r \x01(\x05:\x03\x35\x31\x32\x12\x0b\n\x03key\x18\x05 \x01(\x03\x12\x1f\n\x17last_position_backed_up\x18\x06 \x01(\x03\x12$\n\x1ctotal_bytes_read_from_source\x18\x07 \x01(\x03\x12\x18\n\x10\x65ncoded_filename\x18\x08 \x01(\t\x12#\n\x18volume_area_start_offset\x18\t \x01(\x03:\x01\x30\x12\x1e\n\x16\x64isk_area_start_offset\x18\x0c \x01(\x03\x12\x34\n\ndelta_type\x18\n \x01(\x0e\x32 .cohesity.util.CBTDeltaType.Type\x12\x17\n\x0fmount_point_vec\x18\x0b \x03(\t2b\n\x15physical_virtual_disk\x12\x1b.cohesity.magneto.DiskProto\x18\x65 \x01(\x0b\x32&.cohesity.magneto.physical.VirtualDisk\"\xd8\x0c\n\x0cSnapshotInfo\x12>\n\x06status\x18\x02 \x01(\x0e\x32..cohesity.magneto.physical.SnapshotInfo.Status\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12=\n\x11\x61pp_user_messages\x18\x15 \x01(\x0b\x32\".cohesity.magneto.UserMessageProto\x12\x17\n\x0fjob_instance_id\x18\x04 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x05 \x01(\x05\x12=\n\rvirtual_disks\x18\x06 \x03(\x0b\x32&.cohesity.magneto.physical.VirtualDisk\x12\x34\n\rsub_tasks_vec\x18\x07 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12!\n\x19max_vhd_volume_size_bytes\x18\x12 \x01(\x03\x12I\n\x14server_snapshot_info\x18\x08 \x01(\x0b\x32+.cohesity.magneto.agents.ServerSnapshotInfo\x12,\n$virtual_disk_filepaths_to_be_deleted\x18\x10 \x03(\t\x12&\n\x1eserver_snapshot_info_file_name\x18\t \x01(\t\x12i\n%server_snapshot_serialized_fetch_info\x18\x14 \x01(\x0b\x32:.cohesity.magneto.agents.ServerSnapshotSerializedFetchInfo\x12\x39\n\x13take_snapshot_error\x18\n \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x43\n\x1d\x66\x65tch_snapshot_metadata_error\x18\x0f \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x42\n\x1cnotify_backup_complete_error\x18\x0b \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x36\n\x10\x65nd_backup_error\x18\x0c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12!\n\x19snapshot_deletion_pending\x18\x11 \x01(\x08\x12;\n\x15\x64\x65lete_snapshot_error\x18\r \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12:\n\x14\x61\x62ort_snapshot_error\x18\x0e \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x46\n\x0chost_summary\x18\x13 \x01(\x0b\x32\x30.cohesity.magneto.agents.SnapshotHostInfoSummary\x12;\n\nagent_info\x18\x16 \x01(\x0b\x32\'.cohesity.magneto.agents.AgentInfoProto\x12\x18\n\x10sub_file_size_mb\x18\x17 \x01(\x03\x12\x1e\n\x16system_backup_unc_path\x18\x18 \x01(\t\x12\x1e\n\x16system_backup_nfs_path\x18\x1b \x01(\t\x12\x1f\n\x17system_backup_view_name\x18\x19 \x01(\t\x12\x18\n\x10post_421a_backup\x18\x1a \x01(\x08\"\xa9\x01\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x1f\n\x1bkPrepareHostForSnapshotDone\x10\x01\x12\x12\n\x0ekSnapshotTaken\x10\x02\x12\x14\n\x10kSubTasksCreated\x10\x03\x12\x17\n\x13kSetupFilesFinished\x10\x04\x12\x15\n\x11kSubTasksFinished\x10\x05\x12\x16\n\x12kEndBackupFinished\x10\x06\x32l\n\x16physical_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18g \x01(\x0b\x32\'.cohesity.magneto.physical.SnapshotInfo\"&\n\x0cSystemBackup\x12\x16\n\x0eimage_filename\x18\x05 \x01(\t\"\xf2\x01\n\x10SparseHostConfig\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x31\n\thost_type\x18\x02 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type\x12\x19\n\x11os_version_string\x18\x03 \x01(\t\x12=\n\rvirtual_disks\x18\x04 \x03(\x0b\x32&.cohesity.magneto.physical.VirtualDisk\x12>\n\rsystem_backup\x18\x05 \x01(\x0b\x32\'.cohesity.magneto.physical.SystemBackup\"\xfa\x05\n\x0bRestoreInfo\x12;\n\x05state\x18\x01 \x01(\x0e\x32,.cohesity.magneto.physical.RestoreInfo.State\x12&\n\x1etotal_bytes_to_write_to_source\x18\x02 \x01(\x03\x12\x45\n\x08\x64isk_map\x18\x03 \x03(\x0b\x32\x33.cohesity.magneto.physical.RestoreInfo.DiskMapEntry\x12\x34\n\rsub_tasks_vec\x18\x04 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12;\n\x10\x63onnector_params\x18\x05 \x01(\x0b\x32!.cohesity.magneto.ConnectorParams\x12+\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x1an\n\x08\x44iskInfo\x12\x12\n\nimage_path\x18\x01 \x01(\t\x12\x35\n\x05vdisk\x18\x02 \x01(\x0b\x32&.cohesity.magneto.physical.VirtualDisk\x12\x17\n\x0fvolume_dev_path\x18\x03 \x01(\t\x1a_\n\x0c\x44iskMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.cohesity.magneto.physical.RestoreInfo.DiskInfo:\x02\x38\x01\"c\n\x05State\x12\x0c\n\x08kStarted\x10\x00\x12\x10\n\x0ckFilesCloned\x10\x01\x12\x14\n\x10kSubTasksCreated\x10\x02\x12\x15\n\x11kSubTasksFinished\x10\x03\x12\r\n\tkFinished\x10\x04\x32i\n\x15physical_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18m \x01(\x0b\x32&.cohesity.magneto.physical.RestoreInfoB\x1aZ\x18magneto/base/physical.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.physical_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030magneto/base/physical.pb'
  _globals['_RESTOREINFO_DISKMAPENTRY']._loaded_options = None
  _globals['_RESTOREINFO_DISKMAPENTRY']._serialized_options = b'8\001'
  _globals['_VIRTUALDISK']._serialized_start=248
  _globals['_VIRTUALDISK']._serialized_end=757
  _globals['_SNAPSHOTINFO']._serialized_start=760
  _globals['_SNAPSHOTINFO']._serialized_end=2384
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=2105
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=2274
  _globals['_SYSTEMBACKUP']._serialized_start=2386
  _globals['_SYSTEMBACKUP']._serialized_end=2424
  _globals['_SPARSEHOSTCONFIG']._serialized_start=2427
  _globals['_SPARSEHOSTCONFIG']._serialized_end=2669
  _globals['_RESTOREINFO']._serialized_start=2672
  _globals['_RESTOREINFO']._serialized_end=3434
  _globals['_RESTOREINFO_DISKINFO']._serialized_start=3019
  _globals['_RESTOREINFO_DISKINFO']._serialized_end=3129
  _globals['_RESTOREINFO_DISKMAPENTRY']._serialized_start=3131
  _globals['_RESTOREINFO_DISKMAPENTRY']._serialized_end=3226
  _globals['_RESTOREINFO_STATE']._serialized_start=3228
  _globals['_RESTOREINFO_STATE']._serialized_end=3327
# @@protoc_insertion_point(module_scope)
