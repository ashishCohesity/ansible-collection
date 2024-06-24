from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import ad_pb2 as _ad_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("dc", "error")
    AD_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    ad_snapshot_info: _descriptor.FieldDescriptor
    DC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    dc: _ad_pb2.ADDomainController
    error: _error_pb2.ErrorProto
    def __init__(self, dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VerificationInfo(_message.Message):
    __slots__ = ("host_name", "dc")
    AD_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ad_verification_info: _descriptor.FieldDescriptor
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    DC_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    dc: _ad_pb2.ADDomainController
    def __init__(self, host_name: _Optional[str] = ..., dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("restore_task_state", "ldap_port", "mount_points_vec", "backup_job_id", "dc", "dsamain_proc_id", "restore_disks_task_info_proto", "credentials", "ad_update_options", "ad_restore_status_vec", "num_successfull", "num_failed", "num_running", "mount_and_restore_task_state", "is_mount_and_restore_task", "can_teardown", "sysvol_folder_absolute_path")
    class RestoreTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.RestoreTaskState]
        kVHDMounted: _ClassVar[RestoreInfo.RestoreTaskState]
        kFinished: _ClassVar[RestoreInfo.RestoreTaskState]
    kStarted: RestoreInfo.RestoreTaskState
    kVHDMounted: RestoreInfo.RestoreTaskState
    kFinished: RestoreInfo.RestoreTaskState
    class MountAndRestoreTaskState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[RestoreInfo.MountAndRestoreTaskState.Type]
            kMounted: _ClassVar[RestoreInfo.MountAndRestoreTaskState.Type]
            kObjectsRestored: _ClassVar[RestoreInfo.MountAndRestoreTaskState.Type]
            kFinished: _ClassVar[RestoreInfo.MountAndRestoreTaskState.Type]
        kStarted: RestoreInfo.MountAndRestoreTaskState.Type
        kMounted: RestoreInfo.MountAndRestoreTaskState.Type
        kObjectsRestored: RestoreInfo.MountAndRestoreTaskState.Type
        kFinished: RestoreInfo.MountAndRestoreTaskState.Type
        def __init__(self) -> None: ...
    AD_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    ad_restore_info: _descriptor.FieldDescriptor
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINTS_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DC_FIELD_NUMBER: _ClassVar[int]
    DSAMAIN_PROC_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AD_UPDATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AD_RESTORE_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFULL_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_FIELD_NUMBER: _ClassVar[int]
    NUM_RUNNING_FIELD_NUMBER: _ClassVar[int]
    MOUNT_AND_RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_MOUNT_AND_RESTORE_TASK_FIELD_NUMBER: _ClassVar[int]
    CAN_TEARDOWN_FIELD_NUMBER: _ClassVar[int]
    SYSVOL_FOLDER_ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: RestoreInfo.RestoreTaskState
    ldap_port: int
    mount_points_vec: _containers.RepeatedScalarFieldContainer[str]
    backup_job_id: int
    dc: _ad_pb2.ADDomainController
    dsamain_proc_id: int
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    credentials: _credentials_pb2.Credentials
    ad_update_options: _magneto_pb2.ADUpdateRestoreTaskOptions
    ad_restore_status_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.ADRestoreStatus]
    num_successfull: int
    num_failed: int
    num_running: int
    mount_and_restore_task_state: RestoreInfo.MountAndRestoreTaskState.Type
    is_mount_and_restore_task: bool
    can_teardown: bool
    sysvol_folder_absolute_path: str
    def __init__(self, restore_task_state: _Optional[_Union[RestoreInfo.RestoreTaskState, str]] = ..., ldap_port: _Optional[int] = ..., mount_points_vec: _Optional[_Iterable[str]] = ..., backup_job_id: _Optional[int] = ..., dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ..., dsamain_proc_id: _Optional[int] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., ad_update_options: _Optional[_Union[_magneto_pb2.ADUpdateRestoreTaskOptions, _Mapping]] = ..., ad_restore_status_vec: _Optional[_Iterable[_Union[_magneto_pb2.ADRestoreStatus, _Mapping]]] = ..., num_successfull: _Optional[int] = ..., num_failed: _Optional[int] = ..., num_running: _Optional[int] = ..., mount_and_restore_task_state: _Optional[_Union[RestoreInfo.MountAndRestoreTaskState.Type, str]] = ..., is_mount_and_restore_task: bool = ..., can_teardown: bool = ..., sysvol_folder_absolute_path: _Optional[str] = ...) -> None: ...

class DestroyTaskInfo(_message.Message):
    __slots__ = ("dc", "dsamain_proc_id", "restore_disks_task_info_proto")
    AD_DESTROY_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    ad_destroy_app_task_info: _descriptor.FieldDescriptor
    DC_FIELD_NUMBER: _ClassVar[int]
    DSAMAIN_PROC_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    dc: _ad_pb2.ADDomainController
    dsamain_proc_id: int
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    def __init__(self, dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ..., dsamain_proc_id: _Optional[int] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ...) -> None: ...
