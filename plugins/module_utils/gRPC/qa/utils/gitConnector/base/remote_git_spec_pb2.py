# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/utils/gitConnector/base/remote_git_spec.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0qa/utils/gitConnector/base/remote_git_spec.proto\x12\x19\x63ohesity.qa.git_connector\"M\n\x11RemoteCredentials\x12\x1a\n\x08username\x18\x01 \x02(\t:\x08\x63ohesity\x12\x1c\n\x08password\x18\x02 \x02(\t:\nfr8shst8rt\"m\n\x16RemoteConnectionParams\x12\x10\n\x08\x65ndpoint\x18\x01 \x02(\t\x12\x41\n\x0bremote_cred\x18\x02 \x02(\x0b\x32,.cohesity.qa.git_connector.RemoteCredentials\"b\n\tGitRemote\x12\x42\n\x07machine\x18\x01 \x02(\x0b\x32\x31.cohesity.qa.git_connector.RemoteConnectionParams\x12\x11\n\tbase_path\x18\x02 \x02(\tB/Z-qa/utils/gitConnector/base/remote_git_spec.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.utils.gitConnector.base.remote_git_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-qa/utils/gitConnector/base/remote_git_spec.pb'
  _globals['_REMOTECREDENTIALS']._serialized_start=79
  _globals['_REMOTECREDENTIALS']._serialized_end=156
  _globals['_REMOTECONNECTIONPARAMS']._serialized_start=158
  _globals['_REMOTECONNECTIONPARAMS']._serialized_end=267
  _globals['_GITREMOTE']._serialized_start=269
  _globals['_GITREMOTE']._serialized_end=367
# @@protoc_insertion_point(module_scope)
