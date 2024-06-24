from util.base import universal_id_pb2 as _universal_id_pb2
from util.appspec import appspec_pb2 as _appspec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotOverrideProto(_message.Message):
    __slots__ = ("resource", "snapshot_selector", "resource_identifier", "job_uid", "job_instance_id", "start_time_usecs", "point_in_time_usecs")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    resource: _containers.RepeatedCompositeFieldContainer[_appspec_pb2.Resource]
    snapshot_selector: _appspec_pb2.SnapshotSelector
    resource_identifier: _appspec_pb2.Identifier
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    start_time_usecs: int
    point_in_time_usecs: int
    def __init__(self, resource: _Optional[_Iterable[_Union[_appspec_pb2.Resource, _Mapping]]] = ..., snapshot_selector: _Optional[_Union[_appspec_pb2.SnapshotSelector, _Mapping]] = ..., resource_identifier: _Optional[_Union[_appspec_pb2.Identifier, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., point_in_time_usecs: _Optional[int] = ...) -> None: ...

class OverrideProto(_message.Message):
    __slots__ = ("runbook_uid", "run_id", "snapshot_override_vec")
    RUNBOOK_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_OVERRIDE_VEC_FIELD_NUMBER: _ClassVar[int]
    runbook_uid: str
    run_id: int
    snapshot_override_vec: _containers.RepeatedCompositeFieldContainer[SnapshotOverrideProto]
    def __init__(self, runbook_uid: _Optional[str] = ..., run_id: _Optional[int] = ..., snapshot_override_vec: _Optional[_Iterable[_Union[SnapshotOverrideProto, _Mapping]]] = ...) -> None: ...
