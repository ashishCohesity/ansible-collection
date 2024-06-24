from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateWALStatus(_message.Message):
    __slots__ = ("disk_id", "source_location", "source_incarnation", "target_location", "target_incarnation", "all_chunk_files_migrated", "resume_from_cookie", "num_chunk_files_migrated", "start_usecs")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    ALL_CHUNK_FILES_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    RESUME_FROM_COOKIE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    START_USECS_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    source_location: _cluster_config_pb2.ClusterConfigProto.Disk.ChunkRepoWALLocation
    source_incarnation: int
    target_location: _cluster_config_pb2.ClusterConfigProto.Disk.ChunkRepoWALLocation
    target_incarnation: int
    all_chunk_files_migrated: bool
    resume_from_cookie: str
    num_chunk_files_migrated: int
    start_usecs: int
    def __init__(self, disk_id: _Optional[int] = ..., source_location: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Disk.ChunkRepoWALLocation, str]] = ..., source_incarnation: _Optional[int] = ..., target_location: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Disk.ChunkRepoWALLocation, str]] = ..., target_incarnation: _Optional[int] = ..., all_chunk_files_migrated: bool = ..., resume_from_cookie: _Optional[str] = ..., num_chunk_files_migrated: _Optional[int] = ..., start_usecs: _Optional[int] = ...) -> None: ...

class GCStatus(_message.Message):
    __slots__ = ("disk_id", "gc_complete_until_incarnation")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    GC_COMPLETE_UNTIL_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    gc_complete_until_incarnation: int
    def __init__(self, disk_id: _Optional[int] = ..., gc_complete_until_incarnation: _Optional[int] = ...) -> None: ...
