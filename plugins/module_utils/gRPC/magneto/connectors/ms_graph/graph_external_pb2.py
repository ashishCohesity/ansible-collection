# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/ms_graph/graph_external.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0magneto/connectors/ms_graph/graph_external.proto\x12\x18\x63ohesity.magneto.MSGraph\";\n\x08Identity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"J\n\x12SharepointIdentity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\nlogin_name\x18\x03 \x01(\t\"\xe1\x02\n\x0bIdentitySet\x12\x37\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x32\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x30\n\x04user\x18\x03 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x31\n\x05owner\x18\x04 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x38\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x46\n\x1a\x63onversation_identity_type\x18\x06 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\"\xec\x02\n\x15SharepointIdentitySet\x12\x37\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x32\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x31\n\x05group\x18\x03 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12\x30\n\x04user\x18\x04 \x01(\x0b\x32\".cohesity.magneto.MSGraph.Identity\x12@\n\nsite_group\x18\x05 \x01(\x0b\x32,.cohesity.magneto.MSGraph.SharepointIdentity\x12?\n\tsite_user\x18\x06 \x01(\x0b\x32,.cohesity.magneto.MSGraph.SharepointIdentity\"\xb3\x01\n\x16O365ErrorDBReportEntry\x12R\n\x0e\x64rive_info_vec\x18\x01 \x03(\x0b\x32:.cohesity.magneto.MSGraph.O365ErrorDBReportEntry.DriveInfo\x1a\x45\n\tDriveInfo\x12\x10\n\x08\x64rive_id\x18\x01 \x01(\t\x12\x12\n\ndrive_name\x18\x02 \x01(\t\x12\x12\n\nnum_errors\x18\x03 \x01(\x03\x42/Z-magneto/connectors/ms_graph/graph_external.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.ms_graph.graph_external_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-magneto/connectors/ms_graph/graph_external.pb'
  _globals['_IDENTITY']._serialized_start=78
  _globals['_IDENTITY']._serialized_end=137
  _globals['_SHAREPOINTIDENTITY']._serialized_start=139
  _globals['_SHAREPOINTIDENTITY']._serialized_end=213
  _globals['_IDENTITYSET']._serialized_start=216
  _globals['_IDENTITYSET']._serialized_end=569
  _globals['_SHAREPOINTIDENTITYSET']._serialized_start=572
  _globals['_SHAREPOINTIDENTITYSET']._serialized_end=936
  _globals['_O365ERRORDBREPORTENTRY']._serialized_start=939
  _globals['_O365ERRORDBREPORTENTRY']._serialized_end=1118
  _globals['_O365ERRORDBREPORTENTRY_DRIVEINFO']._serialized_start=1049
  _globals['_O365ERRORDBREPORTENTRY_DRIVEINFO']._serialized_end=1118
# @@protoc_insertion_point(module_scope)
