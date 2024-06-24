from athena.apps.insight.base import common_pb2 as _common_pb2
from athena.apps.insight.base import directory_walker_pb2 as _directory_walker_pb2
from athena.apps.insight.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectProto(_message.Message):
    __slots__ = ("type", "name", "id", "directory_rel_path", "namespace_root_name", "source_id", "source_path", "protected_source_volume_info", "root_source_id", "file_extensions")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kView: _ClassVar[ObjectProto.Type]
        kVirtualMachine: _ClassVar[ObjectProto.Type]
        kNAS: _ClassVar[ObjectProto.Type]
    kView: ObjectProto.Type
    kVirtualMachine: ObjectProto.Type
    kNAS: ObjectProto.Type
    class ProtectedSourceVolumeInfo(_message.Message):
        __slots__ = ("volume_uid", "volume_name")
        VOLUME_UID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        volume_uid: str
        volume_name: str
        def __init__(self, volume_uid: _Optional[str] = ..., volume_name: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_SOURCE_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    ROOT_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    type: ObjectProto.Type
    name: str
    id: int
    directory_rel_path: str
    namespace_root_name: str
    source_id: int
    source_path: str
    protected_source_volume_info: ObjectProto.ProtectedSourceVolumeInfo
    root_source_id: int
    file_extensions: FileExtensions
    def __init__(self, type: _Optional[_Union[ObjectProto.Type, str]] = ..., name: _Optional[str] = ..., id: _Optional[int] = ..., directory_rel_path: _Optional[str] = ..., namespace_root_name: _Optional[str] = ..., source_id: _Optional[int] = ..., source_path: _Optional[str] = ..., protected_source_volume_info: _Optional[_Union[ObjectProto.ProtectedSourceVolumeInfo, _Mapping]] = ..., root_source_id: _Optional[int] = ..., file_extensions: _Optional[_Union[FileExtensions, _Mapping]] = ...) -> None: ...

class FileExtensions(_message.Message):
    __slots__ = ("file_extension_vec",)
    FILE_EXTENSION_VEC_FIELD_NUMBER: _ClassVar[int]
    file_extension_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_extension_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FileFilterProto(_message.Message):
    __slots__ = ("global_file_extensions_vec", "root_source_file_extensions_map")
    class RootSourceFileExtensionsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FileExtensions
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FileExtensions, _Mapping]] = ...) -> None: ...
    GLOBAL_FILE_EXTENSIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_SOURCE_FILE_EXTENSIONS_MAP_FIELD_NUMBER: _ClassVar[int]
    global_file_extensions_vec: _containers.RepeatedScalarFieldContainer[str]
    root_source_file_extensions_map: _containers.MessageMap[int, FileExtensions]
    def __init__(self, global_file_extensions_vec: _Optional[_Iterable[str]] = ..., root_source_file_extensions_map: _Optional[_Mapping[int, FileExtensions]] = ...) -> None: ...

class TaskStatsProto(_message.Message):
    __slots__ = ("dir_walker_stats", "bytes_indexed", "files_skipped", "files_skipped_details")
    DIR_WALKER_STATS_FIELD_NUMBER: _ClassVar[int]
    BYTES_INDEXED_FIELD_NUMBER: _ClassVar[int]
    FILES_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    FILES_SKIPPED_DETAILS_FIELD_NUMBER: _ClassVar[int]
    dir_walker_stats: _directory_walker_pb2.DirectoryWalkerStatsProto
    bytes_indexed: int
    files_skipped: _common_pb2.CounterProto
    files_skipped_details: _containers.RepeatedCompositeFieldContainer[_common_pb2.CounterProto]
    def __init__(self, dir_walker_stats: _Optional[_Union[_directory_walker_pb2.DirectoryWalkerStatsProto, _Mapping]] = ..., bytes_indexed: _Optional[int] = ..., files_skipped: _Optional[_Union[_common_pb2.CounterProto, _Mapping]] = ..., files_skipped_details: _Optional[_Iterable[_Union[_common_pb2.CounterProto, _Mapping]]] = ...) -> None: ...

