# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/base/liveness.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x62ridge/base/liveness.proto\x12\x0f\x63ohesity.bridge\"\x8e\x03\n\rLivenessProto\x12\x0e\n\x02ip\x18\x01 \x02(\tB\x02\x18\x01\x12N\n\x15network_interface_vec\x18\n \x03(\x0b\x32/.cohesity.bridge.LivenessProto.NetworkInterface\x12\x0c\n\x04port\x18\x02 \x02(\x05\x12\x0f\n\x07node_id\x18\x03 \x02(\x03\x12\x12\n\nhydra_port\x18\x05 \x01(\x05\x12 \n\x10\x62ridge_namespace\x18\x04 \x01(\t:\x06\x62ridge\x12*\n\x15\x62ridge_disk_namespace\x18\x06 \x01(\t:\x0b\x62ridge_disk\x12\x1f\n\x17publishes_disk_liveness\x18\x07 \x01(\x08\x12,\n\x16\x62ridge_proxy_namespace\x18\x08 \x01(\t:\x0c\x62ridge_proxy\x12\x19\n\x11\x62ridge_proxy_port\x18\t \x01(\x05\x1a\x32\n\x10NetworkInterface\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x12\n\nspeed_mbps\x18\x02 \x02(\x03\x42\x15\n\x13\x63om.cohesity.bridge')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.base.liveness_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.cohesity.bridge'
  _globals['_LIVENESSPROTO'].fields_by_name['ip']._loaded_options = None
  _globals['_LIVENESSPROTO'].fields_by_name['ip']._serialized_options = b'\030\001'
  _globals['_LIVENESSPROTO']._serialized_start=48
  _globals['_LIVENESSPROTO']._serialized_end=446
  _globals['_LIVENESSPROTO_NETWORKINTERFACE']._serialized_start=396
  _globals['_LIVENESSPROTO_NETWORKINTERFACE']._serialized_end=446
# @@protoc_insertion_point(module_scope)
