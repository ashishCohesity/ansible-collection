# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/misc/bridge_auth_token.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import service_auth_config_pb2 as configs_dot_service__auth__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&open_util/misc/bridge_auth_token.proto\x12\rcohesity.misc\x1a!configs/service_auth_config.proto\"\xed\x01\n\x0e\x41uthTokenProto\x12\x12\n\x07version\x18\x01 \x01(\x05:\x01\x31\x12\x15\n\rcreation_time\x18\x02 \x01(\x03\x12\x18\n\x10\x65ncrypted_secret\x18\x03 \x01(\x0c\x12P\n\x06\x63lient\x18\x04 \x01(\x0e\x32\x38.cohesity.configs.ServiceAuthConfigProto.ClientComponent:\x06kOther\x12\x44\n\tclient_id\x18\x05 \x01(\x0b\x32\x31.cohesity.configs.ServiceAuthConfigProto.ClientID')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.misc.bridge_auth_token_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUTHTOKENPROTO']._serialized_start=93
  _globals['_AUTHTOKENPROTO']._serialized_end=330
# @@protoc_insertion_point(module_scope)
