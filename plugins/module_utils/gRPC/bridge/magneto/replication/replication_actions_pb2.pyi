from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.master.base import master_pb2 as _master_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleReplicationArg(_message.Message):
    __slots__ = ("replication_id", "remote_cluster_id", "remote_cluster_name", "internal_tx_view_expiry_secs_hint", "ancestor_replication_id_hint", "metadata", "disable_rx_megafile", "is_out_of_band", "is_failover_replication", "enable_nfs_smb_permissions", "trigger_full_replication")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TX_VIEW_EXPIRY_SECS_HINT_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_REPLICATION_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RX_MEGAFILE_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NFS_SMB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FULL_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    remote_cluster_id: int
    remote_cluster_name: str
    internal_tx_view_expiry_secs_hint: int
    ancestor_replication_id_hint: _universal_id_pb2.UniversalIdProto
    metadata: _master_pb2.BackupRunReplicationMDProto
    disable_rx_megafile: bool
    is_out_of_band: bool
    is_failover_replication: bool
    enable_nfs_smb_permissions: bool
    trigger_full_replication: bool
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., remote_cluster_id: _Optional[int] = ..., remote_cluster_name: _Optional[str] = ..., internal_tx_view_expiry_secs_hint: _Optional[int] = ..., ancestor_replication_id_hint: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., metadata: _Optional[_Union[_master_pb2.BackupRunReplicationMDProto, _Mapping]] = ..., disable_rx_megafile: bool = ..., is_out_of_band: bool = ..., is_failover_replication: bool = ..., enable_nfs_smb_permissions: bool = ..., trigger_full_replication: bool = ...) -> None: ...

class CancelReplicationArg(_message.Message):
    __slots__ = ("replication_id", "reason")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    reason: str
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class QueryReplicationsArg(_message.Message):
    __slots__ = ("replication_id_vec", "include_job_details")
    REPLICATION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    replication_id_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    include_job_details: bool
    def __init__(self, replication_id_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., include_job_details: bool = ...) -> None: ...

class QueryReplicationsResult(_message.Message):
    __slots__ = ("replication_info_vec",)
    class ReplicationInfo(_message.Message):
        __slots__ = ("replication_id", "base", "metadata")
        REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        replication_id: _universal_id_pb2.UniversalIdProto
        base: _master_pb2.ReplicationInfoBase
        metadata: _master_pb2.BackupRunReplicationMDProto
        def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., base: _Optional[_Union[_master_pb2.ReplicationInfoBase, _Mapping]] = ..., metadata: _Optional[_Union[_master_pb2.BackupRunReplicationMDProto, _Mapping]] = ...) -> None: ...
    REPLICATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_info_vec: _containers.RepeatedCompositeFieldContainer[QueryReplicationsResult.ReplicationInfo]
    def __init__(self, replication_info_vec: _Optional[_Iterable[_Union[QueryReplicationsResult.ReplicationInfo, _Mapping]]] = ...) -> None: ...

class ExpireReplicationViewsArg(_message.Message):
    __slots__ = ("task_id", "job_views")
    class JobViews(_message.Message):
        __slots__ = ("job_uid", "view_names")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAMES_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        view_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_names: _Optional[_Iterable[str]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_VIEWS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    job_views: _containers.RepeatedCompositeFieldContainer[ExpireReplicationViewsArg.JobViews]
    def __init__(self, task_id: _Optional[int] = ..., job_views: _Optional[_Iterable[_Union[ExpireReplicationViewsArg.JobViews, _Mapping]]] = ...) -> None: ...

class ReplicationActionArg(_message.Message):
    __slots__ = ("schedule_replication_arg", "cancel_replication_arg", "query_replications_arg", "expire_replication_views_arg")
    REPLICATION_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    replication_action_arg: _descriptor.FieldDescriptor
    SCHEDULE_REPLICATION_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REPLICATION_ARG_FIELD_NUMBER: _ClassVar[int]
    QUERY_REPLICATIONS_ARG_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_REPLICATION_VIEWS_ARG_FIELD_NUMBER: _ClassVar[int]
    schedule_replication_arg: ScheduleReplicationArg
    cancel_replication_arg: CancelReplicationArg
    query_replications_arg: QueryReplicationsArg
    expire_replication_views_arg: ExpireReplicationViewsArg
    def __init__(self, schedule_replication_arg: _Optional[_Union[ScheduleReplicationArg, _Mapping]] = ..., cancel_replication_arg: _Optional[_Union[CancelReplicationArg, _Mapping]] = ..., query_replications_arg: _Optional[_Union[QueryReplicationsArg, _Mapping]] = ..., expire_replication_views_arg: _Optional[_Union[ExpireReplicationViewsArg, _Mapping]] = ...) -> None: ...

class ReplicationActionResult(_message.Message):
    __slots__ = ("query_replications_result",)
    REPLICATION_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    replication_action_result: _descriptor.FieldDescriptor
    QUERY_REPLICATIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    query_replications_result: QueryReplicationsResult
    def __init__(self, query_replications_result: _Optional[_Union[QueryReplicationsResult, _Mapping]] = ...) -> None: ...
