# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/nfs_portal/auth/kerberos/keytab_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3bridge/nfs_portal/auth/kerberos/keytab_config.proto\x12!cohesity.bridge.nfs.auth.kerberos\"%\n\x0bKeytabProto\x12\x16\n\x0ekeytab_content\x18\x01 \x01(\t\"\xe2\x01\n\x11KeytabConfigProto\x12\x65\n\x12realm_2_keytab_map\x18\x01 \x03(\x0b\x32I.cohesity.bridge.nfs.auth.kerberos.KeytabConfigProto.Realm2KeytabMapEntry\x1a\x66\n\x14Realm2KeytabMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..cohesity.bridge.nfs.auth.kerberos.KeytabProto:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.nfs_portal.auth.kerberos.keytab_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KEYTABCONFIGPROTO_REALM2KEYTABMAPENTRY']._loaded_options = None
  _globals['_KEYTABCONFIGPROTO_REALM2KEYTABMAPENTRY']._serialized_options = b'8\001'
  _globals['_KEYTABPROTO']._serialized_start=90
  _globals['_KEYTABPROTO']._serialized_end=127
  _globals['_KEYTABCONFIGPROTO']._serialized_start=130
  _globals['_KEYTABCONFIGPROTO']._serialized_end=356
  _globals['_KEYTABCONFIGPROTO_REALM2KEYTABMAPENTRY']._serialized_start=254
  _globals['_KEYTABCONFIGPROTO_REALM2KEYTABMAPENTRY']._serialized_end=356
# @@protoc_insertion_point(module_scope)
