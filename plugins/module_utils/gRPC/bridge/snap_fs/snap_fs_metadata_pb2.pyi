from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.virus_scanner import antivirus_scan_metadata_pb2 as _antivirus_scan_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InodeMetadataProto(_message.Message):
    __slots__ = ("view_box_id", "inode_id", "inode_type", "mode", "uid", "gid", "logical_size", "physical_size", "major_device_number", "minor_device_number", "ctime_usecs", "mtime_usecs", "atime_usecs_vec", "parent_inode_id_vec", "create_verifier", "data_fragment_id_vec", "total_directory_entries", "symlink_data", "blob_info", "minion_info", "mega_file_info", "update_intent", "extended_attributes", "creation_time_usecs", "directory_changelog", "s3_metadata", "file_level_datalock_metadata", "madrox_completed_dir_removals_rid", "antivirus_metadata", "archived_location_vec", "dir_quota_ids", "pending_dir_quota_add", "pending_dir_quota_remove", "embedded_data_frag", "io_tracking_info", "hdfs_attrs", "dir_fragments_change_count", "archived_as_minion", "filename_hash")
    class InodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[InodeMetadataProto.InodeType]
        kDirectory: _ClassVar[InodeMetadataProto.InodeType]
        kBlockDevice: _ClassVar[InodeMetadataProto.InodeType]
        kCharacterDevice: _ClassVar[InodeMetadataProto.InodeType]
        kSymLink: _ClassVar[InodeMetadataProto.InodeType]
        kSocket: _ClassVar[InodeMetadataProto.InodeType]
        kPipe: _ClassVar[InodeMetadataProto.InodeType]
    kFile: InodeMetadataProto.InodeType
    kDirectory: InodeMetadataProto.InodeType
    kBlockDevice: InodeMetadataProto.InodeType
    kCharacterDevice: InodeMetadataProto.InodeType
    kSymLink: InodeMetadataProto.InodeType
    kSocket: InodeMetadataProto.InodeType
    kPipe: InodeMetadataProto.InodeType
    class BlobInfo(_message.Message):
        __slots__ = ("owner_view_snap_tree_id", "blob_snap_tree_id", "blob_snap_tree_cloud_location", "immutable", "brick_size")
        OWNER_VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
        IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
        BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        owner_view_snap_tree_id: int
        blob_snap_tree_id: int
        blob_snap_tree_cloud_location: _cloud_pb2.CloudNodePtrProto
        immutable: bool
        brick_size: int
        def __init__(self, owner_view_snap_tree_id: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ..., blob_snap_tree_cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., immutable: bool = ..., brick_size: _Optional[int] = ...) -> None: ...
    class MinionInfo(_message.Message):
        __slots__ = ("owner_view_snap_tree_id", "blob_snap_tree_id", "blob_offset", "reserved_size", "last_update_time_usecs", "immutable", "minion_brick_location_vec")
        class MinionBrickLocation(_message.Message):
            __slots__ = ("offset", "node_ptr")
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            NODE_PTR_FIELD_NUMBER: _ClassVar[int]
            offset: int
            node_ptr: _cloud_pb2.CloudNodePtrProto
            def __init__(self, offset: _Optional[int] = ..., node_ptr: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ...) -> None: ...
        OWNER_VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
        RESERVED_SIZE_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
        MINION_BRICK_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
        owner_view_snap_tree_id: int
        blob_snap_tree_id: int
        blob_offset: int
        reserved_size: int
        last_update_time_usecs: int
        immutable: bool
        minion_brick_location_vec: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.MinionInfo.MinionBrickLocation]
        def __init__(self, owner_view_snap_tree_id: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ..., blob_offset: _Optional[int] = ..., reserved_size: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ..., immutable: bool = ..., minion_brick_location_vec: _Optional[_Iterable[_Union[InodeMetadataProto.MinionInfo.MinionBrickLocation, _Mapping]]] = ...) -> None: ...
    class MegaFileInfo(_message.Message):
        __slots__ = ("is_subfile", "subfile_type", "subfile_size_mb", "variable_subfile_size_vec", "variable_subfile_count_vec", "skip_subfile_size_checks")
        class SubfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFixedSize: _ClassVar[InodeMetadataProto.MegaFileInfo.SubfileType]
            kVariableSize: _ClassVar[InodeMetadataProto.MegaFileInfo.SubfileType]
        kFixedSize: InodeMetadataProto.MegaFileInfo.SubfileType
        kVariableSize: InodeMetadataProto.MegaFileInfo.SubfileType
        IS_SUBFILE_FIELD_NUMBER: _ClassVar[int]
        SUBFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        VARIABLE_SUBFILE_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
        VARIABLE_SUBFILE_COUNT_VEC_FIELD_NUMBER: _ClassVar[int]
        SKIP_SUBFILE_SIZE_CHECKS_FIELD_NUMBER: _ClassVar[int]
        is_subfile: bool
        subfile_type: InodeMetadataProto.MegaFileInfo.SubfileType
        subfile_size_mb: int
        variable_subfile_size_vec: _containers.RepeatedScalarFieldContainer[int]
        variable_subfile_count_vec: _containers.RepeatedScalarFieldContainer[int]
        skip_subfile_size_checks: bool
        def __init__(self, is_subfile: bool = ..., subfile_type: _Optional[_Union[InodeMetadataProto.MegaFileInfo.SubfileType, str]] = ..., subfile_size_mb: _Optional[int] = ..., variable_subfile_size_vec: _Optional[_Iterable[int]] = ..., variable_subfile_count_vec: _Optional[_Iterable[int]] = ..., skip_subfile_size_checks: bool = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id_high", "intent_id_low", "inode_id_vec", "time_usecs", "dir_add_entries", "dir_remove_entries", "adjust_data_fragments", "delete_inode_during_abort", "mega_file_info", "update_remediation_state", "convert_to_mega_file", "inode_value_version", "unlink_dir")
        class DirAddRemoveEntries(_message.Message):
            __slots__ = ("dir_inode_id", "entry_vec")
            class AddRemoveEntry(_message.Message):
                __slots__ = ("entry_inode_id", "entry_name", "is_replacement", "is_rename", "is_decendent_entity", "entry_display_name", "update_dir_quota_ids", "remove_dir_quota_ids", "dependent_inode_id_vec", "is_intent_skipped", "inode_id_being_replaced", "inode_type", "check_for_duplicates", "filename_hash")
                ENTRY_INODE_ID_FIELD_NUMBER: _ClassVar[int]
                ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
                IS_REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
                IS_RENAME_FIELD_NUMBER: _ClassVar[int]
                IS_DECENDENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
                ENTRY_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
                UPDATE_DIR_QUOTA_IDS_FIELD_NUMBER: _ClassVar[int]
                REMOVE_DIR_QUOTA_IDS_FIELD_NUMBER: _ClassVar[int]
                DEPENDENT_INODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
                IS_INTENT_SKIPPED_FIELD_NUMBER: _ClassVar[int]
                INODE_ID_BEING_REPLACED_FIELD_NUMBER: _ClassVar[int]
                INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
                CHECK_FOR_DUPLICATES_FIELD_NUMBER: _ClassVar[int]
                FILENAME_HASH_FIELD_NUMBER: _ClassVar[int]
                entry_inode_id: int
                entry_name: bytes
                is_replacement: bool
                is_rename: bool
                is_decendent_entity: bool
                entry_display_name: bytes
                update_dir_quota_ids: _containers.RepeatedScalarFieldContainer[int]
                remove_dir_quota_ids: _containers.RepeatedScalarFieldContainer[int]
                dependent_inode_id_vec: _containers.RepeatedScalarFieldContainer[int]
                is_intent_skipped: bool
                inode_id_being_replaced: int
                inode_type: InodeMetadataProto.InodeType
                check_for_duplicates: bool
                filename_hash: int
                def __init__(self, entry_inode_id: _Optional[int] = ..., entry_name: _Optional[bytes] = ..., is_replacement: bool = ..., is_rename: bool = ..., is_decendent_entity: bool = ..., entry_display_name: _Optional[bytes] = ..., update_dir_quota_ids: _Optional[_Iterable[int]] = ..., remove_dir_quota_ids: _Optional[_Iterable[int]] = ..., dependent_inode_id_vec: _Optional[_Iterable[int]] = ..., is_intent_skipped: bool = ..., inode_id_being_replaced: _Optional[int] = ..., inode_type: _Optional[_Union[InodeMetadataProto.InodeType, str]] = ..., check_for_duplicates: bool = ..., filename_hash: _Optional[int] = ...) -> None: ...
            DIR_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
            dir_inode_id: int
            entry_vec: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.UpdateIntent.DirAddRemoveEntries.AddRemoveEntry]
            def __init__(self, dir_inode_id: _Optional[int] = ..., entry_vec: _Optional[_Iterable[_Union[InodeMetadataProto.UpdateIntent.DirAddRemoveEntries.AddRemoveEntry, _Mapping]]] = ...) -> None: ...
        class AdjustDataFragments(_message.Message):
            __slots__ = ("inode_id", "new_data_fragment_id_vec", "clone_data", "blob_info", "minion_info")
            INODE_ID_FIELD_NUMBER: _ClassVar[int]
            NEW_DATA_FRAGMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            CLONE_DATA_FIELD_NUMBER: _ClassVar[int]
            BLOB_INFO_FIELD_NUMBER: _ClassVar[int]
            MINION_INFO_FIELD_NUMBER: _ClassVar[int]
            inode_id: int
            new_data_fragment_id_vec: _containers.RepeatedScalarFieldContainer[int]
            clone_data: bytes
            blob_info: InodeMetadataProto.BlobInfo
            minion_info: InodeMetadataProto.MinionInfo
            def __init__(self, inode_id: _Optional[int] = ..., new_data_fragment_id_vec: _Optional[_Iterable[int]] = ..., clone_data: _Optional[bytes] = ..., blob_info: _Optional[_Union[InodeMetadataProto.BlobInfo, _Mapping]] = ..., minion_info: _Optional[_Union[InodeMetadataProto.MinionInfo, _Mapping]] = ...) -> None: ...
        class MegaFileInfo(_message.Message):
            __slots__ = ("variable_subfile_size_vec", "variable_subfile_count_vec", "subfile_logical_size")
            VARIABLE_SUBFILE_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
            VARIABLE_SUBFILE_COUNT_VEC_FIELD_NUMBER: _ClassVar[int]
            SUBFILE_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
            variable_subfile_size_vec: _containers.RepeatedScalarFieldContainer[int]
            variable_subfile_count_vec: _containers.RepeatedScalarFieldContainer[int]
            subfile_logical_size: int
            def __init__(self, variable_subfile_size_vec: _Optional[_Iterable[int]] = ..., variable_subfile_count_vec: _Optional[_Iterable[int]] = ..., subfile_logical_size: _Optional[int] = ...) -> None: ...
        class UpdateRemediationState(_message.Message):
            __slots__ = ("desired_remediation",)
            DESIRED_REMEDIATION_FIELD_NUMBER: _ClassVar[int]
            desired_remediation: InodeMetadataProto.AntivirusMetadata.Remediation
            def __init__(self, desired_remediation: _Optional[_Union[InodeMetadataProto.AntivirusMetadata.Remediation, str]] = ...) -> None: ...
        class ConvertToMegaFile(_message.Message):
            __slots__ = ("megafile_inode_id", "subfile_inode_id", "fragment_id", "subfile_entry_name")
            MEGAFILE_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            SUBFILE_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            SUBFILE_ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
            megafile_inode_id: int
            subfile_inode_id: int
            fragment_id: int
            subfile_entry_name: bytes
            def __init__(self, megafile_inode_id: _Optional[int] = ..., subfile_inode_id: _Optional[int] = ..., fragment_id: _Optional[int] = ..., subfile_entry_name: _Optional[bytes] = ...) -> None: ...
        class UnlinkDir(_message.Message):
            __slots__ = ("dir_inode_id", "child_inode_id", "child_entry_name")
            DIR_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            CHILD_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            CHILD_ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
            dir_inode_id: int
            child_inode_id: int
            child_entry_name: bytes
            def __init__(self, dir_inode_id: _Optional[int] = ..., child_inode_id: _Optional[int] = ..., child_entry_name: _Optional[bytes] = ...) -> None: ...
        INTENT_ID_HIGH_FIELD_NUMBER: _ClassVar[int]
        INTENT_ID_LOW_FIELD_NUMBER: _ClassVar[int]
        INODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        DIR_ADD_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        DIR_REMOVE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        ADJUST_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
        DELETE_INODE_DURING_ABORT_FIELD_NUMBER: _ClassVar[int]
        MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
        UPDATE_REMEDIATION_STATE_FIELD_NUMBER: _ClassVar[int]
        CONVERT_TO_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
        INODE_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        UNLINK_DIR_FIELD_NUMBER: _ClassVar[int]
        intent_id_high: int
        intent_id_low: int
        inode_id_vec: _containers.RepeatedScalarFieldContainer[int]
        time_usecs: int
        dir_add_entries: InodeMetadataProto.UpdateIntent.DirAddRemoveEntries
        dir_remove_entries: InodeMetadataProto.UpdateIntent.DirAddRemoveEntries
        adjust_data_fragments: InodeMetadataProto.UpdateIntent.AdjustDataFragments
        delete_inode_during_abort: bool
        mega_file_info: InodeMetadataProto.UpdateIntent.MegaFileInfo
        update_remediation_state: InodeMetadataProto.UpdateIntent.UpdateRemediationState
        convert_to_mega_file: InodeMetadataProto.UpdateIntent.ConvertToMegaFile
        inode_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        unlink_dir: InodeMetadataProto.UpdateIntent.UnlinkDir
        def __init__(self, intent_id_high: _Optional[int] = ..., intent_id_low: _Optional[int] = ..., inode_id_vec: _Optional[_Iterable[int]] = ..., time_usecs: _Optional[int] = ..., dir_add_entries: _Optional[_Union[InodeMetadataProto.UpdateIntent.DirAddRemoveEntries, _Mapping]] = ..., dir_remove_entries: _Optional[_Union[InodeMetadataProto.UpdateIntent.DirAddRemoveEntries, _Mapping]] = ..., adjust_data_fragments: _Optional[_Union[InodeMetadataProto.UpdateIntent.AdjustDataFragments, _Mapping]] = ..., delete_inode_during_abort: bool = ..., mega_file_info: _Optional[_Union[InodeMetadataProto.UpdateIntent.MegaFileInfo, _Mapping]] = ..., update_remediation_state: _Optional[_Union[InodeMetadataProto.UpdateIntent.UpdateRemediationState, _Mapping]] = ..., convert_to_mega_file: _Optional[_Union[InodeMetadataProto.UpdateIntent.ConvertToMegaFile, _Mapping]] = ..., inode_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., unlink_dir: _Optional[_Union[InodeMetadataProto.UpdateIntent.UnlinkDir, _Mapping]] = ...) -> None: ...
    class ExtendedAttributes(_message.Message):
        __slots__ = ("smb2_file_attributes", "smb2_extended_attributes", "smb2_security_descriptor", "nfsv41_security_descriptor", "smb2_symlink_descriptor", "snap_fs_time_nano_secs", "linux_acl_attributes", "linux_extended_attributes")
        class Smb2ExtendedAttribute(_message.Message):
            __slots__ = ("ea_flag", "name", "value")
            EA_FLAG_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            ea_flag: int
            name: str
            value: bytes
            def __init__(self, ea_flag: _Optional[int] = ..., name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
        class ACE(_message.Message):
            __slots__ = ("ace_type", "ace_flags", "access_mask", "sid", "flags", "data", "object_type", "inherited_object_type")
            ACE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ACE_FLAGS_FIELD_NUMBER: _ClassVar[int]
            ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
            SID_FIELD_NUMBER: _ClassVar[int]
            FLAGS_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
            INHERITED_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
            ace_type: int
            ace_flags: int
            access_mask: int
            sid: _cluster_config_pb2.ClusterConfigProto.SID
            flags: int
            data: bytes
            object_type: _cluster_config_pb2.ClusterConfigProto.SmbGUID
            inherited_object_type: _cluster_config_pb2.ClusterConfigProto.SmbGUID
            def __init__(self, ace_type: _Optional[int] = ..., ace_flags: _Optional[int] = ..., access_mask: _Optional[int] = ..., sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., flags: _Optional[int] = ..., data: _Optional[bytes] = ..., object_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ..., inherited_object_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ...) -> None: ...
        class Smb2SecurityDescriptor(_message.Message):
            __slots__ = ("sbz1", "control", "owner_sid", "group_sid", "sacls", "dacls", "dacl_empty", "marked_for_update")
            SBZ1_FIELD_NUMBER: _ClassVar[int]
            CONTROL_FIELD_NUMBER: _ClassVar[int]
            OWNER_SID_FIELD_NUMBER: _ClassVar[int]
            GROUP_SID_FIELD_NUMBER: _ClassVar[int]
            SACLS_FIELD_NUMBER: _ClassVar[int]
            DACLS_FIELD_NUMBER: _ClassVar[int]
            DACL_EMPTY_FIELD_NUMBER: _ClassVar[int]
            MARKED_FOR_UPDATE_FIELD_NUMBER: _ClassVar[int]
            sbz1: int
            control: int
            owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
            group_sid: _cluster_config_pb2.ClusterConfigProto.SID
            sacls: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.ACE]
            dacls: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.ACE]
            dacl_empty: bool
            marked_for_update: bool
            def __init__(self, sbz1: _Optional[int] = ..., control: _Optional[int] = ..., owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., group_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., sacls: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.ACE, _Mapping]]] = ..., dacls: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.ACE, _Mapping]]] = ..., dacl_empty: bool = ..., marked_for_update: bool = ...) -> None: ...
        class Nfs41ACE(_message.Message):
            __slots__ = ("ace_type", "ace_flags", "access_mask", "principal_name")
            ACE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ACE_FLAGS_FIELD_NUMBER: _ClassVar[int]
            ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
            PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
            ace_type: int
            ace_flags: int
            access_mask: int
            principal_name: str
            def __init__(self, ace_type: _Optional[int] = ..., ace_flags: _Optional[int] = ..., access_mask: _Optional[int] = ..., principal_name: _Optional[str] = ...) -> None: ...
        class Nfsv41SecurityDescriptor(_message.Message):
            __slots__ = ("dacls", "marked_for_update", "owner_user", "owner_group")
            DACLS_FIELD_NUMBER: _ClassVar[int]
            MARKED_FOR_UPDATE_FIELD_NUMBER: _ClassVar[int]
            OWNER_USER_FIELD_NUMBER: _ClassVar[int]
            OWNER_GROUP_FIELD_NUMBER: _ClassVar[int]
            dacls: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.Nfs41ACE]
            marked_for_update: bool
            owner_user: str
            owner_group: str
            def __init__(self, dacls: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.Nfs41ACE, _Mapping]]] = ..., marked_for_update: bool = ..., owner_user: _Optional[str] = ..., owner_group: _Optional[str] = ...) -> None: ...
        class Smb2SymlinkDescriptor(_message.Message):
            __slots__ = ("substitute_name", "print_name", "target_inode_type", "is_path_relative")
            SUBSTITUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            PRINT_NAME_FIELD_NUMBER: _ClassVar[int]
            TARGET_INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
            IS_PATH_RELATIVE_FIELD_NUMBER: _ClassVar[int]
            substitute_name: str
            print_name: str
            target_inode_type: InodeMetadataProto.InodeType
            is_path_relative: bool
            def __init__(self, substitute_name: _Optional[str] = ..., print_name: _Optional[str] = ..., target_inode_type: _Optional[_Union[InodeMetadataProto.InodeType, str]] = ..., is_path_relative: bool = ...) -> None: ...
        class SnapFsTimeNanoSecs(_message.Message):
            __slots__ = ("ctime_nsecs", "mtime_nsecs", "creation_time_nsecs")
            CTIME_NSECS_FIELD_NUMBER: _ClassVar[int]
            MTIME_NSECS_FIELD_NUMBER: _ClassVar[int]
            CREATION_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
            ctime_nsecs: int
            mtime_nsecs: int
            creation_time_nsecs: int
            def __init__(self, ctime_nsecs: _Optional[int] = ..., mtime_nsecs: _Optional[int] = ..., creation_time_nsecs: _Optional[int] = ...) -> None: ...
        class LinuxEntityACL(_message.Message):
            __slots__ = ("user_or_group", "user_or_group_value", "permission")
            USER_OR_GROUP_FIELD_NUMBER: _ClassVar[int]
            USER_OR_GROUP_VALUE_FIELD_NUMBER: _ClassVar[int]
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            user_or_group: str
            user_or_group_value: str
            permission: str
            def __init__(self, user_or_group: _Optional[str] = ..., user_or_group_value: _Optional[str] = ..., permission: _Optional[str] = ...) -> None: ...
        class LinuxFileExtendedAttribute(_message.Message):
            __slots__ = ("name", "value")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        SMB2_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        SMB2_EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        SMB2_SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        NFSV41_SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        SMB2_SYMLINK_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        SNAP_FS_TIME_NANO_SECS_FIELD_NUMBER: _ClassVar[int]
        LINUX_ACL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        LINUX_EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        smb2_file_attributes: int
        smb2_extended_attributes: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.Smb2ExtendedAttribute]
        smb2_security_descriptor: InodeMetadataProto.ExtendedAttributes.Smb2SecurityDescriptor
        nfsv41_security_descriptor: InodeMetadataProto.ExtendedAttributes.Nfsv41SecurityDescriptor
        smb2_symlink_descriptor: InodeMetadataProto.ExtendedAttributes.Smb2SymlinkDescriptor
        snap_fs_time_nano_secs: InodeMetadataProto.ExtendedAttributes.SnapFsTimeNanoSecs
        linux_acl_attributes: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.LinuxEntityACL]
        linux_extended_attributes: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.LinuxFileExtendedAttribute]
        def __init__(self, smb2_file_attributes: _Optional[int] = ..., smb2_extended_attributes: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.Smb2ExtendedAttribute, _Mapping]]] = ..., smb2_security_descriptor: _Optional[_Union[InodeMetadataProto.ExtendedAttributes.Smb2SecurityDescriptor, _Mapping]] = ..., nfsv41_security_descriptor: _Optional[_Union[InodeMetadataProto.ExtendedAttributes.Nfsv41SecurityDescriptor, _Mapping]] = ..., smb2_symlink_descriptor: _Optional[_Union[InodeMetadataProto.ExtendedAttributes.Smb2SymlinkDescriptor, _Mapping]] = ..., snap_fs_time_nano_secs: _Optional[_Union[InodeMetadataProto.ExtendedAttributes.SnapFsTimeNanoSecs, _Mapping]] = ..., linux_acl_attributes: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.LinuxEntityACL, _Mapping]]] = ..., linux_extended_attributes: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.LinuxFileExtendedAttribute, _Mapping]]] = ...) -> None: ...
    class DirectoryChangelog(_message.Message):
        __slots__ = ("start_time_usecs", "last_overwritten_entry_time_usecs", "recent_changes_vec")
        class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAddition: _ClassVar[InodeMetadataProto.DirectoryChangelog.ChangeType]
            kRemoval: _ClassVar[InodeMetadataProto.DirectoryChangelog.ChangeType]
            kNameChangeOldName: _ClassVar[InodeMetadataProto.DirectoryChangelog.ChangeType]
            kNameChangeNewName: _ClassVar[InodeMetadataProto.DirectoryChangelog.ChangeType]
        kAddition: InodeMetadataProto.DirectoryChangelog.ChangeType
        kRemoval: InodeMetadataProto.DirectoryChangelog.ChangeType
        kNameChangeOldName: InodeMetadataProto.DirectoryChangelog.ChangeType
        kNameChangeNewName: InodeMetadataProto.DirectoryChangelog.ChangeType
        class RecentChange(_message.Message):
            __slots__ = ("change_type", "entry_name", "entry_timestamp_usecs", "is_replacement", "entry_inode_id")
            CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
            ENTRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
            IS_REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
            ENTRY_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            change_type: InodeMetadataProto.DirectoryChangelog.ChangeType
            entry_name: bytes
            entry_timestamp_usecs: int
            is_replacement: bool
            entry_inode_id: int
            def __init__(self, change_type: _Optional[_Union[InodeMetadataProto.DirectoryChangelog.ChangeType, str]] = ..., entry_name: _Optional[bytes] = ..., entry_timestamp_usecs: _Optional[int] = ..., is_replacement: bool = ..., entry_inode_id: _Optional[int] = ...) -> None: ...
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_OVERWRITTEN_ENTRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        RECENT_CHANGES_VEC_FIELD_NUMBER: _ClassVar[int]
        start_time_usecs: int
        last_overwritten_entry_time_usecs: int
        recent_changes_vec: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.DirectoryChangelog.RecentChange]
        def __init__(self, start_time_usecs: _Optional[int] = ..., last_overwritten_entry_time_usecs: _Optional[int] = ..., recent_changes_vec: _Optional[_Iterable[_Union[InodeMetadataProto.DirectoryChangelog.RecentChange, _Mapping]]] = ...) -> None: ...
    class S3Metadata(_message.Message):
        __slots__ = ("object_file_metadata", "multi_part_upload_metadata", "part_metadata", "object_dir_metadata", "empty_object_metadata", "intent")
        OBJECT_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        MULTI_PART_UPLOAD_METADATA_FIELD_NUMBER: _ClassVar[int]
        PART_METADATA_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DIR_METADATA_FIELD_NUMBER: _ClassVar[int]
        EMPTY_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        INTENT_FIELD_NUMBER: _ClassVar[int]
        object_file_metadata: _s3_metadata_pb2.ObjectFileMetadataProto
        multi_part_upload_metadata: _s3_metadata_pb2.MultiPartUploadMetadataProto
        part_metadata: _s3_metadata_pb2.PartMetadataProto
        object_dir_metadata: _s3_metadata_pb2.ObjectDirMetadataProto
        empty_object_metadata: _s3_metadata_pb2.EmptyObjectMetadata
        intent: _s3_metadata_pb2.IntentProto
        def __init__(self, object_file_metadata: _Optional[_Union[_s3_metadata_pb2.ObjectFileMetadataProto, _Mapping]] = ..., multi_part_upload_metadata: _Optional[_Union[_s3_metadata_pb2.MultiPartUploadMetadataProto, _Mapping]] = ..., part_metadata: _Optional[_Union[_s3_metadata_pb2.PartMetadataProto, _Mapping]] = ..., object_dir_metadata: _Optional[_Union[_s3_metadata_pb2.ObjectDirMetadataProto, _Mapping]] = ..., empty_object_metadata: _Optional[_Union[_s3_metadata_pb2.EmptyObjectMetadata, _Mapping]] = ..., intent: _Optional[_Union[_s3_metadata_pb2.IntentProto, _Mapping]] = ...) -> None: ...
    class FileLevelDataLockMetadata(_message.Message):
        __slots__ = ("lock_timestamp_usecs", "expiry_timestamp_usecs", "expiry_timestamp_set_explicitly", "mode", "legal_hold_enabled")
        class ExplicitLockingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCompliance: _ClassVar[InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode]
            kEnterprise: _ClassVar[InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode]
        kCompliance: InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode
        kEnterprise: InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode
        LOCK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_SET_EXPLICITLY_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        lock_timestamp_usecs: int
        expiry_timestamp_usecs: int
        expiry_timestamp_set_explicitly: bool
        mode: InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode
        legal_hold_enabled: bool
        def __init__(self, lock_timestamp_usecs: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., expiry_timestamp_set_explicitly: bool = ..., mode: _Optional[_Union[InodeMetadataProto.FileLevelDataLockMetadata.ExplicitLockingMode, str]] = ..., legal_hold_enabled: bool = ...) -> None: ...
    class AntivirusMetadata(_message.Message):
        __slots__ = ("scan_timestamp_usecs", "service_icap_tag_id", "remediation", "infection_desc", "username", "domain_name", "user_sid")
        class Remediation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kQuarantine: _ClassVar[InodeMetadataProto.AntivirusMetadata.Remediation]
            kUnquarantine: _ClassVar[InodeMetadataProto.AntivirusMetadata.Remediation]
        kQuarantine: InodeMetadataProto.AntivirusMetadata.Remediation
        kUnquarantine: InodeMetadataProto.AntivirusMetadata.Remediation
        SCAN_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ICAP_TAG_ID_FIELD_NUMBER: _ClassVar[int]
        REMEDIATION_FIELD_NUMBER: _ClassVar[int]
        INFECTION_DESC_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_SID_FIELD_NUMBER: _ClassVar[int]
        scan_timestamp_usecs: int
        service_icap_tag_id: int
        remediation: InodeMetadataProto.AntivirusMetadata.Remediation
        infection_desc: _antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto
        username: str
        domain_name: str
        user_sid: str
        def __init__(self, scan_timestamp_usecs: _Optional[int] = ..., service_icap_tag_id: _Optional[int] = ..., remediation: _Optional[_Union[InodeMetadataProto.AntivirusMetadata.Remediation, str]] = ..., infection_desc: _Optional[_Union[_antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto, _Mapping]] = ..., username: _Optional[str] = ..., domain_name: _Optional[str] = ..., user_sid: _Optional[str] = ...) -> None: ...
    class DirQuotaID(_message.Message):
        __slots__ = ("dir_quota_id", "parents_inherited")
        DIR_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
        PARENTS_INHERITED_FIELD_NUMBER: _ClassVar[int]
        dir_quota_id: int
        parents_inherited: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, dir_quota_id: _Optional[int] = ..., parents_inherited: _Optional[_Iterable[int]] = ...) -> None: ...
    class IOTrackingInfo(_message.Message):
        __slots__ = ("start_time_usecs", "ttl_usecs", "max_io_count")
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        TTL_USECS_FIELD_NUMBER: _ClassVar[int]
        MAX_IO_COUNT_FIELD_NUMBER: _ClassVar[int]
        start_time_usecs: int
        ttl_usecs: int
        max_io_count: int
        def __init__(self, start_time_usecs: _Optional[int] = ..., ttl_usecs: _Optional[int] = ..., max_io_count: _Optional[int] = ...) -> None: ...
    class HdfsAttributes(_message.Message):
        __slots__ = ("block_size", "replication", "owner", "group", "ext_attributes")
        class ExtAttributesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bytes
            def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_FIELD_NUMBER: _ClassVar[int]
        OWNER_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        EXT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        block_size: int
        replication: int
        owner: str
        group: str
        ext_attributes: _containers.ScalarMap[str, bytes]
        def __init__(self, block_size: _Optional[int] = ..., replication: _Optional[int] = ..., owner: _Optional[str] = ..., group: _Optional[str] = ..., ext_attributes: _Optional[_Mapping[str, bytes]] = ...) -> None: ...
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_INODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    DATA_FRAGMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIRECTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_FIELD_NUMBER: _ClassVar[int]
    MINION_INFO_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_CHANGELOG_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATALOCK_METADATA_FIELD_NUMBER: _ClassVar[int]
    MADROX_COMPLETED_DIR_REMOVALS_RID_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_IDS_FIELD_NUMBER: _ClassVar[int]
    PENDING_DIR_QUOTA_ADD_FIELD_NUMBER: _ClassVar[int]
    PENDING_DIR_QUOTA_REMOVE_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_FRAG_FIELD_NUMBER: _ClassVar[int]
    IO_TRACKING_INFO_FIELD_NUMBER: _ClassVar[int]
    HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
    DIR_FRAGMENTS_CHANGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AS_MINION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_HASH_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    inode_id: int
    inode_type: InodeMetadataProto.InodeType
    mode: int
    uid: int
    gid: int
    logical_size: int
    physical_size: int
    major_device_number: int
    minor_device_number: int
    ctime_usecs: int
    mtime_usecs: int
    atime_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    parent_inode_id_vec: _containers.RepeatedScalarFieldContainer[int]
    create_verifier: int
    data_fragment_id_vec: _containers.RepeatedScalarFieldContainer[int]
    total_directory_entries: int
    symlink_data: str
    blob_info: InodeMetadataProto.BlobInfo
    minion_info: InodeMetadataProto.MinionInfo
    mega_file_info: InodeMetadataProto.MegaFileInfo
    update_intent: InodeMetadataProto.UpdateIntent
    extended_attributes: InodeMetadataProto.ExtendedAttributes
    creation_time_usecs: int
    directory_changelog: InodeMetadataProto.DirectoryChangelog
    s3_metadata: InodeMetadataProto.S3Metadata
    file_level_datalock_metadata: InodeMetadataProto.FileLevelDataLockMetadata
    madrox_completed_dir_removals_rid: _universal_id_pb2.UniversalIdProto
    antivirus_metadata: InodeMetadataProto.AntivirusMetadata
    archived_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchivedLocation]
    dir_quota_ids: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.DirQuotaID]
    pending_dir_quota_add: _containers.RepeatedScalarFieldContainer[int]
    pending_dir_quota_remove: _containers.RepeatedScalarFieldContainer[int]
    embedded_data_frag: InodeDataFragmentProto
    io_tracking_info: InodeMetadataProto.IOTrackingInfo
    hdfs_attrs: InodeMetadataProto.HdfsAttributes
    dir_fragments_change_count: int
    archived_as_minion: bool
    filename_hash: int
    def __init__(self, view_box_id: _Optional[int] = ..., inode_id: _Optional[int] = ..., inode_type: _Optional[_Union[InodeMetadataProto.InodeType, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., logical_size: _Optional[int] = ..., physical_size: _Optional[int] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., atime_usecs_vec: _Optional[_Iterable[int]] = ..., parent_inode_id_vec: _Optional[_Iterable[int]] = ..., create_verifier: _Optional[int] = ..., data_fragment_id_vec: _Optional[_Iterable[int]] = ..., total_directory_entries: _Optional[int] = ..., symlink_data: _Optional[str] = ..., blob_info: _Optional[_Union[InodeMetadataProto.BlobInfo, _Mapping]] = ..., minion_info: _Optional[_Union[InodeMetadataProto.MinionInfo, _Mapping]] = ..., mega_file_info: _Optional[_Union[InodeMetadataProto.MegaFileInfo, _Mapping]] = ..., update_intent: _Optional[_Union[InodeMetadataProto.UpdateIntent, _Mapping]] = ..., extended_attributes: _Optional[_Union[InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., directory_changelog: _Optional[_Union[InodeMetadataProto.DirectoryChangelog, _Mapping]] = ..., s3_metadata: _Optional[_Union[InodeMetadataProto.S3Metadata, _Mapping]] = ..., file_level_datalock_metadata: _Optional[_Union[InodeMetadataProto.FileLevelDataLockMetadata, _Mapping]] = ..., madrox_completed_dir_removals_rid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., antivirus_metadata: _Optional[_Union[InodeMetadataProto.AntivirusMetadata, _Mapping]] = ..., archived_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchivedLocation, _Mapping]]] = ..., dir_quota_ids: _Optional[_Iterable[_Union[InodeMetadataProto.DirQuotaID, _Mapping]]] = ..., pending_dir_quota_add: _Optional[_Iterable[int]] = ..., pending_dir_quota_remove: _Optional[_Iterable[int]] = ..., embedded_data_frag: _Optional[_Union[InodeDataFragmentProto, _Mapping]] = ..., io_tracking_info: _Optional[_Union[InodeMetadataProto.IOTrackingInfo, _Mapping]] = ..., hdfs_attrs: _Optional[_Union[InodeMetadataProto.HdfsAttributes, _Mapping]] = ..., dir_fragments_change_count: _Optional[int] = ..., archived_as_minion: bool = ..., filename_hash: _Optional[int] = ...) -> None: ...

class InodeDataFragmentProto(_message.Message):
    __slots__ = ("owner_inode_id", "directory_entry_vec", "fragment_data", "sorted", "is_garbage")
    class DirectoryEntry(_message.Message):
        __slots__ = ("name", "inode_id", "display_name", "dup_id", "inode_type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DUP_ID_FIELD_NUMBER: _ClassVar[int]
        INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: bytes
        inode_id: int
        display_name: bytes
        dup_id: int
        inode_type: InodeMetadataProto.InodeType
        def __init__(self, name: _Optional[bytes] = ..., inode_id: _Optional[int] = ..., display_name: _Optional[bytes] = ..., dup_id: _Optional[int] = ..., inode_type: _Optional[_Union[InodeMetadataProto.InodeType, str]] = ...) -> None: ...
    OWNER_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SORTED_FIELD_NUMBER: _ClassVar[int]
    IS_GARBAGE_FIELD_NUMBER: _ClassVar[int]
    owner_inode_id: int
    directory_entry_vec: _containers.RepeatedCompositeFieldContainer[InodeDataFragmentProto.DirectoryEntry]
    fragment_data: bytes
    sorted: bool
    is_garbage: bool
    def __init__(self, owner_inode_id: _Optional[int] = ..., directory_entry_vec: _Optional[_Iterable[_Union[InodeDataFragmentProto.DirectoryEntry, _Mapping]]] = ..., fragment_data: _Optional[bytes] = ..., sorted: bool = ..., is_garbage: bool = ...) -> None: ...

class MinionMetadataProto(_message.Message):
    __slots__ = ("blobs", "frozen_blobs")
    class BlobData(_message.Message):
        __slots__ = ("blob_id", "next_avail_offset")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        NEXT_AVAIL_OFFSET_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        next_avail_offset: int
        def __init__(self, blob_id: _Optional[int] = ..., next_avail_offset: _Optional[int] = ...) -> None: ...
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    FROZEN_BLOBS_FIELD_NUMBER: _ClassVar[int]
    blobs: _containers.RepeatedCompositeFieldContainer[MinionMetadataProto.BlobData]
    frozen_blobs: _containers.RepeatedCompositeFieldContainer[MinionMetadataProto.BlobData]
    def __init__(self, blobs: _Optional[_Iterable[_Union[MinionMetadataProto.BlobData, _Mapping]]] = ..., frozen_blobs: _Optional[_Iterable[_Union[MinionMetadataProto.BlobData, _Mapping]]] = ...) -> None: ...

class ViewSnapTreeValueProto(_message.Message):
    __slots__ = ("metadata", "data", "minion_metadata", "mapped_keys", "mapped_key_byte_swapped_with_last_byte", "mapped_key_swap_bit_mask", "metadata_journal_flush_time_usecs")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MINION_METADATA_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_BYTE_SWAPPED_WITH_LAST_BYTE_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_SWAP_BIT_MASK_FIELD_NUMBER: _ClassVar[int]
    METADATA_JOURNAL_FLUSH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    metadata: InodeMetadataProto
    data: InodeDataFragmentProto
    minion_metadata: MinionMetadataProto
    mapped_keys: bool
    mapped_key_byte_swapped_with_last_byte: int
    mapped_key_swap_bit_mask: int
    metadata_journal_flush_time_usecs: int
    def __init__(self, metadata: _Optional[_Union[InodeMetadataProto, _Mapping]] = ..., data: _Optional[_Union[InodeDataFragmentProto, _Mapping]] = ..., minion_metadata: _Optional[_Union[MinionMetadataProto, _Mapping]] = ..., mapped_keys: bool = ..., mapped_key_byte_swapped_with_last_byte: _Optional[int] = ..., mapped_key_swap_bit_mask: _Optional[int] = ..., metadata_journal_flush_time_usecs: _Optional[int] = ...) -> None: ...

class UptierEntityMetadataProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UptierEntityProto(_message.Message):
    __slots__ = ("error", "uptier_metadata", "path_vec", "inode_metadata")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPTIER_METADATA_FIELD_NUMBER: _ClassVar[int]
    PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uptier_metadata: UptierEntityMetadataProto
    path_vec: _containers.RepeatedScalarFieldContainer[str]
    inode_metadata: InodeMetadataProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uptier_metadata: _Optional[_Union[UptierEntityMetadataProto, _Mapping]] = ..., path_vec: _Optional[_Iterable[str]] = ..., inode_metadata: _Optional[_Union[InodeMetadataProto, _Mapping]] = ...) -> None: ...

class PortalValidationData(_message.Message):
    __slots__ = ("s3_validation_data",)
    class S3ValidationData(_message.Message):
        __slots__ = ("mpu_part_info",)
        class MPUPartInfo(_message.Message):
            __slots__ = ("part_number", "uniquifier")
            PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
            UNIQUIFIER_FIELD_NUMBER: _ClassVar[int]
            part_number: int
            uniquifier: int
            def __init__(self, part_number: _Optional[int] = ..., uniquifier: _Optional[int] = ...) -> None: ...
        MPU_PART_INFO_FIELD_NUMBER: _ClassVar[int]
        mpu_part_info: PortalValidationData.S3ValidationData.MPUPartInfo
        def __init__(self, mpu_part_info: _Optional[_Union[PortalValidationData.S3ValidationData.MPUPartInfo, _Mapping]] = ...) -> None: ...
    S3_VALIDATION_DATA_FIELD_NUMBER: _ClassVar[int]
    s3_validation_data: PortalValidationData.S3ValidationData
    def __init__(self, s3_validation_data: _Optional[_Union[PortalValidationData.S3ValidationData, _Mapping]] = ...) -> None: ...
