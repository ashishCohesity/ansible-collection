# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/csharp/protos/unittest_custom_options_proto3.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nYexperimental/smurugesan/protobuf-3.6.0/csharp/protos/unittest_custom_options_proto3.proto\x12\x11protobuf_unittest\x1a google/protobuf/descriptor.proto\"\xd7\x01\n\x1cTestMessageWithCustomOptions\x12\x1e\n\x06\x66ield1\x18\x01 \x01(\tB\x0e\x08\x01\xc1\xe0\xc3\x1d-\xe1u\n\x02\x00\x00\x00\x12\x15\n\x0boneof_field\x18\x02 \x01(\x05H\x00\"S\n\x06\x41nEnum\x12\x16\n\x12\x41NENUM_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41NENUM_VAL1\x10\x01\x12\x16\n\x0b\x41NENUM_VAL2\x10\x02\x1a\x05\xb0\x86\xfa\x05{\x1a\x08\xc5\xf6\xc9\x1d\xeb\xfc\xff\xff:\x10\x08\x00\xe0\xe9\xc2\x1d\xc8\xff\xff\xff\xff\xff\xff\xff\xff\x01\x42\x19\n\x07\x41nOneof\x12\x0e\xf8\xac\xc3\x1d\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x01\"\x18\n\x16\x43ustomOptionFooRequest\"\x19\n\x17\x43ustomOptionFooResponse\"\x1e\n\x1c\x43ustomOptionFooClientMessage\"\x1e\n\x1c\x43ustomOptionFooServerMessage\"\x8f\x01\n\x1a\x44ummyMessageContainingEnum\"q\n\x0cTestEnumType\x12 \n\x1cTEST_OPTION_ENUM_UNSPECIFIED\x10\x00\x12\x1a\n\x16TEST_OPTION_ENUM_TYPE1\x10\x16\x12#\n\x16TEST_OPTION_ENUM_TYPE2\x10\xe9\xff\xff\xff\xff\xff\xff\xff\xff\x01\"!\n\x1f\x44ummyMessageInvalidAsOptionType\"\x8a\x01\n\x1c\x43ustomOptionMinIntegerValues:j\x99\xd6\xa8\x1d\x00\x00\x00\x00\x00\x00\x00\x80\xad\x8d\xaf\x1d\x00\x00\x00\x80\x91\xee\xaf\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x9d\xf5\xaf\x1d\x00\x00\x00\x00\xf8\x97\xb0\x1d\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x80\xc4\xb0\x1d\xff\xff\xff\xff\x0f\xf8\xf5\xb0\x1d\x00\x80\x93\xb2\x1d\x00\xb0\xbc\xb2\x1d\x80\x80\x80\x80\x80\x80\x80\x80\x80\x01\xe8\xc6\xb2\x1d\x80\x80\x80\x80\xf8\xff\xff\xff\xff\x01\xd0\xde\xb2\x1d\x00\"\x91\x01\n\x1c\x43ustomOptionMaxIntegerValues:q\x99\xd6\xa8\x1d\xff\xff\xff\xff\xff\xff\xff\x7f\xad\x8d\xaf\x1d\xff\xff\xff\x7f\x91\xee\xaf\x1d\xff\xff\xff\xff\xff\xff\xff\xff\x9d\xf5\xaf\x1d\xff\xff\xff\xff\xf8\x97\xb0\x1d\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x80\xc4\xb0\x1d\xfe\xff\xff\xff\x0f\xf8\xf5\xb0\x1d\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x80\x93\xb2\x1d\xff\xff\xff\xff\x0f\xb0\xbc\xb2\x1d\xff\xff\xff\xff\xff\xff\xff\xff\x7f\xe8\xc6\xb2\x1d\xff\xff\xff\xff\x07\xd0\xde\xb2\x1d\x01\"n\n\x17\x43ustomOptionOtherValues:S\x88\xd9\xa2\x1d\xe9\xff\xff\xff\xff\xff\xff\xff\xff\x01\xb2\xd9\xa2\x1d\x0bHello\x00World\xaa\xdc\xa2\x1d\x0eHello, \"World\"\xe9\xdc\xa2\x1d\xfbY\x8c\x42\xca\xc0\xf3?\xf5\xdf\xa3\x1d\xe7\x87\x45\x41\xe8\xc6\xb2\x1d\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\"4\n\x1cSettingRealsFromPositiveInts:\x14\xe9\xdc\xa2\x1d\x00\x00\x00\x00\x00@c@\xf5\xdf\xa3\x1d\x00\x00@A\"4\n\x1cSettingRealsFromNegativeInts:\x14\xe9\xdc\xa2\x1d\x00\x00\x00\x00\x00@c\xc0\xf5\xdf\xa3\x1d\x00\x00@\xc1\"K\n\x12\x43omplexOptionType1\x12\x0b\n\x03\x66oo\x18\x01 \x01(\x05\x12\x0c\n\x04\x66oo2\x18\x02 \x01(\x05\x12\x0c\n\x04\x66oo3\x18\x03 \x01(\x05\x12\x0c\n\x04\x66oo4\x18\x04 \x03(\x05\"\x81\x03\n\x12\x43omplexOptionType2\x12\x32\n\x03\x62\x61r\x18\x01 \x01(\x0b\x32%.protobuf_unittest.ComplexOptionType1\x12\x0b\n\x03\x62\x61z\x18\x02 \x01(\x05\x12\x46\n\x04\x66red\x18\x03 \x01(\x0b\x32\x38.protobuf_unittest.ComplexOptionType2.ComplexOptionType4\x12H\n\x06\x62\x61rney\x18\x04 \x03(\x0b\x32\x38.protobuf_unittest.ComplexOptionType2.ComplexOptionType4\x1a\x97\x01\n\x12\x43omplexOptionType4\x12\r\n\x05waldo\x18\x01 \x01(\x05\x32r\n\x0c\x63omplex_opt4\x12\x1f.google.protobuf.MessageOptions\x18\x8a\xf5\xd1\x03 \x01(\x0b\x32\x38.protobuf_unittest.ComplexOptionType2.ComplexOptionType4\"!\n\x12\x43omplexOptionType3\x12\x0b\n\x03qux\x18\x01 \x01(\x05\"N\n\x15VariousComplexOptions:5\xd2\xa8\x8f\x1d\x03\x08\xb3\x0f\xfa\xde\x90\x1d\x02\x08\t\xaa\xfd\x90\x1d\x16\n\x03\x08\xe7\x05\x10\xdb\x07\x1a\x03\x08\xc1\x02\"\x02\x08\x65\"\x03\x08\xd4\x01\xa2\xe2\x95\x1d\x06\x08*\"\x02\x63X\"L\n\tAggregate\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01s\x18\x02 \x01(\t\x12)\n\x03sub\x18\x03 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate\"Y\n\x10\x41ggregateMessage\x12)\n\tfieldname\x18\x01 \x01(\x05\x42\x16\xf2\xa1\x87;\x11\x12\x0f\x46ieldAnnotation:\x1a\xc2\xd1\x86;\x15\x08\x65\x12\x11MessageAnnotation\"\x97\x01\n\x10NestedOptionType\x1a;\n\rNestedMessage\x12\"\n\x0cnested_field\x18\x01 \x01(\x05\x42\x0c\xc1\xe0\xc3\x1d\xea\x03\x00\x00\x00\x00\x00\x00:\x06\xe0\xe9\xc2\x1d\xe9\x07\"F\n\nNestedEnum\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x1d\n\x11NESTED_ENUM_VALUE\x10\x01\x1a\x06\xb0\x86\xfa\x05\xec\x07\x1a\x08\xc5\xf6\xc9\x1d\xeb\x03\x00\x00*R\n\nMethodOpt1\x12\x1a\n\x16METHODOPT1_UNSPECIFIED\x10\x00\x12\x13\n\x0fMETHODOPT1_VAL1\x10\x01\x12\x13\n\x0fMETHODOPT1_VAL2\x10\x02*^\n\rAggregateEnum\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12%\n\x05VALUE\x10\x01\x1a\x1a\xca\xfc\x89;\x15\x12\x13\x45numValueAnnotation\x1a\x15\x92\x95\x88;\x10\x12\x0e\x45numAnnotation2\x8e\x01\n\x1cTestServiceWithCustomOptions\x12\x63\n\x03\x46oo\x12).protobuf_unittest.CustomOptionFooRequest\x1a*.protobuf_unittest.CustomOptionFooResponse\"\x05\xe0\xfa\x8c\x1e\x02\x1a\t\x90\xb2\x8b\x1e\xd3\xdb\x80\xcbI2\x99\x01\n\x10\x41ggregateService\x12k\n\x06Method\x12#.protobuf_unittest.AggregateMessage\x1a#.protobuf_unittest.AggregateMessage\"\x17\xca\xc8\x96;\x12\x12\x10MethodAnnotation\x1a\x18\xca\xfb\x8e;\x13\x12\x11ServiceAnnotation:2\n\tfile_opt1\x12\x1c.google.protobuf.FileOptions\x18\x8e\x9d\xd8\x03 \x01(\x04:8\n\x0cmessage_opt1\x12\x1f.google.protobuf.MessageOptions\x18\x9c\xad\xd8\x03 \x01(\x05:4\n\nfield_opt1\x12\x1d.google.protobuf.FieldOptions\x18\x88\xbc\xd8\x03 \x01(\x06:4\n\noneof_opt1\x12\x1d.google.protobuf.OneofOptions\x18\xcf\xb5\xd8\x03 \x01(\x05:2\n\tenum_opt1\x12\x1c.google.protobuf.EnumOptions\x18\xe8\x9e\xd9\x03 \x01(\x0f:<\n\x0f\x65num_value_opt1\x12!.google.protobuf.EnumValueOptions\x18\xe6\xa0_ \x01(\x05:8\n\x0cservice_opt1\x12\x1f.google.protobuf.ServiceOptions\x18\xa2\xb6\xe1\x03 \x01(\x12:U\n\x0bmethod_opt1\x12\x1e.google.protobuf.MethodOptions\x18\xac\xcf\xe1\x03 \x01(\x0e\x32\x1d.protobuf_unittest.MethodOpt1:4\n\x08\x62ool_opt\x12\x1f.google.protobuf.MessageOptions\x18\xea\xab\xd6\x03 \x01(\x08:5\n\tint32_opt\x12\x1f.google.protobuf.MessageOptions\x18\xed\xa8\xd6\x03 \x01(\x05:5\n\tint64_opt\x12\x1f.google.protobuf.MessageOptions\x18\xc6\xa7\xd6\x03 \x01(\x03:6\n\nuint32_opt\x12\x1f.google.protobuf.MessageOptions\x18\xb0\xa2\xd6\x03 \x01(\r:6\n\nuint64_opt\x12\x1f.google.protobuf.MessageOptions\x18\xdf\x8e\xd6\x03 \x01(\x04:6\n\nsint32_opt\x12\x1f.google.protobuf.MessageOptions\x18\xc0\x88\xd6\x03 \x01(\x11:6\n\nsint64_opt\x12\x1f.google.protobuf.MessageOptions\x18\xff\x82\xd6\x03 \x01(\x12:7\n\x0b\x66ixed32_opt\x12\x1f.google.protobuf.MessageOptions\x18\xd3\xfe\xd5\x03 \x01(\x07:7\n\x0b\x66ixed64_opt\x12\x1f.google.protobuf.MessageOptions\x18\xe2\xfd\xd5\x03 \x01(\x06:8\n\x0csfixed32_opt\x12\x1f.google.protobuf.MessageOptions\x18\xd5\xf1\xd5\x03 \x01(\x0f:8\n\x0csfixed64_opt\x12\x1f.google.protobuf.MessageOptions\x18\xe3\x8a\xd5\x03 \x01(\x10:5\n\tfloat_opt\x12\x1f.google.protobuf.MessageOptions\x18\xfe\xbb\xd4\x03 \x01(\x02:6\n\ndouble_opt\x12\x1f.google.protobuf.MessageOptions\x18\xcd\xab\xd4\x03 \x01(\x01:6\n\nstring_opt\x12\x1f.google.protobuf.MessageOptions\x18\xc5\xab\xd4\x03 \x01(\t:5\n\tbytes_opt\x12\x1f.google.protobuf.MessageOptions\x18\x96\xab\xd4\x03 \x01(\x0c:p\n\x08\x65num_opt\x12\x1f.google.protobuf.MessageOptions\x18\x91\xab\xd4\x03 \x01(\x0e\x32:.protobuf_unittest.DummyMessageContainingEnum.TestEnumType:p\n\x10message_type_opt\x12\x1f.google.protobuf.MessageOptions\x18\xaf\xf2\xd3\x03 \x01(\x0b\x32\x32.protobuf_unittest.DummyMessageInvalidAsOptionType:_\n\x0c\x63omplex_opt1\x12\x1f.google.protobuf.MessageOptions\x18\xa4\xdc\xd2\x03 \x01(\x0b\x32%.protobuf_unittest.ComplexOptionType1:_\n\x0c\x63omplex_opt2\x12\x1f.google.protobuf.MessageOptions\x18\xd5\x8f\xd2\x03 \x01(\x0b\x32%.protobuf_unittest.ComplexOptionType2:_\n\x0c\x63omplex_opt3\x12\x1f.google.protobuf.MessageOptions\x18\xef\x8b\xd2\x03 \x01(\x0b\x32%.protobuf_unittest.ComplexOptionType3:N\n\x07\x66ileopt\x12\x1c.google.protobuf.FileOptions\x18\xcf\xdd\xb0\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:P\n\x06msgopt\x12\x1f.google.protobuf.MessageOptions\x18\x98\xea\xb0\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:P\n\x08\x66ieldopt\x12\x1d.google.protobuf.FieldOptions\x18\x9e\xf4\xb0\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:N\n\x07\x65numopt\x12\x1c.google.protobuf.EnumOptions\x18\xd2\x82\xb1\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:V\n\nenumvalopt\x12!.google.protobuf.EnumValueOptions\x18\xc9\x9f\xb1\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:T\n\nserviceopt\x12\x1f.google.protobuf.ServiceOptions\x18\xb9\xef\xb1\x07 \x01(\x0b\x32\x1c.protobuf_unittest.Aggregate:R\n\tmethodopt\x12\x1e.google.protobuf.MethodOptions\x18\x89\xe9\xb2\x07 \x01(\x0b\x32\x1c.protobuf_unittest.AggregateBU\xaa\x02\x1aUnitTest.Issues.TestProtos\xf0\xe8\xc1\x1d\xea\xad\xc0\xe5$\xfa\xec\x85;*\x08\x64\x12\x0e\x46ileAnnotation\x1a\x16\x12\x14NestedFileAnnotationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.csharp.protos.unittest_custom_options_proto3_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\032UnitTest.Issues.TestProtos\360\350\301\035\352\255\300\345$\372\354\205;*\010d\022\016FileAnnotation\032\026\022\024NestedFileAnnotation'
  _globals['_AGGREGATEENUM']._loaded_options = None
  _globals['_AGGREGATEENUM']._serialized_options = b'\222\225\210;\020\022\016EnumAnnotation'
  _globals['_AGGREGATEENUM'].values_by_name["VALUE"]._loaded_options = None
  _globals['_AGGREGATEENUM'].values_by_name["VALUE"]._serialized_options = b'\312\374\211;\025\022\023EnumValueAnnotation'
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS'].oneofs_by_name['AnOneof']._loaded_options = None
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS'].oneofs_by_name['AnOneof']._serialized_options = b'\370\254\303\035\235\377\377\377\377\377\377\377\377\001'
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM']._loaded_options = None
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM']._serialized_options = b'\305\366\311\035\353\374\377\377'
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM'].values_by_name["ANENUM_VAL2"]._loaded_options = None
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM'].values_by_name["ANENUM_VAL2"]._serialized_options = b'\260\206\372\005{'
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS'].fields_by_name['field1']._loaded_options = None
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS'].fields_by_name['field1']._serialized_options = b'\010\001\301\340\303\035-\341u\n\002\000\000\000'
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS']._loaded_options = None
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS']._serialized_options = b'\010\000\340\351\302\035\310\377\377\377\377\377\377\377\377\001'
  _globals['_CUSTOMOPTIONMININTEGERVALUES']._loaded_options = None
  _globals['_CUSTOMOPTIONMININTEGERVALUES']._serialized_options = b'\231\326\250\035\000\000\000\000\000\000\000\200\255\215\257\035\000\000\000\200\221\356\257\035\000\000\000\000\000\000\000\000\235\365\257\035\000\000\000\000\370\227\260\035\377\377\377\377\377\377\377\377\377\001\200\304\260\035\377\377\377\377\017\370\365\260\035\000\200\223\262\035\000\260\274\262\035\200\200\200\200\200\200\200\200\200\001\350\306\262\035\200\200\200\200\370\377\377\377\377\001\320\336\262\035\000'
  _globals['_CUSTOMOPTIONMAXINTEGERVALUES']._loaded_options = None
  _globals['_CUSTOMOPTIONMAXINTEGERVALUES']._serialized_options = b'\231\326\250\035\377\377\377\377\377\377\377\177\255\215\257\035\377\377\377\177\221\356\257\035\377\377\377\377\377\377\377\377\235\365\257\035\377\377\377\377\370\227\260\035\376\377\377\377\377\377\377\377\377\001\200\304\260\035\376\377\377\377\017\370\365\260\035\377\377\377\377\377\377\377\377\377\001\200\223\262\035\377\377\377\377\017\260\274\262\035\377\377\377\377\377\377\377\377\177\350\306\262\035\377\377\377\377\007\320\336\262\035\001'
  _globals['_CUSTOMOPTIONOTHERVALUES']._loaded_options = None
  _globals['_CUSTOMOPTIONOTHERVALUES']._serialized_options = b'\210\331\242\035\351\377\377\377\377\377\377\377\377\001\262\331\242\035\013Hello\000World\252\334\242\035\016Hello, \"World\"\351\334\242\035\373Y\214B\312\300\363?\365\337\243\035\347\207EA\350\306\262\035\234\377\377\377\377\377\377\377\377\001'
  _globals['_SETTINGREALSFROMPOSITIVEINTS']._loaded_options = None
  _globals['_SETTINGREALSFROMPOSITIVEINTS']._serialized_options = b'\351\334\242\035\000\000\000\000\000@c@\365\337\243\035\000\000@A'
  _globals['_SETTINGREALSFROMNEGATIVEINTS']._loaded_options = None
  _globals['_SETTINGREALSFROMNEGATIVEINTS']._serialized_options = b'\351\334\242\035\000\000\000\000\000@c\300\365\337\243\035\000\000@\301'
  _globals['_VARIOUSCOMPLEXOPTIONS']._loaded_options = None
  _globals['_VARIOUSCOMPLEXOPTIONS']._serialized_options = b'\322\250\217\035\003\010\263\017\372\336\220\035\002\010\t\252\375\220\035\026\n\003\010\347\005\020\333\007\032\003\010\301\002\"\002\010e\"\003\010\324\001\242\342\225\035\006\010*\"\002cX'
  _globals['_AGGREGATEMESSAGE'].fields_by_name['fieldname']._loaded_options = None
  _globals['_AGGREGATEMESSAGE'].fields_by_name['fieldname']._serialized_options = b'\362\241\207;\021\022\017FieldAnnotation'
  _globals['_AGGREGATEMESSAGE']._loaded_options = None
  _globals['_AGGREGATEMESSAGE']._serialized_options = b'\302\321\206;\025\010e\022\021MessageAnnotation'
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE'].fields_by_name['nested_field']._loaded_options = None
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE'].fields_by_name['nested_field']._serialized_options = b'\301\340\303\035\352\003\000\000\000\000\000\000'
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE']._loaded_options = None
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE']._serialized_options = b'\340\351\302\035\351\007'
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM']._loaded_options = None
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM']._serialized_options = b'\305\366\311\035\353\003\000\000'
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM'].values_by_name["NESTED_ENUM_VALUE"]._loaded_options = None
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM'].values_by_name["NESTED_ENUM_VALUE"]._serialized_options = b'\260\206\372\005\354\007'
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS']._loaded_options = None
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS']._serialized_options = b'\220\262\213\036\323\333\200\313I'
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS'].methods_by_name['Foo']._loaded_options = None
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS'].methods_by_name['Foo']._serialized_options = b'\340\372\214\036\002'
  _globals['_AGGREGATESERVICE']._loaded_options = None
  _globals['_AGGREGATESERVICE']._serialized_options = b'\312\373\216;\023\022\021ServiceAnnotation'
  _globals['_AGGREGATESERVICE'].methods_by_name['Method']._loaded_options = None
  _globals['_AGGREGATESERVICE'].methods_by_name['Method']._serialized_options = b'\312\310\226;\022\022\020MethodAnnotation'
  _globals['_METHODOPT1']._serialized_start=2074
  _globals['_METHODOPT1']._serialized_end=2156
  _globals['_AGGREGATEENUM']._serialized_start=2158
  _globals['_AGGREGATEENUM']._serialized_end=2252
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS']._serialized_start=147
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS']._serialized_end=362
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM']._serialized_start=234
  _globals['_TESTMESSAGEWITHCUSTOMOPTIONS_ANENUM']._serialized_end=317
  _globals['_CUSTOMOPTIONFOOREQUEST']._serialized_start=364
  _globals['_CUSTOMOPTIONFOOREQUEST']._serialized_end=388
  _globals['_CUSTOMOPTIONFOORESPONSE']._serialized_start=390
  _globals['_CUSTOMOPTIONFOORESPONSE']._serialized_end=415
  _globals['_CUSTOMOPTIONFOOCLIENTMESSAGE']._serialized_start=417
  _globals['_CUSTOMOPTIONFOOCLIENTMESSAGE']._serialized_end=447
  _globals['_CUSTOMOPTIONFOOSERVERMESSAGE']._serialized_start=449
  _globals['_CUSTOMOPTIONFOOSERVERMESSAGE']._serialized_end=479
  _globals['_DUMMYMESSAGECONTAININGENUM']._serialized_start=482
  _globals['_DUMMYMESSAGECONTAININGENUM']._serialized_end=625
  _globals['_DUMMYMESSAGECONTAININGENUM_TESTENUMTYPE']._serialized_start=512
  _globals['_DUMMYMESSAGECONTAININGENUM_TESTENUMTYPE']._serialized_end=625
  _globals['_DUMMYMESSAGEINVALIDASOPTIONTYPE']._serialized_start=627
  _globals['_DUMMYMESSAGEINVALIDASOPTIONTYPE']._serialized_end=660
  _globals['_CUSTOMOPTIONMININTEGERVALUES']._serialized_start=663
  _globals['_CUSTOMOPTIONMININTEGERVALUES']._serialized_end=801
  _globals['_CUSTOMOPTIONMAXINTEGERVALUES']._serialized_start=804
  _globals['_CUSTOMOPTIONMAXINTEGERVALUES']._serialized_end=949
  _globals['_CUSTOMOPTIONOTHERVALUES']._serialized_start=951
  _globals['_CUSTOMOPTIONOTHERVALUES']._serialized_end=1061
  _globals['_SETTINGREALSFROMPOSITIVEINTS']._serialized_start=1063
  _globals['_SETTINGREALSFROMPOSITIVEINTS']._serialized_end=1115
  _globals['_SETTINGREALSFROMNEGATIVEINTS']._serialized_start=1117
  _globals['_SETTINGREALSFROMNEGATIVEINTS']._serialized_end=1169
  _globals['_COMPLEXOPTIONTYPE1']._serialized_start=1171
  _globals['_COMPLEXOPTIONTYPE1']._serialized_end=1246
  _globals['_COMPLEXOPTIONTYPE2']._serialized_start=1249
  _globals['_COMPLEXOPTIONTYPE2']._serialized_end=1634
  _globals['_COMPLEXOPTIONTYPE2_COMPLEXOPTIONTYPE4']._serialized_start=1483
  _globals['_COMPLEXOPTIONTYPE2_COMPLEXOPTIONTYPE4']._serialized_end=1634
  _globals['_COMPLEXOPTIONTYPE3']._serialized_start=1636
  _globals['_COMPLEXOPTIONTYPE3']._serialized_end=1669
  _globals['_VARIOUSCOMPLEXOPTIONS']._serialized_start=1671
  _globals['_VARIOUSCOMPLEXOPTIONS']._serialized_end=1749
  _globals['_AGGREGATE']._serialized_start=1751
  _globals['_AGGREGATE']._serialized_end=1827
  _globals['_AGGREGATEMESSAGE']._serialized_start=1829
  _globals['_AGGREGATEMESSAGE']._serialized_end=1918
  _globals['_NESTEDOPTIONTYPE']._serialized_start=1921
  _globals['_NESTEDOPTIONTYPE']._serialized_end=2072
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE']._serialized_start=1941
  _globals['_NESTEDOPTIONTYPE_NESTEDMESSAGE']._serialized_end=2000
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM']._serialized_start=2002
  _globals['_NESTEDOPTIONTYPE_NESTEDENUM']._serialized_end=2072
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS']._serialized_start=2255
  _globals['_TESTSERVICEWITHCUSTOMOPTIONS']._serialized_end=2397
  _globals['_AGGREGATESERVICE']._serialized_start=2400
  _globals['_AGGREGATESERVICE']._serialized_end=2553
# @@protoc_insertion_point(module_scope)
