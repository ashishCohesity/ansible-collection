# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/breakfix_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n nexus/base/breakfix_config.proto\x12\x13\x63ohesity.nexus.base\"\x15\n\x04UUID\x12\r\n\x05value\x18\x01 \x01(\t\"X\n\x0c\x42reakfixNode\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x0f\n\x07rack_id\x18\x02 \x01(\t\x12\x12\n\nchassis_id\x18\x03 \x01(\t\x12\x0f\n\x07node_id\x18\x04 \x01(\x03\"\xda\x02\n\x0c\x42reakfixTask\x12*\n\x07task_id\x18\x01 \x01(\x0b\x32\x19.cohesity.nexus.base.UUID\x12=\n\ttask_type\x18\x02 \x01(\x0e\x32*.cohesity.nexus.base.BreakfixTask.TaskType\x12\x41\n\x0btask_status\x18\x03 \x01(\x0e\x32,.cohesity.nexus.base.BreakfixTask.TaskStatus\"C\n\x08TaskType\x12\t\n\x05kNone\x10\x00\x12\x10\n\x0ckReplacement\x10\x01\x12\r\n\tkRollback\x10\x02\x12\x0b\n\x07kLocate\x10\x03\"W\n\nTaskStatus\x12\x0e\n\nkUndefined\x10\x00\x12\x0c\n\x08kRunning\x10\x01\x12\x0e\n\nkSuspended\x10\x02\x12\x0e\n\nkCompleted\x10\x03\x12\x0b\n\x07kFailed\x10\x04\"\x84\x01\n\x0b\x42reakfixFru\x12:\n\x08\x66ru_type\x18\x01 \x01(\x0e\x32(.cohesity.nexus.base.BreakfixFru.FruType\x12\x0e\n\x06\x66ru_id\x18\x02 \x01(\t\")\n\x07\x46ruType\x12\t\n\x05kNone\x10\x00\x12\t\n\x05kDisk\x10\x01\x12\x08\n\x04kFan\x10\x02\"{\n\x19\x46ruReplacementConfigProto\x12\x13\n\x0bgandalf_key\x18\x01 \x01(\t\x12I\n\x16\x66ru_replacement_config\x18\x02 \x03(\x0b\x32).cohesity.nexus.base.FruReplacementConfig\"\xd9\x02\n\x14\x46ruReplacementConfig\x12/\n\x04node\x18\x01 \x01(\x0b\x32!.cohesity.nexus.base.BreakfixNode\x12/\n\x04task\x18\x02 \x01(\x0b\x32!.cohesity.nexus.base.BreakfixTask\x12-\n\x03\x66ru\x18\x03 \x01(\x0b\x32 .cohesity.nexus.base.BreakfixFru\x12\x0f\n\x07step_id\x18\x04 \x01(\x03\x12G\n\nstep_state\x18\x05 \x01(\x0e\x32\x33.cohesity.nexus.base.FruReplacementConfig.StepState\"V\n\tStepState\x12\x0e\n\nkUndefined\x10\x00\x12\x0e\n\nkCompleted\x10\x01\x12\x0c\n\x08kRunning\x10\x02\x12\x0e\n\nkSuspended\x10\x03\x12\x0b\n\x07kFailed\x10\x04\"W\n\x14\x46ruLocateConfigProto\x12?\n\x11\x66ru_locate_config\x18\x02 \x03(\x0b\x32$.cohesity.nexus.base.FruLocateConfig\"\xa2\x01\n\x0f\x46ruLocateConfig\x12/\n\x04node\x18\x01 \x01(\x0b\x32!.cohesity.nexus.base.BreakfixNode\x12/\n\x04task\x18\x02 \x01(\x0b\x32!.cohesity.nexus.base.BreakfixTask\x12-\n\x03\x66ru\x18\x03 \x01(\x0b\x32 .cohesity.nexus.base.BreakfixFru\"\xf2\x01\n\x1b\x46ruReplacementProcedureStep\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0b\n\x03\x65ta\x18\x04 \x01(\x03\x12L\n\tstep_type\x18\x05 \x01(\x0e\x32\x39.cohesity.nexus.base.FruReplacementProcedureStep.StepType\x12\x14\n\x0crun_on_local\x18\x06 \x01(\x08\"2\n\x08StepType\x12\x0e\n\nkUndefined\x10\x00\x12\t\n\x05kAuto\x10\x01\x12\x0b\n\x07kManual\x10\x02\"\xb3\x01\n\x17\x46ruReplacementProcedure\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12-\n\x03\x66ru\x18\x02 \x01(\x0b\x32 .cohesity.nexus.base.BreakfixFru\x12X\n\x1e\x66ru_replacement_procedure_step\x18\x03 \x03(\x0b\x32\x30.cohesity.nexus.base.FruReplacementProcedureStep\"n\n\x1b\x46ruReplacementProcedureList\x12O\n\x19\x66ru_replacement_procedure\x18\x02 \x03(\x0b\x32,.cohesity.nexus.base.FruReplacementProcedureB\x1fZ\x1dnexus/base/breakfix_config.pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.breakfix_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035nexus/base/breakfix_config.pb'
  _globals['_UUID']._serialized_start=57
  _globals['_UUID']._serialized_end=78
  _globals['_BREAKFIXNODE']._serialized_start=80
  _globals['_BREAKFIXNODE']._serialized_end=168
  _globals['_BREAKFIXTASK']._serialized_start=171
  _globals['_BREAKFIXTASK']._serialized_end=517
  _globals['_BREAKFIXTASK_TASKTYPE']._serialized_start=361
  _globals['_BREAKFIXTASK_TASKTYPE']._serialized_end=428
  _globals['_BREAKFIXTASK_TASKSTATUS']._serialized_start=430
  _globals['_BREAKFIXTASK_TASKSTATUS']._serialized_end=517
  _globals['_BREAKFIXFRU']._serialized_start=520
  _globals['_BREAKFIXFRU']._serialized_end=652
  _globals['_BREAKFIXFRU_FRUTYPE']._serialized_start=611
  _globals['_BREAKFIXFRU_FRUTYPE']._serialized_end=652
  _globals['_FRUREPLACEMENTCONFIGPROTO']._serialized_start=654
  _globals['_FRUREPLACEMENTCONFIGPROTO']._serialized_end=777
  _globals['_FRUREPLACEMENTCONFIG']._serialized_start=780
  _globals['_FRUREPLACEMENTCONFIG']._serialized_end=1125
  _globals['_FRUREPLACEMENTCONFIG_STEPSTATE']._serialized_start=1039
  _globals['_FRUREPLACEMENTCONFIG_STEPSTATE']._serialized_end=1125
  _globals['_FRULOCATECONFIGPROTO']._serialized_start=1127
  _globals['_FRULOCATECONFIGPROTO']._serialized_end=1214
  _globals['_FRULOCATECONFIG']._serialized_start=1217
  _globals['_FRULOCATECONFIG']._serialized_end=1379
  _globals['_FRUREPLACEMENTPROCEDURESTEP']._serialized_start=1382
  _globals['_FRUREPLACEMENTPROCEDURESTEP']._serialized_end=1624
  _globals['_FRUREPLACEMENTPROCEDURESTEP_STEPTYPE']._serialized_start=1574
  _globals['_FRUREPLACEMENTPROCEDURESTEP_STEPTYPE']._serialized_end=1624
  _globals['_FRUREPLACEMENTPROCEDURE']._serialized_start=1627
  _globals['_FRUREPLACEMENTPROCEDURE']._serialized_end=1806
  _globals['_FRUREPLACEMENTPROCEDURELIST']._serialized_start=1808
  _globals['_FRUREPLACEMENTPROCEDURELIST']._serialized_end=1918
# @@protoc_insertion_point(module_scope)
