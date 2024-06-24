# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/lib/cohesityConnector/base/perf_stats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.master.base import enums_pb2 as magneto_dot_master_dot_base_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.qa/lib/cohesityConnector/base/perf_stats.proto\x12\x1e\x63ohesity.qa.cohesity_connector\x1a\x18magneto/base/error.proto\x1a\x1fmagneto/master/base/enums.proto\"F\n\rBasePerfStats\x12\x0b\n\x03\x61vg\x18\x01 \x01(\x03\x12\x0b\n\x03min\x18\x02 \x01(\x03\x12\x0b\n\x03max\x18\x03 \x01(\x03\x12\x0e\n\x06median\x18\x04 \x01(\x03\"\x8a\x05\n\x0f\x42ridgePerfStats\x12J\n\x13write_latency_usecs\x18\x01 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12K\n\x14write_ios_per_second\x18\x02 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12T\n\x1d\x64\x61ta_written_bytes_per_second\x18\x03 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12I\n\x12read_latency_usecs\x18\x04 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12J\n\x13read_ios_per_second\x18\x05 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12Q\n\x1a\x64\x61ta_read_bytes_per_second\x18\x06 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12P\n\x19sequential_ios_per_second\x18\x07 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\x12L\n\x15random_ios_per_second\x18\x08 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\"j\n\x15\x42ridgeEntityPerfStats\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12>\n\x05stats\x18\x02 \x01(\x0b\x32/.cohesity.qa.cohesity_connector.BridgePerfStats\"}\n\x16MagnetoEntityPerfStats\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12P\n\x19\x62ytes_backedup_per_second\x18\x02 \x01(\x0b\x32-.cohesity.qa.cohesity_connector.BasePerfStats\"\xb9\x02\n\x11VMBackupTaskStats\x12\x1d\n\x15task_start_time_usecs\x18\x01 \x01(\x03\x12 \n\x18task_schedule_time_usecs\x18\x02 \x01(\x03\x12\x19\n\x11\x62\x61\x63kup_time_usecs\x18\x03 \x01(\x03\x12\x1e\n\x16\x62ytes_read_from_source\x18\x04 \x01(\x03\x12\x1d\n\x15logical_bytes_written\x18\x05 \x01(\x03\x12\x1e\n\x16physical_bytes_written\x18\x06 \x01(\x03\x12<\n\x06status\x18\x07 \x01(\x0e\x32,.cohesity.magneto.master.BackupJobTaskStatus\x12+\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"l\n\rVMBackupStats\x12\r\n\x05moref\x18\x01 \x01(\t\x12L\n\x11\x62\x61\x63kup_task_stats\x18\x02 \x03(\x0b\x32\x31.cohesity.qa.cohesity_connector.VMBackupTaskStatsB-Z+qa/lib/cohesityConnector/base/perf_stats.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.lib.cohesityConnector.base.perf_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+qa/lib/cohesityConnector/base/perf_stats.pb'
  _globals['_BASEPERFSTATS']._serialized_start=141
  _globals['_BASEPERFSTATS']._serialized_end=211
  _globals['_BRIDGEPERFSTATS']._serialized_start=214
  _globals['_BRIDGEPERFSTATS']._serialized_end=864
  _globals['_BRIDGEENTITYPERFSTATS']._serialized_start=866
  _globals['_BRIDGEENTITYPERFSTATS']._serialized_end=972
  _globals['_MAGNETOENTITYPERFSTATS']._serialized_start=974
  _globals['_MAGNETOENTITYPERFSTATS']._serialized_end=1099
  _globals['_VMBACKUPTASKSTATS']._serialized_start=1102
  _globals['_VMBACKUPTASKSTATS']._serialized_end=1415
  _globals['_VMBACKUPSTATS']._serialized_start=1417
  _globals['_VMBACKUPSTATS']._serialized_end=1525
# @@protoc_insertion_point(module_scope)
