from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Slice(_message.Message):
    __slots__ = ("relative_file_path", "file_offset", "length", "sha1", "dedup_range", "data_offset_vec")
    RELATIVE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATA_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
    relative_file_path: str
    file_offset: int
    length: int
    sha1: bytes
    dedup_range: _dedup_range_pb2.DedupRange
    data_offset_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, relative_file_path: _Optional[str] = ..., file_offset: _Optional[int] = ..., length: _Optional[int] = ..., sha1: _Optional[bytes] = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., data_offset_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class RsyncPigeonTransmitOpCheckpoint(_message.Message):
    __slots__ = ("in_flight_entity_vec", "max_completed_entity", "num_work_units_skipped", "logical_bytes_transferred", "file_header", "view_listing_file_path", "start_time_usecs", "metadata_transmit_end_time_usecs", "num_attempts_remaining", "num_attempts_allowed", "num_incarnations", "transmitted_view_logical_range_vec", "debug_mode", "debug_info", "view_diff_state", "version", "raise_skipped_file_alert", "entity_id", "file_offset", "view_listing_file_offset")
    class InFlightEntity(_message.Message):
        __slots__ = ("entity_id", "file_offset", "view_listing_file_offset")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        VIEW_LISTING_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        file_offset: int
        view_listing_file_offset: int
        def __init__(self, entity_id: _Optional[int] = ..., file_offset: _Optional[int] = ..., view_listing_file_offset: _Optional[int] = ...) -> None: ...
    class CompletedEntity(_message.Message):
        __slots__ = ("entity_id", "size", "view_listing_file_offset", "view_logical_offset")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        VIEW_LISTING_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        VIEW_LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        size: int
        view_listing_file_offset: int
        view_logical_offset: int
        def __init__(self, entity_id: _Optional[int] = ..., size: _Optional[int] = ..., view_listing_file_offset: _Optional[int] = ..., view_logical_offset: _Optional[int] = ...) -> None: ...
    class Range(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    class DebugInfo(_message.Message):
        __slots__ = ("entity_state_vec", "ignored_entity_id_range_vec")
        class EntityState(_message.Message):
            __slots__ = ("entity_info", "transmitted_range_vec", "attrs_transmitted", "num_match_errors", "num_write_errors", "num_setattr_errors", "matched_range_vec")
            ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
            TRANSMITTED_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
            ATTRS_TRANSMITTED_FIELD_NUMBER: _ClassVar[int]
            NUM_MATCH_ERRORS_FIELD_NUMBER: _ClassVar[int]
            NUM_WRITE_ERRORS_FIELD_NUMBER: _ClassVar[int]
            NUM_SETATTR_ERRORS_FIELD_NUMBER: _ClassVar[int]
            MATCHED_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
            entity_info: ViewListing.EntityInfo
            transmitted_range_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.Range]
            attrs_transmitted: bool
            num_match_errors: int
            num_write_errors: int
            num_setattr_errors: int
            matched_range_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.Range]
            def __init__(self, entity_info: _Optional[_Union[ViewListing.EntityInfo, _Mapping]] = ..., transmitted_range_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.Range, _Mapping]]] = ..., attrs_transmitted: bool = ..., num_match_errors: _Optional[int] = ..., num_write_errors: _Optional[int] = ..., num_setattr_errors: _Optional[int] = ..., matched_range_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.Range, _Mapping]]] = ...) -> None: ...
        ENTITY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        IGNORED_ENTITY_ID_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_state_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.DebugInfo.EntityState]
        ignored_entity_id_range_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.Range]
        def __init__(self, entity_state_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.DebugInfo.EntityState, _Mapping]]] = ..., ignored_entity_id_range_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.Range, _Mapping]]] = ...) -> None: ...
    class ViewDiffState(_message.Message):
        __slots__ = ("diff_entity_id", "view_diff_listing_file_offset", "view_diff_listing_file_path", "entities_created", "entities_deleted", "entities_modified")
        DIFF_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_DIFF_LISTING_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        VIEW_DIFF_LISTING_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ENTITIES_CREATED_FIELD_NUMBER: _ClassVar[int]
        ENTITIES_DELETED_FIELD_NUMBER: _ClassVar[int]
        ENTITIES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
        diff_entity_id: int
        view_diff_listing_file_offset: int
        view_diff_listing_file_path: str
        entities_created: int
        entities_deleted: int
        entities_modified: int
        def __init__(self, diff_entity_id: _Optional[int] = ..., view_diff_listing_file_offset: _Optional[int] = ..., view_diff_listing_file_path: _Optional[str] = ..., entities_created: _Optional[int] = ..., entities_deleted: _Optional[int] = ..., entities_modified: _Optional[int] = ...) -> None: ...
    IN_FLIGHT_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_COMPLETED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    NUM_WORK_UNITS_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    FILE_HEADER_FIELD_NUMBER: _ClassVar[int]
    VIEW_LISTING_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    METADATA_TRANSMIT_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_ATTEMPTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    NUM_ATTEMPTS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    NUM_INCARNATIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSMITTED_VIEW_LOGICAL_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MODE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_DIFF_STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RAISE_SKIPPED_FILE_ALERT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    VIEW_LISTING_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    in_flight_entity_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.InFlightEntity]
    max_completed_entity: RsyncPigeonTransmitOpCheckpoint.CompletedEntity
    num_work_units_skipped: int
    logical_bytes_transferred: int
    file_header: EntityFileHeader
    view_listing_file_path: str
    start_time_usecs: int
    metadata_transmit_end_time_usecs: int
    num_attempts_remaining: int
    num_attempts_allowed: int
    num_incarnations: int
    transmitted_view_logical_range_vec: _containers.RepeatedCompositeFieldContainer[RsyncPigeonTransmitOpCheckpoint.Range]
    debug_mode: bool
    debug_info: RsyncPigeonTransmitOpCheckpoint.DebugInfo
    view_diff_state: RsyncPigeonTransmitOpCheckpoint.ViewDiffState
    version: int
    raise_skipped_file_alert: bool
    entity_id: int
    file_offset: int
    view_listing_file_offset: int
    def __init__(self, in_flight_entity_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.InFlightEntity, _Mapping]]] = ..., max_completed_entity: _Optional[_Union[RsyncPigeonTransmitOpCheckpoint.CompletedEntity, _Mapping]] = ..., num_work_units_skipped: _Optional[int] = ..., logical_bytes_transferred: _Optional[int] = ..., file_header: _Optional[_Union[EntityFileHeader, _Mapping]] = ..., view_listing_file_path: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., metadata_transmit_end_time_usecs: _Optional[int] = ..., num_attempts_remaining: _Optional[int] = ..., num_attempts_allowed: _Optional[int] = ..., num_incarnations: _Optional[int] = ..., transmitted_view_logical_range_vec: _Optional[_Iterable[_Union[RsyncPigeonTransmitOpCheckpoint.Range, _Mapping]]] = ..., debug_mode: bool = ..., debug_info: _Optional[_Union[RsyncPigeonTransmitOpCheckpoint.DebugInfo, _Mapping]] = ..., view_diff_state: _Optional[_Union[RsyncPigeonTransmitOpCheckpoint.ViewDiffState, _Mapping]] = ..., version: _Optional[int] = ..., raise_skipped_file_alert: bool = ..., entity_id: _Optional[int] = ..., file_offset: _Optional[int] = ..., view_listing_file_offset: _Optional[int] = ...) -> None: ...

