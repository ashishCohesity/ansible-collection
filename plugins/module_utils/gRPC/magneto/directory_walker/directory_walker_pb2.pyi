from magneto.base import enums_pb2 as _enums_pb2
from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityMetadata(_message.Message):
    __slots__ = ("root_dir", "path", "type", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "create_time_usecs", "access_time_usecs", "size", "physical_size", "symlink_target", "num_hardlinks", "major_device_number", "minor_device_number", "inode_id", "smb2_attributes", "first_path_to_hardlink", "extended_attributes", "cifs_xattr", "error", "serialized_metadata", "protocol", "follow_nas_target", "acl_attributes", "owner", "owner_group", "reparse_point_info")
    Extensions: _python_message._ExtensionDict
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[EntityMetadata.EntityType]
        kDirectory: _ClassVar[EntityMetadata.EntityType]
        kBlockDevice: _ClassVar[EntityMetadata.EntityType]
        kCharacterDevice: _ClassVar[EntityMetadata.EntityType]
        kSymLink: _ClassVar[EntityMetadata.EntityType]
        kSocket: _ClassVar[EntityMetadata.EntityType]
        kPipe: _ClassVar[EntityMetadata.EntityType]
    kFile: EntityMetadata.EntityType
    kDirectory: EntityMetadata.EntityType
    kBlockDevice: EntityMetadata.EntityType
    kCharacterDevice: EntityMetadata.EntityType
    kSymLink: EntityMetadata.EntityType
    kSocket: EntityMetadata.EntityType
    kPipe: EntityMetadata.EntityType
    class ExtendedAttribute(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class ACL(_message.Message):
        __slots__ = ("user_or_group", "user_or_group_value", "permission")
        USER_OR_GROUP_FIELD_NUMBER: _ClassVar[int]
        USER_OR_GROUP_VALUE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        user_or_group: str
        user_or_group_value: str
        permission: str
        def __init__(self, user_or_group: _Optional[str] = ..., user_or_group_value: _Optional[str] = ..., permission: _Optional[str] = ...) -> None: ...
    class ReparsePointInfo(_message.Message):
        __slots__ = ("reparse_tag", "symlink_reparse_point_info")
        class SymlinkReparsePointInfo(_message.Message):
            __slots__ = ("substitute_name", "print_name", "is_path_relative")
            SUBSTITUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            PRINT_NAME_FIELD_NUMBER: _ClassVar[int]
            IS_PATH_RELATIVE_FIELD_NUMBER: _ClassVar[int]
            substitute_name: str
            print_name: str
            is_path_relative: bool
            def __init__(self, substitute_name: _Optional[str] = ..., print_name: _Optional[str] = ..., is_path_relative: bool = ...) -> None: ...
        REPARSE_TAG_FIELD_NUMBER: _ClassVar[int]
        SYMLINK_REPARSE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
        reparse_tag: int
        symlink_reparse_point_info: EntityMetadata.ReparsePointInfo.SymlinkReparsePointInfo
        def __init__(self, reparse_tag: _Optional[int] = ..., symlink_reparse_point_info: _Optional[_Union[EntityMetadata.ReparsePointInfo.SymlinkReparsePointInfo, _Mapping]] = ...) -> None: ...
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    NUM_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    SMB2_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FIRST_PATH_TO_HARDLINK_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CIFS_XATTR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_NAS_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    OWNER_GROUP_FIELD_NUMBER: _ClassVar[int]
    REPARSE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    root_dir: bytes
    path: bytes
    type: EntityMetadata.EntityType
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    create_time_usecs: int
    access_time_usecs: int
    size: int
    physical_size: int
    symlink_target: bytes
    num_hardlinks: int
    major_device_number: int
    minor_device_number: int
    inode_id: int
    smb2_attributes: int
    first_path_to_hardlink: bytes
    extended_attributes: _containers.RepeatedCompositeFieldContainer[EntityMetadata.ExtendedAttribute]
    cifs_xattr: bytes
    error: _error_pb2.ErrorProto
    serialized_metadata: bytes
    protocol: _enums_pb2.NasProtocol.Type
    follow_nas_target: bool
    acl_attributes: _containers.RepeatedCompositeFieldContainer[EntityMetadata.ACL]
    owner: str
    owner_group: str
    reparse_point_info: EntityMetadata.ReparsePointInfo
    def __init__(self, root_dir: _Optional[bytes] = ..., path: _Optional[bytes] = ..., type: _Optional[_Union[EntityMetadata.EntityType, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., access_time_usecs: _Optional[int] = ..., size: _Optional[int] = ..., physical_size: _Optional[int] = ..., symlink_target: _Optional[bytes] = ..., num_hardlinks: _Optional[int] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ..., inode_id: _Optional[int] = ..., smb2_attributes: _Optional[int] = ..., first_path_to_hardlink: _Optional[bytes] = ..., extended_attributes: _Optional[_Iterable[_Union[EntityMetadata.ExtendedAttribute, _Mapping]]] = ..., cifs_xattr: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., serialized_metadata: _Optional[bytes] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., follow_nas_target: bool = ..., acl_attributes: _Optional[_Iterable[_Union[EntityMetadata.ACL, _Mapping]]] = ..., owner: _Optional[str] = ..., owner_group: _Optional[str] = ..., reparse_point_info: _Optional[_Union[EntityMetadata.ReparsePointInfo, _Mapping]] = ...) -> None: ...

class SiblingOrderType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLexicographic: _ClassVar[SiblingOrderType.Type]
        kFileFirst: _ClassVar[SiblingOrderType.Type]
    kLexicographic: SiblingOrderType.Type
    kFileFirst: SiblingOrderType.Type
    def __init__(self) -> None: ...

class TraversalType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreOrder: _ClassVar[TraversalType.Type]
        kPostOrder: _ClassVar[TraversalType.Type]
        kLevelOrder: _ClassVar[TraversalType.Type]
    kPreOrder: TraversalType.Type
    kPostOrder: TraversalType.Type
    kLevelOrder: TraversalType.Type
    def __init__(self) -> None: ...

class EntityMDBatchProto(_message.Message):
    __slots__ = ("serialized_entity_vec", "num_directories", "batch_id")
    SERIALIZED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    serialized_entity_vec: _containers.RepeatedScalarFieldContainer[bytes]
    num_directories: int
    batch_id: int
    def __init__(self, serialized_entity_vec: _Optional[_Iterable[bytes]] = ..., num_directories: _Optional[int] = ..., batch_id: _Optional[int] = ...) -> None: ...

class DirWalkerStatsProto(_message.Message):
    __slots__ = ("visit_func_total_pause_time_usecs", "checkpointer_total_pause_time_usecs", "total_fetch_wait_time_msecs", "visit_read_total_wait_time_usecs")
    VISIT_FUNC_TOTAL_PAUSE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTER_TOTAL_PAUSE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FETCH_WAIT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    VISIT_READ_TOTAL_WAIT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    visit_func_total_pause_time_usecs: int
    checkpointer_total_pause_time_usecs: int
    total_fetch_wait_time_msecs: int
    visit_read_total_wait_time_usecs: int
    def __init__(self, visit_func_total_pause_time_usecs: _Optional[int] = ..., checkpointer_total_pause_time_usecs: _Optional[int] = ..., total_fetch_wait_time_msecs: _Optional[int] = ..., visit_read_total_wait_time_usecs: _Optional[int] = ...) -> None: ...
