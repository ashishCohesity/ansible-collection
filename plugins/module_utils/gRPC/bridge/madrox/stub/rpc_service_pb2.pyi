from bridge.base import error_pb2 as _error_pb2
from bridge.madrox import load_info_pb2 as _load_info_pb2
from bridge.madrox import master_replication_state_pb2 as _master_replication_state_pb2
from bridge.madrox import rsync_pigeon_pb2 as _rsync_pigeon_pb2
from bridge.madrox import rsync_snap_tree_diff_pb2 as _rsync_snap_tree_diff_pb2
from bridge.madrox.stub import rsync_inode_sync_work_pb2 as _rsync_inode_sync_work_pb2
from bridge.madrox.stub import rsync_custom_snap_tree_work_pb2 as _rsync_custom_snap_tree_work_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleReplicationArg(_message.Message):
    __slots__ = ("remote_cluster_name", "view_name", "entity_chain_id", "application_name", "replication_id", "snapshot_expiry_secs", "ancestor_replication_id_hint", "high_priority", "disable_rx_megafile", "is_out_of_band", "force_full_replication", "delete_ancestor_views", "is_failover_replication", "application_job_id", "application_job_run_id", "application_job_name", "application_entity_name")
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_SECS_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RX_MEGAFILE_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    DELETE_ANCESTOR_VIEWS_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    remote_cluster_name: str
    view_name: str
    entity_chain_id: str
    application_name: str
    replication_id: _universal_id_pb2.UniversalIdProto
    snapshot_expiry_secs: int
    ancestor_replication_id_hint: _universal_id_pb2.UniversalIdProto
    high_priority: bool
    disable_rx_megafile: bool
    is_out_of_band: bool
    force_full_replication: bool
    delete_ancestor_views: bool
    is_failover_replication: bool
    application_job_id: int
    application_job_run_id: int
    application_job_name: str
    application_entity_name: str
    def __init__(self, remote_cluster_name: _Optional[str] = ..., view_name: _Optional[str] = ..., entity_chain_id: _Optional[str] = ..., application_name: _Optional[str] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., snapshot_expiry_secs: _Optional[int] = ..., ancestor_replication_id_hint: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., high_priority: bool = ..., disable_rx_megafile: bool = ..., is_out_of_band: bool = ..., force_full_replication: bool = ..., delete_ancestor_views: bool = ..., is_failover_replication: bool = ..., application_job_id: _Optional[int] = ..., application_job_run_id: _Optional[int] = ..., application_job_name: _Optional[str] = ..., application_entity_name: _Optional[str] = ...) -> None: ...

class ScheduleReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScheduleReplicationV2Arg(_message.Message):
    __slots__ = ("remote_cluster_name", "application_view_name", "application_ancestor_view_name", "application_name", "replication_id", "ignore_ancestor_not_found_error", "application_job_id", "application_job_run_id", "application_job_name", "application_entity_name")
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ANCESTOR_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ANCESTOR_NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    remote_cluster_name: str
    application_view_name: str
    application_ancestor_view_name: str
    application_name: str
    replication_id: _universal_id_pb2.UniversalIdProto
    ignore_ancestor_not_found_error: bool
    application_job_id: int
    application_job_run_id: int
    application_job_name: str
    application_entity_name: str
    def __init__(self, remote_cluster_name: _Optional[str] = ..., application_view_name: _Optional[str] = ..., application_ancestor_view_name: _Optional[str] = ..., application_name: _Optional[str] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., ignore_ancestor_not_found_error: bool = ..., application_job_id: _Optional[int] = ..., application_job_run_id: _Optional[int] = ..., application_job_name: _Optional[str] = ..., application_entity_name: _Optional[str] = ...) -> None: ...

