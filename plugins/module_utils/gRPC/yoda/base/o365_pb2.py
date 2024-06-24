# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/base/o365.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.connectors.ms_graph import graph_enums_pb2 as magneto_dot_connectors_dot_ms__graph_dot_graph__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14yoda/base/o365.proto\x12\x12\x63ohesity.yoda.base\x1a-magneto/connectors/ms_graph/graph_enums.proto\"\x86\x07\n\x12O365AddSnapshotArg\x12H\n\x0coutlook_info\x18\x01 \x01(\x0b\x32\x32.cohesity.yoda.base.O365AddSnapshotArg.OutlookInfo\x12O\n\x12one_drive_info_vec\x18\x02 \x03(\x0b\x32\x33.cohesity.yoda.base.O365AddSnapshotArg.OneDriveInfo\x12N\n\x0fsharepoint_info\x18\x03 \x01(\x0b\x32\x35.cohesity.yoda.base.O365AddSnapshotArg.SharepointInfo\x12S\n\x12public_folder_info\x18\x04 \x01(\x0b\x32\x37.cohesity.yoda.base.O365AddSnapshotArg.PublicFolderInfo\x12\x44\n\nteams_info\x18\x05 \x01(\x0b\x32\x30.cohesity.yoda.base.O365AddSnapshotArg.TeamsInfo\x12\x44\n\ngroup_info\x18\x06 \x01(\x0b\x32\x30.cohesity.yoda.base.O365AddSnapshotArg.GroupInfo\x1a\x32\n\x0bOutlookInfo\x12#\n\x14should_index_outlook\x18\x01 \x01(\x08:\x05\x66\x61lse\x1a\xe4\x01\n\x0cOneDriveInfo\x12%\n\x16should_index_one_drive\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rpath_to_index\x18\x02 \x01(\t\x12\x12\n\npath_to_db\x18\x03 \x01(\t\x12\x10\n\x08\x64rive_id\x18\x04 \x01(\t\x12$\n\x1cincremental_indexing_enabled\x18\x05 \x01(\x08\x12J\n\ndrive_type\x18\x06 \x01(\x0e\x32(.cohesity.magneto.MSGraph.DriveType.Type:\x0ckUnspecified\x1a\x39\n\x0eSharepointInfo\x12!\n\x12should_index_lists\x18\x02 \x01(\x08:\x05\x66\x61lseJ\x04\x08\x01\x10\x02\x1a\x34\n\x10PublicFolderInfo\x12 \n\x18hierarchy_db_folder_name\x18\x01 \x01(\t\x1a\x0b\n\tTeamsInfo\x1a\x0b\n\tGroupInfo\"\xba\x01\n\x16SharepointItemMetadata\x12K\n\x04type\x18\x01 \x01(\x0e\x32/.cohesity.yoda.base.SharepointItemMetadata.Type:\x0ckUnspecified\"S\n\x04Type\x12\x10\n\x0ckUnspecified\x10\x00\x12\t\n\x05kFile\x10\x01\x12\x0e\n\nkDirectory\x10\x02\x12\x0f\n\x0bkSiteDoclib\x10\x03\x12\r\n\tkSiteList\x10\x04\x42\x13Z\x11yoda/base/o365.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.base.o365_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\021yoda/base/o365.pb'
  _globals['_O365ADDSNAPSHOTARG']._serialized_start=92
  _globals['_O365ADDSNAPSHOTARG']._serialized_end=994
  _globals['_O365ADDSNAPSHOTARG_OUTLOOKINFO']._serialized_start=574
  _globals['_O365ADDSNAPSHOTARG_OUTLOOKINFO']._serialized_end=624
  _globals['_O365ADDSNAPSHOTARG_ONEDRIVEINFO']._serialized_start=627
  _globals['_O365ADDSNAPSHOTARG_ONEDRIVEINFO']._serialized_end=855
  _globals['_O365ADDSNAPSHOTARG_SHAREPOINTINFO']._serialized_start=857
  _globals['_O365ADDSNAPSHOTARG_SHAREPOINTINFO']._serialized_end=914
  _globals['_O365ADDSNAPSHOTARG_PUBLICFOLDERINFO']._serialized_start=916
  _globals['_O365ADDSNAPSHOTARG_PUBLICFOLDERINFO']._serialized_end=968
  _globals['_O365ADDSNAPSHOTARG_TEAMSINFO']._serialized_start=970
  _globals['_O365ADDSNAPSHOTARG_TEAMSINFO']._serialized_end=981
  _globals['_O365ADDSNAPSHOTARG_GROUPINFO']._serialized_start=983
  _globals['_O365ADDSNAPSHOTARG_GROUPINFO']._serialized_end=994
  _globals['_SHAREPOINTITEMMETADATA']._serialized_start=997
  _globals['_SHAREPOINTITEMMETADATA']._serialized_end=1183
  _globals['_SHAREPOINTITEMMETADATA_TYPE']._serialized_start=1100
  _globals['_SHAREPOINTITEMMETADATA_TYPE']._serialized_end=1183
# @@protoc_insertion_point(module_scope)