class EntityFileHeader(_message.Message):
    __slots__ = ("num_entities_in_view", "view_logical_size", "last_view_listing_proto_offset", "num_view_listing_protos", "num_entities_in_diff_listing", "last_diff_listing_proto_offset", "num_diff_listing_protos", "current_view_root_index", "current_ancestor_view_root_index", "directory_walker_checkpoint_version", "special_files_replicated")
    NUM_ENTITIES_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEW_LISTING_PROTO_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEW_LISTING_PROTOS_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTITIES_IN_DIFF_LISTING_FIELD_NUMBER: _ClassVar[int]
    LAST_DIFF_LISTING_PROTO_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_DIFF_LISTING_PROTOS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIEW_ROOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ANCESTOR_VIEW_ROOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_WALKER_CHECKPOINT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FILES_REPLICATED_FIELD_NUMBER: _ClassVar[int]
    num_entities_in_view: int
    view_logical_size: int
    last_view_listing_proto_offset: int
    num_view_listing_protos: int
    num_entities_in_diff_listing: int
    last_diff_listing_proto_offset: int
    num_diff_listing_protos: int
    current_view_root_index: int
    current_ancestor_view_root_index: int
    directory_walker_checkpoint_version: int
    special_files_replicated: int
    def __init__(self, num_entities_in_view: _Optional[int] = ..., view_logical_size: _Optional[int] = ..., last_view_listing_proto_offset: _Optional[int] = ..., num_view_listing_protos: _Optional[int] = ..., num_entities_in_diff_listing: _Optional[int] = ..., last_diff_listing_proto_offset: _Optional[int] = ..., num_diff_listing_protos: _Optional[int] = ..., current_view_root_index: _Optional[int] = ..., current_ancestor_view_root_index: _Optional[int] = ..., directory_walker_checkpoint_version: _Optional[int] = ..., special_files_replicated: _Optional[int] = ...) -> None: ...

