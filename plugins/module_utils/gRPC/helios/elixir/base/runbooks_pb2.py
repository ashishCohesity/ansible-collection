# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/elixir/base/runbooks.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nexus.eagle_agent.base import pipe_data_pb2 as nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!helios/elixir/base/runbooks.proto\x12\x18\x63ohesity.helios.runbooks\x1a&nexus/eagle_agent/base/pipe_data.proto\"{\n\x14RunbooksKafkaMessage\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x15\n\rrunbooks_data\x18\x02 \x01(\x0c\x12\x17\n\x0fis_unregistered\x18\x03 \x01(\x08\x42\x1aZ\x18\x63ohesity/helios/runbooksb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.elixir.base.runbooks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/helios/runbooks'
  _globals['_RUNBOOKSKAFKAMESSAGE']._serialized_start=103
  _globals['_RUNBOOKSKAFKAMESSAGE']._serialized_end=226
# @@protoc_insertion_point(module_scope)
