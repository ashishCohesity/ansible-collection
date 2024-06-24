from apollo.mr.master import master_pb2 as _master_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APIServerWALRecordProto(_message.Message):
    __slots__ = ("schedule_job_request_vec", "add_or_delete_schedule_job_request")
    class AddOrDeleteScheduleJobRequestProto(_message.Message):
        __slots__ = ("job_request", "delete_request")
        JOB_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DELETE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        job_request: _master_pb2.ScheduleJobRequestProto
        delete_request: bool
        def __init__(self, job_request: _Optional[_Union[_master_pb2.ScheduleJobRequestProto, _Mapping]] = ..., delete_request: bool = ...) -> None: ...
    SCHEDULE_JOB_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_DELETE_SCHEDULE_JOB_REQUEST_FIELD_NUMBER: _ClassVar[int]
    schedule_job_request_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.ScheduleJobRequestProto]
    add_or_delete_schedule_job_request: APIServerWALRecordProto.AddOrDeleteScheduleJobRequestProto
    def __init__(self, schedule_job_request_vec: _Optional[_Iterable[_Union[_master_pb2.ScheduleJobRequestProto, _Mapping]]] = ..., add_or_delete_schedule_job_request: _Optional[_Union[APIServerWALRecordProto.AddOrDeleteScheduleJobRequestProto, _Mapping]] = ...) -> None: ...
