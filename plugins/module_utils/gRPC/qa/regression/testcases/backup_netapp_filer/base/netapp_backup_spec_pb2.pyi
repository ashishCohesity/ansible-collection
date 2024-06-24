from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetappCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VolumeSpec(_message.Message):
    __slots__ = ("vserver_name", "volume_size", "volume_name", "vserver_ip")
    VSERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    VSERVER_IP_FIELD_NUMBER: _ClassVar[int]
    vserver_name: str
    volume_size: str
    volume_name: _containers.RepeatedScalarFieldContainer[str]
    vserver_ip: str
    def __init__(self, vserver_name: _Optional[str] = ..., volume_size: _Optional[str] = ..., volume_name: _Optional[_Iterable[str]] = ..., vserver_ip: _Optional[str] = ...) -> None: ...

class BackupJobSpec(_message.Message):
    __slots__ = ("job_name", "viewbox_name", "volume_vec", "policy_name", "recover_name", "recover_view_name_prefix")
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    RECOVER_NAME_FIELD_NUMBER: _ClassVar[int]
    RECOVER_VIEW_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    viewbox_name: str
    volume_vec: VolumeSpec
    policy_name: str
    recover_name: str
    recover_view_name_prefix: str
    def __init__(self, job_name: _Optional[str] = ..., viewbox_name: _Optional[str] = ..., volume_vec: _Optional[_Union[VolumeSpec, _Mapping]] = ..., policy_name: _Optional[str] = ..., recover_name: _Optional[str] = ..., recover_view_name_prefix: _Optional[str] = ...) -> None: ...

class NetappArraySpec(_message.Message):
    __slots__ = ("netapp_mgmt_ip", "netapp_credentials_vec", "backup_job_vec", "netapp_name")
    NETAPP_MGMT_IP_FIELD_NUMBER: _ClassVar[int]
    NETAPP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    NETAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    netapp_mgmt_ip: str
    netapp_credentials_vec: _containers.RepeatedCompositeFieldContainer[NetappCredentials]
    backup_job_vec: _containers.RepeatedCompositeFieldContainer[BackupJobSpec]
    netapp_name: str
    def __init__(self, netapp_mgmt_ip: _Optional[str] = ..., netapp_credentials_vec: _Optional[_Iterable[_Union[NetappCredentials, _Mapping]]] = ..., backup_job_vec: _Optional[_Iterable[_Union[BackupJobSpec, _Mapping]]] = ..., netapp_name: _Optional[str] = ...) -> None: ...

class NetappTestSpec(_message.Message):
    __slots__ = ("netapp_array_vec",)
    NETAPP_ARRAY_VEC_FIELD_NUMBER: _ClassVar[int]
    netapp_array_vec: _containers.RepeatedCompositeFieldContainer[NetappArraySpec]
    def __init__(self, netapp_array_vec: _Optional[_Iterable[_Union[NetappArraySpec, _Mapping]]] = ...) -> None: ...
