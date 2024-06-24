from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from magneto.object_walker import object_metadata_pb2 as _object_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("failed_backup_objects_path_map",)
    class FailedBackupObjectsPathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    OBJECT_STORE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    object_store_snapshot_info: _descriptor.FieldDescriptor
    FAILED_BACKUP_OBJECTS_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    failed_backup_objects_path_map: _containers.ScalarMap[str, bool]
    def __init__(self, failed_backup_objects_path_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class ObjectStoreSubTaskScribeInfo(_message.Message):
    __slots__ = ("finish_line_idx", "hole_idx_map", "running_versions_map", "entities_processed", "bytes_transferred", "bytes_read", "error_map", "total_error_count", "total_non_ignorable_error_count", "has_subtask_progressed", "eh_map")
    class HoleIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class RunningVersionsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class EhMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _entity_handle_pb2.EntityHandleProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    OBJECT_STORE_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    object_store_sub_task_scribe_info: _descriptor.FieldDescriptor
    FINISH_LINE_IDX_FIELD_NUMBER: _ClassVar[int]
    HOLE_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    RUNNING_VERSIONS_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NON_IGNORABLE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_SUBTASK_PROGRESSED_FIELD_NUMBER: _ClassVar[int]
    EH_MAP_FIELD_NUMBER: _ClassVar[int]
    finish_line_idx: int
    hole_idx_map: _containers.ScalarMap[int, bool]
    running_versions_map: _containers.ScalarMap[str, int]
    entities_processed: int
    bytes_transferred: int
    bytes_read: int
    error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    total_error_count: int
    total_non_ignorable_error_count: int
    has_subtask_progressed: bool
    eh_map: _containers.MessageMap[str, _entity_handle_pb2.EntityHandleProto]
    def __init__(self, finish_line_idx: _Optional[int] = ..., hole_idx_map: _Optional[_Mapping[int, bool]] = ..., running_versions_map: _Optional[_Mapping[str, int]] = ..., entities_processed: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., bytes_read: _Optional[int] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., total_error_count: _Optional[int] = ..., total_non_ignorable_error_count: _Optional[int] = ..., has_subtask_progressed: bool = ..., eh_map: _Optional[_Mapping[str, _entity_handle_pb2.EntityHandleProto]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "error", "slave_task_start_time_usecs", "max_concurrent_sub_tasks", "min_multi_part_upload_part_size_bytes", "sub_tasks_vec", "max_work_unit_per_batch", "prefix_results_info", "error_map", "total_error_count")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kPermitGranted: _ClassVar[RestoreInfo.Status]
        kViewCloned: _ClassVar[RestoreInfo.Status]
        kSubTasksFinished: _ClassVar[RestoreInfo.Status]
        kBridgeRestoreEnded: _ClassVar[RestoreInfo.Status]
        kViewDeleted: _ClassVar[RestoreInfo.Status]
        kFinished: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kPermitGranted: RestoreInfo.Status
    kViewCloned: RestoreInfo.Status
    kSubTasksFinished: RestoreInfo.Status
    kBridgeRestoreEnded: RestoreInfo.Status
    kViewDeleted: RestoreInfo.Status
    kFinished: RestoreInfo.Status
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    OBJECT_STORE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    object_store_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    MIN_MULTI_PART_UPLOAD_PART_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_WORK_UNIT_PER_BATCH_FIELD_NUMBER: _ClassVar[int]
    PREFIX_RESULTS_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    error: _error_pb2.ErrorProto
    slave_task_start_time_usecs: int
    max_concurrent_sub_tasks: int
    min_multi_part_upload_part_size_bytes: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    max_work_unit_per_batch: int
    prefix_results_info: _containers.RepeatedCompositeFieldContainer[ObjectStorePrefixInfo]
    error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    total_error_count: int
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., slave_task_start_time_usecs: _Optional[int] = ..., max_concurrent_sub_tasks: _Optional[int] = ..., min_multi_part_upload_part_size_bytes: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., max_work_unit_per_batch: _Optional[int] = ..., prefix_results_info: _Optional[_Iterable[_Union[ObjectStorePrefixInfo, _Mapping]]] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., total_error_count: _Optional[int] = ...) -> None: ...

class ObjectStorePrefixInfo(_message.Message):
    __slots__ = ("prefix_to_recover", "error", "status", "total_error_count")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[ObjectStorePrefixInfo.Status]
        kRunning: _ClassVar[ObjectStorePrefixInfo.Status]
        kSuccessful: _ClassVar[ObjectStorePrefixInfo.Status]
        kFailed: _ClassVar[ObjectStorePrefixInfo.Status]
        kCancelled: _ClassVar[ObjectStorePrefixInfo.Status]
    kNotStarted: ObjectStorePrefixInfo.Status
    kRunning: ObjectStorePrefixInfo.Status
    kSuccessful: ObjectStorePrefixInfo.Status
    kFailed: ObjectStorePrefixInfo.Status
    kCancelled: ObjectStorePrefixInfo.Status
    PREFIX_TO_RECOVER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    prefix_to_recover: str
    error: _error_pb2.ErrorProto
    status: ObjectStorePrefixInfo.Status
    total_error_count: int
    def __init__(self, prefix_to_recover: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[ObjectStorePrefixInfo.Status, str]] = ..., total_error_count: _Optional[int] = ...) -> None: ...

