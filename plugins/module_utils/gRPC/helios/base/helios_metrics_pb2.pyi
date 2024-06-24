from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosMetricsProto(_message.Message):
    __slots__ = ("account_id", "cluster_id", "cluster_incarnation_id", "metric_type", "iris_metrics_data")
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIrisApi: _ClassVar[HeliosMetricsProto.MetricType]
    kIrisApi: HeliosMetricsProto.MetricType
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    IRIS_METRICS_DATA_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    cluster_incarnation_id: str
    metric_type: HeliosMetricsProto.MetricType
    iris_metrics_data: IrisMetricsData
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_incarnation_id: _Optional[str] = ..., metric_type: _Optional[_Union[HeliosMetricsProto.MetricType, str]] = ..., iris_metrics_data: _Optional[_Union[IrisMetricsData, _Mapping]] = ...) -> None: ...

class IrisMetricsData(_message.Message):
    __slots__ = ("is_pass_through", "time_elapsed_nsecs", "url", "request_starttime_nsecs", "error_message", "status_code")
    IS_PASS_THROUGH_FIELD_NUMBER: _ClassVar[int]
    TIME_ELAPSED_NSECS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STARTTIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    is_pass_through: bool
    time_elapsed_nsecs: int
    url: str
    request_starttime_nsecs: int
    error_message: str
    status_code: int
    def __init__(self, is_pass_through: bool = ..., time_elapsed_nsecs: _Optional[int] = ..., url: _Optional[str] = ..., request_starttime_nsecs: _Optional[int] = ..., error_message: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...
