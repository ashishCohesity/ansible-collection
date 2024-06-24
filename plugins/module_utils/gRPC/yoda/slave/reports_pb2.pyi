from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityInfo(_message.Message):
    __slots__ = ("name", "logical_size_bytes", "count", "estimate", "depth", "time_taken_usecs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    logical_size_bytes: int
    count: int
    estimate: float
    depth: int
    time_taken_usecs: int
    def __init__(self, name: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., count: _Optional[int] = ..., estimate: _Optional[float] = ..., depth: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ...) -> None: ...

class ObjectReport(_message.Message):
    __slots__ = ("top_files", "categories", "version", "hist_states", "slow_directories")
    class Entry(_message.Message):
        __slots__ = ("snapshot_timestamp_usecs", "entities")
        SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        snapshot_timestamp_usecs: int
        entities: _containers.RepeatedCompositeFieldContainer[EntityInfo]
        def __init__(self, snapshot_timestamp_usecs: _Optional[int] = ..., entities: _Optional[_Iterable[_Union[EntityInfo, _Mapping]]] = ...) -> None: ...
    class HistogramState(_message.Message):
        __slots__ = ("type", "sampling_factor", "histogram")
        class HistogramEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFileExtension: _ClassVar[ObjectReport.HistogramState.HistogramEntityType]
            kDirectory: _ClassVar[ObjectReport.HistogramState.HistogramEntityType]
            kAddedFileExtension: _ClassVar[ObjectReport.HistogramState.HistogramEntityType]
            kDeletedFileExtension: _ClassVar[ObjectReport.HistogramState.HistogramEntityType]
        kFileExtension: ObjectReport.HistogramState.HistogramEntityType
        kDirectory: ObjectReport.HistogramState.HistogramEntityType
        kAddedFileExtension: ObjectReport.HistogramState.HistogramEntityType
        kDeletedFileExtension: ObjectReport.HistogramState.HistogramEntityType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SAMPLING_FACTOR_FIELD_NUMBER: _ClassVar[int]
        HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        type: ObjectReport.HistogramState.HistogramEntityType
        sampling_factor: float
        histogram: ObjectReport.Entry
        def __init__(self, type: _Optional[_Union[ObjectReport.HistogramState.HistogramEntityType, str]] = ..., sampling_factor: _Optional[float] = ..., histogram: _Optional[_Union[ObjectReport.Entry, _Mapping]] = ...) -> None: ...
    TOP_FILES_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HIST_STATES_FIELD_NUMBER: _ClassVar[int]
    SLOW_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    top_files: _containers.RepeatedCompositeFieldContainer[ObjectReport.Entry]
    categories: _containers.RepeatedCompositeFieldContainer[ObjectReport.Entry]
    version: int
    hist_states: _containers.RepeatedCompositeFieldContainer[ObjectReport.HistogramState]
    slow_directories: _containers.RepeatedCompositeFieldContainer[ObjectReport.Entry]
    def __init__(self, top_files: _Optional[_Iterable[_Union[ObjectReport.Entry, _Mapping]]] = ..., categories: _Optional[_Iterable[_Union[ObjectReport.Entry, _Mapping]]] = ..., version: _Optional[int] = ..., hist_states: _Optional[_Iterable[_Union[ObjectReport.HistogramState, _Mapping]]] = ..., slow_directories: _Optional[_Iterable[_Union[ObjectReport.Entry, _Mapping]]] = ...) -> None: ...

class FileOp(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[FileOp.Type]
        kAdd: _ClassVar[FileOp.Type]
        kDelete: _ClassVar[FileOp.Type]
    kUnknown: FileOp.Type
    kAdd: FileOp.Type
    kDelete: FileOp.Type
    def __init__(self) -> None: ...