class ScheduleReplicationV2Result(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelReplicationArg(_message.Message):
    __slots__ = ("replication_id", "reason")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    reason: str
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseReplicationArg(_message.Message):
    __slots__ = ("replication_id", "reason")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    reason: str
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class PauseReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnpauseReplicationArg(_message.Message):
    __slots__ = ("replication_id",)
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class UnpauseReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListReplicationsArg(_message.Message):
    __slots__ = ("application_name",)
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    def __init__(self, application_name: _Optional[str] = ...) -> None: ...

class ListReplicationsResult(_message.Message):
    __slots__ = ("replication_id_vec",)
    REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class QueryReplicationArg(_message.Message):
    __slots__ = ("replication_id_vec", "include_opaque_metadata")
    REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    include_opaque_metadata: bool
    def __init__(self, replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., include_opaque_metadata: bool = ...) -> None: ...

class QueryReplicationResult(_message.Message):
    __slots__ = ("replication_state_vec",)
    REPLICATION_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_state_vec: _containers.RepeatedCompositeFieldContainer[_master_replication_state_pb2.MasterReplicationStateProto]
    def __init__(self, replication_state_vec: _Optional[_Iterable[_Union[_master_replication_state_pb2.MasterReplicationStateProto, _Mapping]]] = ...) -> None: ...

class ExpireReplicationsArg(_message.Message):
    __slots__ = ("application_name", "view_name_vec", "entity_chain_id_vec", "application_job_uid")
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CHAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    entity_chain_id_vec: _containers.RepeatedScalarFieldContainer[str]
    application_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, application_name: _Optional[str] = ..., view_name_vec: _Optional[_Iterable[str]] = ..., entity_chain_id_vec: _Optional[_Iterable[str]] = ..., application_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ExpireReplicationsResult(_message.Message):
    __slots__ = ("view_name_error_vec", "entity_chain_error_vec")
    VIEW_NAME_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CHAIN_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    view_name_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    entity_chain_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, view_name_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., entity_chain_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class StartViewReplicationArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "rx_view_box_id", "application_name", "application_view_name", "entity_chain_id", "replication_view_metadata", "replication_id", "replication_protocol", "max_supported_replication_protocol", "ancestor_replication_id_vec", "expiry_time_usecs", "compression_enabled", "encryption_enabled", "is_out_of_band", "encrypted_key_vec", "view_user_quota_data_supported", "ping_remote_cluster_supported", "view_dir_quota_data_supported", "encryption_mode")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPORTED_REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_USER_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    PING_REMOTE_CLUSTER_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VIEW_DIR_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    rx_view_box_id: int
    application_name: str
    application_view_name: str
    entity_chain_id: str
    replication_view_metadata: _master_replication_state_pb2.ReplicationViewMetadataProto
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_protocol: _master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol
    max_supported_replication_protocol: int
    ancestor_replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    expiry_time_usecs: int
    compression_enabled: bool
    encryption_enabled: bool
    is_out_of_band: bool
    encrypted_key_vec: _containers.RepeatedScalarFieldContainer[bytes]
    view_user_quota_data_supported: bool
    ping_remote_cluster_supported: bool
    view_dir_quota_data_supported: bool
    encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., rx_view_box_id: _Optional[int] = ..., application_name: _Optional[str] = ..., application_view_name: _Optional[str] = ..., entity_chain_id: _Optional[str] = ..., replication_view_metadata: _Optional[_Union[_master_replication_state_pb2.ReplicationViewMetadataProto, _Mapping]] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_protocol: _Optional[_Union[_master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol, str]] = ..., max_supported_replication_protocol: _Optional[int] = ..., ancestor_replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., expiry_time_usecs: _Optional[int] = ..., compression_enabled: bool = ..., encryption_enabled: bool = ..., is_out_of_band: bool = ..., encrypted_key_vec: _Optional[_Iterable[bytes]] = ..., view_user_quota_data_supported: bool = ..., ping_remote_cluster_supported: bool = ..., view_dir_quota_data_supported: bool = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...

class StartViewReplicationResult(_message.Message):
    __slots__ = ("replication_protocol", "ancestor_replication_id", "rx_viewbox_brick_size", "compression_supported", "session_encryption_key", "rx_megafile_supported", "view_user_quota_data_supported", "replicate_special_files", "s3_key_mapping_supported", "view_dir_quota_data_supported", "rx_swift_view_supported", "rx_dir_sync_verification_supported", "object_store_views_object_names_slashes_supported", "s3_object_snap_tree_supported", "s3_bucket_policy_supported", "s3_bucket_ownership_controls_supported", "s3_object_tagging_supported", "rx_divergence_searching_and_fixing_supported", "s3_efficient_mpu_supported", "filer_lcm_supported")
    REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_VIEWBOX_BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    RX_MEGAFILE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VIEW_USER_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_SPECIAL_FILES_FIELD_NUMBER: _ClassVar[int]
    S3_KEY_MAPPING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VIEW_DIR_QUOTA_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RX_SWIFT_VIEW_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RX_DIR_SYNC_VERIFICATION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_VIEWS_OBJECT_NAMES_SLASHES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_OBJECT_SNAP_TREE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_POLICY_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_OWNERSHIP_CONTROLS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_OBJECT_TAGGING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RX_DIVERGENCE_SEARCHING_AND_FIXING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_EFFICIENT_MPU_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FILER_LCM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    replication_protocol: _master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol
    ancestor_replication_id: _universal_id_pb2.UniversalIdProto
    rx_viewbox_brick_size: int
    compression_supported: bool
    session_encryption_key: bytes
    rx_megafile_supported: bool
    view_user_quota_data_supported: bool
    replicate_special_files: bool
    s3_key_mapping_supported: bool
    view_dir_quota_data_supported: bool
    rx_swift_view_supported: bool
    rx_dir_sync_verification_supported: bool
    object_store_views_object_names_slashes_supported: bool
    s3_object_snap_tree_supported: bool
    s3_bucket_policy_supported: bool
    s3_bucket_ownership_controls_supported: bool
    s3_object_tagging_supported: bool
    rx_divergence_searching_and_fixing_supported: bool
    s3_efficient_mpu_supported: bool
    filer_lcm_supported: bool
    def __init__(self, replication_protocol: _Optional[_Union[_master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol, str]] = ..., ancestor_replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., rx_viewbox_brick_size: _Optional[int] = ..., compression_supported: bool = ..., session_encryption_key: _Optional[bytes] = ..., rx_megafile_supported: bool = ..., view_user_quota_data_supported: bool = ..., replicate_special_files: bool = ..., s3_key_mapping_supported: bool = ..., view_dir_quota_data_supported: bool = ..., rx_swift_view_supported: bool = ..., rx_dir_sync_verification_supported: bool = ..., object_store_views_object_names_slashes_supported: bool = ..., s3_object_snap_tree_supported: bool = ..., s3_bucket_policy_supported: bool = ..., s3_bucket_ownership_controls_supported: bool = ..., s3_object_tagging_supported: bool = ..., rx_divergence_searching_and_fixing_supported: bool = ..., s3_efficient_mpu_supported: bool = ..., filer_lcm_supported: bool = ...) -> None: ...

