from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import source_throttling_pb2 as _source_throttling_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserSettings(_message.Message):
    __slots__ = ("gflag_setting_vec",)
    GFLAG_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    gflag_setting_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.GFlagSetting]
    def __init__(self, gflag_setting_vec: _Optional[_Iterable[_Union[_agent_pb2.GFlagSetting, _Mapping]]] = ...) -> None: ...

class AgentConfigProto(_message.Message):
    __slots__ = ("agent_info_proto", "user_settings", "source_throttling_config")
    AGENT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    USER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    agent_info_proto: _agent_pb2.AgentInfoProto
    user_settings: UserSettings
    source_throttling_config: _source_throttling_pb2.SourceThrottlingConfiguration
    def __init__(self, agent_info_proto: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., user_settings: _Optional[_Union[UserSettings, _Mapping]] = ..., source_throttling_config: _Optional[_Union[_source_throttling_pb2.SourceThrottlingConfiguration, _Mapping]] = ...) -> None: ...
