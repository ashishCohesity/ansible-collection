from magneto.base.entities import flashblade_pb2 as _flashblade_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryEntityHierarchyArg(_message.Message):
    __slots__ = ("smb_domain_name",)
    SMB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    smb_domain_name: str
    def __init__(self, smb_domain_name: _Optional[str] = ...) -> None: ...

class QueryEntityHierarchyResult(_message.Message):
    __slots__ = ("entity_hierarchy",)
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class GetFilesystemArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetFilesystemResult(_message.Message):
    __slots__ = ("file_system",)
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    file_system: _flashblade_pb2.FileSystemInfo
    def __init__(self, file_system: _Optional[_Union[_flashblade_pb2.FileSystemInfo, _Mapping]] = ...) -> None: ...

class UpdateFilesystemArg(_message.Message):
    __slots__ = ("name", "nfs_export_rules")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORT_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    nfs_export_rules: str
    def __init__(self, name: _Optional[str] = ..., nfs_export_rules: _Optional[str] = ...) -> None: ...

class UpdateFilesystemResult(_message.Message):
    __slots__ = ("file_system",)
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    file_system: _flashblade_pb2.FileSystemInfo
    def __init__(self, file_system: _Optional[_Union[_flashblade_pb2.FileSystemInfo, _Mapping]] = ...) -> None: ...

class CreateSnapshotArg(_message.Message):
    __slots__ = ("source", "snapshot_suffix")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    source: str
    snapshot_suffix: str
    def __init__(self, source: _Optional[str] = ..., snapshot_suffix: _Optional[str] = ...) -> None: ...

class CreateSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: GetSnapshotInfoResult
    def __init__(self, snapshot_info: _Optional[_Union[GetSnapshotInfoResult, _Mapping]] = ...) -> None: ...

class GetSnapshotInfoArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSnapshotInfoResult(_message.Message):
    __slots__ = ("name", "source", "creation_time_msecs", "destroyed", "time_remaining_msecs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DESTROYED_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_MSECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source: str
    creation_time_msecs: int
    destroyed: bool
    time_remaining_msecs: int
    def __init__(self, name: _Optional[str] = ..., source: _Optional[str] = ..., creation_time_msecs: _Optional[int] = ..., destroyed: bool = ..., time_remaining_msecs: _Optional[int] = ...) -> None: ...

class DeleteSnapshotArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshSessionArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshSessionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
