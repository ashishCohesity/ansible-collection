from librarian.base import stats_pb2 as _stats_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.ms_graph import graph_external_pb2 as _graph_external_pb2
from magneto.connectors.ms_graph import graph_enums_pb2 as _graph_enums_pb2
from magneto.connectors.outlook import outlook_external_pb2 as _outlook_external_pb2
from yoda.base import reports_pb2 as _reports_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.es import jsonname_pb2 as _jsonname_pb2
from yoda.slave import reports_pb2 as _reports_pb2_1
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from magneto.base.entities import cassandra_pb2 as _cassandra_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LibrarianObjectPrefixFormatMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLocalIntId: _ClassVar[LibrarianObjectPrefixFormatMode]
    kGlobalStringId: _ClassVar[LibrarianObjectPrefixFormatMode]
    kLocalAndGlobalId: _ClassVar[LibrarianObjectPrefixFormatMode]
kLocalIntId: LibrarianObjectPrefixFormatMode
kGlobalStringId: LibrarianObjectPrefixFormatMode
kLocalAndGlobalId: LibrarianObjectPrefixFormatMode

class ObjectSnapshotDocument(_message.Message):
    __slots__ = ("object_id", "object_name", "job_name", "object_aliases", "view_name", "deprecated_snapshot_dir", "view_box_id", "last_verification_time_secs", "DEPRECATED_snapshot_type", "backup_type", "versions", "preferred_read_node_id", "cluster_partition_id", "registered_source_hash", "registered_source", "os_type", "attribute_map", "volume_version_vec", "tenant_id", "finished_librarian_migration_for_cfileindex", "auto_protected_source", "o365_params", "boot_volume_info", "vol_mapping_file_mtime_secs", "volume_mount_io_info_version_vec", "is_reindexing_request", "elasticsearch_index_name", "elasticsearch_doc_type")
    class VersionInfo(_message.Message):
        __slots__ = ("instance_id", "snapshot_timestamp_usecs", "logical_size_bytes", "delta_size_bytes", "physical_size_bytes", "primary_physical_size_bytes", "is_full_backup", "is_app_consistent", "extended_info", "replica_info", "local_snapshot_dir", "num_undetected_partitions", "indexing_status", "view_name", "snapshot_type", "scheduled_backup_type", "time_taken_in_indexing_usecs", "num_entries_indexed", "nas_backup_type_vec", "enable_system_backup", "is_direct_archive_snapshot", "skip_local_replica_in_search", "volume_info", "snapshot_backup_type", "slave_indexing_disabled", "uda_params", "record_stats")
        class IndexingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
            kDone: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
            kNoIndex: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
            kIceboxRestoreStarted: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
            kIceboxRestoreError: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
            kSkipped: _ClassVar[ObjectSnapshotDocument.VersionInfo.IndexingStatus]
        kStarted: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        kDone: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        kNoIndex: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        kIceboxRestoreStarted: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        kIceboxRestoreError: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        kSkipped: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        class UdaParams(_message.Message):
            __slots__ = ("entity_support",)
            ENTITY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
            entity_support: bool
            def __init__(self, entity_support: bool = ...) -> None: ...
        class RecordStats(_message.Message):
            __slots__ = ("deleted", "modified")
            DELETED_FIELD_NUMBER: _ClassVar[int]
            MODIFIED_FIELD_NUMBER: _ClassVar[int]
            deleted: int
            modified: int
            def __init__(self, deleted: _Optional[int] = ..., modified: _Optional[int] = ...) -> None: ...
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        DELTA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
        IS_APP_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_INFO_FIELD_NUMBER: _ClassVar[int]
        REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
        LOCAL_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
        NUM_UNDETECTED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
        INDEXING_STATUS_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIME_TAKEN_IN_INDEXING_USECS_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTRIES_INDEXED_FIELD_NUMBER: _ClassVar[int]
        NAS_BACKUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECT_ARCHIVE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        SKIP_LOCAL_REPLICA_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        SLAVE_INDEXING_DISABLED_FIELD_NUMBER: _ClassVar[int]
        UDA_PARAMS_FIELD_NUMBER: _ClassVar[int]
        RECORD_STATS_FIELD_NUMBER: _ClassVar[int]
        instance_id: _yoda_types_pb2.MagnetoInstanceId
        snapshot_timestamp_usecs: int
        logical_size_bytes: int
        delta_size_bytes: int
        physical_size_bytes: int
        primary_physical_size_bytes: int
        is_full_backup: bool
        is_app_consistent: bool
        extended_info: _yoda_pb2.AddSnapshotArg.ExtendedInformation
        replica_info: _yoda_pb2.SnapshotReplicas
        local_snapshot_dir: str
        num_undetected_partitions: int
        indexing_status: ObjectSnapshotDocument.VersionInfo.IndexingStatus
        view_name: str
        snapshot_type: _magneto_pb2.ObjectSnapshotType.Type
        scheduled_backup_type: _enums_pb2.ScheduledBackupType.Type
        time_taken_in_indexing_usecs: int
        num_entries_indexed: int
        nas_backup_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
        enable_system_backup: bool
        is_direct_archive_snapshot: bool
        skip_local_replica_in_search: bool
        volume_info: _containers.RepeatedCompositeFieldContainer[_reports_pb2.VolumeIndexingInfo]
        snapshot_backup_type: _enums_pb2.Environment.Type
        slave_indexing_disabled: bool
        uda_params: ObjectSnapshotDocument.VersionInfo.UdaParams
        record_stats: ObjectSnapshotDocument.VersionInfo.RecordStats
        def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., delta_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., primary_physical_size_bytes: _Optional[int] = ..., is_full_backup: bool = ..., is_app_consistent: bool = ..., extended_info: _Optional[_Union[_yoda_pb2.AddSnapshotArg.ExtendedInformation, _Mapping]] = ..., replica_info: _Optional[_Union[_yoda_pb2.SnapshotReplicas, _Mapping]] = ..., local_snapshot_dir: _Optional[str] = ..., num_undetected_partitions: _Optional[int] = ..., indexing_status: _Optional[_Union[ObjectSnapshotDocument.VersionInfo.IndexingStatus, str]] = ..., view_name: _Optional[str] = ..., snapshot_type: _Optional[_Union[_magneto_pb2.ObjectSnapshotType.Type, str]] = ..., scheduled_backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., time_taken_in_indexing_usecs: _Optional[int] = ..., num_entries_indexed: _Optional[int] = ..., nas_backup_type_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ..., enable_system_backup: bool = ..., is_direct_archive_snapshot: bool = ..., skip_local_replica_in_search: bool = ..., volume_info: _Optional[_Iterable[_Union[_reports_pb2.VolumeIndexingInfo, _Mapping]]] = ..., snapshot_backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., slave_indexing_disabled: bool = ..., uda_params: _Optional[_Union[ObjectSnapshotDocument.VersionInfo.UdaParams, _Mapping]] = ..., record_stats: _Optional[_Union[ObjectSnapshotDocument.VersionInfo.RecordStats, _Mapping]] = ...) -> None: ...
    class VolumeMapVersion(_message.Message):
        __slots__ = ("volume_map", "instance_id_vec")
        VOLUME_MAP_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        volume_map: _volume_info_pb2.VolumeNameMap
        instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
        def __init__(self, volume_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ..., instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ...) -> None: ...
    class O365Params(_message.Message):
        __slots__ = ("is_outlook_backed_up", "is_one_drive_backed_up")
        IS_OUTLOOK_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
        IS_ONE_DRIVE_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
        is_outlook_backed_up: bool
        is_one_drive_backed_up: bool
        def __init__(self, is_outlook_backed_up: bool = ..., is_one_drive_backed_up: bool = ...) -> None: ...
    class VolumeMountIOInfoMapVersion(_message.Message):
        __slots__ = ("volume_mount_io_info_map", "instance_id_vec")
        VOLUME_MOUNT_IO_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        volume_mount_io_info_map: _reports_pb2.VolumeMappingReport.VolumeMountIOInfo
        instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
        def __init__(self, volume_mount_io_info_map: _Optional[_Union[_reports_pb2.VolumeMappingReport.VolumeMountIOInfo, _Mapping]] = ..., instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ALIASES_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_VERIFICATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_READ_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_LIBRARIAN_MIGRATION_FOR_CFILEINDEX_FIELD_NUMBER: _ClassVar[int]
    AUTO_PROTECTED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    O365_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BOOT_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    VOL_MAPPING_FILE_MTIME_SECS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_IO_INFO_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_REINDEXING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    object_name: str
    job_name: str
    object_aliases: _containers.RepeatedScalarFieldContainer[str]
    view_name: str
    deprecated_snapshot_dir: str
    view_box_id: int
    last_verification_time_secs: int
    DEPRECATED_snapshot_type: _magneto_pb2.ObjectSnapshotType.Type
    backup_type: _enums_pb2.Environment.Type
    versions: _containers.RepeatedCompositeFieldContainer[ObjectSnapshotDocument.VersionInfo]
    preferred_read_node_id: int
    cluster_partition_id: int
    registered_source_hash: int
    registered_source: _entity_pb2.EntityProto
    os_type: str
    attribute_map: _containers.RepeatedCompositeFieldContainer[_yoda_pb2.AddSnapshotArg.KeyValuePair]
    volume_version_vec: _containers.RepeatedCompositeFieldContainer[ObjectSnapshotDocument.VolumeMapVersion]
    tenant_id: str
    finished_librarian_migration_for_cfileindex: bool
    auto_protected_source: _entity_pb2.EntityProto
    o365_params: ObjectSnapshotDocument.O365Params
    boot_volume_info: _volume_info_pb2.VolumeInfo
    vol_mapping_file_mtime_secs: int
    volume_mount_io_info_version_vec: _containers.RepeatedCompositeFieldContainer[ObjectSnapshotDocument.VolumeMountIOInfoMapVersion]
    is_reindexing_request: bool
    elasticsearch_index_name: str
    elasticsearch_doc_type: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., object_name: _Optional[str] = ..., job_name: _Optional[str] = ..., object_aliases: _Optional[_Iterable[str]] = ..., view_name: _Optional[str] = ..., deprecated_snapshot_dir: _Optional[str] = ..., view_box_id: _Optional[int] = ..., last_verification_time_secs: _Optional[int] = ..., DEPRECATED_snapshot_type: _Optional[_Union[_magneto_pb2.ObjectSnapshotType.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., versions: _Optional[_Iterable[_Union[ObjectSnapshotDocument.VersionInfo, _Mapping]]] = ..., preferred_read_node_id: _Optional[int] = ..., cluster_partition_id: _Optional[int] = ..., registered_source_hash: _Optional[int] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., os_type: _Optional[str] = ..., attribute_map: _Optional[_Iterable[_Union[_yoda_pb2.AddSnapshotArg.KeyValuePair, _Mapping]]] = ..., volume_version_vec: _Optional[_Iterable[_Union[ObjectSnapshotDocument.VolumeMapVersion, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., finished_librarian_migration_for_cfileindex: bool = ..., auto_protected_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., o365_params: _Optional[_Union[ObjectSnapshotDocument.O365Params, _Mapping]] = ..., boot_volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., vol_mapping_file_mtime_secs: _Optional[int] = ..., volume_mount_io_info_version_vec: _Optional[_Iterable[_Union[ObjectSnapshotDocument.VolumeMountIOInfoMapVersion, _Mapping]]] = ..., is_reindexing_request: bool = ..., elasticsearch_index_name: _Optional[str] = ..., elasticsearch_doc_type: _Optional[str] = ...) -> None: ...

class CrackedFileDocument(_message.Message):
    __slots__ = ("object_id", "filename", "versions", "file_versions", "document_type", "data_type", "view_box_id", "registered_source_hash", "registered_source_string_id", "tenant_id", "mailbox_item_metadata", "is_directory", "ad_object_metadata", "exchange_mailbox_metadata", "tag_vec", "snapshot_tag_vec", "snapshot_tags_association_map", "one_drive_metadata", "nosql_metadata", "sharepoint_metadata", "public_folder_metadata", "elasticsearch_index_name", "elasticsearch_doc_type", "teams_channel_metadata", "o365_group_metadata", "file_category", "o365_teams_metadata", "magneto_entity_metadata", "uda_metadata", "librarian_mode")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[CrackedFileDocument.DataType]
        kDirectory: _ClassVar[CrackedFileDocument.DataType]
        kSymlink: _ClassVar[CrackedFileDocument.DataType]
        kEmail: _ClassVar[CrackedFileDocument.DataType]
        kEmailFolder: _ClassVar[CrackedFileDocument.DataType]
        kADObject: _ClassVar[CrackedFileDocument.DataType]
        kExchangeMailbox: _ClassVar[CrackedFileDocument.DataType]
        kOneDrive: _ClassVar[CrackedFileDocument.DataType]
        kNoSql: _ClassVar[CrackedFileDocument.DataType]
        kSharepoint: _ClassVar[CrackedFileDocument.DataType]
        kPublicFolder: _ClassVar[CrackedFileDocument.DataType]
        kPublicFolderEmail: _ClassVar[CrackedFileDocument.DataType]
        kTeamsChannel: _ClassVar[CrackedFileDocument.DataType]
        kO365Group: _ClassVar[CrackedFileDocument.DataType]
        kCalendar: _ClassVar[CrackedFileDocument.DataType]
        kCalendarFolder: _ClassVar[CrackedFileDocument.DataType]
        kContact: _ClassVar[CrackedFileDocument.DataType]
        kContactFolder: _ClassVar[CrackedFileDocument.DataType]
        kTeamsContent: _ClassVar[CrackedFileDocument.DataType]
        kUDA: _ClassVar[CrackedFileDocument.DataType]
        kTask: _ClassVar[CrackedFileDocument.DataType]
        kTaskFolder: _ClassVar[CrackedFileDocument.DataType]
        kNote: _ClassVar[CrackedFileDocument.DataType]
        kSearchFolder: _ClassVar[CrackedFileDocument.DataType]
    kFile: CrackedFileDocument.DataType
    kDirectory: CrackedFileDocument.DataType
    kSymlink: CrackedFileDocument.DataType
    kEmail: CrackedFileDocument.DataType
    kEmailFolder: CrackedFileDocument.DataType
    kADObject: CrackedFileDocument.DataType
    kExchangeMailbox: CrackedFileDocument.DataType
    kOneDrive: CrackedFileDocument.DataType
    kNoSql: CrackedFileDocument.DataType
    kSharepoint: CrackedFileDocument.DataType
    kPublicFolder: CrackedFileDocument.DataType
    kPublicFolderEmail: CrackedFileDocument.DataType
    kTeamsChannel: CrackedFileDocument.DataType
    kO365Group: CrackedFileDocument.DataType
    kCalendar: CrackedFileDocument.DataType
    kCalendarFolder: CrackedFileDocument.DataType
    kContact: CrackedFileDocument.DataType
    kContactFolder: CrackedFileDocument.DataType
    kTeamsContent: CrackedFileDocument.DataType
    kUDA: CrackedFileDocument.DataType
    kTask: CrackedFileDocument.DataType
    kTaskFolder: CrackedFileDocument.DataType
    kNote: CrackedFileDocument.DataType
    kSearchFolder: CrackedFileDocument.DataType
    class FileCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOthers: _ClassVar[CrackedFileDocument.FileCategory]
        kExcel: _ClassVar[CrackedFileDocument.FileCategory]
        kPowerpoint: _ClassVar[CrackedFileDocument.FileCategory]
        kDocument: _ClassVar[CrackedFileDocument.FileCategory]
        kImages: _ClassVar[CrackedFileDocument.FileCategory]
        kOneNote: _ClassVar[CrackedFileDocument.FileCategory]
    kOthers: CrackedFileDocument.FileCategory
    kExcel: CrackedFileDocument.FileCategory
    kPowerpoint: CrackedFileDocument.FileCategory
    kDocument: CrackedFileDocument.FileCategory
    kImages: CrackedFileDocument.FileCategory
    kOneNote: CrackedFileDocument.FileCategory
    class VersionInfo(_message.Message):
        __slots__ = ("instance_id", "size_bytes", "mtime_usecs", "snapshot_timestamp_usecs", "content_analysis_tags")
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ANALYSIS_TAGS_FIELD_NUMBER: _ClassVar[int]
        instance_id: _yoda_types_pb2.MagnetoInstanceId
        size_bytes: int
        mtime_usecs: int
        snapshot_timestamp_usecs: int
        content_analysis_tags: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., content_analysis_tags: _Optional[_Iterable[str]] = ...) -> None: ...
    class InstanceIdRange(_message.Message):
        __slots__ = ("lower_limit", "upper_limit")
        LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
        UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
        lower_limit: int
        upper_limit: int
        def __init__(self, lower_limit: _Optional[int] = ..., upper_limit: _Optional[int] = ...) -> None: ...
    class FileVersion(_message.Message):
        __slots__ = ("size_bytes", "mtime_usecs", "instance_ids", "job_instance_ids", "job_instance_id_range_vec", "version_metadata", "backup_source_inode_id")
        class VersionMetadata(_message.Message):
            __slots__ = ("unique_item_identifier",)
            UNIQUE_ITEM_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            unique_item_identifier: str
            def __init__(self, unique_item_identifier: _Optional[str] = ...) -> None: ...
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
        JOB_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
        JOB_INSTANCE_ID_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        VERSION_METADATA_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SOURCE_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        size_bytes: int
        mtime_usecs: int
        instance_ids: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
        job_instance_ids: _containers.RepeatedScalarFieldContainer[int]
        job_instance_id_range_vec: _containers.RepeatedCompositeFieldContainer[CrackedFileDocument.InstanceIdRange]
        version_metadata: CrackedFileDocument.FileVersion.VersionMetadata
        backup_source_inode_id: int
        def __init__(self, size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., instance_ids: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., job_instance_ids: _Optional[_Iterable[int]] = ..., job_instance_id_range_vec: _Optional[_Iterable[_Union[CrackedFileDocument.InstanceIdRange, _Mapping]]] = ..., version_metadata: _Optional[_Union[CrackedFileDocument.FileVersion.VersionMetadata, _Mapping]] = ..., backup_source_inode_id: _Optional[int] = ...) -> None: ...
    class MailboxItemMetadata(_message.Message):
        __slots__ = ("has_attachments", "from_email", "to_recipients_email", "cc_recipients_email", "bcc_recipients_email", "sent_time", "received_time", "subject", "folder_name", "folder_key", "item_key", "full_item_parent_path", "creation_time_secs", "sensitivity", "importance", "last_modified_name", "last_modified_time_secs", "organizer_email", "required_attendees_email_vec", "optional_attendees_email_vec", "is_recurring", "start_time_secs", "end_time_secs", "first_occurrence", "last_occurrence", "recurrence_pattern", "first_name", "middle_name", "last_name", "birthday_secs", "email_addresses_vec", "task_owner", "due_date_secs", "completion_date_secs", "task_status", "contact_email_addresses_vec", "folder_root_type")
        HAS_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
        FROM_EMAIL_FIELD_NUMBER: _ClassVar[int]
        TO_RECIPIENTS_EMAIL_FIELD_NUMBER: _ClassVar[int]
        CC_RECIPIENTS_EMAIL_FIELD_NUMBER: _ClassVar[int]
        BCC_RECIPIENTS_EMAIL_FIELD_NUMBER: _ClassVar[int]
        SENT_TIME_FIELD_NUMBER: _ClassVar[int]
        RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
        FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        ITEM_KEY_FIELD_NUMBER: _ClassVar[int]
        FULL_ITEM_PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        ORGANIZER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_ATTENDEES_EMAIL_VEC_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_ATTENDEES_EMAIL_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_RECURRING_FIELD_NUMBER: _ClassVar[int]
        START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        FIRST_OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
        LAST_OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        BIRTHDAY_SECS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESSES_VEC_FIELD_NUMBER: _ClassVar[int]
        TASK_OWNER_FIELD_NUMBER: _ClassVar[int]
        DUE_DATE_SECS_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_DATE_SECS_FIELD_NUMBER: _ClassVar[int]
        TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTACT_EMAIL_ADDRESSES_VEC_FIELD_NUMBER: _ClassVar[int]
        FOLDER_ROOT_TYPE_FIELD_NUMBER: _ClassVar[int]
        has_attachments: bool
        from_email: str
        to_recipients_email: _containers.RepeatedScalarFieldContainer[str]
        cc_recipients_email: _containers.RepeatedScalarFieldContainer[str]
        bcc_recipients_email: _containers.RepeatedScalarFieldContainer[str]
        sent_time: int
        received_time: int
        subject: str
        folder_name: str
        folder_key: int
        item_key: str
        full_item_parent_path: str
        creation_time_secs: int
        sensitivity: _outlook_external_pb2.ItemMetaData.Sensitivity
        importance: _outlook_external_pb2.ItemMetaData.Importance
        last_modified_name: str
        last_modified_time_secs: int
        organizer_email: str
        required_attendees_email_vec: _containers.RepeatedScalarFieldContainer[str]
        optional_attendees_email_vec: _containers.RepeatedScalarFieldContainer[str]
        is_recurring: bool
        start_time_secs: int
        end_time_secs: int
        first_occurrence: _outlook_external_pb2.ItemMetaData.Occurrence
        last_occurrence: _outlook_external_pb2.ItemMetaData.Occurrence
        recurrence_pattern: _outlook_external_pb2.ItemMetaData.RecurrencePattern
        first_name: str
        middle_name: str
        last_name: str
        birthday_secs: int
        email_addresses_vec: _containers.RepeatedScalarFieldContainer[str]
        task_owner: str
        due_date_secs: int
        completion_date_secs: int
        task_status: _outlook_external_pb2.ItemMetaData.TaskStatus
        contact_email_addresses_vec: _containers.RepeatedScalarFieldContainer[str]
        folder_root_type: _outlook_external_pb2.FolderRootType.Type
        def __init__(self, has_attachments: bool = ..., from_email: _Optional[str] = ..., to_recipients_email: _Optional[_Iterable[str]] = ..., cc_recipients_email: _Optional[_Iterable[str]] = ..., bcc_recipients_email: _Optional[_Iterable[str]] = ..., sent_time: _Optional[int] = ..., received_time: _Optional[int] = ..., subject: _Optional[str] = ..., folder_name: _Optional[str] = ..., folder_key: _Optional[int] = ..., item_key: _Optional[str] = ..., full_item_parent_path: _Optional[str] = ..., creation_time_secs: _Optional[int] = ..., sensitivity: _Optional[_Union[_outlook_external_pb2.ItemMetaData.Sensitivity, str]] = ..., importance: _Optional[_Union[_outlook_external_pb2.ItemMetaData.Importance, str]] = ..., last_modified_name: _Optional[str] = ..., last_modified_time_secs: _Optional[int] = ..., organizer_email: _Optional[str] = ..., required_attendees_email_vec: _Optional[_Iterable[str]] = ..., optional_attendees_email_vec: _Optional[_Iterable[str]] = ..., is_recurring: bool = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., first_occurrence: _Optional[_Union[_outlook_external_pb2.ItemMetaData.Occurrence, _Mapping]] = ..., last_occurrence: _Optional[_Union[_outlook_external_pb2.ItemMetaData.Occurrence, _Mapping]] = ..., recurrence_pattern: _Optional[_Union[_outlook_external_pb2.ItemMetaData.RecurrencePattern, str]] = ..., first_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., last_name: _Optional[str] = ..., birthday_secs: _Optional[int] = ..., email_addresses_vec: _Optional[_Iterable[str]] = ..., task_owner: _Optional[str] = ..., due_date_secs: _Optional[int] = ..., completion_date_secs: _Optional[int] = ..., task_status: _Optional[_Union[_outlook_external_pb2.ItemMetaData.TaskStatus, str]] = ..., contact_email_addresses_vec: _Optional[_Iterable[str]] = ..., folder_root_type: _Optional[_Union[_outlook_external_pb2.FolderRootType.Type, str]] = ...) -> None: ...
    class ADObjectMetadata(_message.Message):
        __slots__ = ("name", "sam_account_name", "guid", "object_type", "distinguished_name", "domain", "email")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SAM_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        GUID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        name: str
        sam_account_name: str
        guid: str
        object_type: str
        distinguished_name: str
        domain: str
        email: str
        def __init__(self, name: _Optional[str] = ..., sam_account_name: _Optional[str] = ..., guid: _Optional[str] = ..., object_type: _Optional[str] = ..., distinguished_name: _Optional[str] = ..., domain: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
    class ExchangeMailboxMetadata(_message.Message):
        __slots__ = ("name", "email", "guid", "database_name")
        NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        GUID_FIELD_NUMBER: _ClassVar[int]
        DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        email: str
        guid: str
        database_name: str
        def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., guid: _Optional[str] = ..., database_name: _Optional[str] = ...) -> None: ...
    class SnapshotTagsAssociationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _yoda_pb2.TaggedSnapshots
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_yoda_pb2.TaggedSnapshots, _Mapping]] = ...) -> None: ...
    class OneDriveMetadata(_message.Message):
        __slots__ = ("doc_type", "size_in_bytes", "creation_time_secs", "owner_name", "owner_email", "owner_id_set", "drive_type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[CrackedFileDocument.OneDriveMetadata.Type]
            kDirectory: _ClassVar[CrackedFileDocument.OneDriveMetadata.Type]
        kFile: CrackedFileDocument.OneDriveMetadata.Type
        kDirectory: CrackedFileDocument.OneDriveMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
        OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_SET_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.OneDriveMetadata.Type
        size_in_bytes: int
        creation_time_secs: int
        owner_name: str
        owner_email: str
        owner_id_set: _graph_external_pb2.IdentitySet
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.OneDriveMetadata.Type, str]] = ..., size_in_bytes: _Optional[int] = ..., creation_time_secs: _Optional[int] = ..., owner_name: _Optional[str] = ..., owner_email: _Optional[str] = ..., owner_id_set: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    class NoSqlMetadata(_message.Message):
        __slots__ = ("doc_type", "name", "parent_name", "cassandra_associated_graph_objects", "keyspace_type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kCassandraKeyspace: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kCassandraTable: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kCouchbaseBucket: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHbaseNamespace: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHbaseTable: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHiveDatabase: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHiveTable: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHivePartition: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kMongoDatabase: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kMongoCollection: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHdfsFile: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
            kHdfsDirectory: _ClassVar[CrackedFileDocument.NoSqlMetadata.Type]
        kUnknown: CrackedFileDocument.NoSqlMetadata.Type
        kCassandraKeyspace: CrackedFileDocument.NoSqlMetadata.Type
        kCassandraTable: CrackedFileDocument.NoSqlMetadata.Type
        kCouchbaseBucket: CrackedFileDocument.NoSqlMetadata.Type
        kHbaseNamespace: CrackedFileDocument.NoSqlMetadata.Type
        kHbaseTable: CrackedFileDocument.NoSqlMetadata.Type
        kHiveDatabase: CrackedFileDocument.NoSqlMetadata.Type
        kHiveTable: CrackedFileDocument.NoSqlMetadata.Type
        kHivePartition: CrackedFileDocument.NoSqlMetadata.Type
        kMongoDatabase: CrackedFileDocument.NoSqlMetadata.Type
        kMongoCollection: CrackedFileDocument.NoSqlMetadata.Type
        kHdfsFile: CrackedFileDocument.NoSqlMetadata.Type
        kHdfsDirectory: CrackedFileDocument.NoSqlMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
        CASSANDRA_ASSOCIATED_GRAPH_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        KEYSPACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.NoSqlMetadata.Type
        name: str
        parent_name: str
        cassandra_associated_graph_objects: _containers.RepeatedScalarFieldContainer[str]
        keyspace_type: _cassandra_pb2.KeyspaceInfo.Type
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.NoSqlMetadata.Type, str]] = ..., name: _Optional[str] = ..., parent_name: _Optional[str] = ..., cassandra_associated_graph_objects: _Optional[_Iterable[str]] = ..., keyspace_type: _Optional[_Union[_cassandra_pb2.KeyspaceInfo.Type, str]] = ...) -> None: ...
    class SharepointListsMetadata(_message.Message):
        __slots__ = ("type", "list_name", "item_count")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kGenericList: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kDocumentLibrary: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kUnused: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kDiscussionBoard: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kSurvey: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kIssue: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
            kUnknown: _ClassVar[CrackedFileDocument.SharepointListsMetadata.Type]
        kGenericList: CrackedFileDocument.SharepointListsMetadata.Type
        kDocumentLibrary: CrackedFileDocument.SharepointListsMetadata.Type
        kUnused: CrackedFileDocument.SharepointListsMetadata.Type
        kDiscussionBoard: CrackedFileDocument.SharepointListsMetadata.Type
        kSurvey: CrackedFileDocument.SharepointListsMetadata.Type
        kIssue: CrackedFileDocument.SharepointListsMetadata.Type
        kUnknown: CrackedFileDocument.SharepointListsMetadata.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LIST_NAME_FIELD_NUMBER: _ClassVar[int]
        ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
        type: CrackedFileDocument.SharepointListsMetadata.Type
        list_name: str
        item_count: int
        def __init__(self, type: _Optional[_Union[CrackedFileDocument.SharepointListsMetadata.Type, str]] = ..., list_name: _Optional[str] = ..., item_count: _Optional[int] = ...) -> None: ...
    class SharepointMetadata(_message.Message):
        __slots__ = ("doc_type", "size_in_bytes", "creation_time_secs", "owner_name", "owner_email", "owner_id_set", "drive_type", "list_metadata")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[CrackedFileDocument.SharepointMetadata.Type]
            kDirectory: _ClassVar[CrackedFileDocument.SharepointMetadata.Type]
            kSiteDoclib: _ClassVar[CrackedFileDocument.SharepointMetadata.Type]
            kSiteList: _ClassVar[CrackedFileDocument.SharepointMetadata.Type]
        kFile: CrackedFileDocument.SharepointMetadata.Type
        kDirectory: CrackedFileDocument.SharepointMetadata.Type
        kSiteDoclib: CrackedFileDocument.SharepointMetadata.Type
        kSiteList: CrackedFileDocument.SharepointMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
        OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_SET_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LIST_METADATA_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.SharepointMetadata.Type
        size_in_bytes: int
        creation_time_secs: int
        owner_name: str
        owner_email: str
        owner_id_set: _graph_external_pb2.IdentitySet
        drive_type: _graph_enums_pb2.DriveType.Type
        list_metadata: CrackedFileDocument.SharepointListsMetadata
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.SharepointMetadata.Type, str]] = ..., size_in_bytes: _Optional[int] = ..., creation_time_secs: _Optional[int] = ..., owner_name: _Optional[str] = ..., owner_email: _Optional[str] = ..., owner_id_set: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ..., list_metadata: _Optional[_Union[CrackedFileDocument.SharepointListsMetadata, _Mapping]] = ...) -> None: ...
    class PublicFolderMetadata(_message.Message):
        __slots__ = ("doc_type", "folder_type", "folder_metadata", "item_metadata")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCalendar: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kContact: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kPost: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kFolder: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kTask: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kJournal: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
            kNote: _ClassVar[CrackedFileDocument.PublicFolderMetadata.Type]
        kCalendar: CrackedFileDocument.PublicFolderMetadata.Type
        kContact: CrackedFileDocument.PublicFolderMetadata.Type
        kPost: CrackedFileDocument.PublicFolderMetadata.Type
        kFolder: CrackedFileDocument.PublicFolderMetadata.Type
        kTask: CrackedFileDocument.PublicFolderMetadata.Type
        kJournal: CrackedFileDocument.PublicFolderMetadata.Type
        kNote: CrackedFileDocument.PublicFolderMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        FOLDER_METADATA_FIELD_NUMBER: _ClassVar[int]
        ITEM_METADATA_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.PublicFolderMetadata.Type
        folder_type: _outlook_external_pb2.FolderType
        folder_metadata: _outlook_external_pb2.FolderContentInfo
        item_metadata: _outlook_external_pb2.ItemMetaData
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.PublicFolderMetadata.Type, str]] = ..., folder_type: _Optional[_Union[_outlook_external_pb2.FolderType, _Mapping]] = ..., folder_metadata: _Optional[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]] = ..., item_metadata: _Optional[_Union[_outlook_external_pb2.ItemMetaData, _Mapping]] = ...) -> None: ...
    class TeamsChannelMetadata(_message.Message):
        __slots__ = ("channel_type", "channel_name", "creation_time_secs", "channel_email", "owner_names", "owner_ids")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kPublic: _ClassVar[CrackedFileDocument.TeamsChannelMetadata.Type]
            kPrivate: _ClassVar[CrackedFileDocument.TeamsChannelMetadata.Type]
        kPublic: CrackedFileDocument.TeamsChannelMetadata.Type
        kPrivate: CrackedFileDocument.TeamsChannelMetadata.Type
        CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_EMAIL_FIELD_NUMBER: _ClassVar[int]
        OWNER_NAMES_FIELD_NUMBER: _ClassVar[int]
        OWNER_IDS_FIELD_NUMBER: _ClassVar[int]
        channel_type: CrackedFileDocument.TeamsChannelMetadata.Type
        channel_name: str
        creation_time_secs: int
        channel_email: str
        owner_names: _containers.RepeatedScalarFieldContainer[str]
        owner_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, channel_type: _Optional[_Union[CrackedFileDocument.TeamsChannelMetadata.Type, str]] = ..., channel_name: _Optional[str] = ..., creation_time_secs: _Optional[int] = ..., channel_email: _Optional[str] = ..., owner_names: _Optional[_Iterable[str]] = ..., owner_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class O365GroupMetadata(_message.Message):
        __slots__ = ("doc_type", "folder_metadata", "email_metadata", "site_metadata")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kEmail: _ClassVar[CrackedFileDocument.O365GroupMetadata.Type]
            kEmailFolder: _ClassVar[CrackedFileDocument.O365GroupMetadata.Type]
            kSiteDoclib: _ClassVar[CrackedFileDocument.O365GroupMetadata.Type]
            kSiteFile: _ClassVar[CrackedFileDocument.O365GroupMetadata.Type]
            kSiteDirectory: _ClassVar[CrackedFileDocument.O365GroupMetadata.Type]
        kEmail: CrackedFileDocument.O365GroupMetadata.Type
        kEmailFolder: CrackedFileDocument.O365GroupMetadata.Type
        kSiteDoclib: CrackedFileDocument.O365GroupMetadata.Type
        kSiteFile: CrackedFileDocument.O365GroupMetadata.Type
        kSiteDirectory: CrackedFileDocument.O365GroupMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        FOLDER_METADATA_FIELD_NUMBER: _ClassVar[int]
        EMAIL_METADATA_FIELD_NUMBER: _ClassVar[int]
        SITE_METADATA_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.O365GroupMetadata.Type
        folder_metadata: _outlook_external_pb2.FolderContentInfo
        email_metadata: _outlook_external_pb2.ItemMetaData
        site_metadata: CrackedFileDocument.SharepointMetadata
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.O365GroupMetadata.Type, str]] = ..., folder_metadata: _Optional[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]] = ..., email_metadata: _Optional[_Union[_outlook_external_pb2.ItemMetaData, _Mapping]] = ..., site_metadata: _Optional[_Union[CrackedFileDocument.SharepointMetadata, _Mapping]] = ...) -> None: ...
    class O365TeamsChannelFilesMetadata(_message.Message):
        __slots__ = ("doc_type", "size_in_bytes", "creation_time_secs", "drive_name", "id")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[CrackedFileDocument.O365TeamsChannelFilesMetadata.Type]
            kDirectory: _ClassVar[CrackedFileDocument.O365TeamsChannelFilesMetadata.Type]
        kFile: CrackedFileDocument.O365TeamsChannelFilesMetadata.Type
        kDirectory: CrackedFileDocument.O365TeamsChannelFilesMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.O365TeamsChannelFilesMetadata.Type
        size_in_bytes: int
        creation_time_secs: int
        drive_name: str
        id: str
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.O365TeamsChannelFilesMetadata.Type, str]] = ..., size_in_bytes: _Optional[int] = ..., creation_time_secs: _Optional[int] = ..., drive_name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class O365TeamsMetadata(_message.Message):
        __slots__ = ("doc_type", "teams_channel_metadata", "teams_channel_file_metadata")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kChannel: _ClassVar[CrackedFileDocument.O365TeamsMetadata.Type]
            kFile: _ClassVar[CrackedFileDocument.O365TeamsMetadata.Type]
            kDoclib: _ClassVar[CrackedFileDocument.O365TeamsMetadata.Type]
        kChannel: CrackedFileDocument.O365TeamsMetadata.Type
        kFile: CrackedFileDocument.O365TeamsMetadata.Type
        kDoclib: CrackedFileDocument.O365TeamsMetadata.Type
        DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEAMS_CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
        TEAMS_CHANNEL_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        doc_type: CrackedFileDocument.O365TeamsMetadata.Type
        teams_channel_metadata: CrackedFileDocument.TeamsChannelMetadata
        teams_channel_file_metadata: CrackedFileDocument.O365TeamsChannelFilesMetadata
        def __init__(self, doc_type: _Optional[_Union[CrackedFileDocument.O365TeamsMetadata.Type, str]] = ..., teams_channel_metadata: _Optional[_Union[CrackedFileDocument.TeamsChannelMetadata, _Mapping]] = ..., teams_channel_file_metadata: _Optional[_Union[CrackedFileDocument.O365TeamsChannelFilesMetadata, _Mapping]] = ...) -> None: ...
    class MagnetoEntityMetadata(_message.Message):
        __slots__ = ("magneto_entity_id",)
        MAGNETO_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        magneto_entity_id: int
        def __init__(self, magneto_entity_id: _Optional[int] = ...) -> None: ...
    class UdaMetadata(_message.Message):
        __slots__ = ("full_name", "entity_type")
        FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        full_name: str
        entity_type: str
        def __init__(self, full_name: _Optional[str] = ..., entity_type: _Optional[str] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ITEM_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    AD_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_MAILBOX_METADATA_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TAGS_ASSOCIATION_MAP_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    NOSQL_METADATA_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_METADATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_METADATA_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    O365_GROUP_METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    O365_TEAMS_METADATA_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    UDA_METADATA_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_MODE_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    filename: str
    versions: _containers.RepeatedCompositeFieldContainer[CrackedFileDocument.VersionInfo]
    file_versions: _containers.RepeatedCompositeFieldContainer[CrackedFileDocument.FileVersion]
    document_type: str
    data_type: CrackedFileDocument.DataType
    view_box_id: int
    registered_source_hash: int
    registered_source_string_id: str
    tenant_id: str
    mailbox_item_metadata: CrackedFileDocument.MailboxItemMetadata
    is_directory: bool
    ad_object_metadata: CrackedFileDocument.ADObjectMetadata
    exchange_mailbox_metadata: CrackedFileDocument.ExchangeMailboxMetadata
    tag_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_tag_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_tags_association_map: _containers.MessageMap[str, _yoda_pb2.TaggedSnapshots]
    one_drive_metadata: CrackedFileDocument.OneDriveMetadata
    nosql_metadata: CrackedFileDocument.NoSqlMetadata
    sharepoint_metadata: CrackedFileDocument.SharepointMetadata
    public_folder_metadata: CrackedFileDocument.PublicFolderMetadata
    elasticsearch_index_name: str
    elasticsearch_doc_type: str
    teams_channel_metadata: CrackedFileDocument.TeamsChannelMetadata
    o365_group_metadata: CrackedFileDocument.O365GroupMetadata
    file_category: CrackedFileDocument.FileCategory
    o365_teams_metadata: CrackedFileDocument.O365TeamsMetadata
    magneto_entity_metadata: CrackedFileDocument.MagnetoEntityMetadata
    uda_metadata: CrackedFileDocument.UdaMetadata
    librarian_mode: LibrarianObjectPrefixFormatMode
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., filename: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[CrackedFileDocument.VersionInfo, _Mapping]]] = ..., file_versions: _Optional[_Iterable[_Union[CrackedFileDocument.FileVersion, _Mapping]]] = ..., document_type: _Optional[str] = ..., data_type: _Optional[_Union[CrackedFileDocument.DataType, str]] = ..., view_box_id: _Optional[int] = ..., registered_source_hash: _Optional[int] = ..., registered_source_string_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., mailbox_item_metadata: _Optional[_Union[CrackedFileDocument.MailboxItemMetadata, _Mapping]] = ..., is_directory: bool = ..., ad_object_metadata: _Optional[_Union[CrackedFileDocument.ADObjectMetadata, _Mapping]] = ..., exchange_mailbox_metadata: _Optional[_Union[CrackedFileDocument.ExchangeMailboxMetadata, _Mapping]] = ..., tag_vec: _Optional[_Iterable[str]] = ..., snapshot_tag_vec: _Optional[_Iterable[str]] = ..., snapshot_tags_association_map: _Optional[_Mapping[str, _yoda_pb2.TaggedSnapshots]] = ..., one_drive_metadata: _Optional[_Union[CrackedFileDocument.OneDriveMetadata, _Mapping]] = ..., nosql_metadata: _Optional[_Union[CrackedFileDocument.NoSqlMetadata, _Mapping]] = ..., sharepoint_metadata: _Optional[_Union[CrackedFileDocument.SharepointMetadata, _Mapping]] = ..., public_folder_metadata: _Optional[_Union[CrackedFileDocument.PublicFolderMetadata, _Mapping]] = ..., elasticsearch_index_name: _Optional[str] = ..., elasticsearch_doc_type: _Optional[str] = ..., teams_channel_metadata: _Optional[_Union[CrackedFileDocument.TeamsChannelMetadata, _Mapping]] = ..., o365_group_metadata: _Optional[_Union[CrackedFileDocument.O365GroupMetadata, _Mapping]] = ..., file_category: _Optional[_Union[CrackedFileDocument.FileCategory, str]] = ..., o365_teams_metadata: _Optional[_Union[CrackedFileDocument.O365TeamsMetadata, _Mapping]] = ..., magneto_entity_metadata: _Optional[_Union[CrackedFileDocument.MagnetoEntityMetadata, _Mapping]] = ..., uda_metadata: _Optional[_Union[CrackedFileDocument.UdaMetadata, _Mapping]] = ..., librarian_mode: _Optional[_Union[LibrarianObjectPrefixFormatMode, str]] = ...) -> None: ...

