from open_util.net import protorpc_pb2 as _protorpc_pb2
from throttler.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Parameters(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Algorithm(_message.Message):
    __slots__ = ("kind", "params")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PassThrough: _ClassVar[Algorithm.Kind]
        StaticReallocation: _ClassVar[Algorithm.Kind]
        DynamicReallocation: _ClassVar[Algorithm.Kind]
    PassThrough: Algorithm.Kind
    StaticReallocation: Algorithm.Kind
    DynamicReallocation: Algorithm.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    kind: Algorithm.Kind
    params: _containers.RepeatedCompositeFieldContainer[Parameters]
    def __init__(self, kind: _Optional[_Union[Algorithm.Kind, str]] = ..., params: _Optional[_Iterable[_Union[Parameters, _Mapping]]] = ...) -> None: ...

class ResourceConfig(_message.Message):
    __slots__ = ("algorithm", "resource_type", "global_limit", "resource_static_critical_limit_percent")
    class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ExternalTargetBandwidth: _ClassVar[ResourceConfig.ResourceType]
    ExternalTargetBandwidth: ResourceConfig.ResourceType
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_STATIC_CRITICAL_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    algorithm: Algorithm
    resource_type: ResourceConfig.ResourceType
    global_limit: int
    resource_static_critical_limit_percent: int
    def __init__(self, algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., resource_type: _Optional[_Union[ResourceConfig.ResourceType, str]] = ..., global_limit: _Optional[int] = ..., resource_static_critical_limit_percent: _Optional[int] = ...) -> None: ...

class ComponentUsage(_message.Message):
    __slots__ = ("component_id", "component_weight", "resource_usage", "resource_critical_usage", "static_resource_usage", "resource_desired_usage")
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CRITICAL_USAGE_FIELD_NUMBER: _ClassVar[int]
    STATIC_RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_DESIRED_USAGE_FIELD_NUMBER: _ClassVar[int]
    component_id: str
    component_weight: int
    resource_usage: int
    resource_critical_usage: int
    static_resource_usage: int
    resource_desired_usage: int
    def __init__(self, component_id: _Optional[str] = ..., component_weight: _Optional[int] = ..., resource_usage: _Optional[int] = ..., resource_critical_usage: _Optional[int] = ..., static_resource_usage: _Optional[int] = ..., resource_desired_usage: _Optional[int] = ...) -> None: ...

class ResourceUsage(_message.Message):
    __slots__ = ("resource_id", "resource_config", "component_usage", "description")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_USAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    resource_config: ResourceConfig
    component_usage: _containers.RepeatedCompositeFieldContainer[ComponentUsage]
    description: str
    def __init__(self, resource_id: _Optional[str] = ..., resource_config: _Optional[_Union[ResourceConfig, _Mapping]] = ..., component_usage: _Optional[_Iterable[_Union[ComponentUsage, _Mapping]]] = ..., description: _Optional[str] = ...) -> None: ...

class HeartbeatArg(_message.Message):
    __slots__ = ("heartbeat_id", "constituent_id", "actual_usage")
    HEARTBEAT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_USAGE_FIELD_NUMBER: _ClassVar[int]
    heartbeat_id: str
    constituent_id: int
    actual_usage: _containers.RepeatedCompositeFieldContainer[ResourceUsage]
    def __init__(self, heartbeat_id: _Optional[str] = ..., constituent_id: _Optional[int] = ..., actual_usage: _Optional[_Iterable[_Union[ResourceUsage, _Mapping]]] = ...) -> None: ...

class HeartbeatResult(_message.Message):
    __slots__ = ("heartbeat_id", "error", "allocated_limits")
    HEARTBEAT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_LIMITS_FIELD_NUMBER: _ClassVar[int]
    heartbeat_id: str
    error: _error_pb2.ErrorProto
    allocated_limits: _containers.RepeatedCompositeFieldContainer[ResourceUsage]
    def __init__(self, heartbeat_id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., allocated_limits: _Optional[_Iterable[_Union[ResourceUsage, _Mapping]]] = ...) -> None: ...
