# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/certificates.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ciris/base/certificates.proto\x12\rcohesity.iris\"\xda\x01\n\x0f\x43\x65rtificateInfo\x12\x12\n\x07version\x18\x01 \x01(\x05:\x01\x31\x12/\n\x0b\x63\x65rtificate\x18\x02 \x01(\x0b\x32\x1a.cohesity.iris.Certificate\x12:\n\thost_type\x18\x03 \x01(\x0e\x32\'.cohesity.iris.CertificateInfo.HostType\x12\x10\n\x08host_ips\x18\x04 \x03(\t\"4\n\x08HostType\x12\n\n\x06kOther\x10\x00\x12\x0e\n\nkSapOracle\x10\x01\x12\x0c\n\x08kSapHana\x10\x02\"l\n\x0b\x43\x65rtificate\x12\x16\n\x0e\x63\x65rtificate_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x17\n\x0fvalidity_period\x18\x03 \x01(\t\x12\x1b\n\x13\x63\x65rtificate_version\x18\x04 \x01(\x03\x42\x1bZ\x19iris/base/certificates.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.certificates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031iris/base/certificates.pb'
  _globals['_CERTIFICATEINFO']._serialized_start=48
  _globals['_CERTIFICATEINFO']._serialized_end=266
  _globals['_CERTIFICATEINFO_HOSTTYPE']._serialized_start=214
  _globals['_CERTIFICATEINFO_HOSTTYPE']._serialized_end=266
  _globals['_CERTIFICATE']._serialized_start=268
  _globals['_CERTIFICATE']._serialized_end=376
# @@protoc_insertion_point(module_scope)
