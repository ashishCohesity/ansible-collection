from magneto.connectors.ms_graph import graph_enums_pb2 as _graph_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365AddSnapshotArg(_message.Message):
    __slots__ = ("outlook_info", "one_drive_info_vec", "sharepoint_info", "public_folder_info", "teams_info", "group_info")
    class OutlookInfo(_message.Message):
        __slots__ = ("should_index_outlook",)
        SHOULD_INDEX_OUTLOOK_FIELD_NUMBER: _ClassVar[int]
        should_index_outlook: bool
        def __init__(self, should_index_outlook: bool = ...) -> None: ...
    class OneDriveInfo(_message.Message):
        __slots__ = ("should_index_one_drive", "path_to_index", "path_to_db", "drive_id", "incremental_indexing_enabled", "drive_type")
        SHOULD_INDEX_ONE_DRIVE_FIELD_NUMBER: _ClassVar[int]
        PATH_TO_INDEX_FIELD_NUMBER: _ClassVar[int]
        PATH_TO_DB_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_INDEXING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        should_index_one_drive: bool
        path_to_index: str
        path_to_db: str
        drive_id: str
        incremental_indexing_enabled: bool
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, should_index_one_drive: bool = ..., path_to_index: _Optional[str] = ..., path_to_db: _Optional[str] = ..., drive_id: _Optional[str] = ..., incremental_indexing_enabled: bool = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    class SharepointInfo(_message.Message):
        __slots__ = ("should_index_lists",)
        SHOULD_INDEX_LISTS_FIELD_NUMBER: _ClassVar[int]
        should_index_lists: bool
        def __init__(self, should_index_lists: bool = ...) -> None: ...
    class PublicFolderInfo(_message.Message):
        __slots__ = ("hierarchy_db_folder_name",)
        HIERARCHY_DB_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
        hierarchy_db_folder_name: str
        def __init__(self, hierarchy_db_folder_name: _Optional[str] = ...) -> None: ...
    class TeamsInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GroupInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    OUTLOOK_INFO_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_INFO_FIELD_NUMBER: _ClassVar[int]
    TEAMS_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_info: O365AddSnapshotArg.OutlookInfo
    one_drive_info_vec: _containers.RepeatedCompositeFieldContainer[O365AddSnapshotArg.OneDriveInfo]
    sharepoint_info: O365AddSnapshotArg.SharepointInfo
    public_folder_info: O365AddSnapshotArg.PublicFolderInfo
    teams_info: O365AddSnapshotArg.TeamsInfo
    group_info: O365AddSnapshotArg.GroupInfo
    def __init__(self, outlook_info: _Optional[_Union[O365AddSnapshotArg.OutlookInfo, _Mapping]] = ..., one_drive_info_vec: _Optional[_Iterable[_Union[O365AddSnapshotArg.OneDriveInfo, _Mapping]]] = ..., sharepoint_info: _Optional[_Union[O365AddSnapshotArg.SharepointInfo, _Mapping]] = ..., public_folder_info: _Optional[_Union[O365AddSnapshotArg.PublicFolderInfo, _Mapping]] = ..., teams_info: _Optional[_Union[O365AddSnapshotArg.TeamsInfo, _Mapping]] = ..., group_info: _Optional[_Union[O365AddSnapshotArg.GroupInfo, _Mapping]] = ...) -> None: ...

class SharepointItemMetadata(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnspecified: _ClassVar[SharepointItemMetadata.Type]
        kFile: _ClassVar[SharepointItemMetadata.Type]
        kDirectory: _ClassVar[SharepointItemMetadata.Type]
        kSiteDoclib: _ClassVar[SharepointItemMetadata.Type]
        kSiteList: _ClassVar[SharepointItemMetadata.Type]
    kUnspecified: SharepointItemMetadata.Type
    kFile: SharepointItemMetadata.Type
    kDirectory: SharepointItemMetadata.Type
    kSiteDoclib: SharepointItemMetadata.Type
    kSiteList: SharepointItemMetadata.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SharepointItemMetadata.Type
    def __init__(self, type: _Optional[_Union[SharepointItemMetadata.Type, str]] = ...) -> None: ...
