# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/java/core/src/test/proto/com/google/protobuf/map_for_proto2_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nmexperimental/smurugesan/protobuf-3.6.0/java/core/src/test/proto/com/google/protobuf/map_for_proto2_test.proto\x12\x13map_for_proto2_test\"\xf6\t\n\x07TestMap\x12Q\n\x14int32_to_int32_field\x18\x01 \x03(\x0b\x32\x33.map_for_proto2_test.TestMap.Int32ToInt32FieldEntry\x12S\n\x15int32_to_string_field\x18\x02 \x03(\x0b\x32\x34.map_for_proto2_test.TestMap.Int32ToStringFieldEntry\x12Q\n\x14int32_to_bytes_field\x18\x03 \x03(\x0b\x32\x33.map_for_proto2_test.TestMap.Int32ToBytesFieldEntry\x12O\n\x13int32_to_enum_field\x18\x04 \x03(\x0b\x32\x32.map_for_proto2_test.TestMap.Int32ToEnumFieldEntry\x12U\n\x16int32_to_message_field\x18\x05 \x03(\x0b\x32\x35.map_for_proto2_test.TestMap.Int32ToMessageFieldEntry\x12S\n\x15string_to_int32_field\x18\x06 \x03(\x0b\x32\x34.map_for_proto2_test.TestMap.StringToInt32FieldEntry\x12R\n\x14required_message_map\x18\x0b \x03(\x0b\x32\x34.map_for_proto2_test.TestMap.RequiredMessageMapEntry\x1a\x1d\n\x0cMessageValue\x12\r\n\x05value\x18\x01 \x01(\x05\x1a\x38\n\x16Int32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17Int32ToStringFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16Int32ToBytesFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a_\n\x15Int32ToEnumFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x35\n\x05value\x18\x02 \x01(\x0e\x32&.map_for_proto2_test.TestMap.EnumValue:\x02\x38\x01\x1a\x65\n\x18Int32ToMessageFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).map_for_proto2_test.TestMap.MessageValue:\x02\x38\x01\x1a\x39\n\x17StringToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a*\n\x19MessageWithRequiredFields\x12\r\n\x05value\x18\x01 \x02(\x05\x1aq\n\x17RequiredMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.map_for_proto2_test.TestMap.MessageWithRequiredFields:\x02\x38\x01\"/\n\tEnumValue\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\x12\x07\n\x03QUX\x10\x03\"\xb0\x01\n\x14TestUnknownEnumValue\x12^\n\x14int32_to_int32_field\x18\x04 \x03(\x0b\x32@.map_for_proto2_test.TestUnknownEnumValue.Int32ToInt32FieldEntry\x1a\x38\n\x16Int32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xdd\x01\n\x10TestRecursiveMap\x12\r\n\x05value\x18\x01 \x01(\x05\x12Y\n\x13recursive_map_field\x18\x02 \x03(\x0b\x32<.map_for_proto2_test.TestRecursiveMap.RecursiveMapFieldEntry\x1a_\n\x16RecursiveMapFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.map_for_proto2_test.TestRecursiveMap:\x02\x38\x01\"\x91\x07\n\x0e\x42izarroTestMap\x12X\n\x14int32_to_int32_field\x18\x01 \x03(\x0b\x32:.map_for_proto2_test.BizarroTestMap.Int32ToInt32FieldEntry\x12Z\n\x15int32_to_string_field\x18\x02 \x03(\x0b\x32;.map_for_proto2_test.BizarroTestMap.Int32ToStringFieldEntry\x12X\n\x14int32_to_bytes_field\x18\x03 \x03(\x0b\x32:.map_for_proto2_test.BizarroTestMap.Int32ToBytesFieldEntry\x12V\n\x13int32_to_enum_field\x18\x04 \x03(\x0b\x32\x39.map_for_proto2_test.BizarroTestMap.Int32ToEnumFieldEntry\x12\\\n\x16int32_to_message_field\x18\x05 \x03(\x0b\x32<.map_for_proto2_test.BizarroTestMap.Int32ToMessageFieldEntry\x12Z\n\x15string_to_int32_field\x18\x06 \x03(\x0b\x32;.map_for_proto2_test.BizarroTestMap.StringToInt32FieldEntry\x1a\x38\n\x16Int32ToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x39\n\x17Int32ToStringFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16Int32ToBytesFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Int32ToEnumFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a:\n\x18Int32ToMessageFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x39\n\x17StringToInt32FieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xf5\x08\n\x12ReservedAsMapField\x12;\n\x02if\x18\x01 \x03(\x0b\x32/.map_for_proto2_test.ReservedAsMapField.IfEntry\x12\x41\n\x05\x63onst\x18\x02 \x03(\x0b\x32\x32.map_for_proto2_test.ReservedAsMapField.ConstEntry\x12\x45\n\x07private\x18\x03 \x03(\x0b\x32\x34.map_for_proto2_test.ReservedAsMapField.PrivateEntry\x12\x41\n\x05\x63lass\x18\x04 \x03(\x0b\x32\x32.map_for_proto2_test.ReservedAsMapField.ClassEntry\x12=\n\x03int\x18\x05 \x03(\x0b\x32\x30.map_for_proto2_test.ReservedAsMapField.IntEntry\x12?\n\x04void\x18\x06 \x03(\x0b\x32\x31.map_for_proto2_test.ReservedAsMapField.VoidEntry\x12\x43\n\x06string\x18\x07 \x03(\x0b\x32\x33.map_for_proto2_test.ReservedAsMapField.StringEntry\x12\x45\n\x07package\x18\x08 \x03(\x0b\x32\x34.map_for_proto2_test.ReservedAsMapField.PackageEntry\x12?\n\x04\x65num\x18\t \x03(\x0b\x32\x31.map_for_proto2_test.ReservedAsMapField.EnumEntry\x12?\n\x04null\x18\n \x03(\x0b\x32\x31.map_for_proto2_test.ReservedAsMapField.NullEntry\x1a)\n\x07IfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a,\n\nConstEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a.\n\x0cPrivateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a,\n\nClassEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a*\n\x08IntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tVoidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a-\n\x0bStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a.\n\x0cPackageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a+\n\tNullEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xaa\x0f\n\x1fReservedAsMapFieldWithEnumValue\x12H\n\x02if\x18\x01 \x03(\x0b\x32<.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.IfEntry\x12N\n\x05\x63onst\x18\x02 \x03(\x0b\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.ConstEntry\x12R\n\x07private\x18\x03 \x03(\x0b\x32\x41.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.PrivateEntry\x12N\n\x05\x63lass\x18\x04 \x03(\x0b\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.ClassEntry\x12J\n\x03int\x18\x05 \x03(\x0b\x32=.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.IntEntry\x12L\n\x04void\x18\x06 \x03(\x0b\x32>.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.VoidEntry\x12P\n\x06string\x18\x07 \x03(\x0b\x32@.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.StringEntry\x12R\n\x07package\x18\x08 \x03(\x0b\x32\x41.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.PackageEntry\x12L\n\x04\x65num\x18\t \x03(\x0b\x32>.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.EnumEntry\x12L\n\x04null\x18\n \x03(\x0b\x32>.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.NullEntry\x1aj\n\x07IfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1am\n\nConstEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1ao\n\x0cPrivateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1am\n\nClassEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1ak\n\x08IntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1al\n\tVoidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1an\n\x0bStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1ao\n\x0cPackageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1al\n\tEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\x1al\n\tNullEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0e\x32?.map_for_proto2_test.ReservedAsMapFieldWithEnumValue.SampleEnum:\x02\x38\x01\"\x1a\n\nSampleEnum\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x42!\n\x08map_testB\x15MapForProto2TestProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.java.core.src.test.proto.com.google.protobuf.map_for_proto2_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\010map_testB\025MapForProto2TestProto'
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
  _globals['_TESTMAP_REQUIREDMESSAGEMAPENTRY']._loaded_options = None
  _globals['_TESTMAP_REQUIREDMESSAGEMAPENTRY']._serialized_options = b'8\001'
  _globals['_TESTUNKNOWNENUMVALUE_INT32TOINT32FIELDENTRY']._loaded_options = None
  _globals['_TESTUNKNOWNENUMVALUE_INT32TOINT32FIELDENTRY']._serialized_options = b'8\001'
  _globals['_TESTRECURSIVEMAP_RECURSIVEMAPFIELDENTRY']._loaded_options = None
  _globals['_TESTRECURSIVEMAP_RECURSIVEMAPFIELDENTRY']._serialized_options = b'8\001'
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
  _globals['_TESTMAP']._serialized_start=135
  _globals['_TESTMAP']._serialized_end=1405
  _globals['_TESTMAP_MESSAGEVALUE']._serialized_start=734
  _globals['_TESTMAP_MESSAGEVALUE']._serialized_end=763
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._serialized_start=765
  _globals['_TESTMAP_INT32TOINT32FIELDENTRY']._serialized_end=821
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_start=823
  _globals['_TESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_end=880
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._serialized_start=882
  _globals['_TESTMAP_INT32TOBYTESFIELDENTRY']._serialized_end=938
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._serialized_start=940
  _globals['_TESTMAP_INT32TOENUMFIELDENTRY']._serialized_end=1035
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_start=1037
  _globals['_TESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_end=1138
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._serialized_start=1140
  _globals['_TESTMAP_STRINGTOINT32FIELDENTRY']._serialized_end=1197
  _globals['_TESTMAP_MESSAGEWITHREQUIREDFIELDS']._serialized_start=1199
  _globals['_TESTMAP_MESSAGEWITHREQUIREDFIELDS']._serialized_end=1241
  _globals['_TESTMAP_REQUIREDMESSAGEMAPENTRY']._serialized_start=1243
  _globals['_TESTMAP_REQUIREDMESSAGEMAPENTRY']._serialized_end=1356
  _globals['_TESTMAP_ENUMVALUE']._serialized_start=1358
  _globals['_TESTMAP_ENUMVALUE']._serialized_end=1405
  _globals['_TESTUNKNOWNENUMVALUE']._serialized_start=1408
  _globals['_TESTUNKNOWNENUMVALUE']._serialized_end=1584
  _globals['_TESTUNKNOWNENUMVALUE_INT32TOINT32FIELDENTRY']._serialized_start=765
  _globals['_TESTUNKNOWNENUMVALUE_INT32TOINT32FIELDENTRY']._serialized_end=821
  _globals['_TESTRECURSIVEMAP']._serialized_start=1587
  _globals['_TESTRECURSIVEMAP']._serialized_end=1808
  _globals['_TESTRECURSIVEMAP_RECURSIVEMAPFIELDENTRY']._serialized_start=1713
  _globals['_TESTRECURSIVEMAP_RECURSIVEMAPFIELDENTRY']._serialized_end=1808
  _globals['_BIZARROTESTMAP']._serialized_start=1811
  _globals['_BIZARROTESTMAP']._serialized_end=2724
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._serialized_start=2375
  _globals['_BIZARROTESTMAP_INT32TOINT32FIELDENTRY']._serialized_end=2431
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_start=2433
  _globals['_BIZARROTESTMAP_INT32TOSTRINGFIELDENTRY']._serialized_end=2490
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._serialized_start=2492
  _globals['_BIZARROTESTMAP_INT32TOBYTESFIELDENTRY']._serialized_end=2548
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._serialized_start=2550
  _globals['_BIZARROTESTMAP_INT32TOENUMFIELDENTRY']._serialized_end=2605
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_start=2607
  _globals['_BIZARROTESTMAP_INT32TOMESSAGEFIELDENTRY']._serialized_end=2665
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._serialized_start=2667
  _globals['_BIZARROTESTMAP_STRINGTOINT32FIELDENTRY']._serialized_end=2724
  _globals['_RESERVEDASMAPFIELD']._serialized_start=2727
  _globals['_RESERVEDASMAPFIELD']._serialized_end=3868
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._serialized_start=3413
  _globals['_RESERVEDASMAPFIELD_IFENTRY']._serialized_end=3454
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._serialized_start=3456
  _globals['_RESERVEDASMAPFIELD_CONSTENTRY']._serialized_end=3500
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._serialized_start=3502
  _globals['_RESERVEDASMAPFIELD_PRIVATEENTRY']._serialized_end=3548
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._serialized_start=3550
  _globals['_RESERVEDASMAPFIELD_CLASSENTRY']._serialized_end=3594
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._serialized_start=3596
  _globals['_RESERVEDASMAPFIELD_INTENTRY']._serialized_end=3638
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._serialized_start=3640
  _globals['_RESERVEDASMAPFIELD_VOIDENTRY']._serialized_end=3683
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._serialized_start=3685
  _globals['_RESERVEDASMAPFIELD_STRINGENTRY']._serialized_end=3730
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._serialized_start=3732
  _globals['_RESERVEDASMAPFIELD_PACKAGEENTRY']._serialized_end=3778
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._serialized_start=3780
  _globals['_RESERVEDASMAPFIELD_ENUMENTRY']._serialized_end=3823
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._serialized_start=3825
  _globals['_RESERVEDASMAPFIELD_NULLENTRY']._serialized_end=3868
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE']._serialized_start=3871
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE']._serialized_end=5833
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._serialized_start=4700
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_IFENTRY']._serialized_end=4806
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._serialized_start=4808
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CONSTENTRY']._serialized_end=4917
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._serialized_start=4919
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PRIVATEENTRY']._serialized_end=5030
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._serialized_start=5032
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_CLASSENTRY']._serialized_end=5141
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._serialized_start=5143
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_INTENTRY']._serialized_end=5250
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._serialized_start=5252
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_VOIDENTRY']._serialized_end=5360
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._serialized_start=5362
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_STRINGENTRY']._serialized_end=5472
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._serialized_start=5474
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_PACKAGEENTRY']._serialized_end=5585
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._serialized_start=5587
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_ENUMENTRY']._serialized_end=5695
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._serialized_start=5697
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_NULLENTRY']._serialized_end=5805
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_SAMPLEENUM']._serialized_start=5807
  _globals['_RESERVEDASMAPFIELDWITHENUMVALUE_SAMPLEENUM']._serialized_end=5833
# @@protoc_insertion_point(module_scope)
