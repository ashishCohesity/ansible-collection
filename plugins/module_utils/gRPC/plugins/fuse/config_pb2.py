# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugins/fuse/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19plugins/fuse/config.proto\x12\x15\x63ohesity.plugins.fuse\"\xb8\x02\n\x14\x46useCertificateProto\x12[\n\x15\x63onnection_config_vec\x18\x01 \x03(\x0b\x32<.cohesity.plugins.fuse.FuseCertificateProto.ConnectionConfig\x1a\xc2\x01\n\x10\x43onnectionConfig\x12\x14\n\x0c\x63luster_cert\x18\x01 \x01(\t\x12\x11\n\tself_cert\x18\x02 \x01(\t\x12$\n\x1cself_cert_priv_key_encrypted\x18\x03 \x01(\x0c\x12\x11\n\ttenant_id\x18\x04 \x01(\t\x12\x16\n\ncluster_id\x18\x05 \x01(\x03:\x02-1\x12\x34\n\x17grpc_server_common_name\x18\x06 \x01(\t:\x13\x43ohesity Inc ServerB\x1b\n\x19\x63om.cohesity.plugins.fuse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.fuse.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cohesity.plugins.fuse'
  _globals['_FUSECERTIFICATEPROTO']._serialized_start=53
  _globals['_FUSECERTIFICATEPROTO']._serialized_end=365
  _globals['_FUSECERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_start=171
  _globals['_FUSECERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_end=365
# @@protoc_insertion_point(module_scope)
