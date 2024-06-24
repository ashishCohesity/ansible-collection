from bridge.base import error_pb2 as _error_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationViewMetadataProto(_message.Message):
    __slots__ = ("view_metadata", "view_logical_size")
    VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    view_metadata: _view_metadata_pb2.ViewIdMappingProto
    view_logical_size: int
    def __init__(self, view_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ..., view_logical_size: _Optional[int] = ...) -> None: ...

class ReplicationStatistics(_message.Message):
    __slots__ = ("file_sync_tx_op_median_run_time", "file_sync_tx_op_95_percentile_run_time", "file_sync_tx_op_median_logical_bytes", "file_sync_tx_op_95_percentile_logical_bytes", "file_sync_tx_op_count", "dir_sync_tx_op_median_run_time", "dir_sync_tx_op_95_percentile_run_time", "dir_sync_tx_op_median_verify_time", "dir_sync_tx_op_95_percentile_verify_time", "dir_sync_tx_op_median_num_children", "dir_sync_tx_op_95_percentile_num_children", "dir_sync_tx_op_count")
    FILE_SYNC_TX_OP_MEDIAN_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_TX_OP_95_PERCENTILE_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_TX_OP_MEDIAN_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_TX_OP_95_PERCENTILE_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_TX_OP_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_MEDIAN_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_95_PERCENTILE_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_MEDIAN_VERIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_95_PERCENTILE_VERIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_MEDIAN_NUM_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_95_PERCENTILE_NUM_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_COUNT_FIELD_NUMBER: _ClassVar[int]
    file_sync_tx_op_median_run_time: float
    file_sync_tx_op_95_percentile_run_time: float
    file_sync_tx_op_median_logical_bytes: float
    file_sync_tx_op_95_percentile_logical_bytes: float
    file_sync_tx_op_count: int
    dir_sync_tx_op_median_run_time: float
    dir_sync_tx_op_95_percentile_run_time: float
    dir_sync_tx_op_median_verify_time: float
    dir_sync_tx_op_95_percentile_verify_time: float
    dir_sync_tx_op_median_num_children: float
    dir_sync_tx_op_95_percentile_num_children: float
    dir_sync_tx_op_count: int
    def __init__(self, file_sync_tx_op_median_run_time: _Optional[float] = ..., file_sync_tx_op_95_percentile_run_time: _Optional[float] = ..., file_sync_tx_op_median_logical_bytes: _Optional[float] = ..., file_sync_tx_op_95_percentile_logical_bytes: _Optional[float] = ..., file_sync_tx_op_count: _Optional[int] = ..., dir_sync_tx_op_median_run_time: _Optional[float] = ..., dir_sync_tx_op_95_percentile_run_time: _Optional[float] = ..., dir_sync_tx_op_median_verify_time: _Optional[float] = ..., dir_sync_tx_op_95_percentile_verify_time: _Optional[float] = ..., dir_sync_tx_op_median_num_children: _Optional[float] = ..., dir_sync_tx_op_95_percentile_num_children: _Optional[float] = ..., dir_sync_tx_op_count: _Optional[int] = ...) -> None: ...

