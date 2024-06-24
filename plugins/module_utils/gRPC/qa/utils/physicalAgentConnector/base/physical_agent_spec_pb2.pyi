from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FsCheckerBinaryUrl(_message.Message):
    __slots__ = ("windows_url", "windows_rpc_url", "linux_url")
    WINDOWS_URL_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_RPC_URL_FIELD_NUMBER: _ClassVar[int]
    LINUX_URL_FIELD_NUMBER: _ClassVar[int]
    windows_url: str
    windows_rpc_url: str
    linux_url: str
    def __init__(self, windows_url: _Optional[str] = ..., windows_rpc_url: _Optional[str] = ..., linux_url: _Optional[str] = ...) -> None: ...

class WindowsCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LinuxCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RestoreFilesToSourceTestInfo(_message.Message):
    __slots__ = ("file_name", "file_path", "win_file_path", "is_folder", "restore_base_path", "win_restore_base_path")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    WIN_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    WIN_RESTORE_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_path: str
    win_file_path: str
    is_folder: bool
    restore_base_path: str
    win_restore_base_path: str
    def __init__(self, file_name: _Optional[str] = ..., file_path: _Optional[str] = ..., win_file_path: _Optional[str] = ..., is_folder: bool = ..., restore_base_path: _Optional[str] = ..., win_restore_base_path: _Optional[str] = ...) -> None: ...

class DownloadFilesTestInfo(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class BrowseFilesTestInfo(_message.Message):
    __slots__ = ("vol_name", "file_path")
    VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    vol_name: str
    file_path: str
    def __init__(self, vol_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class PhysicalHost(_message.Message):
    __slots__ = ("host_type", "host_name", "description", "backup_mount_points", "download_files_test_data", "restore_files_to_src_test_data", "browse_files_test_data")
    class HostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WINDOWS: _ClassVar[PhysicalHost.HostType]
        LINUX: _ClassVar[PhysicalHost.HostType]
    WINDOWS: PhysicalHost.HostType
    LINUX: PhysicalHost.HostType
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_MOUNT_POINTS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILES_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_TO_SRC_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    BROWSE_FILES_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    host_type: PhysicalHost.HostType
    host_name: str
    description: str
    backup_mount_points: _containers.RepeatedScalarFieldContainer[str]
    download_files_test_data: _containers.RepeatedCompositeFieldContainer[DownloadFilesTestInfo]
    restore_files_to_src_test_data: _containers.RepeatedCompositeFieldContainer[RestoreFilesToSourceTestInfo]
    browse_files_test_data: _containers.RepeatedCompositeFieldContainer[BrowseFilesTestInfo]
    def __init__(self, host_type: _Optional[_Union[PhysicalHost.HostType, str]] = ..., host_name: _Optional[str] = ..., description: _Optional[str] = ..., backup_mount_points: _Optional[_Iterable[str]] = ..., download_files_test_data: _Optional[_Iterable[_Union[DownloadFilesTestInfo, _Mapping]]] = ..., restore_files_to_src_test_data: _Optional[_Iterable[_Union[RestoreFilesToSourceTestInfo, _Mapping]]] = ..., browse_files_test_data: _Optional[_Iterable[_Union[BrowseFilesTestInfo, _Mapping]]] = ...) -> None: ...

class TestServers(_message.Message):
    __slots__ = ("fs_checker_binary_url", "windows_credentials", "linux_credentials", "physical_servers_vec")
    FS_CHECKER_BINARY_URL_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    LINUX_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SERVERS_VEC_FIELD_NUMBER: _ClassVar[int]
    fs_checker_binary_url: FsCheckerBinaryUrl
    windows_credentials: WindowsCredentials
    linux_credentials: LinuxCredentials
    physical_servers_vec: _containers.RepeatedCompositeFieldContainer[PhysicalHost]
    def __init__(self, fs_checker_binary_url: _Optional[_Union[FsCheckerBinaryUrl, _Mapping]] = ..., windows_credentials: _Optional[_Union[WindowsCredentials, _Mapping]] = ..., linux_credentials: _Optional[_Union[LinuxCredentials, _Mapping]] = ..., physical_servers_vec: _Optional[_Iterable[_Union[PhysicalHost, _Mapping]]] = ...) -> None: ...
