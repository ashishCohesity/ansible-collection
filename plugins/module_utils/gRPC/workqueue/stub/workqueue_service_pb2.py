# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workqueue/stub/workqueue_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from workqueue.stub import workqueue_service_args_pb2 as workqueue_dot_stub_dot_workqueue__service__args__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&workqueue/stub/workqueue_service.proto\x12\x17\x63ohesity.workqueue.stub\x1a+workqueue/stub/workqueue_service_args.proto2\x96\x05\n\x19WorkqueueWorkerRpcService\x12y\n\x12\x46\x65tchIncarnationId\x12..cohesity.workqueue.stub.FetchIncarnationIdArg\x1a\x31.cohesity.workqueue.stub.FetchIncarnationIdResult\"\x00\x12m\n\x0eRegisterWorker\x12*.cohesity.workqueue.stub.RegisterWorkerArg\x1a-.cohesity.workqueue.stub.RegisterWorkerResult\"\x00\x12\x88\x01\n\x17WorkerToServerHeartbeat\x12\x33.cohesity.workqueue.stub.WorkerToServerHeartbeatArg\x1a\x36.cohesity.workqueue.stub.WorkerToServerHeartbeatResult\"\x00\x12\x7f\n\x14WorkerToServerUpdate\x12\x30.cohesity.workqueue.stub.WorkerToServerUpdateArg\x1a\x33.cohesity.workqueue.stub.WorkerToServerUpdateResult\"\x00\x12\x82\x01\n\x15\x46\x65tchUpdateFromServer\x12\x31.cohesity.workqueue.stub.FetchUpdateFromServerArg\x1a\x34.cohesity.workqueue.stub.FetchUpdateFromServerResult\"\x00\x32\x8e\n\n\x19WorkqueueClientRpcService\x12p\n\x0f\x43reateTaskGroup\x12+.cohesity.workqueue.stub.CreateTaskGroupArg\x1a..cohesity.workqueue.stub.CreateTaskGroupResult\"\x00\x12p\n\x0f\x44\x65leteTaskGroup\x12+.cohesity.workqueue.stub.DeleteTaskGroupArg\x1a..cohesity.workqueue.stub.DeleteTaskGroupResult\"\x00\x12X\n\x07\x41\x64\x64Task\x12#.cohesity.workqueue.stub.AddTaskArg\x1a&.cohesity.workqueue.stub.AddTaskResult\"\x00\x12\x64\n\x0bSubmitTasks\x12\'.cohesity.workqueue.stub.SubmitTasksArg\x1a*.cohesity.workqueue.stub.SubmitTasksResult\"\x00\x12|\n\x13GetTaskGroupSummary\x12/.cohesity.workqueue.stub.GetTaskGroupSummaryArg\x1a\x32.cohesity.workqueue.stub.GetTaskGroupSummaryResult\"\x00\x12j\n\rGetTaskResult\x12).cohesity.workqueue.stub.GetTaskResultArg\x1a,.cohesity.workqueue.stub.GetTaskResultResult\"\x00\x12s\n\x10GetAllTaskResult\x12,.cohesity.workqueue.stub.GetAllTaskResultArg\x1a/.cohesity.workqueue.stub.GetAllTaskResultResult\"\x00\x12\x61\n\nCancelTask\x12&.cohesity.workqueue.stub.CancelTaskArg\x1a).cohesity.workqueue.stub.CancelTaskResult\"\x00\x12p\n\x0f\x43\x61ncelTaskGroup\x12+.cohesity.workqueue.stub.CancelTaskGroupArg\x1a..cohesity.workqueue.stub.CancelTaskGroupResult\"\x00\x12\x9a\x01\n\x1dGetTaskCompletionNotification\x12\x39.cohesity.workqueue.stub.GetTaskCompletionNotificationArg\x1a<.cohesity.workqueue.stub.GetTaskCompletionNotificationResult\"\x00\x12|\n\x13\x44\x65stroyFinishedTask\x12/.cohesity.workqueue.stub.DestroyFinishedTaskArg\x1a\x32.cohesity.workqueue.stub.DestroyFinishedTaskResult\"\x00\x42\x03\x80\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workqueue.stub.workqueue_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\000'
  _globals['_WORKQUEUEWORKERRPCSERVICE']._serialized_start=113
  _globals['_WORKQUEUEWORKERRPCSERVICE']._serialized_end=775
  _globals['_WORKQUEUECLIENTRPCSERVICE']._serialized_start=778
  _globals['_WORKQUEUECLIENTRPCSERVICE']._serialized_end=2072
# @@protoc_insertion_point(module_scope)