from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.connectors.oracle import oracle_pb2 as _oracle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDBInfoArg(_message.Message):
    __slots__ = ("view_name", "relative_db_dir", "uuid")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    relative_db_dir: str
    uuid: str
    def __init__(self, view_name: _Optional[str] = ..., relative_db_dir: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class BackupDBsArg(_message.Message):
    __slots__ = ("base", "view_name", "create_dir_vec", "delete_file_vec", "delete_dir_vec", "delete_dir_if_emtpty", "db_info_vec", "backup_view_name", "get_db_info_arg_vec", "skip_delete_root_dir")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_DIR_IF_EMTPTY_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    GET_DB_INFO_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_DELETE_ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    view_name: str
    create_dir_vec: _containers.RepeatedScalarFieldContainer[str]
    delete_file_vec: _containers.RepeatedScalarFieldContainer[str]
    delete_dir_vec: _containers.RepeatedScalarFieldContainer[str]
    delete_dir_if_emtpty: bool
    db_info_vec: _containers.RepeatedCompositeFieldContainer[_oracle_pb2.DatabaseBackupInfo]
    backup_view_name: str
    get_db_info_arg_vec: _containers.RepeatedCompositeFieldContainer[GetDBInfoArg]
    skip_delete_root_dir: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., view_name: _Optional[str] = ..., create_dir_vec: _Optional[_Iterable[str]] = ..., delete_file_vec: _Optional[_Iterable[str]] = ..., delete_dir_vec: _Optional[_Iterable[str]] = ..., delete_dir_if_emtpty: bool = ..., db_info_vec: _Optional[_Iterable[_Union[_oracle_pb2.DatabaseBackupInfo, _Mapping]]] = ..., backup_view_name: _Optional[str] = ..., get_db_info_arg_vec: _Optional[_Iterable[_Union[GetDBInfoArg, _Mapping]]] = ..., skip_delete_root_dir: bool = ...) -> None: ...

class RestoreDBArg(_message.Message):
    __slots__ = ("type", "view_box_id", "view_name", "dest_relative_path", "create_view", "source_view_name", "relative_path", "file_prefix", "file_name_vec", "ip_addr_str_vec", "get_db_info_arg_vec", "num_catalog_groups", "special_file_name_vec", "archived_log_file_map", "create_dirs", "special_file_name_map", "ignore_error_file_name_map", "trim_data_file_info", "trim_previous_data_file_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneDBBackupFiles: _ClassVar[RestoreDBArg.Type]
        kDeleteRestoreView: _ClassVar[RestoreDBArg.Type]
        kGetDBsBackupInfo: _ClassVar[RestoreDBArg.Type]
    kCloneDBBackupFiles: RestoreDBArg.Type
    kDeleteRestoreView: RestoreDBArg.Type
    kGetDBsBackupInfo: RestoreDBArg.Type
    class ArchivedLogFileMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class SpecialFileNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class IgnoreErrorFileNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    GET_DB_INFO_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_CATALOG_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOG_FILE_MAP_FIELD_NUMBER: _ClassVar[int]
    CREATE_DIRS_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FILE_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ERROR_FILE_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    TRIM_DATA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    TRIM_PREVIOUS_DATA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: RestoreDBArg.Type
    view_box_id: int
    view_name: str
    dest_relative_path: str
    create_view: bool
    source_view_name: str
    relative_path: str
    file_prefix: str
    file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    get_db_info_arg_vec: _containers.RepeatedCompositeFieldContainer[GetDBInfoArg]
    num_catalog_groups: int
    special_file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    archived_log_file_map: _containers.ScalarMap[str, bool]
    create_dirs: bool
    special_file_name_map: _containers.ScalarMap[str, str]
    ignore_error_file_name_map: _containers.ScalarMap[str, bool]
    trim_data_file_info: bool
    trim_previous_data_file_info: bool
    def __init__(self, type: _Optional[_Union[RestoreDBArg.Type, str]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., dest_relative_path: _Optional[str] = ..., create_view: bool = ..., source_view_name: _Optional[str] = ..., relative_path: _Optional[str] = ..., file_prefix: _Optional[str] = ..., file_name_vec: _Optional[_Iterable[str]] = ..., ip_addr_str_vec: _Optional[_Iterable[str]] = ..., get_db_info_arg_vec: _Optional[_Iterable[_Union[GetDBInfoArg, _Mapping]]] = ..., num_catalog_groups: _Optional[int] = ..., special_file_name_vec: _Optional[_Iterable[str]] = ..., archived_log_file_map: _Optional[_Mapping[str, bool]] = ..., create_dirs: bool = ..., special_file_name_map: _Optional[_Mapping[str, str]] = ..., ignore_error_file_name_map: _Optional[_Mapping[str, bool]] = ..., trim_data_file_info: bool = ..., trim_previous_data_file_info: bool = ...) -> None: ...

class CopyDBFilesArg(_message.Message):
    __slots__ = ("view_box_id", "view_name", "relative_db_dir", "destination_dir", "file_prefix", "file_name_vec", "files_info_vec", "job_uid_str", "db_uniq_name")
    class CopyFilesInfo(_message.Message):
        __slots__ = ("view_box_id", "view_name", "relative_dir", "file_name_vec", "prefix", "run_id")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_DIR_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        RUN_ID_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        view_name: str
        relative_dir: str
        file_name_vec: _containers.RepeatedScalarFieldContainer[str]
        prefix: str
        run_id: int
        def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., relative_dir: _Optional[str] = ..., file_name_vec: _Optional[_Iterable[str]] = ..., prefix: _Optional[str] = ..., run_id: _Optional[int] = ...) -> None: ...
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DIR_FIELD_NUMBER: _ClassVar[int]
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    FILES_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_STR_FIELD_NUMBER: _ClassVar[int]
    DB_UNIQ_NAME_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    view_name: str
    relative_db_dir: str
    destination_dir: str
    file_prefix: str
    file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    files_info_vec: _containers.RepeatedCompositeFieldContainer[CopyDBFilesArg.CopyFilesInfo]
    job_uid_str: str
    db_uniq_name: str
    def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., relative_db_dir: _Optional[str] = ..., destination_dir: _Optional[str] = ..., file_prefix: _Optional[str] = ..., file_name_vec: _Optional[_Iterable[str]] = ..., files_info_vec: _Optional[_Iterable[_Union[CopyDBFilesArg.CopyFilesInfo, _Mapping]]] = ..., job_uid_str: _Optional[str] = ..., db_uniq_name: _Optional[str] = ...) -> None: ...

