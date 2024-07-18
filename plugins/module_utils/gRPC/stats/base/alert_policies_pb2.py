# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stats/base/alert_policies.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stats.base import alert_type_pb2 as stats_dot_base_dot_alert__type__pb2
from stats.base import entity_schema_pb2 as stats_dot_base_dot_entity__schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fstats/base/alert_policies.proto\x12\x0e\x63ohesity.stats\x1a\x1bstats/base/alert_type.proto\x1a\x1estats/base/entity_schema.proto\"\xbd\x07\n\x10\x41lertPolicyProto\x12\x38\n\ralert_type_id\x18\x01 \x02(\x0e\x32!.cohesity.stats.AlertTypeProto.Id\x12 \n\x18\x61lert_policy_description\x18\x02 \x02(\t\x12\x1a\n\x12\x65ntity_schema_name\x18\x03 \x02(\t\x12;\n\nmetric_vec\x18\x04 \x03(\x0b\x32\'.cohesity.stats.AlertPolicyProto.Metric\x12\x46\n\x12\x63ritical_threshold\x18\x05 \x01(\x0b\x32*.cohesity.stats.AlertPolicyProto.Threshold\x12\x45\n\x11warning_threshold\x18\x06 \x01(\x0b\x32*.cohesity.stats.AlertPolicyProto.Threshold\x12\x42\n\x0einfo_threshold\x18\x07 \x01(\x0b\x32*.cohesity.stats.AlertPolicyProto.Threshold\x12(\n\x1a\x61scending_order_thresholds\x18\x08 \x01(\x08:\x04true\x12\x1d\n\x15min_allowed_threshold\x18\t \x02(\x01\x12\x1d\n\x15max_allowed_threshold\x18\n \x02(\x01\x12;\n\x08\x64uration\x18\x0b \x02(\x0b\x32).cohesity.stats.AlertPolicyProto.Duration\x12\x13\n\x0bmetric_unit\x18\x0c \x02(\t\x12\x11\n\thelp_text\x18\r \x01(\t\x1av\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x02(\t\x12^\n\x0frollup_function\x18\x02 \x02(\x0b\x32\x45.cohesity.stats.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction\x1a\x46\n\tThreshold\x12\x19\n\x11\x64\x65\x66\x61ult_threshold\x18\x01 \x02(\x01\x12\x1e\n\x16user_defined_threshold\x18\x02 \x01(\x01\x1a\x93\x01\n\x08\x44uration\x12\x1d\n\x15\x64\x65\x66\x61ult_duration_secs\x18\x01 \x02(\x03\x12\"\n\x1auser_defined_duration_secs\x18\x02 \x01(\x03\x12!\n\x19min_allowed_duration_secs\x18\x03 \x02(\x03\x12!\n\x19max_allowed_duration_secs\x18\x04 \x02(\x03\"g\n\x12\x41lertPoliciesProto\x12\x0f\n\x07version\x18\x01 \x02(\x03\x12@\n\x16\x61lert_policy_proto_vec\x18\x02 \x03(\x0b\x32 .cohesity.stats.AlertPolicyProtoB\x1eZ\x1cstats/base/alert_policies.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats.base.alert_policies_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034stats/base/alert_policies.pb'
  _globals['_ALERTPOLICYPROTO']._serialized_start=113
  _globals['_ALERTPOLICYPROTO']._serialized_end=1070
  _globals['_ALERTPOLICYPROTO_METRIC']._serialized_start=730
  _globals['_ALERTPOLICYPROTO_METRIC']._serialized_end=848
  _globals['_ALERTPOLICYPROTO_THRESHOLD']._serialized_start=850
  _globals['_ALERTPOLICYPROTO_THRESHOLD']._serialized_end=920
  _globals['_ALERTPOLICYPROTO_DURATION']._serialized_start=923
  _globals['_ALERTPOLICYPROTO_DURATION']._serialized_end=1070
  _globals['_ALERTPOLICIESPROTO']._serialized_start=1072
  _globals['_ALERTPOLICIESPROTO']._serialized_end=1175
# @@protoc_insertion_point(module_scope)