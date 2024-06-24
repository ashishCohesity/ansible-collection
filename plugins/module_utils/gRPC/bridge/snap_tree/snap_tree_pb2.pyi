from bridge.base import cloud_pb2 as _cloud_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapTreeValueVersionProto(_message.Message):
    __slots__ = ("creation_epoch", "count")
    CREATION_EPOCH_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    creation_epoch: int
    count: int
    def __init__(self, creation_epoch: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class SnapTreeNodeProto(_message.Message):
    __slots__ = ("tree_id", "node_id", "refcount", "is_deduped", "root_info", "key_child_ptr_vec", "leaf_level_distance", "value_version", "opclock_vec", "archived_node_location_vec", "stub_node_restore_in_progress", "parent_node_tree_id", "parent_node_node_id")
    class RootInfo(_message.Message):
        __slots__ = ("min_degree", "max_degree", "multi_homed", "dynamic_max_degree", "immutable", "min_degree_constraint_relaxed")
        MIN_DEGREE_FIELD_NUMBER: _ClassVar[int]
        MAX_DEGREE_FIELD_NUMBER: _ClassVar[int]
        MULTI_HOMED_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_MAX_DEGREE_FIELD_NUMBER: _ClassVar[int]
        IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
        MIN_DEGREE_CONSTRAINT_RELAXED_FIELD_NUMBER: _ClassVar[int]
        min_degree: int
        max_degree: int
        multi_homed: bool
        dynamic_max_degree: bool
        immutable: bool
        min_degree_constraint_relaxed: bool
        def __init__(self, min_degree: _Optional[int] = ..., max_degree: _Optional[int] = ..., multi_homed: bool = ..., dynamic_max_degree: bool = ..., immutable: bool = ..., min_degree_constraint_relaxed: bool = ...) -> None: ...
    class KeyChildPtr(_message.Message):
        __slots__ = ("key_int", "key_str", "child_ptr_tree_id", "child_ptr_node_id", "child_ptr_cloud_location")
        KEY_INT_FIELD_NUMBER: _ClassVar[int]
        KEY_STR_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
        key_int: int
        key_str: bytes
        child_ptr_tree_id: int
        child_ptr_node_id: int
        child_ptr_cloud_location: _cloud_pb2.CloudNodePtrProto
        def __init__(self, key_int: _Optional[int] = ..., key_str: _Optional[bytes] = ..., child_ptr_tree_id: _Optional[int] = ..., child_ptr_node_id: _Optional[int] = ..., child_ptr_cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ...) -> None: ...
    class ArchivedNodeLocation(_message.Message):
        __slots__ = ("archive_id", "entity_id", "base_archive_id", "object_id", "cluster_id", "segment_start_offset", "node_offset", "domain_id", "cloud_location", "max_bst_leaf_level_distance", "sub_tree_logical_size_bytes", "viewbox_id", "minimum_subtree_retention_timestamp_secs", "sha256_summary_checksum")
        ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        BASE_ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENT_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        NODE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
        MAX_BST_LEAF_LEVEL_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        SUB_TREE_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_SUBTREE_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        SHA256_SUMMARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        archive_id: int
        entity_id: int
        base_archive_id: int
        object_id: int
        cluster_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
        segment_start_offset: int
        node_offset: int
        domain_id: int
        cloud_location: _cloud_pb2.CloudNodePtrProto
        max_bst_leaf_level_distance: int
        sub_tree_logical_size_bytes: int
        viewbox_id: int
        minimum_subtree_retention_timestamp_secs: int
        sha256_summary_checksum: bytes
        def __init__(self, archive_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., base_archive_id: _Optional[int] = ..., object_id: _Optional[int] = ..., cluster_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., segment_start_offset: _Optional[int] = ..., node_offset: _Optional[int] = ..., domain_id: _Optional[int] = ..., cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., max_bst_leaf_level_distance: _Optional[int] = ..., sub_tree_logical_size_bytes: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., minimum_subtree_retention_timestamp_secs: _Optional[int] = ..., sha256_summary_checksum: _Optional[bytes] = ...) -> None: ...
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REFCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_DEDUPED_FIELD_NUMBER: _ClassVar[int]
    ROOT_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_CHILD_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    LEAF_LEVEL_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_NODE_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    STUB_NODE_RESTORE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    node_id: int
    refcount: int
    is_deduped: bool
    root_info: SnapTreeNodeProto.RootInfo
    key_child_ptr_vec: _containers.RepeatedCompositeFieldContainer[SnapTreeNodeProto.KeyChildPtr]
    leaf_level_distance: int
    value_version: SnapTreeValueVersionProto
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    archived_node_location_vec: _containers.RepeatedCompositeFieldContainer[SnapTreeNodeProto.ArchivedNodeLocation]
    stub_node_restore_in_progress: bool
    parent_node_tree_id: int
    parent_node_node_id: int
    def __init__(self, tree_id: _Optional[int] = ..., node_id: _Optional[int] = ..., refcount: _Optional[int] = ..., is_deduped: bool = ..., root_info: _Optional[_Union[SnapTreeNodeProto.RootInfo, _Mapping]] = ..., key_child_ptr_vec: _Optional[_Iterable[_Union[SnapTreeNodeProto.KeyChildPtr, _Mapping]]] = ..., leaf_level_distance: _Optional[int] = ..., value_version: _Optional[_Union[SnapTreeValueVersionProto, _Mapping]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., archived_node_location_vec: _Optional[_Iterable[_Union[SnapTreeNodeProto.ArchivedNodeLocation, _Mapping]]] = ..., stub_node_restore_in_progress: bool = ..., parent_node_tree_id: _Optional[int] = ..., parent_node_node_id: _Optional[int] = ...) -> None: ...

class SnapTreeTraversalCookieProto(_message.Message):
    __slots__ = ("cookie_map",)
    class SubTreeCookie(_message.Message):
        __slots__ = ("key_int", "key_str", "is_sub_tree_traversed")
        KEY_INT_FIELD_NUMBER: _ClassVar[int]
        KEY_STR_FIELD_NUMBER: _ClassVar[int]
        IS_SUB_TREE_TRAVERSED_FIELD_NUMBER: _ClassVar[int]
        key_int: int
        key_str: str
        is_sub_tree_traversed: bool
        def __init__(self, key_int: _Optional[int] = ..., key_str: _Optional[str] = ..., is_sub_tree_traversed: bool = ...) -> None: ...
    class CookieMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SnapTreeTraversalCookieProto.SubTreeCookie
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SnapTreeTraversalCookieProto.SubTreeCookie, _Mapping]] = ...) -> None: ...
    COOKIE_MAP_FIELD_NUMBER: _ClassVar[int]
    cookie_map: _containers.MessageMap[int, SnapTreeTraversalCookieProto.SubTreeCookie]
    def __init__(self, cookie_map: _Optional[_Mapping[int, SnapTreeTraversalCookieProto.SubTreeCookie]] = ...) -> None: ...