class PrepareArchiveViewArg(_message.Message):
    __slots__ = ("job_id", "job_instance_id", "view_box_id", "backup_view_name", "clone_suffix", "relative_db_dir")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_instance_id: int
    view_box_id: int
    backup_view_name: str
    clone_suffix: str
    relative_db_dir: str
    def __init__(self, job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., backup_view_name: _Optional[str] = ..., clone_suffix: _Optional[str] = ..., relative_db_dir: _Optional[str] = ...) -> None: ...

class PostProcessArchiveViewArg(_message.Message):
    __slots__ = ("temp_view_for_archival",)
    TEMP_VIEW_FOR_ARCHIVAL_FIELD_NUMBER: _ClassVar[int]
    temp_view_for_archival: str
    def __init__(self, temp_view_for_archival: _Optional[str] = ...) -> None: ...

class OracleActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_dbs_arg", "restore_db_arg", "copy_db_files_arg", "prepare_archive_view_arg", "post_archive_view_arg")
    ORACLE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    oracle_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DBS_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DB_ARG_FIELD_NUMBER: _ClassVar[int]
    COPY_DB_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    PREPARE_ARCHIVE_VIEW_ARG_FIELD_NUMBER: _ClassVar[int]
    POST_ARCHIVE_VIEW_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_dbs_arg: BackupDBsArg
    restore_db_arg: RestoreDBArg
    copy_db_files_arg: CopyDBFilesArg
    prepare_archive_view_arg: PrepareArchiveViewArg
    post_archive_view_arg: PostProcessArchiveViewArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_dbs_arg: _Optional[_Union[BackupDBsArg, _Mapping]] = ..., restore_db_arg: _Optional[_Union[RestoreDBArg, _Mapping]] = ..., copy_db_files_arg: _Optional[_Union[CopyDBFilesArg, _Mapping]] = ..., prepare_archive_view_arg: _Optional[_Union[PrepareArchiveViewArg, _Mapping]] = ..., post_archive_view_arg: _Optional[_Union[PostProcessArchiveViewArg, _Mapping]] = ...) -> None: ...

class JobTaskStateInfo(_message.Message):
    __slots__ = ("ongoing_task_info_vec", "job_id")
    class OngoingTaskInfo(_message.Message):
        __slots__ = ("task_id",)
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        def __init__(self, task_id: _Optional[int] = ...) -> None: ...
    ONGOING_TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ongoing_task_info_vec: _containers.RepeatedCompositeFieldContainer[JobTaskStateInfo.OngoingTaskInfo]
    job_id: int
    def __init__(self, ongoing_task_info_vec: _Optional[_Iterable[_Union[JobTaskStateInfo.OngoingTaskInfo, _Mapping]]] = ..., job_id: _Optional[int] = ...) -> None: ...
