from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from apollo.mr.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulePipelineArg(_message.Message):
    __slots__ = ("name", "pipeline_input", "urgency", "is_forwarded")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_INPUT_FIELD_NUMBER: _ClassVar[int]
    URGENCY_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    name: str
    pipeline_input: bytes
    urgency: int
    is_forwarded: bool
    def __init__(self, name: _Optional[str] = ..., pipeline_input: _Optional[bytes] = ..., urgency: _Optional[int] = ..., is_forwarded: bool = ...) -> None: ...

class SchedulePipelineResult(_message.Message):
    __slots__ = ("error", "request_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    request_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., request_id: _Optional[int] = ...) -> None: ...

class CancelPipelineArg(_message.Message):
    __slots__ = ("pipeline_name", "job_name", "request_id", "cancel_latest_run", "cancel_all", "reason", "is_forwarded")
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_LATEST_RUN_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ALL_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    pipeline_name: str
    job_name: str
    request_id: int
    cancel_latest_run: bool
    cancel_all: bool
    reason: str
    is_forwarded: bool
    def __init__(self, pipeline_name: _Optional[str] = ..., job_name: _Optional[str] = ..., request_id: _Optional[int] = ..., cancel_latest_run: bool = ..., cancel_all: bool = ..., reason: _Optional[str] = ..., is_forwarded: bool = ...) -> None: ...

class CancelPipelineResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetStorageDomainDistributionsArg(_message.Message):
    __slots__ = ("storage_domain_id_vec", "is_forwarded")
    STORAGE_DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    storage_domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
    is_forwarded: bool
    def __init__(self, storage_domain_id_vec: _Optional[_Iterable[int]] = ..., is_forwarded: bool = ...) -> None: ...

class GetStorageDomainDistributionsResult(_message.Message):
    __slots__ = ("error", "result_vec")
    class Result(_message.Message):
        __slots__ = ("storage_domain_id", "file_size_exponential_histogram")
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_EXPONENTIAL_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        storage_domain_id: int
        file_size_exponential_histogram: _histogram_proto_pb2.HistogramProto
        def __init__(self, storage_domain_id: _Optional[int] = ..., file_size_exponential_histogram: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    result_vec: _containers.RepeatedCompositeFieldContainer[GetStorageDomainDistributionsResult.Result]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[GetStorageDomainDistributionsResult.Result, _Mapping]]] = ...) -> None: ...
