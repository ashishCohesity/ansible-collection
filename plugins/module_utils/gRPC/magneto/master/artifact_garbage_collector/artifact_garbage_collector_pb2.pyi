from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArtifactIdProto(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs", "task_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    task_id: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class ArtifactSpecProto(_message.Message):
    __slots__ = ("artifact_id", "environment", "snapfs_data_location_vec")
    Extensions: _python_message._ExtensionDict
    class SnapFsDataLocationProto(_message.Message):
        __slots__ = ("view_name", "path_name")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_NAME_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        path_name: str
        def __init__(self, view_name: _Optional[str] = ..., path_name: _Optional[str] = ...) -> None: ...
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SNAPFS_DATA_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    artifact_id: ArtifactIdProto
    environment: _enums_pb2.Environment.Type
    snapfs_data_location_vec: _containers.RepeatedCompositeFieldContainer[ArtifactSpecProto.SnapFsDataLocationProto]
    def __init__(self, artifact_id: _Optional[_Union[ArtifactIdProto, _Mapping]] = ..., environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., snapfs_data_location_vec: _Optional[_Iterable[_Union[ArtifactSpecProto.SnapFsDataLocationProto, _Mapping]]] = ...) -> None: ...

class SfdcGCArtifactSpecProto(_message.Message):
    __slots__ = ("sfdc_server_timestamp_usecs",)
    SFDC_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    sfdc_artifact: _descriptor.FieldDescriptor
    SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    sfdc_server_timestamp_usecs: int
    def __init__(self, sfdc_server_timestamp_usecs: _Optional[int] = ...) -> None: ...

class ArtifactGCStateProto(_message.Message):
    __slots__ = ("spec", "gc_status", "purged_timestamp_usecs", "error", "incoming_timestamp_usecs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ArtifactGCStateProto.Status]
        kInBacklog: _ClassVar[ArtifactGCStateProto.Status]
        kInProgress: _ClassVar[ArtifactGCStateProto.Status]
        kFinished: _ClassVar[ArtifactGCStateProto.Status]
        kPurged: _ClassVar[ArtifactGCStateProto.Status]
    kInvalid: ArtifactGCStateProto.Status
    kInBacklog: ArtifactGCStateProto.Status
    kInProgress: ArtifactGCStateProto.Status
    kFinished: ArtifactGCStateProto.Status
    kPurged: ArtifactGCStateProto.Status
    SPEC_FIELD_NUMBER: _ClassVar[int]
    GC_STATUS_FIELD_NUMBER: _ClassVar[int]
    PURGED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INCOMING_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    spec: ArtifactSpecProto
    gc_status: ArtifactGCStateProto.Status
    purged_timestamp_usecs: int
    error: _error_pb2.ErrorProto
    incoming_timestamp_usecs: int
    def __init__(self, spec: _Optional[_Union[ArtifactSpecProto, _Mapping]] = ..., gc_status: _Optional[_Union[ArtifactGCStateProto.Status, str]] = ..., purged_timestamp_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., incoming_timestamp_usecs: _Optional[int] = ...) -> None: ...
