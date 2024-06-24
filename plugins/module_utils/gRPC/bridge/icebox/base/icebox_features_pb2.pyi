from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IceboxFeaturesProto(_message.Message):
    __slots__ = ("dedup_supported", "incremental_archives_supported", "dedup_for_nearline_supported", "multiple_views_supported", "parallel_entity_restores_supported", "fix_view_snap_tree_update_intents_supported", "file_restores_supported", "remote_restore_supported", "file_upload_job_supported", "archive_now_supported", "force_full_archive_for_nfoi", "multiple_finalize_objects_tasks_supported")
    DEDUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_ARCHIVES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DEDUP_FOR_NEARLINE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_VIEWS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_ENTITY_RESTORES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FIX_VIEW_SNAP_TREE_UPDATE_INTENTS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_RESTORE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FILE_UPLOAD_JOB_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_NOW_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_ARCHIVE_FOR_NFOI_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_FINALIZE_OBJECTS_TASKS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    dedup_supported: bool
    incremental_archives_supported: bool
    dedup_for_nearline_supported: bool
    multiple_views_supported: bool
    parallel_entity_restores_supported: bool
    fix_view_snap_tree_update_intents_supported: bool
    file_restores_supported: bool
    remote_restore_supported: bool
    file_upload_job_supported: bool
    archive_now_supported: bool
    force_full_archive_for_nfoi: bool
    multiple_finalize_objects_tasks_supported: bool
    def __init__(self, dedup_supported: bool = ..., incremental_archives_supported: bool = ..., dedup_for_nearline_supported: bool = ..., multiple_views_supported: bool = ..., parallel_entity_restores_supported: bool = ..., fix_view_snap_tree_update_intents_supported: bool = ..., file_restores_supported: bool = ..., remote_restore_supported: bool = ..., file_upload_job_supported: bool = ..., archive_now_supported: bool = ..., force_full_archive_for_nfoi: bool = ..., multiple_finalize_objects_tasks_supported: bool = ...) -> None: ...
