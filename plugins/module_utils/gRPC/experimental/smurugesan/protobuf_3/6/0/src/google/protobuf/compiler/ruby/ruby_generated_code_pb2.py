# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/src/google/protobuf/compiler/ruby/ruby_generated_code.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nbexperimental/smurugesan/protobuf-3.6.0/src/google/protobuf/compiler/ruby/ruby_generated_code.proto\x12\x05\x41.B.C\"\xc6\x11\n\x0bTestMessage\x12\x16\n\x0eoptional_int32\x18\x01 \x01(\x05\x12\x16\n\x0eoptional_int64\x18\x02 \x01(\x03\x12\x17\n\x0foptional_uint32\x18\x03 \x01(\r\x12\x17\n\x0foptional_uint64\x18\x04 \x01(\x04\x12\x15\n\roptional_bool\x18\x05 \x01(\x08\x12\x17\n\x0foptional_double\x18\x06 \x01(\x01\x12\x16\n\x0eoptional_float\x18\x07 \x01(\x02\x12\x17\n\x0foptional_string\x18\x08 \x01(\t\x12\x16\n\x0eoptional_bytes\x18\t \x01(\x0c\x12&\n\roptional_enum\x18\n \x01(\x0e\x32\x0f.A.B.C.TestEnum\x12(\n\x0coptional_msg\x18\x0b \x01(\x0b\x32\x12.A.B.C.TestMessage\x12\x16\n\x0erepeated_int32\x18\x15 \x03(\x05\x12\x16\n\x0erepeated_int64\x18\x16 \x03(\x03\x12\x17\n\x0frepeated_uint32\x18\x17 \x03(\r\x12\x17\n\x0frepeated_uint64\x18\x18 \x03(\x04\x12\x15\n\rrepeated_bool\x18\x19 \x03(\x08\x12\x17\n\x0frepeated_double\x18\x1a \x03(\x01\x12\x16\n\x0erepeated_float\x18\x1b \x03(\x02\x12\x17\n\x0frepeated_string\x18\x1c \x03(\t\x12\x16\n\x0erepeated_bytes\x18\x1d \x03(\x0c\x12&\n\rrepeated_enum\x18\x1e \x03(\x0e\x32\x0f.A.B.C.TestEnum\x12(\n\x0crepeated_msg\x18\x1f \x03(\x0b\x32\x12.A.B.C.TestMessage\x12\x15\n\x0boneof_int32\x18) \x01(\x05H\x00\x12\x15\n\x0boneof_int64\x18* \x01(\x03H\x00\x12\x16\n\x0coneof_uint32\x18+ \x01(\rH\x00\x12\x16\n\x0coneof_uint64\x18, \x01(\x04H\x00\x12\x14\n\noneof_bool\x18- \x01(\x08H\x00\x12\x16\n\x0coneof_double\x18. \x01(\x01H\x00\x12\x15\n\x0boneof_float\x18/ \x01(\x02H\x00\x12\x16\n\x0coneof_string\x18\x30 \x01(\tH\x00\x12\x15\n\x0boneof_bytes\x18\x31 \x01(\x0cH\x00\x12%\n\noneof_enum\x18\x32 \x01(\x0e\x32\x0f.A.B.C.TestEnumH\x00\x12\'\n\toneof_msg\x18\x33 \x01(\x0b\x32\x12.A.B.C.TestMessageH\x00\x12@\n\x10map_int32_string\x18= \x03(\x0b\x32&.A.B.C.TestMessage.MapInt32StringEntry\x12@\n\x10map_int64_string\x18> \x03(\x0b\x32&.A.B.C.TestMessage.MapInt64StringEntry\x12\x42\n\x11map_uint32_string\x18? \x03(\x0b\x32\'.A.B.C.TestMessage.MapUint32StringEntry\x12\x42\n\x11map_uint64_string\x18@ \x03(\x0b\x32\'.A.B.C.TestMessage.MapUint64StringEntry\x12>\n\x0fmap_bool_string\x18\x41 \x03(\x0b\x32%.A.B.C.TestMessage.MapBoolStringEntry\x12\x42\n\x11map_string_string\x18\x42 \x03(\x0b\x32\'.A.B.C.TestMessage.MapStringStringEntry\x12<\n\x0emap_string_msg\x18\x43 \x03(\x0b\x32$.A.B.C.TestMessage.MapStringMsgEntry\x12>\n\x0fmap_string_enum\x18\x44 \x03(\x0b\x32%.A.B.C.TestMessage.MapStringEnumEntry\x12@\n\x10map_string_int32\x18\x45 \x03(\x0b\x32&.A.B.C.TestMessage.MapStringInt32Entry\x12>\n\x0fmap_string_bool\x18\x46 \x03(\x0b\x32%.A.B.C.TestMessage.MapStringBoolEntry\x12\x38\n\x0enested_message\x18P \x01(\x0b\x32 .A.B.C.TestMessage.NestedMessage\x1a\x35\n\x13MapInt32StringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13MapInt64StringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14MapUint32StringEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14MapUint64StringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12MapBoolStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14MapStringStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aG\n\x11MapStringMsgEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.A.B.C.TestMessage:\x02\x38\x01\x1a\x45\n\x12MapStringEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0e\x32\x0f.A.B.C.TestEnum:\x02\x38\x01\x1a\x35\n\x13MapStringInt32Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x34\n\x12MapStringBoolEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x1c\n\rNestedMessage\x12\x0b\n\x03\x66oo\x18\x01 \x01(\x05\x42\n\n\x08my_oneof*,\n\x08TestEnum\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x05\n\x01\x41\x10\x01\x12\x05\n\x01\x42\x10\x02\x12\x05\n\x01\x43\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.src.google.protobuf.compiler.ruby.ruby_generated_code_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTMESSAGE_MAPINT32STRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPINT32STRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPINT64STRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPINT64STRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPUINT32STRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPUINT32STRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPUINT64STRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPUINT64STRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPBOOLSTRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPBOOLSTRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPSTRINGSTRINGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPSTRINGSTRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPSTRINGMSGENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPSTRINGMSGENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPSTRINGENUMENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPSTRINGENUMENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPSTRINGINT32ENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPSTRINGINT32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTMESSAGE_MAPSTRINGBOOLENTRY']._loaded_options = None
  _globals['_TESTMESSAGE_MAPSTRINGBOOLENTRY']._serialized_options = b'8\001'
  _globals['_TESTENUM']._serialized_start=2358
  _globals['_TESTENUM']._serialized_end=2402
  _globals['_TESTMESSAGE']._serialized_start=110
  _globals['_TESTMESSAGE']._serialized_end=2356
  _globals['_TESTMESSAGE_MAPINT32STRINGENTRY']._serialized_start=1731
  _globals['_TESTMESSAGE_MAPINT32STRINGENTRY']._serialized_end=1784
  _globals['_TESTMESSAGE_MAPINT64STRINGENTRY']._serialized_start=1786
  _globals['_TESTMESSAGE_MAPINT64STRINGENTRY']._serialized_end=1839
  _globals['_TESTMESSAGE_MAPUINT32STRINGENTRY']._serialized_start=1841
  _globals['_TESTMESSAGE_MAPUINT32STRINGENTRY']._serialized_end=1895
  _globals['_TESTMESSAGE_MAPUINT64STRINGENTRY']._serialized_start=1897
  _globals['_TESTMESSAGE_MAPUINT64STRINGENTRY']._serialized_end=1951
  _globals['_TESTMESSAGE_MAPBOOLSTRINGENTRY']._serialized_start=1953
  _globals['_TESTMESSAGE_MAPBOOLSTRINGENTRY']._serialized_end=2005
  _globals['_TESTMESSAGE_MAPSTRINGSTRINGENTRY']._serialized_start=2007
  _globals['_TESTMESSAGE_MAPSTRINGSTRINGENTRY']._serialized_end=2061
  _globals['_TESTMESSAGE_MAPSTRINGMSGENTRY']._serialized_start=2063
  _globals['_TESTMESSAGE_MAPSTRINGMSGENTRY']._serialized_end=2134
  _globals['_TESTMESSAGE_MAPSTRINGENUMENTRY']._serialized_start=2136
  _globals['_TESTMESSAGE_MAPSTRINGENUMENTRY']._serialized_end=2205
  _globals['_TESTMESSAGE_MAPSTRINGINT32ENTRY']._serialized_start=2207
  _globals['_TESTMESSAGE_MAPSTRINGINT32ENTRY']._serialized_end=2260
  _globals['_TESTMESSAGE_MAPSTRINGBOOLENTRY']._serialized_start=2262
  _globals['_TESTMESSAGE_MAPSTRINGBOOLENTRY']._serialized_end=2314
  _globals['_TESTMESSAGE_NESTEDMESSAGE']._serialized_start=2316
  _globals['_TESTMESSAGE_NESTEDMESSAGE']._serialized_end=2344
# @@protoc_insertion_point(module_scope)
