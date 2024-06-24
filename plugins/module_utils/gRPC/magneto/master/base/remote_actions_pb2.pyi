from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.master.base import master_pb2 as _master_pb2
from magneto.master.base import master_cdp_pb2 as _master_cdp_pb2
from magneto.master.entity_provenance import entity_provenance_pb2 as _entity_provenance_pb2
from magneto.utils import capability_pb2 as _capability_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCapabilitiesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCapabilitiesResult(_message.Message):
    __slots__ = ("capability_proto",)
    CAPABILITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    capability_proto: _capability_pb2.CapabilityProto
    def __init__(self, capability_proto: _Optional[_Union[_capability_pb2.CapabilityProto, _Mapping]] = ...) -> None: ...

class StartReplicationTaskArg(_message.Message):
    __slots__ = ("replication_version", "job_description", "protection_policy", "task_uid", "run_base", "snapshot_expiry_usecs", "rx_view_box_id", "entity_permission_info_vec", "object_level_copy", "entity_provenance_edge_vec", "tx_capability_proto", "backup_run_state", "is_out_of_band_copy_task", "retention_policy", "app_entity_vec")
    REPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    RX_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_COPY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROVENANCE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    TX_CAPABILITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_COPY_TASK_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_version: int
    job_description: _magneto_pb2.BackupJobProto
    protection_policy: _policy_pb2.ProtectionPolicyProto
    task_uid: _universal_id_pb2.UniversalIdProto
    run_base: _master_pb2.BackupJobTaskStateBaseProto
    snapshot_expiry_usecs: int
    rx_view_box_id: int
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.EntityPermissionInfo]
    object_level_copy: bool
    entity_provenance_edge_vec: _containers.RepeatedCompositeFieldContainer[_entity_provenance_pb2.EntityProvenanceEdgeProto]
    tx_capability_proto: _capability_pb2.CapabilityProto
    backup_run_state: _master_pb2.BackupJobRunStateProto
    is_out_of_band_copy_task: bool
    retention_policy: _policy_pb2.RetentionPolicyProto
    app_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, replication_version: _Optional[int] = ..., job_description: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ..., protection_policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_base: _Optional[_Union[_master_pb2.BackupJobTaskStateBaseProto, _Mapping]] = ..., snapshot_expiry_usecs: _Optional[int] = ..., rx_view_box_id: _Optional[int] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[_permissions_pb2.EntityPermissionInfo, _Mapping]]] = ..., object_level_copy: bool = ..., entity_provenance_edge_vec: _Optional[_Iterable[_Union[_entity_provenance_pb2.EntityProvenanceEdgeProto, _Mapping]]] = ..., tx_capability_proto: _Optional[_Union[_capability_pb2.CapabilityProto, _Mapping]] = ..., backup_run_state: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., is_out_of_band_copy_task: bool = ..., retention_policy: _Optional[_Union[_policy_pb2.RetentionPolicyProto, _Mapping]] = ..., app_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class StartReplicationTaskResult(_message.Message):
    __slots__ = ("backup_run_state", "existing_expiry_time_usecs", "existing_data_lock_constraints", "display_sub_tasks_status_based_on_parent")
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXISTING_DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SUB_TASKS_STATUS_BASED_ON_PARENT_FIELD_NUMBER: _ClassVar[int]
    backup_run_state: _master_pb2.BackupJobRunStateProto
    existing_expiry_time_usecs: int
    existing_data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    display_sub_tasks_status_based_on_parent: bool
    def __init__(self, backup_run_state: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., existing_expiry_time_usecs: _Optional[int] = ..., existing_data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., display_sub_tasks_status_based_on_parent: bool = ...) -> None: ...

