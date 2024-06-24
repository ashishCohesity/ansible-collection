# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/form/form_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63onfigs/form/form_config.proto\x12\x15\x63ohesity.configs.form\"\xd1\t\n\tFormField\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tlabel_key\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x38\n\x04type\x18\x04 \x01(\x0e\x32*.cohesity.configs.form.FormField.FieldType\x12\x44\n\rstring_config\x18\x05 \x01(\x0b\x32-.cohesity.configs.form.FormField.StringConfig\x12\x46\n\x0e\x62oolean_config\x18\x06 \x01(\x0b\x32..cohesity.configs.form.FormField.BooleanConfig\x12\x44\n\rnumber_config\x18\x07 \x01(\x0b\x32-.cohesity.configs.form.FormField.NumberConfig\x12M\n\x12radio_group_config\x18\x08 \x01(\x0b\x32\x31.cohesity.configs.form.FormField.RadioGroupConfig\x12H\n\x0fpassword_config\x18\t \x01(\x0b\x32/.cohesity.configs.form.FormField.PasswordConfig\x1ai\n\x0cStringConfig\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\x15\n\rdefault_value\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65scription_key\x18\x03 \x01(\t\x12\x17\n\x0fplaceholder_key\x18\x04 \x01(\t\x1aT\n\x0ePasswordConfig\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\x17\n\x0f\x64\x65scription_key\x18\x03 \x01(\t\x12\x17\n\x0fplaceholder_key\x18\x04 \x01(\t\x1a?\n\rBooleanConfig\x12\x15\n\rdefault_value\x18\x01 \x01(\x08\x12\x17\n\x0f\x64\x65scription_key\x18\x02 \x01(\t\x1a\x97\x01\n\x0cNumberConfig\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\x15\n\rdefault_value\x18\x02 \x01(\t\x12\x15\n\rminimum_value\x18\x03 \x01(\t\x12\x15\n\rmaximum_value\x18\x04 \x01(\t\x12\x17\n\x0f\x64\x65scription_key\x18\x05 \x01(\t\x12\x17\n\x0fplaceholder_key\x18\x06 \x01(\t\x1a\xff\x01\n\x10RadioGroupConfig\x12\x10\n\x08required\x18\x01 \x01(\x08\x12T\n\rradio_buttons\x18\x02 \x03(\x0b\x32=.cohesity.configs.form.FormField.RadioGroupConfig.RadioButton\x12\x15\n\rdefault_value\x18\x03 \x01(\t\x1al\n\x0bRadioButton\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tlabel_key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12/\n\x05panel\x18\x04 \x01(\x0b\x32 .cohesity.configs.form.FormPanel\"S\n\tFieldType\x12\x0b\n\x07KString\x10\x01\x12\x0c\n\x08KBoolean\x10\x02\x12\x0b\n\x07KNumber\x10\x03\x12\x0f\n\x0bKRadioGroup\x10\x04\x12\r\n\tKPassword\x10\x05\"n\n\tFormPanel\x12\n\n\x02id\x18\x04 \x01(\t\x12\x10\n\x08optional\x18\x01 \x01(\x08\x12\x11\n\ttitle_key\x18\x02 \x01(\t\x12\x30\n\x06\x66ields\x18\x03 \x03(\x0b\x32 .cohesity.configs.form.FormFieldB\x1dZ\x1b\x63onfigs/form/form_config.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.form.form_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033configs/form/form_config.pb'
  _globals['_FORMFIELD']._serialized_start=58
  _globals['_FORMFIELD']._serialized_end=1291
  _globals['_FORMFIELD_STRINGCONFIG']._serialized_start=538
  _globals['_FORMFIELD_STRINGCONFIG']._serialized_end=643
  _globals['_FORMFIELD_PASSWORDCONFIG']._serialized_start=645
  _globals['_FORMFIELD_PASSWORDCONFIG']._serialized_end=729
  _globals['_FORMFIELD_BOOLEANCONFIG']._serialized_start=731
  _globals['_FORMFIELD_BOOLEANCONFIG']._serialized_end=794
  _globals['_FORMFIELD_NUMBERCONFIG']._serialized_start=797
  _globals['_FORMFIELD_NUMBERCONFIG']._serialized_end=948
  _globals['_FORMFIELD_RADIOGROUPCONFIG']._serialized_start=951
  _globals['_FORMFIELD_RADIOGROUPCONFIG']._serialized_end=1206
  _globals['_FORMFIELD_RADIOGROUPCONFIG_RADIOBUTTON']._serialized_start=1098
  _globals['_FORMFIELD_RADIOGROUPCONFIG_RADIOBUTTON']._serialized_end=1206
  _globals['_FORMFIELD_FIELDTYPE']._serialized_start=1208
  _globals['_FORMFIELD_FIELDTYPE']._serialized_end=1291
  _globals['_FORMPANEL']._serialized_start=1293
  _globals['_FORMPANEL']._serialized_end=1403
# @@protoc_insertion_point(module_scope)
