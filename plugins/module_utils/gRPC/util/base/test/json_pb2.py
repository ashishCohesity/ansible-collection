# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/base/test/json.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19util/base/test/json.proto\x12\rcohesity.test\"\xdd\x02\n\x0bJsonMessage\x12\x1a\n\x12id_int64_as_string\x18\x01 \x01(\x03\x12\x1f\n\x13id_int64_as_numeric\x18\x07 \x01(\x03\x42\x02\x30\x02\x12\x1b\n\x13id_int32_as_numeric\x18\x08 \x01(\x05\x12\x11\n\tname_long\x18\x02 \x01(\t\x12\x13\n\x0bpercent_vec\x18\x03 \x03(\x02\x12>\n\x0bsub_message\x18\x04 \x01(\x0b\x32).cohesity.test.JsonMessage.SubJsonMessage\x12\x42\n\x0frep_sub_message\x18\x05 \x03(\x0b\x32).cohesity.test.JsonMessage.SubJsonMessage\x12\x14\n\x0cunused_field\x18\x06 \x01(\t\x1a\x32\n\x0eSubJsonMessage\x12\x0e\n\x06sub_id\x18\x01 \x01(\x03\x12\x10\n\x08sub_name\x18\x02 \x01(\t\"G\n\x0fJsonMessageList\x12\x34\n\x10json_message_vec\x18\x01 \x03(\x0b\x32\x1a.cohesity.test.JsonMessage\"(\n\x0cJsonObjectId\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\xbd\x01\n\x17JsonListMessageResponse\x12O\n\x10json_object_list\x18\x01 \x03(\x0b\x32\x35.cohesity.test.JsonListMessageResponse.JsonObjectList\x1aQ\n\x0eJsonObjectList\x12.\n\tobject_id\x18\x01 \x01(\x0b\x32\x1b.cohesity.test.JsonObjectId\x12\x0f\n\x07tag_ids\x18\x02 \x03(\t\")\n\x0eJsonStringList\x12\x17\n\x0fjson_string_vec\x18\x01 \x03(\t\"\xc4\x01\n\x0eJsonListObject\x12U\n\x18json_string_message_list\x18\x01 \x03(\x0b\x32\x33.cohesity.test.JsonListObject.JsonStringMessageList\x1a[\n\x15JsonStringMessageList\x12.\n\tobject_id\x18\x01 \x03(\x0b\x32\x1b.cohesity.test.JsonObjectId\x12\x12\n\nstring_vec\x18\x02 \x03(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.base.test.json_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JSONMESSAGE'].fields_by_name['id_int64_as_numeric']._loaded_options = None
  _globals['_JSONMESSAGE'].fields_by_name['id_int64_as_numeric']._serialized_options = b'0\002'
  _globals['_JSONMESSAGE']._serialized_start=45
  _globals['_JSONMESSAGE']._serialized_end=394
  _globals['_JSONMESSAGE_SUBJSONMESSAGE']._serialized_start=344
  _globals['_JSONMESSAGE_SUBJSONMESSAGE']._serialized_end=394
  _globals['_JSONMESSAGELIST']._serialized_start=396
  _globals['_JSONMESSAGELIST']._serialized_end=467
  _globals['_JSONOBJECTID']._serialized_start=469
  _globals['_JSONOBJECTID']._serialized_end=509
  _globals['_JSONLISTMESSAGERESPONSE']._serialized_start=512
  _globals['_JSONLISTMESSAGERESPONSE']._serialized_end=701
  _globals['_JSONLISTMESSAGERESPONSE_JSONOBJECTLIST']._serialized_start=620
  _globals['_JSONLISTMESSAGERESPONSE_JSONOBJECTLIST']._serialized_end=701
  _globals['_JSONSTRINGLIST']._serialized_start=703
  _globals['_JSONSTRINGLIST']._serialized_end=744
  _globals['_JSONLISTOBJECT']._serialized_start=747
  _globals['_JSONLISTOBJECT']._serialized_end=943
  _globals['_JSONLISTOBJECT_JSONSTRINGMESSAGELIST']._serialized_start=852
  _globals['_JSONLISTOBJECT_JSONSTRINGMESSAGELIST']._serialized_end=943
# @@protoc_insertion_point(module_scope)
