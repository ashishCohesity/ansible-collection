# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/es/query_dsl.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yoda.es import jsonname_pb2 as yoda_dot_es_dot_jsonname__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17yoda/es/query_dsl.proto\x12\x10\x63ohesity.yoda.es\x1a\x16yoda/es/jsonname.proto\"\x8f\x01\n\x08QueryDsl\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.cohesity.yoda.es.Query\x12(\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x18.cohesity.yoda.es.Filter\x12\x31\n\x08\x66iltered\x18\x03 \x01(\x0b\x32\x1f.cohesity.yoda.es.FilteredQuery\"a\n\rFilteredQuery\x12&\n\x05query\x18\x01 \x02(\x0b\x32\x17.cohesity.yoda.es.Query\x12(\n\x06\x66ilter\x18\x02 \x02(\x0b\x32\x18.cohesity.yoda.es.Filter\"4\n\x14StringStringMapEntry\x12\x0c\n\x04_key\x18\x01 \x02(\t\x12\x0e\n\x06_value\x18\x02 \x02(\t\"\\\n\x11MapEntryStringMap\x12\x0c\n\x04_key\x18\x01 \x01(\t\x12\x39\n\x06_value\x18\x02 \x03(\x0b\x32#.cohesity.yoda.es.MapEntryStringIntB\x04\x98\xb5\x18\x01\"1\n\x11MapEntryStringInt\x12\x0c\n\x04_key\x18\x01 \x01(\t\x12\x0e\n\x06_value\x18\x02 \x01(\x03\"\xc6\x02\n\x05Query\x12L\n\nterm_query\x18\x01 \x03(\x0b\x32&.cohesity.yoda.es.StringStringMapEntryB\x10\x92\xb5\x18\x04term\x98\xb5\x18\x01\xa0\xb5\x18\x01\x12P\n\x0cprefix_query\x18\x02 \x03(\x0b\x32&.cohesity.yoda.es.StringStringMapEntryB\x12\x92\xb5\x18\x06prefix\x98\xb5\x18\x01\xa0\xb5\x18\x01\x12P\n\x12query_string_query\x18\x03 \x01(\x0b\x32\".cohesity.yoda.es.QueryStringQueryB\x10\x92\xb5\x18\x0cquery_string\x12K\n\x0brange_query\x18\x04 \x03(\x0b\x32#.cohesity.yoda.es.MapEntryStringMapB\x11\x92\xb5\x18\x05range\x98\xb5\x18\x01\xa0\xb5\x18\x01\">\n\x10QueryStringQuery\x12\r\n\x05query\x18\x01 \x02(\t\x12\x1b\n\rdefault_field\x18\x02 \x01(\t:\x04_all\"\xfa\x01\n\x06\x46ilter\x12M\n\x0bterm_filter\x18\x01 \x03(\x0b\x32&.cohesity.yoda.es.StringStringMapEntryB\x10\x92\xb5\x18\x04term\x98\xb5\x18\x01\xa0\xb5\x18\x01\x12\x35\n\nnot_filter\x18\x02 \x01(\x0b\x32\x18.cohesity.yoda.es.FilterB\x07\x92\xb5\x18\x03not\x12\x35\n\nand_filter\x18\x03 \x03(\x0b\x32\x18.cohesity.yoda.es.FilterB\x07\x92\xb5\x18\x03\x61nd\x12\x33\n\tor_filter\x18\x04 \x03(\x0b\x32\x18.cohesity.yoda.es.FilterB\x06\x92\xb5\x18\x02or')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.es.query_dsl_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MAPENTRYSTRINGMAP'].fields_by_name['_value']._loaded_options = None
  _globals['_MAPENTRYSTRINGMAP'].fields_by_name['_value']._serialized_options = b'\230\265\030\001'
  _globals['_QUERY'].fields_by_name['term_query']._loaded_options = None
  _globals['_QUERY'].fields_by_name['term_query']._serialized_options = b'\222\265\030\004term\230\265\030\001\240\265\030\001'
  _globals['_QUERY'].fields_by_name['prefix_query']._loaded_options = None
  _globals['_QUERY'].fields_by_name['prefix_query']._serialized_options = b'\222\265\030\006prefix\230\265\030\001\240\265\030\001'
  _globals['_QUERY'].fields_by_name['query_string_query']._loaded_options = None
  _globals['_QUERY'].fields_by_name['query_string_query']._serialized_options = b'\222\265\030\014query_string'
  _globals['_QUERY'].fields_by_name['range_query']._loaded_options = None
  _globals['_QUERY'].fields_by_name['range_query']._serialized_options = b'\222\265\030\005range\230\265\030\001\240\265\030\001'
  _globals['_FILTER'].fields_by_name['term_filter']._loaded_options = None
  _globals['_FILTER'].fields_by_name['term_filter']._serialized_options = b'\222\265\030\004term\230\265\030\001\240\265\030\001'
  _globals['_FILTER'].fields_by_name['not_filter']._loaded_options = None
  _globals['_FILTER'].fields_by_name['not_filter']._serialized_options = b'\222\265\030\003not'
  _globals['_FILTER'].fields_by_name['and_filter']._loaded_options = None
  _globals['_FILTER'].fields_by_name['and_filter']._serialized_options = b'\222\265\030\003and'
  _globals['_FILTER'].fields_by_name['or_filter']._loaded_options = None
  _globals['_FILTER'].fields_by_name['or_filter']._serialized_options = b'\222\265\030\002or'
  _globals['_QUERYDSL']._serialized_start=70
  _globals['_QUERYDSL']._serialized_end=213
  _globals['_FILTEREDQUERY']._serialized_start=215
  _globals['_FILTEREDQUERY']._serialized_end=312
  _globals['_STRINGSTRINGMAPENTRY']._serialized_start=314
  _globals['_STRINGSTRINGMAPENTRY']._serialized_end=366
  _globals['_MAPENTRYSTRINGMAP']._serialized_start=368
  _globals['_MAPENTRYSTRINGMAP']._serialized_end=460
  _globals['_MAPENTRYSTRINGINT']._serialized_start=462
  _globals['_MAPENTRYSTRINGINT']._serialized_end=511
  _globals['_QUERY']._serialized_start=514
  _globals['_QUERY']._serialized_end=840
  _globals['_QUERYSTRINGQUERY']._serialized_start=842
  _globals['_QUERYSTRINGQUERY']._serialized_end=904
  _globals['_FILTER']._serialized_start=907
  _globals['_FILTER']._serialized_end=1157
# @@protoc_insertion_point(module_scope)
