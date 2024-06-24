from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmbPermission(_message.Message):
    __slots__ = ("type", "mode", "access", "sid", "special_type", "special_access_mask")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAllow: _ClassVar[SmbPermission.Type]
        kDeny: _ClassVar[SmbPermission.Type]
        kSpecialType: _ClassVar[SmbPermission.Type]
    kAllow: SmbPermission.Type
    kDeny: SmbPermission.Type
    kSpecialType: SmbPermission.Type
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFolderSubFoldersAndFiles: _ClassVar[SmbPermission.Mode]
        kFolderAndSubFolders: _ClassVar[SmbPermission.Mode]
        kFolderAndFiles: _ClassVar[SmbPermission.Mode]
        kFolderOnly: _ClassVar[SmbPermission.Mode]
        kSubFoldersAndFilesOnly: _ClassVar[SmbPermission.Mode]
        kSubFoldersOnly: _ClassVar[SmbPermission.Mode]
        kFilesOnly: _ClassVar[SmbPermission.Mode]
    kFolderSubFoldersAndFiles: SmbPermission.Mode
    kFolderAndSubFolders: SmbPermission.Mode
    kFolderAndFiles: SmbPermission.Mode
    kFolderOnly: SmbPermission.Mode
    kSubFoldersAndFilesOnly: SmbPermission.Mode
    kSubFoldersOnly: SmbPermission.Mode
    kFilesOnly: SmbPermission.Mode
    class Access(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadOnly: _ClassVar[SmbPermission.Access]
        kReadWrite: _ClassVar[SmbPermission.Access]
        kFullControl: _ClassVar[SmbPermission.Access]
        kSpecialAccess: _ClassVar[SmbPermission.Access]
        kModify: _ClassVar[SmbPermission.Access]
        kSuperUser: _ClassVar[SmbPermission.Access]
    kReadOnly: SmbPermission.Access
    kReadWrite: SmbPermission.Access
    kFullControl: SmbPermission.Access
    kSpecialAccess: SmbPermission.Access
    kModify: SmbPermission.Access
    kSuperUser: SmbPermission.Access
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
    type: SmbPermission.Type
    mode: SmbPermission.Mode
    access: SmbPermission.Access
    sid: _cluster_config_pb2.ClusterConfigProto.SID
    special_type: int
    special_access_mask: int
    def __init__(self, type: _Optional[_Union[SmbPermission.Type, str]] = ..., mode: _Optional[_Union[SmbPermission.Mode, str]] = ..., access: _Optional[_Union[SmbPermission.Access, str]] = ..., sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., special_type: _Optional[int] = ..., special_access_mask: _Optional[int] = ...) -> None: ...

class ViewSmbPermissionsInfo(_message.Message):
    __slots__ = ("owner_sid", "permissions", "uid", "gid", "mode")
    OWNER_SID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
    permissions: _containers.RepeatedCompositeFieldContainer[SmbPermission]
    uid: int
    gid: int
    mode: int
    def __init__(self, owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[SmbPermission, _Mapping]]] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., mode: _Optional[int] = ...) -> None: ...

class AliasSmbConfig(_message.Message):
    __slots__ = ("discovery_enabled", "encryption_enabled", "encryption_required", "permissions", "caching_enabled", "is_share_level_permission_empty", "oplock_enabled", "continuous_availability", "superusers", "snapshot_acls")
    DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CACHING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SHARE_LEVEL_PERMISSION_EMPTY_FIELD_NUMBER: _ClassVar[int]
    OPLOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SUPERUSERS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ACLS_FIELD_NUMBER: _ClassVar[int]
    discovery_enabled: bool
    encryption_enabled: bool
    encryption_required: bool
    permissions: _containers.RepeatedCompositeFieldContainer[SmbPermission]
    caching_enabled: bool
    is_share_level_permission_empty: bool
    oplock_enabled: bool
    continuous_availability: bool
    superusers: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    snapshot_acls: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, discovery_enabled: bool = ..., encryption_enabled: bool = ..., encryption_required: bool = ..., permissions: _Optional[_Iterable[_Union[SmbPermission, _Mapping]]] = ..., caching_enabled: bool = ..., is_share_level_permission_empty: bool = ..., oplock_enabled: bool = ..., continuous_availability: bool = ..., superusers: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., snapshot_acls: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...
