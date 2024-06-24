from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VolumeInfo(_message.Message):
    __slots__ = ("guid", "name", "last_snapshot_uuid", "last_snapshot_time_micros", "last_snapshot_size_bytes", "is_snapshot_readable", "delta_info", "snapshot_backup_components_xml", "snapshot_writer_metadata_xml", "snapshot_device")
    class DeltaInfo(_message.Message):
        __slots__ = ("base_snapshot_uuid", "block_size_bytes", "bitmap")
        BASE_SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        BITMAP_FIELD_NUMBER: _ClassVar[int]
        base_snapshot_uuid: str
        block_size_bytes: int
        bitmap: bytes
        def __init__(self, base_snapshot_uuid: _Optional[str] = ..., block_size_bytes: _Optional[int] = ..., bitmap: _Optional[bytes] = ...) -> None: ...
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_TIME_MICROS_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_SNAPSHOT_READABLE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_BACKUP_COMPONENTS_XML_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_WRITER_METADATA_XML_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    last_snapshot_uuid: str
    last_snapshot_time_micros: int
    last_snapshot_size_bytes: int
    is_snapshot_readable: bool
    delta_info: VolumeInfo.DeltaInfo
    snapshot_backup_components_xml: bytes
    snapshot_writer_metadata_xml: bytes
    snapshot_device: str
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., last_snapshot_uuid: _Optional[str] = ..., last_snapshot_time_micros: _Optional[int] = ..., last_snapshot_size_bytes: _Optional[int] = ..., is_snapshot_readable: bool = ..., delta_info: _Optional[_Union[VolumeInfo.DeltaInfo, _Mapping]] = ..., snapshot_backup_components_xml: _Optional[bytes] = ..., snapshot_writer_metadata_xml: _Optional[bytes] = ..., snapshot_device: _Optional[str] = ...) -> None: ...

class QueryVolumesArg(_message.Message):
    __slots__ = ("restrict_to_tracked_volumes",)
    RESTRICT_TO_TRACKED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    restrict_to_tracked_volumes: bool
    def __init__(self, restrict_to_tracked_volumes: bool = ...) -> None: ...

class QueryVolumesResult(_message.Message):
    __slots__ = ("volume_vec",)
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[VolumeInfo, _Mapping]]] = ...) -> None: ...

class SnapshotVolumesArg(_message.Message):
    __slots__ = ("volume_vec", "include_volume_info_in_result", "excluded_vss_writers")
    class Volume(_message.Message):
        __slots__ = ("guid",)
        GUID_FIELD_NUMBER: _ClassVar[int]
        guid: str
        def __init__(self, guid: _Optional[str] = ...) -> None: ...
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VOLUME_INFO_IN_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_VSS_WRITERS_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[SnapshotVolumesArg.Volume]
    include_volume_info_in_result: bool
    excluded_vss_writers: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[SnapshotVolumesArg.Volume, _Mapping]]] = ..., include_volume_info_in_result: bool = ..., excluded_vss_writers: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SnapshotVolumesResult(_message.Message):
    __slots__ = ("snapshot_vec",)
    class SnapshotInfo(_message.Message):
        __slots__ = ("guid", "error", "snapshot_uuid", "vol_info", "snapshot_device")
        GUID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
        VOL_INFO_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_DEVICE_FIELD_NUMBER: _ClassVar[int]
        guid: str
        error: bool
        snapshot_uuid: str
        vol_info: VolumeInfo
        snapshot_device: str
        def __init__(self, guid: _Optional[str] = ..., error: bool = ..., snapshot_uuid: _Optional[str] = ..., vol_info: _Optional[_Union[VolumeInfo, _Mapping]] = ..., snapshot_device: _Optional[str] = ...) -> None: ...
    SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_vec: _containers.RepeatedCompositeFieldContainer[SnapshotVolumesResult.SnapshotInfo]
    def __init__(self, snapshot_vec: _Optional[_Iterable[_Union[SnapshotVolumesResult.SnapshotInfo, _Mapping]]] = ...) -> None: ...

class ReleaseSnapshotsArg(_message.Message):
    __slots__ = ("entry_vec",)
    class Entry(_message.Message):
        __slots__ = ("guid", "snapshot_uuid")
        GUID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
        guid: str
        snapshot_uuid: str
        def __init__(self, guid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ...) -> None: ...
    ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    entry_vec: _containers.RepeatedCompositeFieldContainer[ReleaseSnapshotsArg.Entry]
    def __init__(self, entry_vec: _Optional[_Iterable[_Union[ReleaseSnapshotsArg.Entry, _Mapping]]] = ...) -> None: ...

class StopTrackingVolumeArg(_message.Message):
    __slots__ = ("volume_guid",)
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    volume_guid: str
    def __init__(self, volume_guid: _Optional[str] = ...) -> None: ...

class StopTrackingVolumeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseSnapshotsResult(_message.Message):
    __slots__ = ("status_vec",)
    STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    status_vec: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, status_vec: _Optional[_Iterable[bool]] = ...) -> None: ...
