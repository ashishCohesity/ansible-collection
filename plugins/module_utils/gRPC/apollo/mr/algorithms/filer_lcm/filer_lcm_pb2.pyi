from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilerLcmContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "enable_lcm_pipeline", "lcm_applicable_view_available", "view_ids_for_lcm_vec")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LCM_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    LCM_APPLICABLE_VIEW_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_IDS_FOR_LCM_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    enable_lcm_pipeline: bool
    lcm_applicable_view_available: bool
    view_ids_for_lcm_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., enable_lcm_pipeline: bool = ..., lcm_applicable_view_available: bool = ..., view_ids_for_lcm_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class LcmKeyProto(_message.Message):
    __slots__ = ("node_id", "inode_id", "view_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    inode_id: int
    view_id: int
    def __init__(self, node_id: _Optional[int] = ..., inode_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...

class LcmValueProto(_message.Message):
    __slots__ = ("view_id_vec", "child_node_id_vec", "entity_info", "inode_md", "fragment_md", "view_id_mapping")
    class EntityInfo(_message.Message):
        __slots__ = ("inode_id", "mtime_usecs", "creation_time_usecs", "atime_usecs", "inode_type", "logical_file_size", "parent_info_vec", "is_directory_empty")
        class InodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[LcmValueProto.EntityInfo.InodeType]
            kDirectory: _ClassVar[LcmValueProto.EntityInfo.InodeType]
        kFile: LcmValueProto.EntityInfo.InodeType
        kDirectory: LcmValueProto.EntityInfo.InodeType
        class ParentInfo(_message.Message):
            __slots__ = ("inode_id", "child_names")
            INODE_ID_FIELD_NUMBER: _ClassVar[int]
            CHILD_NAMES_FIELD_NUMBER: _ClassVar[int]
            inode_id: int
            child_names: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, inode_id: _Optional[int] = ..., child_names: _Optional[_Iterable[str]] = ...) -> None: ...
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ATIME_USECS_FIELD_NUMBER: _ClassVar[int]
        INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        PARENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_EMPTY_FIELD_NUMBER: _ClassVar[int]
        inode_id: int
        mtime_usecs: int
        creation_time_usecs: int
        atime_usecs: int
        inode_type: LcmValueProto.EntityInfo.InodeType
        logical_file_size: int
        parent_info_vec: _containers.RepeatedCompositeFieldContainer[LcmValueProto.EntityInfo.ParentInfo]
        is_directory_empty: bool
        def __init__(self, inode_id: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., atime_usecs: _Optional[int] = ..., inode_type: _Optional[_Union[LcmValueProto.EntityInfo.InodeType, str]] = ..., logical_file_size: _Optional[int] = ..., parent_info_vec: _Optional[_Iterable[_Union[LcmValueProto.EntityInfo.ParentInfo, _Mapping]]] = ..., is_directory_empty: bool = ...) -> None: ...
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    INODE_MD_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_MD_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    child_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    entity_info: LcmValueProto.EntityInfo
    inode_md: _snap_fs_metadata_pb2.InodeMetadataProto
    fragment_md: _snap_fs_metadata_pb2.InodeDataFragmentProto
    view_id_mapping: _view_metadata_pb2.ViewIdMappingProto
    def __init__(self, view_id_vec: _Optional[_Iterable[int]] = ..., child_node_id_vec: _Optional[_Iterable[int]] = ..., entity_info: _Optional[_Union[LcmValueProto.EntityInfo, _Mapping]] = ..., inode_md: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., fragment_md: _Optional[_Union[_snap_fs_metadata_pb2.InodeDataFragmentProto, _Mapping]] = ..., view_id_mapping: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ...) -> None: ...
