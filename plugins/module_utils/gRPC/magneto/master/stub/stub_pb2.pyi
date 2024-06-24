from bridge.base import error_pb2 as _error_pb2
from bridge.icebox.master.stub import rpc_service_pb2 as _rpc_service_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.base import gatekeeper_pb2 as _gatekeeper_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.master.base import master_pb2 as _master_pb2
from magneto.master.base import enums_pb2 as _enums_pb2_1
from magneto.master.base import remote_actions_pb2 as _remote_actions_pb2
from resource_manager.base import logical_timestamp_pb2 as _logical_timestamp_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kInProgress: _ClassVar[TaskStatus]
    kFinished: _ClassVar[TaskStatus]
    kError: _ClassVar[TaskStatus]
    kCancelled: _ClassVar[TaskStatus]
    kPaused: _ClassVar[TaskStatus]
kInProgress: TaskStatus
kFinished: TaskStatus
kError: TaskStatus
kCancelled: TaskStatus
kPaused: TaskStatus

class UpdateBackupTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "snapshot_info", "deleted_external_snapshot_vec", "uptier_task", "current_task_state_in_scribe_setting", "update_connection_params", "snapshot_delta")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETED_EXTERNAL_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TASK_STATE_IN_SCRIBE_SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELTA_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    snapshot_info: _magneto_pb2.SnapshotInfoProto
    deleted_external_snapshot_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.ExternalSnapshotInfo]
    uptier_task: bool
    current_task_state_in_scribe_setting: _enums_pb2_1.TaskStateInScribeSetting
    update_connection_params: _magneto_pb2.UpdateConnectionParams
    snapshot_delta: _magneto_pb2.SnapshotDeltaProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., deleted_external_snapshot_vec: _Optional[_Iterable[_Union[_magneto_pb2.ExternalSnapshotInfo, _Mapping]]] = ..., uptier_task: bool = ..., current_task_state_in_scribe_setting: _Optional[_Union[_enums_pb2_1.TaskStateInScribeSetting, str]] = ..., update_connection_params: _Optional[_Union[_magneto_pb2.UpdateConnectionParams, _Mapping]] = ..., snapshot_delta: _Optional[_Union[_magneto_pb2.SnapshotDeltaProto, _Mapping]] = ...) -> None: ...

class UpdateBackupTaskResult(_message.Message):
    __slots__ = ("available_connections",)
    Extensions: _python_message._ExtensionDict
    AVAILABLE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    available_connections: int
    def __init__(self, available_connections: _Optional[int] = ...) -> None: ...

class UpdateFetchStorageInfoTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "entities_storage_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_STORAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    entities_storage_info: _storage_pb2.EntitiesStorageInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities_storage_info: _Optional[_Union[_storage_pb2.EntitiesStorageInfoProto, _Mapping]] = ...) -> None: ...

class UpdateFetchStorageInfoTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateTakeGroupSnapshotTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "entities_group_snapshot_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    entities_group_snapshot_info: _storage_pb2.EntitiesGroupSnapshotInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., entities_group_snapshot_info: _Optional[_Union[_storage_pb2.EntitiesGroupSnapshotInfoProto, _Mapping]] = ...) -> None: ...

class UpdateTakeGroupSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateTeardownGroupSnapshotTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "teardown_task_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    teardown_task_info: _storage_pb2.TeardownGroupSnapshotInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., teardown_task_info: _Optional[_Union[_storage_pb2.TeardownGroupSnapshotInfoProto, _Mapping]] = ...) -> None: ...

class UpdateTeardownGroupSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateRestoreTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "task_uid", "slave_op_clock", "status", "error", "can_teardown", "restore_info", "restore_files_info", "mount_volumes_info", "recover_volumes_state", "cloud_deploy_info", "recover_virtual_disk_info", "uptier_task", "use_existing_agent", "update_connection_params")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CAN_TEARDOWN_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUMES_INFO_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VOLUMES_STATE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIRTUAL_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_AGENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    can_teardown: bool
    restore_info: _magneto_pb2.RestoreInfoProto
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    mount_volumes_info: _magneto_pb2.MountVolumesInfoProto
    recover_volumes_state: _master_pb2.RecoverVolumesTaskStateProto
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    recover_virtual_disk_info: _magneto_pb2.RecoverVirtualDiskInfoProto
    uptier_task: bool
    use_existing_agent: bool
    update_connection_params: _magneto_pb2.UpdateConnectionParams
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., can_teardown: bool = ..., restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ..., mount_volumes_info: _Optional[_Union[_magneto_pb2.MountVolumesInfoProto, _Mapping]] = ..., recover_volumes_state: _Optional[_Union[_master_pb2.RecoverVolumesTaskStateProto, _Mapping]] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., recover_virtual_disk_info: _Optional[_Union[_magneto_pb2.RecoverVirtualDiskInfoProto, _Mapping]] = ..., uptier_task: bool = ..., use_existing_agent: bool = ..., update_connection_params: _Optional[_Union[_magneto_pb2.UpdateConnectionParams, _Mapping]] = ...) -> None: ...

class UpdateRestoreTaskResult(_message.Message):
    __slots__ = ("available_connections",)
    AVAILABLE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    available_connections: int
    def __init__(self, available_connections: _Optional[int] = ...) -> None: ...

class UpdateDestroyCloneTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "destroy_clone_vm_task_info", "destroy_mount_volumes_task_info", "destroy_clone_app_task_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_VM_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_MOUNT_VOLUMES_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    destroy_clone_vm_task_info: _magneto_pb2.DestroyClonedVMTaskInfoProto
    destroy_mount_volumes_task_info: _magneto_pb2.DestroyMountVolumesTaskInfoProto
    destroy_clone_app_task_info: _magneto_pb2.DestroyCloneAppTaskInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., destroy_clone_vm_task_info: _Optional[_Union[_magneto_pb2.DestroyClonedVMTaskInfoProto, _Mapping]] = ..., destroy_mount_volumes_task_info: _Optional[_Union[_magneto_pb2.DestroyMountVolumesTaskInfoProto, _Mapping]] = ..., destroy_clone_app_task_info: _Optional[_Union[_magneto_pb2.DestroyCloneAppTaskInfoProto, _Mapping]] = ...) -> None: ...

class UpdateDestroyCloneTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateDeactivateJobEntitiesTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "status", "error", "deactivate_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    deactivate_info: _magneto_pb2.DeactivateJobEntitiesInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., deactivate_info: _Optional[_Union[_magneto_pb2.DeactivateJobEntitiesInfoProto, _Mapping]] = ...) -> None: ...

class UpdateDeactivateJobEntitiesTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBridgeTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "bridge_gandalf_session_id", "bridge_or_bridge_proxy_constituent_id", "error", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDeleteDirsUpdate: _ClassVar[UpdateBridgeTaskArg.Type]
        kExpireReplicationViewsUpdate: _ClassVar[UpdateBridgeTaskArg.Type]
    kDeleteDirsUpdate: UpdateBridgeTaskArg.Type
    kExpireReplicationViewsUpdate: UpdateBridgeTaskArg.Type
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_OR_BRIDGE_PROXY_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    bridge_gandalf_session_id: int
    bridge_or_bridge_proxy_constituent_id: int
    error: _error_pb2.ErrorProto
    type: UpdateBridgeTaskArg.Type
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., bridge_gandalf_session_id: _Optional[int] = ..., bridge_or_bridge_proxy_constituent_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., type: _Optional[_Union[UpdateBridgeTaskArg.Type, str]] = ...) -> None: ...

class UpdateBridgeTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentStateArg(_message.Message):
    __slots__ = ("api_version", "task_id", "agent_info_proto")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    agent_info_proto: _agent_pb2.AgentInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., agent_info_proto: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ...) -> None: ...

class UpdateAgentStateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateReplicationTaskArg(_message.Message):
    __slots__ = ("replication_id", "bridge_gandalf_session_id", "error", "is_final_schedule_request")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_SCHEDULE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    bridge_gandalf_session_id: int
    error: _error_pb2.ErrorProto
    is_final_schedule_request: bool
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., bridge_gandalf_session_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_final_schedule_request: bool = ...) -> None: ...

class NotifyViewTxCompletedArg(_message.Message):
    __slots__ = ("replication_id", "replication_info")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_info: _master_pb2.ReplicationInfoBase
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_info: _Optional[_Union[_master_pb2.ReplicationInfoBase, _Mapping]] = ...) -> None: ...

