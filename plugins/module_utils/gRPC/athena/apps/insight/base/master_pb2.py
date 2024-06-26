# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/apps/insight/base/master.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from athena.apps.insight.base import common_pb2 as athena_dot_apps_dot_insight_dot_base_dot_common__pb2
from athena.apps.insight.base import directory_walker_pb2 as athena_dot_apps_dot_insight_dot_base_dot_directory__walker__pb2
from athena.apps.insight.base import error_pb2 as athena_dot_apps_dot_insight_dot_base_dot_error__pb2
from athena.apps.insight.base import task_pb2 as athena_dot_apps_dot_insight_dot_base_dot_task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%athena/apps/insight/base/master.proto\x12\x04\x62\x61se\x1a%athena/apps/insight/base/common.proto\x1a/athena/apps/insight/base/directory_walker.proto\x1a$athena/apps/insight/base/error.proto\x1a#athena/apps/insight/base/task.proto\"\xba\x01\n\x10MinionStateProto\x12+\n\x05\x65ndpt\x18\x01 \x01(\x0b\x32\x1c.base.MinionTcpEndpointProto\x12#\n\x04info\x18\x02 \x01(\x0b\x32\x15.base.MinionInfoProto\x12\x31\n\x11sub_task_spec_vec\x18\x03 \x03(\x0b\x32\x16.base.SubTaskSpecProto\x12!\n\x19last_heartbeat_time_nsecs\x18\x04 \x01(\x03\"\xc6\x02\n\x1cSubTaskEnumerationStateProto\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\"\n\x1alisting_file_relative_path\x18\x02 \x01(\t\x12%\n\x1dlisting_file_last_sync_offset\x18\x03 \x01(\x03\x12\x18\n\x10next_sub_task_id\x18\x04 \x01(\x03\x12\x18\n\x10start_time_nsecs\x18\x05 \x01(\x03\x12\x37\n\x05state\x18\x06 \x01(\x0e\x32(.base.SubTaskEnumerationStateProto.State\x12\x16\n\x0e\x65nd_time_nsecs\x18\x07 \x01(\x03\x12\x1f\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x10.base.ErrorProto\"$\n\x05State\x12\x0c\n\x08kRunning\x10\x00\x12\r\n\tkFinished\x10\x01\"\xbc\x02\n\x1aSubTaskExecutionStateProto\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12P\n\x19running_subtask_state_vec\x18\x03 \x03(\x0b\x32-.base.SubTaskExecutionStateProto.SubTaskState\x12\x36\n\x16ready_subtask_spec_vec\x18\x04 \x03(\x0b\x32\x16.base.SubTaskSpecProto\x12%\n\x1dlisting_file_next_read_offset\x18\x05 \x01(\x03\x1a\\\n\x0cSubTaskState\x12$\n\x04spec\x18\x01 \x01(\x0b\x32\x16.base.SubTaskSpecProto\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.base.SubTaskStateProto\"\xc3\x02\n\x14\x41\x63tiveTaskStateProto\x12\x1d\n\x04task\x18\x01 \x01(\x0b\x32\x0f.base.TaskProto\x12?\n\x16\x64irectory_walker_state\x18\x02 \x01(\x0b\x32\x1f.base.DirectoryWalkerStateProto\x12?\n\x16\x64irectory_differ_state\x18\x03 \x01(\x0b\x32\x1f.base.DirectoryDifferStateProto\x12\x46\n\x1asub_task_enumeration_state\x18\x04 \x01(\x0b\x32\".base.SubTaskEnumerationStateProto\x12\x42\n\x18sub_task_execution_state\x18\x05 \x01(\x0b\x32 .base.SubTaskExecutionStateProto\"\xb1\x02\n\x10ObjectStateProto\x12!\n\x06object\x18\x01 \x01(\x0b\x32\x11.base.ObjectProto\x12/\n\x0b\x61\x63tive_task\x18\x02 \x01(\x0b\x32\x1a.base.ActiveTaskStateProto\x12&\n\rpast_task_vec\x18\x03 \x03(\x0b\x32\x0f.base.TaskProto\x12\x44\n last_successful_task_final_state\x18\x04 \x01(\x0b\x32\x1a.base.ActiveTaskStateProto\x12\x19\n\x11index_incarnation\x18\x05 \x01(\x03\x12*\n\"last_index_healthy_timestamp_nsecs\x18\x06 \x01(\x03\x12\x14\n\x0cnon_existent\x18\x07 \x01(\x08\"\xda\x02\n\x15MasterCheckpointProto\x12\x30\n\x10minion_state_vec\x18\x01 \x03(\x0b\x32\x16.base.MinionStateProto\x12\x30\n\x10object_state_vec\x18\x02 \x03(\x0b\x32\x16.base.ObjectStateProto\x12*\n\x0b\x66ile_filter\x18\x03 \x01(\x0b\x32\x15.base.FileFilterProto\x12\x16\n\x0enext_object_id\x18\x04 \x01(\x03\x12\x14\n\x0cnext_task_id\x18\x05 \x01(\x03\x12K\n\x11total_volumes_map\x18\x06 \x03(\x0b\x32\x30.base.MasterCheckpointProto.TotalVolumesMapEntry\x1a\x36\n\x14TotalVolumesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x1bZ\x19\x63ohesity/insight_app/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.apps.insight.base.master_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031cohesity/insight_app/base'
  _globals['_MASTERCHECKPOINTPROTO_TOTALVOLUMESMAPENTRY']._loaded_options = None
  _globals['_MASTERCHECKPOINTPROTO_TOTALVOLUMESMAPENTRY']._serialized_options = b'8\001'
  _globals['_MINIONSTATEPROTO']._serialized_start=211
  _globals['_MINIONSTATEPROTO']._serialized_end=397
  _globals['_SUBTASKENUMERATIONSTATEPROTO']._serialized_start=400
  _globals['_SUBTASKENUMERATIONSTATEPROTO']._serialized_end=726
  _globals['_SUBTASKENUMERATIONSTATEPROTO_STATE']._serialized_start=690
  _globals['_SUBTASKENUMERATIONSTATEPROTO_STATE']._serialized_end=726
  _globals['_SUBTASKEXECUTIONSTATEPROTO']._serialized_start=729
  _globals['_SUBTASKEXECUTIONSTATEPROTO']._serialized_end=1045
  _globals['_SUBTASKEXECUTIONSTATEPROTO_SUBTASKSTATE']._serialized_start=953
  _globals['_SUBTASKEXECUTIONSTATEPROTO_SUBTASKSTATE']._serialized_end=1045
  _globals['_ACTIVETASKSTATEPROTO']._serialized_start=1048
  _globals['_ACTIVETASKSTATEPROTO']._serialized_end=1371
  _globals['_OBJECTSTATEPROTO']._serialized_start=1374
  _globals['_OBJECTSTATEPROTO']._serialized_end=1679
  _globals['_MASTERCHECKPOINTPROTO']._serialized_start=1682
  _globals['_MASTERCHECKPOINTPROTO']._serialized_end=2028
  _globals['_MASTERCHECKPOINTPROTO_TOTALVOLUMESMAPENTRY']._serialized_start=1974
  _globals['_MASTERCHECKPOINTPROTO_TOTALVOLUMESMAPENTRY']._serialized_end=2028
# @@protoc_insertion_point(module_scope)
