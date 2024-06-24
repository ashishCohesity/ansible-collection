from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VcenterBackupSource(_message.Message):
    __slots__ = ("host", "username", "password")
    HOST_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    host: str
    username: str
    password: str
    def __init__(self, host: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VmBackupInfo(_message.Message):
    __slots__ = ("job_name", "view_box_name", "vc_backup_source", "vm_morefs", "job_policy_id", "indexing", "job_timeout")
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VC_BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VM_MOREFS_FIELD_NUMBER: _ClassVar[int]
    JOB_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    INDEXING_FIELD_NUMBER: _ClassVar[int]
    JOB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    view_box_name: str
    vc_backup_source: VcenterBackupSource
    vm_morefs: _containers.RepeatedScalarFieldContainer[str]
    job_policy_id: str
    indexing: bool
    job_timeout: int
    def __init__(self, job_name: _Optional[str] = ..., view_box_name: _Optional[str] = ..., vc_backup_source: _Optional[_Union[VcenterBackupSource, _Mapping]] = ..., vm_morefs: _Optional[_Iterable[str]] = ..., job_policy_id: _Optional[str] = ..., indexing: bool = ..., job_timeout: _Optional[int] = ...) -> None: ...
