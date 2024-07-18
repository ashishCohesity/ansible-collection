# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/vmware/vmware_setup_restore_disks.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base.entities import vmware_common_pb2 as magneto_dot_base_dot_entities_dot_vmware__common__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import storage_pb2 as magneto_dot_base_dot_storage__pb2
from yoda.base import volume_info_pb2 as yoda_dot_base_dot_volume__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:magneto/connectors/vmware/vmware_setup_restore_disks.proto\x12\x17\x63ohesity.magneto.vmware\x1a\x1fmagneto/agents/base/agent.proto\x1a)magneto/base/entities/vmware_common.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1amagneto/base/storage.proto\x1a\x1byoda/base/volume_info.proto\"\x8a\x19\n\x18SetupRestoreDiskTaskInfo\x12Q\n\x0bsetup_state\x18\x01 \x01(\x0e\x32<.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.SetupState\x12\x31\n\x0bsetup_error\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12W\n\x0eteardown_state\x18\x03 \x01(\x0e\x32?.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.TeardownState\x12\x34\n\x0eteardown_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12!\n\x19relative_restore_path_vec\x18\x05 \x03(\t\x12\x1d\n\x15\x65ncoded_disk_path_vec\x18\n \x03(\t\x12W\n\x0e\x64\x61tastore_info\x18\x06 \x01(\x0b\x32?.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.DatastoreInfo\x12\x61\n\x11\x61ttached_disk_map\x18\t \x03(\x0b\x32\x46.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.AttachedDiskMapEntry\x12J\n\x18\x65xisting_volume_info_vec\x18\x07 \x03(\x0b\x32(.cohesity.magneto.agents.VolumeInfoProto\x12J\n\x18\x61ttached_volume_info_vec\x18\x08 \x03(\x0b\x32(.cohesity.magneto.agents.VolumeInfoProto\x12\x42\n\x14volume_file_info_vec\x18\x0c \x03(\x0b\x32$.cohesity.yoda.volumeutil.VolumeInfo\x12G\n\x15mount_volume_info_vec\x18\r \x03(\x0b\x32(.cohesity.magneto.agents.MountVolumeInfo\x12\x1d\n\x15snapshot_files_cloned\x18\x0b \x01(\x08\x12q\n\x1a\x64isk_to_controller_key_map\x18\x0e \x03(\x0b\x32M.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.DiskToControllerKeyMapEntry\x12l\n\x18new_to_old_disk_uuid_map\x18\x0f \x03(\x0b\x32J.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.NewToOldDiskUuidMapEntry\x12\x80\x01\n\"disk_uuid_to_provisioning_info_map\x18\x10 \x03(\x0b\x32T.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.DiskUuidToProvisioningInfoMapEntry\x12\x1a\n\x12\x64isk_unique_id_vec\x18\x11 \x03(\t\x12u\n cloned_storage_snapshot_info_vec\x18\x12 \x03(\x0b\x32K.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.ClonedStorageSnapshotInfo\x12\x1c\n\x11\x63urr_snapshot_idx\x18\x13 \x01(\x05:\x01\x30\x12v\n\x1drestore_path_to_disk_uuid_map\x18\x14 \x03(\x0b\x32O.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.RestorePathToDiskUuidMapEntry\x1a\xbd\x02\n\rDatastoreInfo\x12-\n\x05moref\x18\x01 \x01(\x0b\x32\x1e.cohesity.magneto.vmware.MORef\x12\x32\n\nhost_moref\x18\x02 \x01(\x0b\x32\x1e.cohesity.magneto.vmware.MORef\x12>\n\x16\x64\x61tastore_system_moref\x18\x03 \x01(\x0b\x32\x1e.cohesity.magneto.vmware.MORef\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0bremote_host\x18\x05 \x01(\t\x12\x13\n\x0bremote_path\x18\x06 \x01(\t\x12\x38\n\x10\x64\x61tacenter_moref\x18\x07 \x01(\x0b\x32\x1e.cohesity.magneto.vmware.MORef\x12\x17\n\x0f\x64\x61tacenter_name\x18\x08 \x01(\t\x1a]\n\x10\x41ttachedDiskInfo\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x13\n\x0bunit_number\x18\x02 \x01(\x05\x12\x16\n\x0e\x63ontroller_key\x18\x03 \x01(\x05\x12\x0f\n\x07\x64isk_id\x18\x04 \x01(\t\x1az\n\x14\x41ttachedDiskMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.AttachedDiskInfo:\x02\x38\x01\x1a=\n\x1b\x44iskToControllerKeyMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a:\n\x18NewToOldDiskUuidMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aw\n\x14\x44iskProvisioningInfo\x12\x11\n\tdisk_type\x18\x01 \x01(\x05\x12!\n\x13is_thin_provisioned\x18\x02 \x01(\x08:\x04true\x12)\n\x1bthick_eager_scrub_provision\x18\x03 \x01(\x08:\x04true\x1a\x8c\x01\n\"DiskUuidToProvisioningInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12U\n\x05value\x18\x02 \x01(\x0b\x32\x46.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.DiskProvisioningInfo:\x02\x38\x01\x1a\xad\x02\n\x19\x43lonedStorageSnapshotInfo\x12V\n\x1cstorage_device_snapshot_info\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.StorageDeviceSnapshotInfoProto\x12Z\n\x11mounted_datastore\x18\x02 \x01(\x0b\x32?.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo.DatastoreInfo\x12#\n\x14record_volume_for_gc\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x13snapshot_time_usecs\x18\x04 \x01(\x03\x12\x1a\n\x12src_datastore_name\x18\x05 \x01(\t\x1a?\n\x1dRestorePathToDiskUuidMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\nSetupState\x12\x11\n\rkCloneVMFiles\x10\x00\x12\x13\n\x0fkMountDatastore\x10\x01\x12\x10\n\x0ckAttachVMDKs\x10\x02\x12\x15\n\x11kBringDisksOnline\x10\x03\x12\x12\n\x0ekSetupFinished\x10\x04\x12\x13\n\x0fkSetupCancelled\x10\x05\"`\n\rTeardownState\x12\x10\n\x0ckDetachDisks\x10\x01\x12\x15\n\x11kUnmountDatastore\x10\x02\x12\x0f\n\x0bkDeleteView\x10\x03\x12\x15\n\x11kTeardownFinished\x10\x04\x32\x8f\x01\n#vmware_setup_restore_disk_task_info\x12/.cohesity.magneto.SetupRestoreDiskTaskInfoProto\x18\x64 \x01(\x0b\x32\x31.cohesity.magneto.vmware.SetupRestoreDiskTaskInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.vmware.vmware_setup_restore_disks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKMAPENTRY']._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKMAPENTRY']._serialized_options = b'8\001'
  _globals['_SETUPRESTOREDISKTASKINFO_DISKTOCONTROLLERKEYMAPENTRY']._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_DISKTOCONTROLLERKEYMAPENTRY']._serialized_options = b'8\001'
  _globals['_SETUPRESTOREDISKTASKINFO_NEWTOOLDDISKUUIDMAPENTRY']._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_NEWTOOLDDISKUUIDMAPENTRY']._serialized_options = b'8\001'
  _globals['_SETUPRESTOREDISKTASKINFO_DISKUUIDTOPROVISIONINGINFOMAPENTRY']._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_DISKUUIDTOPROVISIONINGINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_SETUPRESTOREDISKTASKINFO_RESTOREPATHTODISKUUIDMAPENTRY']._loaded_options = None
  _globals['_SETUPRESTOREDISKTASKINFO_RESTOREPATHTODISKUUIDMAPENTRY']._serialized_options = b'8\001'
  _globals['_SETUPRESTOREDISKTASKINFO']._serialized_start=275
  _globals['_SETUPRESTOREDISKTASKINFO']._serialized_end=3485
  _globals['_SETUPRESTOREDISKTASKINFO_DATASTOREINFO']._serialized_start=1812
  _globals['_SETUPRESTOREDISKTASKINFO_DATASTOREINFO']._serialized_end=2129
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKINFO']._serialized_start=2131
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKINFO']._serialized_end=2224
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKMAPENTRY']._serialized_start=2226
  _globals['_SETUPRESTOREDISKTASKINFO_ATTACHEDDISKMAPENTRY']._serialized_end=2348
  _globals['_SETUPRESTOREDISKTASKINFO_DISKTOCONTROLLERKEYMAPENTRY']._serialized_start=2350
  _globals['_SETUPRESTOREDISKTASKINFO_DISKTOCONTROLLERKEYMAPENTRY']._serialized_end=2411
  _globals['_SETUPRESTOREDISKTASKINFO_NEWTOOLDDISKUUIDMAPENTRY']._serialized_start=2413
  _globals['_SETUPRESTOREDISKTASKINFO_NEWTOOLDDISKUUIDMAPENTRY']._serialized_end=2471
  _globals['_SETUPRESTOREDISKTASKINFO_DISKPROVISIONINGINFO']._serialized_start=2473
  _globals['_SETUPRESTOREDISKTASKINFO_DISKPROVISIONINGINFO']._serialized_end=2592
  _globals['_SETUPRESTOREDISKTASKINFO_DISKUUIDTOPROVISIONINGINFOMAPENTRY']._serialized_start=2595
  _globals['_SETUPRESTOREDISKTASKINFO_DISKUUIDTOPROVISIONINGINFOMAPENTRY']._serialized_end=2735
  _globals['_SETUPRESTOREDISKTASKINFO_CLONEDSTORAGESNAPSHOTINFO']._serialized_start=2738
  _globals['_SETUPRESTOREDISKTASKINFO_CLONEDSTORAGESNAPSHOTINFO']._serialized_end=3039
  _globals['_SETUPRESTOREDISKTASKINFO_RESTOREPATHTODISKUUIDMAPENTRY']._serialized_start=3041
  _globals['_SETUPRESTOREDISKTASKINFO_RESTOREPATHTODISKUUIDMAPENTRY']._serialized_end=3104
  _globals['_SETUPRESTOREDISKTASKINFO_SETUPSTATE']._serialized_start=3107
  _globals['_SETUPRESTOREDISKTASKINFO_SETUPSTATE']._serialized_end=3241
  _globals['_SETUPRESTOREDISKTASKINFO_TEARDOWNSTATE']._serialized_start=3243
  _globals['_SETUPRESTOREDISKTASKINFO_TEARDOWNSTATE']._serialized_end=3339
# @@protoc_insertion_point(module_scope)