from bridge.base import error_pb2 as _error_pb2
from bridge.madrox import master_replication_state_pb2 as _master_replication_state_pb2
from bridge.madrox import master_state_pb2 as _master_state_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MasterWALRecordProto(_message.Message):
    __slots__ = ("replication_state_vec", "rid_mark_for_deletion", "rid_delete", "mark_for_cancellation", "rid_cancel", "rid_completion_notified", "pin_unpin_ancestors", "handshake_completed", "progress_report", "assign_slave", "complete_replication", "rid_marked_for_expiration", "application_job_marked_for_expiration", "application_job_expired", "rid_backup_or_restore_quota_data_completed", "remote_cluster_info_vec", "add_or_update_remote_cluster", "delete_remote_cluster", "add_app_handler_context", "mark_for_pause", "rid_pause", "mark_for_unpause")
    class MarkForCancellation(_message.Message):
        __slots__ = ("rid", "reason")
        RID_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        rid: _universal_id_pb2.UniversalIdProto
        reason: str
        def __init__(self, rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
    class PinUnpinAncestors(_message.Message):
        __slots__ = ("replication_id", "ancestor_rid_vec", "perform_pin", "unpin_for_completion_DEPRECATED")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_RID_VEC_FIELD_NUMBER: _ClassVar[int]
        PERFORM_PIN_FIELD_NUMBER: _ClassVar[int]
        UNPIN_FOR_COMPLETION_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        ancestor_rid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        perform_pin: bool
        unpin_for_completion_DEPRECATED: bool
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., ancestor_rid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., perform_pin: bool = ..., unpin_for_completion_DEPRECATED: bool = ...) -> None: ...
    class HandshakeCompleted(_message.Message):
        __slots__ = ("replication_id", "replication_protocol", "time_usecs", "remote_cluster_id", "remote_cluster_incarnation_id", "tx_viewbox_id", "rx_viewbox_brick_size", "session_encryption_key", "rx_megafile_supported", "view_user_quota_data_supported", "compression_enabled_DEPRECATED", "replicate_special_files", "tmp_dir_name", "view_dir_quota_data_supported", "enable_dir_sync_verification", "ancestor_rid", "run_divergence_searching_and_fixing_replication", "is_app_view_replication_divergent_safe")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        REMOTE_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        TX_VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        RX_VIEWBOX_BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        SESSION_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        RX_MEGAFILE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        VIEW_USER_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_ENABLED_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        REPLICATE_SPECIAL_FILES_FIELD_NUMBER: _ClassVar[int]
        TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_DIR_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        ENABLE_DIR_SYNC_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_RID_FIELD_NUMBER: _ClassVar[int]
        RUN_DIVERGENCE_SEARCHING_AND_FIXING_REPLICATION_FIELD_NUMBER: _ClassVar[int]
        IS_APP_VIEW_REPLICATION_DIVERGENT_SAFE_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        replication_protocol: _master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol
        time_usecs: int
        remote_cluster_id: int
        remote_cluster_incarnation_id: int
        tx_viewbox_id: int
        rx_viewbox_brick_size: int
        session_encryption_key: bytes
        rx_megafile_supported: bool
        view_user_quota_data_supported: bool
        compression_enabled_DEPRECATED: bool
        replicate_special_files: bool
        tmp_dir_name: str
        view_dir_quota_data_supported: bool
        enable_dir_sync_verification: bool
        ancestor_rid: _universal_id_pb2.UniversalIdProto
        run_divergence_searching_and_fixing_replication: bool
        is_app_view_replication_divergent_safe: bool
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_protocol: _Optional[_Union[_master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol, str]] = ..., time_usecs: _Optional[int] = ..., remote_cluster_id: _Optional[int] = ..., remote_cluster_incarnation_id: _Optional[int] = ..., tx_viewbox_id: _Optional[int] = ..., rx_viewbox_brick_size: _Optional[int] = ..., session_encryption_key: _Optional[bytes] = ..., rx_megafile_supported: bool = ..., view_user_quota_data_supported: bool = ..., compression_enabled_DEPRECATED: bool = ..., replicate_special_files: bool = ..., tmp_dir_name: _Optional[str] = ..., view_dir_quota_data_supported: bool = ..., enable_dir_sync_verification: bool = ..., ancestor_rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_divergence_searching_and_fixing_replication: bool = ..., is_app_view_replication_divergent_safe: bool = ...) -> None: ...
    class ProgressReport(_message.Message):
        __slots__ = ("replication_id", "slave_session_id", "slave_logical_timestamp", "slave_state_checkpoint", "metadata_actions_completed", "total_metadata_actions", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "view_logical_size", "estimated_logical_bytes_to_transfer", "estimated_changed_entities", "synced_files_logical_size_sum", "logical_bytes_transferred_object_ns", "metadata_actions_completed_object_ns", "dir_sync_progress_detected", "replication_stats", "error")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SLAVE_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SLAVE_STATE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_METADATA_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        SYNCED_FILES_LOGICAL_SIZE_SUM_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
        METADATA_ACTIONS_COMPLETED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
        DIR_SYNC_PROGRESS_DETECTED_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_STATS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        slave_session_id: int
        slave_logical_timestamp: int
        slave_state_checkpoint: bytes
        metadata_actions_completed: int
        total_metadata_actions: int
        pct_completed: int
        logical_bytes_transferred: int
        physical_bytes_transferred: int
        view_logical_size: int
        estimated_logical_bytes_to_transfer: int
        estimated_changed_entities: int
        synced_files_logical_size_sum: int
        logical_bytes_transferred_object_ns: int
        metadata_actions_completed_object_ns: int
        dir_sync_progress_detected: bool
        replication_stats: _master_replication_state_pb2.ReplicationStatistics
        error: _error_pb2.ErrorProto
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., slave_session_id: _Optional[int] = ..., slave_logical_timestamp: _Optional[int] = ..., slave_state_checkpoint: _Optional[bytes] = ..., metadata_actions_completed: _Optional[int] = ..., total_metadata_actions: _Optional[int] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., view_logical_size: _Optional[int] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., estimated_changed_entities: _Optional[int] = ..., synced_files_logical_size_sum: _Optional[int] = ..., logical_bytes_transferred_object_ns: _Optional[int] = ..., metadata_actions_completed_object_ns: _Optional[int] = ..., dir_sync_progress_detected: bool = ..., replication_stats: _Optional[_Union[_master_replication_state_pb2.ReplicationStatistics, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class AssignSlave(_message.Message):
        __slots__ = ("replication_id", "slave_session_id", "time_usecs")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        slave_session_id: int
        time_usecs: int
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., slave_session_id: _Optional[int] = ..., time_usecs: _Optional[int] = ...) -> None: ...
    class CompleteReplication(_message.Message):
        __slots__ = ("replication_id", "time_usecs", "error", "is_tracking_view_already_live", "is_app_view_replication_divergent_safe")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        IS_TRACKING_VIEW_ALREADY_LIVE_FIELD_NUMBER: _ClassVar[int]
        IS_APP_VIEW_REPLICATION_DIVERGENT_SAFE_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        time_usecs: int
        error: _error_pb2.ErrorProto
        is_tracking_view_already_live: bool
        is_app_view_replication_divergent_safe: bool
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_tracking_view_already_live: bool = ..., is_app_view_replication_divergent_safe: bool = ...) -> None: ...
    class AddAppHandlerContext(_message.Message):
        __slots__ = ("replication_id", "app_handler_context")
        class AppHandlerContextEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        APP_HANDLER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        app_handler_context: _containers.ScalarMap[str, str]
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_handler_context: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class MarkForPause(_message.Message):
        __slots__ = ("rid", "reason")
        RID_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        rid: _universal_id_pb2.UniversalIdProto
        reason: str
        def __init__(self, rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
    class MarkForUnpause(_message.Message):
        __slots__ = ("rid",)
        RID_FIELD_NUMBER: _ClassVar[int]
        rid: _universal_id_pb2.UniversalIdProto
        def __init__(self, rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    REPLICATION_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    RID_MARK_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    RID_DELETE_FIELD_NUMBER: _ClassVar[int]
    MARK_FOR_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    RID_CANCEL_FIELD_NUMBER: _ClassVar[int]
    RID_COMPLETION_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    PIN_UNPIN_ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_REPORT_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_SLAVE_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    RID_MARKED_FOR_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_MARKED_FOR_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    RID_BACKUP_OR_RESTORE_QUOTA_DATA_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_REMOTE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DELETE_REMOTE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ADD_APP_HANDLER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MARK_FOR_PAUSE_FIELD_NUMBER: _ClassVar[int]
    RID_PAUSE_FIELD_NUMBER: _ClassVar[int]
    MARK_FOR_UNPAUSE_FIELD_NUMBER: _ClassVar[int]
    replication_state_vec: _containers.RepeatedCompositeFieldContainer[_master_replication_state_pb2.MasterReplicationStateProto]
    rid_mark_for_deletion: _universal_id_pb2.UniversalIdProto
    rid_delete: _universal_id_pb2.UniversalIdProto
    mark_for_cancellation: MasterWALRecordProto.MarkForCancellation
    rid_cancel: _universal_id_pb2.UniversalIdProto
    rid_completion_notified: _universal_id_pb2.UniversalIdProto
    pin_unpin_ancestors: MasterWALRecordProto.PinUnpinAncestors
    handshake_completed: MasterWALRecordProto.HandshakeCompleted
    progress_report: MasterWALRecordProto.ProgressReport
    assign_slave: MasterWALRecordProto.AssignSlave
    complete_replication: MasterWALRecordProto.CompleteReplication
    rid_marked_for_expiration: _universal_id_pb2.UniversalIdProto
    application_job_marked_for_expiration: int
    application_job_expired: int
    rid_backup_or_restore_quota_data_completed: _universal_id_pb2.UniversalIdProto
    remote_cluster_info_vec: _containers.RepeatedCompositeFieldContainer[_master_state_pb2.RemoteClusterInfoProto]
    add_or_update_remote_cluster: _master_state_pb2.RemoteClusterInfoProto
    delete_remote_cluster: _master_state_pb2.RemoteClusterInfoProto
    add_app_handler_context: MasterWALRecordProto.AddAppHandlerContext
    mark_for_pause: MasterWALRecordProto.MarkForPause
    rid_pause: _universal_id_pb2.UniversalIdProto
    mark_for_unpause: MasterWALRecordProto.MarkForUnpause
    def __init__(self, replication_state_vec: _Optional[_Iterable[_Union[_master_replication_state_pb2.MasterReplicationStateProto, _Mapping]]] = ..., rid_mark_for_deletion: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rid_delete: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., mark_for_cancellation: _Optional[_Union[MasterWALRecordProto.MarkForCancellation, _Mapping]] = ..., rid_cancel: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rid_completion_notified: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., pin_unpin_ancestors: _Optional[_Union[MasterWALRecordProto.PinUnpinAncestors, _Mapping]] = ..., handshake_completed: _Optional[_Union[MasterWALRecordProto.HandshakeCompleted, _Mapping]] = ..., progress_report: _Optional[_Union[MasterWALRecordProto.ProgressReport, _Mapping]] = ..., assign_slave: _Optional[_Union[MasterWALRecordProto.AssignSlave, _Mapping]] = ..., complete_replication: _Optional[_Union[MasterWALRecordProto.CompleteReplication, _Mapping]] = ..., rid_marked_for_expiration: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., application_job_marked_for_expiration: _Optional[int] = ..., application_job_expired: _Optional[int] = ..., rid_backup_or_restore_quota_data_completed: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., remote_cluster_info_vec: _Optional[_Iterable[_Union[_master_state_pb2.RemoteClusterInfoProto, _Mapping]]] = ..., add_or_update_remote_cluster: _Optional[_Union[_master_state_pb2.RemoteClusterInfoProto, _Mapping]] = ..., delete_remote_cluster: _Optional[_Union[_master_state_pb2.RemoteClusterInfoProto, _Mapping]] = ..., add_app_handler_context: _Optional[_Union[MasterWALRecordProto.AddAppHandlerContext, _Mapping]] = ..., mark_for_pause: _Optional[_Union[MasterWALRecordProto.MarkForPause, _Mapping]] = ..., rid_pause: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., mark_for_unpause: _Optional[_Union[MasterWALRecordProto.MarkForUnpause, _Mapping]] = ...) -> None: ...
