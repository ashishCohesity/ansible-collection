# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workqueue/stub/workqueue_service_args.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resource_manager import api_pb2 as resource__manager_dot_api__pb2
from workqueue.base import error_pb2 as workqueue_dot_base_dot_error__pb2
from workqueue.base import workqueue_pb2 as workqueue_dot_base_dot_workqueue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+workqueue/stub/workqueue_service_args.proto\x12\x17\x63ohesity.workqueue.stub\x1a\x1aresource_manager/api.proto\x1a\x1aworkqueue/base/error.proto\x1a\x1eworkqueue/base/workqueue.proto\"\xb7\x01\n\x11RegisterWorkerArg\x12/\n\ttask_type\x18\x01 \x01(\x0b\x32\x1c.cohesity.workqueue.TaskType\x12=\n\tworker_id\x18\x02 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\x12\x32\n*worker_heartbeat_fail_crash_duration_msecs\x18\x03 \x01(\x03\"E\n\x14RegisterWorkerResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"\x17\n\x15\x46\x65tchIncarnationIdArg\")\n\x18\x46\x65tchIncarnationIdResult\x12\r\n\x05value\x18\x01 \x01(\x03\"[\n\x1aWorkerToServerHeartbeatArg\x12=\n\tworker_id\x18\x01 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\"\x1f\n\x1dWorkerToServerHeartbeatResult\"\xa1\x01\n\x17WorkerToServerUpdateArg\x12=\n\tworker_id\x18\x01 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\x12\x0e\n\x06msg_id\x18\x03 \x01(\x03\x12\x37\n\x0btask_status\x18\x04 \x03(\x0b\x32\".cohesity.workqueue.TaskStateProto\"\x1c\n\x1aWorkerToServerUpdateResult\"V\n\x18\x46\x65tchUpdateFromServerArg\x12:\n\x06worker\x18\x01 \x01(\x0b\x32*.cohesity.workqueue.WorkerIncarnationProto\"W\n\x1b\x46\x65tchUpdateFromServerResult\x12\x38\n\x0c\x61\x63tive_tasks\x18\x01 \x03(\x0b\x32\".cohesity.workqueue.TaskStateProto\"=\n\x12\x43reateTaskGroupArg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x19\n\x11max_pending_tasks\x18\x02 \x01(\x03\"F\n\x15\x43reateTaskGroupResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"\"\n\x12\x44\x65leteTaskGroupArg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"F\n\x15\x44\x65leteTaskGroupResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"\xa2\x02\n\nAddTaskArg\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\x12\x16\n\x0eparent_task_id\x18\x02 \x01(\t\x12\x17\n\x0ftask_group_uuid\x18\x08 \x01(\t\x12/\n\ttask_type\x18\x03 \x01(\x0b\x32\x1c.cohesity.workqueue.TaskType\x12G\n\x18resource_acquisition_arg\x18\x04 \x01(\x0b\x32%.cohesity.resource_manager.AcquireArg\x12<\n\rnode_affinity\x18\x05 \x01(\x0b\x32%.cohesity.workqueue.NodeAffinityProto\x12\x18\n\x10task_payload_arg\x18\x06 \x01(\x0c\"D\n\rAddTaskResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProtoJ\x04\x08\x02\x10\x03\"H\n\x0eSubmitTasksArg\x12\x36\n\ttask_args\x18\x01 \x03(\x0b\x32#.cohesity.workqueue.stub.AddTaskArg\"B\n\x11SubmitTasksResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"1\n\x16GetTaskGroupSummaryArg\x12\x17\n\x0ftask_group_uuid\x18\x01 \x01(\t\"\x86\x01\n\x19GetTaskGroupSummaryResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\x12:\n\x07summary\x18\x02 \x01(\x0b\x32).cohesity.workqueue.TaskGroupSummaryProto\"%\n\x10GetTaskResultArg\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\"\xa9\x01\n\x13GetTaskResultResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\x12\x11\n\ttask_uuid\x18\x02 \x01(\t\x12\x38\n\x0btask_status\x18\x03 \x01(\x0e\x32#.cohesity.workqueue.TaskStatus.Type\x12\x16\n\x0eresult_payload\x18\x04 \x01(\x0c\"[\n\x13GetAllTaskResultArg\x12\x17\n\x0ftask_group_uuid\x18\x01 \x01(\t\x12\x18\n\x10start_task_index\x18\x02 \x01(\x05\x12\x11\n\tnum_tasks\x18\x03 \x01(\x05\"\x8b\x01\n\x16GetAllTaskResultResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\x12\x42\n\x0ctask_results\x18\x02 \x03(\x0b\x32,.cohesity.workqueue.stub.GetTaskResultResult\"&\n\x0fWaitForTasksArg\x12\x13\n\x0btask_id_set\x18\x01 \x03(\t\"d\n\x16SingleTaskNotification\x12J\n\x14\x66inished_task_result\x18\x01 \x01(\x0b\x32,.cohesity.workqueue.stub.GetTaskResultResult\"+\n\x16\x44\x65stroyFinishedTaskArg\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\"g\n\x19\x44\x65stroyFinishedTaskResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\x12\x1b\n\x13\x61ll_destroyed_tasks\x18\x02 \x03(\t\"\"\n\rCancelTaskArg\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\"A\n\x10\x43\x61ncelTaskResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"Z\n\x12\x43\x61ncelTaskGroupArg\x12\x17\n\x0ftask_group_uuid\x18\x01 \x01(\t\x12+\n\x1d\x63\x61ncel_descendant_task_groups\x18\x02 \x01(\x08:\x04true\"F\n\x15\x43\x61ncelTaskGroupResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\"x\n\x1eRegisterForTaskGroupUpdatesArg\x12\x17\n\x0ftask_group_uuid\x18\x01 \x01(\t\x12\x1c\n\x14max_num_failed_tasks\x18\x02 \x01(\x05\x12\x1f\n\x17progress_cb_interval_ms\x18\x03 \x01(\x05\"d\n GetTaskCompletionNotificationArg\x12@\n\x0ewait_for_tasks\x18\x01 \x01(\x0b\x32(.cohesity.workqueue.stub.WaitForTasksArg\"\xa1\x01\n#GetTaskCompletionNotificationResult\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1e.cohesity.workqueue.ErrorProto\x12K\n\x12task_notifications\x18\x02 \x03(\x0b\x32/.cohesity.workqueue.stub.SingleTaskNotificationB\x19Z\x17\x63ohesity/workqueue/stub')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workqueue.stub.workqueue_service_args_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\027cohesity/workqueue/stub'
  _globals['_REGISTERWORKERARG']._serialized_start=161
  _globals['_REGISTERWORKERARG']._serialized_end=344
  _globals['_REGISTERWORKERRESULT']._serialized_start=346
  _globals['_REGISTERWORKERRESULT']._serialized_end=415
  _globals['_FETCHINCARNATIONIDARG']._serialized_start=417
  _globals['_FETCHINCARNATIONIDARG']._serialized_end=440
  _globals['_FETCHINCARNATIONIDRESULT']._serialized_start=442
  _globals['_FETCHINCARNATIONIDRESULT']._serialized_end=483
  _globals['_WORKERTOSERVERHEARTBEATARG']._serialized_start=485
  _globals['_WORKERTOSERVERHEARTBEATARG']._serialized_end=576
  _globals['_WORKERTOSERVERHEARTBEATRESULT']._serialized_start=578
  _globals['_WORKERTOSERVERHEARTBEATRESULT']._serialized_end=609
  _globals['_WORKERTOSERVERUPDATEARG']._serialized_start=612
  _globals['_WORKERTOSERVERUPDATEARG']._serialized_end=773
  _globals['_WORKERTOSERVERUPDATERESULT']._serialized_start=775
  _globals['_WORKERTOSERVERUPDATERESULT']._serialized_end=803
  _globals['_FETCHUPDATEFROMSERVERARG']._serialized_start=805
  _globals['_FETCHUPDATEFROMSERVERARG']._serialized_end=891
  _globals['_FETCHUPDATEFROMSERVERRESULT']._serialized_start=893
  _globals['_FETCHUPDATEFROMSERVERRESULT']._serialized_end=980
  _globals['_CREATETASKGROUPARG']._serialized_start=982
  _globals['_CREATETASKGROUPARG']._serialized_end=1043
  _globals['_CREATETASKGROUPRESULT']._serialized_start=1045
  _globals['_CREATETASKGROUPRESULT']._serialized_end=1115
  _globals['_DELETETASKGROUPARG']._serialized_start=1117
  _globals['_DELETETASKGROUPARG']._serialized_end=1151
  _globals['_DELETETASKGROUPRESULT']._serialized_start=1153
  _globals['_DELETETASKGROUPRESULT']._serialized_end=1223
  _globals['_ADDTASKARG']._serialized_start=1226
  _globals['_ADDTASKARG']._serialized_end=1516
  _globals['_ADDTASKRESULT']._serialized_start=1518
  _globals['_ADDTASKRESULT']._serialized_end=1586
  _globals['_SUBMITTASKSARG']._serialized_start=1588
  _globals['_SUBMITTASKSARG']._serialized_end=1660
  _globals['_SUBMITTASKSRESULT']._serialized_start=1662
  _globals['_SUBMITTASKSRESULT']._serialized_end=1728
  _globals['_GETTASKGROUPSUMMARYARG']._serialized_start=1730
  _globals['_GETTASKGROUPSUMMARYARG']._serialized_end=1779
  _globals['_GETTASKGROUPSUMMARYRESULT']._serialized_start=1782
  _globals['_GETTASKGROUPSUMMARYRESULT']._serialized_end=1916
  _globals['_GETTASKRESULTARG']._serialized_start=1918
  _globals['_GETTASKRESULTARG']._serialized_end=1955
  _globals['_GETTASKRESULTRESULT']._serialized_start=1958
  _globals['_GETTASKRESULTRESULT']._serialized_end=2127
  _globals['_GETALLTASKRESULTARG']._serialized_start=2129
  _globals['_GETALLTASKRESULTARG']._serialized_end=2220
  _globals['_GETALLTASKRESULTRESULT']._serialized_start=2223
  _globals['_GETALLTASKRESULTRESULT']._serialized_end=2362
  _globals['_WAITFORTASKSARG']._serialized_start=2364
  _globals['_WAITFORTASKSARG']._serialized_end=2402
  _globals['_SINGLETASKNOTIFICATION']._serialized_start=2404
  _globals['_SINGLETASKNOTIFICATION']._serialized_end=2504
  _globals['_DESTROYFINISHEDTASKARG']._serialized_start=2506
  _globals['_DESTROYFINISHEDTASKARG']._serialized_end=2549
  _globals['_DESTROYFINISHEDTASKRESULT']._serialized_start=2551
  _globals['_DESTROYFINISHEDTASKRESULT']._serialized_end=2654
  _globals['_CANCELTASKARG']._serialized_start=2656
  _globals['_CANCELTASKARG']._serialized_end=2690
  _globals['_CANCELTASKRESULT']._serialized_start=2692
  _globals['_CANCELTASKRESULT']._serialized_end=2757
  _globals['_CANCELTASKGROUPARG']._serialized_start=2759
  _globals['_CANCELTASKGROUPARG']._serialized_end=2849
  _globals['_CANCELTASKGROUPRESULT']._serialized_start=2851
  _globals['_CANCELTASKGROUPRESULT']._serialized_end=2921
  _globals['_REGISTERFORTASKGROUPUPDATESARG']._serialized_start=2923
  _globals['_REGISTERFORTASKGROUPUPDATESARG']._serialized_end=3043
  _globals['_GETTASKCOMPLETIONNOTIFICATIONARG']._serialized_start=3045
  _globals['_GETTASKCOMPLETIONNOTIFICATIONARG']._serialized_end=3145
  _globals['_GETTASKCOMPLETIONNOTIFICATIONRESULT']._serialized_start=3148
  _globals['_GETTASKCOMPLETIONNOTIFICATIONRESULT']._serialized_end=3309
# @@protoc_insertion_point(module_scope)