class ProgressReport(_message.Message):
    __slots__ = ("replication_id", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "view_logical_size")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    pct_completed: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    view_logical_size: int
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., view_logical_size: _Optional[int] = ...) -> None: ...

class CompleteViewReplicationArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "error", "cleanup_dst_tmp_dir_name", "progress_report")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_DST_TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_REPORT_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    error: _error_pb2.ErrorProto
    cleanup_dst_tmp_dir_name: str
    progress_report: ProgressReport
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cleanup_dst_tmp_dir_name: _Optional[str] = ..., progress_report: _Optional[_Union[ProgressReport, _Mapping]] = ...) -> None: ...

class CompleteViewReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckViewReplicationArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CheckViewReplicationResult(_message.Message):
    __slots__ = ("error", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "view_logical_size")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pct_completed: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    view_logical_size: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., view_logical_size: _Optional[int] = ...) -> None: ...

class ResumeViewReplicationArg(_message.Message):
    __slots__ = ("expected_slave_session_id", "replication_id", "remote_cluster_name", "expected_remote_cluster_id", "expected_remote_cluster_incarnation_id", "replication_protocol", "ancestor_repl_protocol", "checkpoint", "snap_tree_root_node_floor", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "ancestor_replication_id", "tx_viewbox_id", "rx_viewbox_brick_size", "compression_enabled", "session_encryption_key", "rx_megafile_supported", "replication_view_metadata", "application_name", "tmp_dir_name", "estimated_logical_bytes_to_transfer", "estimated_changed_entities", "synced_files_logical_size_sum", "replicate_special_files", "enable_dir_sync_verification", "divergence_searching_and_fixing_replication", "application_job_id", "application_job_run_id", "application_job_name", "application_entity_name")
    EXPECTED_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REMOTE_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPL_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ROOT_NODE_FLOOR_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    RX_VIEWBOX_BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    RX_MEGAFILE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SYNCED_FILES_LOGICAL_SIZE_SUM_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_SPECIAL_FILES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DIR_SYNC_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DIVERGENCE_SEARCHING_AND_FIXING_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    expected_slave_session_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    remote_cluster_name: str
    expected_remote_cluster_id: int
    expected_remote_cluster_incarnation_id: int
    replication_protocol: _master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol
    ancestor_repl_protocol: _master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol
    checkpoint: bytes
    snap_tree_root_node_floor: int
    pct_completed: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    ancestor_replication_id: _universal_id_pb2.UniversalIdProto
    tx_viewbox_id: int
    rx_viewbox_brick_size: int
    compression_enabled: bool
    session_encryption_key: bytes
    rx_megafile_supported: bool
    replication_view_metadata: _master_replication_state_pb2.ReplicationViewMetadataProto
    application_name: str
    tmp_dir_name: str
    estimated_logical_bytes_to_transfer: int
    estimated_changed_entities: int
    synced_files_logical_size_sum: int
    replicate_special_files: bool
    enable_dir_sync_verification: bool
    divergence_searching_and_fixing_replication: bool
    application_job_id: int
    application_job_run_id: int
    application_job_name: str
    application_entity_name: str
    def __init__(self, expected_slave_session_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., remote_cluster_name: _Optional[str] = ..., expected_remote_cluster_id: _Optional[int] = ..., expected_remote_cluster_incarnation_id: _Optional[int] = ..., replication_protocol: _Optional[_Union[_master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol, str]] = ..., ancestor_repl_protocol: _Optional[_Union[_master_replication_state_pb2.MasterReplicationStateProto.ReplicationProtocol, str]] = ..., checkpoint: _Optional[bytes] = ..., snap_tree_root_node_floor: _Optional[int] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., ancestor_replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., tx_viewbox_id: _Optional[int] = ..., rx_viewbox_brick_size: _Optional[int] = ..., compression_enabled: bool = ..., session_encryption_key: _Optional[bytes] = ..., rx_megafile_supported: bool = ..., replication_view_metadata: _Optional[_Union[_master_replication_state_pb2.ReplicationViewMetadataProto, _Mapping]] = ..., application_name: _Optional[str] = ..., tmp_dir_name: _Optional[str] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., estimated_changed_entities: _Optional[int] = ..., synced_files_logical_size_sum: _Optional[int] = ..., replicate_special_files: bool = ..., enable_dir_sync_verification: bool = ..., divergence_searching_and_fixing_replication: bool = ..., application_job_id: _Optional[int] = ..., application_job_run_id: _Optional[int] = ..., application_job_name: _Optional[str] = ..., application_entity_name: _Optional[str] = ...) -> None: ...

class ResumeViewReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelViewReplicationArg(_message.Message):
    __slots__ = ("expected_slave_session_id", "replication_id")
    EXPECTED_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    expected_slave_session_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    def __init__(self, expected_slave_session_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelViewReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseViewReplicationArg(_message.Message):
    __slots__ = ("expected_slave_session_id", "replication_id")
    EXPECTED_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    expected_slave_session_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    def __init__(self, expected_slave_session_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class PauseViewReplicationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ViewReplicationProgressArg(_message.Message):
    __slots__ = ("replication_id", "slave_session_id", "pct_completed", "logical_bytes_transferred", "physical_bytes_transferred", "view_logical_size", "error", "checkpoint", "slave_transmit_rid_load", "slave_receive_rid_load", "logical_timestamp", "metadata_actions_completed", "total_metadata_actions", "load_info", "estimated_logical_bytes_to_transfer", "estimated_changed_entities", "synced_files_logical_size_sum", "logical_bytes_transferred_object_ns", "metadata_actions_completed_object_ns", "dir_sync_progress_detected", "replication_stats")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PCT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TRANSMIT_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    SLAVE_RECEIVE_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_METADATA_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    LOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SYNCED_FILES_LOGICAL_SIZE_SUM_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_PROGRESS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STATS_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    slave_session_id: int
    pct_completed: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    view_logical_size: int
    error: _error_pb2.ErrorProto
    checkpoint: bytes
    slave_transmit_rid_load: int
    slave_receive_rid_load: int
    logical_timestamp: int
    metadata_actions_completed: int
    total_metadata_actions: int
    load_info: _load_info_pb2.LoadInfo
    estimated_logical_bytes_to_transfer: int
    estimated_changed_entities: int
    synced_files_logical_size_sum: int
    logical_bytes_transferred_object_ns: int
    metadata_actions_completed_object_ns: int
    dir_sync_progress_detected: bool
    replication_stats: _master_replication_state_pb2.ReplicationStatistics
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., slave_session_id: _Optional[int] = ..., pct_completed: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., view_logical_size: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., checkpoint: _Optional[bytes] = ..., slave_transmit_rid_load: _Optional[int] = ..., slave_receive_rid_load: _Optional[int] = ..., logical_timestamp: _Optional[int] = ..., metadata_actions_completed: _Optional[int] = ..., total_metadata_actions: _Optional[int] = ..., load_info: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., estimated_changed_entities: _Optional[int] = ..., synced_files_logical_size_sum: _Optional[int] = ..., logical_bytes_transferred_object_ns: _Optional[int] = ..., metadata_actions_completed_object_ns: _Optional[int] = ..., dir_sync_progress_detected: bool = ..., replication_stats: _Optional[_Union[_master_replication_state_pb2.ReplicationStatistics, _Mapping]] = ...) -> None: ...

class ViewReplicationProgressResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReportLoadArg(_message.Message):
    __slots__ = ("slave_session_id", "slave_transmit_rid_load", "slave_receive_rid_load", "load_info", "fetch_load_map")
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_TRANSMIT_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    SLAVE_RECEIVE_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    LOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_LOAD_MAP_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    slave_transmit_rid_load: int
    slave_receive_rid_load: int
    load_info: _load_info_pb2.LoadInfo
    fetch_load_map: bool
    def __init__(self, slave_session_id: _Optional[int] = ..., slave_transmit_rid_load: _Optional[int] = ..., slave_receive_rid_load: _Optional[int] = ..., load_info: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ..., fetch_load_map: bool = ...) -> None: ...

class ReportLoadResult(_message.Message):
    __slots__ = ("load_map",)
    class LoadMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _load_info_pb2.LoadInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ...) -> None: ...
    LOAD_MAP_FIELD_NUMBER: _ClassVar[int]
    load_map: _containers.MessageMap[int, _load_info_pb2.LoadInfo]
    def __init__(self, load_map: _Optional[_Mapping[int, _load_info_pb2.LoadInfo]] = ...) -> None: ...

class FetchRelatedArg(_message.Message):
    __slots__ = ("replication_id",)
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class FetchRelatedResult(_message.Message):
    __slots__ = ("replication_id_vec",)
    REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class GetAllowedBandwidthArg(_message.Message):
    __slots__ = ("replication_id", "slave_session_id", "remote_cluster_name", "transmitter_id")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSMITTER_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    slave_session_id: int
    remote_cluster_name: str
    transmitter_id: str
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., slave_session_id: _Optional[int] = ..., remote_cluster_name: _Optional[str] = ..., transmitter_id: _Optional[str] = ...) -> None: ...

class GetAllowedBandwidthResult(_message.Message):
    __slots__ = ("rate_limit_bytes_per_sec",)
    RATE_LIMIT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    rate_limit_bytes_per_sec: int
    def __init__(self, rate_limit_bytes_per_sec: _Optional[int] = ...) -> None: ...

class PickSlaveArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "transmit_work", "num_slaves")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSMIT_WORK_FIELD_NUMBER: _ClassVar[int]
    NUM_SLAVES_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    transmit_work: bool
    num_slaves: int
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., transmit_work: bool = ..., num_slaves: _Optional[int] = ...) -> None: ...

