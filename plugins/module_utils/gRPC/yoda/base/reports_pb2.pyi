from bridge.snap_fs.utils import track_data_pb2 as _track_data_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OSType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[OSType.Type]
        kLinux: _ClassVar[OSType.Type]
        kWindows: _ClassVar[OSType.Type]
    kUnknown: OSType.Type
    kLinux: OSType.Type
    kWindows: OSType.Type
    def __init__(self) -> None: ...

class TimestampedSize(_message.Message):
    __slots__ = ("snapshot_time_usecs", "logical_size_bytes", "object_count", "primary_physical_size_bytes", "delta_size_bytes")
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    snapshot_time_usecs: int
    logical_size_bytes: int
    object_count: int
    primary_physical_size_bytes: int
    delta_size_bytes: int
    def __init__(self, snapshot_time_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., object_count: _Optional[int] = ..., primary_physical_size_bytes: _Optional[int] = ..., delta_size_bytes: _Optional[int] = ...) -> None: ...

class EntityUsageInfo(_message.Message):
    __slots__ = ("object_name", "usage")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    usage: _containers.RepeatedCompositeFieldContainer[TimestampedSize]
    def __init__(self, object_name: _Optional[str] = ..., usage: _Optional[_Iterable[_Union[TimestampedSize, _Mapping]]] = ...) -> None: ...

class ObjectTopFilesReport(_message.Message):
    __slots__ = ("top_files_by_size",)
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    TOP_FILES_BY_SIZE_FIELD_NUMBER: _ClassVar[int]
    top_files_by_size: _containers.RepeatedCompositeFieldContainer[EntityUsageInfo]
    def __init__(self, top_files_by_size: _Optional[_Iterable[_Union[EntityUsageInfo, _Mapping]]] = ...) -> None: ...

