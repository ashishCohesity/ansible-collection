from apollo.mr.master import master_pb2 as _master_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApolloJobRunReport(_message.Message):
    __slots__ = ("job_run",)
    JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    job_run: _master_pb2.JobProto
    def __init__(self, job_run: _Optional[_Union[_master_pb2.JobProto, _Mapping]] = ...) -> None: ...
