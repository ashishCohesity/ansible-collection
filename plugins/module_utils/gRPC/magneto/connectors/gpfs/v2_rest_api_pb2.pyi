from magneto.base.entities import gpfs_pb2 as _gpfs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterResponse(_message.Message):
    __slots__ = ("cluster",)
    class Cluster(_message.Message):
        __slots__ = ("cluster_summary",)
        class ClusterSummary(_message.Message):
            __slots__ = ("cluster_id", "cluster_name", "primary_server")
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_SERVER_FIELD_NUMBER: _ClassVar[int]
            cluster_id: int
            cluster_name: str
            primary_server: str
            def __init__(self, cluster_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., primary_server: _Optional[str] = ...) -> None: ...
        CLUSTER_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        cluster_summary: ClusterResponse.Cluster.ClusterSummary
        def __init__(self, cluster_summary: _Optional[_Union[ClusterResponse.Cluster.ClusterSummary, _Mapping]] = ...) -> None: ...
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: ClusterResponse.Cluster
    def __init__(self, cluster: _Optional[_Union[ClusterResponse.Cluster, _Mapping]] = ...) -> None: ...

class CESAddressesResponse(_message.Message):
    __slots__ = ("ces_addresses",)
    class CESAddressDetails(_message.Message):
        __slots__ = ("ces_address", "ces_group", "nodeName")
        CES_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        CES_GROUP_FIELD_NUMBER: _ClassVar[int]
        NODENAME_FIELD_NUMBER: _ClassVar[int]
        ces_address: str
        ces_group: str
        nodeName: str
        def __init__(self, ces_address: _Optional[str] = ..., ces_group: _Optional[str] = ..., nodeName: _Optional[str] = ...) -> None: ...
    CES_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ces_addresses: _containers.RepeatedCompositeFieldContainer[CESAddressesResponse.CESAddressDetails]
    def __init__(self, ces_addresses: _Optional[_Iterable[_Union[CESAddressesResponse.CESAddressDetails, _Mapping]]] = ...) -> None: ...

class FilesystemsResponse(_message.Message):
    __slots__ = ("filesystems",)
    class Filesystem(_message.Message):
        __slots__ = ("uuid", "name", "mount", "block", "settings")
        class MountInfo(_message.Message):
            __slots__ = ("mount_point", "read_only")
            MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
            READ_ONLY_FIELD_NUMBER: _ClassVar[int]
            mount_point: str
            read_only: bool
            def __init__(self, mount_point: _Optional[str] = ..., read_only: bool = ...) -> None: ...
        class BlockInfo(_message.Message):
            __slots__ = ("disks", "block_size", "indirect_block_size", "inode_size", "logfile_size", "meta_data_block_size", "min_fragment_size")
            DISKS_FIELD_NUMBER: _ClassVar[int]
            BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
            INDIRECT_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
            INODE_SIZE_FIELD_NUMBER: _ClassVar[int]
            LOGFILE_SIZE_FIELD_NUMBER: _ClassVar[int]
            META_DATA_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
            MIN_FRAGMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
            disks: str
            block_size: int
            indirect_block_size: int
            inode_size: int
            logfile_size: int
            meta_data_block_size: int
            min_fragment_size: int
            def __init__(self, disks: _Optional[str] = ..., block_size: _Optional[int] = ..., indirect_block_size: _Optional[int] = ..., inode_size: _Optional[int] = ..., logfile_size: _Optional[int] = ..., meta_data_block_size: _Optional[int] = ..., min_fragment_size: _Optional[int] = ...) -> None: ...
        class SettingsInfo(_message.Message):
            __slots__ = ("acl_semantics", "fileLockingSemantics")
            ACL_SEMANTICS_FIELD_NUMBER: _ClassVar[int]
            FILELOCKINGSEMANTICS_FIELD_NUMBER: _ClassVar[int]
            acl_semantics: str
            fileLockingSemantics: str
            def __init__(self, acl_semantics: _Optional[str] = ..., fileLockingSemantics: _Optional[str] = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MOUNT_FIELD_NUMBER: _ClassVar[int]
        BLOCK_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        name: str
        mount: FilesystemsResponse.Filesystem.MountInfo
        block: FilesystemsResponse.Filesystem.BlockInfo
        settings: FilesystemsResponse.Filesystem.SettingsInfo
        def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., mount: _Optional[_Union[FilesystemsResponse.Filesystem.MountInfo, _Mapping]] = ..., block: _Optional[_Union[FilesystemsResponse.Filesystem.BlockInfo, _Mapping]] = ..., settings: _Optional[_Union[FilesystemsResponse.Filesystem.SettingsInfo, _Mapping]] = ...) -> None: ...
    FILESYSTEMS_FIELD_NUMBER: _ClassVar[int]
    filesystems: _containers.RepeatedCompositeFieldContainer[FilesystemsResponse.Filesystem]
    def __init__(self, filesystems: _Optional[_Iterable[_Union[FilesystemsResponse.Filesystem, _Mapping]]] = ...) -> None: ...

