# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/services/vip_service/vip_epoch.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*nexus/services/vip_service/vip_epoch.proto\x12\x1b\x63ohesity.nexus.services.vip\x1a\x1copen_util/net/protorpc.proto\"&\n\x08VipEpoch\x12\x0b\n\x03vip\x18\x01 \x02(\t\x12\r\n\x05\x65poch\x18\x02 \x01(\x03\"O\n\x12LocalVipEpochProto\x12\x39\n\nvip_epochs\x18\x01 \x03(\x0b\x32%.cohesity.nexus.services.vip.VipEpoch\"\x13\n\x11ReloadVipEpochArg\"\x16\n\x14ReloadVipEpochResult2\x92\x01\n\nRpcService\x12u\n\x0eReloadVipEpoch\x12..cohesity.nexus.services.vip.ReloadVipEpochArg\x1a\x31.cohesity.nexus.services.vip.ReloadVipEpochResult\"\x00\x1a\r\x80\xf1\x04\x90N\x88\xf1\x04\x01\x90\xf1\x04\x06\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.services.vip_service.vip_epoch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\220N\210\361\004\001\220\361\004\006'
  _globals['_VIPEPOCH']._serialized_start=105
  _globals['_VIPEPOCH']._serialized_end=143
  _globals['_LOCALVIPEPOCHPROTO']._serialized_start=145
  _globals['_LOCALVIPEPOCHPROTO']._serialized_end=224
  _globals['_RELOADVIPEPOCHARG']._serialized_start=226
  _globals['_RELOADVIPEPOCHARG']._serialized_end=245
  _globals['_RELOADVIPEPOCHRESULT']._serialized_start=247
  _globals['_RELOADVIPEPOCHRESULT']._serialized_end=269
  _globals['_RPCSERVICE']._serialized_start=272
  _globals['_RPCSERVICE']._serialized_end=418
# @@protoc_insertion_point(module_scope)
