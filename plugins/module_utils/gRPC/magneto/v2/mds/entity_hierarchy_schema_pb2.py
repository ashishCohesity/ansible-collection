# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/v2/mds/entity_hierarchy_schema.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,magneto/v2/mds/entity_hierarchy_schema.proto\x12\x14\x63ohesity.magneto.mds\"\xa4\x05\n\x1a\x45ntityAttributesNamesProto\x12 \n\x0bis_taskable\x18\x01 \x01(\t:\x0bis_taskable\x12\x32\n\x14is_registered_source\x18\x02 \x01(\t:\x14is_registered_source\x12\x44\n\x1dregistered_source_primary_key\x18\x03 \x01(\t:\x1dregistered_source_primary_key\x12\x38\n\x17last_refresh_start_time\x18\x04 \x01(\t:\x17last_refresh_start_time\x12.\n\x12last_refresh_error\x18\x05 \x01(\t:\x12last_refresh_error\x12\x36\n\x16num_protected_children\x18\x06 \x01(\t:\x16num_protected_children\x12\x44\n\x1dtotal_protected_bytes_logical\x18\x07 \x01(\t:\x1dtotal_protected_bytes_logical\x12:\n\x18num_unprotected_children\x18\x08 \x01(\t:\x18num_unprotected_children\x12H\n\x1ftotal_unprotected_bytes_logical\x18\t \x01(\t:\x1ftotal_unprotected_bytes_logical\x12\x1a\n\x08\x63hecksum\x18\n \x01(\t:\x08\x63hecksum\x12*\n\x10\x64\x65tached_from_eh\x18\x0b \x01(\t:\x10\x64\x65tached_from_eh\x12\x34\n\x15logical_size_in_bytes\x18\x0c \x01(\t:\x15logical_size_in_bytes\"\xac\x01\n\x1a\x45ntityAttachmentNamesProto\x12,\n\x11registration_info\x18\x01 \x01(\t:\x11registration_info\x12\x36\n\x16registered_entity_info\x18\x02 \x01(\t:\x16registered_entity_info\x12(\n\x0f\x61ggregated_info\x18\x03 \x01(\t:\x0f\x61ggregated_info\"\xfb\x02\n\x19\x41ggregatedEntityInfoProto\x12\x63\n\x17\x61ggregated_counters_vec\x18\x01 \x03(\x0b\x32\x42.cohesity.magneto.mds.AggregatedEntityInfoProto.AggregatedCounters\x1a(\n\x08\x43ounters\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\r\n\x05\x62ytes\x18\x02 \x01(\x03\x1a\xce\x01\n\x12\x41ggregatedCounters\x12\x1c\n\x14\x65nvironment_type_str\x18\x01 \x01(\t\x12K\n\tprotected\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.mds.AggregatedEntityInfoProto.Counters\x12M\n\x0bunprotected\x18\x03 \x01(\x0b\x32\x38.cohesity.magneto.mds.AggregatedEntityInfoProto.Counters\"d\n\x1cPrincipalAttributeNamesProto\x12\x1c\n\ttenant_id\x18\x01 \x01(\t:\ttenant_id\x12&\n\x0eserialized_sid\x18\x02 \x01(\t:\x0eserialized_sid')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.v2.mds.entity_hierarchy_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITYATTRIBUTESNAMESPROTO']._serialized_start=71
  _globals['_ENTITYATTRIBUTESNAMESPROTO']._serialized_end=747
  _globals['_ENTITYATTACHMENTNAMESPROTO']._serialized_start=750
  _globals['_ENTITYATTACHMENTNAMESPROTO']._serialized_end=922
  _globals['_AGGREGATEDENTITYINFOPROTO']._serialized_start=925
  _globals['_AGGREGATEDENTITYINFOPROTO']._serialized_end=1304
  _globals['_AGGREGATEDENTITYINFOPROTO_COUNTERS']._serialized_start=1055
  _globals['_AGGREGATEDENTITYINFOPROTO_COUNTERS']._serialized_end=1095
  _globals['_AGGREGATEDENTITYINFOPROTO_AGGREGATEDCOUNTERS']._serialized_start=1098
  _globals['_AGGREGATEDENTITYINFOPROTO_AGGREGATEDCOUNTERS']._serialized_end=1304
  _globals['_PRINCIPALATTRIBUTENAMESPROTO']._serialized_start=1306
  _globals['_PRINCIPALATTRIBUTENAMESPROTO']._serialized_end=1406
# @@protoc_insertion_point(module_scope)
