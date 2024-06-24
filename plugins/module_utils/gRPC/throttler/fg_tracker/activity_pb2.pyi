from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kComponentNotFound: _ClassVar[ErrorProto.Type]
        kActivityIdNotFound: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kComponentNotFound: ErrorProto.Type
    kActivityIdNotFound: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class ForegroundActivity(_message.Message):
    __slots__ = ("id", "throttling_requests", "start_time_msecs", "expiration_time_msecs")
    class ThrottlingRequest(_message.Message):
        __slots__ = ("background_component", "soft_level", "hard_level", "reason")
        BACKGROUND_COMPONENT_FIELD_NUMBER: _ClassVar[int]
        SOFT_LEVEL_FIELD_NUMBER: _ClassVar[int]
        HARD_LEVEL_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        background_component: _cluster_config_pb2.ClusterConfigProto.Component.QoSComponent
        soft_level: _cluster_config_pb2.ClusterConfigProto.BandwidthLimit.BackgroundIORate
        hard_level: _cluster_config_pb2.ClusterConfigProto.BandwidthLimit.BackgroundIORate
        reason: str
        def __init__(self, background_component: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Component.QoSComponent, str]] = ..., soft_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BandwidthLimit.BackgroundIORate, str]] = ..., hard_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BandwidthLimit.BackgroundIORate, str]] = ..., reason: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    id: str
    throttling_requests: _containers.RepeatedCompositeFieldContainer[ForegroundActivity.ThrottlingRequest]
    start_time_msecs: int
    expiration_time_msecs: int
    def __init__(self, id: _Optional[str] = ..., throttling_requests: _Optional[_Iterable[_Union[ForegroundActivity.ThrottlingRequest, _Mapping]]] = ..., start_time_msecs: _Optional[int] = ..., expiration_time_msecs: _Optional[int] = ...) -> None: ...

class ActivityTrackerProto(_message.Message):
    __slots__ = ("gandalf_key", "foreground_activities")
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    FOREGROUND_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    foreground_activities: _containers.RepeatedCompositeFieldContainer[ForegroundActivity]
    def __init__(self, gandalf_key: _Optional[str] = ..., foreground_activities: _Optional[_Iterable[_Union[ForegroundActivity, _Mapping]]] = ...) -> None: ...
