from magneto.base import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThrottlingConfiguration(_message.Message):
    __slots__ = ("pattern_type", "fixed_threshold", "throttling_windows")
    class PatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoThrottling: _ClassVar[ThrottlingConfiguration.PatternType]
        kFixed: _ClassVar[ThrottlingConfiguration.PatternType]
        kScheduleBased: _ClassVar[ThrottlingConfiguration.PatternType]
    kNoThrottling: ThrottlingConfiguration.PatternType
    kFixed: ThrottlingConfiguration.PatternType
    kScheduleBased: ThrottlingConfiguration.PatternType
    class ThrottlingWindow(_message.Message):
        __slots__ = ("day_time_window", "threshold")
        DAY_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        day_time_window: _policy_pb2.DayTimeWindow
        threshold: int
        def __init__(self, day_time_window: _Optional[_Union[_policy_pb2.DayTimeWindow, _Mapping]] = ..., threshold: _Optional[int] = ...) -> None: ...
    PATTERN_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXED_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    pattern_type: ThrottlingConfiguration.PatternType
    fixed_threshold: int
    throttling_windows: _containers.RepeatedCompositeFieldContainer[ThrottlingConfiguration.ThrottlingWindow]
    def __init__(self, pattern_type: _Optional[_Union[ThrottlingConfiguration.PatternType, str]] = ..., fixed_threshold: _Optional[int] = ..., throttling_windows: _Optional[_Iterable[_Union[ThrottlingConfiguration.ThrottlingWindow, _Mapping]]] = ...) -> None: ...

class SourceThrottlingConfiguration(_message.Message):
    __slots__ = ("cpu_throttling_config", "network_throttling_config")
    CPU_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROTTLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    cpu_throttling_config: ThrottlingConfiguration
    network_throttling_config: ThrottlingConfiguration
    def __init__(self, cpu_throttling_config: _Optional[_Union[ThrottlingConfiguration, _Mapping]] = ..., network_throttling_config: _Optional[_Union[ThrottlingConfiguration, _Mapping]] = ...) -> None: ...