class SnapTreeKeyOperation(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdded: _ClassVar[SnapTreeKeyOperation.Type]
        kUpdated: _ClassVar[SnapTreeKeyOperation.Type]
        kRemoved: _ClassVar[SnapTreeKeyOperation.Type]
    kAdded: SnapTreeKeyOperation.Type
    kUpdated: SnapTreeKeyOperation.Type
    kRemoved: SnapTreeKeyOperation.Type
    def __init__(self) -> None: ...

class SnapTreeUpdateReason(_message.Message):
    __slots__ = ("modifying_op", "reason", "refcount", "fix_type")
    class ModifyingOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdjustNodeRefcountOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kBatchUpdateNanoOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kCloneOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kCreateStubNodesNanoOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kCreatorOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kDeduplicateOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kNodeFixerNanoOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kOverwriteSnapTreeOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kRestoreStubNodeContentOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kShadowCopyNanoOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kTouchNodeOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kUpdateLeafNodeOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kUpdateNodeArchivedLocationOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kUpdateOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kUpdateSnapTreeOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
        kUpdateStubNodeRestoreStateNanoOp: _ClassVar[SnapTreeUpdateReason.ModifyingOp]
    kAdjustNodeRefcountOp: SnapTreeUpdateReason.ModifyingOp
    kBatchUpdateNanoOp: SnapTreeUpdateReason.ModifyingOp
    kCloneOp: SnapTreeUpdateReason.ModifyingOp
    kCreateStubNodesNanoOp: SnapTreeUpdateReason.ModifyingOp
    kCreatorOp: SnapTreeUpdateReason.ModifyingOp
    kDeduplicateOp: SnapTreeUpdateReason.ModifyingOp
    kNodeFixerNanoOp: SnapTreeUpdateReason.ModifyingOp
    kOverwriteSnapTreeOp: SnapTreeUpdateReason.ModifyingOp
    kRestoreStubNodeContentOp: SnapTreeUpdateReason.ModifyingOp
    kShadowCopyNanoOp: SnapTreeUpdateReason.ModifyingOp
    kTouchNodeOp: SnapTreeUpdateReason.ModifyingOp
    kUpdateLeafNodeOp: SnapTreeUpdateReason.ModifyingOp
    kUpdateNodeArchivedLocationOp: SnapTreeUpdateReason.ModifyingOp
    kUpdateOp: SnapTreeUpdateReason.ModifyingOp
    kUpdateSnapTreeOp: SnapTreeUpdateReason.ModifyingOp
    kUpdateStubNodeRestoreStateNanoOp: SnapTreeUpdateReason.ModifyingOp
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateRoot: _ClassVar[SnapTreeUpdateReason.Reason]
        kCreateNode: _ClassVar[SnapTreeUpdateReason.Reason]
        kDeleteNode: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateRoot: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateNode: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateParent: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateSrcRoot: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateDestRoot: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateLeafToAdd: _ClassVar[SnapTreeUpdateReason.Reason]
        kCreateLeaf: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateParentToAddLeaf: _ClassVar[SnapTreeUpdateReason.Reason]
        kUpdateParentToDeleteChild: _ClassVar[SnapTreeUpdateReason.Reason]
    kCreateRoot: SnapTreeUpdateReason.Reason
    kCreateNode: SnapTreeUpdateReason.Reason
    kDeleteNode: SnapTreeUpdateReason.Reason
    kUpdateRoot: SnapTreeUpdateReason.Reason
    kUpdateNode: SnapTreeUpdateReason.Reason
    kUpdateParent: SnapTreeUpdateReason.Reason
    kUpdateSrcRoot: SnapTreeUpdateReason.Reason
    kUpdateDestRoot: SnapTreeUpdateReason.Reason
    kUpdateLeafToAdd: SnapTreeUpdateReason.Reason
    kCreateLeaf: SnapTreeUpdateReason.Reason
    kUpdateParentToAddLeaf: SnapTreeUpdateReason.Reason
    kUpdateParentToDeleteChild: SnapTreeUpdateReason.Reason
    class FixType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[SnapTreeUpdateReason.FixType]
        kSplit: _ClassVar[SnapTreeUpdateReason.FixType]
        kLeftJoin: _ClassVar[SnapTreeUpdateReason.FixType]
        kRightJoin: _ClassVar[SnapTreeUpdateReason.FixType]
        kLeftShuffle: _ClassVar[SnapTreeUpdateReason.FixType]
        kRightShuffle: _ClassVar[SnapTreeUpdateReason.FixType]
    kNone: SnapTreeUpdateReason.FixType
    kSplit: SnapTreeUpdateReason.FixType
    kLeftJoin: SnapTreeUpdateReason.FixType
    kRightJoin: SnapTreeUpdateReason.FixType
    kLeftShuffle: SnapTreeUpdateReason.FixType
    kRightShuffle: SnapTreeUpdateReason.FixType
    MODIFYING_OP_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REFCOUNT_FIELD_NUMBER: _ClassVar[int]
    FIX_TYPE_FIELD_NUMBER: _ClassVar[int]
    modifying_op: SnapTreeUpdateReason.ModifyingOp
    reason: SnapTreeUpdateReason.Reason
    refcount: int
    fix_type: SnapTreeUpdateReason.FixType
    def __init__(self, modifying_op: _Optional[_Union[SnapTreeUpdateReason.ModifyingOp, str]] = ..., reason: _Optional[_Union[SnapTreeUpdateReason.Reason, str]] = ..., refcount: _Optional[int] = ..., fix_type: _Optional[_Union[SnapTreeUpdateReason.FixType, str]] = ...) -> None: ...
