from open_util.net import protorpc_pb2 as _protorpc_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from yoda.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestHeader(_message.Message):
    __slots__ = ("client_api_version",)
    CLIENT_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    client_api_version: int
    def __init__(self, client_api_version: _Optional[int] = ...) -> None: ...

class AgentInfo(_message.Message):
    __slots__ = ("api_version",)
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    api_version: int
    def __init__(self, api_version: _Optional[int] = ...) -> None: ...

class NFSMountArg(_message.Message):
    __slots__ = ("remote_path", "host", "nfs_mounter_readahead_setting_kb")
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNTER_READAHEAD_SETTING_KB_FIELD_NUMBER: _ClassVar[int]
    remote_path: str
    host: str
    nfs_mounter_readahead_setting_kb: int
    def __init__(self, remote_path: _Optional[str] = ..., host: _Optional[str] = ..., nfs_mounter_readahead_setting_kb: _Optional[int] = ...) -> None: ...

class VolumeMountArg(_message.Message):
    __slots__ = ("vm_instance_identifier", "volume_name", "nfs_mount_key", "disk_files_path", "volume_map", "fuse_fs_needed")
    VM_INSTANCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_FILES_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MAP_FIELD_NUMBER: _ClassVar[int]
    FUSE_FS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    vm_instance_identifier: str
    volume_name: str
    nfs_mount_key: str
    disk_files_path: str
    volume_map: _volume_info_pb2.VolumeNameMap
    fuse_fs_needed: bool
    def __init__(self, vm_instance_identifier: _Optional[str] = ..., volume_name: _Optional[str] = ..., nfs_mount_key: _Optional[str] = ..., disk_files_path: _Optional[str] = ..., volume_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., fuse_fs_needed: bool = ...) -> None: ...

class VolMappingFileInfo(_message.Message):
    __slots__ = ("boot_volume_info", "vol_mapping_file_mtime_secs")
    BOOT_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    VOL_MAPPING_FILE_MTIME_SECS_FIELD_NUMBER: _ClassVar[int]
    boot_volume_info: _volume_info_pb2.VolumeInfo
    vol_mapping_file_mtime_secs: int
    def __init__(self, boot_volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., vol_mapping_file_mtime_secs: _Optional[int] = ...) -> None: ...

class PrepareVMVolumeInfoArg(_message.Message):
    __slots__ = ("header", "vm_instance_identifier", "nfs_mount_key", "disk_files_path", "supported_volumes_only", "old_volume_map", "fuse_fs_needed", "vol_mapping_file_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VM_INSTANCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_FILES_PATH_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VOLUMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    OLD_VOLUME_MAP_FIELD_NUMBER: _ClassVar[int]
    FUSE_FS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    VOL_MAPPING_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    vm_instance_identifier: str
    nfs_mount_key: str
    disk_files_path: str
    supported_volumes_only: bool
    old_volume_map: _volume_info_pb2.VolumeNameMap
    fuse_fs_needed: bool
    vol_mapping_file_info: VolMappingFileInfo
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., vm_instance_identifier: _Optional[str] = ..., nfs_mount_key: _Optional[str] = ..., disk_files_path: _Optional[str] = ..., supported_volumes_only: bool = ..., old_volume_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., fuse_fs_needed: bool = ..., vol_mapping_file_info: _Optional[_Union[VolMappingFileInfo, _Mapping]] = ...) -> None: ...

