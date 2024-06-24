from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MachineCredentials(_message.Message):
    __slots__ = ("host", "username", "password")
    HOST_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    host: str
    username: str
    password: str
    def __init__(self, host: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class OsEnv(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Linux: _ClassVar[OsEnv.Type]
        Windows: _ClassVar[OsEnv.Type]
    Linux: OsEnv.Type
    Windows: OsEnv.Type
    def __init__(self) -> None: ...

class HostEnv(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VMware: _ClassVar[HostEnv.Type]
        Physical: _ClassVar[HostEnv.Type]
    VMware: HostEnv.Type
    Physical: HostEnv.Type
    def __init__(self) -> None: ...

class RestoreFilesTestInfo(_message.Message):
    __slots__ = ("file_name", "file_path", "is_folder", "restore_original", "restore_base_path", "restore_name", "os_type", "host_type", "host_info", "job_timeout")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    RESTORE_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_path: str
    is_folder: bool
    restore_original: bool
    restore_base_path: str
    restore_name: str
    os_type: OsEnv.Type
    host_type: HostEnv.Type
    host_info: MachineCredentials
    job_timeout: int
    def __init__(self, file_name: _Optional[str] = ..., file_path: _Optional[str] = ..., is_folder: bool = ..., restore_original: bool = ..., restore_base_path: _Optional[str] = ..., restore_name: _Optional[str] = ..., os_type: _Optional[_Union[OsEnv.Type, str]] = ..., host_type: _Optional[_Union[HostEnv.Type, str]] = ..., host_info: _Optional[_Union[MachineCredentials, _Mapping]] = ..., job_timeout: _Optional[int] = ...) -> None: ...
