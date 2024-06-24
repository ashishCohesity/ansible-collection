from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParamsProto(_message.Message):
    __slots__ = ("cluster_ips", "cluster_port", "view_name", "io_thread_count", "max_io_size_bytes", "rpc_timeout_msecs", "certificate_config_path", "vip_selection_type", "job_type", "pipe_list", "report_progress_interval_ms", "transferred_bytes_path", "use_secure_grpc", "enable_dedup_write", "enable_dedup_read", "enable_read_forwarding", "enable_write_forwarding", "max_snap_fs_io_operations", "max_pipe_io_operations", "max_streams", "listing_file")
    class VIPSelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kConsistentHash: _ClassVar[ParamsProto.VIPSelectionType]
        kRoundRobin: _ClassVar[ParamsProto.VIPSelectionType]
        kLeastConnections: _ClassVar[ParamsProto.VIPSelectionType]
        kMixedMode: _ClassVar[ParamsProto.VIPSelectionType]
    kConsistentHash: ParamsProto.VIPSelectionType
    kRoundRobin: ParamsProto.VIPSelectionType
    kLeastConnections: ParamsProto.VIPSelectionType
    kMixedMode: ParamsProto.VIPSelectionType
    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFullBackup: _ClassVar[ParamsProto.JobType]
        kIncrementalBackup: _ClassVar[ParamsProto.JobType]
        kLogBackup: _ClassVar[ParamsProto.JobType]
        kRestore: _ClassVar[ParamsProto.JobType]
        kPITR: _ClassVar[ParamsProto.JobType]
    kFullBackup: ParamsProto.JobType
    kIncrementalBackup: ParamsProto.JobType
    kLogBackup: ParamsProto.JobType
    kRestore: ParamsProto.JobType
    kPITR: ParamsProto.JobType
    CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PORT_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_IO_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RPC_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    VIP_SELECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPE_LIST_FIELD_NUMBER: _ClassVar[int]
    REPORT_PROGRESS_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_BYTES_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_SECURE_GRPC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEDUP_WRITE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEDUP_READ_FIELD_NUMBER: _ClassVar[int]
    ENABLE_READ_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WRITE_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    MAX_SNAP_FS_IO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_PIPE_IO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_STREAMS_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    cluster_ips: str
    cluster_port: int
    view_name: str
    io_thread_count: int
    max_io_size_bytes: int
    rpc_timeout_msecs: int
    certificate_config_path: str
    vip_selection_type: ParamsProto.VIPSelectionType
    job_type: ParamsProto.JobType
    pipe_list: str
    report_progress_interval_ms: int
    transferred_bytes_path: str
    use_secure_grpc: bool
    enable_dedup_write: bool
    enable_dedup_read: bool
    enable_read_forwarding: bool
    enable_write_forwarding: bool
    max_snap_fs_io_operations: int
    max_pipe_io_operations: int
    max_streams: int
    listing_file: str
    def __init__(self, cluster_ips: _Optional[str] = ..., cluster_port: _Optional[int] = ..., view_name: _Optional[str] = ..., io_thread_count: _Optional[int] = ..., max_io_size_bytes: _Optional[int] = ..., rpc_timeout_msecs: _Optional[int] = ..., certificate_config_path: _Optional[str] = ..., vip_selection_type: _Optional[_Union[ParamsProto.VIPSelectionType, str]] = ..., job_type: _Optional[_Union[ParamsProto.JobType, str]] = ..., pipe_list: _Optional[str] = ..., report_progress_interval_ms: _Optional[int] = ..., transferred_bytes_path: _Optional[str] = ..., use_secure_grpc: bool = ..., enable_dedup_write: bool = ..., enable_dedup_read: bool = ..., enable_read_forwarding: bool = ..., enable_write_forwarding: bool = ..., max_snap_fs_io_operations: _Optional[int] = ..., max_pipe_io_operations: _Optional[int] = ..., max_streams: _Optional[int] = ..., listing_file: _Optional[str] = ...) -> None: ...

class CertificateProto(_message.Message):
    __slots__ = ("connection_config_vec",)
    class ConnectionConfig(_message.Message):
        __slots__ = ("cluster_cert", "self_cert", "self_cert_priv_key_encrypted", "tenant_id", "cluster_id", "grpc_server_common_name")
        CLUSTER_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_PRIV_KEY_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        GRPC_SERVER_COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_cert: str
        self_cert: str
        self_cert_priv_key_encrypted: bytes
        tenant_id: str
        cluster_id: int
        grpc_server_common_name: str
        def __init__(self, cluster_cert: _Optional[str] = ..., self_cert: _Optional[str] = ..., self_cert_priv_key_encrypted: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., cluster_id: _Optional[int] = ..., grpc_server_common_name: _Optional[str] = ...) -> None: ...
    CONNECTION_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    connection_config_vec: _containers.RepeatedCompositeFieldContainer[CertificateProto.ConnectionConfig]
    def __init__(self, connection_config_vec: _Optional[_Iterable[_Union[CertificateProto.ConnectionConfig, _Mapping]]] = ...) -> None: ...
