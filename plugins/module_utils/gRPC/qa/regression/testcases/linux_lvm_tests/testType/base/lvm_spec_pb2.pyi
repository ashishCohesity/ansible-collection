from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinuxCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DownloadFilesTestInfo(_message.Message):
    __slots__ = ("file_name", "md5sum")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MD5SUM_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    md5sum: str
    def __init__(self, file_name: _Optional[str] = ..., md5sum: _Optional[str] = ...) -> None: ...

class BrowseFilesTestInfo(_message.Message):
    __slots__ = ("vol_name", "file_path")
    VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    vol_name: str
    file_path: str
    def __init__(self, vol_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class LinuxHost(_message.Message):
    __slots__ = ("host_name", "moref", "backup_mount_points", "download_files_test_data", "browse_files_test_data")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    MOREF_FIELD_NUMBER: _ClassVar[int]
    BACKUP_MOUNT_POINTS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILES_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    BROWSE_FILES_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    moref: str
    backup_mount_points: _containers.RepeatedScalarFieldContainer[str]
    download_files_test_data: _containers.RepeatedCompositeFieldContainer[DownloadFilesTestInfo]
    browse_files_test_data: _containers.RepeatedCompositeFieldContainer[BrowseFilesTestInfo]
    def __init__(self, host_name: _Optional[str] = ..., moref: _Optional[str] = ..., backup_mount_points: _Optional[_Iterable[str]] = ..., download_files_test_data: _Optional[_Iterable[_Union[DownloadFilesTestInfo, _Mapping]]] = ..., browse_files_test_data: _Optional[_Iterable[_Union[BrowseFilesTestInfo, _Mapping]]] = ...) -> None: ...

class TestServers(_message.Message):
    __slots__ = ("linux_credentials", "lvm_servers_vec")
    LINUX_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    LVM_SERVERS_VEC_FIELD_NUMBER: _ClassVar[int]
    linux_credentials: LinuxCredentials
    lvm_servers_vec: _containers.RepeatedCompositeFieldContainer[LinuxHost]
    def __init__(self, linux_credentials: _Optional[_Union[LinuxCredentials, _Mapping]] = ..., lvm_servers_vec: _Optional[_Iterable[_Union[LinuxHost, _Mapping]]] = ...) -> None: ...