class FilesetsResponse(_message.Message):
    __slots__ = ("filesets",)
    class Fileset(_message.Message):
        __slots__ = ("config", "fileset_name", "filesystem_name")
        class Config(_message.Message):
            __slots__ = ("oid", "path", "is_independent_fileset", "id")
            OID_FIELD_NUMBER: _ClassVar[int]
            PATH_FIELD_NUMBER: _ClassVar[int]
            IS_INDEPENDENT_FILESET_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            oid: int
            path: str
            is_independent_fileset: bool
            id: int
            def __init__(self, oid: _Optional[int] = ..., path: _Optional[str] = ..., is_independent_fileset: bool = ..., id: _Optional[int] = ...) -> None: ...
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        FILESET_NAME_FIELD_NUMBER: _ClassVar[int]
        FILESYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
        config: FilesetsResponse.Fileset.Config
        fileset_name: str
        filesystem_name: str
        def __init__(self, config: _Optional[_Union[FilesetsResponse.Fileset.Config, _Mapping]] = ..., fileset_name: _Optional[str] = ..., filesystem_name: _Optional[str] = ...) -> None: ...
    FILESETS_FIELD_NUMBER: _ClassVar[int]
    filesets: _containers.RepeatedCompositeFieldContainer[FilesetsResponse.Fileset]
    def __init__(self, filesets: _Optional[_Iterable[_Union[FilesetsResponse.Fileset, _Mapping]]] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("snapshot_name",)
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    snapshot_name: str
    def __init__(self, snapshot_name: _Optional[str] = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ("jobs",)
    class JobDetails(_message.Message):
        __slots__ = ("job_id",)
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        job_id: int
        def __init__(self, job_id: _Optional[int] = ...) -> None: ...
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[CreateSnapshotResponse.JobDetails]
    def __init__(self, jobs: _Optional[_Iterable[_Union[CreateSnapshotResponse.JobDetails, _Mapping]]] = ...) -> None: ...

class GetSnapshotInfoResponse(_message.Message):
    __slots__ = ("fileset_snapshot_info_vec",)
    FILESET_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    fileset_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[_gpfs_pb2.FilesetSnapshotInfo]
    def __init__(self, fileset_snapshot_info_vec: _Optional[_Iterable[_Union[_gpfs_pb2.FilesetSnapshotInfo, _Mapping]]] = ...) -> None: ...

class AddNfsExportRequest(_message.Message):
    __slots__ = ("path", "nfs_clients")
    PATH_FIELD_NUMBER: _ClassVar[int]
    NFS_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    path: str
    nfs_clients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, path: _Optional[str] = ..., nfs_clients: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateNfsExportRequest(_message.Message):
    __slots__ = ("nfsadd", "nfschange", "nfsremove")
    NFSADD_FIELD_NUMBER: _ClassVar[int]
    NFSCHANGE_FIELD_NUMBER: _ClassVar[int]
    NFSREMOVE_FIELD_NUMBER: _ClassVar[int]
    nfsadd: str
    nfschange: str
    nfsremove: str
    def __init__(self, nfsadd: _Optional[str] = ..., nfschange: _Optional[str] = ..., nfsremove: _Optional[str] = ...) -> None: ...

class NfsExportResponse(_message.Message):
    __slots__ = ("jobs",)
    class JobDetails(_message.Message):
        __slots__ = ("job_id",)
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        job_id: int
        def __init__(self, job_id: _Optional[int] = ...) -> None: ...
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[NfsExportResponse.JobDetails]
    def __init__(self, jobs: _Optional[_Iterable[_Union[NfsExportResponse.JobDetails, _Mapping]]] = ...) -> None: ...

class GetNfsExportResponse(_message.Message):
    __slots__ = ("nfs_exports",)
    class NfsExport(_message.Message):
        __slots__ = ("nfs_clients",)
        class NfsClient(_message.Message):
            __slots__ = ("client_name",)
            CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
            client_name: str
            def __init__(self, client_name: _Optional[str] = ...) -> None: ...
        NFS_CLIENTS_FIELD_NUMBER: _ClassVar[int]
        nfs_clients: _containers.RepeatedCompositeFieldContainer[GetNfsExportResponse.NfsExport.NfsClient]
        def __init__(self, nfs_clients: _Optional[_Iterable[_Union[GetNfsExportResponse.NfsExport.NfsClient, _Mapping]]] = ...) -> None: ...
    NFS_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    nfs_exports: _containers.RepeatedCompositeFieldContainer[GetNfsExportResponse.NfsExport]
    def __init__(self, nfs_exports: _Optional[_Iterable[_Union[GetNfsExportResponse.NfsExport, _Mapping]]] = ...) -> None: ...

class GetJobInfoRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    def __init__(self, job_id: _Optional[int] = ...) -> None: ...

class GetJobInfoResponse(_message.Message):
    __slots__ = ("jobs",)
    class JobDetails(_message.Message):
        __slots__ = ("status", "result")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RUNNING: _ClassVar[GetJobInfoResponse.JobDetails.Status]
            COMPLETED: _ClassVar[GetJobInfoResponse.JobDetails.Status]
            FAILED: _ClassVar[GetJobInfoResponse.JobDetails.Status]
        RUNNING: GetJobInfoResponse.JobDetails.Status
        COMPLETED: GetJobInfoResponse.JobDetails.Status
        FAILED: GetJobInfoResponse.JobDetails.Status
        class Result(_message.Message):
            __slots__ = ("stdout", "stderr")
            STDOUT_FIELD_NUMBER: _ClassVar[int]
            STDERR_FIELD_NUMBER: _ClassVar[int]
            stdout: _containers.RepeatedScalarFieldContainer[str]
            stderr: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, stdout: _Optional[_Iterable[str]] = ..., stderr: _Optional[_Iterable[str]] = ...) -> None: ...
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        status: GetJobInfoResponse.JobDetails.Status
        result: GetJobInfoResponse.JobDetails.Result
        def __init__(self, status: _Optional[_Union[GetJobInfoResponse.JobDetails.Status, str]] = ..., result: _Optional[_Union[GetJobInfoResponse.JobDetails.Result, _Mapping]] = ...) -> None: ...
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[GetJobInfoResponse.JobDetails]
    def __init__(self, jobs: _Optional[_Iterable[_Union[GetJobInfoResponse.JobDetails, _Mapping]]] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("status",)
    class Status(_message.Message):
        __slots__ = ("code", "msg")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MSG_FIELD_NUMBER: _ClassVar[int]
        code: int
        msg: str
        def __init__(self, code: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ErrorContext.Status
    def __init__(self, status: _Optional[_Union[ErrorContext.Status, _Mapping]] = ...) -> None: ...
