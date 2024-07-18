# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/object_backup_archival.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import object_protection_pb2 as magneto_dot_api_dot_object__protection__pb2
from magneto.master.base import master_pb2 as magneto_dot_master_dot_base_dot_master__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import permissions_pb2 as magneto_dot_base_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0magneto/master/base/object_backup_archival.proto\x12\x17\x63ohesity.magneto.master\x1a#magneto/api/object_protection.proto\x1a magneto/master/base/master.proto\x1a\x19magneto/base/entity.proto\x1a\x1emagneto/base/permissions.proto\"\xe6\x01\n\x1cInternalBackupRunArchiveInfo\x12\x37\n\tspec_info\x18\x01 \x01(\x0b\x32$.cohesity.magneto.api.ObjectSpecInfo\x12\x42\n\rspec_metadata\x18\x02 \x01(\x0b\x32+.cohesity.magneto.master.ObjectSpecMetadata\x12I\n\x10\x62\x61\x63kup_run_state\x18\x03 \x01(\x0b\x32/.cohesity.magneto.master.BackupJobRunStateProto\"\x86\x03\n\x12ObjectSpecMetadata\x12-\n\x06\x65ntity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x34\n\rparent_source\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x37\n\x10\x65h_parent_source\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12*\n\"last_pause_modification_time_usecs\x18\x03 \x01(\x03\x12\x1c\n\x14required_feature_vec\x18\x05 \x03(\t\x12\x46\n\x16\x65ntity_permission_info\x18\x06 \x01(\x0b\x32&.cohesity.magneto.EntityPermissionInfo\x12@\n\x19\x61uto_protect_owner_entity\x18\x07 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.object_backup_archival_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INTERNALBACKUPRUNARCHIVEINFO']._serialized_start=208
  _globals['_INTERNALBACKUPRUNARCHIVEINFO']._serialized_end=438
  _globals['_OBJECTSPECMETADATA']._serialized_start=441
  _globals['_OBJECTSPECMETADATA']._serialized_end=831
# @@protoc_insertion_point(module_scope)