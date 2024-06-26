# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/hyperv/hyperv.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.windows.base import hyperv_pb2 as magneto_dot_agents_dot_windows_dot_base_dot_hyperv__pb2
from magneto.agents.windows.base import file_attrs_pb2 as magneto_dot_agents_dot_windows_dot_base_dot_file__attrs__pb2
from magneto.base import cloud_pb2 as magneto_dot_base_dot_cloud__pb2
from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import storage_pb2 as magneto_dot_base_dot_storage__pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2
from magneto.connectors.file import file_pb2 as magneto_dot_connectors_dot_file_dot_file__pb2
from magneto.connectors.hyperv import hyperv_setup_restore_disks_pb2 as magneto_dot_connectors_dot_hyperv_dot_hyperv__setup__restore__disks__pb2
from util import cbt_delta_pb2 as util_dot_cbt__delta__pb2
from util.disklib.base import enums_pb2 as util_dot_disklib_dot_base_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/connectors/hyperv/hyperv.proto\x12\x17\x63ohesity.magneto.hyperv\x1a(magneto/agents/windows/base/hyperv.proto\x1a,magneto/agents/windows/base/file_attrs.proto\x1a\x18magneto/base/cloud.proto\x1a\x17magneto/base/disk.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1amagneto/base/storage.proto\x1a\x1bmagneto/base/sub_task.proto\x1a\"magneto/connectors/file/file.proto\x1a:magneto/connectors/hyperv/hyperv_setup_restore_disks.proto\x1a\x14util/cbt_delta.proto\x1a\x1dutil/disklib/base/enums.proto\"\xae\x07\n\x0bVirtualDisk\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\x12 \n\x18snapshot_device_filepath\x18\x14 \x01(\t\x12\x18\n\x10parent_full_path\x18\x13 \x01(\t\x12\x18\n\x10parent_disk_uuid\x18\x11 \x01(\t\x12\x10\n\x08\x63\x61pacity\x18\x04 \x01(\x03\x12\x19\n\x11logical_disk_size\x18\x15 \x01(\x03\x12;\n\x0b\x64isk_format\x18\x05 \x01(\x0e\x32&.cohesity.disklib.base.DiskFormat.Type\x12\x42\n\tdisk_type\x18\x06 \x01(\x0e\x32/.cohesity.disklib.base.VirtualHardDiskType.Type\x12\x0e\n\x06rct_id\x18\x07 \x01(\t\x12\x15\n\rsnapshot_uuid\x18\x12 \x01(\x0c\x12\x34\n\ndelta_type\x18\x08 \x01(\x0e\x32 .cohesity.util.CBTDeltaType.Type\x12/\n\ndelta_info\x18\t \x01(\x0b\x32\x1b.cohesity.util.CBTDeltaInfo\x12\x1f\n\x17last_position_backed_up\x18\n \x01(\x03\x12$\n\x1ctotal_bytes_read_from_source\x18\x0b \x01(\x03\x12\x18\n\x10\x65ncoded_filename\x18\x0c \x01(\t\x12\x1e\n\x16\x64isk_area_start_offset\x18\r \x01(\x03\x12\x36\n\x10query_disk_error\x18\x0e \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12H\n\x0f\x66ile_attributes\x18\x0f \x01(\x0b\x32/.cohesity.magneto.agents.windows.FileAttributes\x12&\n\x19logical_sector_size_bytes\x18\x10 \x01(\x05:\x03\x35\x31\x32\x12\x13\n\x0bunit_number\x18\x16 \x01(\x03\x12\x1d\n\x15\x63ontroller_bus_number\x18\x17 \x01(\x03\x12\x17\n\x0f\x63ontroller_type\x18\x18 \x01(\t*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x32^\n\x13hyperv_virtual_disk\x12\x1b.cohesity.magneto.DiskProto\x18g \x01(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\"\xf9\x01\n\x0fLargeConfigFile\x12G\n\x04type\x18\x01 \x01(\x0e\x32\x39.cohesity.magneto.agents.windows.hyperv.VMConfigFile.Type\x12\x32\n\x04\x62\x61se\x18\x02 \x01(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk2i\n\x11large_config_file\x12$.cohesity.magneto.hyperv.VirtualDisk\x18\x64 \x01(\x0b\x32(.cohesity.magneto.hyperv.LargeConfigFile\"\xa7\x02\n\x12LogicalVirtualDisk\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61pacity\x18\x03 \x01(\x03\x12;\n\rvirtual_disks\x18\x04 \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\x12&\n\x19logical_sector_size_bytes\x18\x05 \x01(\x05:\x03\x35\x31\x32\x12;\n\x0b\x64isk_format\x18\x06 \x01(\x0e\x32&.cohesity.disklib.base.DiskFormat.Type\x12\x42\n\tdisk_type\x18\x07 \x01(\x0e\x32/.cohesity.disklib.base.VirtualHardDiskType.Type\"\xf8\x04\n\x0eSparseVMConfig\x12L\n\x0ehyperv_vm_info\x18\x01 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.HyperVVMInfo\x12M\n\x18logical_virtual_disk_vec\x18\x05 \x03(\x0b\x32+.cohesity.magneto.hyperv.LogicalVirtualDisk\x12;\n\rvirtual_disks\x18\x02 \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\x12\\\n\x18\x61\x64\x64itional_file_info_vec\x18\x03 \x03(\x0b\x32:.cohesity.magneto.hyperv.SparseVMConfig.AdditionalFileInfo\x12\"\n\x1avm_snapshot_directory_path\x18\x04 \x01(\t\x12M\n\x1fuser_excluded_virtual_disks_vec\x18\x06 \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\x1a\xba\x01\n\x12\x41\x64\x64itionalFileInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12G\n\x04type\x18\x02 \x01(\x0e\x32\x39.cohesity.magneto.agents.windows.hyperv.VMConfigFile.Type\x12H\n\x0f\x66ile_attributes\x18\x03 \x01(\x0b\x32/.cohesity.magneto.agents.windows.FileAttributes\"(\n\nVolumeInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xf5\x12\n\x0cSnapshotInfo\x12\x0f\n\x07vm_name\x18\x01 \x01(\t\x12\x1e\n\x16\x63heckpoint_instance_id\x18\x02 \x01(\x0c\x12\x17\n\x0fjob_instance_id\x18\x03 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x04 \x01(\x05\x12\x14\n\x0chyperv_vm_id\x18\x0f \x01(\x0c\x12\x19\n\x11is_app_consistent\x18\x13 \x01(\x08\x12\"\n\x1avm_snapshot_directory_path\x18\x10 \x01(\t\x12P\n\x10permit_host_info\x18\x05 \x01(\x0b\x32\x36.cohesity.magneto.agents.windows.hyperv.HyperVHostInfo\x12\x43\n\x16permit_volume_info_vec\x18\x1e \x03(\x0b\x32#.cohesity.magneto.hyperv.VolumeInfo\x12,\n$datastore_throttling_feature_enabled\x18\x1f \x01(\x08\x12V\n\x16server_checkpoint_info\x18\x06 \x01(\x0b\x32\x36.cohesity.magneto.agents.windows.hyperv.CheckpointInfo\x12X\n\x16server_reference_point\x18\x07 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.hyperv.VMReferencePoint\x12<\n\x06status\x18\x08 \x01(\x0e\x32,.cohesity.magneto.hyperv.SnapshotInfo.Status\x12M\n\x15\x66\x65tched_file_info_vec\x18\t \x03(\x0b\x32..cohesity.magneto.hyperv.SnapshotInfo.FileInfo\x12\x17\n\x0fsnapshot_set_id\x18\x14 \x01(\x0c\x12\x19\n\x11is_snapshot_owner\x18\x15 \x01(\x08\x12!\n\x19snapshot_deletion_pending\x18\x16 \x01(\x08\x12;\n\rvirtual_disks\x18\n \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\x12M\n\x1fuser_excluded_virtual_disks_vec\x18\" \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk\x12\x44\n\x12large_config_files\x18  \x03(\x0b\x32(.cohesity.magneto.hyperv.LargeConfigFile\x12M\n\x18logical_virtual_disk_vec\x18\x17 \x03(\x0b\x32+.cohesity.magneto.hyperv.LogicalVirtualDisk\x12\x34\n\rsub_tasks_vec\x18\x0b \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12+\n\x05\x65rror\x18\x0c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12=\n\x11\x61pp_user_messages\x18\r \x01(\x0b\x32\".cohesity.magneto.UserMessageProto\x12\x46\n convert_to_reference_point_error\x18\x0e \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12=\n\x17snapshot_deletion_error\x18\x11 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x18\n\x10sub_file_size_mb\x18\x12 \x01(\x03\x12\x39\n\x13take_snapshot_error\x18\x18 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x42\n\x1cnotify_backup_complete_error\x18\x19 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12:\n\x14\x61\x62ort_snapshot_error\x18\x1a \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1c\n\x14\x64\x65lta_info_in_scribe\x18\x1b \x01(\x08\x12>\n\x18\x66\x65tch_vss_snapshot_error\x18\x1c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12/\n\x08networks\x18\x1d \x03(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x1e\n\x13num_locate_vm_calls\x18! \x01(\x05:\x01\x30\x1a\x98\x02\n\x08\x46ileInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12G\n\x04type\x18\x04 \x01(\x0e\x32\x39.cohesity.magneto.agents.windows.hyperv.VMConfigFile.Type\x12\x1b\n\ris_compressed\x18\x05 \x01(\x08:\x04true\x12H\n\x0f\x66ile_attributes\x18\x06 \x01(\x0b\x32/.cohesity.magneto.agents.windows.FileAttributes\x12\x0e\n\x06length\x18\x07 \x01(\x03\"\x82\x02\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x12\n\x0ekPermitGranted\x10\t\x12\x1f\n\x1bkPrepareHostForSnapshotDone\x10\x08\x12\x19\n\x15kCreateCheckpointDone\x10\x01\x12\x1a\n\x16kCheckpointInfoFetched\x10\x02\x12 \n\x1ckQueryChangesVirtualDiskDone\x10\x03\x12\x17\n\x13kSetupFilesFinished\x10\x04\x12\x14\n\x10kSubTasksCreated\x10\x05\x12\x15\n\x11kSubTasksFinished\x10\x06\x12\x16\n\x12kEndBackupFinished\x10\x07\x32h\n\x14hyperv_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18j \x01(\x0b\x32%.cohesity.magneto.hyperv.SnapshotInfo\"\xd1\x01\n\x12SnapshotScribeInfo\x12>\n\x10virtual_disk_vec\x18\x01 \x03(\x0b\x32$.cohesity.magneto.hyperv.VirtualDisk2{\n\x1bhyperv_snapshot_scribe_info\x12).cohesity.magneto.SnapshotScribeInfoProto\x18\x65 \x01(\x0b\x32+.cohesity.magneto.hyperv.SnapshotScribeInfo\"\xfd\x02\n\x19\x45ntitiesGroupSnapshotInfo\x12I\n\x06status\x18\x01 \x01(\x0e\x32\x39.cohesity.magneto.hyperv.EntitiesGroupSnapshotInfo.Status\x12\x17\n\x0fsnapshot_set_id\x18\x02 \x01(\x0c\"m\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x1f\n\x1bkPrepareHostForSnapshotDone\x10\x01\x12\x15\n\x11kTakeSnapshotDone\x10\x02\x12\r\n\tkFinished\x10\x03\x12\x0e\n\nkCancelled\x10\x04\x32\x8c\x01\n\x1ehyperv_vss_group_snapshot_info\x12\x30.cohesity.magneto.EntitiesGroupSnapshotInfoProto\x18\x65 \x01(\x0b\x32\x32.cohesity.magneto.hyperv.EntitiesGroupSnapshotInfo\"\x80\x07\n\x0bRestoreInfo\x12Q\n\x12restore_task_state\x18\x01 \x01(\x0e\x32\x35.cohesity.magneto.hyperv.RestoreInfo.RestoreTaskState\x12\x16\n\x0evm_folder_name\x18\x02 \x01(\t\x12\x1f\n\x11vm_folder_created\x18\x03 \x01(\x08:\x04true\x12\x1f\n\x17\x63lone_files_path_prefix\x18\x04 \x01(\t\x12\x1f\n\x17storage_vmotion_skipped\x18\x05 \x01(\x08\x12%\n\x1drestore_task_start_time_usecs\x18\x06 \x01(\x03\x12W\n\x13host_info_proto_map\x18\x07 \x03(\x0b\x32:.cohesity.magneto.hyperv.RestoreInfo.HostInfoProtoMapEntry\x12\x32\n$unmount_datastore_after_cancellation\x18\x08 \x01(\x08:\x04true\x1al\n\rHostInfoProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0fnas_mount_error\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x16\n\x0enas_mount_path\x18\x03 \x01(\t\x1ak\n\x15HostInfoProtoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.cohesity.magneto.hyperv.RestoreInfo.HostInfoProto:\x02\x38\x01\"\xac\x01\n\x10RestoreTaskState\x12\x0c\n\x08kStarted\x10\x00\x12\x0e\n\nkVMsCloned\x10\x01\x12\x11\n\rkHostAssigned\x10\x02\x12\x15\n\x11kDatastoreMounted\x10\x03\x12\x0e\n\nkVMCreated\x10\x04\x12\x17\n\x13kDatastoreUnmounted\x10\x05\x12\x12\n\x0ekPermitGranted\x10\x06\x12\x13\n\x0fkPermitReleased\x10\x07\x32\x65\n\x13hyperv_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18i \x01(\x0b\x32$.cohesity.magneto.hyperv.RestoreInfo\"\xd4\x06\n\x11RestoreEntityInfo\x12L\n\x05state\x18\x01 \x01(\x0e\x32=.cohesity.magneto.hyperv.RestoreEntityInfo.RestoreEntityState\x12I\n\thost_info\x18\x02 \x01(\x0b\x32\x36.cohesity.magneto.agents.windows.hyperv.HyperVHostInfo\x12M\n\x0c\x61gent_handle\x18\x03 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\x12\x41\n\x10sparse_vm_config\x18\x04 \x01(\x0b\x32\'.cohesity.magneto.hyperv.SparseVMConfig\x12W\n\x1c\x63hained_logical_disk_mapping\x18\x05 \x01(\x0b\x32\x31.cohesity.magneto.cloud.ChainedLogicalDiskMapping\x12\x43\n\x12restore_files_info\x18\x06 \x01(\x0b\x32\'.cohesity.magneto.RestoreFilesInfoProto\"c\n\x12RestoreEntityState\x12\x0c\n\x08kStarted\x10\x00\x12\r\n\tkImported\x10\x01\x12\x11\n\rkDataMigrated\x10\x02\x12\r\n\tkRealized\x10\x03\x12\x0e\n\nkFinalized\x10\x04\x32\x80\x01\n\x1ahyperv_restore_entity_info\x12\x30.cohesity.magneto.RestoreInfoProto.RestoreEntity\x18\x66 \x01(\x0b\x32*.cohesity.magneto.hyperv.RestoreEntityInfo2\x8d\x01\n\x1fhyperv_cloud_deploy_entity_info\x12\x38.cohesity.magneto.CloudDeployInfoProto.CloudDeployEntity\x18h \x01(\x0b\x32*.cohesity.magneto.hyperv.RestoreEntityInfo\"\xae\x01\n\x12\x45ntitySnapshotInfo\x12\x17\n\x0fsnapshot_set_id\x18\x01 \x01(\t2\x7f\n\x1fhyperv_vss_entity_snapshot_info\x12).cohesity.magneto.EntitySnapshotInfoProto\x18\x65 \x01(\x0b\x32+.cohesity.magneto.hyperv.EntitySnapshotInfo\"\xbc\x04\n\x10RestoreFilesInfo\x12S\n\ntask_state\x18\x01 \x01(\x0e\x32?.cohesity.magneto.hyperv.RestoreFilesInfo.RestoreFilesTaskState\x12R\n\x17restore_disks_task_info\x18\x02 \x01(\x0b\x32\x31.cohesity.magneto.hyperv.SetupRestoreDiskTaskInfo\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x35\n\x0ftear_down_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\xa3\x01\n\x15RestoreFilesTaskState\x12\x0c\n\x08kStarted\x10\x00\x12\x13\n\x0fkSetupCompleted\x10\x01\x12\x17\n\x13kCopyFilesInitiated\x10\x02\x12\x17\n\x13kCopyFilesCompleted\x10\x03\x12\x16\n\x12kTeardownInitiated\x10\x04\x12\r\n\tkFinished\x10\x05\x12\x0e\n\nkCancelled\x10\x06\x32u\n\x19hyperv_restore_files_info\x12\'.cohesity.magneto.RestoreFilesInfoProto\x18g \x01(\x0b\x32).cohesity.magneto.hyperv.RestoreFilesInfo\"\xf6\x02\n\x16RestoreEnvironmentInfo\x12\x45\n\x07vm_info\x18\x01 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.HyperVVMInfo\x12\x66\n\x15\x65ncoded_flat_file_map\x18\x02 \x03(\x0b\x32G.cohesity.magneto.hyperv.RestoreEnvironmentInfo.EncodedFlatFileMapEntry\x1a\x39\n\x17\x45ncodedFlatFileMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32r\n\x10restore_env_info\x12\'.cohesity.magneto.file.RestoreFilesInfo\x18\x66 \x01(\x0b\x32/.cohesity.magneto.hyperv.RestoreEnvironmentInfo\"\xef\x01\n\x15\x44\x65stroyClonedTaskInfo\x12I\n\rhost_info_vec\x18\x01 \x03(\x0b\x32\x32.cohesity.magneto.hyperv.RestoreInfo.HostInfoProto2\x8a\x01\n\"hyperv_destroy_cloned_vm_task_info\x12..cohesity.magneto.DestroyClonedVMTaskInfoProto\x18\x65 \x01(\x0b\x32..cohesity.magneto.hyperv.DestroyClonedTaskInfoB%Z#magneto/connectors/hyperv/hyperv.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.hyperv.hyperv_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#magneto/connectors/hyperv/hyperv.pb'
  _globals['_RESTOREINFO_HOSTINFOPROTOMAPENTRY']._loaded_options = None
  _globals['_RESTOREINFO_HOSTINFOPROTOMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREENVIRONMENTINFO_ENCODEDFLATFILEMAPENTRY']._loaded_options = None
  _globals['_RESTOREENVIRONMENTINFO_ENCODEDFLATFILEMAPENTRY']._serialized_options = b'8\001'
  _globals['_VIRTUALDISK']._serialized_start=494
  _globals['_VIRTUALDISK']._serialized_end=1436
  _globals['_LARGECONFIGFILE']._serialized_start=1439
  _globals['_LARGECONFIGFILE']._serialized_end=1688
  _globals['_LOGICALVIRTUALDISK']._serialized_start=1691
  _globals['_LOGICALVIRTUALDISK']._serialized_end=1986
  _globals['_SPARSEVMCONFIG']._serialized_start=1989
  _globals['_SPARSEVMCONFIG']._serialized_end=2621
  _globals['_SPARSEVMCONFIG_ADDITIONALFILEINFO']._serialized_start=2435
  _globals['_SPARSEVMCONFIG_ADDITIONALFILEINFO']._serialized_end=2621
  _globals['_VOLUMEINFO']._serialized_start=2623
  _globals['_VOLUMEINFO']._serialized_end=2663
  _globals['_SNAPSHOTINFO']._serialized_start=2666
  _globals['_SNAPSHOTINFO']._serialized_end=5087
  _globals['_SNAPSHOTINFO_FILEINFO']._serialized_start=4440
  _globals['_SNAPSHOTINFO_FILEINFO']._serialized_end=4720
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=4723
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=4981
  _globals['_SNAPSHOTSCRIBEINFO']._serialized_start=5090
  _globals['_SNAPSHOTSCRIBEINFO']._serialized_end=5299
  _globals['_ENTITIESGROUPSNAPSHOTINFO']._serialized_start=5302
  _globals['_ENTITIESGROUPSNAPSHOTINFO']._serialized_end=5683
  _globals['_ENTITIESGROUPSNAPSHOTINFO_STATUS']._serialized_start=5431
  _globals['_ENTITIESGROUPSNAPSHOTINFO_STATUS']._serialized_end=5540
  _globals['_RESTOREINFO']._serialized_start=5686
  _globals['_RESTOREINFO']._serialized_end=6582
  _globals['_RESTOREINFO_HOSTINFOPROTO']._serialized_start=6087
  _globals['_RESTOREINFO_HOSTINFOPROTO']._serialized_end=6195
  _globals['_RESTOREINFO_HOSTINFOPROTOMAPENTRY']._serialized_start=6197
  _globals['_RESTOREINFO_HOSTINFOPROTOMAPENTRY']._serialized_end=6304
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_start=6307
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_end=6479
  _globals['_RESTOREENTITYINFO']._serialized_start=6585
  _globals['_RESTOREENTITYINFO']._serialized_end=7437
  _globals['_RESTOREENTITYINFO_RESTOREENTITYSTATE']._serialized_start=7063
  _globals['_RESTOREENTITYINFO_RESTOREENTITYSTATE']._serialized_end=7162
  _globals['_ENTITYSNAPSHOTINFO']._serialized_start=7440
  _globals['_ENTITYSNAPSHOTINFO']._serialized_end=7614
  _globals['_RESTOREFILESINFO']._serialized_start=7617
  _globals['_RESTOREFILESINFO']._serialized_end=8189
  _globals['_RESTOREFILESINFO_RESTOREFILESTASKSTATE']._serialized_start=7907
  _globals['_RESTOREFILESINFO_RESTOREFILESTASKSTATE']._serialized_end=8070
  _globals['_RESTOREENVIRONMENTINFO']._serialized_start=8192
  _globals['_RESTOREENVIRONMENTINFO']._serialized_end=8566
  _globals['_RESTOREENVIRONMENTINFO_ENCODEDFLATFILEMAPENTRY']._serialized_start=8393
  _globals['_RESTOREENVIRONMENTINFO_ENCODEDFLATFILEMAPENTRY']._serialized_end=8450
  _globals['_DESTROYCLONEDTASKINFO']._serialized_start=8569
  _globals['_DESTROYCLONEDTASKINFO']._serialized_end=8808
# @@protoc_insertion_point(module_scope)
