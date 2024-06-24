from magneto.base.entities import gpfs_pb2 as _gpfs_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSnapshotArg(_message.Message):
    __slots__ = ("filesystem", "fileset", "snapshot_name")
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    FILESET_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    filesystem: str
    fileset: str
    snapshot_name: str
    def __init__(self, filesystem: _Optional[str] = ..., fileset: _Optional[str] = ..., snapshot_name: _Optional[str] = ...) -> None: ...

class CreateSnapshotResult(_message.Message):
    __slots__ = ("fileset_snapshot_info",)
    FILESET_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    fileset_snapshot_info: _gpfs_pb2.FilesetSnapshotInfo
    def __init__(self, fileset_snapshot_info: _Optional[_Union[_gpfs_pb2.FilesetSnapshotInfo, _Mapping]] = ...) -> None: ...

class SnapshotArg(_message.Message):
    __slots__ = ("filesystem", "fileset", "snapshot_name")
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    FILESET_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    filesystem: str
    fileset: str
    snapshot_name: str
    def __init__(self, filesystem: _Optional[str] = ..., fileset: _Optional[str] = ..., snapshot_name: _Optional[str] = ...) -> None: ...

class DeleteSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryEntityHierarchyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryEntityHierarchyResult(_message.Message):
    __slots__ = ("entity_hierarchy",)
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class FetchIpAddressesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchIpAddressesResult(_message.Message):
    __slots__ = ("ip_addrs",)
    IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip_addrs: _Optional[_Iterable[str]] = ...) -> None: ...

class NfsExportArg(_message.Message):
    __slots__ = ("path", "nfs_clients_str")
    PATH_FIELD_NUMBER: _ClassVar[int]
    NFS_CLIENTS_STR_FIELD_NUMBER: _ClassVar[int]
    path: str
    nfs_clients_str: str
    def __init__(self, path: _Optional[str] = ..., nfs_clients_str: _Optional[str] = ...) -> None: ...

class NfsExportResult(_message.Message):
    __slots__ = ("job_id", "nfs_clients")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    NFS_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    nfs_clients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, job_id: _Optional[int] = ..., nfs_clients: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateNfsExportArg(_message.Message):
    __slots__ = ("path", "nfsadd", "nfsremove", "nfschange")
    PATH_FIELD_NUMBER: _ClassVar[int]
    NFSADD_FIELD_NUMBER: _ClassVar[int]
    NFSREMOVE_FIELD_NUMBER: _ClassVar[int]
    NFSCHANGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    nfsadd: str
    nfsremove: str
    nfschange: str
    def __init__(self, path: _Optional[str] = ..., nfsadd: _Optional[str] = ..., nfsremove: _Optional[str] = ..., nfschange: _Optional[str] = ...) -> None: ...

class GetJobInfoArg(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    def __init__(self, job_id: _Optional[int] = ...) -> None: ...

class GetJobInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
