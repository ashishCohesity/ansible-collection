# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/acropolis/acropolis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2
from magneto.connectors.acropolis import acropolis_param_pb2 as magneto_dot_connectors_dot_acropolis_dot_acropolis__param__pb2
from magneto.connectors.file import file_pb2 as magneto_dot_connectors_dot_file_dot_file__pb2
from util import cbt_delta_pb2 as util_dot_cbt__delta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,magneto/connectors/acropolis/acropolis.proto\x12\x1a\x63ohesity.magneto.acropolis\x1a\x17magneto/base/disk.proto\x1a\x18magneto/base/error.proto\x1a\x19magneto/base/entity.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1bmagneto/base/sub_task.proto\x1a\x32magneto/connectors/acropolis/acropolis_param.proto\x1a\"magneto/connectors/file/file.proto\x1a\x14util/cbt_delta.proto\"\xd9\x04\n\x0bVirtualDisk\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x1c\n\x14hypervisor_disk_uuid\x18\x0f \x01(\t\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\x12\x19\n\x11snapshot_filepath\x18\x04 \x01(\t\x12\x16\n\x0e\x63\x61pacity_bytes\x18\x05 \x01(\x03\x12\x1e\n\x16storage_container_uuid\x18\x06 \x01(\t\x12\x19\n\x11lun_serial_number\x18\x07 \x01(\t\x12\x15\n\rtarget_suffix\x18\x0e \x01(\t\x12\x34\n\ndelta_type\x18\x08 \x01(\x0e\x32 .cohesity.util.CBTDeltaType.Type\x12/\n\ndelta_info\x18\t \x01(\x0b\x32\x1b.cohesity.util.CBTDeltaInfo\x12\x1f\n\x17last_position_backed_up\x18\n \x01(\x03\x12$\n\x1ctotal_bytes_read_from_source\x18\x0b \x01(\x03\x12\x18\n\x10\x65ncoded_filename\x18\x0c \x01(\t\x12\x36\n\x10query_disk_error\x18\r \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x14\n\x0c\x64isk_address\x18\x10 \x01(\t2d\n\x16\x61\x63ropolis_virtual_disk\x12\x1b.cohesity.magneto.DiskProto\x18h \x01(\x0b\x32\'.cohesity.magneto.acropolis.VirtualDisk\"\x90\x01\n\x08VMConfig\x12@\n\x0eserver_vm_info\x18\x01 \x01(\x0b\x32(.cohesity.magneto.acropolis.VMInfoResult\x12\x42\n\x11virtual_disks_vec\x18\x02 \x03(\x0b\x32\'.cohesity.magneto.acropolis.VirtualDisk\"\xe4\x01\n\x0fVolumeGroupInfo\x12\x19\n\x11volume_group_uuid\x18\x01 \x01(\t\x12\x19\n\x11volume_group_name\x18\x02 \x01(\t\x12+\n#volume_group_uuid_client_identifier\x18\x03 \x01(\t2n\n\x11volume_group_info\x12&.cohesity.magneto.ExternalSnapshotInfo\x18\x64 \x01(\x0b\x32+.cohesity.magneto.acropolis.VolumeGroupInfo\"\xd2\x01\n\x10\x45xternalRepoInfo\x12\x1e\n\x16\x65xternal_repo_uuid_vec\x18\x01 \x03(\t\x12,\n$external_repo_uuid_client_identifier\x18\x03 \x01(\t2p\n\x12\x65xternal_repo_info\x12&.cohesity.magneto.ExternalSnapshotInfo\x18g \x01(\x0b\x32,.cohesity.magneto.acropolis.ExternalRepoInfo\"\xbf\x01\n\x16\x41\x64\x64itionalSnapshotInfo\x12\'\n\x1fsnapshot_uuid_client_identifier\x18\x01 \x01(\t2|\n\x18\x61\x64\x64itional_snapshot_info\x12&.cohesity.magneto.ExternalSnapshotInfo\x18\x65 \x01(\x0b\x32\x32.cohesity.magneto.acropolis.AdditionalSnapshotInfo\"\xfa\x0b\n\x0cSnapshotInfo\x12\x0f\n\x07vm_name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_uuid\x18\x02 \x01(\x0c\x12\x17\n\x0fjob_instance_id\x18\x03 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x04 \x01(\x05\x12@\n\x0eserver_vm_info\x18\x05 \x01(\x0b\x32(.cohesity.magneto.acropolis.VMInfoResult\x12?\n\x06status\x18\x06 \x01(\x0e\x32/.cohesity.magneto.acropolis.SnapshotInfo.Status\x12\x42\n\x11virtual_disks_vec\x18\x07 \x03(\x0b\x32\'.cohesity.magneto.acropolis.VirtualDisk\x12P\n\x1fuser_excluded_virtual_disks_vec\x18\x19 \x03(\x0b\x32\'.cohesity.magneto.acropolis.VirtualDisk\x12\x19\n\x11volume_group_name\x18\x08 \x01(\t\x12\x19\n\x11volume_group_uuid\x18\t \x01(\t\x12\x16\n\x0e\x63lient_iqn_vec\x18\n \x03(\t\x12\x34\n\rsub_tasks_vec\x18\x0b \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12+\n\x05\x65rror\x18\x0c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12=\n\x17snapshot_deletion_error\x18\r \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x41\n\x1bvolume_group_deletion_error\x18\x11 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x10\n\x08quiesced\x18\x0e \x01(\x08\x12 \n\x18\x64\x61ta_services_ip_address\x18\x0f \x01(\t\x12\x18\n\x10sub_file_size_mb\x18\x10 \x01(\x03\x12\x33\n$datastore_throttling_feature_enabled\x18\x12 \x01(\x08:\x05\x66\x61lse\x12?\n\x18storage_containers_in_vm\x18\x13 \x03(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12.\n&ngt_capable_of_app_consistent_snapshot\x18\x14 \x01(\x08\x12!\n\x19ss_uuid_client_identifier\x18\x15 \x01(\t\x12!\n\x19vg_uuid_client_identifier\x18\x16 \x01(\t\x12\x42\n\x1csnapshot_uuid_deletion_error\x18\x17 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x46\n volume_group_uuid_deletion_error\x18\x18 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\x91\x02\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x12\n\x0ekVMInfoFetched\x10\n\x12\x1a\n\x16kSnapshotUuidGenerated\x10\x01\x12\x17\n\x13kCreateSnapshotDone\x10\x02\x12 \n\x1ckQueryChangesVirtualDiskDone\x10\x03\x12\x17\n\x13kVolumeGroupCreated\x10\x04\x12\x14\n\x10kSubTasksCreated\x10\x05\x12\x17\n\x13kSetupFilesFinished\x10\x06\x12\x15\n\x11kSubTasksFinished\x10\x07\x12\x16\n\x12kEndBackupFinished\x10\x08\x12\x17\n\x13kVolumeGroupDeleted\x10\t2n\n\x17\x61\x63ropolis_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18k \x01(\x0b\x32(.cohesity.magneto.acropolis.SnapshotInfo\"\xbb\t\n\x0eVMRecoveryInfo\x12W\n\x12restore_task_state\x18\x01 \x01(\x0e\x32;.cohesity.magneto.acropolis.VMRecoveryInfo.RecoverTaskState\x12\x19\n\x11volume_group_name\x18\x02 \x01(\t\x12\x19\n\x11volume_group_uuid\x18\x03 \x01(\t\x12&\n\x1etotal_bytes_to_write_to_source\x18\x04 \x01(\x03\x12\x16\n\x0e\x63lient_iqn_vec\x18\x05 \x03(\t\x12\x34\n\rsub_tasks_vec\x18\x06 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12 \n\x18\x64\x61ta_services_ip_address\x18\x07 \x01(\t\x12!\n\x19vg_uuid_client_identifier\x18\x08 \x01(\t\x12\x41\n\x1bvolume_group_deletion_error\x18\t \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x46\n volume_group_uuid_deletion_error\x18\n \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12!\n\x19\x65r_uuid_client_identifier\x18\x0b \x01(\t\x12<\n\x16\x65r_uuid_deletion_error\x18\x0c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12U\n\x10\x65r_repo_info_vec\x18\r \x03(\x0b\x32;.cohesity.magneto.acropolis.VMRecoveryInfo.ExternalRepoInfo\x12\x61\n\x16\x64s_uuid_to_er_uuid_map\x18\x0e \x03(\x0b\x32\x41.cohesity.magneto.acropolis.VMRecoveryInfo.DsUuidToErUuidMapEntry\x1a\x99\x01\n\x10\x45xternalRepoInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\x11\x65r_deletion_error\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11server_ip_address\x18\x04 \x01(\t\x12\x15\n\rvms_index_vec\x18\x05 \x03(\x05\x1a\x38\n\x16\x44sUuidToErUuidMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe2\x01\n\x10RecoverTaskState\x12\x0c\n\x08kStarted\x10\x00\x12\x13\n\x0fkVMsFilesCloned\x10\x01\x12\x13\n\x0fkUuidsGenerated\x10\x02\x12\x17\n\x13kVolumeGroupCreated\x10\x03\x12\x14\n\x10kSubTasksCreated\x10\x04\x12\x15\n\x11kSubTasksFinished\x10\x05\x12\x0e\n\nkCreatedVM\x10\x06\x12\x17\n\x13kVolumeGroupDeleted\x10\x07\x12\r\n\tkFinished\x10\x08\x12\x18\n\x14kExternalRepoCreated\x10\t\"\xed\x01\n\x0bRestoreInfo\x12\x44\n\x10vm_recovery_info\x18\x01 \x01(\x0b\x32*.cohesity.magneto.acropolis.VMRecoveryInfo\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto2k\n\x16\x61\x63ropolis_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18j \x01(\x0b\x32\'.cohesity.magneto.acropolis.RestoreInfo\"\xba\x05\n\x11RestoreEntityInfo\x12\x45\n\x07vm_info\x18\x01 \x01(\x0b\x32\x34.cohesity.magneto.acropolis.RestoreEntityInfo.VMInfo\x1an\n\x0e\x44\x61tasourceInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12!\n\x19migration_suspended_count\x18\x02 \x01(\x05\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x1a\xe4\x02\n\x06VMInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\tvm_config\x18\x03 \x01(\x0b\x32$.cohesity.magneto.acropolis.VMConfig\x12\x42\n\x11virtual_disks_vec\x18\x04 \x03(\x0b\x32\'.cohesity.magneto.acropolis.VirtualDisk\x12_\n\x19\x66inished_ds_migration_vec\x18\x05 \x03(\x0b\x32<.cohesity.magneto.acropolis.RestoreEntityInfo.DatasourceInfo\x12`\n\x1asuspended_ds_migration_vec\x18\x06 \x03(\x0b\x32<.cohesity.magneto.acropolis.RestoreEntityInfo.DatasourceInfo2\x86\x01\n\x1d\x61\x63ropolis_restore_entity_info\x12\x30.cohesity.magneto.RestoreInfoProto.RestoreEntity\x18g \x01(\x0b\x32-.cohesity.magneto.acropolis.RestoreEntityInfo\"\xe2\x01\n\x16RestoreEnvironmentInfo\x12@\n\x0eserver_vm_info\x18\x01 \x01(\x0b\x32(.cohesity.magneto.acropolis.VMInfoResult\x12\x0f\n\x07vm_uuid\x18\x02 \x01(\t2u\n\x10restore_env_info\x12\'.cohesity.magneto.file.RestoreFilesInfo\x18\x64 \x01(\x0b\x32\x32.cohesity.magneto.acropolis.RestoreEnvironmentInfoB+Z)magneto/connectors/acropolis/acropolis.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.acropolis.acropolis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)magneto/connectors/acropolis/acropolis.pb'
  _globals['_VMRECOVERYINFO_DSUUIDTOERUUIDMAPENTRY']._loaded_options = None
  _globals['_VMRECOVERYINFO_DSUUIDTOERUUIDMAPENTRY']._serialized_options = b'8\001'
  _globals['_VIRTUALDISK']._serialized_start=322
  _globals['_VIRTUALDISK']._serialized_end=923
  _globals['_VMCONFIG']._serialized_start=926
  _globals['_VMCONFIG']._serialized_end=1070
  _globals['_VOLUMEGROUPINFO']._serialized_start=1073
  _globals['_VOLUMEGROUPINFO']._serialized_end=1301
  _globals['_EXTERNALREPOINFO']._serialized_start=1304
  _globals['_EXTERNALREPOINFO']._serialized_end=1514
  _globals['_ADDITIONALSNAPSHOTINFO']._serialized_start=1517
  _globals['_ADDITIONALSNAPSHOTINFO']._serialized_end=1708
  _globals['_SNAPSHOTINFO']._serialized_start=1711
  _globals['_SNAPSHOTINFO']._serialized_end=3241
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=2856
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=3129
  _globals['_VMRECOVERYINFO']._serialized_start=3244
  _globals['_VMRECOVERYINFO']._serialized_end=4455
  _globals['_VMRECOVERYINFO_EXTERNALREPOINFO']._serialized_start=4015
  _globals['_VMRECOVERYINFO_EXTERNALREPOINFO']._serialized_end=4168
  _globals['_VMRECOVERYINFO_DSUUIDTOERUUIDMAPENTRY']._serialized_start=4170
  _globals['_VMRECOVERYINFO_DSUUIDTOERUUIDMAPENTRY']._serialized_end=4226
  _globals['_VMRECOVERYINFO_RECOVERTASKSTATE']._serialized_start=4229
  _globals['_VMRECOVERYINFO_RECOVERTASKSTATE']._serialized_end=4455
  _globals['_RESTOREINFO']._serialized_start=4458
  _globals['_RESTOREINFO']._serialized_end=4695
  _globals['_RESTOREENTITYINFO']._serialized_start=4698
  _globals['_RESTOREENTITYINFO']._serialized_end=5396
  _globals['_RESTOREENTITYINFO_DATASOURCEINFO']._serialized_start=4790
  _globals['_RESTOREENTITYINFO_DATASOURCEINFO']._serialized_end=4900
  _globals['_RESTOREENTITYINFO_VMINFO']._serialized_start=4903
  _globals['_RESTOREENTITYINFO_VMINFO']._serialized_end=5259
  _globals['_RESTOREENVIRONMENTINFO']._serialized_start=5399
  _globals['_RESTOREENVIRONMENTINFO']._serialized_end=5625
# @@protoc_insertion_point(module_scope)
