# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/csharp/protos/unittest_issues.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJexperimental/smurugesan/protobuf-3.6.0/csharp/protos/unittest_issues.proto\x12\x0funittest_issues\"\'\n\x08Issue307\x1a\x1b\n\nNestedOnce\x1a\r\n\x0bNestedTwice\"\xb0\x01\n\x13NegativeEnumMessage\x12,\n\x05value\x18\x01 \x01(\x0e\x32\x1d.unittest_issues.NegativeEnum\x12\x31\n\x06values\x18\x02 \x03(\x0e\x32\x1d.unittest_issues.NegativeEnumB\x02\x10\x00\x12\x38\n\rpacked_values\x18\x03 \x03(\x0e\x32\x1d.unittest_issues.NegativeEnumB\x02\x10\x01\"\x11\n\x0f\x44\x65precatedChild\"\xb9\x02\n\x17\x44\x65precatedFieldsMessage\x12\x1a\n\x0ePrimitiveValue\x18\x01 \x01(\x05\x42\x02\x18\x01\x12\x1a\n\x0ePrimitiveArray\x18\x02 \x03(\x05\x42\x02\x18\x01\x12:\n\x0cMessageValue\x18\x03 \x01(\x0b\x32 .unittest_issues.DeprecatedChildB\x02\x18\x01\x12:\n\x0cMessageArray\x18\x04 \x03(\x0b\x32 .unittest_issues.DeprecatedChildB\x02\x18\x01\x12\x36\n\tEnumValue\x18\x05 \x01(\x0e\x32\x1f.unittest_issues.DeprecatedEnumB\x02\x18\x01\x12\x36\n\tEnumArray\x18\x06 \x03(\x0e\x32\x1f.unittest_issues.DeprecatedEnumB\x02\x18\x01\"\x19\n\tItemField\x12\x0c\n\x04item\x18\x01 \x01(\x05\"D\n\rReservedNames\x12\r\n\x05types\x18\x01 \x01(\x05\x12\x12\n\ndescriptor\x18\x02 \x01(\x05\x1a\x10\n\x0eSomeNestedType\"\xa0\x01\n\x15TestJsonFieldOrdering\x12\x13\n\x0bplain_int32\x18\x04 \x01(\x05\x12\x13\n\to1_string\x18\x02 \x01(\tH\x00\x12\x12\n\x08o1_int32\x18\x05 \x01(\x05H\x00\x12\x14\n\x0cplain_string\x18\x01 \x01(\t\x12\x12\n\x08o2_int32\x18\x06 \x01(\x05H\x01\x12\x13\n\to2_string\x18\x03 \x01(\tH\x01\x42\x04\n\x02o1B\x04\n\x02o2\"K\n\x0cTestJsonName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0b\x64\x65scription\x18\x02 \x01(\tR\x04\x64\x65sc\x12\x12\n\x04guid\x18\x03 \x01(\tR\x04\x65xid\"\x7f\n\x0cOneofMerging\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x36\n\x06nested\x18\x02 \x01(\x0b\x32$.unittest_issues.OneofMerging.NestedH\x00\x1a\x1e\n\x06Nested\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x42\x07\n\x05value*U\n\x0cNegativeEnum\x12\x16\n\x12NEGATIVE_ENUM_ZERO\x10\x00\x12\x16\n\tFiveBelow\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x15\n\x08MinusOne\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*.\n\x0e\x44\x65precatedEnum\x12\x13\n\x0f\x44\x45PRECATED_ZERO\x10\x00\x12\x07\n\x03one\x10\x01\x42\x1d\xaa\x02\x1aUnitTest.Issues.TestProtosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.csharp.protos.unittest_issues_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\032UnitTest.Issues.TestProtos'
  _globals['_NEGATIVEENUMMESSAGE'].fields_by_name['values']._loaded_options = None
  _globals['_NEGATIVEENUMMESSAGE'].fields_by_name['values']._serialized_options = b'\020\000'
  _globals['_NEGATIVEENUMMESSAGE'].fields_by_name['packed_values']._loaded_options = None
  _globals['_NEGATIVEENUMMESSAGE'].fields_by_name['packed_values']._serialized_options = b'\020\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['PrimitiveValue']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['PrimitiveValue']._serialized_options = b'\030\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['PrimitiveArray']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['PrimitiveArray']._serialized_options = b'\030\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['MessageValue']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['MessageValue']._serialized_options = b'\030\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['MessageArray']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['MessageArray']._serialized_options = b'\030\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['EnumValue']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['EnumValue']._serialized_options = b'\030\001'
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['EnumArray']._loaded_options = None
  _globals['_DEPRECATEDFIELDSMESSAGE'].fields_by_name['EnumArray']._serialized_options = b'\030\001'
  _globals['_NEGATIVEENUM']._serialized_start=1116
  _globals['_NEGATIVEENUM']._serialized_end=1201
  _globals['_DEPRECATEDENUM']._serialized_start=1203
  _globals['_DEPRECATEDENUM']._serialized_end=1249
  _globals['_ISSUE307']._serialized_start=95
  _globals['_ISSUE307']._serialized_end=134
  _globals['_ISSUE307_NESTEDONCE']._serialized_start=107
  _globals['_ISSUE307_NESTEDONCE']._serialized_end=134
  _globals['_ISSUE307_NESTEDONCE_NESTEDTWICE']._serialized_start=121
  _globals['_ISSUE307_NESTEDONCE_NESTEDTWICE']._serialized_end=134
  _globals['_NEGATIVEENUMMESSAGE']._serialized_start=137
  _globals['_NEGATIVEENUMMESSAGE']._serialized_end=313
  _globals['_DEPRECATEDCHILD']._serialized_start=315
  _globals['_DEPRECATEDCHILD']._serialized_end=332
  _globals['_DEPRECATEDFIELDSMESSAGE']._serialized_start=335
  _globals['_DEPRECATEDFIELDSMESSAGE']._serialized_end=648
  _globals['_ITEMFIELD']._serialized_start=650
  _globals['_ITEMFIELD']._serialized_end=675
  _globals['_RESERVEDNAMES']._serialized_start=677
  _globals['_RESERVEDNAMES']._serialized_end=745
  _globals['_RESERVEDNAMES_SOMENESTEDTYPE']._serialized_start=729
  _globals['_RESERVEDNAMES_SOMENESTEDTYPE']._serialized_end=745
  _globals['_TESTJSONFIELDORDERING']._serialized_start=748
  _globals['_TESTJSONFIELDORDERING']._serialized_end=908
  _globals['_TESTJSONNAME']._serialized_start=910
  _globals['_TESTJSONNAME']._serialized_end=985
  _globals['_ONEOFMERGING']._serialized_start=987
  _globals['_ONEOFMERGING']._serialized_end=1114
  _globals['_ONEOFMERGING_NESTED']._serialized_start=1075
  _globals['_ONEOFMERGING_NESTED']._serialized_end=1105
# @@protoc_insertion_point(module_scope)
