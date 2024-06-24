from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBTDeltaType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        None: _ClassVar[CBTDeltaType.Type]
        Used: _ClassVar[CBTDeltaType.Type]
        Incremental: _ClassVar[CBTDeltaType.Type]
    None: CBTDeltaType.Type
    Used: CBTDeltaType.Type
    Incremental: CBTDeltaType.Type
    def __init__(self) -> None: ...

class CBTDeltaInfo(_message.Message):
    __slots__ = ("base_snapshot_uuid", "block_size_bytes", "bitmap", "zlib_compressed", "fullbackup_message", "incremental_after_restart")
    BASE_SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BITMAP_FIELD_NUMBER: _ClassVar[int]
    ZLIB_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    FULLBACKUP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    base_snapshot_uuid: str
    block_size_bytes: int
    bitmap: bytes
    zlib_compressed: bool
    fullbackup_message: str
    incremental_after_restart: bool
    def __init__(self, base_snapshot_uuid: _Optional[str] = ..., block_size_bytes: _Optional[int] = ..., bitmap: _Optional[bytes] = ..., zlib_compressed: bool = ..., fullbackup_message: _Optional[str] = ..., incremental_after_restart: bool = ...) -> None: ...

class WinJobConfig(_message.Message):
    __slots__ = ("objects", "total_bitmap_size")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BITMAP_SIZE_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[WinObjectConfig]
    total_bitmap_size: int
    def __init__(self, objects: _Optional[_Iterable[_Union[WinObjectConfig, _Mapping]]] = ..., total_bitmap_size: _Optional[int] = ...) -> None: ...

class WinObjectConfig(_message.Message):
    __slots__ = ("object_id", "persist_delta_object_id", "bVolume", "jobs")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERSIST_DELTA_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BVOLUME_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    persist_delta_object_id: str
    bVolume: bool
    jobs: _containers.RepeatedCompositeFieldContainer[WinJobInfo]
    def __init__(self, object_id: _Optional[str] = ..., persist_delta_object_id: _Optional[str] = ..., bVolume: bool = ..., jobs: _Optional[_Iterable[_Union[WinJobInfo, _Mapping]]] = ...) -> None: ...

class WinJobInfo(_message.Message):
    __slots__ = ("prev_snapshot_ids", "cluster_job_id", "bitmap_file_size", "bitmap_state", "bitmap_checksum")
    class BitmapState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        bNone: _ClassVar[WinJobInfo.BitmapState]
        bCreated: _ClassVar[WinJobInfo.BitmapState]
        bMerged: _ClassVar[WinJobInfo.BitmapState]
        bInconsistent: _ClassVar[WinJobInfo.BitmapState]
    bNone: WinJobInfo.BitmapState
    bCreated: WinJobInfo.BitmapState
    bMerged: WinJobInfo.BitmapState
    bInconsistent: WinJobInfo.BitmapState
    PREV_SNAPSHOT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    BITMAP_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BITMAP_STATE_FIELD_NUMBER: _ClassVar[int]
    BITMAP_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    prev_snapshot_ids: _containers.RepeatedScalarFieldContainer[str]
    cluster_job_id: str
    bitmap_file_size: int
    bitmap_state: WinJobInfo.BitmapState
    bitmap_checksum: str
    def __init__(self, prev_snapshot_ids: _Optional[_Iterable[str]] = ..., cluster_job_id: _Optional[str] = ..., bitmap_file_size: _Optional[int] = ..., bitmap_state: _Optional[_Union[WinJobInfo.BitmapState, str]] = ..., bitmap_checksum: _Optional[str] = ...) -> None: ...
