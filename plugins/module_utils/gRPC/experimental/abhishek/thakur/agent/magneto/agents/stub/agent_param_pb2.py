# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/abhishek.thakur/agent/magneto/agents/stub/agent_param.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.agents.base import error_pb2 as magneto_dot_agents_dot_base_dot_error__pb2
from magneto.agents.stub import agent_base_pb2 as magneto_dot_agents_dot_stub_dot_agent__base__pb2
from magneto.base import common_pb2 as magneto_dot_base_dot_common__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHexperimental/abhishek.thakur/agent/magneto/agents/stub/agent_param.proto\x12\x1c\x63ohesity.magneto.agents.stub\x1a\x1fmagneto/agents/base/agent.proto\x1a\x1fmagneto/agents/base/error.proto\x1a$magneto/agents/stub/agent_base.proto\x1a\x19magneto/base/common.proto\x1a\x18magneto/base/enums.proto\x1a\x1cutil/base/universal_id.proto\"\xa5\x01\n\x10RegisterAgentArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x10\n\x08\x61gent_id\x18\x02 \x01(\x03\x12\x14\n\x0c\x63luster_name\x18\x04 \x01(\t\x12-\n\tagent_uid\x18\x05 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xc6\x02\n\x13RegisterAgentResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12;\n\nagent_info\x18\x02 \x01(\x0b\x32\'.cohesity.magneto.agents.AgentInfoProto\x12\x41\n\x0fvolume_info_vec\x18\x03 \x03(\x0b\x32(.cohesity.magneto.agents.VolumeInfoProto\x12-\n\tagent_uid\x18\x04 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x42\n\x14system_resource_info\x18\x05 \x01(\x0b\x32$.cohesity.magneto.SystemResourceInfo*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"P\n\x12UnregisterAgentArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\"M\n\x0fGetAgentInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\"\x85\x01\n\x12GetAgentInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12;\n\nagent_info\x18\x07 \x01(\x0b\x32\'.cohesity.magneto.agents.AgentInfoProto\"V\n\x12\x46\x65tchVolumeInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArgJ\x04\x08\x06\x10\x07\"\x8e\x01\n\x15\x46\x65tchVolumeInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x41\n\x0fvolume_info_vec\x18\x02 \x03(\x0b\x32(.cohesity.magneto.agents.VolumeInfoProto\"V\n\x0eGetHostInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x86\x02\n\x11GetHostInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x34\n\thost_info\x18\x02 \x01(\x0b\x32!.cohesity.magneto.agents.HostInfo\x12\x43\n\x11host_info_summary\x18\x04 \x01(\x0b\x32(.cohesity.magneto.agents.HostInfoSummary\x12\x38\n\x08host_env\x18\x06 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type:\x06kLinux*\x08\x08\x64\x10\x80\x80\x80\x80\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.abhishek.thakur.agent.magneto.agents.stub.agent_param_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERAGENTARG']._serialized_start=294
  _globals['_REGISTERAGENTARG']._serialized_end=459
  _globals['_REGISTERAGENTRESULT']._serialized_start=462
  _globals['_REGISTERAGENTRESULT']._serialized_end=788
  _globals['_UNREGISTERAGENTARG']._serialized_start=790
  _globals['_UNREGISTERAGENTARG']._serialized_end=870
  _globals['_GETAGENTINFOARG']._serialized_start=872
  _globals['_GETAGENTINFOARG']._serialized_end=949
  _globals['_GETAGENTINFORESULT']._serialized_start=952
  _globals['_GETAGENTINFORESULT']._serialized_end=1085
  _globals['_FETCHVOLUMEINFOARG']._serialized_start=1087
  _globals['_FETCHVOLUMEINFOARG']._serialized_end=1173
  _globals['_FETCHVOLUMEINFORESULT']._serialized_start=1176
  _globals['_FETCHVOLUMEINFORESULT']._serialized_end=1318
  _globals['_GETHOSTINFOARG']._serialized_start=1320
  _globals['_GETHOSTINFOARG']._serialized_end=1406
  _globals['_GETHOSTINFORESULT']._serialized_start=1409
  _globals['_GETHOSTINFORESULT']._serialized_end=1671
# @@protoc_insertion_point(module_scope)
