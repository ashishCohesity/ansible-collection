# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/api/common/uda.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cmagneto/api/common/uda.proto\x12\x18\x63ohesity.magneto.api.uda\";\n\x11UdaCustomArgument\x12\r\n\x05value\x18\x01 \x01(\t\x12\x17\n\x0f\x65ncrypted_value\x18\x02 \x01(\x0c\"=\n\x1aUdaBackupSourceParamsProto\x12\x1f\n\x17\x65xcluded_object_ids_vec\x18\x01 \x03(\x03\"\xf3\x02\n\x14\x45nvBackupParamsProto\x12k\n\x18\x62\x61\x63kup_job_arguments_map\x18\x01 \x03(\x0b\x32I.cohesity.magneto.api.uda.EnvBackupParamsProto.BackupJobArgumentsMapEntry\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\x05\x12\x0e\n\x06mounts\x18\x03 \x01(\x05\x12\x1c\n\x10\x66ull_backup_args\x18\x04 \x01(\tB\x02\x18\x01\x12#\n\x17incremental_backup_args\x18\x05 \x01(\tB\x02\x18\x01\x12\x1b\n\x0flog_backup_args\x18\x06 \x01(\tB\x02\x18\x01\x1ai\n\x1a\x42\x61\x63kupJobArgumentsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.cohesity.magneto.api.uda.UdaCustomArgument:\x02\x38\x01\x42\x1aZ\x18\x63ohesity/magneto/api/uda')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.api.common.uda_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/magneto/api/uda'
  _globals['_ENVBACKUPPARAMSPROTO_BACKUPJOBARGUMENTSMAPENTRY']._loaded_options = None
  _globals['_ENVBACKUPPARAMSPROTO_BACKUPJOBARGUMENTSMAPENTRY']._serialized_options = b'8\001'
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['full_backup_args']._loaded_options = None
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['full_backup_args']._serialized_options = b'\030\001'
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['incremental_backup_args']._loaded_options = None
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['incremental_backup_args']._serialized_options = b'\030\001'
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['log_backup_args']._loaded_options = None
  _globals['_ENVBACKUPPARAMSPROTO'].fields_by_name['log_backup_args']._serialized_options = b'\030\001'
  _globals['_UDACUSTOMARGUMENT']._serialized_start=58
  _globals['_UDACUSTOMARGUMENT']._serialized_end=117
  _globals['_UDABACKUPSOURCEPARAMSPROTO']._serialized_start=119
  _globals['_UDABACKUPSOURCEPARAMSPROTO']._serialized_end=180
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_start=183
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_end=554
  _globals['_ENVBACKUPPARAMSPROTO_BACKUPJOBARGUMENTSMAPENTRY']._serialized_start=449
  _globals['_ENVBACKUPPARAMSPROTO_BACKUPJOBARGUMENTSMAPENTRY']._serialized_end=554
# @@protoc_insertion_point(module_scope)