class EndReplicationTaskArg(_message.Message):
    __slots__ = ("task_uid", "backup_run_state", "error", "snapshot_expiry_usecs", "legal_hold_enabled", "data_lock_constraints", "initiated_by_dso_role")
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    INITIATED_BY_DSO_ROLE_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    backup_run_state: _master_pb2.BackupJobRunStateProto
    error: _error_pb2.ErrorProto
    snapshot_expiry_usecs: int
    legal_hold_enabled: bool
    data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    initiated_by_dso_role: bool
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_run_state: _Optional[_Union[_master_pb2.BackupJobRunStateProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_expiry_usecs: _Optional[int] = ..., legal_hold_enabled: bool = ..., data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., initiated_by_dso_role: bool = ...) -> None: ...

class CdpEntityRequestArg(_message.Message):
    __slots__ = ("entity_id", "get_cdp_entity_state_arg", "update_cdp_entity_state_arg")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    GET_CDP_ENTITY_STATE_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CDP_ENTITY_STATE_ARG_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    get_cdp_entity_state_arg: GetCdpEntityStateArg
    update_cdp_entity_state_arg: UpdateCdpEntityStateArg
    def __init__(self, entity_id: _Optional[int] = ..., get_cdp_entity_state_arg: _Optional[_Union[GetCdpEntityStateArg, _Mapping]] = ..., update_cdp_entity_state_arg: _Optional[_Union[UpdateCdpEntityStateArg, _Mapping]] = ...) -> None: ...

class CdpEntityRequestResult(_message.Message):
    __slots__ = ("get_cdp_entity_state_result",)
    GET_CDP_ENTITY_STATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    get_cdp_entity_state_result: GetCdpEntityStateResult
    def __init__(self, get_cdp_entity_state_result: _Optional[_Union[GetCdpEntityStateResult, _Mapping]] = ...) -> None: ...

class UpdateCdpEntityStateArg(_message.Message):
    __slots__ = ("enable_cdp",)
    ENABLE_CDP_FIELD_NUMBER: _ClassVar[int]
    enable_cdp: bool
    def __init__(self, enable_cdp: bool = ...) -> None: ...

class GetCdpEntityStateArg(_message.Message):
    __slots__ = ("include_entity_cdp_state_proto", "include_restore_info")
    INCLUDE_ENTITY_CDP_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    include_entity_cdp_state_proto: bool
    include_restore_info: bool
    def __init__(self, include_entity_cdp_state_proto: bool = ..., include_restore_info: bool = ...) -> None: ...

class GetCdpEntityStateResult(_message.Message):
    __slots__ = ("entity_cdp_state_proto", "entity_restore_info")
    class EntityRestoreInfo(_message.Message):
        __slots__ = ("is_waiting_for_snapshot", "hole_info")
        IS_WAITING_FOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        HOLE_INFO_FIELD_NUMBER: _ClassVar[int]
        is_waiting_for_snapshot: bool
        hole_info: _master_cdp_pb2.CDPHoleInfo
        def __init__(self, is_waiting_for_snapshot: bool = ..., hole_info: _Optional[_Union[_master_cdp_pb2.CDPHoleInfo, _Mapping]] = ...) -> None: ...
    ENTITY_CDP_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_cdp_state_proto: _master_cdp_pb2.EntityCdpStateProto
    entity_restore_info: GetCdpEntityStateResult.EntityRestoreInfo
    def __init__(self, entity_cdp_state_proto: _Optional[_Union[_master_cdp_pb2.EntityCdpStateProto, _Mapping]] = ..., entity_restore_info: _Optional[_Union[GetCdpEntityStateResult.EntityRestoreInfo, _Mapping]] = ...) -> None: ...

class RemoteReplicationActions(_message.Message):
    __slots__ = ("rx_cluster_instance_id", "get_capabilities_arg", "start_replication_arg", "end_replication_arg", "cdp_entity_request_arg")
    RX_CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    GET_CAPABILITIES_ARG_FIELD_NUMBER: _ClassVar[int]
    START_REPLICATION_ARG_FIELD_NUMBER: _ClassVar[int]
    END_REPLICATION_ARG_FIELD_NUMBER: _ClassVar[int]
    CDP_ENTITY_REQUEST_ARG_FIELD_NUMBER: _ClassVar[int]
    rx_cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    get_capabilities_arg: GetCapabilitiesArg
    start_replication_arg: StartReplicationTaskArg
    end_replication_arg: EndReplicationTaskArg
    cdp_entity_request_arg: CdpEntityRequestArg
    def __init__(self, rx_cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., get_capabilities_arg: _Optional[_Union[GetCapabilitiesArg, _Mapping]] = ..., start_replication_arg: _Optional[_Union[StartReplicationTaskArg, _Mapping]] = ..., end_replication_arg: _Optional[_Union[EndReplicationTaskArg, _Mapping]] = ..., cdp_entity_request_arg: _Optional[_Union[CdpEntityRequestArg, _Mapping]] = ...) -> None: ...

class RemoteReplicationActionsResult(_message.Message):
    __slots__ = ("get_capabilities_result", "start_replication_result", "cdp_entity_request_result", "capability_proto")
    GET_CAPABILITIES_RESULT_FIELD_NUMBER: _ClassVar[int]
    START_REPLICATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CDP_ENTITY_REQUEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    get_capabilities_result: GetCapabilitiesResult
    start_replication_result: StartReplicationTaskResult
    cdp_entity_request_result: CdpEntityRequestResult
    capability_proto: _capability_pb2.CapabilityProto
    def __init__(self, get_capabilities_result: _Optional[_Union[GetCapabilitiesResult, _Mapping]] = ..., start_replication_result: _Optional[_Union[StartReplicationTaskResult, _Mapping]] = ..., cdp_entity_request_result: _Optional[_Union[CdpEntityRequestResult, _Mapping]] = ..., capability_proto: _Optional[_Union[_capability_pb2.CapabilityProto, _Mapping]] = ...) -> None: ...