class TcpEndpt(_message.Message):
    __slots__ = ("ip", "port")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class PickSlaveResult(_message.Message):
    __slots__ = ("slave_endpt_vec", "slave_ip")
    SLAVE_ENDPT_VEC_FIELD_NUMBER: _ClassVar[int]
    SLAVE_IP_FIELD_NUMBER: _ClassVar[int]
    slave_endpt_vec: _containers.RepeatedCompositeFieldContainer[TcpEndpt]
    slave_ip: str
    def __init__(self, slave_endpt_vec: _Optional[_Iterable[_Union[TcpEndpt, _Mapping]]] = ..., slave_ip: _Optional[str] = ...) -> None: ...

class FetchLoadArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "num_slaves")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_SLAVES_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    num_slaves: int
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., num_slaves: _Optional[int] = ...) -> None: ...

class FetchLoadResult(_message.Message):
    __slots__ = ("slave_info_vec",)
    class SlaveInfo(_message.Message):
        __slots__ = ("slave_endpt", "session_id", "load_info")
        SLAVE_ENDPT_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        LOAD_INFO_FIELD_NUMBER: _ClassVar[int]
        slave_endpt: TcpEndpt
        session_id: int
        load_info: _load_info_pb2.LoadInfo
        def __init__(self, slave_endpt: _Optional[_Union[TcpEndpt, _Mapping]] = ..., session_id: _Optional[int] = ..., load_info: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ...) -> None: ...
    SLAVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    slave_info_vec: _containers.RepeatedCompositeFieldContainer[FetchLoadResult.SlaveInfo]
    def __init__(self, slave_info_vec: _Optional[_Iterable[_Union[FetchLoadResult.SlaveInfo, _Mapping]]] = ...) -> None: ...

class RsyncSnapTreeDiffArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "expected_rx_slave_session_id", "replication_incarnation_id", "file_data_work_vec", "apply_entity_action_work_vec", "verify_dir_sync_work_vec", "custom_snap_tree_work_vec", "batch_unit_load", "find_missing_entities_work_vec")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLY_ENTITY_ACTION_WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    VERIFY_DIR_SYNC_WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SNAP_TREE_WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    BATCH_UNIT_LOAD_FIELD_NUMBER: _ClassVar[int]
    FIND_MISSING_ENTITIES_WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    expected_rx_slave_session_id: int
    replication_incarnation_id: int
    file_data_work_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncFileDataSyncWorkProto]
    apply_entity_action_work_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncApplyEntityActionWorkProto]
    verify_dir_sync_work_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncVerifyDirSyncWorkProto]
    custom_snap_tree_work_vec: _containers.RepeatedCompositeFieldContainer[_rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeWorkProto]
    batch_unit_load: float
    find_missing_entities_work_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncFindMissingEntitiesWorkProto]
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., expected_rx_slave_session_id: _Optional[int] = ..., replication_incarnation_id: _Optional[int] = ..., file_data_work_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncFileDataSyncWorkProto, _Mapping]]] = ..., apply_entity_action_work_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncApplyEntityActionWorkProto, _Mapping]]] = ..., verify_dir_sync_work_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncVerifyDirSyncWorkProto, _Mapping]]] = ..., custom_snap_tree_work_vec: _Optional[_Iterable[_Union[_rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeWorkProto, _Mapping]]] = ..., batch_unit_load: _Optional[float] = ..., find_missing_entities_work_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncFindMissingEntitiesWorkProto, _Mapping]]] = ...) -> None: ...

class RsyncSnapTreeDiffResult(_message.Message):
    __slots__ = ("file_sync_result_vec", "apply_entity_action_error_vec", "rx_slave_load", "rpc_processing_time_usecs", "verify_dir_sync_result_vec", "custom_snap_tree_work_result_vec", "find_missing_entities_result_vec")
    class FileSyncResult(_message.Message):
        __slots__ = ("error", "missing_ranges_proto")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        MISSING_RANGES_PROTO_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        missing_ranges_proto: _rsync_inode_sync_work_pb2.RsyncFileDataMissingRangesProto
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., missing_ranges_proto: _Optional[_Union[_rsync_inode_sync_work_pb2.RsyncFileDataMissingRangesProto, _Mapping]] = ...) -> None: ...
    FILE_SYNC_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLY_ENTITY_ACTION_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    RX_SLAVE_LOAD_FIELD_NUMBER: _ClassVar[int]
    RPC_PROCESSING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_DIR_SYNC_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SNAP_TREE_WORK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    FIND_MISSING_ENTITIES_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    file_sync_result_vec: _containers.RepeatedCompositeFieldContainer[RsyncSnapTreeDiffResult.FileSyncResult]
    apply_entity_action_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    rx_slave_load: _load_info_pb2.LoadInfo
    rpc_processing_time_usecs: int
    verify_dir_sync_result_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncVerifyDirSyncResultProto]
    custom_snap_tree_work_result_vec: _containers.RepeatedCompositeFieldContainer[_rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeResultProto]
    find_missing_entities_result_vec: _containers.RepeatedCompositeFieldContainer[_rsync_inode_sync_work_pb2.RsyncFindMissingEntitiesWorkResult]
    def __init__(self, file_sync_result_vec: _Optional[_Iterable[_Union[RsyncSnapTreeDiffResult.FileSyncResult, _Mapping]]] = ..., apply_entity_action_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., rx_slave_load: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ..., rpc_processing_time_usecs: _Optional[int] = ..., verify_dir_sync_result_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncVerifyDirSyncResultProto, _Mapping]]] = ..., custom_snap_tree_work_result_vec: _Optional[_Iterable[_Union[_rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeResultProto, _Mapping]]] = ..., find_missing_entities_result_vec: _Optional[_Iterable[_Union[_rsync_inode_sync_work_pb2.RsyncFindMissingEntitiesWorkResult, _Mapping]]] = ...) -> None: ...

class RsyncPigeonDedupArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "tx_slave_session_id", "replication_incarnation_id", "match_slice_vec", "write_slice_vec", "slice_data_length_vec", "relative_entity_path_vec", "inode_metadata_vec", "encrypted_inode_metadata", "enc_inode_metadata_length_vec")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_SLICE_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_SLICE_VEC_FIELD_NUMBER: _ClassVar[int]
    SLICE_DATA_LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ENTITY_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    INODE_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENC_INODE_METADATA_LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    tx_slave_session_id: int
    replication_incarnation_id: int
    match_slice_vec: _containers.RepeatedCompositeFieldContainer[_rsync_pigeon_pb2.Slice]
    write_slice_vec: _containers.RepeatedCompositeFieldContainer[_rsync_pigeon_pb2.Slice]
    slice_data_length_vec: _containers.RepeatedScalarFieldContainer[int]
    relative_entity_path_vec: _containers.RepeatedScalarFieldContainer[bytes]
    inode_metadata_vec: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.InodeMetadataProto]
    encrypted_inode_metadata: bytes
    enc_inode_metadata_length_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., tx_slave_session_id: _Optional[int] = ..., replication_incarnation_id: _Optional[int] = ..., match_slice_vec: _Optional[_Iterable[_Union[_rsync_pigeon_pb2.Slice, _Mapping]]] = ..., write_slice_vec: _Optional[_Iterable[_Union[_rsync_pigeon_pb2.Slice, _Mapping]]] = ..., slice_data_length_vec: _Optional[_Iterable[int]] = ..., relative_entity_path_vec: _Optional[_Iterable[bytes]] = ..., inode_metadata_vec: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]]] = ..., encrypted_inode_metadata: _Optional[bytes] = ..., enc_inode_metadata_length_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class RsyncPigeonDedupResult(_message.Message):
    __slots__ = ("match_slice_result_vec", "write_slice_error_vec", "set_attr_error_vec", "rpc_processing_time_usecs")
    class MatchResult(_message.Message):
        __slots__ = ("error", "missing_range_offset_vec", "missing_range_length_vec")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        MISSING_RANGE_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        MISSING_RANGE_LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        missing_range_offset_vec: _containers.RepeatedScalarFieldContainer[int]
        missing_range_length_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., missing_range_offset_vec: _Optional[_Iterable[int]] = ..., missing_range_length_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    MATCH_SLICE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_SLICE_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    SET_ATTR_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    RPC_PROCESSING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    match_slice_result_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonDedupResult.MatchResult]
    write_slice_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    set_attr_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    rpc_processing_time_usecs: int
    def __init__(self, match_slice_result_vec: _Optional[_Iterable[_Union[RsyncPigeonDedupResult.MatchResult, _Mapping]]] = ..., write_slice_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., set_attr_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., rpc_processing_time_usecs: _Optional[int] = ...) -> None: ...

class RsyncPigeonMetadataArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "tx_slave_session_id", "replication_incarnation_id", "entity_info_vec")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    tx_slave_session_id: int
    replication_incarnation_id: int
    entity_info_vec: _containers.RepeatedCompositeFieldContainer[_rsync_pigeon_pb2.ViewListing.EntityInfo]
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., tx_slave_session_id: _Optional[int] = ..., replication_incarnation_id: _Optional[int] = ..., entity_info_vec: _Optional[_Iterable[_Union[_rsync_pigeon_pb2.ViewListing.EntityInfo, _Mapping]]] = ...) -> None: ...

class RsyncPigeonMetadataResult(_message.Message):
    __slots__ = ("entity_error_vec",)
    ENTITY_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, entity_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class MetadataMasterBarrierArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "replication_incarnation_id", "is_forwarded")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_incarnation_id: int
    is_forwarded: bool
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_incarnation_id: _Optional[int] = ..., is_forwarded: bool = ...) -> None: ...

class MetadataMasterBarrierResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MetadataSlaveBarrierArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "replication_incarnation_id")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_incarnation_id: int
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_incarnation_id: _Optional[int] = ...) -> None: ...

class MetadataSlaveBarrierResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RsyncForwardBatchSyncTxOpArg(_message.Message):
    __slots__ = ("rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "replication_incarnation_id", "batch_id", "sender_session_id", "expected_receiver_session_id", "src_new_view_id", "src_old_view_id", "src_new_view_tree_id_floor", "compression_enabled", "session_encryption_key", "case_insensitive_entity_names", "namespace_root_name", "tmp_dir_name", "inode_info_vec", "src_old_view_root_inode_id", "root_namespace_has_s3_intents", "enable_dir_sync_verification", "custom_snap_tree_work", "check_ancestor_dir_divergence_and_fix")
    class InodeInfo(_message.Message):
        __slots__ = ("eh", "is_dir", "path", "inode_metadata", "rsync_inode_map_value_scribe_version", "rsync_inode_map_value")
        EH_FIELD_NUMBER: _ClassVar[int]
        IS_DIR_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
        RSYNC_INODE_MAP_VALUE_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        RSYNC_INODE_MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        is_dir: bool
        path: bytes
        inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
        rsync_inode_map_value_scribe_version: int
        rsync_inode_map_value: _rsync_snap_tree_diff_pb2.RsyncInodeMapValueProto
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_dir: bool = ..., path: _Optional[bytes] = ..., inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., rsync_inode_map_value_scribe_version: _Optional[int] = ..., rsync_inode_map_value: _Optional[_Union[_rsync_snap_tree_diff_pb2.RsyncInodeMapValueProto, _Mapping]] = ...) -> None: ...
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RECEIVER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_NEW_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_OLD_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_NEW_VIEW_TREE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    TMP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SRC_OLD_VIEW_ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAMESPACE_HAS_S3_INTENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DIR_SYNC_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SNAP_TREE_WORK_FIELD_NUMBER: _ClassVar[int]
    CHECK_ANCESTOR_DIR_DIVERGENCE_AND_FIX_FIELD_NUMBER: _ClassVar[int]
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_incarnation_id: int
    batch_id: int
    sender_session_id: int
    expected_receiver_session_id: int
    src_new_view_id: int
    src_old_view_id: int
    src_new_view_tree_id_floor: int
    compression_enabled: bool
    session_encryption_key: bytes
    case_insensitive_entity_names: bool
    namespace_root_name: str
    tmp_dir_name: str
    inode_info_vec: _containers.RepeatedCompositeFieldContainer[RsyncForwardBatchSyncTxOpArg.InodeInfo]
    src_old_view_root_inode_id: int
    root_namespace_has_s3_intents: bool
    enable_dir_sync_verification: bool
    custom_snap_tree_work: _rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeWorkProto
    check_ancestor_dir_divergence_and_fix: bool
    def __init__(self, rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_incarnation_id: _Optional[int] = ..., batch_id: _Optional[int] = ..., sender_session_id: _Optional[int] = ..., expected_receiver_session_id: _Optional[int] = ..., src_new_view_id: _Optional[int] = ..., src_old_view_id: _Optional[int] = ..., src_new_view_tree_id_floor: _Optional[int] = ..., compression_enabled: bool = ..., session_encryption_key: _Optional[bytes] = ..., case_insensitive_entity_names: bool = ..., namespace_root_name: _Optional[str] = ..., tmp_dir_name: _Optional[str] = ..., inode_info_vec: _Optional[_Iterable[_Union[RsyncForwardBatchSyncTxOpArg.InodeInfo, _Mapping]]] = ..., src_old_view_root_inode_id: _Optional[int] = ..., root_namespace_has_s3_intents: bool = ..., enable_dir_sync_verification: bool = ..., custom_snap_tree_work: _Optional[_Union[_rsync_custom_snap_tree_work_pb2.RsyncCustomSnapTreeWorkProto, _Mapping]] = ..., check_ancestor_dir_divergence_and_fix: bool = ...) -> None: ...

class RsyncForwardBatchSyncTxOpResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RsyncCancelBatchSyncTxOpArg(_message.Message):
    __slots__ = ("replication_id", "replication_incarnation_id", "batch_id", "sender_session_id", "expected_receiver_session_id", "is_pause_request")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RECEIVER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_incarnation_id: int
    batch_id: int
    sender_session_id: int
    expected_receiver_session_id: int
    is_pause_request: bool
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_incarnation_id: _Optional[int] = ..., batch_id: _Optional[int] = ..., sender_session_id: _Optional[int] = ..., expected_receiver_session_id: _Optional[int] = ..., is_pause_request: bool = ...) -> None: ...

class RsyncCancelBatchSyncTxOpResult(_message.Message):
    __slots__ = ("wait_for_op_completion_report",)
    WAIT_FOR_OP_COMPLETION_REPORT_FIELD_NUMBER: _ClassVar[int]
    wait_for_op_completion_report: bool
    def __init__(self, wait_for_op_completion_report: bool = ...) -> None: ...

