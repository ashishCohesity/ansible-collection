from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ("identifier", "status", "user_id", "create_timestamp_msecs", "update_timestamp_msecs", "status_message", "configuration", "num_runs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[Job.Status]
        kPaused: _ClassVar[Job.Status]
        kInProgress: _ClassVar[Job.Status]
        kFailed: _ClassVar[Job.Status]
    kCreated: Job.Status
    kPaused: Job.Status
    kInProgress: Job.Status
    kFailed: Job.Status
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NUM_RUNS_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    status: Job.Status
    user_id: str
    create_timestamp_msecs: int
    update_timestamp_msecs: int
    status_message: str
    configuration: Configuration
    num_runs: int
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., status: _Optional[_Union[Job.Status, str]] = ..., user_id: _Optional[str] = ..., create_timestamp_msecs: _Optional[int] = ..., update_timestamp_msecs: _Optional[int] = ..., status_message: _Optional[str] = ..., configuration: _Optional[_Union[Configuration, _Mapping]] = ..., num_runs: _Optional[int] = ...) -> None: ...

class Identifier(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class Configuration(_message.Message):
    __slots__ = ("bucket_name", "scheduling_interval_min", "project_id", "result_file_name", "start_time_scan_objects", "bucket_scan_folder")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_INTERVAL_MIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SCAN_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_SCAN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    scheduling_interval_min: int
    project_id: str
    result_file_name: str
    start_time_scan_objects: str
    bucket_scan_folder: str
    def __init__(self, bucket_name: _Optional[str] = ..., scheduling_interval_min: _Optional[int] = ..., project_id: _Optional[str] = ..., result_file_name: _Optional[str] = ..., start_time_scan_objects: _Optional[str] = ..., bucket_scan_folder: _Optional[str] = ...) -> None: ...