class VMVolumeInfoResult(_message.Message):
    __slots__ = ("error", "volume_name_map", "skipped_disk_or_volume", "vol_mapping_file_info", "disk_or_volume_skip_reason_vec", "corrupted_disk_info_vec")
    class CorruptedDiskInfo(_message.Message):
        __slots__ = ("disk_uuid", "disk_name")
        DISK_UUID_FIELD_NUMBER: _ClassVar[int]
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        disk_uuid: str
        disk_name: str
        def __init__(self, disk_uuid: _Optional[str] = ..., disk_name: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_DISK_OR_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VOL_MAPPING_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    DISK_OR_VOLUME_SKIP_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    CORRUPTED_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_name_map: _volume_info_pb2.VolumeNameMap
    skipped_disk_or_volume: bool
    vol_mapping_file_info: VolMappingFileInfo
    disk_or_volume_skip_reason_vec: _containers.RepeatedScalarFieldContainer[str]
    corrupted_disk_info_vec: _containers.RepeatedCompositeFieldContainer[VMVolumeInfoResult.CorruptedDiskInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_name_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., skipped_disk_or_volume: bool = ..., vol_mapping_file_info: _Optional[_Union[VolMappingFileInfo, _Mapping]] = ..., disk_or_volume_skip_reason_vec: _Optional[_Iterable[str]] = ..., corrupted_disk_info_vec: _Optional[_Iterable[_Union[VMVolumeInfoResult.CorruptedDiskInfo, _Mapping]]] = ...) -> None: ...

class PrepareResult(_message.Message):
    __slots__ = ("error", "task_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_id: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetTaskStatusArg(_message.Message):
    __slots__ = ("header", "task_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    task_id: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetTaskStatusResult(_message.Message):
    __slots__ = ("error", "vm_volume_info_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_VOLUME_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_volume_info_result: VMVolumeInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_volume_info_result: _Optional[_Union[VMVolumeInfoResult, _Mapping]] = ...) -> None: ...

class MountArg(_message.Message):
    __slots__ = ("header", "nfs_mount_arg", "volume_mount_arg", "mount_options")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_ARG_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    nfs_mount_arg: NFSMountArg
    volume_mount_arg: VolumeMountArg
    mount_options: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., nfs_mount_arg: _Optional[_Union[NFSMountArg, _Mapping]] = ..., volume_mount_arg: _Optional[_Union[VolumeMountArg, _Mapping]] = ..., mount_options: _Optional[str] = ...) -> None: ...

class MountResult(_message.Message):
    __slots__ = ("error", "mount_key", "mount_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mount_key: str
    mount_path: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mount_key: _Optional[str] = ..., mount_path: _Optional[str] = ...) -> None: ...

class UnmountArg(_message.Message):
    __slots__ = ("header", "mount_type", "volume_key")
    class MountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVmfs: _ClassVar[UnmountArg.MountType]
        kNFS: _ClassVar[UnmountArg.MountType]
        kFuse: _ClassVar[UnmountArg.MountType]
    kVmfs: UnmountArg.MountType
    kNFS: UnmountArg.MountType
    kFuse: UnmountArg.MountType
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_KEY_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    mount_type: UnmountArg.MountType
    volume_key: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., mount_type: _Optional[_Union[UnmountArg.MountType, str]] = ..., volume_key: _Optional[str] = ...) -> None: ...

class UnmountResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("header", "volume_mount_key", "filepath", "start_offset", "length")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    volume_mount_key: str
    filepath: str
    start_offset: int
    length: int
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., volume_mount_key: _Optional[str] = ..., filepath: _Optional[str] = ..., start_offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("error", "file_size", "data", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_size: int
    data: bytes
    eof: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_size: _Optional[int] = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class FileStatInfo(_message.Message):
    __slots__ = ("size", "mtime_usecs", "type", "mode", "uid", "gid", "ctime_usecs", "access_time_usecs", "num_hardlinks", "inode_id")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    size: int
    mtime_usecs: int
    type: ReadDirResult.DirEntry.Type
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    access_time_usecs: int
    num_hardlinks: int
    inode_id: int
    def __init__(self, size: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., type: _Optional[_Union[ReadDirResult.DirEntry.Type, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., access_time_usecs: _Optional[int] = ..., num_hardlinks: _Optional[int] = ..., inode_id: _Optional[int] = ...) -> None: ...

class ReadDirCookie(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class ReadDirArg(_message.Message):
    __slots__ = ("header", "volume_mount_key", "dir_path", "max_entries", "max_bytes", "stat_file_entries", "cookie", "num_max_concurrent_stats", "prefetch_child_dir_entries", "num_dirs_prefetch_allowed")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    STAT_FILE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    NUM_MAX_CONCURRENT_STATS_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_CHILD_DIR_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRS_PREFETCH_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    volume_mount_key: str
    dir_path: str
    max_entries: int
    max_bytes: int
    stat_file_entries: bool
    cookie: ReadDirCookie
    num_max_concurrent_stats: int
    prefetch_child_dir_entries: bool
    num_dirs_prefetch_allowed: int
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., volume_mount_key: _Optional[str] = ..., dir_path: _Optional[str] = ..., max_entries: _Optional[int] = ..., max_bytes: _Optional[int] = ..., stat_file_entries: bool = ..., cookie: _Optional[_Union[ReadDirCookie, _Mapping]] = ..., num_max_concurrent_stats: _Optional[int] = ..., prefetch_child_dir_entries: bool = ..., num_dirs_prefetch_allowed: _Optional[int] = ...) -> None: ...

class ReadDirResult(_message.Message):
    __slots__ = ("error", "entry_vec", "cookie", "prefetched_child_dir_entry_vec")
    class DirEntry(_message.Message):
        __slots__ = ("type", "name", "fstat_info")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[ReadDirResult.DirEntry.Type]
            kDirectory: _ClassVar[ReadDirResult.DirEntry.Type]
            kSymlink: _ClassVar[ReadDirResult.DirEntry.Type]
            kOther: _ClassVar[ReadDirResult.DirEntry.Type]
        kFile: ReadDirResult.DirEntry.Type
        kDirectory: ReadDirResult.DirEntry.Type
        kSymlink: ReadDirResult.DirEntry.Type
        kOther: ReadDirResult.DirEntry.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FSTAT_INFO_FIELD_NUMBER: _ClassVar[int]
        type: ReadDirResult.DirEntry.Type
        name: bytes
        fstat_info: FileStatInfo
        def __init__(self, type: _Optional[_Union[ReadDirResult.DirEntry.Type, str]] = ..., name: _Optional[bytes] = ..., fstat_info: _Optional[_Union[FileStatInfo, _Mapping]] = ...) -> None: ...
    class ChildDirEntry(_message.Message):
        __slots__ = ("inode_id", "entry_vec", "cookie")
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        inode_id: int
        entry_vec: _containers.RepeatedCompositeFieldContainer[ReadDirResult.DirEntry]
        cookie: ReadDirCookie
        def __init__(self, inode_id: _Optional[int] = ..., entry_vec: _Optional[_Iterable[_Union[ReadDirResult.DirEntry, _Mapping]]] = ..., cookie: _Optional[_Union[ReadDirCookie, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    PREFETCHED_CHILD_DIR_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entry_vec: _containers.RepeatedCompositeFieldContainer[ReadDirResult.DirEntry]
    cookie: ReadDirCookie
    prefetched_child_dir_entry_vec: _containers.RepeatedCompositeFieldContainer[ReadDirResult.ChildDirEntry]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entry_vec: _Optional[_Iterable[_Union[ReadDirResult.DirEntry, _Mapping]]] = ..., cookie: _Optional[_Union[ReadDirCookie, _Mapping]] = ..., prefetched_child_dir_entry_vec: _Optional[_Iterable[_Union[ReadDirResult.ChildDirEntry, _Mapping]]] = ...) -> None: ...

class FileStatArg(_message.Message):
    __slots__ = ("header", "volume_mount_key", "file_path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    volume_mount_key: str
    file_path: bytes
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., volume_mount_key: _Optional[str] = ..., file_path: _Optional[bytes] = ...) -> None: ...

class FileStatResult(_message.Message):
    __slots__ = ("error", "fstat_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FSTAT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    fstat_info: FileStatInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fstat_info: _Optional[_Union[FileStatInfo, _Mapping]] = ...) -> None: ...

class HealthCheckArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class HealthCheckResult(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHealthy: _ClassVar[HealthCheckResult.Status]
        kInitializing: _ClassVar[HealthCheckResult.Status]
        kStuckInCleanup: _ClassVar[HealthCheckResult.Status]
    kHealthy: HealthCheckResult.Status
    kInitializing: HealthCheckResult.Status
    kStuckInCleanup: HealthCheckResult.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: HealthCheckResult.Status
    def __init__(self, status: _Optional[_Union[HealthCheckResult.Status, str]] = ...) -> None: ...

class RemovePathArg(_message.Message):
    __slots__ = ("header", "mount_type", "volume_mount_key", "entity_type", "mails_identifier", "filepath_vec")
    class MountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVmfs: _ClassVar[RemovePathArg.MountType]
        kNFS: _ClassVar[RemovePathArg.MountType]
    kVmfs: RemovePathArg.MountType
    kNFS: RemovePathArg.MountType
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMware: _ClassVar[RemovePathArg.EntityType]
        kNAS: _ClassVar[RemovePathArg.EntityType]
        kO365: _ClassVar[RemovePathArg.EntityType]
        kView: _ClassVar[RemovePathArg.EntityType]
    kVMware: RemovePathArg.EntityType
    kNAS: RemovePathArg.EntityType
    kO365: RemovePathArg.EntityType
    kView: RemovePathArg.EntityType
    class MailsIdentifier(_message.Message):
        __slots__ = ("sparse_outlook_config_directory", "folder_key", "item_key")
        SPARSE_OUTLOOK_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        ITEM_KEY_FIELD_NUMBER: _ClassVar[int]
        sparse_outlook_config_directory: str
        folder_key: str
        item_key: str
        def __init__(self, sparse_outlook_config_directory: _Optional[str] = ..., folder_key: _Optional[str] = ..., item_key: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAILS_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    mount_type: RemovePathArg.MountType
    volume_mount_key: str
    entity_type: RemovePathArg.EntityType
    mails_identifier: _containers.RepeatedCompositeFieldContainer[RemovePathArg.MailsIdentifier]
    filepath_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., mount_type: _Optional[_Union[RemovePathArg.MountType, str]] = ..., volume_mount_key: _Optional[str] = ..., entity_type: _Optional[_Union[RemovePathArg.EntityType, str]] = ..., mails_identifier: _Optional[_Iterable[_Union[RemovePathArg.MailsIdentifier, _Mapping]]] = ..., filepath_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RemovePathResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
