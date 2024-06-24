# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/enums.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmagneto/master/base/enums.proto\x12\x17\x63ohesity.magneto.master\"\xc6\x01\n\x1aStorageSnapshotsTaskStatus\"\xa7\x01\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x16\n\x12kPreProcessingDone\x10\x01\x12\r\n\tkAdmitted\x10\x02\x12\x17\n\x13kFetchedStorageInfo\x10\x03\x12\x12\n\x0ekGroupsCreated\x10\x04\x12\x1e\n\x1akGroupSnapshotTasksCreated\x10\x05\x12\r\n\tkFinished\x10\x06\x12\x0e\n\nkCancelled\x10\x07\"\xc3\x01\n\x17GroupSnapshotTaskStatus\"\xa7\x01\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x16\n\x12kPreProcessingDone\x10\x01\x12\r\n\tkAdmitted\x10\x02\x12\x17\n\x13kGroupSnapshotTaken\x10\x03\x12\x18\n\x14kNotifiedBackupTasks\x10\x04\x12\x18\n\x14kTeardownTaskCreated\x10\x05\x12\r\n\tkFinished\x10\x06\x12\x0e\n\nkCancelled\x10\x07\"\x85\x01\n\x1fTeardownGroupSnapshotTaskStatus\"b\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x16\n\x12kPreProcessingDone\x10\x01\x12\r\n\tkAdmitted\x10\x02\x12\x16\n\x12kSlaveTaskFinished\x10\x03\x12\r\n\tkFinished\x10\x04\"\xa2\x01\n\x12\x43\x61ncellationReason\"\x8b\x01\n\x04Type\x12\x12\n\x0ekUserInitiated\x10\x00\x12\x15\n\x11kDeadlineExceeded\x10\x01\x12\x1a\n\x16kMissedAdmissionWindow\x10\x02\x12\x0e\n\nkLateRetry\x10\x03\x12\x14\n\x10kTimeoutExceeded\x10\x04\x12\x16\n\x12kInMaintenanceMode\x10\x05\">\n\x0bPauseReason\"/\n\x04Type\x12\x12\n\x0ekUserInitiated\x10\x00\x12\x13\n\x0fkBlackoutWindow\x10\x01\"[\n\x0cResumeReason\"K\n\x04Type\x12\x12\n\x0ekUserInitiated\x10\x00\x12\x13\n\x0fkBlackoutWindow\x10\x01\x12\x1a\n\x16kCancellationRequested\x10\x02\"M\n\x0bPauseStatus\">\n\x04Type\x12\x0c\n\x08kRunning\x10\x00\x12\x0c\n\x08kPausing\x10\x01\x12\x0b\n\x07kPaused\x10\x02\x12\r\n\tkResuming\x10\x03\"B\n\x14\x42lackoutWindowAction\"*\n\x04Type\x12\t\n\x05kNone\x10\x00\x12\x0b\n\x07kCancel\x10\x01\x12\n\n\x06kPause\x10\x02\"\xd4\x02\n\x11RestoreTaskStatus\"\xbe\x02\n\x04Type\x12\x14\n\x10kReadyToSchedule\x10\x00\x12\x1b\n\x17kProgressMonitorCreated\x10\x04\x12\x18\n\x14kInternalViewCreated\x10\x08\x12\x19\n\x15kRetrievedFromArchive\x10\x06\x12\x14\n\x10kCDPViewHydrated\x10\x0c\x12\x15\n\x11kZipFileRequested\x10\t\x12\r\n\tkAdmitted\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\x0b\n\x07kOnHold\x10\n\x12\x1d\n\x19kFinishingProgressMonitor\x10\x05\x12\r\n\tkFinished\x10\x03\x12\x0e\n\nkCancelled\x10\x07\x12\x13\n\x0fkCloneDestroyed\x10\x0b\x12\x10\n\x0ckRestoreDone\x10\r\x12\x0f\n\x0bkFinalizing\x10\x0e\"\xd5\x01\n\x11RefreshTaskStatus\"\xbf\x01\n\x04Type\x12\x14\n\x10kReadyToSchedule\x10\x00\x12\r\n\tkAdmitted\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\x1b\n\x17kProgressMonitorCreated\x10\x03\x12\x13\n\x0fkCloneDestroyed\x10\x05\x12\x1d\n\x19kFinishingProgressMonitor\x10\x04\x12\x11\n\rkCloneCreated\x10\x06\x12\r\n\tkFinished\x10\x07\x12\x0e\n\nkCancelled\x10\x08\"\x88\x01\n\x10RestoreJobStatus\"t\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x16\n\x12kPreProcessingDone\x10\x01\x12\r\n\tkAdmitted\x10\x02\x12\x18\n\x14kRestoreTasksCreated\x10\x03\x12\r\n\tkFinished\x10\x04\x12\x0e\n\nkCancelled\x10\x05\"U\n\x17\x44\x65stroyClonedTaskStatus\":\n\x04Type\x12\x14\n\x10kReadyToSchedule\x10\x00\x12\r\n\tkAdmitted\x10\x01\x12\r\n\tkFinished\x10\x02\"Q\n\x13\x44\x65\x61\x63tivateJobStatus\":\n\x04Type\x12\x14\n\x10kReadyToSchedule\x10\x00\x12\r\n\tkAdmitted\x10\x01\x12\r\n\tkFinished\x10\x02\"@\n\x19UpdateBackupRunTaskStatus\"#\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\r\n\tkFinished\x10\x01\"\x88\x01\n\x1dUpdateBackupObjectsTaskStatus\"g\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x13\n\x0fkCopyRunCreated\x10\x01\x12\x12\n\x0ekIceboxUpdated\x10\x02\x12\r\n\tkFinished\x10\x03\x12\x19\n\x15kRemoteReplicaUpdated\x10\x04\"\xa0\x01\n DeleteBackupJobPostProcessStatus\"|\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\r\n\tkFinished\x10\x01\x12\x12\n\x0ekUDACleanupJob\x10\x02\x12\x14\n\x10kUDACleanupViews\x10\x03\x12\x15\n\x11kUDADeleteLogView\x10\x04\x12\x16\n\x12kUDADeleteDataView\x10\x05*\x9f\x01\n\x13\x42\x61\x63kupJobTaskStatus\x12\x17\n\x13kWaitingForSnapshot\x10\x05\x12\x14\n\x10kReadyToSchedule\x10\x00\x12\x1b\n\x17kProgressMonitorCreated\x10\x04\x12\r\n\tkAdmitted\x10\x01\x12\x0e\n\nkFinishing\x10\x06\x12\r\n\tkFinished\x10\x02\x12\x0e\n\nkCancelled\x10\x03*z\n\x18TaskStateInScribeSetting\x12\r\n\tkDisabled\x10\x00\x12\x0c\n\x08kEnabled\x10\x01\x12\x1a\n\x16kUnsupportedInMasterOp\x10\x02\x12%\n!kDisabledDueToScribeRowConstraint\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKUPJOBTASKSTATUS']._serialized_start=2301
  _globals['_BACKUPJOBTASKSTATUS']._serialized_end=2460
  _globals['_TASKSTATEINSCRIBESETTING']._serialized_start=2462
  _globals['_TASKSTATEINSCRIBESETTING']._serialized_end=2584
  _globals['_STORAGESNAPSHOTSTASKSTATUS']._serialized_start=61
  _globals['_STORAGESNAPSHOTSTASKSTATUS']._serialized_end=259
  _globals['_STORAGESNAPSHOTSTASKSTATUS_TYPE']._serialized_start=92
  _globals['_STORAGESNAPSHOTSTASKSTATUS_TYPE']._serialized_end=259
  _globals['_GROUPSNAPSHOTTASKSTATUS']._serialized_start=262
  _globals['_GROUPSNAPSHOTTASKSTATUS']._serialized_end=457
  _globals['_GROUPSNAPSHOTTASKSTATUS_TYPE']._serialized_start=290
  _globals['_GROUPSNAPSHOTTASKSTATUS_TYPE']._serialized_end=457
  _globals['_TEARDOWNGROUPSNAPSHOTTASKSTATUS']._serialized_start=460
  _globals['_TEARDOWNGROUPSNAPSHOTTASKSTATUS']._serialized_end=593
  _globals['_TEARDOWNGROUPSNAPSHOTTASKSTATUS_TYPE']._serialized_start=495
  _globals['_TEARDOWNGROUPSNAPSHOTTASKSTATUS_TYPE']._serialized_end=593
  _globals['_CANCELLATIONREASON']._serialized_start=596
  _globals['_CANCELLATIONREASON']._serialized_end=758
  _globals['_CANCELLATIONREASON_TYPE']._serialized_start=619
  _globals['_CANCELLATIONREASON_TYPE']._serialized_end=758
  _globals['_PAUSEREASON']._serialized_start=760
  _globals['_PAUSEREASON']._serialized_end=822
  _globals['_PAUSEREASON_TYPE']._serialized_start=775
  _globals['_PAUSEREASON_TYPE']._serialized_end=822
  _globals['_RESUMEREASON']._serialized_start=824
  _globals['_RESUMEREASON']._serialized_end=915
  _globals['_RESUMEREASON_TYPE']._serialized_start=840
  _globals['_RESUMEREASON_TYPE']._serialized_end=915
  _globals['_PAUSESTATUS']._serialized_start=917
  _globals['_PAUSESTATUS']._serialized_end=994
  _globals['_PAUSESTATUS_TYPE']._serialized_start=932
  _globals['_PAUSESTATUS_TYPE']._serialized_end=994
  _globals['_BLACKOUTWINDOWACTION']._serialized_start=996
  _globals['_BLACKOUTWINDOWACTION']._serialized_end=1062
  _globals['_BLACKOUTWINDOWACTION_TYPE']._serialized_start=1020
  _globals['_BLACKOUTWINDOWACTION_TYPE']._serialized_end=1062
  _globals['_RESTORETASKSTATUS']._serialized_start=1065
  _globals['_RESTORETASKSTATUS']._serialized_end=1405
  _globals['_RESTORETASKSTATUS_TYPE']._serialized_start=1087
  _globals['_RESTORETASKSTATUS_TYPE']._serialized_end=1405
  _globals['_REFRESHTASKSTATUS']._serialized_start=1408
  _globals['_REFRESHTASKSTATUS']._serialized_end=1621
  _globals['_REFRESHTASKSTATUS_TYPE']._serialized_start=1430
  _globals['_REFRESHTASKSTATUS_TYPE']._serialized_end=1621
  _globals['_RESTOREJOBSTATUS']._serialized_start=1624
  _globals['_RESTOREJOBSTATUS']._serialized_end=1760
  _globals['_RESTOREJOBSTATUS_TYPE']._serialized_start=1644
  _globals['_RESTOREJOBSTATUS_TYPE']._serialized_end=1760
  _globals['_DESTROYCLONEDTASKSTATUS']._serialized_start=1762
  _globals['_DESTROYCLONEDTASKSTATUS']._serialized_end=1847
  _globals['_DESTROYCLONEDTASKSTATUS_TYPE']._serialized_start=1789
  _globals['_DESTROYCLONEDTASKSTATUS_TYPE']._serialized_end=1847
  _globals['_DEACTIVATEJOBSTATUS']._serialized_start=1849
  _globals['_DEACTIVATEJOBSTATUS']._serialized_end=1930
  _globals['_DEACTIVATEJOBSTATUS_TYPE']._serialized_start=1789
  _globals['_DEACTIVATEJOBSTATUS_TYPE']._serialized_end=1847
  _globals['_UPDATEBACKUPRUNTASKSTATUS']._serialized_start=1932
  _globals['_UPDATEBACKUPRUNTASKSTATUS']._serialized_end=1996
  _globals['_UPDATEBACKUPRUNTASKSTATUS_TYPE']._serialized_start=1961
  _globals['_UPDATEBACKUPRUNTASKSTATUS_TYPE']._serialized_end=1996
  _globals['_UPDATEBACKUPOBJECTSTASKSTATUS']._serialized_start=1999
  _globals['_UPDATEBACKUPOBJECTSTASKSTATUS']._serialized_end=2135
  _globals['_UPDATEBACKUPOBJECTSTASKSTATUS_TYPE']._serialized_start=2032
  _globals['_UPDATEBACKUPOBJECTSTASKSTATUS_TYPE']._serialized_end=2135
  _globals['_DELETEBACKUPJOBPOSTPROCESSSTATUS']._serialized_start=2138
  _globals['_DELETEBACKUPJOBPOSTPROCESSSTATUS']._serialized_end=2298
  _globals['_DELETEBACKUPJOBPOSTPROCESSSTATUS_TYPE']._serialized_start=2174
  _globals['_DELETEBACKUPJOBPOSTPROCESSSTATUS_TYPE']._serialized_end=2298
# @@protoc_insertion_point(module_scope)
