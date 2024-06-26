# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/uda/uda.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.stub import uda_param_pb2 as magneto_dot_agents_dot_stub_dot_uda__param__pb2
from magneto.base.entities import azure_pb2 as magneto_dot_base_dot_entities_dot_azure__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import uda_pb2 as magneto_dot_base_dot_uda__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n magneto/connectors/uda/uda.proto\x12\x14\x63ohesity.magneto.uda\x1a#magneto/agents/stub/uda_param.proto\x1a!magneto/base/entities/azure.proto\x1a\x1amagneto/base/magneto.proto\x1a\x16magneto/base/uda.proto\x1a\x18magneto/base/error.proto\x1a\x19magneto/base/entity.proto\"\xba\x0f\n\x0cSnapshotInfo\x12\x18\n\x10\x62\x61\x63kup_view_name\x18\x01 \x01(\t\x12\x17\n\x0fjob_instance_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x03 \x01(\x05\x12\x18\n\x10progress_percent\x18\x04 \x01(\x05\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12)\n\x05stats\x18\x06 \x01(\x0b\x32\x1a.cohesity.magneto.UdaStats\x12\x0f\n\x07task_id\x18\x07 \x01(\x03\x12\x44\n\x0c\x62\x61\x63kup_state\x18\x08 \x01(\x0e\x32..cohesity.magneto.uda.SnapshotInfo.BackupState\x12\x0f\n\x04page\x18\t \x01(\x05:\x01\x30\x12\x43\n\x0cprocess_info\x18\n \x01(\x0b\x32-.cohesity.magneto.agents.uda.stub.ProcessInfo\x12\x1a\n\x0fpulse_log_index\x18\x0b \x01(\x05:\x01\x30\x12\x16\n\x0emountpoint_vec\x18\x0c \x03(\t\x12\x13\n\x07view_id\x18\r \x01(\x03:\x02-1\x12)\n\x1e\x63\x61ncel_job_retry_current_count\x18\x0e \x01(\x05:\x01\x30\x12\'\n\x1blog_backup_start_epoch_secs\x18\x0f \x01(\x03:\x02-1\x12%\n\x19log_backup_end_epoch_secs\x18\x10 \x01(\x03:\x02-1\x12\x14\n\x0c\x63ontrol_node\x18\x11 \x01(\t\x12\x15\n\rlog_view_name\x18\x12 \x01(\t\x12\x13\n\x0blog_view_id\x18\x13 \x01(\x03\x12$\n\x15\x61uto_log_view_mounted\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x17\x61uto_log_mountpoint_vec\x18\x15 \x03(\t\x12\x12\n\nmount_vips\x18\x16 \x03(\t\x12!\n\x16job_status_retry_count\x18\x17 \x01(\x05:\x01\x30\x12!\n\x19\x63loned_auto_log_view_name\x18\x18 \x01(\t\x12\"\n\x16\x64\x61ta_backup_epoch_secs\x18\x19 \x01(\x03:\x02-1\x12\x1f\n\x13snapshot_time_usecs\x18\x1a \x01(\x03:\x02-1\x12\"\n\x16\x62ifrost_constituent_id\x18\x1b \x01(\x03:\x02-1\x12 \n\x18heimdall_disk_request_id\x18\x1c \x01(\t\x12 \n\x18heimdall_disk_mountpoint\x18\x1d \x01(\t\x12\x36\n\x0f\x61ncestor_entity\x18\x1e \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x14\n\x05\x61\x62ort\x18\x1f \x01(\x08:\x05\x66\x61lse\x12>\n\nazure_info\x18  \x01(\x0b\x32*.cohesity.magneto.azure.AzureSnapshotProps\x12T\n\x15\x63ohesity_cp_copy_mode\x18! \x01(\x0e\x32\x35.cohesity.magneto.uda.SnapshotInfo.CohesityCpCopyMode\"\xe2\x04\n\x0b\x42\x61\x63kupState\x12\x0c\n\x08kStarted\x10\x00\x12\x12\n\x0ekViewFinalized\x10\x01\x12\x15\n\x11kMaybeViewCreated\x10\x02\x12\x15\n\x11kMaybeViewMounted\x10\x03\x12\x11\n\rkSentEntities\x10\x04\x12\x13\n\x0fkStartedAttempt\x10\x05\x12\x14\n\x10kFinishedAttempt\x10\x06\x12\x16\n\x12kJobDetailsFetched\x10\x07\x12\x17\n\x13kMaybeViewUnmounted\x10\x08\x12\x0f\n\x0bkClonedView\x10\t\x12\r\n\tkFinished\x10\n\x12\x0e\n\nkCancelJob\x10\x0b\x12\x19\n\x15kAutoLogViewFinalized\x10\x0c\x12\x1c\n\x18kMaybeAutoLogViewCreated\x10\r\x12\x16\n\x12kClonedAutoLogView\x10\x0e\x12\x14\n\x10kGotAllEndPoints\x10\x0f\x12\x17\n\x13kRemovedStaleMounts\x10\x10\x12\x18\n\x14kDeletedPreviousView\x10\x11\x12\x18\n\x14kCreatedIndexingView\x10\x12\x12\x19\n\x15kMaybeAutoViewMounted\x10\x13\x12\x14\n\x10kMaybeModifyView\x10\x14\x12\x1b\n\x17kMaybeModifyAutoLogView\x10\x15\x12\x12\n\x0ekPermitGranted\x10\x16\x12\x12\n\x0ekPreBackupDone\x10\x17\x12\x1b\n\x17kMaybeExternalDiskAdded\x10\x18\x12\x1d\n\x19kMaybeExternalDiskRemoved\x10\x19\"B\n\x12\x43ohesityCpCopyMode\x12\x10\n\x0ckCloudSnapFS\x10\x01\x12\x14\n\x10kRemoteWanSnapFS\x10\x02\"\x04\x08\x00\x10\x00\x32\x62\n\x11uda_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18~ \x01(\x0b\x32\".cohesity.magneto.uda.SnapshotInfo\"n\n\x0bRestoreInfo2_\n\x10uda_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18z \x01(\x0b\x32!.cohesity.magneto.uda.RestoreInfo\"\x8c\r\n\x11RestoreEntityInfo\x12I\n\x12recover_task_state\x18\x01 \x01(\x0e\x32-.cohesity.magneto.uda.RestoreEntityInfo.State\x12\x18\n\x10progress_percent\x18\x02 \x01(\x05\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12)\n\x05stats\x18\x04 \x01(\x0b\x32\x1a.cohesity.magneto.UdaStats\x12\x43\n\x0cprocess_info\x18\x05 \x01(\x0b\x32-.cohesity.magneto.agents.uda.stub.ProcessInfo\x12\x1a\n\x0fpulse_log_index\x18\x06 \x01(\x05:\x01\x30\x12.\n\x08warnings\x18\x07 \x03(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x0f\n\x07task_id\x18\x08 \x01(\x03\x12\x0f\n\x04page\x18\t \x01(\x05:\x01\x30\x12)\n\x1e\x63\x61ncel_job_retry_current_count\x18\n \x01(\x05:\x01\x30\x12R\n\x0emountpoint_map\x18\x0b \x03(\x0b\x32:.cohesity.magneto.uda.RestoreEntityInfo.MountpointMapEntry\x12Y\n\x12log_mountpoint_map\x18\x0c \x03(\x0b\x32=.cohesity.magneto.uda.RestoreEntityInfo.LogMountpointMapEntry\x12\x14\n\x0c\x63ontrol_node\x18\r \x01(\t\x12\x11\n\tview_vips\x18\x0e \x03(\t\x12\x1a\n\x0e\x63loned_view_id\x18\x0f \x01(\x03:\x02-1\x12\x1e\n\x12\x63loned_log_view_id\x18\x10 \x01(\x03:\x02-1\x12!\n\x16job_status_retry_count\x18\x11 \x01(\x05:\x01\x30\x12\"\n\x16\x62ifrost_constituent_id\x18\x12 \x01(\x03:\x02-1\x12 \n\x18heimdall_disk_request_id\x18\x13 \x01(\t\x12 \n\x18heimdall_disk_mountpoint\x18\x14 \x01(\t\x12\x14\n\x05\x61\x62ort\x18\x16 \x01(\x08:\x05\x66\x61lse\x1a[\n\x12MountpointMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.cohesity.magneto.uda.MountedPathInfo:\x02\x38\x01\x1a^\n\x15LogMountpointMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.cohesity.magneto.uda.MountedPathInfo:\x02\x38\x01\"\xed\x03\n\x05State\x12\x0c\n\x08kStarted\x10\x01\x12\x19\n\x15kClonedFullBackupView\x10\x02\x12\x18\n\x14kClonedLogBackupView\x10\x03\x12\x1a\n\x16kMountedFullBackupView\x10\x04\x12\x19\n\x15kMountedLogBackupView\x10\x05\x12\x12\n\x0ekPermitGranted\x10\x06\x12\x16\n\x12kEntitiesSubmitted\x10\x07\x12\x18\n\x14kRestoreJobSubmitted\x10\x08\x12\"\n\x1ekRestoreJobCompletedOrCanceled\x10\t\x12\x1d\n\x19kRestoreJobDetailsFetched\x10\n\x12\x1c\n\x18kUnmountedFullBackupView\x10\x0b\x12\x1b\n\x17kUnmountedLogBackupView\x10\x0c\x12\x1a\n\x16kFullBackupViewDeleted\x10\r\x12\x19\n\x15kLogBackupViewDeleted\x10\x0e\x12\r\n\tkFinished\x10\x0f\x12\x0e\n\nkCancelJob\x10\x10\x12\x14\n\x10kGotAllEndPoints\x10\x11\x12\x1b\n\x17kMaybeExternalDiskAdded\x10\x12\x12\x1d\n\x19kMaybeExternalDiskRemoved\x10\x13\x32z\n\x17uda_restore_entity_info\x12\x30.cohesity.magneto.RestoreInfoProto.RestoreEntity\x18p \x01(\x0b\x32\'.cohesity.magneto.uda.RestoreEntityInfo\">\n\x0fMountedPathInfo\x12\x18\n\x10mounted_path_vec\x18\x01 \x03(\t\x12\x11\n\tview_vips\x18\x02 \x03(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.uda.uda_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESTOREENTITYINFO_MOUNTPOINTMAPENTRY']._loaded_options = None
  _globals['_RESTOREENTITYINFO_MOUNTPOINTMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREENTITYINFO_LOGMOUNTPOINTMAPENTRY']._loaded_options = None
  _globals['_RESTOREENTITYINFO_LOGMOUNTPOINTMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO']._serialized_start=236
  _globals['_SNAPSHOTINFO']._serialized_end=2214
  _globals['_SNAPSHOTINFO_BACKUPSTATE']._serialized_start=1436
  _globals['_SNAPSHOTINFO_BACKUPSTATE']._serialized_end=2046
  _globals['_SNAPSHOTINFO_COHESITYCPCOPYMODE']._serialized_start=2048
  _globals['_SNAPSHOTINFO_COHESITYCPCOPYMODE']._serialized_end=2114
  _globals['_RESTOREINFO']._serialized_start=2216
  _globals['_RESTOREINFO']._serialized_end=2326
  _globals['_RESTOREENTITYINFO']._serialized_start=2329
  _globals['_RESTOREENTITYINFO']._serialized_end=4005
  _globals['_RESTOREENTITYINFO_MOUNTPOINTMAPENTRY']._serialized_start=3198
  _globals['_RESTOREENTITYINFO_MOUNTPOINTMAPENTRY']._serialized_end=3289
  _globals['_RESTOREENTITYINFO_LOGMOUNTPOINTMAPENTRY']._serialized_start=3291
  _globals['_RESTOREENTITYINFO_LOGMOUNTPOINTMAPENTRY']._serialized_end=3385
  _globals['_RESTOREENTITYINFO_STATE']._serialized_start=3388
  _globals['_RESTOREENTITYINFO_STATE']._serialized_end=3881
  _globals['_MOUNTEDPATHINFO']._serialized_start=4007
  _globals['_MOUNTEDPATHINFO']._serialized_end=4069
# @@protoc_insertion_point(module_scope)
