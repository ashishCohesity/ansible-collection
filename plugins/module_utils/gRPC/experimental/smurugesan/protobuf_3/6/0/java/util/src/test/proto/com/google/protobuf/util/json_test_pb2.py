# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/java/util/src/test/proto/com/google/protobuf/util/json_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nhexperimental/smurugesan/protobuf-3.6.0/java/util/src/test/proto/com/google/protobuf/util/json_test.proto\x12\tjson_test\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd9\x08\n\x0cTestAllTypes\x12\x16\n\x0eoptional_int32\x18\x01 \x01(\x05\x12\x16\n\x0eoptional_int64\x18\x02 \x01(\x03\x12\x17\n\x0foptional_uint32\x18\x03 \x01(\r\x12\x17\n\x0foptional_uint64\x18\x04 \x01(\x04\x12\x17\n\x0foptional_sint32\x18\x05 \x01(\x11\x12\x17\n\x0foptional_sint64\x18\x06 \x01(\x12\x12\x18\n\x10optional_fixed32\x18\x07 \x01(\x07\x12\x18\n\x10optional_fixed64\x18\x08 \x01(\x06\x12\x19\n\x11optional_sfixed32\x18\t \x01(\x0f\x12\x19\n\x11optional_sfixed64\x18\n \x01(\x10\x12\x16\n\x0eoptional_float\x18\x0b \x01(\x02\x12\x17\n\x0foptional_double\x18\x0c \x01(\x01\x12\x15\n\roptional_bool\x18\r \x01(\x08\x12\x17\n\x0foptional_string\x18\x0e \x01(\t\x12\x16\n\x0eoptional_bytes\x18\x0f \x01(\x0c\x12\x46\n\x17optional_nested_message\x18\x12 \x01(\x0b\x32%.json_test.TestAllTypes.NestedMessage\x12@\n\x14optional_nested_enum\x18\x15 \x01(\x0e\x32\".json_test.TestAllTypes.NestedEnum\x12\x16\n\x0erepeated_int32\x18\x1f \x03(\x05\x12\x16\n\x0erepeated_int64\x18  \x03(\x03\x12\x17\n\x0frepeated_uint32\x18! \x03(\r\x12\x17\n\x0frepeated_uint64\x18\" \x03(\x04\x12\x17\n\x0frepeated_sint32\x18# \x03(\x11\x12\x17\n\x0frepeated_sint64\x18$ \x03(\x12\x12\x18\n\x10repeated_fixed32\x18% \x03(\x07\x12\x18\n\x10repeated_fixed64\x18& \x03(\x06\x12\x19\n\x11repeated_sfixed32\x18\' \x03(\x0f\x12\x19\n\x11repeated_sfixed64\x18( \x03(\x10\x12\x16\n\x0erepeated_float\x18) \x03(\x02\x12\x17\n\x0frepeated_double\x18* \x03(\x01\x12\x15\n\rrepeated_bool\x18+ \x03(\x08\x12\x17\n\x0frepeated_string\x18, \x03(\t\x12\x16\n\x0erepeated_bytes\x18- \x03(\x0c\x12\x46\n\x17repeated_nested_message\x18\x30 \x03(\x0b\x32%.json_test.TestAllTypes.NestedMessage\x12@\n\x14repeated_nested_enum\x18\x33 \x03(\x0e\x32\".json_test.TestAllTypes.NestedEnum\x1a\x1e\n\rNestedMessage\x12\r\n\x05value\x18\x01 \x01(\x05\"\'\n\nNestedEnum\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\"\xb0\x01\n\tTestOneof\x12\x15\n\x0boneof_int32\x18\x01 \x01(\x05H\x00\x12\x45\n\x14oneof_nested_message\x18\x02 \x01(\x0b\x32%.json_test.TestAllTypes.NestedMessageH\x00\x12\x36\n\x10oneof_null_value\x18\x03 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x42\r\n\x0boneof_field\"\xda\x1c\n\x07TestMap\x12\x43\n\x12int32_to_int32_map\x18\x01 \x03(\x0b\x32\'.json_test.TestMap.Int32ToInt32MapEntry\x12\x43\n\x12int64_to_int32_map\x18\x02 \x03(\x0b\x32\'.json_test.TestMap.Int64ToInt32MapEntry\x12\x45\n\x13uint32_to_int32_map\x18\x03 \x03(\x0b\x32(.json_test.TestMap.Uint32ToInt32MapEntry\x12\x45\n\x13uint64_to_int32_map\x18\x04 \x03(\x0b\x32(.json_test.TestMap.Uint64ToInt32MapEntry\x12\x45\n\x13sint32_to_int32_map\x18\x05 \x03(\x0b\x32(.json_test.TestMap.Sint32ToInt32MapEntry\x12\x45\n\x13sint64_to_int32_map\x18\x06 \x03(\x0b\x32(.json_test.TestMap.Sint64ToInt32MapEntry\x12G\n\x14\x66ixed32_to_int32_map\x18\x07 \x03(\x0b\x32).json_test.TestMap.Fixed32ToInt32MapEntry\x12G\n\x14\x66ixed64_to_int32_map\x18\x08 \x03(\x0b\x32).json_test.TestMap.Fixed64ToInt32MapEntry\x12I\n\x15sfixed32_to_int32_map\x18\t \x03(\x0b\x32*.json_test.TestMap.Sfixed32ToInt32MapEntry\x12I\n\x15sfixed64_to_int32_map\x18\n \x03(\x0b\x32*.json_test.TestMap.Sfixed64ToInt32MapEntry\x12\x41\n\x11\x62ool_to_int32_map\x18\x0b \x03(\x0b\x32&.json_test.TestMap.BoolToInt32MapEntry\x12\x45\n\x13string_to_int32_map\x18\x0c \x03(\x0b\x32(.json_test.TestMap.StringToInt32MapEntry\x12\x43\n\x12int32_to_int64_map\x18\x65 \x03(\x0b\x32\'.json_test.TestMap.Int32ToInt64MapEntry\x12\x45\n\x13int32_to_uint32_map\x18\x66 \x03(\x0b\x32(.json_test.TestMap.Int32ToUint32MapEntry\x12\x45\n\x13int32_to_uint64_map\x18g \x03(\x0b\x32(.json_test.TestMap.Int32ToUint64MapEntry\x12\x45\n\x13int32_to_sint32_map\x18h \x03(\x0b\x32(.json_test.TestMap.Int32ToSint32MapEntry\x12\x45\n\x13int32_to_sint64_map\x18i \x03(\x0b\x32(.json_test.TestMap.Int32ToSint64MapEntry\x12G\n\x14int32_to_fixed32_map\x18j \x03(\x0b\x32).json_test.TestMap.Int32ToFixed32MapEntry\x12G\n\x14int32_to_fixed64_map\x18k \x03(\x0b\x32).json_test.TestMap.Int32ToFixed64MapEntry\x12I\n\x15int32_to_sfixed32_map\x18l \x03(\x0b\x32*.json_test.TestMap.Int32ToSfixed32MapEntry\x12I\n\x15int32_to_sfixed64_map\x18m \x03(\x0b\x32*.json_test.TestMap.Int32ToSfixed64MapEntry\x12\x43\n\x12int32_to_float_map\x18n \x03(\x0b\x32\'.json_test.TestMap.Int32ToFloatMapEntry\x12\x45\n\x13int32_to_double_map\x18o \x03(\x0b\x32(.json_test.TestMap.Int32ToDoubleMapEntry\x12\x41\n\x11int32_to_bool_map\x18p \x03(\x0b\x32&.json_test.TestMap.Int32ToBoolMapEntry\x12\x45\n\x13int32_to_string_map\x18q \x03(\x0b\x32(.json_test.TestMap.Int32ToStringMapEntry\x12\x43\n\x12int32_to_bytes_map\x18r \x03(\x0b\x32\'.json_test.TestMap.Int32ToBytesMapEntry\x12G\n\x14int32_to_message_map\x18s \x03(\x0b\x32).json_test.TestMap.Int32ToMessageMapEntry\x12\x41\n\x11int32_to_enum_map\x18t \x03(\x0b\x32&.json_test.TestMap.Int32ToEnumMapEntry\x1a\x36\n\x14Int32ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14Int64ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Uint32ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Uint64ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Sint32ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Sint64ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16\x46ixed32ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16\x46ixed64ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17Sfixed32ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17Sfixed64ToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x35\n\x13\x42oolToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15StringToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14Int32ToInt64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x37\n\x15Int32ToUint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x37\n\x15Int32ToUint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x37\n\x15Int32ToSint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11:\x02\x38\x01\x1a\x37\n\x15Int32ToSint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x38\n\x16Int32ToFixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x07:\x02\x38\x01\x1a\x38\n\x16Int32ToFixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x06:\x02\x38\x01\x1a\x39\n\x17Int32ToSfixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0f:\x02\x38\x01\x1a\x39\n\x17Int32ToSfixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x10:\x02\x38\x01\x1a\x36\n\x14Int32ToFloatMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x37\n\x15Int32ToDoubleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x35\n\x13Int32ToBoolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x37\n\x15Int32ToStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14Int32ToBytesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a_\n\x16Int32ToMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.json_test.TestAllTypes.NestedMessage:\x02\x38\x01\x1aY\n\x13Int32ToEnumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x31\n\x05value\x18\x02 \x01(\x0e\x32\".json_test.TestAllTypes.NestedEnum:\x02\x38\x01\"\xd6\x03\n\x0cTestWrappers\x12\x30\n\x0bint32_value\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\x0cuint32_value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x30\n\x0bint64_value\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0cuint64_value\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\x0b\x66loat_value\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\x0c\x64ouble_value\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\nbool_value\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0cstring_value\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0b\x62ytes_value\x18\t \x01(\x0b\x32\x1b.google.protobuf.BytesValue\"D\n\rTestTimestamp\x12\x33\n\x0ftimestamp_value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"A\n\x0cTestDuration\x12\x31\n\x0e\x64uration_value\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"E\n\rTestFieldMask\x12\x34\n\x10\x66ield_mask_value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x92\x01\n\nTestStruct\x12-\n\x0cstruct_value\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12.\n\nlist_value\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\"\xa8\x01\n\x07TestAny\x12\'\n\tany_value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12/\n\x07\x61ny_map\x18\x02 \x03(\x0b\x32\x1e.json_test.TestAny.AnyMapEntry\x1a\x43\n\x0b\x41nyMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"+\n\x12TestCustomJsonName\x12\x15\n\x05value\x18\x01 \x01(\x05R\x06@value\"H\n\rTestRecursive\x12\r\n\x05value\x18\x01 \x01(\x05\x12(\n\x06nested\x18\x02 \x01(\x0b\x32\x18.json_test.TestRecursiveB)\n\x18\x63om.google.protobuf.utilB\rJsonTestProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.java.util.src.test.proto.com.google.protobuf.util.json_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.google.protobuf.utilB\rJsonTestProto'
  _globals['_TESTMAP_INT32TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT64TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT64TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_UINT32TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_UINT32TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_UINT64TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_UINT64TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_SINT32TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_SINT32TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_SINT64TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_SINT64TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_FIXED32TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_FIXED32TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_FIXED64TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_FIXED64TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_SFIXED32TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_SFIXED32TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_SFIXED64TOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_SFIXED64TOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_BOOLTOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_BOOLTOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_STRINGTOINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_STRINGTOINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOINT64MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOINT64MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOUINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOUINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOUINT64MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOUINT64MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSINT32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSINT32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSINT64MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSINT64MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOFIXED32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOFIXED32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOFIXED64MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOFIXED64MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSFIXED32MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSFIXED32MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSFIXED64MAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSFIXED64MAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOFLOATMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOFLOATMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TODOUBLEMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TODOUBLEMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOBOOLMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOBOOLMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSTRINGMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSTRINGMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOBYTESMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOBYTESMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOMESSAGEMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOMESSAGEMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOENUMMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOENUMMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTANY_ANYMAPENTRY']._loaded_options = None
  _globals['_TESTANY_ANYMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTALLTYPES']._serialized_start=308
  _globals['_TESTALLTYPES']._serialized_end=1421
  _globals['_TESTALLTYPES_NESTEDMESSAGE']._serialized_start=1350
  _globals['_TESTALLTYPES_NESTEDMESSAGE']._serialized_end=1380
  _globals['_TESTALLTYPES_NESTEDENUM']._serialized_start=1382
  _globals['_TESTALLTYPES_NESTEDENUM']._serialized_end=1421
  _globals['_TESTONEOF']._serialized_start=1424
  _globals['_TESTONEOF']._serialized_end=1600
  _globals['_TESTMAP']._serialized_start=1603
  _globals['_TESTMAP']._serialized_end=5277
  _globals['_TESTMAP_INT32TOINT32MAPENTRY']._serialized_start=3606
  _globals['_TESTMAP_INT32TOINT32MAPENTRY']._serialized_end=3660
  _globals['_TESTMAP_INT64TOINT32MAPENTRY']._serialized_start=3662
  _globals['_TESTMAP_INT64TOINT32MAPENTRY']._serialized_end=3716
  _globals['_TESTMAP_UINT32TOINT32MAPENTRY']._serialized_start=3718
  _globals['_TESTMAP_UINT32TOINT32MAPENTRY']._serialized_end=3773
  _globals['_TESTMAP_UINT64TOINT32MAPENTRY']._serialized_start=3775
  _globals['_TESTMAP_UINT64TOINT32MAPENTRY']._serialized_end=3830
  _globals['_TESTMAP_SINT32TOINT32MAPENTRY']._serialized_start=3832
  _globals['_TESTMAP_SINT32TOINT32MAPENTRY']._serialized_end=3887
  _globals['_TESTMAP_SINT64TOINT32MAPENTRY']._serialized_start=3889
  _globals['_TESTMAP_SINT64TOINT32MAPENTRY']._serialized_end=3944
  _globals['_TESTMAP_FIXED32TOINT32MAPENTRY']._serialized_start=3946
  _globals['_TESTMAP_FIXED32TOINT32MAPENTRY']._serialized_end=4002
  _globals['_TESTMAP_FIXED64TOINT32MAPENTRY']._serialized_start=4004
  _globals['_TESTMAP_FIXED64TOINT32MAPENTRY']._serialized_end=4060
  _globals['_TESTMAP_SFIXED32TOINT32MAPENTRY']._serialized_start=4062
  _globals['_TESTMAP_SFIXED32TOINT32MAPENTRY']._serialized_end=4119
  _globals['_TESTMAP_SFIXED64TOINT32MAPENTRY']._serialized_start=4121
  _globals['_TESTMAP_SFIXED64TOINT32MAPENTRY']._serialized_end=4178
  _globals['_TESTMAP_BOOLTOINT32MAPENTRY']._serialized_start=4180
  _globals['_TESTMAP_BOOLTOINT32MAPENTRY']._serialized_end=4233
  _globals['_TESTMAP_STRINGTOINT32MAPENTRY']._serialized_start=4235
  _globals['_TESTMAP_STRINGTOINT32MAPENTRY']._serialized_end=4290
  _globals['_TESTMAP_INT32TOINT64MAPENTRY']._serialized_start=4292
  _globals['_TESTMAP_INT32TOINT64MAPENTRY']._serialized_end=4346
  _globals['_TESTMAP_INT32TOUINT32MAPENTRY']._serialized_start=4348
  _globals['_TESTMAP_INT32TOUINT32MAPENTRY']._serialized_end=4403
  _globals['_TESTMAP_INT32TOUINT64MAPENTRY']._serialized_start=4405
  _globals['_TESTMAP_INT32TOUINT64MAPENTRY']._serialized_end=4460
  _globals['_TESTMAP_INT32TOSINT32MAPENTRY']._serialized_start=4462
  _globals['_TESTMAP_INT32TOSINT32MAPENTRY']._serialized_end=4517
  _globals['_TESTMAP_INT32TOSINT64MAPENTRY']._serialized_start=4519
  _globals['_TESTMAP_INT32TOSINT64MAPENTRY']._serialized_end=4574
  _globals['_TESTMAP_INT32TOFIXED32MAPENTRY']._serialized_start=4576
  _globals['_TESTMAP_INT32TOFIXED32MAPENTRY']._serialized_end=4632
  _globals['_TESTMAP_INT32TOFIXED64MAPENTRY']._serialized_start=4634
  _globals['_TESTMAP_INT32TOFIXED64MAPENTRY']._serialized_end=4690
  _globals['_TESTMAP_INT32TOSFIXED32MAPENTRY']._serialized_start=4692
  _globals['_TESTMAP_INT32TOSFIXED32MAPENTRY']._serialized_end=4749
  _globals['_TESTMAP_INT32TOSFIXED64MAPENTRY']._serialized_start=4751
  _globals['_TESTMAP_INT32TOSFIXED64MAPENTRY']._serialized_end=4808
  _globals['_TESTMAP_INT32TOFLOATMAPENTRY']._serialized_start=4810
  _globals['_TESTMAP_INT32TOFLOATMAPENTRY']._serialized_end=4864
  _globals['_TESTMAP_INT32TODOUBLEMAPENTRY']._serialized_start=4866
  _globals['_TESTMAP_INT32TODOUBLEMAPENTRY']._serialized_end=4921
  _globals['_TESTMAP_INT32TOBOOLMAPENTRY']._serialized_start=4923
  _globals['_TESTMAP_INT32TOBOOLMAPENTRY']._serialized_end=4976
  _globals['_TESTMAP_INT32TOSTRINGMAPENTRY']._serialized_start=4978
  _globals['_TESTMAP_INT32TOSTRINGMAPENTRY']._serialized_end=5033
  _globals['_TESTMAP_INT32TOBYTESMAPENTRY']._serialized_start=5035
  _globals['_TESTMAP_INT32TOBYTESMAPENTRY']._serialized_end=5089
  _globals['_TESTMAP_INT32TOMESSAGEMAPENTRY']._serialized_start=5091
  _globals['_TESTMAP_INT32TOMESSAGEMAPENTRY']._serialized_end=5186
  _globals['_TESTMAP_INT32TOENUMMAPENTRY']._serialized_start=5188
  _globals['_TESTMAP_INT32TOENUMMAPENTRY']._serialized_end=5277
  _globals['_TESTWRAPPERS']._serialized_start=5280
  _globals['_TESTWRAPPERS']._serialized_end=5750
  _globals['_TESTTIMESTAMP']._serialized_start=5752
  _globals['_TESTTIMESTAMP']._serialized_end=5820
  _globals['_TESTDURATION']._serialized_start=5822
  _globals['_TESTDURATION']._serialized_end=5887
  _globals['_TESTFIELDMASK']._serialized_start=5889
  _globals['_TESTFIELDMASK']._serialized_end=5958
  _globals['_TESTSTRUCT']._serialized_start=5961
  _globals['_TESTSTRUCT']._serialized_end=6107
  _globals['_TESTANY']._serialized_start=6110
  _globals['_TESTANY']._serialized_end=6278
  _globals['_TESTANY_ANYMAPENTRY']._serialized_start=6211
  _globals['_TESTANY_ANYMAPENTRY']._serialized_end=6278
  _globals['_TESTCUSTOMJSONNAME']._serialized_start=6280
  _globals['_TESTCUSTOMJSONNAME']._serialized_end=6323
  _globals['_TESTRECURSIVE']._serialized_start=6325
  _globals['_TESTRECURSIVE']._serialized_end=6397
# @@protoc_insertion_point(module_scope)