# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/objectivec/Tests/unittest_deprecated.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQexperimental/smurugesan/protobuf-3.6.0/objectivec/Tests/unittest_deprecated.proto\x12\x13protobuf_deprecated\"\x8c\x01\n\x04Msg1\x12\x18\n\x0cstring_field\x18\x01 \x01(\tB\x02\x18\x01\x12\x15\n\tint_field\x18\x02 \x02(\x05\x42\x02\x18\x01\x12\x17\n\x0b\x66ixed_field\x18\x03 \x03(\x07\x42\x02\x18\x01\x12\x30\n\tmsg_field\x18\x04 \x01(\x0b\x32\x19.protobuf_deprecated.Msg1B\x02\x18\x01*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x87\x02\n\x05Msg1A29\n\x11string_ext2_field\x12\x19.protobuf_deprecated.Msg1\x18\xc9\x01 \x01(\tB\x02\x18\x01\x32\x36\n\x0eint_ext2_field\x12\x19.protobuf_deprecated.Msg1\x18\xca\x01 \x01(\x05\x42\x02\x18\x01\x32\x38\n\x10\x66ixed_ext2_field\x12\x19.protobuf_deprecated.Msg1\x18\xcb\x01 \x03(\x07\x42\x02\x18\x01\x32Q\n\x0emsg_ext2_field\x12\x19.protobuf_deprecated.Msg1\x18\xcc\x01 \x01(\x0b\x32\x19.protobuf_deprecated.Msg1B\x02\x18\x01\"H\n\x04Msg2\x12\x14\n\x0cstring_field\x18\x01 \x01(\t\x12\x11\n\tint_field\x18\x02 \x02(\x05\x12\x13\n\x0b\x66ixed_field\x18\x03 \x03(\x07:\x02\x18\x01*:\n\x05\x45num1\x12\r\n\tENUM1_ONE\x10\x01\x12\r\n\tENUM1_TWO\x10\x02\x12\x13\n\x0b\x45NUM1_THREE\x10\x03\x1a\x02\x08\x01*:\n\x05\x45num2\x12\r\n\tENUM2_ONE\x10\x01\x12\r\n\tENUM2_TWO\x10\x02\x12\x0f\n\x0b\x45NUM2_THREE\x10\x03\x1a\x02\x18\x01:7\n\x10string_ext_field\x12\x19.protobuf_deprecated.Msg1\x18\x65 \x01(\tB\x02\x18\x01:4\n\rint_ext_field\x12\x19.protobuf_deprecated.Msg1\x18\x66 \x01(\x05\x42\x02\x18\x01:6\n\x0f\x66ixed_ext_field\x12\x19.protobuf_deprecated.Msg1\x18g \x03(\x07\x42\x02\x18\x01:O\n\rmsg_ext_field\x12\x19.protobuf_deprecated.Msg1\x18h \x01(\x0b\x32\x19.protobuf_deprecated.Msg1B\x02\x18\x01\x42\x06\xa2\x02\x03\x44\x65p')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.objectivec.Tests.unittest_deprecated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\242\002\003Dep'
  _globals['_ENUM1'].values_by_name["ENUM1_THREE"]._loaded_options = None
  _globals['_ENUM1'].values_by_name["ENUM1_THREE"]._serialized_options = b'\010\001'
  _globals['_ENUM2']._loaded_options = None
  _globals['_ENUM2']._serialized_options = b'\030\001'
  _globals['string_ext_field']._loaded_options = None
  _globals['string_ext_field']._serialized_options = b'\030\001'
  _globals['int_ext_field']._loaded_options = None
  _globals['int_ext_field']._serialized_options = b'\030\001'
  _globals['fixed_ext_field']._loaded_options = None
  _globals['fixed_ext_field']._serialized_options = b'\030\001'
  _globals['msg_ext_field']._loaded_options = None
  _globals['msg_ext_field']._serialized_options = b'\030\001'
  _globals['_MSG1'].fields_by_name['string_field']._loaded_options = None
  _globals['_MSG1'].fields_by_name['string_field']._serialized_options = b'\030\001'
  _globals['_MSG1'].fields_by_name['int_field']._loaded_options = None
  _globals['_MSG1'].fields_by_name['int_field']._serialized_options = b'\030\001'
  _globals['_MSG1'].fields_by_name['fixed_field']._loaded_options = None
  _globals['_MSG1'].fields_by_name['fixed_field']._serialized_options = b'\030\001'
  _globals['_MSG1'].fields_by_name['msg_field']._loaded_options = None
  _globals['_MSG1'].fields_by_name['msg_field']._serialized_options = b'\030\001'
  _globals['_MSG1A'].extensions_by_name['string_ext2_field']._loaded_options = None
  _globals['_MSG1A'].extensions_by_name['string_ext2_field']._serialized_options = b'\030\001'
  _globals['_MSG1A'].extensions_by_name['int_ext2_field']._loaded_options = None
  _globals['_MSG1A'].extensions_by_name['int_ext2_field']._serialized_options = b'\030\001'
  _globals['_MSG1A'].extensions_by_name['fixed_ext2_field']._loaded_options = None
  _globals['_MSG1A'].extensions_by_name['fixed_ext2_field']._serialized_options = b'\030\001'
  _globals['_MSG1A'].extensions_by_name['msg_ext2_field']._loaded_options = None
  _globals['_MSG1A'].extensions_by_name['msg_ext2_field']._serialized_options = b'\030\001'
  _globals['_MSG2']._loaded_options = None
  _globals['_MSG2']._serialized_options = b'\030\001'
  _globals['_ENUM1']._serialized_start=589
  _globals['_ENUM1']._serialized_end=647
  _globals['_ENUM2']._serialized_start=649
  _globals['_ENUM2']._serialized_end=707
  _globals['_MSG1']._serialized_start=107
  _globals['_MSG1']._serialized_end=247
  _globals['_MSG1A']._serialized_start=250
  _globals['_MSG1A']._serialized_end=513
  _globals['_MSG2']._serialized_start=515
  _globals['_MSG2']._serialized_end=587
# @@protoc_insertion_point(module_scope)