class MasterReplicationStateProto(_message.Message):
    __slots__ = ("remote_cluster_name", "application_name", "replication_id", "application_view_name", "entity_chain_id", "replication_view_metadata", "handshake_completed_time_usecs", "start_time_usecs", "completion_time_usecs", "completion_notified", "expiry_time_usecs", "internal_view_name", "snap_tree_root_node_ceiling", "error", "pinned_refcount", "marked_for_deletion", "marked_for_cancellation", "cancellation_reason", "metadata_actions_completed", "total_metadata_actions", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "view_logical_size", "opaque_metadata_size", "ancestor_replication_id_hint", "max_rsync_enum", "replication_protocol", "handshake_completed", "remote_cluster_id", "remote_cluster_incarnation_id", "tx_viewbox_id", "rx_viewbox_brick_size", "view_transmit_op_state", "view_receive_op_state", "high_priority", "key_encryption_key", "session_encryption_key", "compression_enabled", "rx_megafile_supported", "view_user_quota_data_supported", "view_dir_quota_data_supported", "replicate_special_files", "tmp_dir_name", "is_out_of_band", "force_full_replication", "delete_ancestor_views", "tx_supports_ping_remote_cluster", "blackout_remaining_time_usecs", "estimated_logical_bytes_to_transfer", "estimated_changed_entities", "synced_files_logical_size_sum", "is_failover_replication", "enable_dir_sync_verification", "app_handler_context", "ancestor_rid", "logical_bytes_transferred_object_ns", "metadata_actions_completed_object_ns", "is_full_replication", "marked_for_pause", "pause_reason", "is_paused", "is_v2_replication", "application_ancestor_view_name", "ancestor_internal_view_name", "ignore_ancestor_not_found_error", "divergence_searching_and_fixing_replication_running", "is_app_view_replication_divergent_safe", "replication_stats", "encryption_mode", "application_job_id", "application_job_run_id", "application_job_name", "application_entity_name", "last_progress_timestamp_usecs", "tx_viewbox_id_DEPRECATED")
    class ReplicationProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRsyncPigeonDedup: _ClassVar[MasterReplicationStateProto.ReplicationProtocol]
        kRsyncPigeonMetadata: _ClassVar[MasterReplicationStateProto.ReplicationProtocol]
        kRsyncSnapTreeDiff: _ClassVar[MasterReplicationStateProto.ReplicationProtocol]
        kRsync: _ClassVar[MasterReplicationStateProto.ReplicationProtocol]
        kRsyncPigeon: _ClassVar[MasterReplicationStateProto.ReplicationProtocol]
    kRsyncPigeonDedup: MasterReplicationStateProto.ReplicationProtocol
    kRsyncPigeonMetadata: MasterReplicationStateProto.ReplicationProtocol
    kRsyncSnapTreeDiff: MasterReplicationStateProto.ReplicationProtocol
    kRsync: MasterReplicationStateProto.ReplicationProtocol
    kRsyncPigeon: MasterReplicationStateProto.ReplicationProtocol
    class ViewTransmitOpState(_message.Message):
        __slots__ = ("slave_checkpoint", "pinned_replication_id_vec", "slave_session_id", "slave_logical_timestamp", "error", "backup_quota_data_completed")
        SLAVE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        PINNED_REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SLAVE_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        BACKUP_QUOTA_DATA_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        slave_checkpoint: bytes
        pinned_replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        slave_session_id: int
        slave_logical_timestamp: int
        error: _error_pb2.ErrorProto
        backup_quota_data_completed: bool
        def __init__(self, slave_checkpoint: _Optional[bytes] = ..., pinned_replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., slave_session_id: _Optional[int] = ..., slave_logical_timestamp: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_quota_data_completed: bool = ...) -> None: ...
    class ViewReceiveOpState(_message.Message):
        __slots__ = ("pinned_replication_id", "view_box_id", "restore_quota_data_completed")
        PINNED_REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_QUOTA_DATA_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        pinned_replication_id: _universal_id_pb2.UniversalIdProto
        view_box_id: int
        restore_quota_data_completed: bool
        def __init__(self, pinned_replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_box_id: _Optional[int] = ..., restore_quota_data_completed: bool = ...) -> None: ...
    class AppHandlerContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_COMPLETED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ROOT_NODE_CEILING_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PINNED_REFCOUNT_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_METADATA_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_METADATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    MAX_RSYNC_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    RX_VIEWBOX_BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    VIEW_TRANSMIT_OP_STATE_FIELD_NUMBER: _ClassVar[int]
    VIEW_RECEIVE_OP_STATE_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    KEY_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RX_MEGAFILE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VIEW_USER_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VIEW_DIR_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_SPECIAL_FILES_FIELD_NUMBER: _ClassVar[int]
    TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    DELETE_ANCESTOR_VIEWS_FIELD_NUMBER: _ClassVar[int]
    TX_SUPPORTS_PING_REMOTE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    BLACKOUT_REMAINING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SYNCED_FILES_LOGICAL_SIZE_SUM_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DIR_SYNC_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    APP_HANDLER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_RID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_PAUSE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_REASON_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    IS_V2_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ANCESTOR_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ANCESTOR_NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
    DIVERGENCE_SEARCHING_AND_FIXING_REPLICATION_RUNNING_FIELD_NUMBER: _ClassVar[int]
    IS_APP_VIEW_REPLICATION_DIVERGENT_SAFE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STATS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_PROGRESS_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    TX_VIEWBOX_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    remote_cluster_name: str
    application_name: str
    replication_id: _universal_id_pb2.UniversalIdProto
    application_view_name: str
    entity_chain_id: str
    replication_view_metadata: ReplicationViewMetadataProto
    handshake_completed_time_usecs: int
    start_time_usecs: int
    completion_time_usecs: int
    completion_notified: bool
    expiry_time_usecs: int
    internal_view_name: str
    snap_tree_root_node_ceiling: int
    error: _error_pb2.ErrorProto
    pinned_refcount: int
    marked_for_deletion: bool
    marked_for_cancellation: bool
    cancellation_reason: str
    metadata_actions_completed: int
    total_metadata_actions: int
    pct_completed: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    view_logical_size: int
    opaque_metadata_size: int
    ancestor_replication_id_hint: _universal_id_pb2.UniversalIdProto
    max_rsync_enum: int
    replication_protocol: MasterReplicationStateProto.ReplicationProtocol
    handshake_completed: bool
    remote_cluster_id: int
    remote_cluster_incarnation_id: int
    tx_viewbox_id: int
    rx_viewbox_brick_size: int
    view_transmit_op_state: MasterReplicationStateProto.ViewTransmitOpState
    view_receive_op_state: MasterReplicationStateProto.ViewReceiveOpState
    high_priority: bool
    key_encryption_key: bytes
    session_encryption_key: bytes
    compression_enabled: bool
    rx_megafile_supported: bool
    view_user_quota_data_supported: bool
    view_dir_quota_data_supported: bool
    replicate_special_files: bool
    tmp_dir_name: str
    is_out_of_band: bool
    force_full_replication: bool
    delete_ancestor_views: bool
    tx_supports_ping_remote_cluster: bool
    blackout_remaining_time_usecs: int
    estimated_logical_bytes_to_transfer: int
    estimated_changed_entities: int
    synced_files_logical_size_sum: int
    is_failover_replication: bool
    enable_dir_sync_verification: bool
    app_handler_context: _containers.ScalarMap[str, str]
    ancestor_rid: _universal_id_pb2.UniversalIdProto
    logical_bytes_transferred_object_ns: int
    metadata_actions_completed_object_ns: int
    is_full_replication: bool
    marked_for_pause: bool
    pause_reason: str
    is_paused: bool
    is_v2_replication: bool
    application_ancestor_view_name: str
    ancestor_internal_view_name: str
    ignore_ancestor_not_found_error: bool
    divergence_searching_and_fixing_replication_running: bool
    is_app_view_replication_divergent_safe: bool
    replication_stats: ReplicationStatistics
    encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    application_job_id: int
    application_job_run_id: int
    application_job_name: str
    application_entity_name: str
    last_progress_timestamp_usecs: int
    tx_viewbox_id_DEPRECATED: int
    def __init__(self, remote_cluster_name: _Optional[str] = ..., application_name: _Optional[str] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., application_view_name: _Optional[str] = ..., entity_chain_id: _Optional[str] = ..., replication_view_metadata: _Optional[_Union[ReplicationViewMetadataProto, _Mapping]] = ..., handshake_completed_time_usecs: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., completion_time_usecs: _Optional[int] = ..., completion_notified: bool = ..., expiry_time_usecs: _Optional[int] = ..., internal_view_name: _Optional[str] = ..., snap_tree_root_node_ceiling: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pinned_refcount: _Optional[int] = ..., marked_for_deletion: bool = ..., marked_for_cancellation: bool = ..., cancellation_reason: _Optional[str] = ..., metadata_actions_completed: _Optional[int] = ..., total_metadata_actions: _Optional[int] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., view_logical_size: _Optional[int] = ..., opaque_metadata_size: _Optional[int] = ..., ancestor_replication_id_hint: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., max_rsync_enum: _Optional[int] = ..., replication_protocol: _Optional[_Union[MasterReplicationStateProto.ReplicationProtocol, str]] = ..., handshake_completed: bool = ..., remote_cluster_id: _Optional[int] = ..., remote_cluster_incarnation_id: _Optional[int] = ..., tx_viewbox_id: _Optional[int] = ..., rx_viewbox_brick_size: _Optional[int] = ..., view_transmit_op_state: _Optional[_Union[MasterReplicationStateProto.ViewTransmitOpState, _Mapping]] = ..., view_receive_op_state: _Optional[_Union[MasterReplicationStateProto.ViewReceiveOpState, _Mapping]] = ..., high_priority: bool = ..., key_encryption_key: _Optional[bytes] = ..., session_encryption_key: _Optional[bytes] = ..., compression_enabled: bool = ..., rx_megafile_supported: bool = ..., view_user_quota_data_supported: bool = ..., view_dir_quota_data_supported: bool = ..., replicate_special_files: bool = ..., tmp_dir_name: _Optional[str] = ..., is_out_of_band: bool = ..., force_full_replication: bool = ..., delete_ancestor_views: bool = ..., tx_supports_ping_remote_cluster: bool = ..., blackout_remaining_time_usecs: _Optional[int] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., estimated_changed_entities: _Optional[int] = ..., synced_files_logical_size_sum: _Optional[int] = ..., is_failover_replication: bool = ..., enable_dir_sync_verification: bool = ..., app_handler_context: _Optional[_Mapping[str, str]] = ..., ancestor_rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., logical_bytes_transferred_object_ns: _Optional[int] = ..., metadata_actions_completed_object_ns: _Optional[int] = ..., is_full_replication: bool = ..., marked_for_pause: bool = ..., pause_reason: _Optional[str] = ..., is_paused: bool = ..., is_v2_replication: bool = ..., application_ancestor_view_name: _Optional[str] = ..., ancestor_internal_view_name: _Optional[str] = ..., ignore_ancestor_not_found_error: bool = ..., divergence_searching_and_fixing_replication_running: bool = ..., is_app_view_replication_divergent_safe: bool = ..., replication_stats: _Optional[_Union[ReplicationStatistics, _Mapping]] = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., application_job_id: _Optional[int] = ..., application_job_run_id: _Optional[int] = ..., application_job_name: _Optional[str] = ..., application_entity_name: _Optional[str] = ..., last_progress_timestamp_usecs: _Optional[int] = ..., tx_viewbox_id_DEPRECATED: _Optional[int] = ...) -> None: ...
