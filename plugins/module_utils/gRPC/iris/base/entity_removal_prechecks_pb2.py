# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/entity_removal_prechecks.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(iris/base/entity_removal_prechecks.proto\x12\x13\x63ohesity.nexus.base\"_\n\rPrechecksInfo\x12\x15\n\rprecheck_name\x18\x01 \x01(\t\x12\x17\n\x0fprecheck_passed\x18\x02 \x01(\x08\x12\x1e\n\x16precheck_error_message\x18\x03 \x01(\t\"\x86\x01\n\x0fPrechecksResult\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12 \n\x18\x65xecution_timestamp_secs\x18\x02 \x01(\x03\x12>\n\x12prechecks_info_vec\x18\x03 \x03(\x0b\x32\".cohesity.nexus.base.PrechecksInfo\"W\n\x10PrechecksResults\x12\x43\n\x15prechecks_results_vec\x18\x01 \x03(\x0b\x32$.cohesity.nexus.base.PrechecksResultB\'Z%iris/base/entity_removal_prechecks.pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.entity_removal_prechecks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%iris/base/entity_removal_prechecks.pb'
  _globals['_PRECHECKSINFO']._serialized_start=65
  _globals['_PRECHECKSINFO']._serialized_end=160
  _globals['_PRECHECKSRESULT']._serialized_start=163
  _globals['_PRECHECKSRESULT']._serialized_end=297
  _globals['_PRECHECKSRESULTS']._serialized_start=299
  _globals['_PRECHECKSRESULTS']._serialized_end=386
# @@protoc_insertion_point(module_scope)
