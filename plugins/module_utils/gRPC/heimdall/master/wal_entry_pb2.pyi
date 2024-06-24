from heimdall.master.base import master_pb2 as _master_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeimdallWALEntry(_message.Message):
    __slots__ = ("delta_op_type", "resource_info_map", "resource_info", "connector_params_map", "source_entity_id", "connector_params", "fleet_info_map", "fleet_info")
    class DeltaOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateOrUpdate: _ClassVar[HeimdallWALEntry.DeltaOpType]
        kDelete: _ClassVar[HeimdallWALEntry.DeltaOpType]
        kConnectorParam: _ClassVar[HeimdallWALEntry.DeltaOpType]
    kCreateOrUpdate: HeimdallWALEntry.DeltaOpType
    kDelete: HeimdallWALEntry.DeltaOpType
    kConnectorParam: HeimdallWALEntry.DeltaOpType
    class ResourceInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _master_pb2.ResourceInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_master_pb2.ResourceInfo, _Mapping]] = ...) -> None: ...
    class ConnectorParamsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _magneto_pb2.ConnectorParams
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...
    class FleetInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _master_pb2.FleetInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_master_pb2.FleetInfo, _Mapping]] = ...) -> None: ...
    DELTA_OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_MAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FLEET_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    FLEET_INFO_FIELD_NUMBER: _ClassVar[int]
    delta_op_type: HeimdallWALEntry.DeltaOpType
    resource_info_map: _containers.MessageMap[str, _master_pb2.ResourceInfo]
    resource_info: _master_pb2.ResourceInfo
    connector_params_map: _containers.MessageMap[int, _magneto_pb2.ConnectorParams]
    source_entity_id: int
    connector_params: _magneto_pb2.ConnectorParams
    fleet_info_map: _containers.MessageMap[str, _master_pb2.FleetInfo]
    fleet_info: _master_pb2.FleetInfo
    def __init__(self, delta_op_type: _Optional[_Union[HeimdallWALEntry.DeltaOpType, str]] = ..., resource_info_map: _Optional[_Mapping[str, _master_pb2.ResourceInfo]] = ..., resource_info: _Optional[_Union[_master_pb2.ResourceInfo, _Mapping]] = ..., connector_params_map: _Optional[_Mapping[int, _magneto_pb2.ConnectorParams]] = ..., source_entity_id: _Optional[int] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., fleet_info_map: _Optional[_Mapping[str, _master_pb2.FleetInfo]] = ..., fleet_info: _Optional[_Union[_master_pb2.FleetInfo, _Mapping]] = ...) -> None: ...
