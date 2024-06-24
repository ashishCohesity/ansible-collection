from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import enums_pb2 as _enums_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSnapshotLivenessInfoArg(_message.Message):
    __slots__ = ("base", "job_uid", "object_id_vec", "run_start_time_usecs", "time_interval")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    job_uid: _universal_id_pb2.UniversalIdProto
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    run_start_time_usecs: int
    time_interval: _magneto_external_base_pb2.TimeInterval
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ..., run_start_time_usecs: _Optional[int] = ..., time_interval: _Optional[_Union[_magneto_external_base_pb2.TimeInterval, _Mapping]] = ...) -> None: ...

class ObjectSnapshotLivenessInfoProto(_message.Message):
    __slots__ = ("object", "snapshot_info_vec")
    class SnapshotInfo(_message.Message):
        __slots__ = ("view_box_id", "job_uid", "run_start_time_usecs", "copy_info_vec")
        class LocalCopyInfo(_message.Message):
            __slots__ = ("view_name", "local_snapshot_path")
            VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
            LOCAL_SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
            view_name: str
            local_snapshot_path: str
            def __init__(self, view_name: _Optional[str] = ..., local_snapshot_path: _Optional[str] = ...) -> None: ...
        class CopyInfo(_message.Message):
            __slots__ = ("local_copy", "archival_target", "is_deleted_in_magneto_state", "is_deleted_in_yoda_state", "is_deleted_on_snap_fs", "is_deleted_on_icebox")
            LOCAL_COPY_FIELD_NUMBER: _ClassVar[int]
            ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
            IS_DELETED_IN_MAGNETO_STATE_FIELD_NUMBER: _ClassVar[int]
            IS_DELETED_IN_YODA_STATE_FIELD_NUMBER: _ClassVar[int]
            IS_DELETED_ON_SNAP_FS_FIELD_NUMBER: _ClassVar[int]
            IS_DELETED_ON_ICEBOX_FIELD_NUMBER: _ClassVar[int]
            local_copy: ObjectSnapshotLivenessInfoProto.SnapshotInfo.LocalCopyInfo
            archival_target: _magneto_external_base_pb2.ArchivalTargetProto
            is_deleted_in_magneto_state: bool
            is_deleted_in_yoda_state: bool
            is_deleted_on_snap_fs: bool
            is_deleted_on_icebox: bool
            def __init__(self, local_copy: _Optional[_Union[ObjectSnapshotLivenessInfoProto.SnapshotInfo.LocalCopyInfo, _Mapping]] = ..., archival_target: _Optional[_Union[_magneto_external_base_pb2.ArchivalTargetProto, _Mapping]] = ..., is_deleted_in_magneto_state: bool = ..., is_deleted_in_yoda_state: bool = ..., is_deleted_on_snap_fs: bool = ..., is_deleted_on_icebox: bool = ...) -> None: ...
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        COPY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        job_uid: _universal_id_pb2.UniversalIdProto
        run_start_time_usecs: int
        copy_info_vec: _containers.RepeatedCompositeFieldContainer[ObjectSnapshotLivenessInfoProto.SnapshotInfo.CopyInfo]
        def __init__(self, view_box_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., copy_info_vec: _Optional[_Iterable[_Union[ObjectSnapshotLivenessInfoProto.SnapshotInfo.CopyInfo, _Mapping]]] = ...) -> None: ...
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    object: _magneto_external_base_pb2.ObjectProto
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[ObjectSnapshotLivenessInfoProto.SnapshotInfo]
    def __init__(self, object: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., snapshot_info_vec: _Optional[_Iterable[_Union[ObjectSnapshotLivenessInfoProto.SnapshotInfo, _Mapping]]] = ...) -> None: ...

