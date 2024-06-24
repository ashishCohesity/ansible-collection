from bridge.base import apollo_actions_base_pb2 as _apollo_actions_base_pb2
from bridge.quota import quota_tree_metadata_pb2 as _quota_tree_metadata_pb2
from bridge.smb_portal import smb_portal_metadata_pb2 as _smb_portal_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdjustNodeRefcountProto(_message.Message):
    __slots__ = ("tree_id", "is_view_snap_tree_node_deprecated", "node_id", "adjust_refcount_amount", "expected_scribe_version", "is_blob_snaptree_root", "snap_tree_name", "is_view_snaptree_root")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_NODE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ADJUST_REFCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_SNAPTREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAPTREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    is_view_snap_tree_node_deprecated: bool
    node_id: int
    adjust_refcount_amount: int
    expected_scribe_version: int
    is_blob_snaptree_root: bool
    snap_tree_name: _apollo_actions_base_pb2.SnapTreeName
    is_view_snaptree_root: bool
    def __init__(self, tree_id: _Optional[int] = ..., is_view_snap_tree_node_deprecated: bool = ..., node_id: _Optional[int] = ..., adjust_refcount_amount: _Optional[int] = ..., expected_scribe_version: _Optional[int] = ..., is_blob_snaptree_root: bool = ..., snap_tree_name: _Optional[_Union[_apollo_actions_base_pb2.SnapTreeName, str]] = ..., is_view_snaptree_root: bool = ...) -> None: ...

class FreeBlobByteRange(_message.Message):
    __slots__ = ("blob_snap_tree_id", "range", "verify_brick_info_vec")
    class Range(_message.Message):
        __slots__ = ("offset", "count")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        offset: int
        count: int
        def __init__(self, offset: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    class BrickInfo(_message.Message):
        __slots__ = ("brick_number", "brick_value_version")
        BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        BRICK_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        brick_number: int
        brick_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, brick_number: _Optional[int] = ..., brick_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_BRICK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    range: FreeBlobByteRange.Range
    verify_brick_info_vec: _containers.RepeatedCompositeFieldContainer[FreeBlobByteRange.BrickInfo]
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., range: _Optional[_Union[FreeBlobByteRange.Range, _Mapping]] = ..., verify_brick_info_vec: _Optional[_Iterable[_Union[FreeBlobByteRange.BrickInfo, _Mapping]]] = ...) -> None: ...

class FixUserQuotaUsage(_message.Message):
    __slots__ = ("view_id", "user_entry_vec", "quota_usage_snaptree_id")
    class FixUserQuotaUsageEntry(_message.Message):
        __slots__ = ("user_id", "usage_in_bytes", "expected_version")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
        user_id: _quota_tree_metadata_pb2.QuotaUID
        usage_in_bytes: int
        expected_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, user_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., usage_in_bytes: _Optional[int] = ..., expected_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    QUOTA_USAGE_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    user_entry_vec: _containers.RepeatedCompositeFieldContainer[FixUserQuotaUsage.FixUserQuotaUsageEntry]
    quota_usage_snaptree_id: int
    def __init__(self, view_id: _Optional[int] = ..., user_entry_vec: _Optional[_Iterable[_Union[FixUserQuotaUsage.FixUserQuotaUsageEntry, _Mapping]]] = ..., quota_usage_snaptree_id: _Optional[int] = ...) -> None: ...

class DeleteUserQuotaUsage(_message.Message):
    __slots__ = ("view_id", "user_entry_vec", "quota_usage_snaptree_id")
    class DeleteUserQuotaUsageEntry(_message.Message):
        __slots__ = ("user_id", "expected_version")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
        user_id: _quota_tree_metadata_pb2.QuotaUID
        expected_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, user_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., expected_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    QUOTA_USAGE_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    user_entry_vec: _containers.RepeatedCompositeFieldContainer[DeleteUserQuotaUsage.DeleteUserQuotaUsageEntry]
    quota_usage_snaptree_id: int
    def __init__(self, view_id: _Optional[int] = ..., user_entry_vec: _Optional[_Iterable[_Union[DeleteUserQuotaUsage.DeleteUserQuotaUsageEntry, _Mapping]]] = ..., quota_usage_snaptree_id: _Optional[int] = ...) -> None: ...

class DeleteExpiredSmbSession(_message.Message):
    __slots__ = ("session_id", "entities")
    class EntityInfo(_message.Message):
        __slots__ = ("entity_id", "entity_id_proto")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_PROTO_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        entity_id_proto: _smb_portal_metadata_pb2.SmbEntityIdProto
        def __init__(self, entity_id: _Optional[int] = ..., entity_id_proto: _Optional[_Union[_smb_portal_metadata_pb2.SmbEntityIdProto, _Mapping]] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    entities: _containers.RepeatedCompositeFieldContainer[DeleteExpiredSmbSession.EntityInfo]
    def __init__(self, session_id: _Optional[int] = ..., entities: _Optional[_Iterable[_Union[DeleteExpiredSmbSession.EntityInfo, _Mapping]]] = ...) -> None: ...

class DeleteView(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class FixView(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class FixEntityHandle(_message.Message):
    __slots__ = ("view_id", "root_inode_id", "entity_id", "snap_fs_intent", "s3_intent", "s3_empty_dir_deletion")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_INTENT_FIELD_NUMBER: _ClassVar[int]
    S3_INTENT_FIELD_NUMBER: _ClassVar[int]
    S3_EMPTY_DIR_DELETION_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    root_inode_id: int
    entity_id: int
    snap_fs_intent: bool
    s3_intent: bool
    s3_empty_dir_deletion: bool
    def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., snap_fs_intent: bool = ..., s3_intent: bool = ..., s3_empty_dir_deletion: bool = ...) -> None: ...
