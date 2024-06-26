# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/aws/aws_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from bridge.vault.base import vault_pb2 as bridge_dot_vault_dot_base_dot_vault__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.base.entities import aws_pb2 as magneto_dot_base_dot_entities_dot_aws__pb2
from magneto.base.entities import vmware_pb2 as magneto_dot_base_dot_entities_dot_vmware__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.connectors.aws import aws_pb2 as magneto_dot_connectors_dot_aws_dot_aws__pb2
from nexus.cloud.base import credentials_pb2 as nexus_dot_cloud_dot_base_dot_credentials__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$bridge/magneto/aws/aws_actions.proto\x12\x1b\x63ohesity.bridge.magneto.aws\x1a)bridge/magneto/base/magneto_actions.proto\x1a\x1d\x62ridge/vault/base/vault.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x17magneto/base/disk.proto\x1a\x1fmagneto/base/entities/aws.proto\x1a\"magneto/base/entities/vmware.proto\x1a\x19magneto/base/entity.proto\x1a magneto/connectors/aws/aws.proto\x1a\"nexus/cloud/base/credentials.proto\"\xdf\x03\n\x0e\x42\x61\x63kupAWSVMArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12>\n\x04type\x18\x02 \x01(\x0e\x32\x30.cohesity.bridge.magneto.aws.BackupAWSVMArg.Type\x12\x31\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.aws.Entity\x12/\n\tvm_entity\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.aws.Entity\x12\x31\n\tvm_config\x18\x05 \x01(\x0b\x32\x1e.cohesity.magneto.aws.VMConfig\x12#\n\x14\x65xported_root_volume\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x17\x65xported_disk_file_name\x18\x07 \x01(\t\x12\x1b\n\x0cuse_diff_api\x18\x08 \x01(\x08:\x05\x66\x61lse\"]\n\x04Type\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkSetupFiles\x10\x02\x12\x0f\n\x0bkBackupDisk\x10\x03\x12\x0f\n\x0bkEndSubTask\x10\x04\x12\x0e\n\nkEndBackup\x10\x05\"\xd9\t\n\rRestoreVMsArg\x12\x35\n\x04\x62\x61se\x18\n \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.cohesity.bridge.magneto.aws.RestoreVMsArg.Type\x12R\n\x10vm_restore_infos\x18\x02 \x03(\x0b\x32\x38.cohesity.bridge.magneto.aws.RestoreVMsArg.VMRestoreInfo\x12\x13\n\x0bview_box_id\x18\x03 \x01(\x03\x12\x1d\n\x15\x64\x65stination_view_name\x18\x04 \x01(\t\x12\x11\n\ts3_bucket\x18\x06 \x01(\t\x12\x39\n\x0b\x63redentials\x18\x07 \x01(\x0b\x32$.cohesity.nexus.cloud.AwsCredentials\x12\x12\n\naws_region\x18\x08 \x01(\t\x12G\n\tdisk_info\x18\t \x01(\x0b\x32\x34.cohesity.magneto.aws.CloudDeployEntityInfo.DiskInfo\x12 \n\x11use_ebs_write_api\x18\x0b \x01(\x08:\x05\x66\x61lse\x1a\xbc\x04\n\rVMRestoreInfo\x12\x32\n\tvm_entity\x18\x01 \x01(\x0b\x32\x1f.cohesity.magneto.vmware.Entity\x12-\n\x06\x65ntity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12`\n\x10\x61ws_entity_infos\x18\x02 \x03(\x0b\x32\x46.cohesity.bridge.magneto.aws.RestoreVMsArg.VMRestoreInfo.AWSEntityInfo\x12\"\n\x1asnapshot_relative_dir_path\x18\x03 \x01(\t\x1a\xc1\x02\n\rAWSEntityInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x19vm_disk_relative_filepath\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x03\x12G\n\tdisk_info\x18\x08 \x01(\x0b\x32\x34.cohesity.magneto.aws.CloudDeployEntityInfo.DiskInfo\x12-\n\x04\x61rea\x18\x05 \x01(\x0b\x32\x1f.cohesity.magneto.DiskAreaProto\x12Q\n\x19vm_disk_s3_upload_context\x18\x06 \x01(\x0b\x32..cohesity.bridge.vault.VaultUploadContextProto\x12\x10\n\x08part_num\x18\x07 \x01(\x05\x12\x14\n\x0cis_s3_object\x18\x02 \x01(\x08\"\xbd\x01\n\x04Type\x12\x10\n\x0ckRestoreDisk\x10\t\x12\x14\n\x10kCreateS3Objects\x10\x01\x12\x15\n\x11kCreateEBSVolumes\x10\x02\x12\x11\n\rkCopyDiskArea\x10\x03\x12\x16\n\x12kFinalizeS3Objects\x10\x04\x12\x0f\n\x0bkEndRestore\x10\x05\x12\x16\n\x12kDeleteAWSEntities\x10\x06\x12\x11\n\rkFetchVMsInfo\x10\x07\x12\x0f\n\x0bkEndSubTask\x10\x08\"\x93\x02\n\x0f\x44ownloadDiskArg\x12\x11\n\ts3_bucket\x18\x01 \x01(\t\x12\x16\n\x0es3_object_name\x18\x02 \x01(\t\x12\x39\n\x10object_area_info\x18\x03 \x01(\x0b\x32\x1f.cohesity.magneto.DiskAreaProto\x12\x39\n\x0b\x63redentials\x18\x04 \x01(\x0b\x32$.cohesity.nexus.cloud.AwsCredentials\x12\x12\n\naws_region\x18\x05 \x01(\t\x12\x13\n\x0bview_box_id\x18\x06 \x01(\x03\x12\x18\n\x10target_view_name\x18\x07 \x01(\t\x12\x1c\n\x14target_file_rel_path\x18\x08 \x01(\t\"\xab\x01\n\rCopyVolumeArg\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x11\n\tview_name\x18\x02 \x01(\t\x12\x19\n\x11src_file_rel_path\x18\x03 \x01(\t\x12\x1c\n\x14target_file_rel_path\x18\x04 \x01(\t\x12\x39\n\x10object_area_info\x18\x05 \x01(\x0b\x32\x1f.cohesity.magneto.DiskAreaProto\"\xc8\x04\n\x0c\x41WSActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x05 \x01(\x03:\x02-1\x12\x42\n\rbackup_vm_arg\x18\x07 \x01(\x0b\x32+.cohesity.bridge.magneto.aws.BackupAWSVMArg\x12\x43\n\x0frestore_vms_arg\x18\x02 \x01(\x0b\x32*.cohesity.bridge.magneto.aws.RestoreVMsArg\x12?\n\x0f\x63\x61ncel_task_arg\x18\x03 \x01(\x0b\x32&.cohesity.bridge.magneto.CancelTaskArg\x12G\n\x11\x64ownload_disk_arg\x18\x04 \x01(\x0b\x32,.cohesity.bridge.magneto.aws.DownloadDiskArg\x12\x43\n\x0f\x63opy_volume_arg\x18\x06 \x01(\x0b\x32*.cohesity.bridge.magneto.aws.CopyVolumeArg\x12H\n\nvault_type\x18\x08 \x01(\x0e\x32/.cohesity.configs.ClusterConfigProto.Vault.Type:\x03kS32l\n\x0e\x61ws_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18p \x01(\x0b\x32).cohesity.bridge.magneto.aws.AWSActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.aws.aws_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKUPAWSVMARG']._serialized_start=365
  _globals['_BACKUPAWSVMARG']._serialized_end=844
  _globals['_BACKUPAWSVMARG_TYPE']._serialized_start=751
  _globals['_BACKUPAWSVMARG_TYPE']._serialized_end=844
  _globals['_RESTOREVMSARG']._serialized_start=847
  _globals['_RESTOREVMSARG']._serialized_end=2088
  _globals['_RESTOREVMSARG_VMRESTOREINFO']._serialized_start=1324
  _globals['_RESTOREVMSARG_VMRESTOREINFO']._serialized_end=1896
  _globals['_RESTOREVMSARG_VMRESTOREINFO_AWSENTITYINFO']._serialized_start=1575
  _globals['_RESTOREVMSARG_VMRESTOREINFO_AWSENTITYINFO']._serialized_end=1896
  _globals['_RESTOREVMSARG_TYPE']._serialized_start=1899
  _globals['_RESTOREVMSARG_TYPE']._serialized_end=2088
  _globals['_DOWNLOADDISKARG']._serialized_start=2091
  _globals['_DOWNLOADDISKARG']._serialized_end=2366
  _globals['_COPYVOLUMEARG']._serialized_start=2369
  _globals['_COPYVOLUMEARG']._serialized_end=2540
  _globals['_AWSACTIONARG']._serialized_start=2543
  _globals['_AWSACTIONARG']._serialized_end=3127
# @@protoc_insertion_point(module_scope)