class RsyncReportBatchProgressArg(_message.Message):
    __slots__ = ("replication_id", "replication_incarnation_id", "batch_id", "sender_session_id", "expected_receiver_session_id", "logical_bytes_transferred", "physical_bytes_transferred", "metadata_actions_completed", "morphed_physical_bytes_transferred", "dir_sync_progress_detected", "completed_error", "load_info", "num_entries_added", "num_entries_removed", "err_logical_bytes_transferred", "err_physical_bytes_transferred", "dir_sync_added_children_eid_vec", "changed_files_logical_size_bytes_vec", "file_sync_tx_op_run_times_usecs_vec", "dir_sync_tx_op_run_times_usecs_vec", "dir_sync_tx_op_verify_times_usecs_vec", "dir_sync_tx_op_num_dir_children_vec", "sync_completed_eid_vec", "new_files_synced_eid_vec")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RECEIVER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_PROGRESS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_ERROR_FIELD_NUMBER: _ClassVar[int]
    LOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    ERR_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    ERR_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_ADDED_CHILDREN_EID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FILES_LOGICAL_SIZE_BYTES_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_TX_OP_RUN_TIMES_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_RUN_TIMES_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_VERIFY_TIMES_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_TX_OP_NUM_DIR_CHILDREN_VEC_FIELD_NUMBER: _ClassVar[int]
    SYNC_COMPLETED_EID_VEC_FIELD_NUMBER: _ClassVar[int]
    NEW_FILES_SYNCED_EID_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_incarnation_id: int
    batch_id: int
    sender_session_id: int
    expected_receiver_session_id: int
    logical_bytes_transferred: int
    physical_bytes_transferred: int
    metadata_actions_completed: int
    morphed_physical_bytes_transferred: int
    dir_sync_progress_detected: bool
    completed_error: _error_pb2.ErrorProto
    load_info: _load_info_pb2.LoadInfo
    num_entries_added: int
    num_entries_removed: int
    err_logical_bytes_transferred: int
    err_physical_bytes_transferred: int
    dir_sync_added_children_eid_vec: _containers.RepeatedScalarFieldContainer[int]
    changed_files_logical_size_bytes_vec: _containers.RepeatedScalarFieldContainer[int]
    file_sync_tx_op_run_times_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    dir_sync_tx_op_run_times_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    dir_sync_tx_op_verify_times_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    dir_sync_tx_op_num_dir_children_vec: _containers.RepeatedScalarFieldContainer[int]
    sync_completed_eid_vec: _containers.RepeatedScalarFieldContainer[int]
    new_files_synced_eid_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_incarnation_id: _Optional[int] = ..., batch_id: _Optional[int] = ..., sender_session_id: _Optional[int] = ..., expected_receiver_session_id: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., metadata_actions_completed: _Optional[int] = ..., morphed_physical_bytes_transferred: _Optional[int] = ..., dir_sync_progress_detected: bool = ..., completed_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., load_info: _Optional[_Union[_load_info_pb2.LoadInfo, _Mapping]] = ..., num_entries_added: _Optional[int] = ..., num_entries_removed: _Optional[int] = ..., err_logical_bytes_transferred: _Optional[int] = ..., err_physical_bytes_transferred: _Optional[int] = ..., dir_sync_added_children_eid_vec: _Optional[_Iterable[int]] = ..., changed_files_logical_size_bytes_vec: _Optional[_Iterable[int]] = ..., file_sync_tx_op_run_times_usecs_vec: _Optional[_Iterable[int]] = ..., dir_sync_tx_op_run_times_usecs_vec: _Optional[_Iterable[int]] = ..., dir_sync_tx_op_verify_times_usecs_vec: _Optional[_Iterable[int]] = ..., dir_sync_tx_op_num_dir_children_vec: _Optional[_Iterable[int]] = ..., sync_completed_eid_vec: _Optional[_Iterable[int]] = ..., new_files_synced_eid_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class RsyncReportBatchProgressResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingRemoteClusterArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "progress_report_vec")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_REPORT_VEC_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    progress_report_vec: _containers.RepeatedCompositeFieldContainer[ProgressReport]
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., progress_report_vec: _Optional[_Iterable[_Union[ProgressReport, _Mapping]]] = ...) -> None: ...

class PingRemoteClusterResult(_message.Message):
    __slots__ = ("encrypt_handshake_supported",)
    ENCRYPT_HANDSHAKE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    encrypt_handshake_supported: bool
    def __init__(self, encrypt_handshake_supported: bool = ...) -> None: ...

class EncryptedHandshakeArg(_message.Message):
    __slots__ = ("is_forwarded", "tx_cluster_id", "tx_cluster_incarnation_id", "rx_cluster_id", "rx_cluster_incarnation_id", "replication_id", "encrypted_start_arg_size", "start_arg_checksum", "opaque_metadata_checksum")
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_START_ARG_SIZE_FIELD_NUMBER: _ClassVar[int]
    START_ARG_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_METADATA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    is_forwarded: bool
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    rx_cluster_id: int
    rx_cluster_incarnation_id: int
    replication_id: _universal_id_pb2.UniversalIdProto
    encrypted_start_arg_size: int
    start_arg_checksum: int
    opaque_metadata_checksum: int
    def __init__(self, is_forwarded: bool = ..., tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., rx_cluster_id: _Optional[int] = ..., rx_cluster_incarnation_id: _Optional[int] = ..., replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., encrypted_start_arg_size: _Optional[int] = ..., start_arg_checksum: _Optional[int] = ..., opaque_metadata_checksum: _Optional[int] = ...) -> None: ...
