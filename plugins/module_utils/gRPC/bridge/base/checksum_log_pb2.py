# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/base/checksum_log.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x62ridge/base/checksum_log.proto\x12\x0f\x63ohesity.bridge\"\xd3\x02\n\x10\x43hecksumLogProto\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x17\n\x0f\x66ile_identifier\x18\x02 \x01(\t\x12\x14\n\x0cis_forwarded\x18\x03 \x01(\x08\x12:\n\tchunk_vec\x18\x04 \x03(\x0b\x32\'.cohesity.bridge.ChecksumLogProto.Chunk\x12\r\n\x05\x65rror\x18\x05 \x01(\x05\x12\x43\n\x0crequest_type\x18\x06 \x01(\x0e\x32-.cohesity.bridge.ChecksumLogProto.RequestType\x1aN\n\x05\x43hunk\x12\x0e\n\x06offset\x18\x01 \x02(\x03\x12\x0e\n\x06length\x18\x02 \x02(\x05\x12\x10\n\x08\x63hecksum\x18\x03 \x02(\x05\x12\x13\n\x0bsample_data\x18\x04 \x01(\x0c\"$\n\x0bRequestType\x12\t\n\x05kRead\x10\x00\x12\n\n\x06kWrite\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.base.checksum_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHECKSUMLOGPROTO']._serialized_start=52
  _globals['_CHECKSUMLOGPROTO']._serialized_end=391
  _globals['_CHECKSUMLOGPROTO_CHUNK']._serialized_start=275
  _globals['_CHECKSUMLOGPROTO_CHUNK']._serialized_end=353
  _globals['_CHECKSUMLOGPROTO_REQUESTTYPE']._serialized_start=355
  _globals['_CHECKSUMLOGPROTO_REQUESTTYPE']._serialized_end=391
# @@protoc_insertion_point(module_scope)
