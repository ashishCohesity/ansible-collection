# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keychain/base/key_info.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from keychain.base import keychain_pb2 as keychain_dot_base_dot_keychain__pb2
from util.base import cluster_instance_identifier_pb2 as util_dot_base_dot_cluster__instance__identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ckeychain/base/key_info.proto\x12\x11\x63ohesity.keychain\x1a\x1ckeychain/base/keychain.proto\x1a+util/base/cluster_instance_identifier.proto\"\xb7\x02\n\x0cKeyInfoProto\x12\x0e\n\x06key_id\x18\x01 \x01(\x03\x12+\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x1b.cohesity.keychain.EntityId\x12\x15\n\rkms_server_id\x18\x03 \x01(\x03\x12\x0f\n\x07key_uid\x18\x04 \x01(\x0c\x12\x0c\n\x04\x65\x64\x65k\x18\x05 \x01(\x0c\x12$\n\x1c\x64\x65k_creation_timestamp_msecs\x18\x06 \x01(\x03\x12)\n!kek_last_rotation_timestamp_msecs\x18\x07 \x01(\x03\x12\x0b\n\x03kek\x18\t \x01(\x0c\x12\x14\n\x0crandom_nonce\x18\n \x01(\x0c\x12@\n\x13\x63luster_instance_id\x18\x0b \x01(\x0b\x32#.cohesity.ClusterInstanceIdentifier\"\x8a\x01\n\x0bKeyInfoList\x12\x35\n\x0ckey_info_vec\x18\x01 \x03(\x0b\x32\x1f.cohesity.keychain.KeyInfoProto\x12\"\n\x16\x63luster_config_version\x18\x02 \x01(\x03:\x02-1\x12 \n\x14object_state_version\x18\x03 \x01(\x03:\x02-1\"\\\n\x14UploadedKeyInfoProto\x12\x0e\n\x06key_id\x18\x01 \x01(\x03\x12\x15\n\rkms_server_id\x18\x02 \x01(\x03\x12\x0f\n\x07key_uid\x18\x03 \x01(\x0c\x12\x0c\n\x04\x65\x64\x65k\x18\x04 \x01(\x0c\"\xfa\x01\n\x12UploadedKeyInfoMap\x12\\\n\x15uploaded_key_info_map\x18\x01 \x03(\x0b\x32=.cohesity.keychain.UploadedKeyInfoMap.UploadedKeyInfoMapEntry\x12\"\n\x16\x63luster_config_version\x18\x02 \x01(\x03:\x02-1\x1a\x62\n\x17UploadedKeyInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.cohesity.keychain.UploadedKeyInfoProto:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'keychain.base.key_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_UPLOADEDKEYINFOMAP_UPLOADEDKEYINFOMAPENTRY']._loaded_options = None
  _globals['_UPLOADEDKEYINFOMAP_UPLOADEDKEYINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_KEYINFOPROTO']._serialized_start=127
  _globals['_KEYINFOPROTO']._serialized_end=438
  _globals['_KEYINFOLIST']._serialized_start=441
  _globals['_KEYINFOLIST']._serialized_end=579
  _globals['_UPLOADEDKEYINFOPROTO']._serialized_start=581
  _globals['_UPLOADEDKEYINFOPROTO']._serialized_end=673
  _globals['_UPLOADEDKEYINFOMAP']._serialized_start=676
  _globals['_UPLOADEDKEYINFOMAP']._serialized_end=926
  _globals['_UPLOADEDKEYINFOMAP_UPLOADEDKEYINFOMAPENTRY']._serialized_start=828
  _globals['_UPLOADEDKEYINFOMAP_UPLOADEDKEYINFOMAPENTRY']._serialized_end=926
# @@protoc_insertion_point(module_scope)
