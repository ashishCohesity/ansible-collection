# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: java/plugins/mysql/agent/src/main/proto/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4java/plugins/mysql/agent/src/main/proto/config.proto\x12\x1a\x63om.cohesity.plugins.agent\"\x9b\x02\n\x12MysqlMetadataProto\x12R\n\x0f\x62\x61\x63kup_info_vec\x18\x01 \x03(\x0b\x32\x39.com.cohesity.plugins.agent.MysqlMetadataProto.BackupInfo\x1a\xb0\x01\n\nBackupInfo\x12L\n\x04type\x18\x01 \x01(\x0e\x32>.com.cohesity.plugins.agent.MysqlMetadataProto.BackupInfo.Type\x12\x19\n\x11\x62\x61\x63kup_image_name\x18\x02 \x01(\t\"9\n\x04Type\x12\t\n\x05kFull\x10\x01\x12\x10\n\x0ckIncremental\x10\x02\x12\x08\n\x04kLog\x10\x03\x12\n\n\x06kOther\x10\x04\"\xdc\x02\n\x16SybaseAseMetadataProto\x12V\n\x0f\x62\x61\x63kup_info_vec\x18\x01 \x03(\x0b\x32=.com.cohesity.plugins.agent.SybaseAseMetadataProto.BackupInfo\x1a\xe9\x01\n\nBackupInfo\x12P\n\x04type\x18\x01 \x01(\x0e\x32\x42.com.cohesity.plugins.agent.SybaseAseMetadataProto.BackupInfo.Type\x12\x19\n\x11\x62\x61\x63kup_image_name\x18\x02 \x01(\t\x12\x16\n\x0e\x62\x61\x63kup_streams\x18\x03 \x01(\x05\x12\x1b\n\x13\x62\x61\x63kup_instant_time\x18\x04 \x01(\t\"9\n\x04Type\x12\t\n\x05kFull\x10\x01\x12\x10\n\x0ckIncremental\x10\x02\x12\x08\n\x04kLog\x10\x03\x12\n\n\x06kOther\x10\x04\x42\x1c\n\x1a\x63om.cohesity.plugins.agent')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'java.plugins.mysql.agent.src.main.proto.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cohesity.plugins.agent'
  _globals['_MYSQLMETADATAPROTO']._serialized_start=85
  _globals['_MYSQLMETADATAPROTO']._serialized_end=368
  _globals['_MYSQLMETADATAPROTO_BACKUPINFO']._serialized_start=192
  _globals['_MYSQLMETADATAPROTO_BACKUPINFO']._serialized_end=368
  _globals['_MYSQLMETADATAPROTO_BACKUPINFO_TYPE']._serialized_start=311
  _globals['_MYSQLMETADATAPROTO_BACKUPINFO_TYPE']._serialized_end=368
  _globals['_SYBASEASEMETADATAPROTO']._serialized_start=371
  _globals['_SYBASEASEMETADATAPROTO']._serialized_end=719
  _globals['_SYBASEASEMETADATAPROTO_BACKUPINFO']._serialized_start=486
  _globals['_SYBASEASEMETADATAPROTO_BACKUPINFO']._serialized_end=719
  _globals['_SYBASEASEMETADATAPROTO_BACKUPINFO_TYPE']._serialized_start=311
  _globals['_SYBASEASEMETADATAPROTO_BACKUPINFO_TYPE']._serialized_end=368
# @@protoc_insertion_point(module_scope)