class ViewListing(_message.Message):
    __slots__ = ("entity_info_vec",)
    class EntityHandleProto(_message.Message):
        __slots__ = ("view_id", "root_inode_id", "entity_id")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_inode_id: int
        entity_id: int
        def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
    class EntityInfo(_message.Message):
        __slots__ = ("entity_id", "relative_path", "mode", "size", "symlink_target", "original_link_relative_path", "view_logical_offset", "entity_action", "mega_file_subfile_size_mb", "set_attribute", "force_data_sync", "snap_fs_eh", "data_unchanged_from_ancestor", "has_ancestor", "ancestor_snap_fs_eh", "major_device_number", "minor_device_number")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCreate: _ClassVar[ViewListing.EntityInfo.Action]
            kDelete: _ClassVar[ViewListing.EntityInfo.Action]
            kSetSize: _ClassVar[ViewListing.EntityInfo.Action]
        kCreate: ViewListing.EntityInfo.Action
        kDelete: ViewListing.EntityInfo.Action
        kSetSize: ViewListing.EntityInfo.Action
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_LINK_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        VIEW_LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ACTION_FIELD_NUMBER: _ClassVar[int]
        MEGA_FILE_SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        SET_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        FORCE_DATA_SYNC_FIELD_NUMBER: _ClassVar[int]
        SNAP_FS_EH_FIELD_NUMBER: _ClassVar[int]
        DATA_UNCHANGED_FROM_ANCESTOR_FIELD_NUMBER: _ClassVar[int]
        HAS_ANCESTOR_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_SNAP_FS_EH_FIELD_NUMBER: _ClassVar[int]
        MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        relative_path: bytes
        mode: int
        size: int
        symlink_target: str
        original_link_relative_path: bytes
        view_logical_offset: int
        entity_action: ViewListing.EntityInfo.Action
        mega_file_subfile_size_mb: int
        set_attribute: bool
        force_data_sync: bool
        snap_fs_eh: ViewListing.EntityHandleProto
        data_unchanged_from_ancestor: bool
        has_ancestor: bool
        ancestor_snap_fs_eh: ViewListing.EntityHandleProto
        major_device_number: int
        minor_device_number: int
        def __init__(self, entity_id: _Optional[int] = ..., relative_path: _Optional[bytes] = ..., mode: _Optional[int] = ..., size: _Optional[int] = ..., symlink_target: _Optional[str] = ..., original_link_relative_path: _Optional[bytes] = ..., view_logical_offset: _Optional[int] = ..., entity_action: _Optional[_Union[ViewListing.EntityInfo.Action, str]] = ..., mega_file_subfile_size_mb: _Optional[int] = ..., set_attribute: bool = ..., force_data_sync: bool = ..., snap_fs_eh: _Optional[_Union[ViewListing.EntityHandleProto, _Mapping]] = ..., data_unchanged_from_ancestor: bool = ..., has_ancestor: bool = ..., ancestor_snap_fs_eh: _Optional[_Union[ViewListing.EntityHandleProto, _Mapping]] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ...) -> None: ...
    ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_info_vec: _containers.RepeatedCompositeFieldContainer[ViewListing.EntityInfo]
    def __init__(self, entity_info_vec: _Optional[_Iterable[_Union[ViewListing.EntityInfo, _Mapping]]] = ...) -> None: ...