class GetSnapshotLivenessInfoPaginationCookie(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...

class GetSnapshotLivenessInfoResult(_message.Message):
    __slots__ = ("base", "liveness_map", "warnings")
    class LivenessMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ObjectSnapshotLivenessInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ObjectSnapshotLivenessInfoProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_MAP_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    liveness_map: _containers.MessageMap[int, ObjectSnapshotLivenessInfoProto]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., liveness_map: _Optional[_Mapping[int, ObjectSnapshotLivenessInfoProto]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupRunsInternalStateArg(_message.Message):
    __slots__ = ("base", "job_uid", "run_start_time_usecs", "time_interval")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    time_interval: _magneto_external_base_pb2.TimeInterval
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., time_interval: _Optional[_Union[_magneto_external_base_pb2.TimeInterval, _Mapping]] = ...) -> None: ...

class BackupRunsInternalStateInfoProto(_message.Message):
    __slots__ = ("is_gc_run", "is_run_in_memory", "scribe_key_vec")
    IS_GC_RUN_FIELD_NUMBER: _ClassVar[int]
    IS_RUN_IN_MEMORY_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    is_gc_run: bool
    is_run_in_memory: bool
    scribe_key_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_gc_run: bool = ..., is_run_in_memory: bool = ..., scribe_key_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupRunsInternalStateResult(_message.Message):
    __slots__ = ("base", "backup_runs_map")
    class BackupRunsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BackupRunsInternalStateInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BackupRunsInternalStateInfoProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUNS_MAP_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    backup_runs_map: _containers.MessageMap[int, BackupRunsInternalStateInfoProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., backup_runs_map: _Optional[_Mapping[int, BackupRunsInternalStateInfoProto]] = ...) -> None: ...

class ExportMetadataArg(_message.Message):
    __slots__ = ("base", "metadata_selector", "location", "data_format_type")
    class MetadataSelector(_message.Message):
        __slots__ = ("tenant_id", "include_policies", "include_job_descriptions", "include_restore_tasks", "include_environments", "entity_selector", "run_selector")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_POLICIES_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_JOB_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_RESTORE_TASKS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
        ENTITY_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        RUN_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        include_policies: bool
        include_job_descriptions: bool
        include_restore_tasks: bool
        include_environments: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.EnvironmentProto]
        entity_selector: _magneto_external_base_pb2.EntitySelectorProto
        run_selector: _magneto_external_base_pb2.ProtectionRunSelectorProto
        def __init__(self, tenant_id: _Optional[str] = ..., include_policies: bool = ..., include_job_descriptions: bool = ..., include_restore_tasks: bool = ..., include_environments: _Optional[_Iterable[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]]] = ..., entity_selector: _Optional[_Union[_magneto_external_base_pb2.EntitySelectorProto, _Mapping]] = ..., run_selector: _Optional[_Union[_magneto_external_base_pb2.ProtectionRunSelectorProto, _Mapping]] = ...) -> None: ...
    class Location(_message.Message):
        __slots__ = ("type", "view_name")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        type: _magneto_external_base_pb2.DataLocatorProto.Type
        view_name: str
        def __init__(self, type: _Optional[_Union[_magneto_external_base_pb2.DataLocatorProto.Type, str]] = ..., view_name: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    METADATA_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    metadata_selector: ExportMetadataArg.MetadataSelector
    location: ExportMetadataArg.Location
    data_format_type: _enums_pb2.DataFormatType.Type
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., metadata_selector: _Optional[_Union[ExportMetadataArg.MetadataSelector, _Mapping]] = ..., location: _Optional[_Union[ExportMetadataArg.Location, _Mapping]] = ..., data_format_type: _Optional[_Union[_enums_pb2.DataFormatType.Type, str]] = ...) -> None: ...

class ExportMetadataResult(_message.Message):
    __slots__ = ("base", "export_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    export_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., export_operation_id: _Optional[str] = ...) -> None: ...

class QueryExportMetadataStatusArg(_message.Message):
    __slots__ = ("base", "export_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    export_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., export_operation_id: _Optional[str] = ...) -> None: ...

class QueryExportMetadataStatusResult(_message.Message):
    __slots__ = ("base", "status", "export_location")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[QueryExportMetadataStatusResult.Status]
        kFinished: _ClassVar[QueryExportMetadataStatusResult.Status]
    kRunning: QueryExportMetadataStatusResult.Status
    kFinished: QueryExportMetadataStatusResult.Status
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    status: QueryExportMetadataStatusResult.Status
    export_location: _magneto_external_base_pb2.DataLocatorProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., status: _Optional[_Union[QueryExportMetadataStatusResult.Status, str]] = ..., export_location: _Optional[_Union[_magneto_external_base_pb2.DataLocatorProto, _Mapping]] = ...) -> None: ...

class ImportMetadataArg(_message.Message):
    __slots__ = ("base", "import_location")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    import_location: _magneto_external_base_pb2.DataLocatorProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., import_location: _Optional[_Union[_magneto_external_base_pb2.DataLocatorProto, _Mapping]] = ...) -> None: ...

class ImportMetadataResult(_message.Message):
    __slots__ = ("base", "import_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    import_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., import_operation_id: _Optional[str] = ...) -> None: ...

class QueryImportMetadataStatusArg(_message.Message):
    __slots__ = ("base", "import_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    import_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., import_operation_id: _Optional[str] = ...) -> None: ...

class QueryImportMetadataStatusResult(_message.Message):
    __slots__ = ("base", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[QueryImportMetadataStatusResult.Status]
        kFinished: _ClassVar[QueryImportMetadataStatusResult.Status]
    kRunning: QueryImportMetadataStatusResult.Status
    kFinished: QueryImportMetadataStatusResult.Status
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    status: QueryImportMetadataStatusResult.Status
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., status: _Optional[_Union[QueryImportMetadataStatusResult.Status, str]] = ...) -> None: ...

class ValidateTenantMigrationMetadataArg(_message.Message):
    __slots__ = ("base", "import_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    import_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., import_operation_id: _Optional[str] = ...) -> None: ...

class ValidateTenantMigrationMetadataResult(_message.Message):
    __slots__ = ("base", "validate_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    validate_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., validate_operation_id: _Optional[str] = ...) -> None: ...

class QueryTenantMigrationValidationStatusArg(_message.Message):
    __slots__ = ("base", "validate_operation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    validate_operation_id: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., validate_operation_id: _Optional[str] = ...) -> None: ...

class QueryTenantMigrationValidationStatusResult(_message.Message):
    __slots__ = ("base", "status", "report_location")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[QueryTenantMigrationValidationStatusResult.Status]
        kFinished: _ClassVar[QueryTenantMigrationValidationStatusResult.Status]
    kRunning: QueryTenantMigrationValidationStatusResult.Status
    kFinished: QueryTenantMigrationValidationStatusResult.Status
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    status: QueryTenantMigrationValidationStatusResult.Status
    report_location: _magneto_external_base_pb2.DataLocatorProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., status: _Optional[_Union[QueryTenantMigrationValidationStatusResult.Status, str]] = ..., report_location: _Optional[_Union[_magneto_external_base_pb2.DataLocatorProto, _Mapping]] = ...) -> None: ...
