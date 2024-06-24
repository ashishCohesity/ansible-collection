from util.appspec import appspec_pb2 as _appspec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationInfoProto(_message.Message):
    __slots__ = ("resource_id", "severity", "summary")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ValidationInfoProto.Severity]
        kInfo: _ClassVar[ValidationInfoProto.Severity]
        kWarning: _ClassVar[ValidationInfoProto.Severity]
        kError: _ClassVar[ValidationInfoProto.Severity]
    kUnknown: ValidationInfoProto.Severity
    kInfo: ValidationInfoProto.Severity
    kWarning: ValidationInfoProto.Severity
    kError: ValidationInfoProto.Severity
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    resource_id: _appspec_pb2.Identifier
    severity: ValidationInfoProto.Severity
    summary: str
    def __init__(self, resource_id: _Optional[_Union[_appspec_pb2.Identifier, _Mapping]] = ..., severity: _Optional[_Union[ValidationInfoProto.Severity, str]] = ..., summary: _Optional[str] = ...) -> None: ...

class ValidationResultProto(_message.Message):
    __slots__ = ("id", "runbook_uid", "validation_info_vec", "result", "appspec_json", "start_time_usecs", "end_time_usecs")
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[ValidationResultProto.Result]
        kSuccess: _ClassVar[ValidationResultProto.Result]
        kFailure: _ClassVar[ValidationResultProto.Result]
        kWarning: _ClassVar[ValidationResultProto.Result]
        kCanceled: _ClassVar[ValidationResultProto.Result]
        kCanceling: _ClassVar[ValidationResultProto.Result]
    kInProgress: ValidationResultProto.Result
    kSuccess: ValidationResultProto.Result
    kFailure: ValidationResultProto.Result
    kWarning: ValidationResultProto.Result
    kCanceled: ValidationResultProto.Result
    kCanceling: ValidationResultProto.Result
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNBOOK_UID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    APPSPEC_JSON_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    id: int
    runbook_uid: str
    validation_info_vec: _containers.RepeatedCompositeFieldContainer[ValidationInfoProto]
    result: ValidationResultProto.Result
    appspec_json: str
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, id: _Optional[int] = ..., runbook_uid: _Optional[str] = ..., validation_info_vec: _Optional[_Iterable[_Union[ValidationInfoProto, _Mapping]]] = ..., result: _Optional[_Union[ValidationResultProto.Result, str]] = ..., appspec_json: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...
