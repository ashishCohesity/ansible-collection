from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CrashInjectionSiteInfo(_message.Message):
    __slots__ = ("subsystem_name", "site_name", "probability", "crash_count", "execution_count", "default_probability")
    SUBSYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    CRASH_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    subsystem_name: str
    site_name: str
    probability: float
    crash_count: int
    execution_count: int
    default_probability: float
    def __init__(self, subsystem_name: _Optional[str] = ..., site_name: _Optional[str] = ..., probability: _Optional[float] = ..., crash_count: _Optional[int] = ..., execution_count: _Optional[int] = ..., default_probability: _Optional[float] = ...) -> None: ...

class ErrorInjectionSiteInfo(_message.Message):
    __slots__ = ("subsystem_name", "site_name", "probability", "default_probability", "error_count", "execution_count", "default_error_window_msec", "error_window_msec", "default_interval_window_msec", "interval_window_msec")
    SUBSYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ERROR_WINDOW_MSEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_WINDOW_MSEC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INTERVAL_WINDOW_MSEC_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WINDOW_MSEC_FIELD_NUMBER: _ClassVar[int]
    subsystem_name: str
    site_name: str
    probability: float
    default_probability: float
    error_count: int
    execution_count: int
    default_error_window_msec: int
    error_window_msec: int
    default_interval_window_msec: int
    interval_window_msec: int
    def __init__(self, subsystem_name: _Optional[str] = ..., site_name: _Optional[str] = ..., probability: _Optional[float] = ..., default_probability: _Optional[float] = ..., error_count: _Optional[int] = ..., execution_count: _Optional[int] = ..., default_error_window_msec: _Optional[int] = ..., error_window_msec: _Optional[int] = ..., default_interval_window_msec: _Optional[int] = ..., interval_window_msec: _Optional[int] = ...) -> None: ...

class FaultInjectionSitesInfo(_message.Message):
    __slots__ = ("crash_vec", "error_vec")
    CRASH_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    crash_vec: _containers.RepeatedCompositeFieldContainer[CrashInjectionSiteInfo]
    error_vec: _containers.RepeatedCompositeFieldContainer[ErrorInjectionSiteInfo]
    def __init__(self, crash_vec: _Optional[_Iterable[_Union[CrashInjectionSiteInfo, _Mapping]]] = ..., error_vec: _Optional[_Iterable[_Union[ErrorInjectionSiteInfo, _Mapping]]] = ...) -> None: ...
