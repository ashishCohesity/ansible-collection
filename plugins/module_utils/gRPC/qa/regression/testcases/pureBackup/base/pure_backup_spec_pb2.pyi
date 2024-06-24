from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PureCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VolumeSpec(_message.Message):
    __slots__ = ("volume_name", "volume_size")
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    volume_size: str
    def __init__(self, volume_name: _Optional[str] = ..., volume_size: _Optional[str] = ...) -> None: ...

class BackupJobSpec(_message.Message):
    __slots__ = ("job_name", "volume_vec")
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    volume_vec: _containers.RepeatedCompositeFieldContainer[VolumeSpec]
    def __init__(self, job_name: _Optional[str] = ..., volume_vec: _Optional[_Iterable[_Union[VolumeSpec, _Mapping]]] = ...) -> None: ...

class PureArraySpec(_message.Message):
    __slots__ = ("pure_mgmt_ip", "pure_credentials", "backup_job_vec")
    PURE_MGMT_IP_FIELD_NUMBER: _ClassVar[int]
    PURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    pure_mgmt_ip: str
    pure_credentials: PureCredentials
    backup_job_vec: _containers.RepeatedCompositeFieldContainer[BackupJobSpec]
    def __init__(self, pure_mgmt_ip: _Optional[str] = ..., pure_credentials: _Optional[_Union[PureCredentials, _Mapping]] = ..., backup_job_vec: _Optional[_Iterable[_Union[BackupJobSpec, _Mapping]]] = ...) -> None: ...

class PureTestSpec(_message.Message):
    __slots__ = ("pure_array_vec",)
    PURE_ARRAY_VEC_FIELD_NUMBER: _ClassVar[int]
    pure_array_vec: _containers.RepeatedCompositeFieldContainer[PureArraySpec]
    def __init__(self, pure_array_vec: _Optional[_Iterable[_Union[PureArraySpec, _Mapping]]] = ...) -> None: ...