class NotifyViewRxCompletedArg(_message.Message):
    __slots__ = ("replication_id", "replication_info", "post_rx_error", "metadata", "replica_view_entity", "replica_view_logical_size")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    POST_RX_ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VIEW_ENTITY_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    replication_info: _master_pb2.ReplicationInfoBase
    post_rx_error: _error_pb2.ErrorProto
    metadata: _master_pb2.BackupRunReplicationMDProto
    replica_view_entity: _entity_pb2.EntityProto
    replica_view_logical_size: int
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_info: _Optional[_Union[_master_pb2.ReplicationInfoBase, _Mapping]] = ..., post_rx_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metadata: _Optional[_Union[_master_pb2.BackupRunReplicationMDProto, _Mapping]] = ..., replica_view_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., replica_view_logical_size: _Optional[int] = ...) -> None: ...

class QueryViewRxAllowedArg(_message.Message):
    __slots__ = ("replication_id", "metadata")
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    replication_id: _universal_id_pb2.UniversalIdProto
    metadata: _master_pb2.BackupRunReplicationMDProto
    def __init__(self, replication_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., metadata: _Optional[_Union[_master_pb2.BackupRunReplicationMDProto, _Mapping]] = ...) -> None: ...

class HandleReplicationCallbackArg(_message.Message):
    __slots__ = ("api_version", "update_replication_task_arg", "notify_view_tx_completed_arg", "notify_view_rx_completed_arg", "view_rx_allowed_arg")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_REPLICATION_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_VIEW_TX_COMPLETED_ARG_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_VIEW_RX_COMPLETED_ARG_FIELD_NUMBER: _ClassVar[int]
    VIEW_RX_ALLOWED_ARG_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    update_replication_task_arg: UpdateReplicationTaskArg
    notify_view_tx_completed_arg: NotifyViewTxCompletedArg
    notify_view_rx_completed_arg: NotifyViewRxCompletedArg
    view_rx_allowed_arg: QueryViewRxAllowedArg
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., update_replication_task_arg: _Optional[_Union[UpdateReplicationTaskArg, _Mapping]] = ..., notify_view_tx_completed_arg: _Optional[_Union[NotifyViewTxCompletedArg, _Mapping]] = ..., notify_view_rx_completed_arg: _Optional[_Union[NotifyViewRxCompletedArg, _Mapping]] = ..., view_rx_allowed_arg: _Optional[_Union[QueryViewRxAllowedArg, _Mapping]] = ...) -> None: ...

class HandleReplicationCallbackResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifyArchivalTaskCompletedArg(_message.Message):
    __slots__ = ("archive_state",)
    ARCHIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    archive_state: _rpc_service_pb2.ArchivalJobStateProto
    def __init__(self, archive_state: _Optional[_Union[_rpc_service_pb2.ArchivalJobStateProto, _Mapping]] = ...) -> None: ...

