from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrechecksInfo(_message.Message):
    __slots__ = ("precheck_name", "precheck_passed", "precheck_error_message")
    PRECHECK_NAME_FIELD_NUMBER: _ClassVar[int]
    PRECHECK_PASSED_FIELD_NUMBER: _ClassVar[int]
    PRECHECK_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    precheck_name: str
    precheck_passed: bool
    precheck_error_message: str
    def __init__(self, precheck_name: _Optional[str] = ..., precheck_passed: bool = ..., precheck_error_message: _Optional[str] = ...) -> None: ...

class PrechecksResult(_message.Message):
    __slots__ = ("entity_id", "execution_timestamp_secs", "prechecks_info_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    PRECHECKS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    execution_timestamp_secs: int
    prechecks_info_vec: _containers.RepeatedCompositeFieldContainer[PrechecksInfo]
    def __init__(self, entity_id: _Optional[int] = ..., execution_timestamp_secs: _Optional[int] = ..., prechecks_info_vec: _Optional[_Iterable[_Union[PrechecksInfo, _Mapping]]] = ...) -> None: ...

class PrechecksResults(_message.Message):
    __slots__ = ("prechecks_results_vec",)
    PRECHECKS_RESULTS_VEC_FIELD_NUMBER: _ClassVar[int]
    prechecks_results_vec: _containers.RepeatedCompositeFieldContainer[PrechecksResult]
    def __init__(self, prechecks_results_vec: _Optional[_Iterable[_Union[PrechecksResult, _Mapping]]] = ...) -> None: ...
