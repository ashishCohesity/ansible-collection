# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groot/etl/wal_entry.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19groot/etl/wal_entry.proto\x12\x12\x63ohesity.groot.etl\"\xf8\x05\n\x0b\x45tlWALEntry\x12J\n\x11\x63luster_etl_state\x18\x01 \x01(\x0b\x32/.cohesity.groot.etl.EtlWALEntry.ClusterEtlState\x12\x46\n\x0fstats_etl_state\x18\x02 \x01(\x0b\x32-.cohesity.groot.etl.EtlWALEntry.StatsEtlState\x12J\n\x11magneto_etl_state\x18\x03 \x01(\x0b\x32/.cohesity.groot.etl.EtlWALEntry.MagnetoEtlState\x1a\x30\n\x0f\x43lusterEtlState\x12\x1d\n\x15last_update_time_secs\x18\x01 \x01(\x03\x1a\xa7\x01\n\rStatsEtlState\x12\x31\n)last_io_performance_stats_fetch_time_secs\x18\x01 \x01(\x03\x12\x31\n)last_resource_usage_stats_fetch_time_secs\x18\x02 \x01(\x03\x12\x30\n(last_storage_usage_stats_fetch_time_secs\x18\x03 \x01(\x03\x1a\xac\x02\n\x0fMagnetoEtlState\x12i\n\x17last_run_start_time_map\x18\x03 \x03(\x0b\x32H.cohesity.groot.etl.EtlWALEntry.MagnetoEtlState.LastRunStartTimeMapEntry\x12.\n&last_restored_objects_update_time_secs\x18\x04 \x01(\x03\x12!\n\x19last_data_fetch_time_secs\x18\x05 \x01(\x03\x12\x1f\n\x17should_trigger_fullsync\x18\x06 \x01(\x08\x1a:\n\x18LastRunStartTimeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'groot.etl.wal_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ETLWALENTRY_MAGNETOETLSTATE_LASTRUNSTARTTIMEMAPENTRY']._loaded_options = None
  _globals['_ETLWALENTRY_MAGNETOETLSTATE_LASTRUNSTARTTIMEMAPENTRY']._serialized_options = b'8\001'
  _globals['_ETLWALENTRY']._serialized_start=50
  _globals['_ETLWALENTRY']._serialized_end=810
  _globals['_ETLWALENTRY_CLUSTERETLSTATE']._serialized_start=289
  _globals['_ETLWALENTRY_CLUSTERETLSTATE']._serialized_end=337
  _globals['_ETLWALENTRY_STATSETLSTATE']._serialized_start=340
  _globals['_ETLWALENTRY_STATSETLSTATE']._serialized_end=507
  _globals['_ETLWALENTRY_MAGNETOETLSTATE']._serialized_start=510
  _globals['_ETLWALENTRY_MAGNETOETLSTATE']._serialized_end=810
  _globals['_ETLWALENTRY_MAGNETOETLSTATE_LASTRUNSTARTTIMEMAPENTRY']._serialized_start=752
  _globals['_ETLWALENTRY_MAGNETOETLSTATE_LASTRUNSTARTTIMEMAPENTRY']._serialized_end=810
# @@protoc_insertion_point(module_scope)
