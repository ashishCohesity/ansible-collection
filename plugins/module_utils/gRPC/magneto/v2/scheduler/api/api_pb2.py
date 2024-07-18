# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/v2/scheduler/api/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import magneto_external_base_pb2 as magneto_dot_api_dot_magneto__external__base__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"magneto/v2/scheduler/api/api.proto\x12\x1a\x63ohesity.magneto.sched.api\x1a\'magneto/api/magneto_external_base.proto\x1a\x18magneto/base/error.proto\x1a\x1cutil/base/universal_id.proto\"\x13\n\x11\x41\x64\x64OrUpdateJobArg\"\x16\n\x14\x41\x64\x64OrUpdateJobResult\"\x0e\n\x0cRemoveJobArg\"\x11\n\x0fRemoveJobResult\"\x1e\n\x1c\x41\x64\x64OrUpdateProtectionSpecArg\"!\n\x1f\x41\x64\x64OrUpdateProtectionSpecResult\"\x19\n\x17RemoveProtectionSpecArg\"\x1c\n\x1aRemoveProtectionSpecResult\"\x16\n\x14\x41\x64\x64OrUpdatePolicyArg\"\x19\n\x17\x41\x64\x64OrUpdatePolicyResult\"\x11\n\x0fRemovePolicyArg\"\x14\n\x12RemovePolicyResult\"\xa1\x01\n\x0e\x43\x61ncelTasksArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07run_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x30\n\x0ctask_uid_vec\x18\x03 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xd4\x02\n\x11\x43\x61ncelTasksResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12T\n\x16run_cancelation_result\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.sched.api.CancelTasksResult.Result\x12Y\n\x1btask_cancelation_result_vec\x18\x03 \x03(\x0b\x32\x34.cohesity.magneto.sched.api.CancelTasksResult.Result\x1a^\n\x06Result\x12\'\n\x03uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\xa0\x01\n\rPauseTasksArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07run_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x30\n\x0ctask_uid_vec\x18\x03 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xca\x02\n\x10PauseTasksResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12M\n\x10run_pause_result\x18\x02 \x01(\x0b\x32\x33.cohesity.magneto.sched.api.PauseTasksResult.Result\x12R\n\x15task_pause_result_vec\x18\x03 \x03(\x0b\x32\x33.cohesity.magneto.sched.api.PauseTasksResult.Result\x1a\x63\n\x06Result\x12,\n\x08task_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\xa1\x01\n\x0eResumeTasksArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07run_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x30\n\x0ctask_uid_vec\x18\x03 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xd9\x02\n\x11ResumeTasksResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12T\n\x16run_cancelation_result\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.sched.api.ResumeTasksResult.Result\x12Y\n\x1btask_cancelation_result_vec\x18\x03 \x03(\x0b\x32\x34.cohesity.magneto.sched.api.ResumeTasksResult.Result\x1a\x63\n\x06Result\x12,\n\x08task_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProtoB\x1cZ\x1a\x63ohesity/magneto/sched/api')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.v2.scheduler.api.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032cohesity/magneto/sched/api'
  _globals['_ADDORUPDATEJOBARG']._serialized_start=163
  _globals['_ADDORUPDATEJOBARG']._serialized_end=182
  _globals['_ADDORUPDATEJOBRESULT']._serialized_start=184
  _globals['_ADDORUPDATEJOBRESULT']._serialized_end=206
  _globals['_REMOVEJOBARG']._serialized_start=208
  _globals['_REMOVEJOBARG']._serialized_end=222
  _globals['_REMOVEJOBRESULT']._serialized_start=224
  _globals['_REMOVEJOBRESULT']._serialized_end=241
  _globals['_ADDORUPDATEPROTECTIONSPECARG']._serialized_start=243
  _globals['_ADDORUPDATEPROTECTIONSPECARG']._serialized_end=273
  _globals['_ADDORUPDATEPROTECTIONSPECRESULT']._serialized_start=275
  _globals['_ADDORUPDATEPROTECTIONSPECRESULT']._serialized_end=308
  _globals['_REMOVEPROTECTIONSPECARG']._serialized_start=310
  _globals['_REMOVEPROTECTIONSPECARG']._serialized_end=335
  _globals['_REMOVEPROTECTIONSPECRESULT']._serialized_start=337
  _globals['_REMOVEPROTECTIONSPECRESULT']._serialized_end=365
  _globals['_ADDORUPDATEPOLICYARG']._serialized_start=367
  _globals['_ADDORUPDATEPOLICYARG']._serialized_end=389
  _globals['_ADDORUPDATEPOLICYRESULT']._serialized_start=391
  _globals['_ADDORUPDATEPOLICYRESULT']._serialized_end=416
  _globals['_REMOVEPOLICYARG']._serialized_start=418
  _globals['_REMOVEPOLICYARG']._serialized_end=435
  _globals['_REMOVEPOLICYRESULT']._serialized_start=437
  _globals['_REMOVEPOLICYRESULT']._serialized_end=457
  _globals['_CANCELTASKSARG']._serialized_start=460
  _globals['_CANCELTASKSARG']._serialized_end=621
  _globals['_CANCELTASKSRESULT']._serialized_start=624
  _globals['_CANCELTASKSRESULT']._serialized_end=964
  _globals['_CANCELTASKSRESULT_RESULT']._serialized_start=870
  _globals['_CANCELTASKSRESULT_RESULT']._serialized_end=964
  _globals['_PAUSETASKSARG']._serialized_start=967
  _globals['_PAUSETASKSARG']._serialized_end=1127
  _globals['_PAUSETASKSRESULT']._serialized_start=1130
  _globals['_PAUSETASKSRESULT']._serialized_end=1460
  _globals['_PAUSETASKSRESULT_RESULT']._serialized_start=1361
  _globals['_PAUSETASKSRESULT_RESULT']._serialized_end=1460
  _globals['_RESUMETASKSARG']._serialized_start=1463
  _globals['_RESUMETASKSARG']._serialized_end=1624
  _globals['_RESUMETASKSRESULT']._serialized_start=1627
  _globals['_RESUMETASKSRESULT']._serialized_end=1972
  _globals['_RESUMETASKSRESULT_RESULT']._serialized_start=1361
  _globals['_RESUMETASKSRESULT_RESULT']._serialized_end=1460
# @@protoc_insertion_point(module_scope)