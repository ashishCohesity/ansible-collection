# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/agent/agent_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bridge/magneto/agent/agent_actions.proto\x12\x1d\x63ohesity.bridge.magneto.agent\x1a)bridge/magneto/base/magneto_actions.proto\x1a\x1amagneto/base/magneto.proto\"{\n\tAgentInfo\x12;\n\x10\x63onnector_params\x18\x01 \x01(\x0b\x32!.cohesity.magneto.ConnectorParams\x12\x13\n\x0b\x61pi_version\x18\x02 \x01(\x03\x12\x1c\n\x14\x61gent_incarnation_id\x18\x03 \x01(\x03\"\x88\x02\n\x17\x46\x65tchAndStoreDataAction\x12V\n\rfile_info_vec\x18\x01 \x03(\x0b\x32?.cohesity.bridge.magneto.agent.FetchAndStoreDataAction.FileInfo\x12\x16\n\ncluster_id\x18\x0c \x01(\x03:\x02-1\x12\"\n\x16\x63luster_incarnation_id\x18\r \x01(\x03:\x02-1\x1aY\n\x08\x46ileInfo\x12\x1c\n\x14snapfs_full_dir_path\x18\x01 \x01(\t\x12\x18\n\x10snapfs_file_name\x18\x02 \x01(\t\x12\x15\n\ragent_data_id\x18\x03 \x01(\x0c\"\xb0\x02\n\x0e\x41gentActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12<\n\nagent_info\x18\x02 \x01(\x0b\x32(.cohesity.bridge.magneto.agent.AgentInfo\x12[\n\x1b\x66\x65tch_and_store_data_action\x18\x03 \x01(\x0b\x32\x36.cohesity.bridge.magneto.agent.FetchAndStoreDataAction2r\n\x10\x61gent_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18k \x01(\x0b\x32-.cohesity.bridge.magneto.agent.AgentActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.agent.agent_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AGENTINFO']._serialized_start=146
  _globals['_AGENTINFO']._serialized_end=269
  _globals['_FETCHANDSTOREDATAACTION']._serialized_start=272
  _globals['_FETCHANDSTOREDATAACTION']._serialized_end=536
  _globals['_FETCHANDSTOREDATAACTION_FILEINFO']._serialized_start=447
  _globals['_FETCHANDSTOREDATAACTION_FILEINFO']._serialized_end=536
  _globals['_AGENTACTIONARG']._serialized_start=539
  _globals['_AGENTACTIONARG']._serialized_end=843
# @@protoc_insertion_point(module_scope)
