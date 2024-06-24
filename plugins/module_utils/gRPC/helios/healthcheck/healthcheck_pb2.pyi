from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckResult(_message.Message):
    __slots__ = ("check_id", "node_ip", "name", "description", "result", "end_time_sec", "short_output", "long_output", "check_type")
    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPass: _ClassVar[HealthCheckResult.ResultType]
        kFail: _ClassVar[HealthCheckResult.ResultType]
        kWarning: _ClassVar[HealthCheckResult.ResultType]
        kSkipped: _ClassVar[HealthCheckResult.ResultType]
        kError: _ClassVar[HealthCheckResult.ResultType]
        kTimeout: _ClassVar[HealthCheckResult.ResultType]
    kPass: HealthCheckResult.ResultType
    kFail: HealthCheckResult.ResultType
    kWarning: HealthCheckResult.ResultType
    kSkipped: HealthCheckResult.ResultType
    kError: HealthCheckResult.ResultType
    kTimeout: HealthCheckResult.ResultType
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    SHORT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LONG_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    check_id: str
    node_ip: str
    name: str
    description: str
    result: HealthCheckResult.ResultType
    end_time_sec: int
    short_output: str
    long_output: str
    check_type: str
    def __init__(self, check_id: _Optional[str] = ..., node_ip: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., result: _Optional[_Union[HealthCheckResult.ResultType, str]] = ..., end_time_sec: _Optional[int] = ..., short_output: _Optional[str] = ..., long_output: _Optional[str] = ..., check_type: _Optional[str] = ...) -> None: ...

class CombinedResult(_message.Message):
    __slots__ = ("healthcheck_results_vec",)
    HEALTHCHECK_RESULTS_VEC_FIELD_NUMBER: _ClassVar[int]
    healthcheck_results_vec: _containers.RepeatedCompositeFieldContainer[HealthCheckResult]
    def __init__(self, healthcheck_results_vec: _Optional[_Iterable[_Union[HealthCheckResult, _Mapping]]] = ...) -> None: ...
