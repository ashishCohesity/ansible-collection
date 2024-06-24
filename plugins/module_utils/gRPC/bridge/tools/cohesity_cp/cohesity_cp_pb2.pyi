from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CohesityCpCheckpoint(_message.Message):
    __slots__ = ("state", "chunk_size_bytes", "dir_eh", "remaining_files", "file_in_progress")
    class CopyStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotInitialized: _ClassVar[CohesityCpCheckpoint.CopyStates]
        kInitialized: _ClassVar[CohesityCpCheckpoint.CopyStates]
        kLookupPathDone: _ClassVar[CohesityCpCheckpoint.CopyStates]
        kDirectoryTraversalDone: _ClassVar[CohesityCpCheckpoint.CopyStates]
        kWriteDone: _ClassVar[CohesityCpCheckpoint.CopyStates]
    kNotInitialized: CohesityCpCheckpoint.CopyStates
    kInitialized: CohesityCpCheckpoint.CopyStates
    kLookupPathDone: CohesityCpCheckpoint.CopyStates
    kDirectoryTraversalDone: CohesityCpCheckpoint.CopyStates
    kWriteDone: CohesityCpCheckpoint.CopyStates
    class FileInProgress(_message.Message):
        __slots__ = ("filepath", "file_eh", "logical_size", "offset_info", "chunk_bitmap")
        FILEPATH_FIELD_NUMBER: _ClassVar[int]
        FILE_EH_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_INFO_FIELD_NUMBER: _ClassVar[int]
        CHUNK_BITMAP_FIELD_NUMBER: _ClassVar[int]
        filepath: str
        file_eh: _entity_handle_pb2.EntityHandleProto
        logical_size: int
        offset_info: _containers.RepeatedScalarFieldContainer[int]
        chunk_bitmap: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, filepath: _Optional[str] = ..., file_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., logical_size: _Optional[int] = ..., offset_info: _Optional[_Iterable[int]] = ..., chunk_bitmap: _Optional[_Iterable[bool]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FILES_FIELD_NUMBER: _ClassVar[int]
    FILE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    state: CohesityCpCheckpoint.CopyStates
    chunk_size_bytes: int
    dir_eh: _entity_handle_pb2.EntityHandleProto
    remaining_files: _containers.RepeatedScalarFieldContainer[str]
    file_in_progress: CohesityCpCheckpoint.FileInProgress
    def __init__(self, state: _Optional[_Union[CohesityCpCheckpoint.CopyStates, str]] = ..., chunk_size_bytes: _Optional[int] = ..., dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., remaining_files: _Optional[_Iterable[str]] = ..., file_in_progress: _Optional[_Union[CohesityCpCheckpoint.FileInProgress, _Mapping]] = ...) -> None: ...
