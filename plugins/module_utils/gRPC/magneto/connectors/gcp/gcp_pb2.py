# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/gcp/gcp.proto
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
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import proxy_pb2 as magneto_dot_base_dot_proxy__pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2
from magneto.connectors.cloud import cloud_pb2 as magneto_dot_connectors_dot_cloud_dot_cloud__pb2
from magneto.connectors.file import file_pb2 as magneto_dot_connectors_dot_file_dot_file__pb2
from magneto.connectors.gcp import gcp_param_pb2 as magneto_dot_connectors_dot_gcp_dot_gcp__param__pb2
from util import cbt_delta_pb2 as util_dot_cbt__delta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n magneto/connectors/gcp/gcp.proto\x12\x14\x63ohesity.magneto.gcp\x1a\x17magneto/base/disk.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x18magneto/base/proxy.proto\x1a\x1bmagneto/base/sub_task.proto\x1a$magneto/connectors/cloud/cloud.proto\x1a\"magneto/connectors/file/file.proto\x1a&magneto/connectors/gcp/gcp_param.proto\x1a\x14util/cbt_delta.proto\"\x8a\x07\n\x0ePersistentDisk\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12>\n\x10\x64isk_device_info\x18\x02 \x01(\x0b\x32$.cohesity.magneto.gcp.DiskDeviceInfo\x12\x13\n\x0bsnapshot_id\x18\x03 \x01(\t\x12$\n\x1csnapshot_creation_time_usecs\x18\x04 \x01(\x03\x12Q\n\x12snapshot_disk_info\x18\x05 \x01(\x0b\x32\x35.cohesity.magneto.gcp.PersistentDisk.SnapshotDiskInfo\x12;\n\x06status\x18\x06 \x01(\x0e\x32+.cohesity.magneto.gcp.PersistentDisk.Status\x12\x34\n\ndelta_type\x18\x07 \x01(\x0e\x32 .cohesity.util.CBTDeltaType.Type\x12\x1f\n\x17last_position_backed_up\x18\x08 \x01(\x03\x12$\n\x1ctotal_bytes_read_from_source\x18\t \x01(\x03\x12\x18\n\x10\x65ncoded_filename\x18\n \x01(\t\x12+\n\x05\x65rror\x18\x0b \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1d\n\x15vm_disk_relative_path\x18\x0c \x01(\t\x1aj\n\x10SnapshotDiskInfo\x12%\n\x1dsnapshot_persistent_disk_name\x18\x01 \x01(\t\x12/\n\nproxy_info\x18\x02 \x01(\x0b\x32\x1b.cohesity.magneto.ProxyInfo\"\xb0\x01\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x14\n\x10kSnapshotCreated\x10\x01\x12\x15\n\x11kSnapshotFinished\x10\x02\x12\x15\n\x11kSnapshotAttached\x10\x03\x12\x15\n\x11kSubTasksFinished\x10\x04\x12\x15\n\x11kSnapshotDetached\x10\x05\x12\x10\n\x0ckDiskDeleted\x10\x06\x12\x14\n\x10kSnapshotDeleted\x10\x07\x32^\n\x13gcp_persistent_disk\x12\x1b.cohesity.magneto.DiskProto\x18l \x01(\x0b\x32$.cohesity.magneto.gcp.PersistentDisk\"\xa8\x02\n\x12VMNetworkInterface\x12\x12\n\nnetwork_ip\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08vpc_name\x18\x03 \x01(\t\x12\x13\n\x0bsubnet_name\x18\x04 \x01(\t\x12\x64\n\x12\x61\x63\x63\x65ss_configs_vec\x18\x05 \x03(\x0b\x32H.cohesity.magneto.gcp.VMNetworkInterface.VMNetworkInterfaceAccessConfigs\x1a\x63\n\x1fVMNetworkInterfaceAccessConfigs\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06nat_ip\x18\x03 \x01(\t\x12\x14\n\x0cnetwork_tier\x18\x04 \x01(\t\"\xfa\x04\n\x06VMDisk\x12\x0e\n\x02id\x18\x01 \x01(\x03:\x02-1\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x0bis_bootable\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x0c\n\x04mode\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\x1a\n\x0b\x61uto_delete\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x11\n\tinterface\x18\t \x01(\t\x12\x0c\n\x04type\x18\n \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x0b \x01(\t\x12\x0e\n\x06region\x18\x0c \x01(\t\x12\x15\n\rreplica_zones\x18\r \x03(\t\x12\x13\n\x07size_gb\x18\x0e \x01(\x05:\x02-1\x12\x10\n\x08licenses\x18\x0f \x03(\t\x12G\n\x11guest_os_features\x18\x10 \x03(\x0b\x32,.cohesity.magneto.gcp.VMDisk.GuestOsFeatures\x12K\n\x13\x64isk_encryption_key\x18\x11 \x01(\x0b\x32..cohesity.magneto.gcp.VMDisk.DiskEncryptionKey\x12?\n\nlabels_map\x18\x12 \x03(\x0b\x32+.cohesity.magneto.gcp.VMDisk.LabelsMapEntry\x1a\x1f\n\x0fGuestOsFeatures\x12\x0c\n\x04type\x18\x01 \x01(\t\x1a)\n\x11\x44iskEncryptionKey\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x1a\x30\n\x0eLabelsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x97\x01\n\nVMMetadata\x12\x13\n\x0b\x66ingerprint\x18\x01 \x01(\t\x12\x42\n\x05items\x18\x02 \x03(\x0b\x32\x33.cohesity.magneto.gcp.VMMetadata.VMMetadataKeyValue\x1a\x30\n\x12VMMetadataKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"Y\n\nScheduling\x12\x19\n\x11\x61utomatic_restart\x18\x01 \x01(\x08\x12\x1b\n\x13on_host_maintenance\x18\x02 \x01(\t\x12\x13\n\x0bpreemptible\x18\x03 \x01(\x08\"/\n\x0eServiceAccount\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t\"\x94\x05\n\x06VMInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x16\n\x0estatus_message\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12\x0e\n\x06region\x18\x12 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12K\n\x19vm_network_interfaces_vec\x18\t \x03(\x0b\x32(.cohesity.magneto.gcp.VMNetworkInterface\x12\x35\n\x0bvm_metadata\x18\n \x01(\x0b\x32 .cohesity.magneto.gcp.VMMetadata\x12\x32\n\x0cvm_disks_vec\x18\x0b \x03(\x0b\x32\x1c.cohesity.magneto.gcp.VMDisk\x12\x0f\n\x07vm_tags\x18\x0c \x03(\t\x12?\n\nlabels_map\x18\r \x03(\x0b\x32+.cohesity.magneto.gcp.VMInfo.LabelsMapEntry\x12\"\n\x13\x64\x65letion_protection\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0e\x63\x61n_ip_forward\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x34\n\nscheduling\x18\x10 \x01(\x0b\x32 .cohesity.magneto.gcp.Scheduling\x12>\n\x10service_accounts\x18\x11 \x03(\x0b\x32$.cohesity.magneto.gcp.ServiceAccount\x1a\x30\n\x0eLabelsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x08VMConfig\x12-\n\x07vm_info\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.gcp.VMInfo\x12\x42\n\x14persistent_disks_vec\x18\x02 \x03(\x0b\x32$.cohesity.magneto.gcp.PersistentDisk\"\x95\x06\n\x0cSnapshotInfo\x12\x17\n\x0fjob_instance_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x03 \x01(\x05\x12\x34\n\x0esource_vm_info\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.gcp.VMInfo\x12\x39\n\x06status\x18\x06 \x01(\x0e\x32).cohesity.magneto.gcp.SnapshotInfo.Status\x12\x33\n\x05\x64isks\x18\x07 \x03(\x0b\x32$.cohesity.magneto.gcp.PersistentDisk\x12\x34\n\rsub_tasks_vec\x18\x08 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12+\n\x05\x65rror\x18\t \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12=\n\x17snapshot_deletion_error\x18\n \x03(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x10\n\x08quiesced\x18\x0b \x01(\x08\x12\x18\n\x10sub_file_size_mb\x18\x0c \x01(\x03\x12\x0e\n\x06region\x18\r \x01(\t\x12\x0c\n\x04zone\x18\x0e \x01(\t\x12\x0e\n\x06subnet\x18\x0f \x01(\t\x12&\n\x17multiple_subnet_enabled\x18\x10 \x01(\x08:\x05\x66\x61lse\"\xa8\x01\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x12\n\x0ekVMInfoFetched\x10\x01\x12\x1e\n\x1akCreateSnapshotInitialized\x10\x02\x12\x14\n\x10kSubTasksCreated\x10\x03\x12\x17\n\x13kSetupFilesFinished\x10\x04\x12\x15\n\x11kSubTasksFinished\x10\x05\x12\x16\n\x12kEndBackupFinished\x10\x06\x32\x62\n\x11gcp_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18r \x01(\x0b\x32\".cohesity.magneto.gcp.SnapshotInfo\"\xcb\x08\n\x15\x43loudDeployEntityInfo\x12\x43\n\x07vm_info\x18\x01 \x01(\x0b\x32\x32.cohesity.magneto.gcp.CloudDeployEntityInfo.VMInfo\x12\x42\n\x0b\x63ommon_info\x18\x02 \x01(\x0b\x32-.cohesity.magneto.cloud.CloudEntityCommonInfo\x1a\x8e\x02\n\x08\x44iskInfo\x12\x1d\n\x15vm_disk_relative_path\x18\x01 \x01(\t\x12\x1b\n\x0cis_boot_disk\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12\x16\n\x0e\x63opy_disk_name\x18\x04 \x01(\t\x12\x1a\n\x12restored_disk_name\x18\x05 \x01(\t\x12;\n\rrestored_disk\x18\x06 \x01(\x0b\x32$.cohesity.magneto.gcp.PersistentDisk\x12>\n\x10\x64isk_device_info\x18\x07 \x01(\x0b\x32$.cohesity.magneto.gcp.DiskDeviceInfo\x1a\x89\x03\n\x06VMInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16restored_instance_name\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12Z\n\rdisk_info_map\x18\x04 \x03(\x0b\x32\x43.cohesity.magneto.gcp.CloudDeployEntityInfo.VMInfo.DiskInfoMapEntry\x12\x16\n\x0e\x62oot_disk_name\x18\x05 \x01(\t\x12\x31\n\tvm_config\x18\x06 \x01(\x0b\x32\x1e.cohesity.magneto.gcp.VMConfig\x12\x0e\n\x06region\x18\x07 \x01(\t\x12\x0c\n\x04zone\x18\x08 \x01(\t\x12\x0e\n\x06subnet\x18\t \x01(\t\x1ah\n\x10\x44iskInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.gcp.CloudDeployEntityInfo.DiskInfo:\x02\x38\x01\x32~\n\x17gcp_restore_entity_info\x12\x30.cohesity.magneto.RestoreInfoProto.RestoreEntity\x18k \x01(\x0b\x32+.cohesity.magneto.gcp.CloudDeployEntityInfo2\x8b\x01\n\x1cgcp_cloud_deploy_entity_info\x12\x38.cohesity.magneto.CloudDeployInfoProto.CloudDeployEntity\x18g \x01(\x0b\x32+.cohesity.magneto.gcp.CloudDeployEntityInfo\"\xab\x06\n\x0f\x43loudDeployInfo\x12<\n\x06status\x18\x01 \x01(\x0e\x32,.cohesity.magneto.gcp.CloudDeployInfo.Status\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x39\n\x13view_deletion_error\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x34\n\rsub_tasks_vec\x18\x04 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12&\n\x1etotal_bytes_to_write_to_source\x18\x05 \x01(\x03\x12\'\n\x18permit_on_restore_region\x18\x06 \x01(\x08:\x05\x66\x61lse\x12&\n\x17multiple_subnet_enabled\x18\x07 \x01(\x08:\x05\x66\x61lse\"\xef\x01\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x0b\n\x07kCloned\x10\x01\x12\x12\n\x0ekVMInfoFetched\x10\x02\x12\x12\n\x0ekPermitGranted\x10\x03\x12\x12\n\x0ekDisksAttached\x10\x04\x12\x14\n\x10kSubTasksCreated\x10\x05\x12\x15\n\x11kSubTasksFinished\x10\x06\x12\x15\n\x11kSnapshotsCreated\x10\x07\x12\x12\n\x0ekDisksRestored\x10\x08\x12\x0e\n\nkVMCreated\x10\x0b\x12\x17\n\x13kEndRestoreFinished\x10\t\x12\r\n\tkFinished\x10\n2c\n\x10gcp_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18p \x01(\x0b\x32%.cohesity.magneto.gcp.CloudDeployInfo2l\n\x15gcp_cloud_deploy_info\x12&.cohesity.magneto.CloudDeployInfoProto\x18\x66 \x01(\x0b\x32%.cohesity.magneto.gcp.CloudDeployInfo\"\xd5\x02\n\x17GcpVMRestoreSubTaskInfo\x12\x44\n\x06status\x18\x01 \x01(\x0e\x32\x34.cohesity.magneto.gcp.GcpVMRestoreSubTaskInfo.Status\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"S\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x0f\n\x0bkDiskCopied\x10\x01\x12\x11\n\rkDiskRestored\x10\x02\x12\x17\n\x13kProxyVMDiskDeleted\x10\x03\x32r\n\x1cgcp_vm_restore_sub_task_info\x12\x1d.cohesity.magneto.SubTaskInfo\x18n \x01(\x0b\x32-.cohesity.magneto.gcp.GcpVMRestoreSubTaskInfo\"\xc5\x05\n\x16RestoreEnvironmentInfo\x12\x34\n\x0eserver_vm_info\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.gcp.VMInfo\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t\x12\x13\n\x0bprivate_key\x18\x04 \x01(\t\x12/\n\nproxy_info\x18\x05 \x01(\x0b\x32\x1b.cohesity.magneto.ProxyInfo\x12\x16\n\x0e\x63opy_disk_name\x18\x06 \x01(\t\x12\x15\n\rsnapshot_name\x18\x07 \x01(\t\x12\x16\n\x0euser_disk_name\x18\x08 \x01(\t\x12\x1d\n\x15user_disk_device_name\x18\t \x01(\t\x12\x19\n\x11https_trigger_url\x18\n \x01(\t\x12L\n\x0c\x66ile_batches\x18\x0b \x03(\x0b\x32\x36.cohesity.magneto.gcp.RestoreEnvironmentInfo.FileBatch\x12\x43\n\x06status\x18\x0c \x01(\x0e\x32\x33.cohesity.magneto.gcp.RestoreEnvironmentInfo.Status\x1aX\n\tFileBatch\x12\x14\n\x0c\x62\x61tch_number\x18\x01 \x01(\x05\x12\x1b\n\x13\x61\x62solute_file_paths\x18\x02 \x03(\t\x12\x18\n\tprocessed\x18\x03 \x01(\x08:\x05\x66\x61lse\"*\n\x06Status\x12\x0c\n\x08kStarted\x10\x01\x12\x12\n\x0ekVMInfoFetched\x10\x02\x32o\n\x10restore_env_info\x12\'.cohesity.magneto.file.RestoreFilesInfo\x18h \x01(\x0b\x32,.cohesity.magneto.gcp.RestoreEnvironmentInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.gcp.gcp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VMDISK_LABELSMAPENTRY']._loaded_options = None
  _globals['_VMDISK_LABELSMAPENTRY']._serialized_options = b'8\001'
  _globals['_VMINFO_LABELSMAPENTRY']._loaded_options = None
  _globals['_VMINFO_LABELSMAPENTRY']._serialized_options = b'8\001'
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO_DISKINFOMAPENTRY']._loaded_options = None
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO_DISKINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_PERSISTENTDISK']._serialized_start=329
  _globals['_PERSISTENTDISK']._serialized_end=1235
  _globals['_PERSISTENTDISK_SNAPSHOTDISKINFO']._serialized_start=854
  _globals['_PERSISTENTDISK_SNAPSHOTDISKINFO']._serialized_end=960
  _globals['_PERSISTENTDISK_STATUS']._serialized_start=963
  _globals['_PERSISTENTDISK_STATUS']._serialized_end=1139
  _globals['_VMNETWORKINTERFACE']._serialized_start=1238
  _globals['_VMNETWORKINTERFACE']._serialized_end=1534
  _globals['_VMNETWORKINTERFACE_VMNETWORKINTERFACEACCESSCONFIGS']._serialized_start=1435
  _globals['_VMNETWORKINTERFACE_VMNETWORKINTERFACEACCESSCONFIGS']._serialized_end=1534
  _globals['_VMDISK']._serialized_start=1537
  _globals['_VMDISK']._serialized_end=2171
  _globals['_VMDISK_GUESTOSFEATURES']._serialized_start=2047
  _globals['_VMDISK_GUESTOSFEATURES']._serialized_end=2078
  _globals['_VMDISK_DISKENCRYPTIONKEY']._serialized_start=2080
  _globals['_VMDISK_DISKENCRYPTIONKEY']._serialized_end=2121
  _globals['_VMDISK_LABELSMAPENTRY']._serialized_start=2123
  _globals['_VMDISK_LABELSMAPENTRY']._serialized_end=2171
  _globals['_VMMETADATA']._serialized_start=2174
  _globals['_VMMETADATA']._serialized_end=2325
  _globals['_VMMETADATA_VMMETADATAKEYVALUE']._serialized_start=2277
  _globals['_VMMETADATA_VMMETADATAKEYVALUE']._serialized_end=2325
  _globals['_SCHEDULING']._serialized_start=2327
  _globals['_SCHEDULING']._serialized_end=2416
  _globals['_SERVICEACCOUNT']._serialized_start=2418
  _globals['_SERVICEACCOUNT']._serialized_end=2465
  _globals['_VMINFO']._serialized_start=2468
  _globals['_VMINFO']._serialized_end=3128
  _globals['_VMINFO_LABELSMAPENTRY']._serialized_start=2123
  _globals['_VMINFO_LABELSMAPENTRY']._serialized_end=2171
  _globals['_VMCONFIG']._serialized_start=3130
  _globals['_VMCONFIG']._serialized_end=3255
  _globals['_SNAPSHOTINFO']._serialized_start=3258
  _globals['_SNAPSHOTINFO']._serialized_end=4047
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=3779
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=3947
  _globals['_CLOUDDEPLOYENTITYINFO']._serialized_start=4050
  _globals['_CLOUDDEPLOYENTITYINFO']._serialized_end=5149
  _globals['_CLOUDDEPLOYENTITYINFO_DISKINFO']._serialized_start=4213
  _globals['_CLOUDDEPLOYENTITYINFO_DISKINFO']._serialized_end=4483
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO']._serialized_start=4486
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO']._serialized_end=4879
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO_DISKINFOMAPENTRY']._serialized_start=4775
  _globals['_CLOUDDEPLOYENTITYINFO_VMINFO_DISKINFOMAPENTRY']._serialized_end=4879
  _globals['_CLOUDDEPLOYINFO']._serialized_start=5152
  _globals['_CLOUDDEPLOYINFO']._serialized_end=5963
  _globals['_CLOUDDEPLOYINFO_STATUS']._serialized_start=5513
  _globals['_CLOUDDEPLOYINFO_STATUS']._serialized_end=5752
  _globals['_GCPVMRESTORESUBTASKINFO']._serialized_start=5966
  _globals['_GCPVMRESTORESUBTASKINFO']._serialized_end=6307
  _globals['_GCPVMRESTORESUBTASKINFO_STATUS']._serialized_start=6108
  _globals['_GCPVMRESTORESUBTASKINFO_STATUS']._serialized_end=6191
  _globals['_RESTOREENVIRONMENTINFO']._serialized_start=6310
  _globals['_RESTOREENVIRONMENTINFO']._serialized_end=7019
  _globals['_RESTOREENVIRONMENTINFO_FILEBATCH']._serialized_start=6774
  _globals['_RESTOREENVIRONMENTINFO_FILEBATCH']._serialized_end=6862
  _globals['_RESTOREENVIRONMENTINFO_STATUS']._serialized_start=6864
  _globals['_RESTOREENVIRONMENTINFO_STATUS']._serialized_end=6906
# @@protoc_insertion_point(module_scope)
