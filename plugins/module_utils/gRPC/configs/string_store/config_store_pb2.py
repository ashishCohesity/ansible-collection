# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/string_store/config_store.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'configs/string_store/config_store.proto\x12\x10\x63ohesity.configs\"\x9a\x01\n\nConfigItem\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x15\n\x0bint32_value\x18\x03 \x01(\x05H\x00\x12\x15\n\x0bint64_value\x18\x04 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x42\x0b\n\tValueType\"^\n\x11TenantConfigProto\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x36\n\x10\x63onfig_item_list\x18\x02 \x03(\x0b\x32\x1c.cohesity.configs.ConfigItem\"}\n\x16TenantScopeConfigProto\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x11\n\tsub_scope\x18\x02 \x01(\t\x12?\n\x12tenant_config_list\x18\x03 \x03(\x0b\x32#.cohesity.configs.TenantConfigProto\"u\n\x17\x43lusterScopeConfigProto\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x11\n\tsub_scope\x18\x02 \x01(\t\x12\x36\n\x10\x63onfig_item_list\x18\x03 \x03(\x0b\x32\x1c.cohesity.configs.ConfigItemb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.string_store.config_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONFIGITEM']._serialized_start=62
  _globals['_CONFIGITEM']._serialized_end=216
  _globals['_TENANTCONFIGPROTO']._serialized_start=218
  _globals['_TENANTCONFIGPROTO']._serialized_end=312
  _globals['_TENANTSCOPECONFIGPROTO']._serialized_start=314
  _globals['_TENANTSCOPECONFIGPROTO']._serialized_end=439
  _globals['_CLUSTERSCOPECONFIGPROTO']._serialized_start=441
  _globals['_CLUSTERSCOPECONFIGPROTO']._serialized_end=558
# @@protoc_insertion_point(module_scope)