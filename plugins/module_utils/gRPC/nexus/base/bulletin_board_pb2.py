# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/bulletin_board.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fnexus/base/bulletin_board.proto\x12\x13\x63ohesity.nexus.base\"\xe9\x05\n\rBulletinProto\x12\x37\n\x07row_vec\x18\x01 \x03(\x0b\x32&.cohesity.nexus.base.BulletinProto.Row\x1a\xae\x01\n\nStateValue\x12\x13\n\x0bpackage_url\x18\x01 \x01(\t\x12\x1f\n\x17target_software_version\x18\x02 \x01(\t\x12=\n\x04type\x18\x03 \x01(\x0e\x32/.cohesity.nexus.base.BulletinProto.AppStateType\x12\x12\n\x06\x61pp_id\x18\x04 \x01(\x05\x42\x02\x18\x01\x12\x17\n\x0b\x61pp_version\x18\x05 \x01(\x05\x42\x02\x18\x01\x1a\x41\n\x0b\x43lusterInfo\x12\x12\n\ncluster_id\x18\x01 \x02(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x02 \x02(\x03\x1a\x35\n\x08UserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sid\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x1a\x98\x02\n\x03Row\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.cohesity.nexus.base.BulletinProto.StateType\x12<\n\x05state\x18\x02 \x01(\x0b\x32-.cohesity.nexus.base.BulletinProto.StateValue\x12\x43\n\x0b\x63luster_vec\x18\x03 \x03(\x0b\x32..cohesity.nexus.base.BulletinProto.ClusterInfo\x12\x17\n\x0ftimestamp_msecs\x18\x04 \x01(\x03\x12\x39\n\x04user\x18\x05 \x01(\x0b\x32+.cohesity.nexus.base.BulletinProto.UserInfo\"1\n\tStateType\x12\x13\n\x0fkClusterVersion\x10\x01\x12\x0f\n\x0bkAppVersion\x10\x02\"&\n\x0c\x41ppStateType\x12\x08\n\x04kGet\x10\x01\x12\x0c\n\x08kInstall\x10\x02\x42\x1eZ\x1cnexus/base/bulletin_board.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.bulletin_board_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034nexus/base/bulletin_board.pb'
  _globals['_BULLETINPROTO_STATEVALUE'].fields_by_name['app_id']._loaded_options = None
  _globals['_BULLETINPROTO_STATEVALUE'].fields_by_name['app_id']._serialized_options = b'\030\001'
  _globals['_BULLETINPROTO_STATEVALUE'].fields_by_name['app_version']._loaded_options = None
  _globals['_BULLETINPROTO_STATEVALUE'].fields_by_name['app_version']._serialized_options = b'\030\001'
  _globals['_BULLETINPROTO']._serialized_start=57
  _globals['_BULLETINPROTO']._serialized_end=802
  _globals['_BULLETINPROTO_STATEVALUE']._serialized_start=132
  _globals['_BULLETINPROTO_STATEVALUE']._serialized_end=306
  _globals['_BULLETINPROTO_CLUSTERINFO']._serialized_start=308
  _globals['_BULLETINPROTO_CLUSTERINFO']._serialized_end=373
  _globals['_BULLETINPROTO_USERINFO']._serialized_start=375
  _globals['_BULLETINPROTO_USERINFO']._serialized_end=428
  _globals['_BULLETINPROTO_ROW']._serialized_start=431
  _globals['_BULLETINPROTO_ROW']._serialized_end=711
  _globals['_BULLETINPROTO_STATETYPE']._serialized_start=713
  _globals['_BULLETINPROTO_STATETYPE']._serialized_end=762
  _globals['_BULLETINPROTO_APPSTATETYPE']._serialized_start=764
  _globals['_BULLETINPROTO_APPSTATETYPE']._serialized_end=802
# @@protoc_insertion_point(module_scope)