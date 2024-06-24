from bridge.base import error_pb2 as _error_pb2
from bridge.madrox import rsync_snap_tree_diff_pb2 as _rsync_snap_tree_diff_pb2
from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RsyncFileDataSyncWorkProto(_message.Message):
    __slots__ = ("namespace_root_name", "file_dst_path", "is_non_dedup_write", "dedup_range", "payload_bytes", "forwarding_disabled")
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DST_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_NON_DEDUP_WRITE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    namespace_root_name: str
    file_dst_path: bytes
    is_non_dedup_write: bool
    dedup_range: _dedup_range_pb2.DedupRange
    payload_bytes: int
    forwarding_disabled: bool
    def __init__(self, namespace_root_name: _Optional[str] = ..., file_dst_path: _Optional[bytes] = ..., is_non_dedup_write: bool = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., payload_bytes: _Optional[int] = ..., forwarding_disabled: bool = ...) -> None: ...

class RsyncFileDataMissingRangesProto(_message.Message):
    __slots__ = ("range_vec",)
    class Range(_message.Message):
        __slots__ = ("file_offset", "size_bytes")
        FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        file_offset: int
        size_bytes: int
        def __init__(self, file_offset: _Optional[int] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    range_vec: _containers.RepeatedCompositeFieldContainer[RsyncFileDataMissingRangesProto.Range]
    def __init__(self, range_vec: _Optional[_Iterable[_Union[RsyncFileDataMissingRangesProto.Range, _Mapping]]] = ...) -> None: ...

class RsyncApplyEntityActionWorkProto(_message.Message):
    __slots__ = ("namespace_root_name", "apply_action_vec", "is_roll_forward", "expected_final_entries_in_dir")
    class ApplyActionInfo(_message.Message):
        __slots__ = ("operation", "src_path", "target_path", "target_path_metadata", "is_missing_inode_work")
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        SRC_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_PATH_METADATA_FIELD_NUMBER: _ClassVar[int]
        IS_MISSING_INODE_WORK_FIELD_NUMBER: _ClassVar[int]
        operation: _rsync_snap_tree_diff_pb2.RsyncOperation.Type
        src_path: bytes
        target_path: bytes
        target_path_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
        is_missing_inode_work: bool
        def __init__(self, operation: _Optional[_Union[_rsync_snap_tree_diff_pb2.RsyncOperation.Type, str]] = ..., src_path: _Optional[bytes] = ..., target_path: _Optional[bytes] = ..., target_path_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., is_missing_inode_work: bool = ...) -> None: ...
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLY_ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_ROLL_FORWARD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FINAL_ENTRIES_IN_DIR_FIELD_NUMBER: _ClassVar[int]
    namespace_root_name: str
    apply_action_vec: _containers.RepeatedCompositeFieldContainer[RsyncApplyEntityActionWorkProto.ApplyActionInfo]
    is_roll_forward: bool
    expected_final_entries_in_dir: int
    def __init__(self, namespace_root_name: _Optional[str] = ..., apply_action_vec: _Optional[_Iterable[_Union[RsyncApplyEntityActionWorkProto.ApplyActionInfo, _Mapping]]] = ..., is_roll_forward: bool = ..., expected_final_entries_in_dir: _Optional[int] = ...) -> None: ...

class RsyncVerifyDirSyncWorkProto(_message.Message):
    __slots__ = ("root_namespace_name", "tmp_dir_name", "directory_path", "num_children")
    ROOT_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    root_namespace_name: str
    tmp_dir_name: str
    directory_path: bytes
    num_children: int
    def __init__(self, root_namespace_name: _Optional[str] = ..., tmp_dir_name: _Optional[str] = ..., directory_path: _Optional[bytes] = ..., num_children: _Optional[int] = ...) -> None: ...

class RsyncVerifyDirSyncResultProto(_message.Message):
    __slots__ = ("error", "num_children", "child_name_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    num_children: int
    child_name_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., num_children: _Optional[int] = ..., child_name_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RsyncFindMissingEntitiesWorkProto(_message.Message):
    __slots__ = ("find_action_vec", "root_namespace_name")
    class FindActionInfo(_message.Message):
        __slots__ = ("entity_path",)
        ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
        entity_path: bytes
        def __init__(self, entity_path: _Optional[bytes] = ...) -> None: ...
    FIND_ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    find_action_vec: _containers.RepeatedCompositeFieldContainer[RsyncFindMissingEntitiesWorkProto.FindActionInfo]
    root_namespace_name: str
    def __init__(self, find_action_vec: _Optional[_Iterable[_Union[RsyncFindMissingEntitiesWorkProto.FindActionInfo, _Mapping]]] = ..., root_namespace_name: _Optional[str] = ...) -> None: ...

class RsyncFindMissingEntitiesWorkResult(_message.Message):
    __slots__ = ("error", "missing_entity_name_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTITY_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    missing_entity_name_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., missing_entity_name_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...
