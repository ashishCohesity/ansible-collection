# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/java/core/src/test/proto/com/google/protobuf/map_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nbexperimental/smurugesan/protobuf-3.6.0/java/core/src/test/proto/com/google/protobuf/map_test.proto\x12\x08map_test\"\xb2\t\n\x07TestMap\x12\x46\n\x14int32_to_int32_field\x18\x01 \x03(\x0b\x32(.map_test.TestMap.Int32ToInt32FieldEntry\x12H\n\x15int32_to_string_field\x18\x02 \x03(\x0b\x32).map_test.TestMap.Int32ToStringFieldEntry\x12\x46\n\x14int32_to_bytes_field\x18\x03 \x03(\x0b\x32(.map_test.TestMap.Int32ToBytesFieldEntry\x12\x44\n\x13int32_to_enum_field\x18\x04 \x03(\x0b\x32\'.map_test.TestMap.Int32ToEnumFieldEntry\x12J\n\x16int32_to_message_field\x18\x05 \x03(\x0b\x32*.map_test.TestMap.Int32ToMessageFieldEntry\x12H\n\x15string_to_int32_field\x18\x06 \x03(\x0b\x32).map_test.TestMap.StringToInt32FieldEntry\x12H\n\x15uint32_to_int32_field\x18\x07 \x03(\x0b\x32).map_test.TestMap.Uint32ToInt32FieldEntry\x12\x46\n\x14int64_to_int32_field\x18\x08 \x03(\x0b\x32(.map_test.TestMap.Int64ToInt32FieldEntry\x1a\x1d\n\x0cMessageValue\x12\r\n\x05value\x18\x01 \x01(\x05\x1a\x38\n\x16Int32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17Int32ToStringFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16Int32ToBytesFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1aT\n\x15Int32ToEnumFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12*\n\x05value\x18\x02 \x01(\x0e\x32\x1b.map_test.TestMap.EnumValue:\x02\x38\x01\x1aZ\n\x18Int32ToMessageFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.map_test.TestMap.MessageValue:\x02\x38\x01\x1a\x39\n\x17StringToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17Uint32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16Int64ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"/\n\tEnumValue\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\x12\x07\n\x03QUX\x10\x03\"K\n\x1cTestOnChangeEventPropagation\x12+\n\x10optional_message\x18\x01 \x01(\x0b\x32\x11.map_test.TestMap\"\xcf\x06\n\x0e\x42izarroTestMap\x12M\n\x14int32_to_int32_field\x18\x01 \x03(\x0b\x32/.map_test.BizarroTestMap.Int32ToInt32FieldEntry\x12O\n\x15int32_to_string_field\x18\x02 \x03(\x0b\x32\x30.map_test.BizarroTestMap.Int32ToStringFieldEntry\x12M\n\x14int32_to_bytes_field\x18\x03 \x03(\x0b\x32/.map_test.BizarroTestMap.Int32ToBytesFieldEntry\x12K\n\x13int32_to_enum_field\x18\x04 \x03(\x0b\x32..map_test.BizarroTestMap.Int32ToEnumFieldEntry\x12Q\n\x16int32_to_message_field\x18\x05 \x03(\x0b\x32\x31.map_test.BizarroTestMap.Int32ToMessageFieldEntry\x12O\n\x15string_to_int32_field\x18\x06 \x03(\x0b\x32\x30.map_test.BizarroTestMap.StringToInt32FieldEntry\x1a\x38\n\x16Int32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x39\n\x17Int32ToStringFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16Int32ToBytesFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Int32ToEnumFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a:\n\x18Int32ToMessageFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x39\n\x17StringToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x87\x08\n\x12ReservedAsMapField\x12\x30\n\x02if\x18\x01 \x03(\x0b\x32$.map_test.ReservedAsMapField.IfEntry\x12\x36\n\x05\x63onst\x18\x02 \x03(\x0b\x32\'.map_test.ReservedAsMapField.ConstEntry\x12:\n\x07private\x18\x03 \x03(\x0b\x32).map_test.ReservedAsMapField.PrivateEntry\x12\x36\n\x05\x63lass\x18\x04 \x03(\x0b\x32\'.map_test.ReservedAsMapField.ClassEntry\x12\x32\n\x03int\x18\x05 \x03(\x0b\x32%.map_test.ReservedAsMapField.IntEntry\x12\x34\n\x04void\x18\x06 \x03(\x0b\x32&.map_test.ReservedAsMapField.VoidEntry\x12\x38\n\x06string\x18\x07 \x03(\x0b\x32(.map_test.ReservedAsMapField.StringEntry\x12:\n\x07package\x18\x08 \x03(\x0b\x32).map_test.ReservedAsMapField.PackageEntry\x12\x34\n\x04\x65num\x18\t \x03(\x0b\x32&.map_test.ReservedAsMapField.EnumEntry\x12\x34\n\x04null\x18\n \x03(\x0b\x32&.map_test.ReservedAsMapField.NullEntry\x1a)\n\x07IfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a,\n\nConstEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a.\n\x0cPrivateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a,\n\nClassEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a*\n\x08IntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tVoidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a-\n\x0bStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a.\n\x0cPackageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tNullEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xce\r\n\x1fReservedAsMapFieldWithEnumValue\x12=\n\x02if\x18\x01 \x03(\x0b\x32\x31.map_test.ReservedAsMapFieldWithEnumValue.IfEntry\x12\x43\n\x05\x63onst\x18\x02 \x03(\x0b\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.ConstEntry\x12G\n\x07private\x18\x03 \x03(\x0b\x32\x36.map_test.ReservedAsMapFieldWithEnumValue.PrivateEntry\x12\x43\n\x05\x63lass\x18\x04 \x03(\x0b\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.ClassEntry\x12?\n\x03int\x18\x05 \x03(\x0b\x32\x32.map_test.ReservedAsMapFieldWithEnumValue.IntEntry\x12\x41\n\x04void\x18\x06 \x03(\x0b\x32\x33.map_test.ReservedAsMapFieldWithEnumValue.VoidEntry\x12\x45\n\x06string\x18\x07 \x03(\x0b\x32\x35.map_test.ReservedAsMapFieldWithEnumValue.StringEntry\x12G\n\x07package\x18\x08 \x03(\x0b\x32\x36.map_test.ReservedAsMapFieldWithEnumValue.PackageEntry\x12\x41\n\x04\x65num\x18\t \x03(\x0b\x32\x33.map_test.ReservedAsMapFieldWithEnumValue.EnumEntry\x12\x41\n\x04null\x18\n \x03(\x0b\x32\x33.map_test.ReservedAsMapFieldWithEnumValue.NullEntry\x1a_\n\x07IfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x62\n\nConstEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x64\n\x0cPrivateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x62\n\nClassEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a`\n\x08IntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x61\n\tVoidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x63\n\x0bStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x64\n\x0cPackageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x61\n\tEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1a\x61\n\tNullEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.map_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\"\x1a\n\nSampleEnum\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x42\x18\n\x08map_testB\x0cMapTestProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.java.core.src.test.proto.com.google.protobuf.map_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\010map_testB\014MapTestProto'
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_UINT32TOINT32FIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_UINT32TOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP_INT64TOINT32FIELDENTRY']._loaded_options = None
  _globals['_TESTMAP_INT64TOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_options = b'8\001'
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._loaded_options = None
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._serialized_options = b'8\001'
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._loaded_options = None
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._serialized_options = b'8\001'
  _globals['_TESTMAP']._serialized_start=113
  _globals['_TESTMAP']._serialized_end=1315
  _globals['_TESTMAP_MESSAGEVALUE']._serialized_start=708
  _globals['_TESTMAP_MESSAGEVALUE']._serialized_end=737
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._serialized_start=739
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._serialized_end=795
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_start=797
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_end=854
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._serialized_start=856
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._serialized_end=912
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._serialized_start=914
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._serialized_end=998
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_start=1000
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_end=1090
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._serialized_start=1092
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._serialized_end=1149
  _globals['_TESTMAP_UINT32TOINT32FIELDENTRY']._serialized_start=1151
  _globals['_TESTMAP_UINT32TOINT32FIELDENTRY']._serialized_end=1208
  _globals['_TESTMAP_INT64TOINT32FIELDENTRY']._serialized_start=1210
  _globals['_TESTMAP_INT64TOINT32FIELDENTRY']._serialized_end=1266
  _globals['_TESTMAP_ENUMVALUE']._serialized_start=1268
  _globals['_TESTMAP_ENUMVALUE']._serialized_end=1315
  _globals['_TESTONCHANGEEVENTPROPAGATION']._serialized_start=1317
  _globals['_TESTONCHANGEEVENTPROPAGATION']._serialized_end=1392
  _globals['_BIZARROTESTMAP']._serialized_start=1395
  _globals['_BIZARROTESTMAP']._serialized_end=2242
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._serialized_start=1893
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._serialized_end=1949
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_start=1951
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_end=2008
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._serialized_start=2010
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._serialized_end=2066
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._serialized_start=2068
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._serialized_end=2123
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_start=2125
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_end=2183
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._serialized_start=2185
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._serialized_end=2242
  _globals['_RESERVEDASMAPFIELD']._serialized_start=2245
  _globals['_RESERVEDASMAPFIELD']._serialized_end=3276
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._serialized_start=2821
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._serialized_end=2862
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._serialized_start=2864
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._serialized_end=2908
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._serialized_start=2910
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._serialized_end=2956
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._serialized_start=2958
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._serialized_end=3002
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._serialized_start=3004
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._serialized_end=3046
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._serialized_start=3048
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._serialized_end=3091
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._serialized_start=3093
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._serialized_end=3138
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._serialized_start=3140
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._serialized_end=3186
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._serialized_start=3188
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._serialized_end=3231
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._serialized_start=3233
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._serialized_end=3276
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE']._serialized_start=3279
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE']._serialized_end=5021
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._serialized_start=3998
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._serialized_end=4093
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._serialized_start=4095
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._serialized_end=4193
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._serialized_start=4195
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._serialized_end=4295
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._serialized_start=4297
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._serialized_end=4395
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._serialized_start=4397
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._serialized_end=4493
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._serialized_start=4495
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._serialized_end=4592
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._serialized_start=4594
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._serialized_end=4693
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._serialized_start=4695
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._serialized_end=4795
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._serialized_start=4797
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._serialized_end=4894
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._serialized_start=4896
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._serialized_end=4993
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_SAMPLEENUM']._serialized_start=4995
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_SAMPLEENUM']._serialized_end=5021
# @@protoc_insertion_point(module_scope)