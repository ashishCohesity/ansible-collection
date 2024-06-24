from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileTypeBucket(_message.Message):
    __slots__ = ("file_type_tag", "file_type_bucket_extensions")
    FILE_TYPE_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_BUCKET_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    file_type_tag: str
    file_type_bucket_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_type_tag: _Optional[str] = ..., file_type_bucket_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class FileSizeBucket(_message.Message):
    __slots__ = ("file_size_tag", "file_size_start", "file_size_end")
    FILE_SIZE_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_START_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_END_FIELD_NUMBER: _ClassVar[int]
    file_size_tag: str
    file_size_start: int
    file_size_end: int
    def __init__(self, file_size_tag: _Optional[str] = ..., file_size_start: _Optional[int] = ..., file_size_end: _Optional[int] = ...) -> None: ...

class AccessTimeBucket(_message.Message):
    __slots__ = ("access_time_tag", "access_time_start", "access_time_end")
    ACCESS_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_START_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_END_FIELD_NUMBER: _ClassVar[int]
    access_time_tag: str
    access_time_start: int
    access_time_end: int
    def __init__(self, access_time_tag: _Optional[str] = ..., access_time_start: _Optional[int] = ..., access_time_end: _Optional[int] = ...) -> None: ...

class ModTimeBucket(_message.Message):
    __slots__ = ("mod_time_tag", "mod_time_start", "mod_time_end")
    MOD_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_START_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_END_FIELD_NUMBER: _ClassVar[int]
    mod_time_tag: str
    mod_time_start: int
    mod_time_end: int
    def __init__(self, mod_time_tag: _Optional[str] = ..., mod_time_start: _Optional[int] = ..., mod_time_end: _Optional[int] = ...) -> None: ...

class ProtoCubeCell(_message.Message):
    __slots__ = ("file_type_tag", "file_size_tag", "access_time_tag", "mod_time_tag", "file_count", "total_size", "cell_id")
    FILE_TYPE_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_TAG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    file_type_tag: str
    file_size_tag: str
    access_time_tag: str
    mod_time_tag: str
    file_count: int
    total_size: int
    cell_id: int
    def __init__(self, file_type_tag: _Optional[str] = ..., file_size_tag: _Optional[str] = ..., access_time_tag: _Optional[str] = ..., mod_time_tag: _Optional[str] = ..., file_count: _Optional[int] = ..., total_size: _Optional[int] = ..., cell_id: _Optional[int] = ...) -> None: ...

class ProtoCubeAttributes(_message.Message):
    __slots__ = ("dimension_nr", "file_type_buckets", "file_size_buckets", "access_time_buckets", "mod_time_buckets")
    DIMENSION_NR_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    dimension_nr: int
    file_type_buckets: _containers.RepeatedCompositeFieldContainer[FileTypeBucket]
    file_size_buckets: _containers.RepeatedCompositeFieldContainer[FileSizeBucket]
    access_time_buckets: _containers.RepeatedCompositeFieldContainer[AccessTimeBucket]
    mod_time_buckets: _containers.RepeatedCompositeFieldContainer[ModTimeBucket]
    def __init__(self, dimension_nr: _Optional[int] = ..., file_type_buckets: _Optional[_Iterable[_Union[FileTypeBucket, _Mapping]]] = ..., file_size_buckets: _Optional[_Iterable[_Union[FileSizeBucket, _Mapping]]] = ..., access_time_buckets: _Optional[_Iterable[_Union[AccessTimeBucket, _Mapping]]] = ..., mod_time_buckets: _Optional[_Iterable[_Union[ModTimeBucket, _Mapping]]] = ...) -> None: ...

class EntitySamplingRule(_message.Message):
    __slots__ = ("entity_type", "metric")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    entity_type: _directory_walker_pb2.EntityMetadata.EntityType
    metric: _containers.RepeatedScalarFieldContainer[ProtoCube.MetricType]
    def __init__(self, entity_type: _Optional[_Union[_directory_walker_pb2.EntityMetadata.EntityType, str]] = ..., metric: _Optional[_Iterable[_Union[ProtoCube.MetricType, str]]] = ...) -> None: ...

class EntityStatPolicy(_message.Message):
    __slots__ = ("policy_record",)
    POLICY_RECORD_FIELD_NUMBER: _ClassVar[int]
    policy_record: _containers.RepeatedCompositeFieldContainer[EntitySamplingRule]
    def __init__(self, policy_record: _Optional[_Iterable[_Union[EntitySamplingRule, _Mapping]]] = ...) -> None: ...

class ProtoCube(_message.Message):
    __slots__ = ("cube_attr", "cellIndexMap", "active_cell_nr", "data_cell", "policy")
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFileCount: _ClassVar[ProtoCube.MetricType]
        kDirCount: _ClassVar[ProtoCube.MetricType]
        kTotalSize: _ClassVar[ProtoCube.MetricType]
    kFileCount: ProtoCube.MetricType
    kDirCount: ProtoCube.MetricType
    kTotalSize: ProtoCube.MetricType
    CUBE_ATTR_FIELD_NUMBER: _ClassVar[int]
    CELLINDEXMAP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CELL_NR_FIELD_NUMBER: _ClassVar[int]
    DATA_CELL_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    cube_attr: ProtoCubeAttributes
    cellIndexMap: _containers.RepeatedScalarFieldContainer[int]
    active_cell_nr: int
    data_cell: _containers.RepeatedCompositeFieldContainer[ProtoCubeCell]
    policy: EntityStatPolicy
    def __init__(self, cube_attr: _Optional[_Union[ProtoCubeAttributes, _Mapping]] = ..., cellIndexMap: _Optional[_Iterable[int]] = ..., active_cell_nr: _Optional[int] = ..., data_cell: _Optional[_Iterable[_Union[ProtoCubeCell, _Mapping]]] = ..., policy: _Optional[_Union[EntityStatPolicy, _Mapping]] = ...) -> None: ...
