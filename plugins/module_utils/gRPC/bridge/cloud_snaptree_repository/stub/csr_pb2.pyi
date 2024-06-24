from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionedObjectProto(_message.Message):
    __slots__ = ("object_id", "object_version", "session_id", "domain_instance_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    object_version: int
    session_id: int
    domain_instance_id: int
    def __init__(self, object_id: _Optional[int] = ..., object_version: _Optional[int] = ..., session_id: _Optional[int] = ..., domain_instance_id: _Optional[int] = ...) -> None: ...

class SnapTreeNodeInfoProto(_message.Message):
    __slots__ = ("snap_tree_node_id", "serialized_snap_tree_node_buffer_ptr", "serialized_snap_tree_node_payload_buffer_ptr", "tree_type", "existing_cloud_object_id", "is_view_snap_tree_node")
    class BufferPtr(_message.Message):
        __slots__ = ("buffer_size", "buffer_offset")
        BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
        BUFFER_OFFSET_FIELD_NUMBER: _ClassVar[int]
        buffer_size: int
        buffer_offset: int
        def __init__(self, buffer_size: _Optional[int] = ..., buffer_offset: _Optional[int] = ...) -> None: ...
    SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SNAP_TREE_NODE_BUFFER_PTR_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SNAP_TREE_NODE_PAYLOAD_BUFFER_PTR_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_NODE_FIELD_NUMBER: _ClassVar[int]
    snap_tree_node_id: int
    serialized_snap_tree_node_buffer_ptr: SnapTreeNodeInfoProto.BufferPtr
    serialized_snap_tree_node_payload_buffer_ptr: SnapTreeNodeInfoProto.BufferPtr
    tree_type: _icebox_pb2.IceboxSnapTreeType
    existing_cloud_object_id: int
    is_view_snap_tree_node: bool
    def __init__(self, snap_tree_node_id: _Optional[int] = ..., serialized_snap_tree_node_buffer_ptr: _Optional[_Union[SnapTreeNodeInfoProto.BufferPtr, _Mapping]] = ..., serialized_snap_tree_node_payload_buffer_ptr: _Optional[_Union[SnapTreeNodeInfoProto.BufferPtr, _Mapping]] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., existing_cloud_object_id: _Optional[int] = ..., is_view_snap_tree_node: bool = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("domain_id", "snap_tree_node_vec", "payload_adler32_checksum", "to_check_status_object_vec", "force_flush", "epoch_id", "to_touch_object_id_vec", "worm_params", "retention_timestamp_secs", "retention_mode")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ADLER32_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    TO_CHECK_STATUS_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_FLUSH_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    TO_TOUCH_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    snap_tree_node_vec: _containers.RepeatedCompositeFieldContainer[SnapTreeNodeInfoProto]
    payload_adler32_checksum: int
    to_check_status_object_vec: _containers.RepeatedCompositeFieldContainer[VersionedObjectProto]
    force_flush: bool
    epoch_id: int
    to_touch_object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    worm_params: _worm_pb2.WORMParams
    retention_timestamp_secs: int
    retention_mode: _worm_pb2.RetentionMode.Type
    def __init__(self, domain_id: _Optional[int] = ..., snap_tree_node_vec: _Optional[_Iterable[_Union[SnapTreeNodeInfoProto, _Mapping]]] = ..., payload_adler32_checksum: _Optional[int] = ..., to_check_status_object_vec: _Optional[_Iterable[_Union[VersionedObjectProto, _Mapping]]] = ..., force_flush: bool = ..., epoch_id: _Optional[int] = ..., to_touch_object_id_vec: _Optional[_Iterable[int]] = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ..., retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("object_node_id_vec", "persisted_object_vec", "unknown_object_vec")
    class ObjectNodeIds(_message.Message):
        __slots__ = ("versioned_object", "node_local_id_vec")
        class SnapTreeNodeLocalId(_message.Message):
            __slots__ = ("node_id", "local_id")
            NODE_ID_FIELD_NUMBER: _ClassVar[int]
            LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
            node_id: int
            local_id: int
            def __init__(self, node_id: _Optional[int] = ..., local_id: _Optional[int] = ...) -> None: ...
        VERSIONED_OBJECT_FIELD_NUMBER: _ClassVar[int]
        NODE_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        versioned_object: VersionedObjectProto
        node_local_id_vec: _containers.RepeatedCompositeFieldContainer[WriteResult.ObjectNodeIds.SnapTreeNodeLocalId]
        def __init__(self, versioned_object: _Optional[_Union[VersionedObjectProto, _Mapping]] = ..., node_local_id_vec: _Optional[_Iterable[_Union[WriteResult.ObjectNodeIds.SnapTreeNodeLocalId, _Mapping]]] = ...) -> None: ...
    OBJECT_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PERSISTED_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    object_node_id_vec: _containers.RepeatedCompositeFieldContainer[WriteResult.ObjectNodeIds]
    persisted_object_vec: _containers.RepeatedCompositeFieldContainer[VersionedObjectProto]
    unknown_object_vec: _containers.RepeatedCompositeFieldContainer[VersionedObjectProto]
    def __init__(self, object_node_id_vec: _Optional[_Iterable[_Union[WriteResult.ObjectNodeIds, _Mapping]]] = ..., persisted_object_vec: _Optional[_Iterable[_Union[VersionedObjectProto, _Mapping]]] = ..., unknown_object_vec: _Optional[_Iterable[_Union[VersionedObjectProto, _Mapping]]] = ...) -> None: ...

class WriteMetadataArg(_message.Message):
    __slots__ = ("domain_id", "cloud_node_prefix_ptr", "tags", "worm_params")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NODE_PREFIX_PTR_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    cloud_node_prefix_ptr: _cloud_pb2.CloudNodePrefixPtrProto
    tags: _containers.ScalarMap[str, str]
    worm_params: _worm_pb2.WORMParams
    def __init__(self, domain_id: _Optional[int] = ..., cloud_node_prefix_ptr: _Optional[_Union[_cloud_pb2.CloudNodePrefixPtrProto, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ...) -> None: ...

class WriteMetadataResult(_message.Message):
    __slots__ = ("cloud_node_prefix_ptr",)
    CLOUD_NODE_PREFIX_PTR_FIELD_NUMBER: _ClassVar[int]
    cloud_node_prefix_ptr: _cloud_pb2.CloudNodePrefixPtrProto
    def __init__(self, cloud_node_prefix_ptr: _Optional[_Union[_cloud_pb2.CloudNodePrefixPtrProto, _Mapping]] = ...) -> None: ...

class FetchCloudObjectIdsArg(_message.Message):
    __slots__ = ("domain_id", "key", "num_ids_to_fetch", "reuse_existing_ids")
    class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCSR: _ClassVar[FetchCloudObjectIdsArg.Key]
        kCCR: _ClassVar[FetchCloudObjectIdsArg.Key]
        kLease: _ClassVar[FetchCloudObjectIdsArg.Key]
    kCSR: FetchCloudObjectIdsArg.Key
    kCCR: FetchCloudObjectIdsArg.Key
    kLease: FetchCloudObjectIdsArg.Key
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_IDS_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    REUSE_EXISTING_IDS_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    key: FetchCloudObjectIdsArg.Key
    num_ids_to_fetch: int
    reuse_existing_ids: bool
    def __init__(self, domain_id: _Optional[int] = ..., key: _Optional[_Union[FetchCloudObjectIdsArg.Key, str]] = ..., num_ids_to_fetch: _Optional[int] = ..., reuse_existing_ids: bool = ...) -> None: ...

class FetchCloudObjectIdsResult(_message.Message):
    __slots__ = ("object_id_range_vec", "reuse_object_id_vec")
    class ObjectIdsRange(_message.Message):
        __slots__ = ("start_id", "num_ids")
        START_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_IDS_FIELD_NUMBER: _ClassVar[int]
        start_id: int
        num_ids: int
        def __init__(self, start_id: _Optional[int] = ..., num_ids: _Optional[int] = ...) -> None: ...
    OBJECT_ID_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    REUSE_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    object_id_range_vec: _containers.RepeatedCompositeFieldContainer[FetchCloudObjectIdsResult.ObjectIdsRange]
    reuse_object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, object_id_range_vec: _Optional[_Iterable[_Union[FetchCloudObjectIdsResult.ObjectIdsRange, _Mapping]]] = ..., reuse_object_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("domain_id", "cloud_location_vec")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    cloud_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudNodePtrProto]
    def __init__(self, domain_id: _Optional[int] = ..., cloud_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]]] = ...) -> None: ...

class DeleteNodesArg(_message.Message):
    __slots__ = ("domain_id", "object_to_delete_nodes_info_vec")
    class ObjectToDeleteNodesInfo(_message.Message):
        __slots__ = ("object_id", "scribe_version", "delete_local_id_vec")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        DELETE_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        scribe_version: int
        delete_local_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, object_id: _Optional[int] = ..., scribe_version: _Optional[int] = ..., delete_local_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TO_DELETE_NODES_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    object_to_delete_nodes_info_vec: _containers.RepeatedCompositeFieldContainer[DeleteNodesArg.ObjectToDeleteNodesInfo]
    def __init__(self, domain_id: _Optional[int] = ..., object_to_delete_nodes_info_vec: _Optional[_Iterable[_Union[DeleteNodesArg.ObjectToDeleteNodesInfo, _Mapping]]] = ...) -> None: ...

class DeleteNodesResult(_message.Message):
    __slots__ = ("delete_nodes_error_vec",)
    class DeleteNodesError(_message.Message):
        __slots__ = ("object_id", "error", "nodes_deleted")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        NODES_DELETED_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        error: _error_pb2.ErrorProto
        nodes_deleted: bool
        def __init__(self, object_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., nodes_deleted: bool = ...) -> None: ...
    DELETE_NODES_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    delete_nodes_error_vec: _containers.RepeatedCompositeFieldContainer[DeleteNodesResult.DeleteNodesError]
    def __init__(self, delete_nodes_error_vec: _Optional[_Iterable[_Union[DeleteNodesResult.DeleteNodesError, _Mapping]]] = ...) -> None: ...

class UndeleteNodesArg(_message.Message):
    __slots__ = ("domain_id", "object_to_undelete_nodes_info_vec")
    class ObjectToUndeleteNodesInfo(_message.Message):
        __slots__ = ("object_id", "scribe_version", "undelete_local_id_vec")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        UNDELETE_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        scribe_version: int
        undelete_local_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, object_id: _Optional[int] = ..., scribe_version: _Optional[int] = ..., undelete_local_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TO_UNDELETE_NODES_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    object_to_undelete_nodes_info_vec: _containers.RepeatedCompositeFieldContainer[UndeleteNodesArg.ObjectToUndeleteNodesInfo]
    def __init__(self, domain_id: _Optional[int] = ..., object_to_undelete_nodes_info_vec: _Optional[_Iterable[_Union[UndeleteNodesArg.ObjectToUndeleteNodesInfo, _Mapping]]] = ...) -> None: ...

class UndeleteNodesResult(_message.Message):
    __slots__ = ("undelete_nodes_error_vec",)
    class UndeleteNodesError(_message.Message):
        __slots__ = ("object_id", "error", "failed_to_undelete_local_id_vec", "num_nodes_undeleted")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        FAILED_TO_UNDELETE_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_NODES_UNDELETED_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        error: _error_pb2.ErrorProto
        failed_to_undelete_local_id_vec: _containers.RepeatedScalarFieldContainer[int]
        num_nodes_undeleted: int
        def __init__(self, object_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., failed_to_undelete_local_id_vec: _Optional[_Iterable[int]] = ..., num_nodes_undeleted: _Optional[int] = ...) -> None: ...
    UNDELETE_NODES_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    undelete_nodes_error_vec: _containers.RepeatedCompositeFieldContainer[UndeleteNodesResult.UndeleteNodesError]
    def __init__(self, undelete_nodes_error_vec: _Optional[_Iterable[_Union[UndeleteNodesResult.UndeleteNodesError, _Mapping]]] = ...) -> None: ...

class TouchOpClockArg(_message.Message):
    __slots__ = ("domain_id", "opclock", "object_id_vec")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    opclock: _op_clock_pb2.OpClock
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, domain_id: _Optional[int] = ..., opclock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class TouchOpClockResult(_message.Message):
    __slots__ = ("error_map",)
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    error_map: _containers.MessageMap[int, _error_pb2.ErrorProto]
    def __init__(self, error_map: _Optional[_Mapping[int, _error_pb2.ErrorProto]] = ...) -> None: ...

class PutRetentionArg(_message.Message):
    __slots__ = ("domain_id", "object_id_vec", "worm_params")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    worm_params: _worm_pb2.WORMParams
    def __init__(self, domain_id: _Optional[int] = ..., object_id_vec: _Optional[_Iterable[int]] = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ...) -> None: ...

class PutRetentionResult(_message.Message):
    __slots__ = ("object_info_vec", "non_extendable_object_id_vec")
    class ObjectInfo(_message.Message):
        __slots__ = ("object_id", "retention_timestamp_secs", "retention_mode", "error")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        retention_timestamp_secs: int
        retention_mode: _worm_pb2.RetentionMode.Type
        error: _error_pb2.ErrorProto
        def __init__(self, object_id: _Optional[int] = ..., retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NON_EXTENDABLE_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    object_info_vec: _containers.RepeatedCompositeFieldContainer[PutRetentionResult.ObjectInfo]
    non_extendable_object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, object_info_vec: _Optional[_Iterable[_Union[PutRetentionResult.ObjectInfo, _Mapping]]] = ..., non_extendable_object_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
