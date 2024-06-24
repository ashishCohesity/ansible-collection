from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteActionArg(_message.Message):
    __slots__ = ("api_version", "action_type", "env_type", "source_env_type", "expected_bridge_incarnation_id", "op_clock", "user_info", "is_using_bifrost", "delete_dirs_arg", "delete_files_arg", "fetch_files_arg", "clone_dir_arg", "sync_request", "sub_task_id", "task_attributes")
    Extensions: _python_message._ExtensionDict
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMwareAction: _ClassVar[ExecuteActionArg.ActionType]
        kDeleteFilesAction: _ClassVar[ExecuteActionArg.ActionType]
        kDeleteDirsAction: _ClassVar[ExecuteActionArg.ActionType]
        kReplicationAction: _ClassVar[ExecuteActionArg.ActionType]
        kSqlAction: _ClassVar[ExecuteActionArg.ActionType]
        kViewAction: _ClassVar[ExecuteActionArg.ActionType]
        kFetchFilesAction: _ClassVar[ExecuteActionArg.ActionType]
        kPhysicalAction: _ClassVar[ExecuteActionArg.ActionType]
        kSanAction: _ClassVar[ExecuteActionArg.ActionType]
        kAzureAction: _ClassVar[ExecuteActionArg.ActionType]
        kFileAction: _ClassVar[ExecuteActionArg.ActionType]
        kAgentAction: _ClassVar[ExecuteActionArg.ActionType]
        kHyperVAction: _ClassVar[ExecuteActionArg.ActionType]
        kAcropolisAction: _ClassVar[ExecuteActionArg.ActionType]
        kKVMAction: _ClassVar[ExecuteActionArg.ActionType]
        kCloudAction: _ClassVar[ExecuteActionArg.ActionType]
        kHyperVVSSAction: _ClassVar[ExecuteActionArg.ActionType]
        kAWSAction: _ClassVar[ExecuteActionArg.ActionType]
        kAppFileAction: _ClassVar[ExecuteActionArg.ActionType]
        kOracleAction: _ClassVar[ExecuteActionArg.ActionType]
        kOutlookAction: _ClassVar[ExecuteActionArg.ActionType]
        kGCPAction: _ClassVar[ExecuteActionArg.ActionType]
        kOneDriveAction: _ClassVar[ExecuteActionArg.ActionType]
        kO365Action: _ClassVar[ExecuteActionArg.ActionType]
        kSharepointAction: _ClassVar[ExecuteActionArg.ActionType]
        kCloneDirAction: _ClassVar[ExecuteActionArg.ActionType]
        kPublicFolderAction: _ClassVar[ExecuteActionArg.ActionType]
        kTeamsAction: _ClassVar[ExecuteActionArg.ActionType]
        kGroupAction: _ClassVar[ExecuteActionArg.ActionType]
        kCDPAction: _ClassVar[ExecuteActionArg.ActionType]
        kObjectStoreAction: _ClassVar[ExecuteActionArg.ActionType]
    kVMwareAction: ExecuteActionArg.ActionType
    kDeleteFilesAction: ExecuteActionArg.ActionType
    kDeleteDirsAction: ExecuteActionArg.ActionType
    kReplicationAction: ExecuteActionArg.ActionType
    kSqlAction: ExecuteActionArg.ActionType
    kViewAction: ExecuteActionArg.ActionType
    kFetchFilesAction: ExecuteActionArg.ActionType
    kPhysicalAction: ExecuteActionArg.ActionType
    kSanAction: ExecuteActionArg.ActionType
    kAzureAction: ExecuteActionArg.ActionType
    kFileAction: ExecuteActionArg.ActionType
    kAgentAction: ExecuteActionArg.ActionType
    kHyperVAction: ExecuteActionArg.ActionType
    kAcropolisAction: ExecuteActionArg.ActionType
    kKVMAction: ExecuteActionArg.ActionType
    kCloudAction: ExecuteActionArg.ActionType
    kHyperVVSSAction: ExecuteActionArg.ActionType
    kAWSAction: ExecuteActionArg.ActionType
    kAppFileAction: ExecuteActionArg.ActionType
    kOracleAction: ExecuteActionArg.ActionType
    kOutlookAction: ExecuteActionArg.ActionType
    kGCPAction: ExecuteActionArg.ActionType
    kOneDriveAction: ExecuteActionArg.ActionType
    kO365Action: ExecuteActionArg.ActionType
    kSharepointAction: ExecuteActionArg.ActionType
    kCloneDirAction: ExecuteActionArg.ActionType
    kPublicFolderAction: ExecuteActionArg.ActionType
    kTeamsAction: ExecuteActionArg.ActionType
    kGroupAction: ExecuteActionArg.ActionType
    kCDPAction: ExecuteActionArg.ActionType
    kObjectStoreAction: ExecuteActionArg.ActionType
    class DeleteDirsArg(_message.Message):
        __slots__ = ("task_id", "dirs_to_delete_DEPRECATED", "dirs_to_delete")
        class DirToDelete(_message.Message):
            __slots__ = ("dir", "view_box_id")
            DIR_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            dir: str
            view_box_id: int
            def __init__(self, dir: _Optional[str] = ..., view_box_id: _Optional[int] = ...) -> None: ...
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        DIRS_TO_DELETE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        DIRS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        dirs_to_delete_DEPRECATED: _containers.RepeatedScalarFieldContainer[str]
        dirs_to_delete: _containers.RepeatedCompositeFieldContainer[ExecuteActionArg.DeleteDirsArg.DirToDelete]
        def __init__(self, task_id: _Optional[int] = ..., dirs_to_delete_DEPRECATED: _Optional[_Iterable[str]] = ..., dirs_to_delete: _Optional[_Iterable[_Union[ExecuteActionArg.DeleteDirsArg.DirToDelete, _Mapping]]] = ...) -> None: ...
    class DeleteFilesArg(_message.Message):
        __slots__ = ("task_id", "files_to_delete_vec", "delete_empty_parent_dir")
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        FILES_TO_DELETE_VEC_FIELD_NUMBER: _ClassVar[int]
        DELETE_EMPTY_PARENT_DIR_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        files_to_delete_vec: _containers.RepeatedScalarFieldContainer[str]
        delete_empty_parent_dir: bool
        def __init__(self, task_id: _Optional[int] = ..., files_to_delete_vec: _Optional[_Iterable[str]] = ..., delete_empty_parent_dir: bool = ...) -> None: ...
    class FetchFilesArg(_message.Message):
        __slots__ = ("task_id", "dir_vec")
        class Dir(_message.Message):
            __slots__ = ("full_dir_path", "file_vec")
            class File(_message.Message):
                __slots__ = ("file_name", "num_bytes")
                FILE_NAME_FIELD_NUMBER: _ClassVar[int]
                NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
                file_name: str
                num_bytes: int
                def __init__(self, file_name: _Optional[str] = ..., num_bytes: _Optional[int] = ...) -> None: ...
            FULL_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
            FILE_VEC_FIELD_NUMBER: _ClassVar[int]
            full_dir_path: str
            file_vec: _containers.RepeatedCompositeFieldContainer[ExecuteActionArg.FetchFilesArg.Dir.File]
            def __init__(self, full_dir_path: _Optional[str] = ..., file_vec: _Optional[_Iterable[_Union[ExecuteActionArg.FetchFilesArg.Dir.File, _Mapping]]] = ...) -> None: ...
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        DIR_VEC_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        dir_vec: _containers.RepeatedCompositeFieldContainer[ExecuteActionArg.FetchFilesArg.Dir]
        def __init__(self, task_id: _Optional[int] = ..., dir_vec: _Optional[_Iterable[_Union[ExecuteActionArg.FetchFilesArg.Dir, _Mapping]]] = ...) -> None: ...
    class CloneDirArg(_message.Message):
        __slots__ = ("task_id", "absolute_src_parent_path", "absolute_dst_parent_path", "src_dir", "dst_dir")
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_SRC_PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_DST_PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
        SRC_DIR_FIELD_NUMBER: _ClassVar[int]
        DST_DIR_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        absolute_src_parent_path: str
        absolute_dst_parent_path: str
        src_dir: str
        dst_dir: str
        def __init__(self, task_id: _Optional[int] = ..., absolute_src_parent_path: _Optional[str] = ..., absolute_dst_parent_path: _Optional[str] = ..., src_dir: _Optional[str] = ..., dst_dir: _Optional[str] = ...) -> None: ...
    class TaskAttributes(_message.Message):
        __slots__ = ("task_id", "job_uid", "data_source", "registered_source", "env_type")
        class SourceInfo(_message.Message):
            __slots__ = ("source_id", "source_name")
            SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
            SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
            source_id: int
            source_name: str
            def __init__(self, source_id: _Optional[int] = ..., source_name: _Optional[str] = ...) -> None: ...
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
        ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        job_uid: _universal_id_pb2.UniversalIdProto
        data_source: ExecuteActionArg.TaskAttributes.SourceInfo
        registered_source: ExecuteActionArg.TaskAttributes.SourceInfo
        env_type: _enums_pb2.Environment.Type
        def __init__(self, task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., data_source: _Optional[_Union[ExecuteActionArg.TaskAttributes.SourceInfo, _Mapping]] = ..., registered_source: _Optional[_Union[ExecuteActionArg.TaskAttributes.SourceInfo, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BRIDGE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_USING_BIFROST_FIELD_NUMBER: _ClassVar[int]
    DELETE_DIRS_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_DIR_ARG_FIELD_NUMBER: _ClassVar[int]
    SYNC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    action_type: ExecuteActionArg.ActionType
    env_type: _enums_pb2.Environment.Type
    source_env_type: _enums_pb2.Environment.Type
    expected_bridge_incarnation_id: int
    op_clock: _op_clock_pb2.OpClock
    user_info: _permissions_pb2.UserInformation
    is_using_bifrost: bool
    delete_dirs_arg: ExecuteActionArg.DeleteDirsArg
    delete_files_arg: ExecuteActionArg.DeleteFilesArg
    fetch_files_arg: ExecuteActionArg.FetchFilesArg
    clone_dir_arg: ExecuteActionArg.CloneDirArg
    sync_request: bool
    sub_task_id: int
    task_attributes: ExecuteActionArg.TaskAttributes
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., action_type: _Optional[_Union[ExecuteActionArg.ActionType, str]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., source_env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., expected_bridge_incarnation_id: _Optional[int] = ..., op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., is_using_bifrost: bool = ..., delete_dirs_arg: _Optional[_Union[ExecuteActionArg.DeleteDirsArg, _Mapping]] = ..., delete_files_arg: _Optional[_Union[ExecuteActionArg.DeleteFilesArg, _Mapping]] = ..., fetch_files_arg: _Optional[_Union[ExecuteActionArg.FetchFilesArg, _Mapping]] = ..., clone_dir_arg: _Optional[_Union[ExecuteActionArg.CloneDirArg, _Mapping]] = ..., sync_request: bool = ..., sub_task_id: _Optional[int] = ..., task_attributes: _Optional[_Union[ExecuteActionArg.TaskAttributes, _Mapping]] = ...) -> None: ...

class ExecuteActionResult(_message.Message):
    __slots__ = ("bridge_incarnation_id", "action_update_arg")
    Extensions: _python_message._ExtensionDict
    BRIDGE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    bridge_incarnation_id: int
    action_update_arg: _bridge_updates_pb2.ActionUpdateArg
    def __init__(self, bridge_incarnation_id: _Optional[int] = ..., action_update_arg: _Optional[_Union[_bridge_updates_pb2.ActionUpdateArg, _Mapping]] = ...) -> None: ...

class BackupBaseArg(_message.Message):
    __slots__ = ("job_id", "job_instance_id", "attempt_num", "previous_snapshot_root_path", "previous_snapshot_relative_path", "view_box_id", "view_name", "qos_principal_name", "connector_params", "additional_file_data_vec", "disk_info_vec", "backup_aborted", "stats_container_id", "sub_file_size_mb", "root_path", "relative_snapshot_dir")
    class FileData(_message.Message):
        __slots__ = ("file_name", "data", "is_compressed", "should_delete", "file_attributes")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
        SHOULD_DELETE_FIELD_NUMBER: _ClassVar[int]
        FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        data: bytes
        is_compressed: bool
        should_delete: bool
        file_attributes: _file_attrs_pb2.FileAttributes
        def __init__(self, file_name: _Optional[str] = ..., data: _Optional[bytes] = ..., is_compressed: bool = ..., should_delete: bool = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ...) -> None: ...
    class DiskInfo(_message.Message):
        __slots__ = ("disk", "should_delete", "prev_disk", "area", "sub_task_disk_info_vec", "key", "capacity", "filename", "filepath")
        class SubTaskDiskInfo(_message.Message):
            __slots__ = ("sub_task_id", "start_pos", "end_pos")
            SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
            START_POS_FIELD_NUMBER: _ClassVar[int]
            END_POS_FIELD_NUMBER: _ClassVar[int]
            sub_task_id: int
            start_pos: int
            end_pos: int
            def __init__(self, sub_task_id: _Optional[int] = ..., start_pos: _Optional[int] = ..., end_pos: _Optional[int] = ...) -> None: ...
        DISK_FIELD_NUMBER: _ClassVar[int]
        SHOULD_DELETE_FIELD_NUMBER: _ClassVar[int]
        PREV_DISK_FIELD_NUMBER: _ClassVar[int]
        AREA_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        FILEPATH_FIELD_NUMBER: _ClassVar[int]
        disk: _disk_pb2.DiskProto
        should_delete: bool
        prev_disk: _disk_pb2.DiskProto
        area: _disk_pb2.DiskAreaProto
        sub_task_disk_info_vec: _containers.RepeatedCompositeFieldContainer[BackupBaseArg.DiskInfo.SubTaskDiskInfo]
        key: int
        capacity: int
        filename: str
        filepath: str
        def __init__(self, disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., should_delete: bool = ..., prev_disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., area: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ..., sub_task_disk_info_vec: _Optional[_Iterable[_Union[BackupBaseArg.DiskInfo.SubTaskDiskInfo, _Mapping]]] = ..., key: _Optional[int] = ..., capacity: _Optional[int] = ..., filename: _Optional[str] = ..., filepath: _Optional[str] = ...) -> None: ...
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FILE_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ABORTED_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_instance_id: int
    attempt_num: int
    previous_snapshot_root_path: str
    previous_snapshot_relative_path: str
    view_box_id: int
    view_name: str
    qos_principal_name: str
    connector_params: _magneto_pb2.ConnectorParams
    additional_file_data_vec: _containers.RepeatedCompositeFieldContainer[BackupBaseArg.FileData]
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[BackupBaseArg.DiskInfo]
    backup_aborted: bool
    stats_container_id: int
    sub_file_size_mb: int
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., previous_snapshot_root_path: _Optional[str] = ..., previous_snapshot_relative_path: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., qos_principal_name: _Optional[str] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., additional_file_data_vec: _Optional[_Iterable[_Union[BackupBaseArg.FileData, _Mapping]]] = ..., disk_info_vec: _Optional[_Iterable[_Union[BackupBaseArg.DiskInfo, _Mapping]]] = ..., backup_aborted: bool = ..., stats_container_id: _Optional[int] = ..., sub_file_size_mb: _Optional[int] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("task_id", "dead_slave_constituent_id", "dead_slave_incarnation_id", "wait_for_cancellation")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    dead_slave_constituent_id: int
    dead_slave_incarnation_id: int
    wait_for_cancellation: bool
    def __init__(self, task_id: _Optional[int] = ..., dead_slave_constituent_id: _Optional[int] = ..., dead_slave_incarnation_id: _Optional[int] = ..., wait_for_cancellation: bool = ...) -> None: ...

class RestoreBaseArg(_message.Message):
    __slots__ = ("disk_info", "host_entity", "connector_params", "job_id")
    class DiskInfo(_message.Message):
        __slots__ = ("disk", "area", "device_path", "encoded_filename", "key")
        DISK_FIELD_NUMBER: _ClassVar[int]
        AREA_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
        ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        disk: _disk_pb2.DiskProto
        area: _disk_pb2.DiskAreaProto
        device_path: bytes
        encoded_filename: str
        key: int
        def __init__(self, disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., area: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ..., device_path: _Optional[bytes] = ..., encoded_filename: _Optional[str] = ..., key: _Optional[int] = ...) -> None: ...
    DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    disk_info: RestoreBaseArg.DiskInfo
    host_entity: _entity_pb2.EntityProto
    connector_params: _magneto_pb2.ConnectorParams
    job_id: int
    def __init__(self, disk_info: _Optional[_Union[RestoreBaseArg.DiskInfo, _Mapping]] = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., job_id: _Optional[int] = ...) -> None: ...
