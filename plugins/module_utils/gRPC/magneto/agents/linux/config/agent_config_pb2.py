# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/linux/config/agent_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base import source_throttling_pb2 as magneto_dot_base_dot_source__throttling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.magneto/agents/linux/config/agent_config.proto\x12\x1d\x63ohesity.magneto.agents.linux\x1a\x1fmagneto/agents/base/agent.proto\x1a$magneto/base/source_throttling.proto\"P\n\x0cUserSettings\x12@\n\x11gflag_setting_vec\x18\x01 \x03(\x0b\x32%.cohesity.magneto.agents.GFlagSetting\"\xec\x01\n\x10\x41gentConfigProto\x12\x41\n\x10\x61gent_info_proto\x18\x01 \x01(\x0b\x32\'.cohesity.magneto.agents.AgentInfoProto\x12\x42\n\ruser_settings\x18\x02 \x01(\x0b\x32+.cohesity.magneto.agents.linux.UserSettings\x12Q\n\x18source_throttling_config\x18\x03 \x01(\x0b\x32/.cohesity.magneto.SourceThrottlingConfigurationB\"\n com.cohesity.magneto.agents.base')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.linux.config.agent_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.cohesity.magneto.agents.base'
  _globals['_USERSETTINGS']._serialized_start=152
  _globals['_USERSETTINGS']._serialized_end=232
  _globals['_AGENTCONFIGPROTO']._serialized_start=235
  _globals['_AGENTCONFIGPROTO']._serialized_end=471
# @@protoc_insertion_point(module_scope)
