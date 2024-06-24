from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorContext(_message.Message):
    __slots__ = ("code", "message", "context", "msg")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    context: str
    msg: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., context: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class ErrorContextVec(_message.Message):
    __slots__ = ("error_ctx_vec", "errors_ctx_vec")
    ERROR_CTX_VEC_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CTX_VEC_FIELD_NUMBER: _ClassVar[int]
    error_ctx_vec: _containers.RepeatedCompositeFieldContainer[ErrorContext]
    errors_ctx_vec: _containers.RepeatedCompositeFieldContainer[ErrorContext]
    def __init__(self, error_ctx_vec: _Optional[_Iterable[_Union[ErrorContext, _Mapping]]] = ..., errors_ctx_vec: _Optional[_Iterable[_Union[ErrorContext, _Mapping]]] = ...) -> None: ...

class PaginationInfo(_message.Message):
    __slots__ = ("total_item_count", "continuation_token")
    TOTAL_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    total_item_count: int
    continuation_token: str
    def __init__(self, total_item_count: _Optional[int] = ..., continuation_token: _Optional[str] = ...) -> None: ...

class ArraySpaceStats(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FileSystemSpaceStats(_message.Message):
    __slots__ = ("total_physical_usage_in_bytes", "unique_usage_in_bytes", "logical_usage_in_bytes")
    TOTAL_PHYSICAL_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_physical_usage_in_bytes: int
    unique_usage_in_bytes: int
    logical_usage_in_bytes: int
    def __init__(self, total_physical_usage_in_bytes: _Optional[int] = ..., unique_usage_in_bytes: _Optional[int] = ..., logical_usage_in_bytes: _Optional[int] = ...) -> None: ...

class NFSRule(_message.Message):
    __slots__ = ("enabled", "export_rules")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RULES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    export_rules: str
    def __init__(self, enabled: bool = ..., export_rules: _Optional[str] = ...) -> None: ...

class SMBRule(_message.Message):
    __slots__ = ("enabled", "acl_mode")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACL_MODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    acl_mode: str
    def __init__(self, enabled: bool = ..., acl_mode: _Optional[str] = ...) -> None: ...

class HTTPRule(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class Array(_message.Message):
    __slots__ = ("name", "id", "revision", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    revision: str
    version: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., revision: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ActiveDirectory(_message.Message):
    __slots__ = ("computer_name", "domain")
    COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    computer_name: str
    domain: str
    def __init__(self, computer_name: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class ActiveDirectoryResponse(_message.Message):
    __slots__ = ("pagination_info", "active_directory_vec")
    PAGINATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_VEC_FIELD_NUMBER: _ClassVar[int]
    pagination_info: PaginationInfo
    active_directory_vec: _containers.RepeatedCompositeFieldContainer[ActiveDirectory]
    def __init__(self, pagination_info: _Optional[_Union[PaginationInfo, _Mapping]] = ..., active_directory_vec: _Optional[_Iterable[_Union[ActiveDirectory, _Mapping]]] = ...) -> None: ...

class DirectoryService(_message.Message):
    __slots__ = ("name", "services", "enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    services: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, name: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class DirectoryServiceResponse(_message.Message):
    __slots__ = ("pagination_info", "directory_services_vec")
    PAGINATION_INFO_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
    pagination_info: PaginationInfo
    directory_services_vec: _containers.RepeatedCompositeFieldContainer[DirectoryService]
    def __init__(self, pagination_info: _Optional[_Union[PaginationInfo, _Mapping]] = ..., directory_services_vec: _Optional[_Iterable[_Union[DirectoryService, _Mapping]]] = ...) -> None: ...

class FileSystem(_message.Message):
    __slots__ = ("name", "creation_time_msecs", "logical_capacity_bytes", "snapshot_dir_enabled", "destroyed", "nfs_rule", "smb_rule", "http_rule", "space")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DESTROYED_FIELD_NUMBER: _ClassVar[int]
    NFS_RULE_FIELD_NUMBER: _ClassVar[int]
    SMB_RULE_FIELD_NUMBER: _ClassVar[int]
    HTTP_RULE_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    creation_time_msecs: int
    logical_capacity_bytes: int
    snapshot_dir_enabled: bool
    destroyed: bool
    nfs_rule: NFSRule
    smb_rule: SMBRule
    http_rule: HTTPRule
    space: FileSystemSpaceStats
    def __init__(self, name: _Optional[str] = ..., creation_time_msecs: _Optional[int] = ..., logical_capacity_bytes: _Optional[int] = ..., snapshot_dir_enabled: bool = ..., destroyed: bool = ..., nfs_rule: _Optional[_Union[NFSRule, _Mapping]] = ..., smb_rule: _Optional[_Union[SMBRule, _Mapping]] = ..., http_rule: _Optional[_Union[HTTPRule, _Mapping]] = ..., space: _Optional[_Union[FileSystemSpaceStats, _Mapping]] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class ListAPIVersionsResponse(_message.Message):
    __slots__ = ("versions",)
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, versions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetArrayResponse(_message.Message):
    __slots__ = ("array_vec",)
    ARRAY_VEC_FIELD_NUMBER: _ClassVar[int]
    array_vec: _containers.RepeatedCompositeFieldContainer[Array]
    def __init__(self, array_vec: _Optional[_Iterable[_Union[Array, _Mapping]]] = ...) -> None: ...

class NetworkInterface(_message.Message):
    __slots__ = ("ip_address", "enabled", "name", "service_vec", "vlan_id")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    enabled: bool
    name: str
    service_vec: _containers.RepeatedScalarFieldContainer[str]
    vlan_id: int
    def __init__(self, ip_address: _Optional[str] = ..., enabled: bool = ..., name: _Optional[str] = ..., service_vec: _Optional[_Iterable[str]] = ..., vlan_id: _Optional[int] = ...) -> None: ...

class GetNetworksResponse(_message.Message):
    __slots__ = ("pagination_info", "network_vec")
    PAGINATION_INFO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    pagination_info: PaginationInfo
    network_vec: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    def __init__(self, pagination_info: _Optional[_Union[PaginationInfo, _Mapping]] = ..., network_vec: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]] = ...) -> None: ...

class GetFileSystemsResponse(_message.Message):
    __slots__ = ("pagination_info", "file_system_vec")
    PAGINATION_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_VEC_FIELD_NUMBER: _ClassVar[int]
    pagination_info: PaginationInfo
    file_system_vec: _containers.RepeatedCompositeFieldContainer[FileSystem]
    def __init__(self, pagination_info: _Optional[_Union[PaginationInfo, _Mapping]] = ..., file_system_vec: _Optional[_Iterable[_Union[FileSystem, _Mapping]]] = ...) -> None: ...

class UpdateFileSystemsRequest(_message.Message):
    __slots__ = ("nfs_rule",)
    NFS_RULE_FIELD_NUMBER: _ClassVar[int]
    nfs_rule: NFSRule
    def __init__(self, nfs_rule: _Optional[_Union[NFSRule, _Mapping]] = ...) -> None: ...

class UpdateFileSystemsResponse(_message.Message):
    __slots__ = ("file_system_vec",)
    FILE_SYSTEM_VEC_FIELD_NUMBER: _ClassVar[int]
    file_system_vec: _containers.RepeatedCompositeFieldContainer[FileSystem]
    def __init__(self, file_system_vec: _Optional[_Iterable[_Union[FileSystem, _Mapping]]] = ...) -> None: ...

class FileSystemSnapshot(_message.Message):
    __slots__ = ("creation_time_msecs", "destroyed", "name", "source", "suffix", "source_destroyed", "time_remaining_msecs")
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DESTROYED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESTROYED_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_MSECS_FIELD_NUMBER: _ClassVar[int]
    creation_time_msecs: int
    destroyed: bool
    name: str
    source: str
    suffix: str
    source_destroyed: bool
    time_remaining_msecs: int
    def __init__(self, creation_time_msecs: _Optional[int] = ..., destroyed: bool = ..., name: _Optional[str] = ..., source: _Optional[str] = ..., suffix: _Optional[str] = ..., source_destroyed: bool = ..., time_remaining_msecs: _Optional[int] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("suffix",)
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    def __init__(self, suffix: _Optional[str] = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ("file_system_snapshot_vec",)
    FILE_SYSTEM_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    file_system_snapshot_vec: _containers.RepeatedCompositeFieldContainer[FileSystemSnapshot]
    def __init__(self, file_system_snapshot_vec: _Optional[_Iterable[_Union[FileSystemSnapshot, _Mapping]]] = ...) -> None: ...

class GetSnapshotsResponse(_message.Message):
    __slots__ = ("file_system_snapshot_vec",)
    FILE_SYSTEM_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    file_system_snapshot_vec: _containers.RepeatedCompositeFieldContainer[FileSystemSnapshot]
    def __init__(self, file_system_snapshot_vec: _Optional[_Iterable[_Union[FileSystemSnapshot, _Mapping]]] = ...) -> None: ...

class UpdateSnapshotRequest(_message.Message):
    __slots__ = ("destroyed",)
    DESTROYED_FIELD_NUMBER: _ClassVar[int]
    destroyed: bool
    def __init__(self, destroyed: bool = ...) -> None: ...
