# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/base/tag_updates.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dhelios/base/tag_updates.proto\x12\x1a\x63ohesity.helios.tagupdates\"\x8f\x01\n\x16TagUpdatesKafkaMessage\x12\x12\n\ncluster_id\x18\x01 \x01(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x02 \x01(\x03\x12\x15\n\rsf_account_id\x18\x03 \x01(\t\x12\x13\n\x0btag_updates\x18\x04 \x01(\x0c\x12\x15\n\ris_compressed\x18\x05 \x01(\x08\x42\x1cZ\x1a\x63ohesity/helios/tagupdatesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.base.tag_updates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032cohesity/helios/tagupdates'
  _globals['_TAGUPDATESKAFKAMESSAGE']._serialized_start=62
  _globals['_TAGUPDATESKAFKAMESSAGE']._serialized_end=205
# @@protoc_insertion_point(module_scope)
