# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: java/bridge/snap_fs/client/src/main/proto/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6java/bridge/snap_fs/client/src/main/proto/config.proto\x12\x1b\x63om.cohesity.bridge.snap_fs\"\xb6\x02\n\x10\x43\x65rtificateProto\x12]\n\x15\x63onnection_config_vec\x18\x01 \x03(\x0b\x32>.com.cohesity.bridge.snap_fs.CertificateProto.ConnectionConfig\x1a\xc2\x01\n\x10\x43onnectionConfig\x12\x14\n\x0c\x63luster_cert\x18\x01 \x01(\t\x12\x11\n\tself_cert\x18\x02 \x01(\t\x12$\n\x1cself_cert_priv_key_encrypted\x18\x03 \x01(\x0c\x12\x11\n\ttenant_id\x18\x04 \x01(\t\x12\x16\n\ncluster_id\x18\x05 \x01(\x03:\x02-1\x12\x34\n\x17grpc_server_common_name\x18\x06 \x01(\t:\x13\x43ohesity Inc Server\"E\n\rEncryptHeader\x12\n\n\x02iv\x18\x01 \x02(\x0c\x12\x1b\n\x13morphed_data_length\x18\x02 \x01(\x07\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x42\x1d\n\x1b\x63om.cohesity.bridge.snap_fs')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'java.bridge.snap_fs.client.src.main.proto.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cohesity.bridge.snap_fs'
  _globals['_CERTIFICATEPROTO']._serialized_start=88
  _globals['_CERTIFICATEPROTO']._serialized_end=398
  _globals['_CERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_start=204
  _globals['_CERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_end=398
  _globals['_ENCRYPTHEADER']._serialized_start=400
  _globals['_ENCRYPTHEADER']._serialized_end=469
# @@protoc_insertion_point(module_scope)