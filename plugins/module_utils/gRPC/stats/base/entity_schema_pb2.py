# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stats/base/entity_schema.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from stats.base import stats_types_pb2 as stats_dot_base_dot_stats__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1estats/base/entity_schema.proto\x12\x0e\x63ohesity.stats\x1a google/protobuf/descriptor.proto\x1a\x1cstats/base/stats_types.proto\"\x96\x01\n\x18StatsMessageOptionsProto\x12\x1c\n\x14\x63luster_id_attribute\x18\x01 \x01(\t\x12(\n cluster_incarnation_id_attribute\x18\x02 \x01(\t\x12\x32\n\x0eids_value_type\x18\x03 \x01(\x0e\x32\x1a.cohesity.stats.Value.Type\"\x81\x17\n\x11\x45ntitySchemaProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1f\n\x17schema_descriptive_name\x18\x05 \x01(\t\x12\x12\n\x07version\x18\x02 \x01(\x03:\x01\x30\x12U\n\x15\x61ttributes_descriptor\x18\x03 \x02(\x0b\x32\x36.cohesity.stats.EntitySchemaProto.AttributesDescriptor\x12Z\n\x1atime_series_descriptor_vec\x18\x04 \x03(\x0b\x32\x36.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor\x12\x18\n\x10schema_help_text\x18\x06 \x01(\t\x12\x1a\n\x12is_internal_schema\x18\x07 \x01(\x08\x12\x1f\n\x13\x66lush_interval_secs\x18\x08 \x01(\x05:\x02\x36\x30\x12#\n\x1blargest_flush_interval_secs\x18\t \x01(\x05\x12\x19\n\x11time_to_live_secs\x18\n \x01(\x03\x12M\n\x16rollup_granularity_vec\x18\x0b \x03(\x0b\x32-.cohesity.stats.EntitySchemaProto.Granularity\x12\x1b\n\renable_rollup\x18\x0c \x01(\x08:\x04true\x12\"\n\x1a\x65ntities_time_to_live_secs\x18\x0e \x01(\x03\x1aV\n\x12KeyValueDescriptor\x12\x10\n\x08key_name\x18\x01 \x02(\t\x12.\n\nvalue_type\x18\x02 \x02(\x0e\x32\x1a.cohesity.stats.Value.Type\x1a\xb1\x01\n\x14\x41ttributesDescriptor\x12K\n\rattribute_vec\x18\x01 \x03(\x0b\x32\x34.cohesity.stats.EntitySchemaProto.KeyValueDescriptor\x12 \n\x18key_attribute_name_index\x18\x02 \x02(\x05:*\x82\xb5\x18&\n\ncluster_id\x12\x16\x63luster_incarnation_id\x18\x00\x1a\xd7\x0f\n\x14TimeSeriesDescriptor\x12\x13\n\x0bmetric_name\x18\x01 \x02(\t\x12\x1f\n\x17metric_descriptive_name\x18\x08 \x01(\t\x12.\n\nvalue_type\x18\x02 \x02(\x0e\x32\x1a.cohesity.stats.Value.Type\x12V\n\x0bmetric_unit\x18\t \x01(\x0b\x32\x41.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.MetricUnit\x12l\n\x16\x61ggregation_descriptor\x18\x03 \x01(\x0b\x32L.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.AggregationDescriptor\x12\x31\n%raw_metric_publish_interval_hint_secs\x18\x04 \x01(\x05:\x02\x33\x30\x12\x19\n\x11time_to_live_secs\x18\x05 \x02(\x03\x12\x61\n\x19local_cluster_rollups_vec\x18\x06 \x03(\x0b\x32>.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.Rollups\x12\x62\n\x1aremote_cluster_rollups_vec\x18\x07 \x03(\x0b\x32>.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.Rollups\x1a\x85\x02\n\nMetricUnit\x12T\n\x04type\x18\x01 \x02(\x0e\x32\x46.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type\"\xa0\x01\n\x04Type\x12\n\n\x06kBytes\x10\x00\x12\x0e\n\nkTimeUsecs\x10\x01\x12\x0e\n\nkTimeMsecs\x10\x02\x12\r\n\tkTimeSecs\x10\x03\x12\r\n\tkTimeMins\x10\x04\x12\x0c\n\x08kCounter\x10\x05\x12\x13\n\x0fkTempCentigrade\x10\x06\x12\x13\n\x0fkTempFahrenheit\x10\x07\x12\x08\n\x04kRpm\x10\x08\x12\x0c\n\x08kPercent\x10\t\x1a\xb4\x01\n\x13\x41ggregationFunction\x12]\n\x04type\x18\x01 \x02(\x0e\x32O.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type\">\n\x04Type\x12\x08\n\x04kSum\x10\x00\x12\x0c\n\x08kAverage\x10\x01\x12\n\n\x06kCount\x10\x02\x12\x08\n\x04kMax\x10\x03\x12\x08\n\x04kMin\x10\x04\x1a\xa5\x03\n\x15\x41ggregationDescriptor\x12\x1a\n\x12source_schema_name\x18\x01 \x01(\t\x12\x1e\n\x16source_metric_name_vec\x18\x02 \x03(\t\x12%\n\x18\x61ggregation_interval_sec\x18\x03 \x01(\x05:\x03\x33\x30\x30\x12h\n\x14\x61ggregation_function\x18\x04 \x02(\x0b\x32J.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction\x12^\n\x0frollup_function\x18\x05 \x02(\x0b\x32\x45.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction\x12#\n\x15use_latest_data_point\x18\x06 \x01(\x08:\x04true\x12:\n+skip_aggregation_for_missing_source_metrics\x18\x07 \x01(\x08:\x05\x66\x61lse\x1a\xfd\x01\n\x0eRollupFunction\x12X\n\x04type\x18\x01 \x02(\x0e\x32J.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type\"\x90\x01\n\x04Type\x12\x08\n\x04kSum\x10\x00\x12\x0c\n\x08kAverage\x10\x01\x12\n\n\x06kCount\x10\x02\x12\x08\n\x04kMax\x10\x03\x12\x08\n\x04kMin\x10\x04\x12\x0b\n\x07kMedian\x10\x05\x12\x11\n\rkPercentile95\x10\x06\x12\x0b\n\x07kLatest\x10\x07\x12\t\n\x05kRate\x10\x08\x12\x18\n\x14kRollupFunctionCount\x10\t\x1a\x96\x02\n\x07Rollups\x12^\n\x0frollup_function\x18\x01 \x02(\x0b\x32\x45.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction\x12\x63\n\x0fgranularity_vec\x18\x02 \x03(\x0b\x32J.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.Rollups.Granularity\x1a\x46\n\x0bGranularity\x12\x1c\n\x14rollup_interval_secs\x18\x01 \x02(\x05\x12\x19\n\x11time_to_live_secs\x18\x02 \x02(\x03\x1a\x46\n\x0bGranularity\x12\x1c\n\x14rollup_interval_secs\x18\x01 \x02(\x05\x12\x19\n\x11time_to_live_secs\x18\x02 \x02(\x03J\x04\x08\r\x10\x0eR\x1b\x65ntities_time_to_live_msecs\"L\n\x10\x45ntitySchemaList\x12\x38\n\rentity_schema\x18\x01 \x03(\x0b\x32!.cohesity.stats.EntitySchemaProto:j\n\x15stats_message_options\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x0b\x32(.cohesity.stats.StatsMessageOptionsProtoB\x1dZ\x1bstats/base/entity_schema.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats.base.entity_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033stats/base/entity_schema.pb'
  _globals['_ENTITYSCHEMAPROTO_ATTRIBUTESDESCRIPTOR']._loaded_options = None
  _globals['_ENTITYSCHEMAPROTO_ATTRIBUTESDESCRIPTOR']._serialized_options = b'\202\265\030&\n\ncluster_id\022\026cluster_incarnation_id\030\000'
  _globals['_STATSMESSAGEOPTIONSPROTO']._serialized_start=115
  _globals['_STATSMESSAGEOPTIONSPROTO']._serialized_end=265
  _globals['_ENTITYSCHEMAPROTO']._serialized_start=268
  _globals['_ENTITYSCHEMAPROTO']._serialized_end=3213
  _globals['_ENTITYSCHEMAPROTO_KEYVALUEDESCRIPTOR']._serialized_start=830
  _globals['_ENTITYSCHEMAPROTO_KEYVALUEDESCRIPTOR']._serialized_end=916
  _globals['_ENTITYSCHEMAPROTO_ATTRIBUTESDESCRIPTOR']._serialized_start=919
  _globals['_ENTITYSCHEMAPROTO_ATTRIBUTESDESCRIPTOR']._serialized_end=1096
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR']._serialized_start=1099
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR']._serialized_end=3106
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_METRICUNIT']._serialized_start=1701
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_METRICUNIT']._serialized_end=1962
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_METRICUNIT_TYPE']._serialized_start=1802
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_METRICUNIT_TYPE']._serialized_end=1962
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONFUNCTION']._serialized_start=1965
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONFUNCTION']._serialized_end=2145
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONFUNCTION_TYPE']._serialized_start=2083
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONFUNCTION_TYPE']._serialized_end=2145
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONDESCRIPTOR']._serialized_start=2148
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_AGGREGATIONDESCRIPTOR']._serialized_end=2569
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPFUNCTION']._serialized_start=2572
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPFUNCTION']._serialized_end=2825
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPFUNCTION_TYPE']._serialized_start=2681
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPFUNCTION_TYPE']._serialized_end=2825
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPS']._serialized_start=2828
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPS']._serialized_end=3106
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPS_GRANULARITY']._serialized_start=3036
  _globals['_ENTITYSCHEMAPROTO_TIMESERIESDESCRIPTOR_ROLLUPS_GRANULARITY']._serialized_end=3106
  _globals['_ENTITYSCHEMAPROTO_GRANULARITY']._serialized_start=3036
  _globals['_ENTITYSCHEMAPROTO_GRANULARITY']._serialized_end=3106
  _globals['_ENTITYSCHEMALIST']._serialized_start=3215
  _globals['_ENTITYSCHEMALIST']._serialized_end=3291
# @@protoc_insertion_point(module_scope)
