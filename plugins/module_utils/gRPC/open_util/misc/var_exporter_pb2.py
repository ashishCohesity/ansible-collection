# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/misc/var_exporter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!open_util/misc/var_exporter.proto\x12\rcohesity.misc\"\xea\x03\n\x10VarExporterProto\x12P\n\x12key_value_pair_map\x18\x01 \x03(\x0b\x32\x34.cohesity.misc.VarExporterProto.KeyValuePairMapEntry\x1a\x9f\x02\n\nValueProto\x12\x10\n\x08val_bool\x18\x01 \x01(\x08\x12\x11\n\tval_int64\x18\x02 \x01(\x03\x12\x16\n\x0eval_int128_msb\x18\x03 \x01(\x03\x12\x12\n\nval_uint64\x18\x04 \x01(\x04\x12\x17\n\x0fval_uint128_msb\x18\x05 \x01(\x04\x12\x12\n\nval_string\x18\x06 \x01(\t\x12\x12\n\nval_double\x18\x07 \x01(\x01\x12;\n\x07val_vec\x18\x08 \x03(\x0b\x32*.cohesity.misc.VarExporterProto.ValueProto\x12\x42\n\x0eval_mapkey_vec\x18\t \x03(\x0b\x32*.cohesity.misc.VarExporterProto.ValueProto\x1a\x62\n\x14KeyValuePairMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.cohesity.misc.VarExporterProto.ValueProto:\x02\x38\x01\x42 Z\x1eopen_util/misc/var_exporter.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.misc.var_exporter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\036open_util/misc/var_exporter.pb'
  _globals['_VAREXPORTERPROTO_KEYVALUEPAIRMAPENTRY']._loaded_options = None
  _globals['_VAREXPORTERPROTO_KEYVALUEPAIRMAPENTRY']._serialized_options = b'8\001'
  _globals['_VAREXPORTERPROTO']._serialized_start=53
  _globals['_VAREXPORTERPROTO']._serialized_end=543
  _globals['_VAREXPORTERPROTO_VALUEPROTO']._serialized_start=156
  _globals['_VAREXPORTERPROTO_VALUEPROTO']._serialized_end=443
  _globals['_VAREXPORTERPROTO_KEYVALUEPAIRMAPENTRY']._serialized_start=445
  _globals['_VAREXPORTERPROTO_KEYVALUEPAIRMAPENTRY']._serialized_end=543
# @@protoc_insertion_point(module_scope)
