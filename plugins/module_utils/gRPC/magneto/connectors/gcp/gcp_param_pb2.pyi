from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskDeviceInfo(_message.Message):
    __slots__ = ("device_name", "persistent_disk_id", "disk_size_bytes", "disk_type", "disk_auto_delete", "is_encrypted", "snapshot_id", "interface", "mode", "auto_delete", "region", "replica_zones")
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    device_name: str
    persistent_disk_id: str
    disk_size_bytes: int
    disk_type: str
    disk_auto_delete: bool
    is_encrypted: bool
    snapshot_id: str
    interface: str
    mode: str
    auto_delete: bool
    region: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, device_name: _Optional[str] = ..., persistent_disk_id: _Optional[str] = ..., disk_size_bytes: _Optional[int] = ..., disk_type: _Optional[str] = ..., disk_auto_delete: bool = ..., is_encrypted: bool = ..., snapshot_id: _Optional[str] = ..., interface: _Optional[str] = ..., mode: _Optional[str] = ..., auto_delete: bool = ..., region: _Optional[str] = ..., replica_zones: _Optional[_Iterable[str]] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CreateDiskSnapshotArg(_message.Message):
    __slots__ = ("disk_name", "snapshot_name", "region", "metadata")
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    disk_name: str
    snapshot_name: str
    region: str
    metadata: KeyValue
    def __init__(self, disk_name: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., region: _Optional[str] = ..., metadata: _Optional[_Union[KeyValue, _Mapping]] = ...) -> None: ...

class CreateDiskSnapshotResult(_message.Message):
    __slots__ = ("snapshot_result_vec",)
    class DiskSnapshotResult(_message.Message):
        __slots__ = ("snapshot_name", "disk_name", "size_bytes")
        SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        snapshot_name: str
        disk_name: str
        size_bytes: int
        def __init__(self, snapshot_name: _Optional[str] = ..., disk_name: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    SNAPSHOT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_result_vec: _containers.RepeatedCompositeFieldContainer[CreateDiskSnapshotResult.DiskSnapshotResult]
    def __init__(self, snapshot_result_vec: _Optional[_Iterable[_Union[CreateDiskSnapshotResult.DiskSnapshotResult, _Mapping]]] = ...) -> None: ...

class FetchSnapshotsInfoResult(_message.Message):
    __slots__ = ("snapshot_info_vec",)
    class SnapshotDetails(_message.Message):
        __slots__ = ("snapshot_name", "disk_name", "status", "disk_size_gb")
        class SnapshotStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kPending: _ClassVar[FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus]
            kComplete: _ClassVar[FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus]
            kError: _ClassVar[FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus]
            kNotSet: _ClassVar[FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus]
        kPending: FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus
        kComplete: FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus
        kError: FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus
        kNotSet: FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus
        SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        snapshot_name: str
        disk_name: str
        status: FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus
        disk_size_gb: int
        def __init__(self, snapshot_name: _Optional[str] = ..., disk_name: _Optional[str] = ..., status: _Optional[_Union[FetchSnapshotsInfoResult.SnapshotDetails.SnapshotStatus, str]] = ..., disk_size_gb: _Optional[int] = ...) -> None: ...
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[FetchSnapshotsInfoResult.SnapshotDetails]
    def __init__(self, snapshot_info_vec: _Optional[_Iterable[_Union[FetchSnapshotsInfoResult.SnapshotDetails, _Mapping]]] = ...) -> None: ...

class CreateDiskResult(_message.Message):
    __slots__ = ("name", "disk_size_gibs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GIBS_FIELD_NUMBER: _ClassVar[int]
    name: str
    disk_size_gibs: int
    def __init__(self, name: _Optional[str] = ..., disk_size_gibs: _Optional[int] = ...) -> None: ...
