# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/util/work_item.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19yoda/util/work_item.proto\x12\x12\x63ohesity.yoda.util\"\x85\x01\n\x08WorkItem\x12\x1f\n\x17\x44\x45PRECATED_partition_id\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x15\n\rarrival_usecs\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x05\x12\x14\n\x0cpartition_id\x18\x05 \x01(\t*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x42\x1aH\x02Z\x16yoda/util/work_item.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.util.work_item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\002Z\026yoda/util/work_item.pb'
  _globals['_WORKITEM']._serialized_start=50
  _globals['_WORKITEM']._serialized_end=183
# @@protoc_insertion_point(module_scope)