# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/base/job_update.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1chelios/base/job_update.proto\x12\x19\x63ohesity.helios.jobupdate\"\xa5\x01\n\x15JobUpdateKafkaMessage\x12\x12\n\ncluster_id\x18\x01 \x01(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x02 \x01(\x03\x12\x15\n\rsf_account_id\x18\x03 \x01(\t\x12\x0e\n\x06job_id\x18\x04 \x01(\x03\x12\x0e\n\x06run_id\x18\x05 \x01(\x03\x12\x11\n\tentity_id\x18\x06 \x01(\x03\x12\x0e\n\x06source\x18\x07 \x01(\x05\x42\x1bZ\x19\x63ohesity/helios/jobupdateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.base.job_update_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031cohesity/helios/jobupdate'
  _globals['_JOBUPDATEKAFKAMESSAGE']._serialized_start=60
  _globals['_JOBUPDATEKAFKAMESSAGE']._serialized_end=225
# @@protoc_insertion_point(module_scope)