class ViewMountMethod(_message.Message):
    __slots__ = ("protocol", "server_ip", "username", "password", "job_run_info")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNFS: _ClassVar[ViewMountMethod.Protocol]
        kSMB: _ClassVar[ViewMountMethod.Protocol]
        kProtectedObject: _ClassVar[ViewMountMethod.Protocol]
    kNFS: ViewMountMethod.Protocol
    kSMB: ViewMountMethod.Protocol
    kProtectedObject: ViewMountMethod.Protocol
    class JobRunInfo(_message.Message):
        __slots__ = ("job_id", "run_id", "job_start_time_usecs")
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        RUN_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        job_id: int
        run_id: int
        job_start_time_usecs: int
        def __init__(self, job_id: _Optional[int] = ..., run_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ...) -> None: ...
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    protocol: ViewMountMethod.Protocol
    server_ip: str
    username: str
    password: str
    job_run_info: ViewMountMethod.JobRunInfo
    def __init__(self, protocol: _Optional[_Union[ViewMountMethod.Protocol, str]] = ..., server_ip: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., job_run_info: _Optional[_Union[ViewMountMethod.JobRunInfo, _Mapping]] = ...) -> None: ...

class TaskProto(_message.Message):
    __slots__ = ("id", "object", "file_filter", "creation_time_nsecs", "start_time_nsecs", "state", "stats", "error", "end_time_nsecs", "view_mount_method")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[TaskProto.State]
        kFinished: _ClassVar[TaskProto.State]
    kRunning: TaskProto.State
    kFinished: TaskProto.State
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    FILE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    END_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_METHOD_FIELD_NUMBER: _ClassVar[int]
    id: int
    object: ObjectProto
    file_filter: FileFilterProto
    creation_time_nsecs: int
    start_time_nsecs: int
    state: TaskProto.State
    stats: TaskStatsProto
    error: _error_pb2.ErrorProto
    end_time_nsecs: int
    view_mount_method: ViewMountMethod
    def __init__(self, id: _Optional[int] = ..., object: _Optional[_Union[ObjectProto, _Mapping]] = ..., file_filter: _Optional[_Union[FileFilterProto, _Mapping]] = ..., creation_time_nsecs: _Optional[int] = ..., start_time_nsecs: _Optional[int] = ..., state: _Optional[_Union[TaskProto.State, str]] = ..., stats: _Optional[_Union[TaskStatsProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_time_nsecs: _Optional[int] = ..., view_mount_method: _Optional[_Union[ViewMountMethod, _Mapping]] = ...) -> None: ...

class SubTaskIdProto(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "incarnation")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    incarnation: int
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., incarnation: _Optional[int] = ...) -> None: ...

class SubTaskSpecProto(_message.Message):
    __slots__ = ("id", "object", "file_filter", "file_slice_vec", "size_bytes", "view_mount_method")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[SubTaskSpecProto.ActionType]
        kAddOrUpdateDocument: _ClassVar[SubTaskSpecProto.ActionType]
        kDeleteDocument: _ClassVar[SubTaskSpecProto.ActionType]
    kNotSet: SubTaskSpecProto.ActionType
    kAddOrUpdateDocument: SubTaskSpecProto.ActionType
    kDeleteDocument: SubTaskSpecProto.ActionType
    class FileSlice(_message.Message):
        __slots__ = ("metadata", "offset", "length", "action")
        METADATA_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        metadata: _directory_walker_pb2.DirectoryWalkerListingEntryProto
        offset: int
        length: int
        action: SubTaskSpecProto.ActionType
        def __init__(self, metadata: _Optional[_Union[_directory_walker_pb2.DirectoryWalkerListingEntryProto, _Mapping]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., action: _Optional[_Union[SubTaskSpecProto.ActionType, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    FILE_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILE_SLICE_VEC_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_METHOD_FIELD_NUMBER: _ClassVar[int]
    id: SubTaskIdProto
    object: ObjectProto
    file_filter: FileFilterProto
    file_slice_vec: _containers.RepeatedCompositeFieldContainer[SubTaskSpecProto.FileSlice]
    size_bytes: int
    view_mount_method: ViewMountMethod
    def __init__(self, id: _Optional[_Union[SubTaskIdProto, _Mapping]] = ..., object: _Optional[_Union[ObjectProto, _Mapping]] = ..., file_filter: _Optional[_Union[FileFilterProto, _Mapping]] = ..., file_slice_vec: _Optional[_Iterable[_Union[SubTaskSpecProto.FileSlice, _Mapping]]] = ..., size_bytes: _Optional[int] = ..., view_mount_method: _Optional[_Union[ViewMountMethod, _Mapping]] = ...) -> None: ...

class SubTaskStateProto(_message.Message):
    __slots__ = ("id", "start_time_nsecs", "state", "error", "end_time_nsecs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[SubTaskStateProto.State]
        kFinished: _ClassVar[SubTaskStateProto.State]
    kRunning: SubTaskStateProto.State
    kFinished: SubTaskStateProto.State
    ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    END_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    id: SubTaskIdProto
    start_time_nsecs: int
    state: SubTaskStateProto.State
    error: _error_pb2.ErrorProto
    end_time_nsecs: int
    def __init__(self, id: _Optional[_Union[SubTaskIdProto, _Mapping]] = ..., start_time_nsecs: _Optional[int] = ..., state: _Optional[_Union[SubTaskStateProto.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_time_nsecs: _Optional[int] = ...) -> None: ...

class SubTaskFileSliceProto(_message.Message):
    __slots__ = ("file_slice", "extracted_file_info")
    class ExtractedFileInfoProto(_message.Message):
        __slots__ = ("relative_file_path", "absolute_file_path", "length", "file_type")
        class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[SubTaskFileSliceProto.ExtractedFileInfoProto.FileType]
            TEXT: _ClassVar[SubTaskFileSliceProto.ExtractedFileInfoProto.FileType]
            SUPPORTED_NON_TEXT: _ClassVar[SubTaskFileSliceProto.ExtractedFileInfoProto.FileType]
            OTHERS: _ClassVar[SubTaskFileSliceProto.ExtractedFileInfoProto.FileType]
        DEFAULT: SubTaskFileSliceProto.ExtractedFileInfoProto.FileType
        TEXT: SubTaskFileSliceProto.ExtractedFileInfoProto.FileType
        SUPPORTED_NON_TEXT: SubTaskFileSliceProto.ExtractedFileInfoProto.FileType
        OTHERS: SubTaskFileSliceProto.ExtractedFileInfoProto.FileType
        RELATIVE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        relative_file_path: str
        absolute_file_path: str
        length: int
        file_type: SubTaskFileSliceProto.ExtractedFileInfoProto.FileType
        def __init__(self, relative_file_path: _Optional[str] = ..., absolute_file_path: _Optional[str] = ..., length: _Optional[int] = ..., file_type: _Optional[_Union[SubTaskFileSliceProto.ExtractedFileInfoProto.FileType, str]] = ...) -> None: ...
    FILE_SLICE_FIELD_NUMBER: _ClassVar[int]
    EXTRACTED_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    file_slice: SubTaskSpecProto.FileSlice
    extracted_file_info: SubTaskFileSliceProto.ExtractedFileInfoProto
    def __init__(self, file_slice: _Optional[_Union[SubTaskSpecProto.FileSlice, _Mapping]] = ..., extracted_file_info: _Optional[_Union[SubTaskFileSliceProto.ExtractedFileInfoProto, _Mapping]] = ...) -> None: ...

class IndexingState(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAnalyzing: _ClassVar[IndexingState.State]
        kIndexing: _ClassVar[IndexingState.State]
        kCompleted: _ClassVar[IndexingState.State]
        kPaused: _ClassVar[IndexingState.State]
    kAnalyzing: IndexingState.State
    kIndexing: IndexingState.State
    kCompleted: IndexingState.State
    kPaused: IndexingState.State
    def __init__(self) -> None: ...

class FileExtensionsSource(_message.Message):
    __slots__ = ()
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kObjectFileExtensions: _ClassVar[FileExtensionsSource.Source]
        kRootSourceFileExtensions: _ClassVar[FileExtensionsSource.Source]
        kGlobalFileExtensions: _ClassVar[FileExtensionsSource.Source]
    kObjectFileExtensions: FileExtensionsSource.Source
    kRootSourceFileExtensions: FileExtensionsSource.Source
    kGlobalFileExtensions: FileExtensionsSource.Source
    def __init__(self) -> None: ...
