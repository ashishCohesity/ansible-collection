# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/master/api_server_WAL.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo.mr.master import master_pb2 as apollo_dot_mr_dot_master_dot_master__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%apollo/mr/master/api_server_WAL.proto\x12\x19\x63ohesity.apollo.mr.master\x1a\x1d\x61pollo/mr/master/master.proto\"\xfb\x02\n\x17\x41PIServerWALRecordProto\x12T\n\x18schedule_job_request_vec\x18\x01 \x03(\x0b\x32\x32.cohesity.apollo.mr.master.ScheduleJobRequestProto\x12\x81\x01\n\"add_or_delete_schedule_job_request\x18\x02 \x01(\x0b\x32U.cohesity.apollo.mr.master.APIServerWALRecordProto.AddOrDeleteScheduleJobRequestProto\x1a\x85\x01\n\"AddOrDeleteScheduleJobRequestProto\x12G\n\x0bjob_request\x18\x01 \x01(\x0b\x32\x32.cohesity.apollo.mr.master.ScheduleJobRequestProto\x12\x16\n\x0e\x64\x65lete_request\x18\x02 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.master.api_server_WAL_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APISERVERWALRECORDPROTO']._serialized_start=100
  _globals['_APISERVERWALRECORDPROTO']._serialized_end=479
  _globals['_APISERVERWALRECORDPROTO_ADDORDELETESCHEDULEJOBREQUESTPROTO']._serialized_start=346
  _globals['_APISERVERWALRECORDPROTO_ADDORDELETESCHEDULEJOBREQUESTPROTO']._serialized_end=479
# @@protoc_insertion_point(module_scope)
