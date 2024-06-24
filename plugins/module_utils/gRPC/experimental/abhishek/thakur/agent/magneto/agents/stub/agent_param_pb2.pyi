from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterAgentArg(_message.Message):
    __slots__ = ("header", "agent_id", "cluster_name", "agent_uid")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    agent_id: int
    cluster_name: str
    agent_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., agent_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class RegisterAgentResult(_message.Message):
    __slots__ = ("error", "agent_info", "volume_info_vec", "agent_uid", "system_resource_info")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    agent_info: _agent_pb2.AgentInfoProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    agent_uid: _universal_id_pb2.UniversalIdProto
    system_resource_info: _common_pb2.SystemResourceInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ...) -> None: ...

class UnregisterAgentArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetAgentInfoArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetAgentInfoResult(_message.Message):
    __slots__ = ("error", "agent_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    agent_info: _agent_pb2.AgentInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ...) -> None: ...

class FetchVolumeInfoArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class FetchVolumeInfoResult(_message.Message):
    __slots__ = ("error", "volume_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ...) -> None: ...

class GetHostInfoArg(_message.Message):
    __slots__ = ("header",)
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class GetHostInfoResult(_message.Message):
    __slots__ = ("error", "host_info", "host_info_summary", "host_env")
    Extensions: _python_message._ExtensionDict
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    HOST_ENV_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    host_info: _agent_pb2.HostInfo
    host_info_summary: _agent_pb2.HostInfoSummary
    host_env: _enums_pb2.HostEnv.Type
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_info: _Optional[_Union[_agent_pb2.HostInfo, _Mapping]] = ..., host_info_summary: _Optional[_Union[_agent_pb2.HostInfoSummary, _Mapping]] = ..., host_env: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ...) -> None: ...
