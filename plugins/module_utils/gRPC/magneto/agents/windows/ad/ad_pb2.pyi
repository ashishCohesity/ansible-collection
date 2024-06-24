from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base.entities import ad_pb2 as _ad_pb2
from magneto.agents.windows.stub import ad_param_pb2 as _ad_param_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ADAppFileInfo(_message.Message):
    __slots__ = ("dc", "ad_topology")
    APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_info: _descriptor.FieldDescriptor
    DC_FIELD_NUMBER: _ClassVar[int]
    AD_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    dc: _ad_pb2.ADDomainController
    ad_topology: _ad_param_pb2.GetADDomainRootTopologyResult
    def __init__(self, dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ..., ad_topology: _Optional[_Union[_ad_param_pb2.GetADDomainRootTopologyResult, _Mapping]] = ...) -> None: ...
