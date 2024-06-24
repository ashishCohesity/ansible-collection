from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WinVolumeCredentials(_message.Message):
    __slots__ = ("username", "password", "cifs_path", "drive_letter", "persistent_mount", "credential_on", "drive_replicate_letter", "volume_name", "vol_host_ip", "vol_host_port")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CIFS_PATH_FIELD_NUMBER: _ClassVar[int]
    DRIVE_LETTER_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_MOUNT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ON_FIELD_NUMBER: _ClassVar[int]
    DRIVE_REPLICATE_LETTER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_HOST_IP_FIELD_NUMBER: _ClassVar[int]
    VOL_HOST_PORT_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    cifs_path: str
    drive_letter: str
    persistent_mount: str
    credential_on: bool
    drive_replicate_letter: str
    volume_name: str
    vol_host_ip: str
    vol_host_port: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., cifs_path: _Optional[str] = ..., drive_letter: _Optional[str] = ..., persistent_mount: _Optional[str] = ..., credential_on: bool = ..., drive_replicate_letter: _Optional[str] = ..., volume_name: _Optional[str] = ..., vol_host_ip: _Optional[str] = ..., vol_host_port: _Optional[str] = ...) -> None: ...

class ScriptsPath(_message.Message):
    __slots__ = ("vdbench_path", "vdbench_config_file", "filerop_path", "boltdb_path", "boltdb_store_path")
    VDBENCH_PATH_FIELD_NUMBER: _ClassVar[int]
    VDBENCH_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    FILEROP_PATH_FIELD_NUMBER: _ClassVar[int]
    BOLTDB_PATH_FIELD_NUMBER: _ClassVar[int]
    BOLTDB_STORE_PATH_FIELD_NUMBER: _ClassVar[int]
    vdbench_path: str
    vdbench_config_file: str
    filerop_path: str
    boltdb_path: str
    boltdb_store_path: str
    def __init__(self, vdbench_path: _Optional[str] = ..., vdbench_config_file: _Optional[str] = ..., filerop_path: _Optional[str] = ..., boltdb_path: _Optional[str] = ..., boltdb_store_path: _Optional[str] = ...) -> None: ...

class SeverSpec(_message.Message):
    __slots__ = ("host_ip", "win_volume_credentials", "scripts_path")
    HOST_IP_FIELD_NUMBER: _ClassVar[int]
    WIN_VOLUME_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_PATH_FIELD_NUMBER: _ClassVar[int]
    host_ip: str
    win_volume_credentials: _containers.RepeatedCompositeFieldContainer[WinVolumeCredentials]
    scripts_path: _containers.RepeatedCompositeFieldContainer[ScriptsPath]
    def __init__(self, host_ip: _Optional[str] = ..., win_volume_credentials: _Optional[_Iterable[_Union[WinVolumeCredentials, _Mapping]]] = ..., scripts_path: _Optional[_Iterable[_Union[ScriptsPath, _Mapping]]] = ...) -> None: ...

class WinServerArraySpec(_message.Message):
    __slots__ = ("win_array_vec",)
    WIN_ARRAY_VEC_FIELD_NUMBER: _ClassVar[int]
    win_array_vec: _containers.RepeatedCompositeFieldContainer[SeverSpec]
    def __init__(self, win_array_vec: _Optional[_Iterable[_Union[SeverSpec, _Mapping]]] = ...) -> None: ...
