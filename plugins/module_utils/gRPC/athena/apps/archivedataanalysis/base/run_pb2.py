# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/apps/archivedataanalysis/base/run.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.athena/apps/archivedataanalysis/base/run.proto\x12\x04\x62\x61se\"\xe3\x01\n\x03Run\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07job_uid\x18\x02 \x01(\t\x12 \n\x06status\x18\x03 \x01(\x0e\x32\x10.base.Run.Status\x12\x18\n\x10start_time_msecs\x18\x04 \x01(\x03\x12\x16\n\x0e\x65nd_time_msecs\x18\x05 \x01(\x03\x12\x1b\n\x13\x66indings_table_name\x18\x07 \x01(\t\x12\x16\n\x0estatus_message\x18\x08 \x01(\t\"6\n\x06Status\x12\x0f\n\x0bkInProgress\x10\x00\x12\x0e\n\nkCompleted\x10\x01\x12\x0b\n\x07kFailed\x10\x02\x42\'Z%cohesity/archivedataanalysis_app/base')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.apps.archivedataanalysis.base.run_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%cohesity/archivedataanalysis_app/base'
  _globals['_RUN']._serialized_start=57
  _globals['_RUN']._serialized_end=284
  _globals['_RUN_STATUS']._serialized_start=230
  _globals['_RUN_STATUS']._serialized_end=284
# @@protoc_insertion_point(module_scope)