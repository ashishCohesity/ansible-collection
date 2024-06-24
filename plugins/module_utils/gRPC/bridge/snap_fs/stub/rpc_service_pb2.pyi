from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.virus_scanner import antivirus_scan_metadata_pb2 as _antivirus_scan_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from bridge.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestSequencer(_message.Message):
    __slots__ = ("key", "rpc_session_id")
    class SequencerKey(_message.Message):
        __slots__ = ("constituent_id", "view_id")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        view_id: int
        def __init__(self, constituent_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    RPC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    key: RequestSequencer.SequencerKey
    rpc_session_id: int
    def __init__(self, key: _Optional[_Union[RequestSequencer.SequencerKey, _Mapping]] = ..., rpc_session_id: _Optional[int] = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("eh", "offset", "is_optional", "durability", "stats_container", "is_magneto_request", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_blob_ticket_sequencer", "constituent_id", "is_forwarded", "qos_context", "forwarding_enabled", "data", "force_complete_write", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "expect_non_mega_file", "request_context", "request_sequencer", "populate_wcc_metadata", "range_data_vec", "portal_validation_data")
    class RangeData(_message.Message):
        __slots__ = ("offset", "length", "data")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        data: bytes
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    EH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    DURABILITY_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_TICKET_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_COMPLETE_WRITE_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    POPULATE_WCC_METADATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    PORTAL_VALIDATION_DATA_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    offset: int
    is_optional: bool
    durability: int
    stats_container: int
    is_magneto_request: bool
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_blob_ticket_sequencer: bool
    constituent_id: int
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    forwarding_enabled: bool
    data: bytes
    force_complete_write: bool
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    expect_non_mega_file: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    populate_wcc_metadata: bool
    range_data_vec: _containers.RepeatedCompositeFieldContainer[WriteArg.RangeData]
    portal_validation_data: _snap_fs_metadata_pb2.PortalValidationData
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., offset: _Optional[int] = ..., is_optional: bool = ..., durability: _Optional[int] = ..., stats_container: _Optional[int] = ..., is_magneto_request: bool = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_blob_ticket_sequencer: bool = ..., constituent_id: _Optional[int] = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., forwarding_enabled: bool = ..., data: _Optional[bytes] = ..., force_complete_write: bool = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., expect_non_mega_file: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., populate_wcc_metadata: bool = ..., range_data_vec: _Optional[_Iterable[_Union[WriteArg.RangeData, _Mapping]]] = ..., portal_validation_data: _Optional[_Union[_snap_fs_metadata_pb2.PortalValidationData, _Mapping]] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("durability", "count", "remote_session_id", "remote_ticket_sequencer_high", "remote_ticket_sequencer_low", "error", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "pre_inode_proto", "post_inode_proto")
    DURABILITY_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    PRE_INODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    POST_INODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    durability: int
    count: int
    remote_session_id: int
    remote_ticket_sequencer_high: int
    remote_ticket_sequencer_low: int
    error: _error_pb2.ErrorProto
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    pre_inode_proto: _snap_fs_metadata_pb2.InodeMetadataProto
    post_inode_proto: _snap_fs_metadata_pb2.InodeMetadataProto
    def __init__(self, durability: _Optional[int] = ..., count: _Optional[int] = ..., remote_session_id: _Optional[int] = ..., remote_ticket_sequencer_high: _Optional[int] = ..., remote_ticket_sequencer_low: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., pre_inode_proto: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., post_inode_proto: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("eh", "is_optional", "offset", "size", "is_magneto_request", "is_forwarded", "qos_context", "forwarding_enabled", "force_complete_read", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "disable_dir_prefetch", "expect_non_mega_file", "request_context", "request_sequencer")
    EH_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_COMPLETE_READ_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DIR_PREFETCH_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    is_optional: bool
    offset: int
    size: int
    is_magneto_request: bool
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    forwarding_enabled: bool
    force_complete_read: bool
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    disable_dir_prefetch: bool
    expect_non_mega_file: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_optional: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., is_magneto_request: bool = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., forwarding_enabled: bool = ..., force_complete_read: bool = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., disable_dir_prefetch: bool = ..., expect_non_mega_file: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("eof", "remote_session_id", "remote_ticket_sequencer_high", "remote_ticket_sequencer_low", "data", "error", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low")
    EOF_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    eof: bool
    remote_session_id: int
    remote_ticket_sequencer_high: int
    remote_ticket_sequencer_low: int
    data: bytes
    error: _error_pb2.ErrorProto
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    def __init__(self, eof: bool = ..., remote_session_id: _Optional[int] = ..., remote_ticket_sequencer_high: _Optional[int] = ..., remote_ticket_sequencer_low: _Optional[int] = ..., data: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class FindBlobBrickSnapTreeIdsArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "length", "qos_context", "is_forwarded", "is_optional", "ignore_data_journal_ranges")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DATA_JOURNAL_RANGES_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    length: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_forwarded: bool
    is_optional: bool
    ignore_data_journal_ranges: bool
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_forwarded: bool = ..., is_optional: bool = ..., ignore_data_journal_ranges: bool = ...) -> None: ...

class FindBlobBrickSnapTreeIdsResult(_message.Message):
    __slots__ = ("bricks", "error", "remote_session_id")
    class BrickInfo(_message.Message):
        __slots__ = ("brick_number", "snap_tree_root_id", "snap_tree_node_id")
        BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        brick_number: int
        snap_tree_root_id: int
        snap_tree_node_id: int
        def __init__(self, brick_number: _Optional[int] = ..., snap_tree_root_id: _Optional[int] = ..., snap_tree_node_id: _Optional[int] = ...) -> None: ...
    BRICKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    bricks: _containers.RepeatedCompositeFieldContainer[FindBlobBrickSnapTreeIdsResult.BrickInfo]
    error: _error_pb2.ErrorProto
    remote_session_id: int
    def __init__(self, bricks: _Optional[_Iterable[_Union[FindBlobBrickSnapTreeIdsResult.BrickInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., remote_session_id: _Optional[int] = ...) -> None: ...

class LookupMegaFileSubfilesArg(_message.Message):
    __slots__ = ("eh", "offset", "length", "qos_context", "request_sequencer")
    EH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    offset: int
    length: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LookupMegaFileSubfilesResult(_message.Message):
    __slots__ = ("subfiles", "error")
    class SubfileInfo(_message.Message):
        __slots__ = ("subfile_id", "eh", "logical_offset", "subfile_offset", "length")
        SUBFILE_ID_FIELD_NUMBER: _ClassVar[int]
        EH_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
        SUBFILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        subfile_id: int
        eh: _entity_handle_pb2.EntityHandleProto
        logical_offset: int
        subfile_offset: int
        length: int
        def __init__(self, subfile_id: _Optional[int] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., logical_offset: _Optional[int] = ..., subfile_offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    SUBFILES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    subfiles: _containers.RepeatedCompositeFieldContainer[LookupMegaFileSubfilesResult.SubfileInfo]
    error: _error_pb2.ErrorProto
    def __init__(self, subfiles: _Optional[_Iterable[_Union[LookupMegaFileSubfilesResult.SubfileInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DedupReadArg(_message.Message):
    __slots__ = ("eh", "offset", "count", "dedup_fps", "is_magneto_request", "can_forward", "qos_context", "is_optional", "is_forwarded", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "expect_non_mega_file", "return_location_for_cloud_chunks", "return_data_for_local_chunks", "skip_ccfm_cache", "request_context", "request_sequencer")
    class DedupChunkKey(_message.Message):
        __slots__ = ("length", "fingerprint")
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        length: int
        fingerprint: bytes
        def __init__(self, length: _Optional[int] = ..., fingerprint: _Optional[bytes] = ...) -> None: ...
    EH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_FPS_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CAN_FORWARD_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    RETURN_LOCATION_FOR_CLOUD_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    RETURN_DATA_FOR_LOCAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    SKIP_CCFM_CACHE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    offset: int
    count: int
    dedup_fps: _containers.RepeatedCompositeFieldContainer[DedupReadArg.DedupChunkKey]
    is_magneto_request: bool
    can_forward: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_optional: bool
    is_forwarded: bool
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    expect_non_mega_file: bool
    return_location_for_cloud_chunks: bool
    return_data_for_local_chunks: bool
    skip_ccfm_cache: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., offset: _Optional[int] = ..., count: _Optional[int] = ..., dedup_fps: _Optional[_Iterable[_Union[DedupReadArg.DedupChunkKey, _Mapping]]] = ..., is_magneto_request: bool = ..., can_forward: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_optional: bool = ..., is_forwarded: bool = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., expect_non_mega_file: bool = ..., return_location_for_cloud_chunks: bool = ..., return_data_for_local_chunks: bool = ..., skip_ccfm_cache: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class DedupReadResult(_message.Message):
    __slots__ = ("dedup_range", "eof", "remote_session_id", "next_offset_to_read", "error", "data", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low")
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_TO_READ_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    dedup_range: _dedup_range_pb2.DedupRange
    eof: bool
    remote_session_id: int
    next_offset_to_read: int
    error: _error_pb2.ErrorProto
    data: bytes
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    def __init__(self, dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., eof: bool = ..., remote_session_id: _Optional[int] = ..., next_offset_to_read: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class LookupInodeMetadataArg(_message.Message):
    __slots__ = ("eh", "qos_context", "is_forwarded", "can_include_garbage", "can_ignore_update_intent", "request_context", "request_sequencer")
    EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    CAN_INCLUDE_GARBAGE_FIELD_NUMBER: _ClassVar[int]
    CAN_IGNORE_UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_forwarded: bool
    can_include_garbage: bool
    can_ignore_update_intent: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_forwarded: bool = ..., can_include_garbage: bool = ..., can_ignore_update_intent: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LookupInodeMetadataResult(_message.Message):
    __slots__ = ("inode_metadata", "value_version", "error")
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    error: _error_pb2.ErrorProto
    def __init__(self, inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupPathArg(_message.Message):
    __slots__ = ("path", "qos_context", "request_sequencer")
    PATH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    path: str
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, path: _Optional[str] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LookupPathResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupDedupParamsArg(_message.Message):
    __slots__ = ("view_id", "qos_context")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, view_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class LookupDedupParamsResult(_message.Message):
    __slots__ = ("is_dedup_enabled", "min_chunk_size", "max_chunk_size", "fp_algo", "error")
    class ChunkingAlgo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHS_FP_1: _ClassVar[LookupDedupParamsResult.ChunkingAlgo]
    CHS_FP_1: LookupDedupParamsResult.ChunkingAlgo
    IS_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    FP_ALGO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    is_dedup_enabled: bool
    min_chunk_size: int
    max_chunk_size: int
    fp_algo: LookupDedupParamsResult.ChunkingAlgo
    error: _error_pb2.ErrorProto
    def __init__(self, is_dedup_enabled: bool = ..., min_chunk_size: _Optional[int] = ..., max_chunk_size: _Optional[int] = ..., fp_algo: _Optional[_Union[LookupDedupParamsResult.ChunkingAlgo, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupDirEntryArg(_message.Message):
    __slots__ = ("dir_eh", "entry_name", "qos_context", "is_forwarded", "check_exact_name", "request_context", "request_sequencer")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    CHECK_EXACT_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    entry_name: str
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_forwarded: bool
    check_exact_name: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., entry_name: _Optional[str] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_forwarded: bool = ..., check_exact_name: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LookupDirEntryResult(_message.Message):
    __slots__ = ("entity_handle", "error", "display_name")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    display_name: str
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...

class LookupDirectoryEntryNameArg(_message.Message):
    __slots__ = ("entry_eh", "parent_eh", "qos_context", "lookup_first_entity_only", "request_sequencer")
    ENTRY_EH_FIELD_NUMBER: _ClassVar[int]
    PARENT_EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_FIRST_ENTITY_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    entry_eh: _entity_handle_pb2.EntityHandleProto
    parent_eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    lookup_first_entity_only: bool
    request_sequencer: RequestSequencer
    def __init__(self, entry_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., parent_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., lookup_first_entity_only: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LookupDirectoryEntryNameResult(_message.Message):
    __slots__ = ("entry_name_vec", "parent_eh", "error")
    ENTRY_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_EH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entry_name_vec: _containers.RepeatedScalarFieldContainer[str]
    parent_eh: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entry_name_vec: _Optional[_Iterable[str]] = ..., parent_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CookieInfo(_message.Message):
    __slots__ = ("key", "tree_id", "node_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    key: int
    tree_id: int
    node_id: int
    def __init__(self, key: _Optional[int] = ..., tree_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class LookupViewSnapTreeNodesArg(_message.Message):
    __slots__ = ("eh", "cookie", "include_internal", "node_id_floor", "max_nodes", "min_key", "max_key", "request_id", "tree_id_floor", "qos_context")
    EH_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    MAX_NODES_FIELD_NUMBER: _ClassVar[int]
    MIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    cookie: CookieInfo
    include_internal: bool
    node_id_floor: int
    max_nodes: int
    min_key: int
    max_key: int
    request_id: int
    tree_id_floor: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., cookie: _Optional[_Union[CookieInfo, _Mapping]] = ..., include_internal: bool = ..., node_id_floor: _Optional[int] = ..., max_nodes: _Optional[int] = ..., min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., request_id: _Optional[int] = ..., tree_id_floor: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class LookupViewSnapTreeNodesResult(_message.Message):
    __slots__ = ("node_vec", "cookie", "error")
    class NodeVecItem(_message.Message):
        __slots__ = ("key", "tree_id", "node_id")
        KEY_FIELD_NUMBER: _ClassVar[int]
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        key: int
        tree_id: int
        node_id: int
        def __init__(self, key: _Optional[int] = ..., tree_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[LookupViewSnapTreeNodesResult.NodeVecItem]
    cookie: CookieInfo
    error: _error_pb2.ErrorProto
    def __init__(self, node_vec: _Optional[_Iterable[_Union[LookupViewSnapTreeNodesResult.NodeVecItem, _Mapping]]] = ..., cookie: _Optional[_Union[CookieInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReverseNameLookupArg(_message.Message):
    __slots__ = ("eh", "qos_context", "is_forwarded", "request_sequencer", "request_context")
    EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_forwarded: bool
    request_sequencer: RequestSequencer
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_forwarded: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class ReverseNameLookupResult(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: _error_pb2.ErrorProto
    def __init__(self, path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReverseNameLookupAllPathsArg(_message.Message):
    __slots__ = ("eh", "qos_context", "is_forwarded", "request_sequencer")
    EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_forwarded: bool
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_forwarded: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class ReverseNameLookupAllPathsResult(_message.Message):
    __slots__ = ("paths", "error")
    PATHS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.ErrorProto
    def __init__(self, paths: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("dir_eh", "file_name", "ctype", "create_verifier", "mode", "uid", "gid", "size_bytes", "ctime_usecs", "mtime_usecs", "entity_id", "expected_entity_id", "existing_is_dir", "extended_attr", "s3_metadata", "qos_context", "creation_time_usecs", "archived_location", "hdfs_attrs", "file_level_datalock_metadata", "mega_file_info", "request_sequencer", "skip_inode_precreation")
    class CreateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnchecked: _ClassVar[CreateFileArg.CreateType]
        kGuarded: _ClassVar[CreateFileArg.CreateType]
        kExclusive: _ClassVar[CreateFileArg.CreateType]
        kUnchecked4: _ClassVar[CreateFileArg.CreateType]
    kUnchecked: CreateFileArg.CreateType
    kGuarded: CreateFileArg.CreateType
    kExclusive: CreateFileArg.CreateType
    kUnchecked4: CreateFileArg.CreateType
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXISTING_IS_DIR_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATALOCK_METADATA_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    SKIP_INODE_PRECREATION_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    file_name: str
    ctype: CreateFileArg.CreateType
    create_verifier: int
    mode: int
    uid: int
    gid: int
    size_bytes: int
    ctime_usecs: int
    mtime_usecs: int
    entity_id: int
    expected_entity_id: int
    existing_is_dir: bool
    extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    creation_time_usecs: int
    archived_location: _cloud_pb2.ArchivedLocation
    hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
    file_level_datalock_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata
    mega_file_info: _snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo
    request_sequencer: RequestSequencer
    skip_inode_precreation: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., file_name: _Optional[str] = ..., ctype: _Optional[_Union[CreateFileArg.CreateType, str]] = ..., create_verifier: _Optional[int] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., expected_entity_id: _Optional[int] = ..., existing_is_dir: bool = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., archived_location: _Optional[_Union[_cloud_pb2.ArchivedLocation, _Mapping]] = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., file_level_datalock_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata, _Mapping]] = ..., mega_file_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., skip_inode_precreation: bool = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateMegaFileArg(_message.Message):
    __slots__ = ("dir_eh", "file_name", "mode", "uid", "gid", "size_bytes", "subfile_size_mb", "ctime_usecs", "mtime_usecs", "qos_context", "mega_file_info", "request_sequencer", "s3_metadata", "skip_inode_precreation")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    SKIP_INODE_PRECREATION_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    file_name: str
    mode: int
    uid: int
    gid: int
    size_bytes: int
    subfile_size_mb: int
    ctime_usecs: int
    mtime_usecs: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    mega_file_info: _snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo
    request_sequencer: RequestSequencer
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    skip_inode_precreation: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., file_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., subfile_size_mb: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., mega_file_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., skip_inode_precreation: bool = ...) -> None: ...

class CreateMegaFileResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloneToMegaFileArg(_message.Message):
    __slots__ = ("dst_dir_eh", "dst_file_name", "mode", "uid", "gid", "desired_subfile_size_mb", "ctime_usecs", "mtime_usecs", "src_file_eh_vec", "s3_metadata", "qos_context", "request_sequencer")
    DST_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SRC_FILE_EH_VEC_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    dst_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_file_name: str
    mode: int
    uid: int
    gid: int
    desired_subfile_size_mb: int
    ctime_usecs: int
    mtime_usecs: int
    src_file_eh_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, dst_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_file_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., desired_subfile_size_mb: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., src_file_eh_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class CloneToMegaFileResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloneFileArg(_message.Message):
    __slots__ = ("src_eh", "dst_dir_eh", "dst_file_name", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "extended_attr", "s3_metadata", "ctype", "request_id", "qos_context", "request_sequencer")
    class CreateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnchecked: _ClassVar[CloneFileArg.CreateType]
        kGuarded: _ClassVar[CloneFileArg.CreateType]
        kExclusive: _ClassVar[CloneFileArg.CreateType]
    kUnchecked: CloneFileArg.CreateType
    kGuarded: CloneFileArg.CreateType
    kExclusive: CloneFileArg.CreateType
    SRC_EH_FIELD_NUMBER: _ClassVar[int]
    DST_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    src_eh: _entity_handle_pb2.EntityHandleProto
    dst_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_file_name: str
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    ctype: CloneFileArg.CreateType
    request_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, src_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_file_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., ctype: _Optional[_Union[CloneFileArg.CreateType, str]] = ..., request_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class CloneFileResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloneDirectoryArg(_message.Message):
    __slots__ = ("src_dir_eh", "dst_dir_eh", "dst_dir_name", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "request_id", "qos_context", "retain_entity_ids", "request_sequencer")
    SRC_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RETAIN_ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    src_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_dir_name: str
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    request_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    retain_entity_ids: bool
    request_sequencer: RequestSequencer
    def __init__(self, src_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_dir_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., request_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., retain_entity_ids: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class CloneDirectoryResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloneDirectoryRecursiveArg(_message.Message):
    __slots__ = ("src_dir_eh", "dst_parent_dir_eh", "dst_dir_name", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "extended_attr", "s3_metadata", "ctype", "qos_context", "retain_entity_ids", "request_sequencer")
    class CreateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnchecked: _ClassVar[CloneDirectoryRecursiveArg.CreateType]
        kGuarded: _ClassVar[CloneDirectoryRecursiveArg.CreateType]
        kExclusive: _ClassVar[CloneDirectoryRecursiveArg.CreateType]
    kUnchecked: CloneDirectoryRecursiveArg.CreateType
    kGuarded: CloneDirectoryRecursiveArg.CreateType
    kExclusive: CloneDirectoryRecursiveArg.CreateType
    SRC_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_PARENT_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RETAIN_ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    src_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_parent_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_dir_name: str
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    ctype: CloneDirectoryRecursiveArg.CreateType
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    retain_entity_ids: bool
    request_sequencer: RequestSequencer
    def __init__(self, src_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_parent_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_dir_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., ctype: _Optional[_Union[CloneDirectoryRecursiveArg.CreateType, str]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., retain_entity_ids: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class CloneDirectoryRecursiveResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateEntityArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "mode", "uid", "gid", "size_bytes", "ctime_usecs", "mtime_usecs", "create_type", "node_info", "dir_info", "link_info", "file_info", "qos_context", "creation_time_usecs", "entity_id", "is_forwarded", "request_id", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_inode_created", "is_retry", "request_context", "request_sequencer", "skip_dir_lookup", "skip_inode_precreation")
    class CreateEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNode: _ClassVar[CreateEntityArg.CreateEntityType]
        kDirectory: _ClassVar[CreateEntityArg.CreateEntityType]
        kSymlink: _ClassVar[CreateEntityArg.CreateEntityType]
        kFile: _ClassVar[CreateEntityArg.CreateEntityType]
    kNode: CreateEntityArg.CreateEntityType
    kDirectory: CreateEntityArg.CreateEntityType
    kSymlink: CreateEntityArg.CreateEntityType
    kFile: CreateEntityArg.CreateEntityType
    class MknodInfo(_message.Message):
        __slots__ = ("type", "major_device_num", "minor_device_num", "extended_attr")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MAJOR_DEVICE_NUM_FIELD_NUMBER: _ClassVar[int]
        MINOR_DEVICE_NUM_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
        type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
        major_device_num: int
        minor_device_num: int
        extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
        def __init__(self, type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., major_device_num: _Optional[int] = ..., minor_device_num: _Optional[int] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ...) -> None: ...
    class MkdirInfo(_message.Message):
        __slots__ = ("entity_id", "expected_existing_id", "is_dir", "extended_attr", "s3_metadata", "subfile_size_mb", "is_mega_file", "hdfs_attrs", "mega_file_info")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_EXISTING_ID_FIELD_NUMBER: _ClassVar[int]
        IS_DIR_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
        S3_METADATA_FIELD_NUMBER: _ClassVar[int]
        SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        IS_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
        HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
        MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        expected_existing_id: int
        is_dir: bool
        extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
        s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
        subfile_size_mb: int
        is_mega_file: bool
        hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
        mega_file_info: _snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo
        def __init__(self, entity_id: _Optional[int] = ..., expected_existing_id: _Optional[int] = ..., is_dir: bool = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., subfile_size_mb: _Optional[int] = ..., is_mega_file: bool = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., mega_file_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo, _Mapping]] = ...) -> None: ...
    class SymlinkInfo(_message.Message):
        __slots__ = ("symlink_data", "extended_attr")
        SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
        symlink_data: str
        extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
        def __init__(self, symlink_data: _Optional[str] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ...) -> None: ...
    class FileInfo(_message.Message):
        __slots__ = ("ctype", "create_verifier", "expected_entity_id", "existing_is_dir", "extended_attr", "s3_metadata", "is_sub_file", "archived_location_vec", "minion_info", "blob_info", "hdfs_attrs", "file_level_datalock_metadata", "mega_file_info")
        class CreateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnchecked: _ClassVar[CreateEntityArg.FileInfo.CreateType]
            kGuarded: _ClassVar[CreateEntityArg.FileInfo.CreateType]
            kExclusive: _ClassVar[CreateEntityArg.FileInfo.CreateType]
            kUnchecked4: _ClassVar[CreateEntityArg.FileInfo.CreateType]
        kUnchecked: CreateEntityArg.FileInfo.CreateType
        kGuarded: CreateEntityArg.FileInfo.CreateType
        kExclusive: CreateEntityArg.FileInfo.CreateType
        kUnchecked4: CreateEntityArg.FileInfo.CreateType
        CTYPE_FIELD_NUMBER: _ClassVar[int]
        CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EXISTING_IS_DIR_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
        S3_METADATA_FIELD_NUMBER: _ClassVar[int]
        IS_SUB_FILE_FIELD_NUMBER: _ClassVar[int]
        ARCHIVED_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
        MINION_INFO_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_FIELD_NUMBER: _ClassVar[int]
        HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
        FILE_LEVEL_DATALOCK_METADATA_FIELD_NUMBER: _ClassVar[int]
        MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
        ctype: CreateEntityArg.FileInfo.CreateType
        create_verifier: int
        expected_entity_id: int
        existing_is_dir: bool
        extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
        s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
        is_sub_file: bool
        archived_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchivedLocation]
        minion_info: _snap_fs_metadata_pb2.InodeMetadataProto.MinionInfo
        blob_info: _snap_fs_metadata_pb2.InodeMetadataProto.BlobInfo
        hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
        file_level_datalock_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata
        mega_file_info: _snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo
        def __init__(self, ctype: _Optional[_Union[CreateEntityArg.FileInfo.CreateType, str]] = ..., create_verifier: _Optional[int] = ..., expected_entity_id: _Optional[int] = ..., existing_is_dir: bool = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., is_sub_file: bool = ..., archived_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchivedLocation, _Mapping]]] = ..., minion_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MinionInfo, _Mapping]] = ..., blob_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.BlobInfo, _Mapping]] = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., file_level_datalock_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata, _Mapping]] = ..., mega_file_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo, _Mapping]] = ...) -> None: ...
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    DIR_INFO_FIELD_NUMBER: _ClassVar[int]
    LINK_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_INODE_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_RETRY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    SKIP_DIR_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    SKIP_INODE_PRECREATION_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    mode: int
    uid: int
    gid: int
    size_bytes: int
    ctime_usecs: int
    mtime_usecs: int
    create_type: CreateEntityArg.CreateEntityType
    node_info: CreateEntityArg.MknodInfo
    dir_info: CreateEntityArg.MkdirInfo
    link_info: CreateEntityArg.SymlinkInfo
    file_info: CreateEntityArg.FileInfo
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    creation_time_usecs: int
    entity_id: int
    is_forwarded: bool
    request_id: int
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_inode_created: bool
    is_retry: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    skip_dir_lookup: bool
    skip_inode_precreation: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_type: _Optional[_Union[CreateEntityArg.CreateEntityType, str]] = ..., node_info: _Optional[_Union[CreateEntityArg.MknodInfo, _Mapping]] = ..., dir_info: _Optional[_Union[CreateEntityArg.MkdirInfo, _Mapping]] = ..., link_info: _Optional[_Union[CreateEntityArg.SymlinkInfo, _Mapping]] = ..., file_info: _Optional[_Union[CreateEntityArg.FileInfo, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., is_forwarded: bool = ..., request_id: _Optional[int] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_inode_created: bool = ..., is_retry: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., skip_dir_lookup: bool = ..., skip_inode_precreation: bool = ...) -> None: ...

class CreateEntityResult(_message.Message):
    __slots__ = ("entity_handle", "error")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    error: _error_pb2.ErrorProto
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateEntityProto(_message.Message):
    __slots__ = ("entry_name", "inode_type", "size_bytes", "physical_size_bytes", "mode", "uid", "gid", "creation_ctime_usecs", "creation_mtime_usecs", "creation_time_usecs", "symlink_data", "major_device_number", "minor_device_number", "extended_attributes", "s3_metadata", "is_mega_file", "mega_file_subfile_size_mb", "create_type", "entity_id", "expected_existing_entity_id", "create_verifier", "hdfs_attrs", "skip_dir_lookup")
    class CreateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnchecked: _ClassVar[CreateEntityProto.CreateType]
        kGuarded: _ClassVar[CreateEntityProto.CreateType]
        kExclusive: _ClassVar[CreateEntityProto.CreateType]
        kUnchecked4: _ClassVar[CreateEntityProto.CreateType]
    kUnchecked: CreateEntityProto.CreateType
    kGuarded: CreateEntityProto.CreateType
    kExclusive: CreateEntityProto.CreateType
    kUnchecked4: CreateEntityProto.CreateType
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CREATION_CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATION_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
    MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    CREATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_EXISTING_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
    SKIP_DIR_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    entry_name: str
    inode_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
    size_bytes: int
    physical_size_bytes: int
    mode: int
    uid: int
    gid: int
    creation_ctime_usecs: int
    creation_mtime_usecs: int
    creation_time_usecs: int
    symlink_data: str
    major_device_number: int
    minor_device_number: int
    extended_attributes: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    is_mega_file: bool
    mega_file_subfile_size_mb: int
    create_type: CreateEntityProto.CreateType
    entity_id: int
    expected_existing_entity_id: int
    create_verifier: int
    hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
    skip_dir_lookup: bool
    def __init__(self, entry_name: _Optional[str] = ..., inode_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., creation_ctime_usecs: _Optional[int] = ..., creation_mtime_usecs: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., symlink_data: _Optional[str] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ..., extended_attributes: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., is_mega_file: bool = ..., mega_file_subfile_size_mb: _Optional[int] = ..., create_type: _Optional[_Union[CreateEntityProto.CreateType, str]] = ..., entity_id: _Optional[int] = ..., expected_existing_entity_id: _Optional[int] = ..., create_verifier: _Optional[int] = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., skip_dir_lookup: bool = ...) -> None: ...

class CreateRemoveEntitiesBatchArg(_message.Message):
    __slots__ = ("dir_eh", "create_entity_vec", "remove_entity_vec", "qos_context", "request_sequencer", "adjust_fragments_on_deletion", "expected_final_entries_in_dir", "allow_minion_reservation", "early_notification")
    class RemoveEntityProto(_message.Message):
        __slots__ = ("entry_name", "expected_existing_entity_id", "existing_entity_is_directory", "dir_metadata_inconsistent")
        ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_EXISTING_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EXISTING_ENTITY_IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        DIR_METADATA_INCONSISTENT_FIELD_NUMBER: _ClassVar[int]
        entry_name: str
        expected_existing_entity_id: int
        existing_entity_is_directory: bool
        dir_metadata_inconsistent: bool
        def __init__(self, entry_name: _Optional[str] = ..., expected_existing_entity_id: _Optional[int] = ..., existing_entity_is_directory: bool = ..., dir_metadata_inconsistent: bool = ...) -> None: ...
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CREATE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    ADJUST_FRAGMENTS_ON_DELETION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FINAL_ENTRIES_IN_DIR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MINION_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    EARLY_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    create_entity_vec: _containers.RepeatedCompositeFieldContainer[CreateEntityProto]
    remove_entity_vec: _containers.RepeatedCompositeFieldContainer[CreateRemoveEntitiesBatchArg.RemoveEntityProto]
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    adjust_fragments_on_deletion: bool
    expected_final_entries_in_dir: int
    allow_minion_reservation: bool
    early_notification: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., create_entity_vec: _Optional[_Iterable[_Union[CreateEntityProto, _Mapping]]] = ..., remove_entity_vec: _Optional[_Iterable[_Union[CreateRemoveEntitiesBatchArg.RemoveEntityProto, _Mapping]]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., adjust_fragments_on_deletion: bool = ..., expected_final_entries_in_dir: _Optional[int] = ..., allow_minion_reservation: bool = ..., early_notification: bool = ...) -> None: ...

class CreateRemoveEntitiesBatchResult(_message.Message):
    __slots__ = ("batch_result", "error")
    class BatchResultProto(_message.Message):
        __slots__ = ("error", "entity_name", "entity_handle", "removed_entity_size_bytes")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        REMOVED_ENTITY_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_name: str
        entity_handle: _entity_handle_pb2.EntityHandleProto
        removed_entity_size_bytes: int
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_name: _Optional[str] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., removed_entity_size_bytes: _Optional[int] = ...) -> None: ...
    BATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    batch_result: _containers.RepeatedCompositeFieldContainer[CreateRemoveEntitiesBatchResult.BatchResultProto]
    error: _error_pb2.ErrorProto
    def __init__(self, batch_result: _Optional[_Iterable[_Union[CreateRemoveEntitiesBatchResult.BatchResultProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RemoveFileArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "expected_entity_id", "request_id", "qos_context", "is_privileged", "request_sequencer")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    expected_entity_id: int
    request_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    is_privileged: bool
    request_sequencer: RequestSequencer
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., expected_entity_id: _Optional[int] = ..., request_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., is_privileged: bool = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class RemoveFileResult(_message.Message):
    __slots__ = ("error", "eh", "deleted_file_size_bytes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EH_FIELD_NUMBER: _ClassVar[int]
    DELETED_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    eh: _entity_handle_pb2.EntityHandleProto
    deleted_file_size_bytes: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., deleted_file_size_bytes: _Optional[int] = ...) -> None: ...

class RmdirArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "expected_ent_id", "qos_context", "request_sequencer", "metadata_inconsistent")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENT_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    METADATA_INCONSISTENT_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    expected_ent_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    metadata_inconsistent: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., expected_ent_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., metadata_inconsistent: bool = ...) -> None: ...

class RmdirResult(_message.Message):
    __slots__ = ("error", "eh")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    eh: _entity_handle_pb2.EntityHandleProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class RemoveEntityArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "expected_entity_id", "is_directory", "is_forwarded", "qos_context", "request_id", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_privileged", "request_context", "request_sequencer", "dir_metadata_inconsistent", "filer_lcm_triggered_removal")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    DIR_METADATA_INCONSISTENT_FIELD_NUMBER: _ClassVar[int]
    FILER_LCM_TRIGGERED_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    expected_entity_id: int
    is_directory: bool
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_id: int
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_privileged: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    dir_metadata_inconsistent: bool
    filer_lcm_triggered_removal: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., expected_entity_id: _Optional[int] = ..., is_directory: bool = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_id: _Optional[int] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_privileged: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., dir_metadata_inconsistent: bool = ..., filer_lcm_triggered_removal: bool = ...) -> None: ...

class RemoveEntityResult(_message.Message):
    __slots__ = ("error", "entity_handle", "removed_file_size_bytes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_handle: _entity_handle_pb2.EntityHandleProto
    removed_file_size_bytes: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., removed_file_size_bytes: _Optional[int] = ...) -> None: ...

class UnlinkDirectoryArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "qos_context", "request_sequencer")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class UnlinkDirectoryResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LinkArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "child_eh", "qos_context", "request_sequencer")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    CHILD_EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    child_eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., child_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class LinkResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SetattrArg(_message.Message):
    __slots__ = ("eh", "mode", "uid", "gid", "size_bytes", "mtime_usecs", "expected_ctime_usecs", "extended_attr", "inode_creation_time_usecs", "ctime_usecs", "s3_metadata", "mega_file_info", "phy_size_bytes", "request_id_deprecated", "qos_context", "atime_usecs", "data_lock_file", "madrox_completed_dir_removals_rid", "fld_metadata", "antivirus_metadata", "symlink_data", "infection_desc", "clear_file_contents", "archived_location", "dir_quota_id", "inode_type", "is_privileged", "is_forwarded", "request_id", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "hdfs_attrs", "atime_usecs_overwrite_vec", "request_sequencer", "populate_wcc_metadata")
    EH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
    INODE_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ATIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_FILE_FIELD_NUMBER: _ClassVar[int]
    MADROX_COMPLETED_DIR_REMOVALS_RID_FIELD_NUMBER: _ClassVar[int]
    FLD_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_METADATA_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
    INFECTION_DESC_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
    ATIME_USECS_OVERWRITE_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    POPULATE_WCC_METADATA_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    mode: int
    uid: int
    gid: int
    size_bytes: int
    mtime_usecs: int
    expected_ctime_usecs: int
    extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    inode_creation_time_usecs: int
    ctime_usecs: int
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    mega_file_info: _snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo
    phy_size_bytes: int
    request_id_deprecated: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    atime_usecs: int
    data_lock_file: bool
    madrox_completed_dir_removals_rid: _universal_id_pb2.UniversalIdProto
    fld_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata
    antivirus_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata
    symlink_data: bytes
    infection_desc: _antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto
    clear_file_contents: bool
    archived_location: _cloud_pb2.ArchivedLocation
    dir_quota_id: int
    inode_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
    is_privileged: bool
    is_forwarded: bool
    request_id: int
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
    atime_usecs_overwrite_vec: _containers.RepeatedScalarFieldContainer[int]
    request_sequencer: RequestSequencer
    populate_wcc_metadata: bool
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., expected_ctime_usecs: _Optional[int] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., inode_creation_time_usecs: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., mega_file_info: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.MegaFileInfo, _Mapping]] = ..., phy_size_bytes: _Optional[int] = ..., request_id_deprecated: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., atime_usecs: _Optional[int] = ..., data_lock_file: bool = ..., madrox_completed_dir_removals_rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., fld_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata, _Mapping]] = ..., antivirus_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata, _Mapping]] = ..., symlink_data: _Optional[bytes] = ..., infection_desc: _Optional[_Union[_antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto, _Mapping]] = ..., clear_file_contents: bool = ..., archived_location: _Optional[_Union[_cloud_pb2.ArchivedLocation, _Mapping]] = ..., dir_quota_id: _Optional[int] = ..., inode_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., is_privileged: bool = ..., is_forwarded: bool = ..., request_id: _Optional[int] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., atime_usecs_overwrite_vec: _Optional[_Iterable[int]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., populate_wcc_metadata: bool = ...) -> None: ...

class SetattrResult(_message.Message):
    __slots__ = ("error", "pre_inode_proto", "post_inode_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PRE_INODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    POST_INODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pre_inode_proto: _snap_fs_metadata_pb2.InodeMetadataProto
    post_inode_proto: _snap_fs_metadata_pb2.InodeMetadataProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pre_inode_proto: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., post_inode_proto: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ...) -> None: ...

class ReaddirArg(_message.Message):
    __slots__ = ("eh", "cookie", "cookie_verifier", "prefetch_metadata", "qos_context", "num_prefetch_levels", "is_forwarded", "max_message_size", "entry_overhead_bytes", "request_sequencer", "caller_requested_frag_index", "issue_prefetch_always", "prefetching_count_limit", "prefetch_next_fragment")
    EH_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NUM_PREFETCH_LEVELS_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_OVERHEAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    CALLER_REQUESTED_FRAG_INDEX_FIELD_NUMBER: _ClassVar[int]
    ISSUE_PREFETCH_ALWAYS_FIELD_NUMBER: _ClassVar[int]
    PREFETCHING_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_NEXT_FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    cookie: int
    cookie_verifier: int
    prefetch_metadata: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    num_prefetch_levels: int
    is_forwarded: bool
    max_message_size: int
    entry_overhead_bytes: int
    request_sequencer: RequestSequencer
    caller_requested_frag_index: int
    issue_prefetch_always: bool
    prefetching_count_limit: int
    prefetch_next_fragment: bool
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., cookie: _Optional[int] = ..., cookie_verifier: _Optional[int] = ..., prefetch_metadata: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., num_prefetch_levels: _Optional[int] = ..., is_forwarded: bool = ..., max_message_size: _Optional[int] = ..., entry_overhead_bytes: _Optional[int] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ..., caller_requested_frag_index: _Optional[int] = ..., issue_prefetch_always: bool = ..., prefetching_count_limit: _Optional[int] = ..., prefetch_next_fragment: bool = ...) -> None: ...

class ReaddirResult(_message.Message):
    __slots__ = ("cookie_verifier", "is_eof", "dir_entries", "error")
    class DirEntry(_message.Message):
        __slots__ = ("entry_name", "entity_id", "cookie", "entity_type")
        ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        entry_name: str
        entity_id: int
        cookie: int
        entity_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
        def __init__(self, entry_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., cookie: _Optional[int] = ..., entity_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ...) -> None: ...
    COOKIE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_EOF_FIELD_NUMBER: _ClassVar[int]
    DIR_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    cookie_verifier: int
    is_eof: bool
    dir_entries: _containers.RepeatedCompositeFieldContainer[ReaddirResult.DirEntry]
    error: _error_pb2.ErrorProto
    def __init__(self, cookie_verifier: _Optional[int] = ..., is_eof: bool = ..., dir_entries: _Optional[_Iterable[_Union[ReaddirResult.DirEntry, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RenameArg(_message.Message):
    __slots__ = ("src_dir_eh", "src_entry_name", "dst_dir_eh", "dst_entry_name", "qos_context", "request_sequencer")
    SRC_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    SRC_ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    DST_DIR_EH_FIELD_NUMBER: _ClassVar[int]
    DST_ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    src_dir_eh: _entity_handle_pb2.EntityHandleProto
    src_entry_name: str
    dst_dir_eh: _entity_handle_pb2.EntityHandleProto
    dst_entry_name: str
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, src_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., src_entry_name: _Optional[str] = ..., dst_dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_entry_name: _Optional[str] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class RenameResult(_message.Message):
    __slots__ = ("error", "inode_type", "src_eh")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_EH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    inode_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
    src_eh: _entity_handle_pb2.EntityHandleProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., inode_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., src_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class CloneBytesArg(_message.Message):
    __slots__ = ("src_eh", "src_offset", "dst_eh", "dst_offset", "count", "desired_durability", "stats_container", "is_magneto_user", "request_id", "qos_context", "request_sequencer")
    class Durability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnstable: _ClassVar[CloneBytesArg.Durability]
        kDataSync: _ClassVar[CloneBytesArg.Durability]
        kFileSync: _ClassVar[CloneBytesArg.Durability]
    kUnstable: CloneBytesArg.Durability
    kDataSync: CloneBytesArg.Durability
    kFileSync: CloneBytesArg.Durability
    SRC_EH_FIELD_NUMBER: _ClassVar[int]
    SRC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DST_EH_FIELD_NUMBER: _ClassVar[int]
    DST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_USER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    src_eh: _entity_handle_pb2.EntityHandleProto
    src_offset: int
    dst_eh: _entity_handle_pb2.EntityHandleProto
    dst_offset: int
    count: int
    desired_durability: CloneBytesArg.Durability
    stats_container: int
    is_magneto_user: bool
    request_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, src_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., src_offset: _Optional[int] = ..., dst_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dst_offset: _Optional[int] = ..., count: _Optional[int] = ..., desired_durability: _Optional[_Union[CloneBytesArg.Durability, str]] = ..., stats_container: _Optional[int] = ..., is_magneto_user: bool = ..., request_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class CloneBytesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DedupWriteArg(_message.Message):
    __slots__ = ("eh", "dedup_range", "stats_container", "is_magneto_user", "restoring_stub_file", "is_optional", "is_forwarded", "qos_context", "data", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "expect_non_mega_file", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_blob_ticket_sequencer", "request_context", "request_sequencer")
    EH_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_USER_FIELD_NUMBER: _ClassVar[int]
    RESTORING_STUB_FILE_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_TICKET_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    dedup_range: _dedup_range_pb2.DedupRange
    stats_container: int
    is_magneto_user: bool
    restoring_stub_file: bool
    is_optional: bool
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    data: bytes
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    expect_non_mega_file: bool
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_blob_ticket_sequencer: bool
    request_context: _request_context_pb2.RequestContextProto
    request_sequencer: RequestSequencer
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., stats_container: _Optional[int] = ..., is_magneto_user: bool = ..., restoring_stub_file: bool = ..., is_optional: bool = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., data: _Optional[bytes] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., expect_non_mega_file: bool = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_blob_ticket_sequencer: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class DedupWriteResult(_message.Message):
    __slots__ = ("missing_ranges", "remote_session_id", "next_offset_to_write", "bytes_written", "error", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low")
    class Range(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    MISSING_RANGES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_TO_WRITE_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    missing_ranges: _containers.RepeatedCompositeFieldContainer[DedupWriteResult.Range]
    remote_session_id: int
    next_offset_to_write: int
    bytes_written: int
    error: _error_pb2.ErrorProto
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    def __init__(self, missing_ranges: _Optional[_Iterable[_Union[DedupWriteResult.Range, _Mapping]]] = ..., remote_session_id: _Optional[int] = ..., next_offset_to_write: _Optional[int] = ..., bytes_written: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class FindKnownIdenticalRangesArg(_message.Message):
    __slots__ = ("eh1", "eh2", "offset", "length", "is_magneto_request", "request_id", "qos_context", "ignore_data_journal_ranges")
    EH1_FIELD_NUMBER: _ClassVar[int]
    EH2_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DATA_JOURNAL_RANGES_FIELD_NUMBER: _ClassVar[int]
    eh1: _entity_handle_pb2.EntityHandleProto
    eh2: _entity_handle_pb2.EntityHandleProto
    offset: int
    length: int
    is_magneto_request: bool
    request_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    ignore_data_journal_ranges: bool
    def __init__(self, eh1: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., eh2: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., is_magneto_request: bool = ..., request_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., ignore_data_journal_ranges: bool = ...) -> None: ...

class FindKnownIdenticalRangesResult(_message.Message):
    __slots__ = ("identical_ranges", "error")
    class IdenticalRange(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    IDENTICAL_RANGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    identical_ranges: _containers.RepeatedCompositeFieldContainer[FindKnownIdenticalRangesResult.IdenticalRange]
    error: _error_pb2.ErrorProto
    def __init__(self, identical_ranges: _Optional[_Iterable[_Union[FindKnownIdenticalRangesResult.IdenticalRange, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FixEntityHandleArg(_message.Message):
    __slots__ = ("eh_to_fix", "qos_context", "request_sequencer")
    EH_TO_FIX_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    eh_to_fix: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, eh_to_fix: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class FixEntityHandleResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchViewSnapTreeValuesArg(_message.Message):
    __slots__ = ("root_eh", "cookie", "tree_id_floor", "max_values", "qos_context", "max_cookie")
    ROOT_EH_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUES_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_COOKIE_FIELD_NUMBER: _ClassVar[int]
    root_eh: _entity_handle_pb2.EntityHandleProto
    cookie: int
    tree_id_floor: int
    max_values: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    max_cookie: int
    def __init__(self, root_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., cookie: _Optional[int] = ..., tree_id_floor: _Optional[int] = ..., max_values: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., max_cookie: _Optional[int] = ...) -> None: ...

class FetchViewSnapTreeValuesResult(_message.Message):
    __slots__ = ("snap_tree_value_vec", "next_cookie", "error")
    class SnapTreeValue(_message.Message):
        __slots__ = ("entity_id", "value", "value_version", "cookie", "tree_id")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
        value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        cookie: int
        tree_id: int
        def __init__(self, entity_id: _Optional[int] = ..., value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., cookie: _Optional[int] = ..., tree_id: _Optional[int] = ...) -> None: ...
    SNAP_TREE_VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    snap_tree_value_vec: _containers.RepeatedCompositeFieldContainer[FetchViewSnapTreeValuesResult.SnapTreeValue]
    next_cookie: int
    error: _error_pb2.ErrorProto
    def __init__(self, snap_tree_value_vec: _Optional[_Iterable[_Union[FetchViewSnapTreeValuesResult.SnapTreeValue, _Mapping]]] = ..., next_cookie: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchViewSearchKeysArg(_message.Message):
    __slots__ = ("root_eh", "max_levels", "qos_context")
    ROOT_EH_FIELD_NUMBER: _ClassVar[int]
    MAX_LEVELS_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    root_eh: _entity_handle_pb2.EntityHandleProto
    max_levels: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, root_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., max_levels: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class FetchViewSearchKeysResult(_message.Message):
    __slots__ = ("key_int_vec", "key_str_vec", "num_leaves_estimate", "error")
    KEY_INT_VEC_FIELD_NUMBER: _ClassVar[int]
    KEY_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_LEAVES_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    key_int_vec: _containers.RepeatedScalarFieldContainer[int]
    key_str_vec: _containers.RepeatedScalarFieldContainer[str]
    num_leaves_estimate: int
    error: _error_pb2.ErrorProto
    def __init__(self, key_int_vec: _Optional[_Iterable[int]] = ..., key_str_vec: _Optional[_Iterable[str]] = ..., num_leaves_estimate: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TrackEntityHandleReadIOArg(_message.Message):
    __slots__ = ("track_file_eh_vec", "time_to_live_secs", "read_io_count", "is_persistent", "is_forwarded", "qos_context")
    TRACK_FILE_EH_VEC_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    READ_IO_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    track_file_eh_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    time_to_live_secs: int
    read_io_count: int
    is_persistent: bool
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, track_file_eh_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ..., time_to_live_secs: _Optional[int] = ..., read_io_count: _Optional[int] = ..., is_persistent: bool = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class TrackEntityHandleReadIOResult(_message.Message):
    __slots__ = ("track_result_vec", "error")
    class TrackResultProto(_message.Message):
        __slots__ = ("error", "entity_handle")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_handle: _entity_handle_pb2.EntityHandleProto
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    TRACK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    track_result_vec: _containers.RepeatedCompositeFieldContainer[TrackEntityHandleReadIOResult.TrackResultProto]
    error: _error_pb2.ErrorProto
    def __init__(self, track_result_vec: _Optional[_Iterable[_Union[TrackEntityHandleReadIOResult.TrackResultProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UntrackEntityHandleReadIOArg(_message.Message):
    __slots__ = ("untrack_file_eh_vec", "is_forwarded", "is_persistent", "qos_context")
    UNTRACK_FILE_EH_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    IS_PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    untrack_file_eh_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    is_forwarded: bool
    is_persistent: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, untrack_file_eh_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ..., is_forwarded: bool = ..., is_persistent: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class UntrackEntityHandleReadIOResult(_message.Message):
    __slots__ = ("error", "untrack_result_vec")
    class UntrackResultProto(_message.Message):
        __slots__ = ("error", "entity_handle")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_handle: _entity_handle_pb2.EntityHandleProto
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UNTRACK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    untrack_result_vec: _containers.RepeatedCompositeFieldContainer[UntrackEntityHandleReadIOResult.UntrackResultProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., untrack_result_vec: _Optional[_Iterable[_Union[UntrackEntityHandleReadIOResult.UntrackResultProto, _Mapping]]] = ...) -> None: ...

class GetNonPersistentTrackedIOTracesArg(_message.Message):
    __slots__ = ("eh_vec", "qos_context")
    EH_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, eh_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class GetNonPersistentTrackedIOTracesResult(_message.Message):
    __slots__ = ("error", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class AddNonPersistentIOTracesToPredictorArg(_message.Message):
    __slots__ = ("eh_vec", "time_to_live_secs", "data", "qos_context")
    EH_VEC_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    time_to_live_secs: int
    data: bytes
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, eh_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ..., time_to_live_secs: _Optional[int] = ..., data: _Optional[bytes] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class AddNonPersistentIOTracesToPredictorResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetCloudChunkFilesForExternalWriteArg(_message.Message):
    __slots__ = ("cloud_domain_id", "num_chunk_files_to_fetch", "qos_context")
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    num_chunk_files_to_fetch: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, cloud_domain_id: _Optional[int] = ..., num_chunk_files_to_fetch: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class GetCloudChunkFilesForExternalWriteResult(_message.Message):
    __slots__ = ("error", "cloud_chunk_file_vec", "view_box_id", "credentials")
    class CloudChunkFileInfo(_message.Message):
        __slots__ = ("cloud_object_id", "version", "ttl_secs")
        CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        TTL_SECS_FIELD_NUMBER: _ClassVar[int]
        cloud_object_id: _cloud_pb2.CloudObjectIdProto
        version: int
        ttl_secs: int
        def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., version: _Optional[int] = ..., ttl_secs: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cloud_chunk_file_vec: _containers.RepeatedCompositeFieldContainer[GetCloudChunkFilesForExternalWriteResult.CloudChunkFileInfo]
    view_box_id: int
    credentials: _cluster_config_pb2.ClusterConfigProto.CloudCredentials
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cloud_chunk_file_vec: _Optional[_Iterable[_Union[GetCloudChunkFilesForExternalWriteResult.CloudChunkFileInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., credentials: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.CloudCredentials, _Mapping]] = ...) -> None: ...

class ReleaseCloudChunkFileExternalWritePermArg(_message.Message):
    __slots__ = ("cloud_object_id_vec", "qos_context")
    CLOUD_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudObjectIdProto]
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, cloud_object_id_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class ReleaseCloudChunkFileExternalWritePermResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupNASUptierTableArg(_message.Message):
    __slots__ = ("eh", "qos_context")
    EH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class LookupNASUptierTableResult(_message.Message):
    __slots__ = ("uptier_entity_vec", "error")
    class UptierEntityValue(_message.Message):
        __slots__ = ("entity", "uptier_entity_value")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        UPTIER_ENTITY_VALUE_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_handle_pb2.EntityHandleProto
        uptier_entity_value: _snap_fs_metadata_pb2.UptierEntityProto
        def __init__(self, entity: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., uptier_entity_value: _Optional[_Union[_snap_fs_metadata_pb2.UptierEntityProto, _Mapping]] = ...) -> None: ...
    UPTIER_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    uptier_entity_vec: _containers.RepeatedCompositeFieldContainer[LookupNASUptierTableResult.UptierEntityValue]
    error: _error_pb2.ErrorProto
    def __init__(self, uptier_entity_vec: _Optional[_Iterable[_Union[LookupNASUptierTableResult.UptierEntityValue, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupPreferredIOParamsArg(_message.Message):
    __slots__ = ("view_id", "qos_context")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, view_id: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class LookupPreferredIOParamsResult(_message.Message):
    __slots__ = ("read_params", "write_params", "error")
    class IOParams(_message.Message):
        __slots__ = ("io_size",)
        IO_SIZE_FIELD_NUMBER: _ClassVar[int]
        io_size: int
        def __init__(self, io_size: _Optional[int] = ...) -> None: ...
    READ_PARAMS_FIELD_NUMBER: _ClassVar[int]
    WRITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    read_params: LookupPreferredIOParamsResult.IOParams
    write_params: LookupPreferredIOParamsResult.IOParams
    error: _error_pb2.ErrorProto
    def __init__(self, read_params: _Optional[_Union[LookupPreferredIOParamsResult.IOParams, _Mapping]] = ..., write_params: _Optional[_Union[LookupPreferredIOParamsResult.IOParams, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class InitOrClearDirectoryChangelogArg(_message.Message):
    __slots__ = ("eh", "start_time_usecs", "is_forwarded", "qos_context", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low")
    EH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    start_time_usecs: int
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class InitOrClearDirectoryChangelogResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BulkDeleteSnapTreeKeysArg(_message.Message):
    __slots__ = ("view_id", "snap_tree_root_node_id", "key_id_vec", "qos_context", "request_sequencer")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    snap_tree_root_node_id: int
    key_id_vec: _containers.RepeatedScalarFieldContainer[int]
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, view_id: _Optional[int] = ..., snap_tree_root_node_id: _Optional[int] = ..., key_id_vec: _Optional[_Iterable[int]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class BulkDeleteSnapTreeKeysResult(_message.Message):
    __slots__ = ("error", "error_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class BatchMinionDedupWriteArg(_message.Message):
    __slots__ = ("minion_entity_vec", "qos_context", "request_sequencer")
    class MinionEntityInfo(_message.Message):
        __slots__ = ("eh", "value", "dedup_range", "data", "view_snap_tree_id", "view_leaf_node_id", "original_snap_tree_node")
        EH_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_SNAP_TREE_NODE_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
        dedup_range: _dedup_range_pb2.DedupRange
        data: bytes
        view_snap_tree_id: int
        view_leaf_node_id: int
        original_snap_tree_node: _snap_tree_pb2.SnapTreeNodeProto
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., data: _Optional[bytes] = ..., view_snap_tree_id: _Optional[int] = ..., view_leaf_node_id: _Optional[int] = ..., original_snap_tree_node: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ...) -> None: ...
    MINION_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    minion_entity_vec: _containers.RepeatedCompositeFieldContainer[BatchMinionDedupWriteArg.MinionEntityInfo]
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_sequencer: RequestSequencer
    def __init__(self, minion_entity_vec: _Optional[_Iterable[_Union[BatchMinionDedupWriteArg.MinionEntityInfo, _Mapping]]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_sequencer: _Optional[_Union[RequestSequencer, _Mapping]] = ...) -> None: ...

class BatchMinionDedupWriteResult(_message.Message):
    __slots__ = ("write_result_vec", "error")
    class MinionEntityDedupWriteResult(_message.Message):
        __slots__ = ("eh", "missing_dedup_range", "view_leaf_node_id", "restored_stub_node")
        EH_FIELD_NUMBER: _ClassVar[int]
        MISSING_DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
        VIEW_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        RESTORED_STUB_NODE_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        missing_dedup_range: _dedup_range_pb2.DedupRange
        view_leaf_node_id: int
        restored_stub_node: _snap_tree_pb2.SnapTreeNodeProto
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., missing_dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., view_leaf_node_id: _Optional[int] = ..., restored_stub_node: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ...) -> None: ...
    WRITE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    write_result_vec: _containers.RepeatedCompositeFieldContainer[BatchMinionDedupWriteResult.MinionEntityDedupWriteResult]
    error: _error_pb2.ErrorProto
    def __init__(self, write_result_vec: _Optional[_Iterable[_Union[BatchMinionDedupWriteResult.MinionEntityDedupWriteResult, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
