from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvCapabilityProto(_message.Message):
    __slots__ = ("type", "supported_features", "tx_version", "rx_min_supported_version", "rx_max_supported_version")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    TX_VERSION_FIELD_NUMBER: _ClassVar[int]
    RX_MIN_SUPPORTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    RX_MAX_SUPPORTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    supported_features: _containers.RepeatedScalarFieldContainer[str]
    tx_version: int
    rx_min_supported_version: int
    rx_max_supported_version: int
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., supported_features: _Optional[_Iterable[str]] = ..., tx_version: _Optional[int] = ..., rx_min_supported_version: _Optional[int] = ..., rx_max_supported_version: _Optional[int] = ...) -> None: ...

class GlobalCapabilityProto(_message.Message):
    __slots__ = ("supported_features",)
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    supported_features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, supported_features: _Optional[_Iterable[str]] = ...) -> None: ...

class CapabilityProto(_message.Message):
    __slots__ = ("env_capability_vec", "global_capability")
    ENV_CAPABILITY_VEC_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    env_capability_vec: _containers.RepeatedCompositeFieldContainer[EnvCapabilityProto]
    global_capability: GlobalCapabilityProto
    def __init__(self, env_capability_vec: _Optional[_Iterable[_Union[EnvCapabilityProto, _Mapping]]] = ..., global_capability: _Optional[_Union[GlobalCapabilityProto, _Mapping]] = ...) -> None: ...
