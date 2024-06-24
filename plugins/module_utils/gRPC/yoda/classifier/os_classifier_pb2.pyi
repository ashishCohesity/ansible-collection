from yoda.base import reports_pb2 as _reports_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OSFeature(_message.Message):
    __slots__ = ("name", "os_type", "weight", "is_partial", "low_hit_threshold", "high_hit_threshold")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    LOW_HIT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    HIGH_HIT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    name: str
    os_type: _reports_pb2.OSType.Type
    weight: float
    is_partial: bool
    low_hit_threshold: int
    high_hit_threshold: int
    def __init__(self, name: _Optional[str] = ..., os_type: _Optional[_Union[_reports_pb2.OSType.Type, str]] = ..., weight: _Optional[float] = ..., is_partial: bool = ..., low_hit_threshold: _Optional[int] = ..., high_hit_threshold: _Optional[int] = ...) -> None: ...

class OSModel(_message.Message):
    __slots__ = ("features",)
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[OSFeature]
    def __init__(self, features: _Optional[_Iterable[_Union[OSFeature, _Mapping]]] = ...) -> None: ...
