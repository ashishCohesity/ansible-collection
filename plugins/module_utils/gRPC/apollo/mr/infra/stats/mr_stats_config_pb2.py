# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/infra/stats/mr_stats_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+apollo/mr/infra/stats/mr_stats_config.proto\x12\x18\x63ohesity.apollo.mr.stats\"\x83\x04\n\x11UsageMetricsProto\"\xed\x03\n\x04Type\x12\x16\n\x12kBrickBytesLogical\x10\x00\x12\x16\n\x12kChunkBytesLogical\x10\x01\x12\x16\n\x12kChunkBytesMorphed\x10\x02\x12\x17\n\x13kChunkBytesPhysical\x10\x03\x12\x19\n\x15kStorageConsumedBytes\x10\x04\x12\x12\n\x0ekCapacityBytes\x10\x05\x12%\n!kLocalTierResiliencyOverheadBytes\x10\x06\x12\x1f\n\x1bkLocalTierChunkBytesMorphed\x10\x07\x12\x15\n\x11kLogicalSizeBytes\x10\x08\x12\r\n\tkNumFiles\x10\t\x12\x13\n\x0fkNumDirectories\x10\n\x12\x1d\n\x19kUniqueChunkBytesPhysical\x10\x0b\x12\x1b\n\x17kCloudChunkBytesMorphed\x10\x0c\x12\x1b\n\x17kLocalChunkBytesMorphed\x10\r\x12\x1e\n\x1akCloudStorageConsumedBytes\x10\x0e\x12\x1e\n\x1akLocalStorageConsumedBytes\x10\x0f\x12\x16\n\x12kInodeBytesLogical\x10\x10\x12!\n\x1dkLocalUniqueChunkBytesMorphed\x10\x11\"j\n\x10StatsSchemaProto\x12\x13\n\x0bschema_name\x18\x01 \x01(\t\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\x12\x15\n\rint_entity_id\x18\x03 \x01(\x03\x12\x15\n\rstr_entity_id\x18\x04 \x01(\t\"\xce\x01\n\x10SchemaNamesProto\x12>\n apollo_cluster_stats_schema_name\x18\x01 \x01(\t:\x14\x41polloV2ClusterStats\x12\x43\n\'apollo_storage_domain_stats_schema_name\x18\x02 \x01(\t:\x12\x41polloViewBoxStats\x12\x35\n\x1c\x62ookkeeper_stats_schema_name\x18\x03 \x01(\t:\x0f\x42ookKeeperStatsB*Z(apollo/mr/infra/stats/mr_stats_config.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.infra.stats.mr_stats_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(apollo/mr/infra/stats/mr_stats_config.pb'
  _globals['_USAGEMETRICSPROTO']._serialized_start=74
  _globals['_USAGEMETRICSPROTO']._serialized_end=589
  _globals['_USAGEMETRICSPROTO_TYPE']._serialized_start=96
  _globals['_USAGEMETRICSPROTO_TYPE']._serialized_end=589
  _globals['_STATSSCHEMAPROTO']._serialized_start=591
  _globals['_STATSSCHEMAPROTO']._serialized_end=697
  _globals['_SCHEMANAMESPROTO']._serialized_start=700
  _globals['_SCHEMANAMESPROTO']._serialized_end=906
# @@protoc_insertion_point(module_scope)