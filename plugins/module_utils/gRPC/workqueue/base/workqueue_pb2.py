# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workqueue/base/workqueue.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from workqueue.base import error_pb2 as workqueue_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eworkqueue/base/workqueue.proto\x12\x12\x63ohesity.workqueue\x1a\x1aworkqueue/base/error.proto\"\xaf\x01\n\x08TaskType\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.cohesity.workqueue.TaskType.Type\"r\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x18\n\x14kNumberGeneratorTest\x10\x01\x12\x13\n\x0fkO365BackupTask\x10\x02\x12\x15\n\x11kO365RecoveryTask\x10\x03\x12\x16\n\x12kGenericBackupTask\x10\x04\"\xab\x01\n\nTaskStatus\"\x9c\x01\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x11\n\rkInitializing\x10\x01\x12\x18\n\x14kWaitingForResources\x10\x02\x12\x1f\n\x1bkWaitingForWorkerAssignment\x10\x03\x12\x0c\n\x08kRunning\x10\x04\x12\x1b\n\x17kWaitingForCancellation\x10\x05\x12\r\n\tkFinished\x10\x06\"E\n\x14PodNodeAffinityProto\x12\x10\n\x08pod_name\x18\x01 \x01(\t\x12\x1b\n\x13node_affinity_label\x18\x02 \x01(\t\"u\n\x11NodeAffinityProto\x12\x1b\n\x13node_affinity_label\x18\x01 \x01(\t\x12\x43\n\x11pod_node_affinity\x18\x02 \x03(\x0b\x32(.cohesity.workqueue.PodNodeAffinityProto\"\xd1\x01\n\x15TaskGroupSummaryProto\x12X\n\x15task_status_count_vec\x18\x01 \x03(\x0b\x32\x39.cohesity.workqueue.TaskGroupSummaryProto.TaskStatusCount\x1a^\n\x0fTaskStatusCount\x12\x38\n\x0btask_status\x18\x01 \x01(\x0e\x32#.cohesity.workqueue.TaskStatus.Type\x12\x11\n\tnum_tasks\x18\x02 \x01(\x05\"<\n\x16WorkerIncarnationProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0eincarnation_id\x18\x02 \x01(\x03\"\x91\x02\n\x0eTaskStateProto\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x16\n\x0eparent_task_id\x18\x02 \x01(\t\x12*\n\x04type\x18\x03 \x01(\x0b\x32\x1c.cohesity.workqueue.TaskType\x12\x33\n\x06status\x18\x04 \x01(\x0e\x32#.cohesity.workqueue.TaskStatus.Type\x12\x46\n\x12\x61ssigned_worker_id\x18\x05 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\x12-\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"\x9e\x01\n\x10WorkerStateProto\x12=\n\tworker_id\x18\x01 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\x12\x33\n+idle_worker_expiry_duration_at_server_msecs\x18\x02 \x01(\x03\x12\x16\n\x08\x63\x61pacity\x18\x03 \x01(\r:\x04\x39\x39\x39\x39\"N\n\x1aWorkqueueServerConfigProto\x12\x30\n\x12gandalf_master_key\x18\x01 \x01(\t:\x14workqueue_server_key')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workqueue.base.workqueue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKTYPE']._serialized_start=83
  _globals['_TASKTYPE']._serialized_end=258
  _globals['_TASKTYPE_TYPE']._serialized_start=144
  _globals['_TASKTYPE_TYPE']._serialized_end=258
  _globals['_TASKSTATUS']._serialized_start=261
  _globals['_TASKSTATUS']._serialized_end=432
  _globals['_TASKSTATUS_TYPE']._serialized_start=276
  _globals['_TASKSTATUS_TYPE']._serialized_end=432
  _globals['_PODNODEAFFINITYPROTO']._serialized_start=434
  _globals['_PODNODEAFFINITYPROTO']._serialized_end=503
  _globals['_NODEAFFINITYPROTO']._serialized_start=505
  _globals['_NODEAFFINITYPROTO']._serialized_end=622
  _globals['_TASKGROUPSUMMARYPROTO']._serialized_start=625
  _globals['_TASKGROUPSUMMARYPROTO']._serialized_end=834
  _globals['_TASKGROUPSUMMARYPROTO_TASKSTATUSCOUNT']._serialized_start=740
  _globals['_TASKGROUPSUMMARYPROTO_TASKSTATUSCOUNT']._serialized_end=834
  _globals['_WORKERINCARNATIONPROTO']._serialized_start=836
  _globals['_WORKERINCARNATIONPROTO']._serialized_end=896
  _globals['_TASKSTATEPROTO']._serialized_start=899
  _globals['_TASKSTATEPROTO']._serialized_end=1172
  _globals['_WORKERSTATEPROTO']._serialized_start=1175
  _globals['_WORKERSTATEPROTO']._serialized_end=1333
  _globals['_WORKQUEUESERVERCONFIGPROTO']._serialized_start=1335
  _globals['_WORKQUEUESERVERCONFIGPROTO']._serialized_end=1413
# @@protoc_insertion_point(module_scope)