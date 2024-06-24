# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/sessions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18iris/base/sessions.proto\x12\rcohesity.iris\"\xa8\x01\n\x07Session\x12\x12\n\x07version\x18\x01 \x01(\x05:\x01\x31\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x39\n\x13user_session_claims\x18\x03 \x01(\x0b\x32\x1c.cohesity.iris.SessionClaims\x12\x1a\n\x12\x63reated_time_msecs\x18\x05 \x01(\x03\x12\x1e\n\x16last_access_time_msecs\x18\x06 \x01(\x03\"\xfd\x02\n\rSessionClaims\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x0e\n\x06\x64omain\x18\x04 \x01(\t\x12\x11\n\ttenant_id\x18\x05 \x01(\t\x12\x0b\n\x03sid\x18\x06 \x01(\t\x12\x11\n\tsids_hash\x18\x07 \x01(\t\x12\x11\n\troles_str\x18\x08 \x01(\t\x12\x16\n\x0eprivileges_str\x18\t \x01(\t\x12\x12\n\naccount_id\x18\n \x01(\t\x12\x0f\n\x07user_id\x18\x0b \x01(\t\x12\x12\n\nin_cluster\x18\x0c \x01(\x08\x12\x0e\n\x06locale\x18\r \x01(\t\x12\x13\n\x0b\x65xpiry_time\x18\x0e \x01(\x03\x12\x11\n\tauth_type\x18\x0f \x01(\x05\x12\x12\n\nidp_groups\x18\x10 \x03(\t\x12\x0e\n\x06idp_id\x18\x11 \x01(\x03\x12\x13\n\x0bidp_user_id\x18\x12 \x01(\t\x12\x1b\n\x13\x63luster_identifiers\x18\x13 \x01(\tB\x17Z\x15iris/base/sessions.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.sessions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025iris/base/sessions.pb'
  _globals['_SESSION']._serialized_start=44
  _globals['_SESSION']._serialized_end=212
  _globals['_SESSIONCLAIMS']._serialized_start=215
  _globals['_SESSIONCLAIMS']._serialized_end=596
# @@protoc_insertion_point(module_scope)
