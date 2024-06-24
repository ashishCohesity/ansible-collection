from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobSchedulingConfigProto(_message.Message):
    __slots__ = ("version", "start_all_jobs", "tenant_vec")
    class TenantProto(_message.Message):
        __slots__ = ("tenant_id", "start_all_jobs_for_tenant", "max_running_jobs_count")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        START_ALL_JOBS_FOR_TENANT_FIELD_NUMBER: _ClassVar[int]
        MAX_RUNNING_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        start_all_jobs_for_tenant: bool
        max_running_jobs_count: int
        def __init__(self, tenant_id: _Optional[str] = ..., start_all_jobs_for_tenant: bool = ..., max_running_jobs_count: _Optional[int] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    START_ALL_JOBS_FIELD_NUMBER: _ClassVar[int]
    TENANT_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    start_all_jobs: bool
    tenant_vec: _containers.RepeatedCompositeFieldContainer[JobSchedulingConfigProto.TenantProto]
    def __init__(self, version: _Optional[int] = ..., start_all_jobs: bool = ..., tenant_vec: _Optional[_Iterable[_Union[JobSchedulingConfigProto.TenantProto, _Mapping]]] = ...) -> None: ...
