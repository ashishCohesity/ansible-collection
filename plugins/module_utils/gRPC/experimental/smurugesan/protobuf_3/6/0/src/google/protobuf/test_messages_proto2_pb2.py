# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/src/google/protobuf/test_messages_proto2.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nUexperimental/smurugesan/protobuf-3.6.0/src/google/protobuf/test_messages_proto2.proto\x12\x1dprotobuf_test_messages.proto2\"\xde\x32\n\x12TestAllTypesProto2\x12\x16\n\x0eoptional_int32\x18\x01 \x01(\x05\x12\x16\n\x0eoptional_int64\x18\x02 \x01(\x03\x12\x17\n\x0foptional_uint32\x18\x03 \x01(\r\x12\x17\n\x0foptional_uint64\x18\x04 \x01(\x04\x12\x17\n\x0foptional_sint32\x18\x05 \x01(\x11\x12\x17\n\x0foptional_sint64\x18\x06 \x01(\x12\x12\x18\n\x10optional_fixed32\x18\x07 \x01(\x07\x12\x18\n\x10optional_fixed64\x18\x08 \x01(\x06\x12\x19\n\x11optional_sfixed32\x18\t \x01(\x0f\x12\x19\n\x11optional_sfixed64\x18\n \x01(\x10\x12\x16\n\x0eoptional_float\x18\x0b \x01(\x02\x12\x17\n\x0foptional_double\x18\x0c \x01(\x01\x12\x15\n\roptional_bool\x18\r \x01(\x08\x12\x17\n\x0foptional_string\x18\x0e \x01(\t\x12\x16\n\x0eoptional_bytes\x18\x0f \x01(\x0c\x12`\n\x17optional_nested_message\x18\x12 \x01(\x0b\x32?.protobuf_test_messages.proto2.TestAllTypesProto2.NestedMessage\x12U\n\x18optional_foreign_message\x18\x13 \x01(\x0b\x32\x33.protobuf_test_messages.proto2.ForeignMessageProto2\x12Z\n\x14optional_nested_enum\x18\x15 \x01(\x0e\x32<.protobuf_test_messages.proto2.TestAllTypesProto2.NestedEnum\x12O\n\x15optional_foreign_enum\x18\x16 \x01(\x0e\x32\x30.protobuf_test_messages.proto2.ForeignEnumProto2\x12!\n\x15optional_string_piece\x18\x18 \x01(\tB\x02\x08\x02\x12\x19\n\roptional_cord\x18\x19 \x01(\tB\x02\x08\x01\x12L\n\x11recursive_message\x18\x1b \x01(\x0b\x32\x31.protobuf_test_messages.proto2.TestAllTypesProto2\x12\x16\n\x0erepeated_int32\x18\x1f \x03(\x05\x12\x16\n\x0erepeated_int64\x18  \x03(\x03\x12\x17\n\x0frepeated_uint32\x18! \x03(\r\x12\x17\n\x0frepeated_uint64\x18\" \x03(\x04\x12\x17\n\x0frepeated_sint32\x18# \x03(\x11\x12\x17\n\x0frepeated_sint64\x18$ \x03(\x12\x12\x18\n\x10repeated_fixed32\x18% \x03(\x07\x12\x18\n\x10repeated_fixed64\x18& \x03(\x06\x12\x19\n\x11repeated_sfixed32\x18\' \x03(\x0f\x12\x19\n\x11repeated_sfixed64\x18( \x03(\x10\x12\x16\n\x0erepeated_float\x18) \x03(\x02\x12\x17\n\x0frepeated_double\x18* \x03(\x01\x12\x15\n\rrepeated_bool\x18+ \x03(\x08\x12\x17\n\x0frepeated_string\x18, \x03(\t\x12\x16\n\x0erepeated_bytes\x18- \x03(\x0c\x12`\n\x17repeated_nested_message\x18\x30 \x03(\x0b\x32?.protobuf_test_messages.proto2.TestAllTypesProto2.NestedMessage\x12U\n\x18repeated_foreign_message\x18\x31 \x03(\x0b\x32\x33.protobuf_test_messages.proto2.ForeignMessageProto2\x12Z\n\x14repeated_nested_enum\x18\x33 \x03(\x0e\x32<.protobuf_test_messages.proto2.TestAllTypesProto2.NestedEnum\x12O\n\x15repeated_foreign_enum\x18\x34 \x03(\x0e\x32\x30.protobuf_test_messages.proto2.ForeignEnumProto2\x12!\n\x15repeated_string_piece\x18\x36 \x03(\tB\x02\x08\x02\x12\x19\n\rrepeated_cord\x18\x37 \x03(\tB\x02\x08\x01\x12]\n\x0fmap_int32_int32\x18\x38 \x03(\x0b\x32\x44.protobuf_test_messages.proto2.TestAllTypesProto2.MapInt32Int32Entry\x12]\n\x0fmap_int64_int64\x18\x39 \x03(\x0b\x32\x44.protobuf_test_messages.proto2.TestAllTypesProto2.MapInt64Int64Entry\x12\x61\n\x11map_uint32_uint32\x18: \x03(\x0b\x32\x46.protobuf_test_messages.proto2.TestAllTypesProto2.MapUint32Uint32Entry\x12\x61\n\x11map_uint64_uint64\x18; \x03(\x0b\x32\x46.protobuf_test_messages.proto2.TestAllTypesProto2.MapUint64Uint64Entry\x12\x61\n\x11map_sint32_sint32\x18< \x03(\x0b\x32\x46.protobuf_test_messages.proto2.TestAllTypesProto2.MapSint32Sint32Entry\x12\x61\n\x11map_sint64_sint64\x18= \x03(\x0b\x32\x46.protobuf_test_messages.proto2.TestAllTypesProto2.MapSint64Sint64Entry\x12\x65\n\x13map_fixed32_fixed32\x18> \x03(\x0b\x32H.protobuf_test_messages.proto2.TestAllTypesProto2.MapFixed32Fixed32Entry\x12\x65\n\x13map_fixed64_fixed64\x18? \x03(\x0b\x32H.protobuf_test_messages.proto2.TestAllTypesProto2.MapFixed64Fixed64Entry\x12i\n\x15map_sfixed32_sfixed32\x18@ \x03(\x0b\x32J.protobuf_test_messages.proto2.TestAllTypesProto2.MapSfixed32Sfixed32Entry\x12i\n\x15map_sfixed64_sfixed64\x18\x41 \x03(\x0b\x32J.protobuf_test_messages.proto2.TestAllTypesProto2.MapSfixed64Sfixed64Entry\x12]\n\x0fmap_int32_float\x18\x42 \x03(\x0b\x32\x44.protobuf_test_messages.proto2.TestAllTypesProto2.MapInt32FloatEntry\x12_\n\x10map_int32_double\x18\x43 \x03(\x0b\x32\x45.protobuf_test_messages.proto2.TestAllTypesProto2.MapInt32DoubleEntry\x12Y\n\rmap_bool_bool\x18\x44 \x03(\x0b\x32\x42.protobuf_test_messages.proto2.TestAllTypesProto2.MapBoolBoolEntry\x12\x61\n\x11map_string_string\x18\x45 \x03(\x0b\x32\x46.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringStringEntry\x12_\n\x10map_string_bytes\x18\x46 \x03(\x0b\x32\x45.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringBytesEntry\x12p\n\x19map_string_nested_message\x18G \x03(\x0b\x32M.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringNestedMessageEntry\x12r\n\x1amap_string_foreign_message\x18H \x03(\x0b\x32N.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringForeignMessageEntry\x12j\n\x16map_string_nested_enum\x18I \x03(\x0b\x32J.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringNestedEnumEntry\x12l\n\x17map_string_foreign_enum\x18J \x03(\x0b\x32K.protobuf_test_messages.proto2.TestAllTypesProto2.MapStringForeignEnumEntry\x12\x16\n\x0coneof_uint32\x18o \x01(\rH\x00\x12_\n\x14oneof_nested_message\x18p \x01(\x0b\x32?.protobuf_test_messages.proto2.TestAllTypesProto2.NestedMessageH\x00\x12\x16\n\x0coneof_string\x18q \x01(\tH\x00\x12\x15\n\x0boneof_bytes\x18r \x01(\x0cH\x00\x12\x14\n\noneof_bool\x18s \x01(\x08H\x00\x12\x16\n\x0coneof_uint64\x18t \x01(\x04H\x00\x12\x15\n\x0boneof_float\x18u \x01(\x02H\x00\x12\x16\n\x0coneof_double\x18v \x01(\x01H\x00\x12R\n\noneof_enum\x18w \x01(\x0e\x32<.protobuf_test_messages.proto2.TestAllTypesProto2.NestedEnumH\x00\x12\x45\n\x04\x64\x61ta\x18\xc9\x01 \x01(\n26.protobuf_test_messages.proto2.TestAllTypesProto2.Data\x12\x13\n\nfieldname1\x18\x91\x03 \x01(\x05\x12\x14\n\x0b\x66ield_name2\x18\x92\x03 \x01(\x05\x12\x15\n\x0c_field_name3\x18\x93\x03 \x01(\x05\x12\x16\n\rfield__name4_\x18\x94\x03 \x01(\x05\x12\x14\n\x0b\x66ield0name5\x18\x95\x03 \x01(\x05\x12\x16\n\rfield_0_name6\x18\x96\x03 \x01(\x05\x12\x13\n\nfieldName7\x18\x97\x03 \x01(\x05\x12\x13\n\nFieldName8\x18\x98\x03 \x01(\x05\x12\x14\n\x0b\x66ield_Name9\x18\x99\x03 \x01(\x05\x12\x15\n\x0c\x46ield_Name10\x18\x9a\x03 \x01(\x05\x12\x15\n\x0c\x46IELD_NAME11\x18\x9b\x03 \x01(\x05\x12\x15\n\x0c\x46IELD_name12\x18\x9c\x03 \x01(\x05\x12\x17\n\x0e__field_name13\x18\x9d\x03 \x01(\x05\x12\x17\n\x0e__Field_name14\x18\x9e\x03 \x01(\x05\x12\x16\n\rfield__name15\x18\x9f\x03 \x01(\x05\x12\x16\n\rfield__Name16\x18\xa0\x03 \x01(\x05\x12\x17\n\x0e\x66ield_name17__\x18\xa1\x03 \x01(\x05\x12\x17\n\x0e\x46ield_name18__\x18\xa2\x03 \x01(\x05\x1a\x62\n\rNestedMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x46\n\x0b\x63orecursive\x18\x02 \x01(\x0b\x32\x31.protobuf_test_messages.proto2.TestAllTypesProto2\x1a\x34\n\x12MapInt32Int32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x34\n\x12MapInt64Int64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x36\n\x14MapUint32Uint32Entry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14MapUint64Uint64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x36\n\x14MapSint32Sint32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11:\x02\x38\x01\x1a\x36\n\x14MapSint64Sint64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x38\n\x16MapFixed32Fixed32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x07:\x02\x38\x01\x1a\x38\n\x16MapFixed64Fixed64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x06:\x02\x38\x01\x1a:\n\x18MapSfixed32Sfixed32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\r\n\x05value\x18\x02 \x01(\x0f:\x02\x38\x01\x1a:\n\x18MapSfixed64Sfixed64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\r\n\x05value\x18\x02 \x01(\x10:\x02\x38\x01\x1a\x34\n\x12MapInt32FloatEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x35\n\x13MapInt32DoubleEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x32\n\x10MapBoolBoolEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x36\n\x14MapStringStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13MapStringBytesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a~\n\x1bMapStringNestedMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.protobuf_test_messages.proto2.TestAllTypesProto2.NestedMessage:\x02\x38\x01\x1as\n\x1cMapStringForeignMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.protobuf_test_messages.proto2.ForeignMessageProto2:\x02\x38\x01\x1ax\n\x18MapStringNestedEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12K\n\x05value\x18\x02 \x01(\x0e\x32<.protobuf_test_messages.proto2.TestAllTypesProto2.NestedEnum:\x02\x38\x01\x1am\n\x19MapStringForeignEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0e\x32\x30.protobuf_test_messages.proto2.ForeignEnumProto2:\x02\x38\x01\x1a\x33\n\x04\x44\x61ta\x12\x14\n\x0bgroup_int32\x18\xca\x01 \x01(\x05\x12\x15\n\x0cgroup_uint32\x18\xcb\x01 \x01(\r\x1a!\n\x11MessageSetCorrect*\x08\x08\x04\x10\xff\xff\xff\xff\x07:\x02\x08\x01\x1a\xe0\x01\n\x1bMessageSetCorrectExtension1\x12\x0b\n\x03str\x18\x19 \x01(\t2\xb3\x01\n\x15message_set_extension\x12\x43.protobuf_test_messages.proto2.TestAllTypesProto2.MessageSetCorrect\x18\xf9\xbb^ \x01(\x0b\x32M.protobuf_test_messages.proto2.TestAllTypesProto2.MessageSetCorrectExtension1\x1a\xdf\x01\n\x1bMessageSetCorrectExtension2\x12\t\n\x01i\x18\t \x01(\x05\x32\xb4\x01\n\x15message_set_extension\x12\x43.protobuf_test_messages.proto2.TestAllTypesProto2.MessageSetCorrect\x18\x90\xb3\xfc\x01 \x01(\x0b\x32M.protobuf_test_messages.proto2.TestAllTypesProto2.MessageSetCorrectExtension2\"9\n\nNestedEnum\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\x12\x10\n\x03NEG\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\x05\x08x\x10\xc9\x01\x42\r\n\x0boneof_field\"!\n\x14\x46oreignMessageProto2\x12\t\n\x01\x63\x18\x01 \x01(\x05*F\n\x11\x46oreignEnumProto2\x12\x0f\n\x0b\x46OREIGN_FOO\x10\x00\x12\x0f\n\x0b\x46OREIGN_BAR\x10\x01\x12\x0f\n\x0b\x46OREIGN_BAZ\x10\x02:J\n\x0f\x65xtension_int32\x12\x31.protobuf_test_messages.proto2.TestAllTypesProto2\x18x \x01(\x05\x42/\n(com.google.protobuf_test_messages.proto2H\x01\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.src.google.protobuf.test_messages_proto2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.protobuf_test_messages.proto2H\001\370\001\001'
  _globals['_TESTALLTYPESPROTO2_MAPINT32INT32ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPINT32INT32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPINT64INT64ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPINT64INT64ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPUINT32UINT32ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPUINT32UINT32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPUINT64UINT64ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPUINT64UINT64ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSINT32SINT32ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSINT32SINT32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSINT64SINT64ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSINT64SINT64ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPFIXED32FIXED32ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPFIXED32FIXED32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPFIXED64FIXED64ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPFIXED64FIXED64ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED32SFIXED32ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED32SFIXED32ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED64SFIXED64ENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED64SFIXED64ENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPINT32FLOATENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPINT32FLOATENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPINT32DOUBLEENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPINT32DOUBLEENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPBOOLBOOLENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPBOOLBOOLENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGSTRINGENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGSTRINGENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGBYTESENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGBYTESENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDMESSAGEENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDMESSAGEENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNMESSAGEENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNMESSAGEENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDENUMENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDENUMENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNENUMENTRY']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNENUMENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECT']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECT']._serialized_options = b'\010\001'
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['optional_string_piece']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['optional_string_piece']._serialized_options = b'\010\002'
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['optional_cord']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['optional_cord']._serialized_options = b'\010\001'
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['repeated_string_piece']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['repeated_string_piece']._serialized_options = b'\010\002'
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['repeated_cord']._loaded_options = None
  _globals['_TESTALLTYPESPROTO2'].fields_by_name['repeated_cord']._serialized_options = b'\010\001'
  _globals['_FOREIGNENUMPROTO2']._serialized_start=6652
  _globals['_FOREIGNENUMPROTO2']._serialized_end=6722
  _globals['_TESTALLTYPESPROTO2']._serialized_start=121
  _globals['_TESTALLTYPESPROTO2']._serialized_end=6615
  _globals['_TESTALLTYPESPROTO2_NESTEDMESSAGE']._serialized_start=4577
  _globals['_TESTALLTYPESPROTO2_NESTEDMESSAGE']._serialized_end=4675
  _globals['_TESTALLTYPESPROTO2_MAPINT32INT32ENTRY']._serialized_start=4677
  _globals['_TESTALLTYPESPROTO2_MAPINT32INT32ENTRY']._serialized_end=4729
  _globals['_TESTALLTYPESPROTO2_MAPINT64INT64ENTRY']._serialized_start=4731
  _globals['_TESTALLTYPESPROTO2_MAPINT64INT64ENTRY']._serialized_end=4783
  _globals['_TESTALLTYPESPROTO2_MAPUINT32UINT32ENTRY']._serialized_start=4785
  _globals['_TESTALLTYPESPROTO2_MAPUINT32UINT32ENTRY']._serialized_end=4839
  _globals['_TESTALLTYPESPROTO2_MAPUINT64UINT64ENTRY']._serialized_start=4841
  _globals['_TESTALLTYPESPROTO2_MAPUINT64UINT64ENTRY']._serialized_end=4895
  _globals['_TESTALLTYPESPROTO2_MAPSINT32SINT32ENTRY']._serialized_start=4897
  _globals['_TESTALLTYPESPROTO2_MAPSINT32SINT32ENTRY']._serialized_end=4951
  _globals['_TESTALLTYPESPROTO2_MAPSINT64SINT64ENTRY']._serialized_start=4953
  _globals['_TESTALLTYPESPROTO2_MAPSINT64SINT64ENTRY']._serialized_end=5007
  _globals['_TESTALLTYPESPROTO2_MAPFIXED32FIXED32ENTRY']._serialized_start=5009
  _globals['_TESTALLTYPESPROTO2_MAPFIXED32FIXED32ENTRY']._serialized_end=5065
  _globals['_TESTALLTYPESPROTO2_MAPFIXED64FIXED64ENTRY']._serialized_start=5067
  _globals['_TESTALLTYPESPROTO2_MAPFIXED64FIXED64ENTRY']._serialized_end=5123
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED32SFIXED32ENTRY']._serialized_start=5125
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED32SFIXED32ENTRY']._serialized_end=5183
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED64SFIXED64ENTRY']._serialized_start=5185
  _globals['_TESTALLTYPESPROTO2_MAPSFIXED64SFIXED64ENTRY']._serialized_end=5243
  _globals['_TESTALLTYPESPROTO2_MAPINT32FLOATENTRY']._serialized_start=5245
  _globals['_TESTALLTYPESPROTO2_MAPINT32FLOATENTRY']._serialized_end=5297
  _globals['_TESTALLTYPESPROTO2_MAPINT32DOUBLEENTRY']._serialized_start=5299
  _globals['_TESTALLTYPESPROTO2_MAPINT32DOUBLEENTRY']._serialized_end=5352
  _globals['_TESTALLTYPESPROTO2_MAPBOOLBOOLENTRY']._serialized_start=5354
  _globals['_TESTALLTYPESPROTO2_MAPBOOLBOOLENTRY']._serialized_end=5404
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGSTRINGENTRY']._serialized_start=5406
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGSTRINGENTRY']._serialized_end=5460
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGBYTESENTRY']._serialized_start=5462
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGBYTESENTRY']._serialized_end=5515
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDMESSAGEENTRY']._serialized_start=5517
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDMESSAGEENTRY']._serialized_end=5643
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNMESSAGEENTRY']._serialized_start=5645
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNMESSAGEENTRY']._serialized_end=5760
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDENUMENTRY']._serialized_start=5762
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGNESTEDENUMENTRY']._serialized_end=5882
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNENUMENTRY']._serialized_start=5884
  _globals['_TESTALLTYPESPROTO2_MAPSTRINGFOREIGNENUMENTRY']._serialized_end=5993
  _globals['_TESTALLTYPESPROTO2_DATA']._serialized_start=5995
  _globals['_TESTALLTYPESPROTO2_DATA']._serialized_end=6046
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECT']._serialized_start=6048
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECT']._serialized_end=6081
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECTEXTENSION1']._serialized_start=6084
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECTEXTENSION1']._serialized_end=6308
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECTEXTENSION2']._serialized_start=6311
  _globals['_TESTALLTYPESPROTO2_MESSAGESETCORRECTEXTENSION2']._serialized_end=6534
  _globals['_TESTALLTYPESPROTO2_NESTEDENUM']._serialized_start=6536
  _globals['_TESTALLTYPESPROTO2_NESTEDENUM']._serialized_end=6593
  _globals['_FOREIGNMESSAGEPROTO2']._serialized_start=6617
  _globals['_FOREIGNMESSAGEPROTO2']._serialized_end=6650
# @@protoc_insertion_point(module_scope)
