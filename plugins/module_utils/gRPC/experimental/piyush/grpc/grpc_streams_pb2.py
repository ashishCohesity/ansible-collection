# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/piyush/grpc/grpc_streams.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/piyush/grpc/grpc_streams.proto\x12\x14\x63ohesity.echoservice\"%\n\x13\x45\x63hoNumberStreamArg\x12\x0e\n\x06number\x18\x01 \x01(\x03\"(\n\x16\x45\x63hoNumberStreamResult\x12\x0e\n\x06number\x18\x02 \x01(\x03\"\xc3\x03\n\x18\x43lientAndServerTlsConfig\x12S\n\x11server_tls_config\x18\x01 \x01(\x0b\x32\x38.cohesity.echoservice.ClientAndServerTlsConfig.TlsConfig\x12S\n\x11\x63lient_tls_config\x18\x02 \x01(\x0b\x32\x38.cohesity.echoservice.ClientAndServerTlsConfig.TlsConfig\x1a\xfc\x01\n\tTlsConfig\x12\x19\n\x11root_certificates\x18\x01 \x01(\x0c\x12_\n\x11key_cert_pair_vec\x18\x02 \x03(\x0b\x32\x44.cohesity.echoservice.ClientAndServerTlsConfig.TlsConfig.KeyCertPair\x1as\n\x0bKeyCertPair\x12\x19\n\x11\x63\x65rtificate_chain\x18\x01 \x01(\x0c\x12\x1f\n\x15\x65ncrypted_private_key\x18\x02 \x01(\x0cH\x00\x12\x15\n\x0bprivate_key\x18\x03 \x01(\x0cH\x00\x42\x11\n\x0f\x63\x65rtificate_key2}\n\x08\x45\x63hoBidi\x12q\n\x10\x45\x63hoNumberStream\x12).cohesity.echoservice.EchoNumberStreamArg\x1a,.cohesity.echoservice.EchoNumberStreamResult\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.piyush.grpc.grpc_streams_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ECHONUMBERSTREAMARG']._serialized_start=69
  _globals['_ECHONUMBERSTREAMARG']._serialized_end=106
  _globals['_ECHONUMBERSTREAMRESULT']._serialized_start=108
  _globals['_ECHONUMBERSTREAMRESULT']._serialized_end=148
  _globals['_CLIENTANDSERVERTLSCONFIG']._serialized_start=151
  _globals['_CLIENTANDSERVERTLSCONFIG']._serialized_end=602
  _globals['_CLIENTANDSERVERTLSCONFIG_TLSCONFIG']._serialized_start=350
  _globals['_CLIENTANDSERVERTLSCONFIG_TLSCONFIG']._serialized_end=602
  _globals['_CLIENTANDSERVERTLSCONFIG_TLSCONFIG_KEYCERTPAIR']._serialized_start=487
  _globals['_CLIENTANDSERVERTLSCONFIG_TLSCONFIG_KEYCERTPAIR']._serialized_end=602
  _globals['_ECHOBIDI']._serialized_start=604
  _globals['_ECHOBIDI']._serialized_end=729
# @@protoc_insertion_point(module_scope)
