# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gandalf/base/common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19gandalf/base/common.proto\x12\x10\x63ohesity.gandalf\"\x8c\x03\n\x15\x43onstituentStatsProto\x12\x16\n\x0e\x63onstituent_id\x18\x01 \x01(\x03\x12\x1d\n\x15last_known_session_id\x18\x02 \x01(\x03\x12\x1a\n\x12last_up_time_usecs\x18\x03 \x01(\x03\x12\x1c\n\x14last_down_time_usecs\x18\x04 \x01(\x03\x12 \n\x18total_up_time_secs_5_min\x18\x05 \x01(\x01\x12\x1c\n\x14total_up_count_5_min\x18\x06 \x01(\x01\x12!\n\x19total_up_time_secs_1_hour\x18\x07 \x01(\x01\x12\x1d\n\x15total_up_count_1_hour\x18\x08 \x01(\x01\x12 \n\x18total_up_time_secs_1_day\x18\t \x01(\x01\x12\x1c\n\x14total_up_count_1_day\x18\n \x01(\x01\x12!\n\x19total_up_time_secs_1_week\x18\x0b \x01(\x01\x12\x1d\n\x15total_up_count_1_week\x18\x0c \x01(\x01\"k\n\x15TransformKeyOperation\"R\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x1c\n\x18kSetGreaterThanOrEqualTo\x10\x01\x12\x1e\n\x19kThrowNotImplementedError\x10\xe7\x07\"i\n\x0cLockPriority\"Y\n\x0cPriorityType\x12\x0f\n\x0bkNoPriority\x10\x00\x12\x10\n\x0ckLowPriority\x10\x01\x12\x13\n\x0fkMediumPriority\x10\x02\x12\x11\n\rkHighPriority\x10\x03\x42.\n\x14\x63om.cohesity.gandalfZ\x16gandalf/base/common.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gandalf.base.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.gandalfZ\026gandalf/base/common.pb'
  _globals['_CONSTITUENTSTATSPROTO']._serialized_start=48
  _globals['_CONSTITUENTSTATSPROTO']._serialized_end=444
  _globals['_TRANSFORMKEYOPERATION']._serialized_start=446
  _globals['_TRANSFORMKEYOPERATION']._serialized_end=553
  _globals['_TRANSFORMKEYOPERATION_TYPE']._serialized_start=471
  _globals['_TRANSFORMKEYOPERATION_TYPE']._serialized_end=553
  _globals['_LOCKPRIORITY']._serialized_start=555
  _globals['_LOCKPRIORITY']._serialized_end=660
  _globals['_LOCKPRIORITY_PRIORITYTYPE']._serialized_start=571
  _globals['_LOCKPRIORITY_PRIORITYTYPE']._serialized_end=660
# @@protoc_insertion_point(module_scope)
