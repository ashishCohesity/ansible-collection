from athena.apps.insight.base import common_pb2 as _common_pb2
from athena.apps.insight.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DirectoryWalkerListingEntryProto(_message.Message):
    __slots__ = ("relative_path", "size", "mode", "mtime_nsecs", "symlink_target", "hardlink_leader_relative_path", "isAsciiFile")
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MTIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_LEADER_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    ISASCIIFILE_FIELD_NUMBER: _ClassVar[int]
    relative_path: str
    size: int
    mode: int
    mtime_nsecs: int
    symlink_target: str
    hardlink_leader_relative_path: str
    isAsciiFile: bool
    def __init__(self, relative_path: _Optional[str] = ..., size: _Optional[int] = ..., mode: _Optional[int] = ..., mtime_nsecs: _Optional[int] = ..., symlink_target: _Optional[str] = ..., hardlink_leader_relative_path: _Optional[str] = ..., isAsciiFile: bool = ...) -> None: ...

class DirectoryWalkerStatsProto(_message.Message):
    __slots__ = ("num_entities", "num_files", "num_directories", "num_hard_links", "num_sym_links", "num_bytes", "num_errors")
    NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    NUM_HARD_LINKS_FIELD_NUMBER: _ClassVar[int]
    NUM_SYM_LINKS_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    num_entities: int
    num_files: int
    num_directories: int
    num_hard_links: int
    num_sym_links: int
    num_bytes: int
    num_errors: int
    def __init__(self, num_entities: _Optional[int] = ..., num_files: _Optional[int] = ..., num_directories: _Optional[int] = ..., num_hard_links: _Optional[int] = ..., num_sym_links: _Optional[int] = ..., num_bytes: _Optional[int] = ..., num_errors: _Optional[int] = ...) -> None: ...

class DirectoryWalkerStateProto(_message.Message):
    __slots__ = ("root_dir_relative_path", "listing_file_relative_path", "listing_file_last_sync_offset", "start_time_nsecs", "state", "end_time_nsecs", "error", "stats")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[DirectoryWalkerStateProto.State]
        kFinished: _ClassVar[DirectoryWalkerStateProto.State]
    kRunning: DirectoryWalkerStateProto.State
    kFinished: DirectoryWalkerStateProto.State
    ROOT_DIR_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_LAST_SYNC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    START_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    root_dir_relative_path: str
    listing_file_relative_path: str
    listing_file_last_sync_offset: int
    start_time_nsecs: int
    state: DirectoryWalkerStateProto.State
    end_time_nsecs: int
    error: _error_pb2.ErrorProto
    stats: DirectoryWalkerStatsProto
    def __init__(self, root_dir_relative_path: _Optional[str] = ..., listing_file_relative_path: _Optional[str] = ..., listing_file_last_sync_offset: _Optional[int] = ..., start_time_nsecs: _Optional[int] = ..., state: _Optional[_Union[DirectoryWalkerStateProto.State, str]] = ..., end_time_nsecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[DirectoryWalkerStatsProto, _Mapping]] = ...) -> None: ...

class DirectoryDifferStatsProto(_message.Message):
    __slots__ = ("counter_vec",)
    COUNTER_VEC_FIELD_NUMBER: _ClassVar[int]
    counter_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.CounterProto]
    def __init__(self, counter_vec: _Optional[_Iterable[_Union[_common_pb2.CounterProto, _Mapping]]] = ...) -> None: ...

class DirectoryDifferStateProto(_message.Message):
    __slots__ = ("oldDirWalkResumeEntityRelPath", "newDirWalkResumeEntityRelPath", "start_time_nsecs", "state", "end_time_nsecs", "error", "stats")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[DirectoryDifferStateProto.State]
        kFinished: _ClassVar[DirectoryDifferStateProto.State]
    kRunning: DirectoryDifferStateProto.State
    kFinished: DirectoryDifferStateProto.State
    OLDDIRWALKRESUMEENTITYRELPATH_FIELD_NUMBER: _ClassVar[int]
    NEWDIRWALKRESUMEENTITYRELPATH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    oldDirWalkResumeEntityRelPath: str
    newDirWalkResumeEntityRelPath: str
    start_time_nsecs: int
    state: DirectoryDifferStateProto.State
    end_time_nsecs: int
    error: _error_pb2.ErrorProto
    stats: DirectoryDifferStatsProto
    def __init__(self, oldDirWalkResumeEntityRelPath: _Optional[str] = ..., newDirWalkResumeEntityRelPath: _Optional[str] = ..., start_time_nsecs: _Optional[int] = ..., state: _Optional[_Union[DirectoryDifferStateProto.State, str]] = ..., end_time_nsecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats: _Optional[_Union[DirectoryDifferStatsProto, _Mapping]] = ...) -> None: ...
