# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/ad/ad.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import credentials_pb2 as magneto_dot_base_dot_credentials__pb2
from magneto.base.entities import ad_pb2 as magneto_dot_base_dot_entities_dot_ad__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emagneto/connectors/ad/ad.proto\x12\x13\x63ohesity.magneto.ad\x1a\x1emagneto/base/credentials.proto\x1a\x1emagneto/base/entities/ad.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\"\xd2\x01\n\x0cSnapshotInfo\x12\x33\n\x02\x64\x63\x18\x02 \x01(\x0b\x32\'.cohesity.magneto.ad.ADDomainController\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto2`\n\x10\x61\x64_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18s \x01(\x0b\x32!.cohesity.magneto.ad.SnapshotInfo\"\xc8\x01\n\x10VerificationInfo\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x33\n\x02\x64\x63\x18\x02 \x01(\x0b\x32\'.cohesity.magneto.ad.ADDomainController2l\n\x14\x61\x64_verification_info\x12\'.cohesity.magneto.VerificationInfoProto\x18\x66 \x01(\x0b\x32%.cohesity.magneto.ad.VerificationInfo\"\x91\x08\n\x0bRestoreInfo\x12M\n\x12restore_task_state\x18\x01 \x01(\x0e\x32\x31.cohesity.magneto.ad.RestoreInfo.RestoreTaskState\x12\x11\n\tldap_port\x18\x02 \x01(\x05\x12\x18\n\x10mount_points_vec\x18\x03 \x03(\t\x12\x15\n\rbackup_job_id\x18\x04 \x01(\x03\x12\x33\n\x02\x64\x63\x18\x05 \x01(\x0b\x32\'.cohesity.magneto.ad.ADDomainController\x12\x17\n\x0f\x64samain_proc_id\x18\x06 \x01(\x05\x12V\n\x1drestore_disks_task_info_proto\x18\x07 \x01(\x0b\x32/.cohesity.magneto.SetupRestoreDiskTaskInfoProto\x12\x32\n\x0b\x63redentials\x18\x08 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x12G\n\x11\x61\x64_update_options\x18\t \x01(\x0b\x32,.cohesity.magneto.ADUpdateRestoreTaskOptions\x12@\n\x15\x61\x64_restore_status_vec\x18\n \x03(\x0b\x32!.cohesity.magneto.ADRestoreStatus\x12\x17\n\x0fnum_successfull\x18\x0b \x01(\x05\x12\x12\n\nnum_failed\x18\x0c \x01(\x05\x12\x13\n\x0bnum_running\x18\r \x01(\x05\x12\x64\n\x1cmount_and_restore_task_state\x18\x0e \x01(\x0e\x32>.cohesity.magneto.ad.RestoreInfo.MountAndRestoreTaskState.Type\x12!\n\x19is_mount_and_restore_task\x18\x0f \x01(\x08\x12\x14\n\x0c\x63\x61n_teardown\x18\x10 \x01(\x08\x12#\n\x1bsysvol_folder_absolute_path\x18\x11 \x01(\t\x1a\x63\n\x18MountAndRestoreTaskState\"G\n\x04Type\x12\x0c\n\x08kStarted\x10\x00\x12\x0c\n\x08kMounted\x10\x01\x12\x14\n\x10kObjectsRestored\x10\x02\x12\r\n\tkFinished\x10\x03\"@\n\x10RestoreTaskState\x12\x0c\n\x08kStarted\x10\x01\x12\x0f\n\x0bkVHDMounted\x10\x02\x12\r\n\tkFinished\x10\x03\x32]\n\x0f\x61\x64_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18q \x01(\x0b\x32 .cohesity.magneto.ad.RestoreInfo\"\xb3\x02\n\x0f\x44\x65stroyTaskInfo\x12\x33\n\x02\x64\x63\x18\x01 \x01(\x0b\x32\'.cohesity.magneto.ad.ADDomainController\x12\x1b\n\x0f\x64samain_proc_id\x18\x02 \x01(\x05:\x02-1\x12V\n\x1drestore_disks_task_info_proto\x18\x03 \x01(\x0b\x32/.cohesity.magneto.SetupRestoreDiskTaskInfoProto2v\n\x18\x61\x64_destroy_app_task_info\x12..cohesity.magneto.DestroyCloneAppTaskInfoProto\x18\x66 \x01(\x0b\x32$.cohesity.magneto.ad.DestroyTaskInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.ad.ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SNAPSHOTINFO']._serialized_start=174
  _globals['_SNAPSHOTINFO']._serialized_end=384
  _globals['_VERIFICATIONINFO']._serialized_start=387
  _globals['_VERIFICATIONINFO']._serialized_end=587
  _globals['_RESTOREINFO']._serialized_start=590
  _globals['_RESTOREINFO']._serialized_end=1631
  _globals['_RESTOREINFO_MOUNTANDRESTORETASKSTATE']._serialized_start=1371
  _globals['_RESTOREINFO_MOUNTANDRESTORETASKSTATE']._serialized_end=1470
  _globals['_RESTOREINFO_MOUNTANDRESTORETASKSTATE_TYPE']._serialized_start=1399
  _globals['_RESTOREINFO_MOUNTANDRESTORETASKSTATE_TYPE']._serialized_end=1470
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_start=1472
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_end=1536
  _globals['_DESTROYTASKINFO']._serialized_start=1634
  _globals['_DESTROYTASKINFO']._serialized_end=1941
# @@protoc_insertion_point(module_scope)