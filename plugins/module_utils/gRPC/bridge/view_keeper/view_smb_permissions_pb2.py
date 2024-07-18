# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/view_keeper/view_smb_permissions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-bridge/view_keeper/view_smb_permissions.proto\x12\x14\x63ohesity.bridge.view\x1a\x1c\x63onfigs/cluster_config.proto\"\xec\x04\n\rSmbPermission\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.cohesity.bridge.view.SmbPermission.Type\x12\x36\n\x04mode\x18\x02 \x01(\x0e\x32(.cohesity.bridge.view.SmbPermission.Mode\x12:\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32*.cohesity.bridge.view.SmbPermission.Access\x12\x35\n\x03sid\x18\x04 \x02(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\x12\x14\n\x0cspecial_type\x18\x05 \x01(\x05\x12\x1b\n\x13special_access_mask\x18\x06 \x01(\r\"/\n\x04Type\x12\n\n\x06kAllow\x10\x01\x12\t\n\x05kDeny\x10\x02\x12\x10\n\x0ckSpecialType\x10\x03\"\xa7\x01\n\x04Mode\x12\x1d\n\x19kFolderSubFoldersAndFiles\x10\x01\x12\x18\n\x14kFolderAndSubFolders\x10\x02\x12\x13\n\x0fkFolderAndFiles\x10\x03\x12\x0f\n\x0bkFolderOnly\x10\x04\x12\x1b\n\x17kSubFoldersAndFilesOnly\x10\x05\x12\x13\n\x0fkSubFoldersOnly\x10\x06\x12\x0e\n\nkFilesOnly\x10\x07\"j\n\x06\x41\x63\x63\x65ss\x12\r\n\tkReadOnly\x10\x01\x12\x0e\n\nkReadWrite\x10\x02\x12\x10\n\x0ckFullControl\x10\x03\x12\x12\n\x0ekSpecialAccess\x10\x04\x12\x0b\n\x07kModify\x10\x05\x12\x0e\n\nkSuperUser\x10\x06\"\xb7\x01\n\x16ViewSmbPermissionsInfo\x12;\n\towner_sid\x18\x01 \x01(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\x12\x38\n\x0bpermissions\x18\x02 \x03(\x0b\x32#.cohesity.bridge.view.SmbPermission\x12\x0b\n\x03uid\x18\x03 \x01(\r\x12\x0b\n\x03gid\x18\x04 \x01(\r\x12\x0c\n\x04mode\x18\x05 \x01(\r\"\xa4\x03\n\x0e\x41liasSmbConfig\x12\x19\n\x11\x64iscovery_enabled\x18\x01 \x01(\x08\x12\x1a\n\x12\x65ncryption_enabled\x18\x02 \x01(\x08\x12\x1b\n\x13\x65ncryption_required\x18\x03 \x01(\x08\x12\x38\n\x0bpermissions\x18\x04 \x03(\x0b\x32#.cohesity.bridge.view.SmbPermission\x12\x17\n\x0f\x63\x61\x63hing_enabled\x18\x05 \x01(\x08\x12\'\n\x1fis_share_level_permission_empty\x18\x06 \x01(\x08\x12\x1c\n\x0eoplock_enabled\x18\x07 \x01(\x08:\x04true\x12%\n\x17\x63ontinuous_availability\x18\x08 \x01(\x08:\x04true\x12<\n\nsuperusers\x18\t \x03(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\x12?\n\rsnapshot_acls\x18\n \x03(\x0b\x32(.cohesity.configs.ClusterConfigProto.SIDB,Z*bridge/view_keeper/view_smb_permissions.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.view_keeper.view_smb_permissions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*bridge/view_keeper/view_smb_permissions.pb'
  _globals['_SMBPERMISSION']._serialized_start=102
  _globals['_SMBPERMISSION']._serialized_end=722
  _globals['_SMBPERMISSION_TYPE']._serialized_start=397
  _globals['_SMBPERMISSION_TYPE']._serialized_end=444
  _globals['_SMBPERMISSION_MODE']._serialized_start=447
  _globals['_SMBPERMISSION_MODE']._serialized_end=614
  _globals['_SMBPERMISSION_ACCESS']._serialized_start=616
  _globals['_SMBPERMISSION_ACCESS']._serialized_end=722
  _globals['_VIEWSMBPERMISSIONSINFO']._serialized_start=725
  _globals['_VIEWSMBPERMISSIONSINFO']._serialized_end=908
  _globals['_ALIASSMBCONFIG']._serialized_start=911
  _globals['_ALIASSMBCONFIG']._serialized_end=1331
# @@protoc_insertion_point(module_scope)