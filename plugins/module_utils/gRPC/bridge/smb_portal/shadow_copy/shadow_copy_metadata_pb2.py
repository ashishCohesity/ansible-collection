# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/smb_portal/shadow_copy/shadow_copy_metadata.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8bridge/smb_portal/shadow_copy/shadow_copy_metadata.proto\x12\x13\x63ohesity.bridge.smb\"\xec\x06\n\x12ShadowCopySetProto\x12#\n\x1bserver_shadow_copy_set_guid\x18\x01 \x01(\t\x12>\n\x06status\x18\x02 \x01(\x0e\x32..cohesity.bridge.smb.ShadowCopySetProto.Status\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\x03\x12\x15\n\rfsrvp_version\x18\x04 \x01(\x03\x12S\n\x0fshadow_copy_map\x18\x05 \x03(\x0b\x32:.cohesity.bridge.smb.ShadowCopySetProto.ShadowCopyMapEntry\x1a]\n\x13ShadowShareMapProto\x12\x12\n\nshare_name\x18\x01 \x01(\t\x12\x1e\n\x16shadow_copy_share_name\x18\x02 \x01(\t\x12\x12\n\nis_exposed\x18\x03 \x01(\x08\x1a\xba\x02\n\x0fShadowCopyProto\x12\x1f\n\x17server_shadow_copy_guid\x18\x01 \x01(\t\x12\x11\n\tview_name\x18\x02 \x01(\t\x12\x0f\n\x07view_id\x18\x03 \x01(\x03\x12\x1a\n\x12\x63reation_timestamp\x18\x04 \x01(\x03\x12X\n\tshare_map\x18\x05 \x03(\x0b\x32\x45.cohesity.bridge.smb.ShadowCopySetProto.ShadowCopyProto.ShareMapEntry\x1al\n\rShareMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.cohesity.bridge.smb.ShadowCopySetProto.ShadowShareMapProto:\x02\x38\x01\x1am\n\x12ShadowCopyMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.cohesity.bridge.smb.ShadowCopySetProto.ShadowCopyProto:\x02\x38\x01\"i\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\n\n\x06kAdded\x10\x01\x12\x17\n\x13kCreationInProgress\x10\x02\x12\x0e\n\nkCommitted\x10\x03\x12\x0c\n\x08kExposed\x10\x04\x12\x0e\n\nkRecovered\x10\x05\"\xb5\x01\n\x19ShadowCopySetContextProto\x12\x17\n\x0f\x63urrent_context\x18\x01 \x01(\r\x12\x1a\n\x12\x63lient_retry_count\x18\x02 \x01(\x03\x12\x19\n\x11\x63ontext_timestamp\x18\x03 \x01(\x03\x12H\n\x17\x63urrent_shadow_copy_set\x18\x04 \x01(\x0b\x32\'.cohesity.bridge.smb.ShadowCopySetProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.smb_portal.shadow_copy.shadow_copy_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO_SHAREMAPENTRY']._loaded_options = None
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO_SHAREMAPENTRY']._serialized_options = b'8\001'
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYMAPENTRY']._loaded_options = None
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYMAPENTRY']._serialized_options = b'8\001'
  _globals['_SHADOWCOPYSETPROTO']._serialized_start=82
  _globals['_SHADOWCOPYSETPROTO']._serialized_end=958
  _globals['_SHADOWCOPYSETPROTO_SHADOWSHAREMAPPROTO']._serialized_start=330
  _globals['_SHADOWCOPYSETPROTO_SHADOWSHAREMAPPROTO']._serialized_end=423
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO']._serialized_start=426
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO']._serialized_end=740
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO_SHAREMAPENTRY']._serialized_start=632
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYPROTO_SHAREMAPENTRY']._serialized_end=740
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYMAPENTRY']._serialized_start=742
  _globals['_SHADOWCOPYSETPROTO_SHADOWCOPYMAPENTRY']._serialized_end=851
  _globals['_SHADOWCOPYSETPROTO_STATUS']._serialized_start=853
  _globals['_SHADOWCOPYSETPROTO_STATUS']._serialized_end=958
  _globals['_SHADOWCOPYSETCONTEXTPROTO']._serialized_start=961
  _globals['_SHADOWCOPYSETCONTEXTPROTO']._serialized_end=1142
# @@protoc_insertion_point(module_scope)
