from apollo.mr.algorithms.icebox import grpc_service_args_pb2 as _grpc_service_args_pb2
from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.apollo import actions_v2_pb2 as _actions_v2_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.icebox.master.stub import rpc_service_pb2 as _rpc_service_pb2
from apollo.mr.algorithms.utils import universal_id_set_pb2 as _universal_id_set_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IceboxRestoreJobsContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "apollo_mr_enable_icebox_restore_jobs_algos", "in_use_restore_job_uids")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_ICEBOX_RESTORE_JOBS_ALGOS_FIELD_NUMBER: _ClassVar[int]
    IN_USE_RESTORE_JOB_UIDS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    apollo_mr_enable_icebox_restore_jobs_algos: bool
    in_use_restore_job_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., apollo_mr_enable_icebox_restore_jobs_algos: bool = ..., in_use_restore_job_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ...) -> None: ...

class IceboxArchiveJobsContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "apollo_mr_enable_icebox_archive_jobs_algos", "in_use_archive_uids", "in_use_unretired_ref_archive_uids", "non_ref_archive_uids", "retired_ref_archive_uids", "epoch_id_info_vec", "icebox_master_migrate_to_separate_process_ready")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_ICEBOX_ARCHIVE_JOBS_ALGOS_FIELD_NUMBER: _ClassVar[int]
    IN_USE_ARCHIVE_UIDS_FIELD_NUMBER: _ClassVar[int]
    IN_USE_UNRETIRED_REF_ARCHIVE_UIDS_FIELD_NUMBER: _ClassVar[int]
    NON_REF_ARCHIVE_UIDS_FIELD_NUMBER: _ClassVar[int]
    RETIRED_REF_ARCHIVE_UIDS_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_MASTER_MIGRATE_TO_SEPARATE_PROCESS_READY_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    apollo_mr_enable_icebox_archive_jobs_algos: bool
    in_use_archive_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    in_use_unretired_ref_archive_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    non_ref_archive_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    retired_ref_archive_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    epoch_id_info_vec: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.EpochIdInfo]
    icebox_master_migrate_to_separate_process_ready: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., apollo_mr_enable_icebox_archive_jobs_algos: bool = ..., in_use_archive_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., in_use_unretired_ref_archive_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., non_ref_archive_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., retired_ref_archive_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., epoch_id_info_vec: _Optional[_Iterable[_Union[_rpc_service_pb2.EpochIdInfo, _Mapping]]] = ..., icebox_master_migrate_to_separate_process_ready: bool = ...) -> None: ...

class IceboxArchiveRetirementInfoProto(_message.Message):
    __slots__ = ("is_reference_archive", "is_archive_retired", "num_chunk_expired", "num_chunk_alive", "num_chunk_with_op_in_progress", "num_chunk_without_access_timestamp")
    IS_REFERENCE_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVE_RETIRED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_ALIVE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_WITH_OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_WITHOUT_ACCESS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    is_reference_archive: bool
    is_archive_retired: bool
    num_chunk_expired: int
    num_chunk_alive: int
    num_chunk_with_op_in_progress: int
    num_chunk_without_access_timestamp: int
    def __init__(self, is_reference_archive: bool = ..., is_archive_retired: bool = ..., num_chunk_expired: _Optional[int] = ..., num_chunk_alive: _Optional[int] = ..., num_chunk_with_op_in_progress: _Optional[int] = ..., num_chunk_without_access_timestamp: _Optional[int] = ...) -> None: ...

class IceboxDirectArchiveContextDataProto(_message.Message):
    __slots__ = ("input_arg", "apollo_mr_enable_direct_archive_files_gc", "max_archives_per_shard", "expired_tree_uids", "live_tree_uids", "signal_icebox_action", "vault_id", "use_node_uid")
    INPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_DIRECT_ARCHIVE_FILES_GC_FIELD_NUMBER: _ClassVar[int]
    MAX_ARCHIVES_PER_SHARD_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_TREE_UIDS_FIELD_NUMBER: _ClassVar[int]
    LIVE_TREE_UIDS_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_ICEBOX_ACTION_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    USE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    input_arg: _grpc_service_args_pb2.ScheduleIceboxDirectArchivePipelineArg
    apollo_mr_enable_direct_archive_files_gc: bool
    max_archives_per_shard: int
    expired_tree_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    live_tree_uids: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
    signal_icebox_action: _actions_v2_pb2.IceboxDirectArchiveFilesGC
    vault_id: int
    use_node_uid: bool
    def __init__(self, input_arg: _Optional[_Union[_grpc_service_args_pb2.ScheduleIceboxDirectArchivePipelineArg, _Mapping]] = ..., apollo_mr_enable_direct_archive_files_gc: bool = ..., max_archives_per_shard: _Optional[int] = ..., expired_tree_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., live_tree_uids: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., signal_icebox_action: _Optional[_Union[_actions_v2_pb2.IceboxDirectArchiveFilesGC, _Mapping]] = ..., vault_id: _Optional[int] = ..., use_node_uid: bool = ...) -> None: ...

class IceboxDirectArchiveFilesGCKeyProto(_message.Message):
    __slots__ = ("node_uid", "node_ptr")
    NODE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    node_uid: _universal_id_pb2.UniversalIdProto
    node_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    def __init__(self, node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ...) -> None: ...

class IceboxDirectArchiveFilesGCValueProto(_message.Message):
    __slots__ = ("num_references", "inode_proto", "non_file_leaf_node", "root_node_uid_vec", "child_node_vec")
    NUM_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    INODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    NON_FILE_LEAF_NODE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    num_references: int
    inode_proto: _snap_fs_metadata_pb2.InodeMetadataProto
    non_file_leaf_node: bool
    root_node_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    child_node_vec: _containers.RepeatedCompositeFieldContainer[IceboxDirectArchiveFilesGCKeyProto]
    def __init__(self, num_references: _Optional[int] = ..., inode_proto: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., non_file_leaf_node: bool = ..., root_node_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., child_node_vec: _Optional[_Iterable[_Union[IceboxDirectArchiveFilesGCKeyProto, _Mapping]]] = ...) -> None: ...