class EntityRange(_message.Message):
    __slots__ = ("start_entity", "end_entity", "start_part_number", "end_part_number")
    START_ENTITY_FIELD_NUMBER: _ClassVar[int]
    END_ENTITY_FIELD_NUMBER: _ClassVar[int]
    START_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    END_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    start_entity: _object_metadata_pb2.ObjectMetadata
    end_entity: _object_metadata_pb2.ObjectMetadata
    start_part_number: int
    end_part_number: int
    def __init__(self, start_entity: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., end_entity: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., start_part_number: _Optional[int] = ..., end_part_number: _Optional[int] = ...) -> None: ...

class ObjectStoreRestoreSubTaskInfo(_message.Message):
    __slots__ = ("is_finished_sub_task", "range", "is_multi_part", "total_error_count", "entities_processed", "total_work_units_to_process")
    OBJECT_STORE_RESTORE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    object_store_restore_sub_task_info: _descriptor.FieldDescriptor
    IS_FINISHED_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_PART_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WORK_UNITS_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
    is_finished_sub_task: bool
    range: EntityRange
    is_multi_part: bool
    total_error_count: int
    entities_processed: int
    total_work_units_to_process: int
    def __init__(self, is_finished_sub_task: bool = ..., range: _Optional[_Union[EntityRange, _Mapping]] = ..., is_multi_part: bool = ..., total_error_count: _Optional[int] = ..., entities_processed: _Optional[int] = ..., total_work_units_to_process: _Optional[int] = ...) -> None: ...

class RestoreScribeInfo(_message.Message):
    __slots__ = ("object_info_map", "last_seen_object")
    class ObjectInfo(_message.Message):
        __slots__ = ("requires_multi_part_upload", "version_info_vec")
        REQUIRES_MULTI_PART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
        VERSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        requires_multi_part_upload: bool
        version_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreScribeInfo.ObjectVersionInfo]
        def __init__(self, requires_multi_part_upload: bool = ..., version_info_vec: _Optional[_Iterable[_Union[RestoreScribeInfo.ObjectVersionInfo, _Mapping]]] = ...) -> None: ...
    class ObjectVersionInfo(_message.Message):
        __slots__ = ("version_id", "source_eh", "is_finalized", "upload_id", "part_info_vec")
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_EH_FIELD_NUMBER: _ClassVar[int]
        IS_FINALIZED_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        PART_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        version_id: str
        source_eh: _entity_handle_pb2.EntityHandleProto
        is_finalized: bool
        upload_id: str
        part_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreScribeInfo.PartInfo]
        def __init__(self, version_id: _Optional[str] = ..., source_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_finalized: bool = ..., upload_id: _Optional[str] = ..., part_info_vec: _Optional[_Iterable[_Union[RestoreScribeInfo.PartInfo, _Mapping]]] = ...) -> None: ...
    class PartInfo(_message.Message):
        __slots__ = ("part_id", "etag")
        PART_ID_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        part_id: int
        etag: str
        def __init__(self, part_id: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...
    class ObjectInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RestoreScribeInfo.ObjectInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreScribeInfo.ObjectInfo, _Mapping]] = ...) -> None: ...
    class ObjectDetail(_message.Message):
        __slots__ = ("key", "version_id", "prev_metadata")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        PREV_METADATA_FIELD_NUMBER: _ClassVar[int]
        key: str
        version_id: str
        prev_metadata: _object_metadata_pb2.ObjectMetadata
        def __init__(self, key: _Optional[str] = ..., version_id: _Optional[str] = ..., prev_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ...) -> None: ...
    OBJECT_STORE_RESTORE_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    object_store_restore_scribe_info: _descriptor.FieldDescriptor
    OBJECT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_OBJECT_FIELD_NUMBER: _ClassVar[int]
    object_info_map: _containers.MessageMap[str, RestoreScribeInfo.ObjectInfo]
    last_seen_object: RestoreScribeInfo.ObjectDetail
    def __init__(self, object_info_map: _Optional[_Mapping[str, RestoreScribeInfo.ObjectInfo]] = ..., last_seen_object: _Optional[_Union[RestoreScribeInfo.ObjectDetail, _Mapping]] = ...) -> None: ...

class S3SubTaskInfo(_message.Message):
    __slots__ = ("range",)
    S3_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    s3_sub_task_info: _descriptor.FieldDescriptor
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: EntityRange
    def __init__(self, range: _Optional[_Union[EntityRange, _Mapping]] = ...) -> None: ...

class ObjectStoreObjectArea(_message.Message):
    __slots__ = ("object_metadata", "upload_id", "part_id", "part_size")
    OBJECT_STORE_OBJECT_AREA_FIELD_NUMBER: _ClassVar[int]
    object_store_object_area: _descriptor.FieldDescriptor
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_ID_FIELD_NUMBER: _ClassVar[int]
    PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    object_metadata: _object_metadata_pb2.ObjectMetadata
    upload_id: str
    part_id: int
    part_size: int
    def __init__(self, object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., upload_id: _Optional[str] = ..., part_id: _Optional[int] = ..., part_size: _Optional[int] = ...) -> None: ...