class JobRunsProto(_message.Message):
    __slots__ = ("instance_ids",)
    INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    instance_ids: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    def __init__(self, instance_ids: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ...) -> None: ...

class CrackedFileInstanceProto(_message.Message):
    __slots__ = ("instance_id", "indexing_policy", "num_undetected_partitions", "use_ranges", "num_entries_indexed", "num_total_view_entities")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    NUM_UNDETECTED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    USE_RANGES_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_INDEXED_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_VIEW_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    indexing_policy: _env_params_pb2.IndexingPolicyProto
    num_undetected_partitions: int
    use_ranges: bool
    num_entries_indexed: int
    num_total_view_entities: int
    def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., indexing_policy: _Optional[_Union[_env_params_pb2.IndexingPolicyProto, _Mapping]] = ..., num_undetected_partitions: _Optional[int] = ..., use_ranges: bool = ..., num_entries_indexed: _Optional[int] = ..., num_total_view_entities: _Optional[int] = ...) -> None: ...

class CheckPointInfoProto(_message.Message):
    __slots__ = ("instance_id", "cur_volume", "cur_checkpoint", "object_report", "time_taken_in_indexing_usecs", "num_entries_indexed", "checkpoint_source", "doc_stats", "start_time_usecs", "num_entries_deleted")
    class CheckpointSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDFSWalker: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kNTFSParser: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kXFSParser: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kRocksdbMailboxIterator: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kViewForcedFullIndex: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kViewIncrementalIndex: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kViewDeleteOlderVersions: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kViewIndexFromNasCheckpoint: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kPublicFolderHierarchyDBIter: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kSharepointDrivesCheckpoint: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kSnapDiffCheckpoint: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kRocksdbGroupMailboxIterator: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kTeamsChannelSiteIterator: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kOneDriveIterator: _ClassVar[CheckPointInfoProto.CheckpointSource]
        kLevelOrder: _ClassVar[CheckPointInfoProto.CheckpointSource]
    kDFSWalker: CheckPointInfoProto.CheckpointSource
    kNTFSParser: CheckPointInfoProto.CheckpointSource
    kXFSParser: CheckPointInfoProto.CheckpointSource
    kRocksdbMailboxIterator: CheckPointInfoProto.CheckpointSource
    kViewForcedFullIndex: CheckPointInfoProto.CheckpointSource
    kViewIncrementalIndex: CheckPointInfoProto.CheckpointSource
    kViewDeleteOlderVersions: CheckPointInfoProto.CheckpointSource
    kViewIndexFromNasCheckpoint: CheckPointInfoProto.CheckpointSource
    kPublicFolderHierarchyDBIter: CheckPointInfoProto.CheckpointSource
    kSharepointDrivesCheckpoint: CheckPointInfoProto.CheckpointSource
    kSnapDiffCheckpoint: CheckPointInfoProto.CheckpointSource
    kRocksdbGroupMailboxIterator: CheckPointInfoProto.CheckpointSource
    kTeamsChannelSiteIterator: CheckPointInfoProto.CheckpointSource
    kOneDriveIterator: CheckPointInfoProto.CheckpointSource
    kLevelOrder: CheckPointInfoProto.CheckpointSource
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_VOLUME_FIELD_NUMBER: _ClassVar[int]
    CUR_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REPORT_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_IN_INDEXING_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_INDEXED_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DOC_STATS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_DELETED_FIELD_NUMBER: _ClassVar[int]
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    cur_volume: bytes
    cur_checkpoint: bytes
    object_report: _reports_pb2_1.ObjectReport
    time_taken_in_indexing_usecs: int
    num_entries_indexed: int
    checkpoint_source: CheckPointInfoProto.CheckpointSource
    doc_stats: _stats_pb2.DocumentStats
    start_time_usecs: int
    num_entries_deleted: int
    def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cur_volume: _Optional[bytes] = ..., cur_checkpoint: _Optional[bytes] = ..., object_report: _Optional[_Union[_reports_pb2_1.ObjectReport, _Mapping]] = ..., time_taken_in_indexing_usecs: _Optional[int] = ..., num_entries_indexed: _Optional[int] = ..., checkpoint_source: _Optional[_Union[CheckPointInfoProto.CheckpointSource, str]] = ..., doc_stats: _Optional[_Union[_stats_pb2.DocumentStats, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., num_entries_deleted: _Optional[int] = ...) -> None: ...

class MailboxCheckpointProto(_message.Message):
    __slots__ = ("key", "mailbox_folder_key", "operation", "cookie")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFolderOperation: _ClassVar[MailboxCheckpointProto.Operation]
        kIncrementalIndexing: _ClassVar[MailboxCheckpointProto.Operation]
        kFullUpdateDoc: _ClassVar[MailboxCheckpointProto.Operation]
        kFullAddDoc: _ClassVar[MailboxCheckpointProto.Operation]
    kFolderOperation: MailboxCheckpointProto.Operation
    kIncrementalIndexing: MailboxCheckpointProto.Operation
    kFullUpdateDoc: MailboxCheckpointProto.Operation
    kFullAddDoc: MailboxCheckpointProto.Operation
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    key: str
    mailbox_folder_key: int
    operation: MailboxCheckpointProto.Operation
    cookie: bytes
    def __init__(self, key: _Optional[str] = ..., mailbox_folder_key: _Optional[int] = ..., operation: _Optional[_Union[MailboxCheckpointProto.Operation, str]] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class BucketState(_message.Message):
    __slots__ = ("start_folder_key", "end_folder_key", "last_processed_folder_key")
    START_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    END_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    start_folder_key: str
    end_folder_key: str
    last_processed_folder_key: str
    def __init__(self, start_folder_key: _Optional[str] = ..., end_folder_key: _Optional[str] = ..., last_processed_folder_key: _Optional[str] = ...) -> None: ...

class OneDriveCheckpointProto(_message.Message):
    __slots__ = ("key", "operation", "cookie", "num_files_added", "num_dirs_added", "drive_counter")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFullAddDoc: _ClassVar[OneDriveCheckpointProto.Operation]
        kFullUpdateDoc: _ClassVar[OneDriveCheckpointProto.Operation]
        kIncrementalIndexing: _ClassVar[OneDriveCheckpointProto.Operation]
    kFullAddDoc: OneDriveCheckpointProto.Operation
    kFullUpdateDoc: OneDriveCheckpointProto.Operation
    kIncrementalIndexing: OneDriveCheckpointProto.Operation
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_ADDED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRS_ADDED_FIELD_NUMBER: _ClassVar[int]
    DRIVE_COUNTER_FIELD_NUMBER: _ClassVar[int]
    key: str
    operation: OneDriveCheckpointProto.Operation
    cookie: bytes
    num_files_added: int
    num_dirs_added: int
    drive_counter: int
    def __init__(self, key: _Optional[str] = ..., operation: _Optional[_Union[OneDriveCheckpointProto.Operation, str]] = ..., cookie: _Optional[bytes] = ..., num_files_added: _Optional[int] = ..., num_dirs_added: _Optional[int] = ..., drive_counter: _Optional[int] = ...) -> None: ...

class PublicFolderCheckpointProto(_message.Message):
    __slots__ = ("last_visited_key", "num_folders_processed", "is_operation_parallel", "bucket_state_vec")
    LAST_VISITED_KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_FOLDERS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    IS_OPERATION_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    BUCKET_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    last_visited_key: str
    num_folders_processed: int
    is_operation_parallel: bool
    bucket_state_vec: _containers.RepeatedCompositeFieldContainer[BucketState]
    def __init__(self, last_visited_key: _Optional[str] = ..., num_folders_processed: _Optional[int] = ..., is_operation_parallel: bool = ..., bucket_state_vec: _Optional[_Iterable[_Union[BucketState, _Mapping]]] = ...) -> None: ...

class SharepointCheckpointProto(_message.Message):
    __slots__ = ("doc_lib_counter", "last_visited_key")
    DOC_LIB_COUNTER_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_KEY_FIELD_NUMBER: _ClassVar[int]
    doc_lib_counter: int
    last_visited_key: str
    def __init__(self, doc_lib_counter: _Optional[int] = ..., last_visited_key: _Optional[str] = ...) -> None: ...

class TeamsCheckpointProto(_message.Message):
    __slots__ = ("last_visited_channel", "site_checkpoint", "is_public_site_checkpoint")
    LAST_VISITED_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SITE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_SITE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    last_visited_channel: int
    site_checkpoint: SharepointCheckpointProto
    is_public_site_checkpoint: bool
    def __init__(self, last_visited_channel: _Optional[int] = ..., site_checkpoint: _Optional[_Union[SharepointCheckpointProto, _Mapping]] = ..., is_public_site_checkpoint: bool = ...) -> None: ...

class ViewForcedFullIndexCheckpoint(_message.Message):
    __slots__ = ("cookie",)
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    cookie: bytes
    def __init__(self, cookie: _Optional[bytes] = ...) -> None: ...

class NasIndexCheckpoint(_message.Message):
    __slots__ = ("entity_metadata",)
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    entity_metadata: _directory_walker_pb2.EntityMetadata
    def __init__(self, entity_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ...) -> None: ...

class ViewIncrementalIndexCheckpoint(_message.Message):
    __slots__ = ("view_snap_tree_cookie", "diff_directory_inode_id", "diff_directory_child_inode_id", "diff_directory_child_entry_name", "deletion_cookie", "directory_traversal_checkpoint")
    VIEW_SNAP_TREE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DIFF_DIRECTORY_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_DIRECTORY_CHILD_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_DIRECTORY_CHILD_ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_TRAVERSAL_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    view_snap_tree_cookie: int
    diff_directory_inode_id: int
    diff_directory_child_inode_id: int
    diff_directory_child_entry_name: str
    deletion_cookie: bytes
    directory_traversal_checkpoint: bytes
    def __init__(self, view_snap_tree_cookie: _Optional[int] = ..., diff_directory_inode_id: _Optional[int] = ..., diff_directory_child_inode_id: _Optional[int] = ..., diff_directory_child_entry_name: _Optional[str] = ..., deletion_cookie: _Optional[bytes] = ..., directory_traversal_checkpoint: _Optional[bytes] = ...) -> None: ...

class SnapDiffCheckpoint(_message.Message):
    __slots__ = ("checkpoint_type", "source_root_close_range_prefix", "source_root_close_range_cookie", "movegroup_index", "move_operation_index", "src_scan_cookie", "last_visited_key_for_deletion", "deletion_cookie", "last_visited_key_for_update")
    class CheckpointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSourceCloseRangeCookie: _ClassVar[SnapDiffCheckpoint.CheckpointType]
        kMoveOperation: _ClassVar[SnapDiffCheckpoint.CheckpointType]
        kRocksDbMetadataDeletion: _ClassVar[SnapDiffCheckpoint.CheckpointType]
        kRocksDbMetadataUpdate: _ClassVar[SnapDiffCheckpoint.CheckpointType]
    kSourceCloseRangeCookie: SnapDiffCheckpoint.CheckpointType
    kMoveOperation: SnapDiffCheckpoint.CheckpointType
    kRocksDbMetadataDeletion: SnapDiffCheckpoint.CheckpointType
    kRocksDbMetadataUpdate: SnapDiffCheckpoint.CheckpointType
    CHECKPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOT_CLOSE_RANGE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOT_CLOSE_RANGE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    MOVEGROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    MOVE_OPERATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    SRC_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_KEY_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    DELETION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_KEY_FOR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    checkpoint_type: SnapDiffCheckpoint.CheckpointType
    source_root_close_range_prefix: str
    source_root_close_range_cookie: bytes
    movegroup_index: int
    move_operation_index: int
    src_scan_cookie: bytes
    last_visited_key_for_deletion: str
    deletion_cookie: bytes
    last_visited_key_for_update: str
    def __init__(self, checkpoint_type: _Optional[_Union[SnapDiffCheckpoint.CheckpointType, str]] = ..., source_root_close_range_prefix: _Optional[str] = ..., source_root_close_range_cookie: _Optional[bytes] = ..., movegroup_index: _Optional[int] = ..., move_operation_index: _Optional[int] = ..., src_scan_cookie: _Optional[bytes] = ..., last_visited_key_for_deletion: _Optional[str] = ..., deletion_cookie: _Optional[bytes] = ..., last_visited_key_for_update: _Optional[str] = ...) -> None: ...

class CookieCheckpointProto(_message.Message):
    __slots__ = ("instance_id_vec", "base_instance_id", "cookie")
    INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cookie: bytes
    def __init__(self, instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class LibrarianMigrationCheckpoint(_message.Message):
    __slots__ = ("object_id", "exclusive_start_key", "num_docs_processed", "time_spent_usecs", "cloned_db_path", "finished")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_START_KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TIME_SPENT_USECS_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_PATH_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    exclusive_start_key: str
    num_docs_processed: int
    time_spent_usecs: int
    cloned_db_path: str
    finished: bool
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., exclusive_start_key: _Optional[str] = ..., num_docs_processed: _Optional[int] = ..., time_spent_usecs: _Optional[int] = ..., cloned_db_path: _Optional[str] = ..., finished: bool = ...) -> None: ...

class ComputeStatsCheckpoint(_message.Message):
    __slots__ = ("cookie", "object_id", "instance_id", "base_instance_id", "cluster_partition_id", "hist_states", "finished")
    class EntityInfo(_message.Message):
        __slots__ = ("name", "estimate")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ESTIMATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        estimate: float
        def __init__(self, name: _Optional[str] = ..., estimate: _Optional[float] = ...) -> None: ...
    class HistogramState(_message.Message):
        __slots__ = ("type", "sampling_factor", "histogram")
        class HistogramEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFileExtension: _ClassVar[ComputeStatsCheckpoint.HistogramState.HistogramEntityType]
            kDirectory: _ClassVar[ComputeStatsCheckpoint.HistogramState.HistogramEntityType]
            kAddedFileExtension: _ClassVar[ComputeStatsCheckpoint.HistogramState.HistogramEntityType]
            kDeletedFileExtension: _ClassVar[ComputeStatsCheckpoint.HistogramState.HistogramEntityType]
        kFileExtension: ComputeStatsCheckpoint.HistogramState.HistogramEntityType
        kDirectory: ComputeStatsCheckpoint.HistogramState.HistogramEntityType
        kAddedFileExtension: ComputeStatsCheckpoint.HistogramState.HistogramEntityType
        kDeletedFileExtension: ComputeStatsCheckpoint.HistogramState.HistogramEntityType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SAMPLING_FACTOR_FIELD_NUMBER: _ClassVar[int]
        HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        type: ComputeStatsCheckpoint.HistogramState.HistogramEntityType
        sampling_factor: float
        histogram: _containers.RepeatedCompositeFieldContainer[ComputeStatsCheckpoint.EntityInfo]
        def __init__(self, type: _Optional[_Union[ComputeStatsCheckpoint.HistogramState.HistogramEntityType, str]] = ..., sampling_factor: _Optional[float] = ..., histogram: _Optional[_Iterable[_Union[ComputeStatsCheckpoint.EntityInfo, _Mapping]]] = ...) -> None: ...
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    HIST_STATES_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    cookie: bytes
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cluster_partition_id: int
    hist_states: _containers.RepeatedCompositeFieldContainer[ComputeStatsCheckpoint.HistogramState]
    finished: bool
    def __init__(self, cookie: _Optional[bytes] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., hist_states: _Optional[_Iterable[_Union[ComputeStatsCheckpoint.HistogramState, _Mapping]]] = ..., finished: bool = ...) -> None: ...

class LibrarianResponseFilteringMode(_message.Message):
    __slots__ = ("modes",)
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotExists: _ClassVar[LibrarianResponseFilteringMode.Mode]
        kAll: _ClassVar[LibrarianResponseFilteringMode.Mode]
        kLocalIntId: _ClassVar[LibrarianResponseFilteringMode.Mode]
        kGlobalStringId: _ClassVar[LibrarianResponseFilteringMode.Mode]
    kNotExists: LibrarianResponseFilteringMode.Mode
    kAll: LibrarianResponseFilteringMode.Mode
    kLocalIntId: LibrarianResponseFilteringMode.Mode
    kGlobalStringId: LibrarianResponseFilteringMode.Mode
    MODES_FIELD_NUMBER: _ClassVar[int]
    modes: _containers.RepeatedScalarFieldContainer[LibrarianResponseFilteringMode.Mode]
    def __init__(self, modes: _Optional[_Iterable[_Union[LibrarianResponseFilteringMode.Mode, str]]] = ...) -> None: ...

class EntityIdTransitionStatesProto(_message.Message):
    __slots__ = ("states", "transition_type")
    class TransitionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kV0ToV1: _ClassVar[EntityIdTransitionStatesProto.TransitionType]
    kV0ToV1: EntityIdTransitionStatesProto.TransitionType
    class StateProto(_message.Message):
        __slots__ = ("current_state", "start_time_usecs", "end_time_usecs", "suggested_next_state", "suggested_end_time_usecs")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kState1: _ClassVar[EntityIdTransitionStatesProto.StateProto.State]
            kState2: _ClassVar[EntityIdTransitionStatesProto.StateProto.State]
            kState3: _ClassVar[EntityIdTransitionStatesProto.StateProto.State]
            kState4: _ClassVar[EntityIdTransitionStatesProto.StateProto.State]
            kState5: _ClassVar[EntityIdTransitionStatesProto.StateProto.State]
        kState1: EntityIdTransitionStatesProto.StateProto.State
        kState2: EntityIdTransitionStatesProto.StateProto.State
        kState3: EntityIdTransitionStatesProto.StateProto.State
        kState4: EntityIdTransitionStatesProto.StateProto.State
        kState5: EntityIdTransitionStatesProto.StateProto.State
        CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_NEXT_STATE_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        current_state: EntityIdTransitionStatesProto.StateProto.State
        start_time_usecs: int
        end_time_usecs: int
        suggested_next_state: EntityIdTransitionStatesProto.StateProto.State
        suggested_end_time_usecs: int
        def __init__(self, current_state: _Optional[_Union[EntityIdTransitionStatesProto.StateProto.State, str]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., suggested_next_state: _Optional[_Union[EntityIdTransitionStatesProto.StateProto.State, str]] = ..., suggested_end_time_usecs: _Optional[int] = ...) -> None: ...
    STATES_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedCompositeFieldContainer[EntityIdTransitionStatesProto.StateProto]
    transition_type: EntityIdTransitionStatesProto.TransitionType
    def __init__(self, states: _Optional[_Iterable[_Union[EntityIdTransitionStatesProto.StateProto, _Mapping]]] = ..., transition_type: _Optional[_Union[EntityIdTransitionStatesProto.TransitionType, str]] = ...) -> None: ...

class EntityIdTransitionStateMap(_message.Message):
    __slots__ = ("env_entity_id_state_map",)
    class KeyValuePair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EntityIdTransitionStatesProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EntityIdTransitionStatesProto, _Mapping]] = ...) -> None: ...
    ENV_ENTITY_ID_STATE_MAP_FIELD_NUMBER: _ClassVar[int]
    env_entity_id_state_map: _containers.RepeatedCompositeFieldContainer[EntityIdTransitionStateMap.KeyValuePair]
    def __init__(self, env_entity_id_state_map: _Optional[_Iterable[_Union[EntityIdTransitionStateMap.KeyValuePair, _Mapping]]] = ...) -> None: ...

class AuxDbFullIndexingOnEntityIdTransitionValue(_message.Message):
    __slots__ = ("full_indexing_intent", "full_indexing_done")
    FULL_INDEXING_INTENT_FIELD_NUMBER: _ClassVar[int]
    FULL_INDEXING_DONE_FIELD_NUMBER: _ClassVar[int]
    full_indexing_intent: str
    full_indexing_done: str
    def __init__(self, full_indexing_intent: _Optional[str] = ..., full_indexing_done: _Optional[str] = ...) -> None: ...