class NotifyArchivalRestoreTaskCompletedArg(_message.Message):
    __slots__ = ("restore_state", "relative_snapshot_dir_map", "migration_uid", "user_info")
    class RelativeSnapshotDirMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_STATE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_MAP_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_state: _rpc_service_pb2.RestoreJobStateProto
    relative_snapshot_dir_map: _containers.ScalarMap[str, str]
    migration_uid: str
    user_info: _permissions_pb2.UserInformation
    def __init__(self, restore_state: _Optional[_Union[_rpc_service_pb2.RestoreJobStateProto, _Mapping]] = ..., relative_snapshot_dir_map: _Optional[_Mapping[str, str]] = ..., migration_uid: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class RegisterBackupJobRunArg(_message.Message):
    __slots__ = ("job_run_metadata", "viewbox_id", "vault_id", "archival_job_state", "origin_cluster_name", "migration_uid")
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    viewbox_id: int
    vault_id: int
    archival_job_state: _rpc_service_pb2.ArchivalJobStateProto
    origin_cluster_name: str
    migration_uid: str
    def __init__(self, job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., archival_job_state: _Optional[_Union[_rpc_service_pb2.ArchivalJobStateProto, _Mapping]] = ..., origin_cluster_name: _Optional[str] = ..., migration_uid: _Optional[str] = ...) -> None: ...

class RegisterBackupJobRunResult(_message.Message):
    __slots__ = ("entity_id_map", "local_job_uid", "registered_source", "error")
    class EntityIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_id_map: _containers.ScalarMap[int, int]
    local_job_uid: _universal_id_pb2.UniversalIdProto
    registered_source: _entity_pb2.EntityProto
    error: _error_pb2_1.ErrorProto
    def __init__(self, entity_id_map: _Optional[_Mapping[int, int]] = ..., local_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class RegisterArchivedBackupRunArg(_message.Message):
    __slots__ = ("register_backup_job_run_proto", "register_backup_job_run_proto_vec", "migration_uid", "user_info")
    REGISTER_BACKUP_JOB_RUN_PROTO_FIELD_NUMBER: _ClassVar[int]
    REGISTER_BACKUP_JOB_RUN_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    register_backup_job_run_proto: RegisterBackupJobRunArg
    register_backup_job_run_proto_vec: _containers.RepeatedCompositeFieldContainer[RegisterBackupJobRunArg]
    migration_uid: str
    user_info: _permissions_pb2.UserInformation
    def __init__(self, register_backup_job_run_proto: _Optional[_Union[RegisterBackupJobRunArg, _Mapping]] = ..., register_backup_job_run_proto_vec: _Optional[_Iterable[_Union[RegisterBackupJobRunArg, _Mapping]]] = ..., migration_uid: _Optional[str] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class RegisterArchivedBackupRunResult(_message.Message):
    __slots__ = ("register_backup_job_run_result", "register_backup_job_run_result_vec")
    REGISTER_BACKUP_JOB_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    REGISTER_BACKUP_JOB_RUN_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    register_backup_job_run_result: RegisterBackupJobRunResult
    register_backup_job_run_result_vec: _containers.RepeatedCompositeFieldContainer[RegisterBackupJobRunResult]
    def __init__(self, register_backup_job_run_result: _Optional[_Union[RegisterBackupJobRunResult, _Mapping]] = ..., register_backup_job_run_result_vec: _Optional[_Iterable[_Union[RegisterBackupJobRunResult, _Mapping]]] = ...) -> None: ...

class HandleArchivalCallbackArg(_message.Message):
    __slots__ = ("api_version", "notify_archival_task_completed_arg", "notify_archival_restore_task_completed_arg", "register_archived_backup_run_arg")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ARCHIVAL_TASK_COMPLETED_ARG_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ARCHIVAL_RESTORE_TASK_COMPLETED_ARG_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ARCHIVED_BACKUP_RUN_ARG_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    notify_archival_task_completed_arg: NotifyArchivalTaskCompletedArg
    notify_archival_restore_task_completed_arg: NotifyArchivalRestoreTaskCompletedArg
    register_archived_backup_run_arg: RegisterArchivedBackupRunArg
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., notify_archival_task_completed_arg: _Optional[_Union[NotifyArchivalTaskCompletedArg, _Mapping]] = ..., notify_archival_restore_task_completed_arg: _Optional[_Union[NotifyArchivalRestoreTaskCompletedArg, _Mapping]] = ..., register_archived_backup_run_arg: _Optional[_Union[RegisterArchivedBackupRunArg, _Mapping]] = ...) -> None: ...

class HandleArchivalCallbackResult(_message.Message):
    __slots__ = ("register_archived_backup_run_result",)
    REGISTER_ARCHIVED_BACKUP_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    register_archived_backup_run_result: RegisterArchivedBackupRunResult
    def __init__(self, register_archived_backup_run_result: _Optional[_Union[RegisterArchivedBackupRunResult, _Mapping]] = ...) -> None: ...

class RequestYodaProxyArg(_message.Message):
    __slots__ = ("api_version", "request_id", "object_id", "instance_id", "disk_name_vec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    request_id: str
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    disk_name_vec: str
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., disk_name_vec: _Optional[str] = ...) -> None: ...

class RequestYodaProxyResult(_message.Message):
    __slots__ = ("proxy_info",)
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    proxy_info: _proxy_pb2.ProxyInfo
    def __init__(self, proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ...) -> None: ...

class ReleaseYodaProxyArg(_message.Message):
    __slots__ = ("api_version", "request_id", "proxy_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    request_id: str
    proxy_info: _proxy_pb2.ProxyInfo
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ...) -> None: ...

class ReleaseYodaProxyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermitTaskArg(_message.Message):
    __slots__ = ("api_version", "task", "logical_timestamp")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task: _gatekeeper_pb2.Task
    logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ...) -> None: ...

class PermitTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseTaskArg(_message.Message):
    __slots__ = ("api_version", "task", "entities_to_unlock", "release_subtask_permits", "logical_timestamp", "release_resources_only")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TO_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    RELEASE_SUBTASK_PERMITS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RELEASE_RESOURCES_ONLY_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task: _gatekeeper_pb2.Task
    entities_to_unlock: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    release_subtask_permits: bool
    logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    release_resources_only: bool
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., entities_to_unlock: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., release_subtask_permits: bool = ..., logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ..., release_resources_only: bool = ...) -> None: ...

class ReleaseTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExecRemoteReplicationActionsArg(_message.Message):
    __slots__ = ("api_version", "actions")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    actions: _remote_actions_pb2.RemoteReplicationActions
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., actions: _Optional[_Union[_remote_actions_pb2.RemoteReplicationActions, _Mapping]] = ...) -> None: ...

class ExecRemoteReplicationActionsResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _remote_actions_pb2.RemoteReplicationActionsResult
    def __init__(self, result: _Optional[_Union[_remote_actions_pb2.RemoteReplicationActionsResult, _Mapping]] = ...) -> None: ...

class UpdateVerifyEntityRegistrationArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "entity", "verification_status", "verification_error", "app_verification_errors", "verification_info")
    class AppVerificationErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _error_pb2_1.ErrorProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_VERIFICATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    entity: _entity_pb2.EntityProto
    verification_status: _enums_pb2.VerificationStatus.Type
    verification_error: _error_pb2_1.ErrorProto
    app_verification_errors: _containers.MessageMap[int, _error_pb2_1.ErrorProto]
    verification_info: _magneto_pb2.VerificationInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., verification_status: _Optional[_Union[_enums_pb2.VerificationStatus.Type, str]] = ..., verification_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., app_verification_errors: _Optional[_Mapping[int, _error_pb2_1.ErrorProto]] = ..., verification_info: _Optional[_Union[_magneto_pb2.VerificationInfoProto, _Mapping]] = ...) -> None: ...

class UpdateVerifyEntityRegistrationResult(_message.Message):
    __slots__ = ("api_version",)
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ...) -> None: ...

class UpdateConversionTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "slave_op_clock", "conversion_status", "error", "conversion_info")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    slave_op_clock: _op_clock_pb2.OpClock
    conversion_status: _enums_pb2.ConversionStatus.Type
    error: _error_pb2_1.ErrorProto
    conversion_info: _magneto_pb2.ConversionInfoProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., conversion_status: _Optional[_Union[_enums_pb2.ConversionStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., conversion_info: _Optional[_Union[_magneto_pb2.ConversionInfoProto, _Mapping]] = ...) -> None: ...

class UpdateConversionTaskResult(_message.Message):
    __slots__ = ("api_version",)
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ...) -> None: ...

class CloudDeployUpdate(_message.Message):
    __slots__ = ("slave_op_clock", "status", "error", "cloud_deploy_info", "restore_info")
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    slave_op_clock: _op_clock_pb2.OpClock
    status: TaskStatus
    error: _error_pb2_1.ErrorProto
    cloud_deploy_info: _magneto_pb2.CloudDeployInfoProto
    restore_info: _magneto_pb2.RestoreInfoProto
    def __init__(self, slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., cloud_deploy_info: _Optional[_Union[_magneto_pb2.CloudDeployInfoProto, _Mapping]] = ..., restore_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto, _Mapping]] = ...) -> None: ...

class UpdateCloudDeployTaskArg(_message.Message):
    __slots__ = ("api_version", "task_uid", "cloud_deploy_update")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_uid: _universal_id_pb2.UniversalIdProto
    cloud_deploy_update: CloudDeployUpdate
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cloud_deploy_update: _Optional[_Union[CloudDeployUpdate, _Mapping]] = ...) -> None: ...

class UpdateCloudDeployTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateDownloadFilesTaskArg(_message.Message):
    __slots__ = ("api_version", "task_id", "error")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    task_id: int
    error: _error_pb2_1.ErrorProto
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateDownloadFilesTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