class TopFilesReport(_message.Message):
    __slots__ = ("top_files",)
    class Entry(_message.Message):
        __slots__ = ("filename", "object_id", "registered_source", "registered_source_hash", "view_box_id", "latest_snapshot_timestamp_usecs", "logical_size_bytes", "history")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        LATEST_SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        HISTORY_FIELD_NUMBER: _ClassVar[int]
        filename: str
        object_id: _entity_pb2.EntityProto
        registered_source: _entity_pb2.EntityProto
        registered_source_hash: int
        view_box_id: int
        latest_snapshot_timestamp_usecs: int
        logical_size_bytes: int
        history: _containers.RepeatedCompositeFieldContainer[TimestampedSize]
        def __init__(self, filename: _Optional[str] = ..., object_id: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., registered_source_hash: _Optional[int] = ..., view_box_id: _Optional[int] = ..., latest_snapshot_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., history: _Optional[_Iterable[_Union[TimestampedSize, _Mapping]]] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    TOP_FILES_FIELD_NUMBER: _ClassVar[int]
    top_files: _containers.RepeatedCompositeFieldContainer[TopFilesReport.Entry]
    def __init__(self, top_files: _Optional[_Iterable[_Union[TopFilesReport.Entry, _Mapping]]] = ...) -> None: ...

class CategoryUsageReport(_message.Message):
    __slots__ = ("categories_by_size",)
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    CATEGORIES_BY_SIZE_FIELD_NUMBER: _ClassVar[int]
    categories_by_size: _containers.RepeatedCompositeFieldContainer[EntityUsageInfo]
    def __init__(self, categories_by_size: _Optional[_Iterable[_Union[EntityUsageInfo, _Mapping]]] = ...) -> None: ...

class SourceGrowthReport(_message.Message):
    __slots__ = ("sources",)
    class Entry(_message.Message):
        __slots__ = ("registered_source", "history")
        REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
        HISTORY_FIELD_NUMBER: _ClassVar[int]
        registered_source: _entity_pb2.EntityProto
        history: _containers.RepeatedCompositeFieldContainer[TimestampedSize]
        def __init__(self, registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., history: _Optional[_Iterable[_Union[TimestampedSize, _Mapping]]] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[SourceGrowthReport.Entry]
    def __init__(self, sources: _Optional[_Iterable[_Union[SourceGrowthReport.Entry, _Mapping]]] = ...) -> None: ...

class ObjectReport(_message.Message):
    __slots__ = ("object_ids",)
    class Entry(_message.Message):
        __slots__ = ("object_id", "history")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        HISTORY_FIELD_NUMBER: _ClassVar[int]
        object_id: _magneto_pb2.MagnetoObjectId
        history: _containers.RepeatedCompositeFieldContainer[TimestampedSize]
        def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., history: _Optional[_Iterable[_Union[TimestampedSize, _Mapping]]] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    object_ids: _containers.RepeatedCompositeFieldContainer[ObjectReport.Entry]
    def __init__(self, object_ids: _Optional[_Iterable[_Union[ObjectReport.Entry, _Mapping]]] = ...) -> None: ...

class OSTypeReport(_message.Message):
    __slots__ = ("os_type", "confidence")
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    os_type: OSType.Type
    confidence: float
    def __init__(self, os_type: _Optional[_Union[OSType.Type, str]] = ..., confidence: _Optional[float] = ...) -> None: ...

class VolumeMappingReport(_message.Message):
    __slots__ = ("mapping_work", "instance_id", "instance_id_vec", "volume_map", "base_instance_id", "skip_disk_or_volume", "boot_volume_info", "vol_mapping_file_mtime_secs", "volume_mount_io_info_mapping_work", "volume_mount_io_info_map")
    class MappingWork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAddMapping: _ClassVar[VolumeMappingReport.MappingWork]
        kCopyMapping: _ClassVar[VolumeMappingReport.MappingWork]
        kRemoveMapping: _ClassVar[VolumeMappingReport.MappingWork]
    kAddMapping: VolumeMappingReport.MappingWork
    kCopyMapping: VolumeMappingReport.MappingWork
    kRemoveMapping: VolumeMappingReport.MappingWork
    class VolumeMountIOInfoMappingWork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAddMountIOInfoMapping: _ClassVar[VolumeMappingReport.VolumeMountIOInfoMappingWork]
        kCopyMountIOInfoMapping: _ClassVar[VolumeMappingReport.VolumeMountIOInfoMappingWork]
        kRemoveMountIOInfoMapping: _ClassVar[VolumeMappingReport.VolumeMountIOInfoMappingWork]
    kAddMountIOInfoMapping: VolumeMappingReport.VolumeMountIOInfoMappingWork
    kCopyMountIOInfoMapping: VolumeMappingReport.VolumeMountIOInfoMappingWork
    kRemoveMountIOInfoMapping: VolumeMappingReport.VolumeMountIOInfoMappingWork
    class VolumeMountIOInfo(_message.Message):
        __slots__ = ("volume_mount_reads",)
        class VolumeMountReadsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _track_data_pb2.ReadIODataProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_track_data_pb2.ReadIODataProto, _Mapping]] = ...) -> None: ...
        VOLUME_MOUNT_READS_FIELD_NUMBER: _ClassVar[int]
        volume_mount_reads: _containers.MessageMap[str, _track_data_pb2.ReadIODataProto]
        def __init__(self, volume_mount_reads: _Optional[_Mapping[str, _track_data_pb2.ReadIODataProto]] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    MAPPING_WORK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MAP_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_DISK_OR_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BOOT_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    VOL_MAPPING_FILE_MTIME_SECS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_IO_INFO_MAPPING_WORK_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_IO_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    mapping_work: VolumeMappingReport.MappingWork
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    volume_map: _volume_info_pb2.VolumeNameMap
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    skip_disk_or_volume: bool
    boot_volume_info: _volume_info_pb2.VolumeInfo
    vol_mapping_file_mtime_secs: int
    volume_mount_io_info_mapping_work: VolumeMappingReport.VolumeMountIOInfoMappingWork
    volume_mount_io_info_map: VolumeMappingReport.VolumeMountIOInfo
    def __init__(self, mapping_work: _Optional[_Union[VolumeMappingReport.MappingWork, str]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., volume_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., skip_disk_or_volume: bool = ..., boot_volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., vol_mapping_file_mtime_secs: _Optional[int] = ..., volume_mount_io_info_mapping_work: _Optional[_Union[VolumeMappingReport.VolumeMountIOInfoMappingWork, str]] = ..., volume_mount_io_info_map: _Optional[_Union[VolumeMappingReport.VolumeMountIOInfo, _Mapping]] = ...) -> None: ...

class VolumeIndexingInfo(_message.Message):
    __slots__ = ("volume_name", "num_entries_indexed", "time_taken_in_vol_indexing_usecs")
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_INDEXED_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_IN_VOL_INDEXING_USECS_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    num_entries_indexed: int
    time_taken_in_vol_indexing_usecs: int
    def __init__(self, volume_name: _Optional[str] = ..., num_entries_indexed: _Optional[int] = ..., time_taken_in_vol_indexing_usecs: _Optional[int] = ...) -> None: ...

class VMIndexingReport(_message.Message):
    __slots__ = ("instance_id", "num_undetected_partitions", "time_taken_in_indexing_usecs", "num_entries_indexed", "volume_info", "tenant_id")
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_UNDETECTED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_IN_INDEXING_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_INDEXED_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    num_undetected_partitions: int
    time_taken_in_indexing_usecs: int
    num_entries_indexed: int
    volume_info: _containers.RepeatedCompositeFieldContainer[VolumeIndexingInfo]
    tenant_id: str
    def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., num_undetected_partitions: _Optional[int] = ..., time_taken_in_indexing_usecs: _Optional[int] = ..., num_entries_indexed: _Optional[int] = ..., volume_info: _Optional[_Iterable[_Union[VolumeIndexingInfo, _Mapping]]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class ObjectIndexReport(_message.Message):
    __slots__ = ("index_report_vec",)
    class Entry(_message.Message):
        __slots__ = ("object_id", "num_detected_volumes", "num_undetected_partitions")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_DETECTED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
        NUM_UNDETECTED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
        object_id: _magneto_pb2.MagnetoObjectId
        num_detected_volumes: int
        num_undetected_partitions: int
        def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., num_detected_volumes: _Optional[int] = ..., num_undetected_partitions: _Optional[int] = ...) -> None: ...
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    INDEX_REPORT_VEC_FIELD_NUMBER: _ClassVar[int]
    index_report_vec: _containers.RepeatedCompositeFieldContainer[ObjectIndexReport.Entry]
    def __init__(self, index_report_vec: _Optional[_Iterable[_Union[ObjectIndexReport.Entry, _Mapping]]] = ...) -> None: ...

class DirectoryIndexingInfo(_message.Message):
    __slots__ = ("name", "depth", "time_taken_usecs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    depth: int
    time_taken_usecs: int
    def __init__(self, name: _Optional[str] = ..., depth: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ...) -> None: ...

class SlowDirectoriesReport(_message.Message):
    __slots__ = ("slow_directories",)
    REPORT_EXT_FIELD_NUMBER: _ClassVar[int]
    report_ext: _descriptor.FieldDescriptor
    SLOW_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    slow_directories: _containers.RepeatedCompositeFieldContainer[DirectoryIndexingInfo]
    def __init__(self, slow_directories: _Optional[_Iterable[_Union[DirectoryIndexingInfo, _Mapping]]] = ...) -> None: ...

class YodaReport(_message.Message):
    __slots__ = ("DEPRECATED_version", "instance_id")
    Extensions: _python_message._ExtensionDict
    DEPRECATED_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_version: int
    instance_id: int
    def __init__(self, DEPRECATED_version: _Optional[int] = ..., instance_id: _Optional[int] = ...) -> None: ...
