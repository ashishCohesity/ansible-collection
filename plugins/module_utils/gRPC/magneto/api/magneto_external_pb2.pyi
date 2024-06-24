from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import enums_pb2 as _enums_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api import magneto_external_entity_metadata_pb2 as _magneto_external_entity_metadata_pb2
from magneto.api import magneto_external_objects_pb2 as _magneto_external_objects_pb2
from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from magneto.api import object_protection_pb2 as _object_protection_pb2
from magneto.api import retention_policy_pb2 as _retention_policy_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublicStatusProto(_message.Message):
    __slots__ = ("status",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[PublicStatusProto.Type]
        kScheduled: _ClassVar[PublicStatusProto.Type]
        kInProgress: _ClassVar[PublicStatusProto.Type]
        kSucceeded: _ClassVar[PublicStatusProto.Type]
        kFailed: _ClassVar[PublicStatusProto.Type]
        kCanceled: _ClassVar[PublicStatusProto.Type]
    kUnknown: PublicStatusProto.Type
    kScheduled: PublicStatusProto.Type
    kInProgress: PublicStatusProto.Type
    kSucceeded: PublicStatusProto.Type
    kFailed: PublicStatusProto.Type
    kCanceled: PublicStatusProto.Type
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: PublicStatusProto.Type
    def __init__(self, status: _Optional[_Union[PublicStatusProto.Type, str]] = ...) -> None: ...

class LocateMasterResult(_message.Message):
    __slots__ = ("base", "ip", "api_server_grpc_port")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    API_SERVER_GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    ip: str
    api_server_grpc_port: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., ip: _Optional[str] = ..., api_server_grpc_port: _Optional[int] = ...) -> None: ...

class FetchEntityHierarchyArg(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ...) -> None: ...

class FetchEntityHierarchyResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class AddOrUpdateEntitiesMetadataArg(_message.Message):
    __slots__ = ("base", "entity_args")
    class EntityArg(_message.Message):
        __slots__ = ("entity_id", "ext_metadata")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EXT_METADATA_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        ext_metadata: _magneto_external_entity_metadata_pb2.EntityExternalMetadataProto
        def __init__(self, entity_id: _Optional[int] = ..., ext_metadata: _Optional[_Union[_magneto_external_entity_metadata_pb2.EntityExternalMetadataProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ARGS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_args: _containers.RepeatedCompositeFieldContainer[AddOrUpdateEntitiesMetadataArg.EntityArg]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_args: _Optional[_Iterable[_Union[AddOrUpdateEntitiesMetadataArg.EntityArg, _Mapping]]] = ...) -> None: ...

class AddOrUpdateEntitiesMetadataResult(_message.Message):
    __slots__ = ("base", "err", "entity_results")
    class EntityResult(_message.Message):
        __slots__ = ("entity_id", "err")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ERR_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        err: _magneto_external_base_pb2.ErrorProto
        def __init__(self, entity_id: _Optional[int] = ..., err: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    err: _magneto_external_base_pb2.ErrorProto
    entity_results: _containers.RepeatedCompositeFieldContainer[AddOrUpdateEntitiesMetadataResult.EntityResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., err: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., entity_results: _Optional[_Iterable[_Union[AddOrUpdateEntitiesMetadataResult.EntityResult, _Mapping]]] = ...) -> None: ...

class FetchClonesSummaryArg(_message.Message):
    __slots__ = ("base", "filters")
    class Filters(_message.Message):
        __slots__ = ("environment_vec", "name", "status", "clone_uids", "task_uids")
        ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CLONE_UIDS_FIELD_NUMBER: _ClassVar[int]
        TASK_UIDS_FIELD_NUMBER: _ClassVar[int]
        environment_vec: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.EnvironmentProto]
        name: str
        status: _containers.RepeatedScalarFieldContainer[PublicStatusProto.Type]
        clone_uids: _containers.RepeatedScalarFieldContainer[str]
        task_uids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, environment_vec: _Optional[_Iterable[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]]] = ..., name: _Optional[str] = ..., status: _Optional[_Iterable[_Union[PublicStatusProto.Type, str]]] = ..., clone_uids: _Optional[_Iterable[str]] = ..., task_uids: _Optional[_Iterable[str]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    filters: FetchClonesSummaryArg.Filters
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., filters: _Optional[_Union[FetchClonesSummaryArg.Filters, _Mapping]] = ...) -> None: ...

class CloneSummaryInfoProto(_message.Message):
    __slots__ = ("entity_uid", "name", "environment", "status", "created_by_user", "last_action", "source_entity", "logical_size_bytes", "sql_info", "oracle_info")
    class SQLInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class OracleInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    ORACLE_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_uid: str
    name: str
    environment: _enum_wrappers_pb2.EnvironmentProto
    status: PublicStatusProto.Type
    created_by_user: _permissions_external_pb2.UserInformationProto
    last_action: TimelineEventProto
    source_entity: _magneto_external_base_pb2.ObjectProto
    logical_size_bytes: int
    sql_info: CloneSummaryInfoProto.SQLInfo
    oracle_info: CloneSummaryInfoProto.OracleInfo
    def __init__(self, entity_uid: _Optional[str] = ..., name: _Optional[str] = ..., environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., status: _Optional[_Union[PublicStatusProto.Type, str]] = ..., created_by_user: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ..., last_action: _Optional[_Union[TimelineEventProto, _Mapping]] = ..., source_entity: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., sql_info: _Optional[_Union[CloneSummaryInfoProto.SQLInfo, _Mapping]] = ..., oracle_info: _Optional[_Union[CloneSummaryInfoProto.OracleInfo, _Mapping]] = ...) -> None: ...

class FetchClonesSummaryResult(_message.Message):
    __slots__ = ("base", "clone_summary_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CLONE_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    clone_summary_vec: _containers.RepeatedCompositeFieldContainer[CloneSummaryInfoProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., clone_summary_vec: _Optional[_Iterable[_Union[CloneSummaryInfoProto, _Mapping]]] = ...) -> None: ...

class AppTdmTaskSummaryProto(_message.Message):
    __slots__ = ("uid", "type", "name", "status", "error_detail", "start_timestamp_usecs", "end_timestamp_usecs", "pulse_path")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PULSE_PATH_FIELD_NUMBER: _ClassVar[int]
    uid: str
    type: _enum_wrappers_pb2.OperationProto
    name: str
    status: PublicStatusProto.Type
    error_detail: str
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    pulse_path: str
    def __init__(self, uid: _Optional[str] = ..., type: _Optional[_Union[_enum_wrappers_pb2.OperationProto, _Mapping]] = ..., name: _Optional[str] = ..., status: _Optional[_Union[PublicStatusProto.Type, str]] = ..., error_detail: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., pulse_path: _Optional[str] = ...) -> None: ...

class FetchAppTdmTasksSummaryArg(_message.Message):
    __slots__ = ("base", "filters")
    class Filters(_message.Message):
        __slots__ = ("task_types", "created_after_usecs", "created_before_usecs", "status", "uids", "environments", "clone_uids")
        TASK_TYPES_FIELD_NUMBER: _ClassVar[int]
        CREATED_AFTER_USECS_FIELD_NUMBER: _ClassVar[int]
        CREATED_BEFORE_USECS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UIDS_FIELD_NUMBER: _ClassVar[int]
        ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
        CLONE_UIDS_FIELD_NUMBER: _ClassVar[int]
        task_types: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.OperationProto]
        created_after_usecs: int
        created_before_usecs: int
        status: _containers.RepeatedScalarFieldContainer[PublicStatusProto.Type]
        uids: _containers.RepeatedScalarFieldContainer[str]
        environments: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.EnvironmentProto]
        clone_uids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, task_types: _Optional[_Iterable[_Union[_enum_wrappers_pb2.OperationProto, _Mapping]]] = ..., created_after_usecs: _Optional[int] = ..., created_before_usecs: _Optional[int] = ..., status: _Optional[_Iterable[_Union[PublicStatusProto.Type, str]]] = ..., uids: _Optional[_Iterable[str]] = ..., environments: _Optional[_Iterable[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]]] = ..., clone_uids: _Optional[_Iterable[str]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    filters: FetchAppTdmTasksSummaryArg.Filters
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., filters: _Optional[_Union[FetchAppTdmTasksSummaryArg.Filters, _Mapping]] = ...) -> None: ...

class FetchAppTdmTasksSummaryResult(_message.Message):
    __slots__ = ("base", "task_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_vec: _containers.RepeatedCompositeFieldContainer[AppTdmTaskSummaryProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_vec: _Optional[_Iterable[_Union[AppTdmTaskSummaryProto, _Mapping]]] = ...) -> None: ...

class FetchAppTdmTaskDetailsArg(_message.Message):
    __slots__ = ("base", "uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., uid: _Optional[str] = ...) -> None: ...

class FetchAppTdmTaskDetailsResult(_message.Message):
    __slots__ = ("base", "event_vec", "pulse_path", "name")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    PULSE_PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    event_vec: _containers.RepeatedCompositeFieldContainer[TimelineEventProto]
    pulse_path: str
    name: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., event_vec: _Optional[_Iterable[_Union[TimelineEventProto, _Mapping]]] = ..., pulse_path: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OperationOnCloneSpecProto(_message.Message):
    __slots__ = ("type", "user_description", "source_snapshot_uid", "snapshot_timestamp_usecs", "source_entity", "initiated_by_user", "sql_info", "oracle_info")
    class SQLInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class OracleInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_UID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    INITIATED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    ORACLE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _enum_wrappers_pb2.OperationProto
    user_description: str
    source_snapshot_uid: str
    snapshot_timestamp_usecs: int
    source_entity: _magneto_external_base_pb2.ObjectProto
    initiated_by_user: _permissions_external_pb2.UserInformationProto
    sql_info: OperationOnCloneSpecProto.SQLInfo
    oracle_info: OperationOnCloneSpecProto.OracleInfo
    def __init__(self, type: _Optional[_Union[_enum_wrappers_pb2.OperationProto, _Mapping]] = ..., user_description: _Optional[str] = ..., source_snapshot_uid: _Optional[str] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., source_entity: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., initiated_by_user: _Optional[_Union[_permissions_external_pb2.UserInformationProto, _Mapping]] = ..., sql_info: _Optional[_Union[OperationOnCloneSpecProto.SQLInfo, _Mapping]] = ..., oracle_info: _Optional[_Union[OperationOnCloneSpecProto.OracleInfo, _Mapping]] = ...) -> None: ...

class OperationOnCloneStatusProto(_message.Message):
    __slots__ = ("task_uid", "start_timestamp_usecs", "error_detail", "status", "end_timestamp_usecs", "sql_info", "oracle_info")
    class SQLInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class OracleInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    ORACLE_INFO_FIELD_NUMBER: _ClassVar[int]
    task_uid: str
    start_timestamp_usecs: int
    error_detail: str
    status: PublicStatusProto.Type
    end_timestamp_usecs: int
    sql_info: OperationOnCloneStatusProto.SQLInfo
    oracle_info: OperationOnCloneStatusProto.OracleInfo
    def __init__(self, task_uid: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., error_detail: _Optional[str] = ..., status: _Optional[_Union[PublicStatusProto.Type, str]] = ..., end_timestamp_usecs: _Optional[int] = ..., sql_info: _Optional[_Union[OperationOnCloneStatusProto.SQLInfo, _Mapping]] = ..., oracle_info: _Optional[_Union[OperationOnCloneStatusProto.OracleInfo, _Mapping]] = ...) -> None: ...

class TimelineEventProto(_message.Message):
    __slots__ = ("spec", "status", "incarnation_id")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    spec: OperationOnCloneSpecProto
    status: OperationOnCloneStatusProto
    incarnation_id: str
    def __init__(self, spec: _Optional[_Union[OperationOnCloneSpecProto, _Mapping]] = ..., status: _Optional[_Union[OperationOnCloneStatusProto, _Mapping]] = ..., incarnation_id: _Optional[str] = ...) -> None: ...

class FetchTimelineForCloneArg(_message.Message):
    __slots__ = ("base", "entity_uid", "start_timestamp_usecs", "end_timestamp_usecs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_uid: str
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_uid: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ...) -> None: ...

class FetchTimelineForCloneResult(_message.Message):
    __slots__ = ("base", "summary_info", "timeline_event_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    summary_info: CloneSummaryInfoProto
    timeline_event_vec: _containers.RepeatedCompositeFieldContainer[TimelineEventProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., summary_info: _Optional[_Union[CloneSummaryInfoProto, _Mapping]] = ..., timeline_event_vec: _Optional[_Iterable[_Union[TimelineEventProto, _Mapping]]] = ...) -> None: ...

class ViewParamsProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSnapshotOfClonesArg(_message.Message):
    __slots__ = ("base", "clone_uids", "snapshot_label")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CLONE_UIDS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    clone_uids: _containers.RepeatedScalarFieldContainer[str]
    snapshot_label: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., clone_uids: _Optional[_Iterable[str]] = ..., snapshot_label: _Optional[str] = ...) -> None: ...

class CreateSnapshotOfClonesResult(_message.Message):
    __slots__ = ("base", "missed_clone_uids", "task_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSED_CLONE_UIDS_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    missed_clone_uids: _containers.RepeatedScalarFieldContainer[str]
    task_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., missed_clone_uids: _Optional[_Iterable[str]] = ..., task_uid: _Optional[str] = ...) -> None: ...

class UpdateSnapshotOfCloneArg(_message.Message):
    __slots__ = ("base", "snapshot_uid", "snapshot_label")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    snapshot_uid: str
    snapshot_label: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., snapshot_uid: _Optional[str] = ..., snapshot_label: _Optional[str] = ...) -> None: ...

class UpdateSnapshotOfCloneResult(_message.Message):
    __slots__ = ("base", "snapshot_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    snapshot_info: _magneto_external_base_pb2.EntitySnapshotInfoProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., snapshot_info: _Optional[_Union[_magneto_external_base_pb2.EntitySnapshotInfoProto, _Mapping]] = ...) -> None: ...

class DeleteSnapshotsOfClonesArg(_message.Message):
    __slots__ = ("base", "snapshot_uids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UIDS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    snapshot_uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., snapshot_uids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteSnapshotsOfClonesResult(_message.Message):
    __slots__ = ("base", "task_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_uid: _Optional[str] = ...) -> None: ...

class CreateCloneArg(_message.Message):
    __slots__ = ("base", "snapshot_uid", "name", "username", "environment", "environment_params", "point_in_time_usecs", "target_host_entity_id", "pre_script", "post_script")
    class SqlCloneParams(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class OracleCloneParams(_message.Message):
        __slots__ = ("database_name", "base_dir", "home_dir", "database_file_destination", "sga_target_size", "no_open_mode")
        DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_DIR_FIELD_NUMBER: _ClassVar[int]
        HOME_DIR_FIELD_NUMBER: _ClassVar[int]
        DATABASE_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        SGA_TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
        NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
        database_name: str
        base_dir: str
        home_dir: str
        database_file_destination: str
        sga_target_size: str
        no_open_mode: bool
        def __init__(self, database_name: _Optional[str] = ..., base_dir: _Optional[str] = ..., home_dir: _Optional[str] = ..., database_file_destination: _Optional[str] = ..., sga_target_size: _Optional[str] = ..., no_open_mode: bool = ...) -> None: ...
    class EnvironmentParams(_message.Message):
        __slots__ = ("oracle_params", "sql_params")
        ORACLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        SQL_PARAMS_FIELD_NUMBER: _ClassVar[int]
        oracle_params: CreateCloneArg.OracleCloneParams
        sql_params: CreateCloneArg.SqlCloneParams
        def __init__(self, oracle_params: _Optional[_Union[CreateCloneArg.OracleCloneParams, _Mapping]] = ..., sql_params: _Optional[_Union[CreateCloneArg.SqlCloneParams, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    snapshot_uid: str
    name: str
    username: str
    environment: _enum_wrappers_pb2.EnvironmentProto
    environment_params: CreateCloneArg.EnvironmentParams
    point_in_time_usecs: int
    target_host_entity_id: int
    pre_script: _magneto_external_base_pb2.RemoteScriptProto
    post_script: _magneto_external_base_pb2.RemoteScriptProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., snapshot_uid: _Optional[str] = ..., name: _Optional[str] = ..., username: _Optional[str] = ..., environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., environment_params: _Optional[_Union[CreateCloneArg.EnvironmentParams, _Mapping]] = ..., point_in_time_usecs: _Optional[int] = ..., target_host_entity_id: _Optional[int] = ..., pre_script: _Optional[_Union[_magneto_external_base_pb2.RemoteScriptProto, _Mapping]] = ..., post_script: _Optional[_Union[_magneto_external_base_pb2.RemoteScriptProto, _Mapping]] = ...) -> None: ...

class CreateCloneResult(_message.Message):
    __slots__ = ("base", "task_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_uid: _Optional[str] = ...) -> None: ...

class CloneRefreshArg(_message.Message):
    __slots__ = ("base", "name", "clone_uid", "snapshot_uid", "point_in_time_usecs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_UID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UID_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    name: str
    clone_uid: str
    snapshot_uid: str
    point_in_time_usecs: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., name: _Optional[str] = ..., clone_uid: _Optional[str] = ..., snapshot_uid: _Optional[str] = ..., point_in_time_usecs: _Optional[int] = ...) -> None: ...

class CloneRefreshResult(_message.Message):
    __slots__ = ("base", "task_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_uid: _Optional[str] = ...) -> None: ...

class DestroyCloneArg(_message.Message):
    __slots__ = ("base", "clone_uid", "user")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CLONE_UID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    clone_uid: str
    user: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., clone_uid: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class DestroyCloneResult(_message.Message):
    __slots__ = ("base", "task_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_uid: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_uid: _Optional[str] = ...) -> None: ...

class LookupEntitiesArg(_message.Message):
    __slots__ = ("base", "entity_arg_vec", "fetch_linked_local_entities")
    class EntityArg(_message.Message):
        __slots__ = ("entity_id", "entity_external_metadata", "hash_string")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
        HASH_STRING_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        entity_external_metadata: _magneto_external_objects_pb2.EntityExternalMetadata
        hash_string: str
        def __init__(self, entity_id: _Optional[int] = ..., entity_external_metadata: _Optional[_Union[_magneto_external_objects_pb2.EntityExternalMetadata, _Mapping]] = ..., hash_string: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    FETCH_LINKED_LOCAL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_arg_vec: _containers.RepeatedCompositeFieldContainer[LookupEntitiesArg.EntityArg]
    fetch_linked_local_entities: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_arg_vec: _Optional[_Iterable[_Union[LookupEntitiesArg.EntityArg, _Mapping]]] = ..., fetch_linked_local_entities: bool = ...) -> None: ...

class LookupEntitiesResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class EntityResult(_message.Message):
        __slots__ = ("error", "entity", "linked_local_entity_vec")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        LINKED_LOCAL_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
        error: _magneto_external_base_pb2.ErrorProto
        entity: _magneto_external_base_pb2.ObjectProto
        linked_local_entity_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ObjectProto]
        def __init__(self, error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., entity: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., linked_local_entity_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[LookupEntitiesResult.EntityResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[LookupEntitiesResult.EntityResult, _Mapping]]] = ...) -> None: ...

class RunsFilterParams(_message.Message):
    __slots__ = ("only_return_basic_info", "run_info_type_vec", "targets", "backup_type_vec", "return_only_successful_runs")
    ONLY_RETURN_BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    RUN_INFO_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_SUCCESSFUL_RUNS_FIELD_NUMBER: _ClassVar[int]
    only_return_basic_info: bool
    run_info_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.RunInfoType.Type]
    targets: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.SnapshotTargetProto]
    backup_type_vec: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.MagnetoBackupType]
    return_only_successful_runs: bool
    def __init__(self, only_return_basic_info: bool = ..., run_info_type_vec: _Optional[_Iterable[_Union[_enums_pb2.RunInfoType.Type, str]]] = ..., targets: _Optional[_Iterable[_Union[_magneto_external_base_pb2.SnapshotTargetProto, _Mapping]]] = ..., backup_type_vec: _Optional[_Iterable[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]]] = ..., return_only_successful_runs: bool = ...) -> None: ...

class GetProtectionGroupRunsArg(_message.Message):
    __slots__ = ("base", "job_uid", "run_start_time_usecs", "time_interval", "filter_params", "object_id_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    time_interval: _magneto_external_base_pb2.TimeInterval
    filter_params: RunsFilterParams
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., time_interval: _Optional[_Union[_magneto_external_base_pb2.TimeInterval, _Mapping]] = ..., filter_params: _Optional[_Union[RunsFilterParams, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetProtectionGroupRunsResult(_message.Message):
    __slots__ = ("base", "protection_group_runs", "additional_protection_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUP_RUNS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROTECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    protection_group_runs: _containers.RepeatedCompositeFieldContainer[_magneto_external_objects_pb2.ProtectionGroupRunInfo]
    additional_protection_info: _magneto_external_objects_pb2.AdditionalProtectionInfo
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., protection_group_runs: _Optional[_Iterable[_Union[_magneto_external_objects_pb2.ProtectionGroupRunInfo, _Mapping]]] = ..., additional_protection_info: _Optional[_Union[_magneto_external_objects_pb2.AdditionalProtectionInfo, _Mapping]] = ...) -> None: ...

class GetObjectRunsArg(_message.Message):
    __slots__ = ("base", "object_id", "action_key", "job_uid", "time_interval", "run_start_time_usecs", "filter_params", "return_only_object_protection_runs", "return_detailed_object_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_OBJECT_PROTECTION_RUNS_FIELD_NUMBER: _ClassVar[int]
    RETURN_DETAILED_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_id: int
    action_key: _magneto_external_base_pb2.ObjectActionKey
    job_uid: _universal_id_pb2.UniversalIdProto
    time_interval: _magneto_external_base_pb2.TimeInterval
    run_start_time_usecs: int
    filter_params: RunsFilterParams
    return_only_object_protection_runs: bool
    return_detailed_object_info: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_id: _Optional[int] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., time_interval: _Optional[_Union[_magneto_external_base_pb2.TimeInterval, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., filter_params: _Optional[_Union[RunsFilterParams, _Mapping]] = ..., return_only_object_protection_runs: bool = ..., return_detailed_object_info: bool = ...) -> None: ...

class GetObjectRunsPaginationCookie(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...

class GetObjectRunsResult(_message.Message):
    __slots__ = ("base", "object_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    object_info: _magneto_external_objects_pb2.ObjectSummary
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., object_info: _Optional[_Union[_magneto_external_objects_pb2.ObjectSummary, _Mapping]] = ...) -> None: ...

class GetObjectsLastRunArg(_message.Message):
    __slots__ = ("base", "object_id_vec", "time_interval", "job_uid_vec", "filter_params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    time_interval: _magneto_external_base_pb2.TimeInterval
    job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    filter_params: RunsFilterParams
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ..., time_interval: _Optional[_Union[_magneto_external_base_pb2.TimeInterval, _Mapping]] = ..., job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., filter_params: _Optional[_Union[RunsFilterParams, _Mapping]] = ...) -> None: ...

class GetObjectsLastRunResult(_message.Message):
    __slots__ = ("base", "object_info_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_objects_pb2.ObjectSummary]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., object_info_vec: _Optional[_Iterable[_Union[_magneto_external_objects_pb2.ObjectSummary, _Mapping]]] = ...) -> None: ...

class NasAnalysisStatsArgJobInfo(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetNasAnalysisStatsArg(_message.Message):
    __slots__ = ("base", "job_info_vec", "run_start_time_usecs", "job_uid")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    job_info_vec: _containers.RepeatedCompositeFieldContainer[NasAnalysisStatsArgJobInfo]
    run_start_time_usecs: int
    job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., job_info_vec: _Optional[_Iterable[_Union[NasAnalysisStatsArgJobInfo, _Mapping]]] = ..., run_start_time_usecs: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class StatsBucket(_message.Message):
    __slots__ = ("file_type_tag", "file_size_tag", "access_time_tag", "mod_time_tag", "file_count", "total_size", "cell_id")
    FILE_TYPE_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_TAG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_TAG_FIELD_NUMBER: _ClassVar[int]
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    file_type_tag: str
    file_size_tag: str
    access_time_tag: str
    mod_time_tag: str
    file_count: int
    total_size: int
    cell_id: int
    def __init__(self, file_type_tag: _Optional[str] = ..., file_size_tag: _Optional[str] = ..., access_time_tag: _Optional[str] = ..., mod_time_tag: _Optional[str] = ..., file_count: _Optional[int] = ..., total_size: _Optional[int] = ..., cell_id: _Optional[int] = ...) -> None: ...

class ShareAnalysisInfo(_message.Message):
    __slots__ = ("status", "err_message", "share_id", "share_name", "bucket", "stats_attr")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    STATS_ATTR_FIELD_NUMBER: _ClassVar[int]
    status: _enum_wrappers_pb2.MagnetoPublicStatus
    err_message: str
    share_id: int
    share_name: str
    bucket: _containers.RepeatedCompositeFieldContainer[StatsBucket]
    stats_attr: _containers.RepeatedCompositeFieldContainer[AttrInfo]
    def __init__(self, status: _Optional[_Union[_enum_wrappers_pb2.MagnetoPublicStatus, _Mapping]] = ..., err_message: _Optional[str] = ..., share_id: _Optional[int] = ..., share_name: _Optional[str] = ..., bucket: _Optional[_Iterable[_Union[StatsBucket, _Mapping]]] = ..., stats_attr: _Optional[_Iterable[_Union[AttrInfo, _Mapping]]] = ...) -> None: ...

class BucketTag(_message.Message):
    __slots__ = ("bucket_label", "bucket_value")
    BUCKET_LABEL_FIELD_NUMBER: _ClassVar[int]
    BUCKET_VALUE_FIELD_NUMBER: _ClassVar[int]
    bucket_label: str
    bucket_value: str
    def __init__(self, bucket_label: _Optional[str] = ..., bucket_value: _Optional[str] = ...) -> None: ...

class AttrInfo(_message.Message):
    __slots__ = ("bucket_type", "bucket_tag")
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TAG_FIELD_NUMBER: _ClassVar[int]
    bucket_type: str
    bucket_tag: _containers.RepeatedCompositeFieldContainer[BucketTag]
    def __init__(self, bucket_type: _Optional[str] = ..., bucket_tag: _Optional[_Iterable[_Union[BucketTag, _Mapping]]] = ...) -> None: ...

class NasAnalysisStatsResultRunInfo(_message.Message):
    __slots__ = ("run_start_time_usecs", "share_record")
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SHARE_RECORD_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    share_record: _containers.RepeatedCompositeFieldContainer[ShareAnalysisInfo]
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., share_record: _Optional[_Iterable[_Union[ShareAnalysisInfo, _Mapping]]] = ...) -> None: ...

class NasAnalysisStatsResultJobInfo(_message.Message):
    __slots__ = ("job_uid", "entity_id", "run_record")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_RECORD_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    entity_id: _universal_id_pb2.UniversalIdProto
    run_record: _containers.RepeatedCompositeFieldContainer[NasAnalysisStatsResultRunInfo]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_record: _Optional[_Iterable[_Union[NasAnalysisStatsResultRunInfo, _Mapping]]] = ...) -> None: ...

class GetNasAnalysisStatsResult(_message.Message):
    __slots__ = ("base", "job_record", "entity_id", "share_record", "stats_attr")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_RECORD_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_RECORD_FIELD_NUMBER: _ClassVar[int]
    STATS_ATTR_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    job_record: _containers.RepeatedCompositeFieldContainer[NasAnalysisStatsResultJobInfo]
    entity_id: _universal_id_pb2.UniversalIdProto
    share_record: _containers.RepeatedCompositeFieldContainer[ShareAnalysisInfo]
    stats_attr: _containers.RepeatedCompositeFieldContainer[AttrInfo]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., job_record: _Optional[_Iterable[_Union[NasAnalysisStatsResultJobInfo, _Mapping]]] = ..., entity_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., share_record: _Optional[_Iterable[_Union[ShareAnalysisInfo, _Mapping]]] = ..., stats_attr: _Optional[_Iterable[_Union[AttrInfo, _Mapping]]] = ...) -> None: ...

class GetNasAnalysisDefaultConfigArg(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ...) -> None: ...

class GetNasAnalysisDefaultConfigResult(_message.Message):
    __slots__ = ("base", "stats_config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    stats_config: _containers.RepeatedCompositeFieldContainer[AttrInfo]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., stats_config: _Optional[_Iterable[_Union[AttrInfo, _Mapping]]] = ...) -> None: ...

class CreateObjectBackupArg(_message.Message):
    __slots__ = ("base", "common_backup_params", "object_groups", "is_paused", "activate_remote_object_protection", "use_existing_job_description_for_activation", "validation_only")
    class ObjectGroup(_message.Message):
        __slots__ = ("environment_type", "env_specific_params", "objects")
        class Object(_message.Message):
            __slots__ = ("object_id", "object_string_id", "object_specific_params")
            OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
            OBJECT_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
            object_id: int
            object_string_id: str
            object_specific_params: _object_protection_pb2.ObjectSpecificBackupParamsProto
            def __init__(self, object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., object_specific_params: _Optional[_Union[_object_protection_pb2.ObjectSpecificBackupParamsProto, _Mapping]] = ...) -> None: ...
        ENVIRONMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENV_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_FIELD_NUMBER: _ClassVar[int]
        environment_type: _enum_wrappers_pb2.EnvironmentProto
        env_specific_params: _object_protection_pb2.EnvSpecificBackupParamsProto
        objects: _containers.RepeatedCompositeFieldContainer[CreateObjectBackupArg.ObjectGroup.Object]
        def __init__(self, environment_type: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., env_specific_params: _Optional[_Union[_object_protection_pb2.EnvSpecificBackupParamsProto, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[CreateObjectBackupArg.ObjectGroup.Object, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_REMOTE_OBJECT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    USE_EXISTING_JOB_DESCRIPTION_FOR_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ONLY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    common_backup_params: _object_protection_pb2.CommonBackupParamsProto
    object_groups: _containers.RepeatedCompositeFieldContainer[CreateObjectBackupArg.ObjectGroup]
    is_paused: bool
    activate_remote_object_protection: bool
    use_existing_job_description_for_activation: bool
    validation_only: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., common_backup_params: _Optional[_Union[_object_protection_pb2.CommonBackupParamsProto, _Mapping]] = ..., object_groups: _Optional[_Iterable[_Union[CreateObjectBackupArg.ObjectGroup, _Mapping]]] = ..., is_paused: bool = ..., activate_remote_object_protection: bool = ..., use_existing_job_description_for_activation: bool = ..., validation_only: bool = ...) -> None: ...

class CreateObjectBackupResult(_message.Message):
    __slots__ = ("base", "protected_objects")
    class ProtectedObject(_message.Message):
        __slots__ = ("object", "error")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object: _magneto_external_base_pb2.ObjectProto
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, object: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    protected_objects: _containers.RepeatedCompositeFieldContainer[CreateObjectBackupResult.ProtectedObject]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., protected_objects: _Optional[_Iterable[_Union[CreateObjectBackupResult.ProtectedObject, _Mapping]]] = ...) -> None: ...

class UpdateObjectBackupArg(_message.Message):
    __slots__ = ("base", "object_id", "object_string_id", "object_specific_params", "env_specific_params", "common_backup_params", "action_key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENV_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_id: int
    object_string_id: str
    object_specific_params: _object_protection_pb2.ObjectSpecificBackupParamsProto
    env_specific_params: _object_protection_pb2.EnvSpecificBackupParamsProto
    common_backup_params: _object_protection_pb2.CommonBackupParamsProto
    action_key: _magneto_external_base_pb2.ObjectActionKey
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., object_specific_params: _Optional[_Union[_object_protection_pb2.ObjectSpecificBackupParamsProto, _Mapping]] = ..., env_specific_params: _Optional[_Union[_object_protection_pb2.EnvSpecificBackupParamsProto, _Mapping]] = ..., common_backup_params: _Optional[_Union[_object_protection_pb2.CommonBackupParamsProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...

class UpdateObjectBackupResult(_message.Message):
    __slots__ = ("base", "object", "action_key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    object: _magneto_external_base_pb2.ObjectProto
    action_key: _magneto_external_base_pb2.ObjectActionKey
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., object: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...

class GetProtectedObjectsPaginationCookie(_message.Message):
    __slots__ = ("entity_id", "action_key")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    action_key: _magneto_external_base_pb2.ObjectActionKey
    def __init__(self, entity_id: _Optional[int] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...

class GetProtectedObjectsArg(_message.Message):
    __slots__ = ("base", "object_id_vec", "action_key_vec", "policy_id_vec", "parent_id", "parent_action_key", "environment_type_vec", "only_protected_objects", "only_unprotected_objects", "only_leaf_objects", "only_auto_protected_objects", "return_object_backup_spec", "include_last_run_info", "return_detailed_object_info", "return_object_protections_count_only", "remove_exclude_source_ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ONLY_PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ONLY_UNPROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ONLY_LEAF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ONLY_AUTO_PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_OBJECT_BACKUP_SPEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LAST_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    RETURN_DETAILED_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    RETURN_OBJECT_PROTECTIONS_COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXCLUDE_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    action_key_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ObjectActionKey]
    policy_id_vec: _containers.RepeatedScalarFieldContainer[str]
    parent_id: int
    parent_action_key: _magneto_external_base_pb2.ObjectActionKey
    environment_type_vec: _containers.RepeatedCompositeFieldContainer[_enum_wrappers_pb2.EnvironmentProto]
    only_protected_objects: bool
    only_unprotected_objects: bool
    only_leaf_objects: bool
    only_auto_protected_objects: bool
    return_object_backup_spec: bool
    include_last_run_info: bool
    return_detailed_object_info: bool
    return_object_protections_count_only: bool
    remove_exclude_source_ids: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_id_vec: _Optional[_Iterable[int]] = ..., action_key_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]]] = ..., policy_id_vec: _Optional[_Iterable[str]] = ..., parent_id: _Optional[int] = ..., parent_action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ..., environment_type_vec: _Optional[_Iterable[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]]] = ..., only_protected_objects: bool = ..., only_unprotected_objects: bool = ..., only_leaf_objects: bool = ..., only_auto_protected_objects: bool = ..., return_object_backup_spec: bool = ..., include_last_run_info: bool = ..., return_detailed_object_info: bool = ..., return_object_protections_count_only: bool = ..., remove_exclude_source_ids: bool = ...) -> None: ...

class ListProtectionGroupsPaginationCookie(_message.Message):
    __slots__ = ("last_job_visited",)
    LAST_JOB_VISITED_FIELD_NUMBER: _ClassVar[int]
    last_job_visited: _universal_id_pb2.UniversalIdProto
    def __init__(self, last_job_visited: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ListProtectionGroupsArg(_message.Message):
    __slots__ = ("base", "return_only_paused_protection_groups", "return_only_deleted_protection_groups")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_PAUSED_PROTECTION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_DELETED_PROTECTION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    return_only_paused_protection_groups: bool
    return_only_deleted_protection_groups: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., return_only_paused_protection_groups: bool = ..., return_only_deleted_protection_groups: bool = ...) -> None: ...

class ListProtectionGroupsResult(_message.Message):
    __slots__ = ("base", "protection_groups_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUPS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    protection_groups_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ProtectionGroupSpec]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., protection_groups_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ProtectionGroupSpec, _Mapping]]] = ...) -> None: ...

class GetProtectedObjectsResult(_message.Message):
    __slots__ = ("base", "object_info_vec", "object_protections_count")
    class ObjectInfo(_message.Message):
        __slots__ = ("error", "object_id", "protection_groups_vec", "is_protected", "protected_atleast_once", "object_backup_spec_uid", "auto_protect_parent_spec_uid", "object_backup_configuration", "object_summary", "action_key")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_GROUPS_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_ATLEAST_ONCE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_BACKUP_SPEC_UID_FIELD_NUMBER: _ClassVar[int]
        AUTO_PROTECT_PARENT_SPEC_UID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_BACKUP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
        error: _magneto_external_base_pb2.ErrorProto
        object_id: int
        protection_groups_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ProtectionGroupSpec]
        is_protected: bool
        protected_atleast_once: bool
        object_backup_spec_uid: _universal_id_pb2.UniversalIdProto
        auto_protect_parent_spec_uid: _universal_id_pb2.UniversalIdProto
        object_backup_configuration: _object_protection_pb2.ObjectSpecInfo
        object_summary: _magneto_external_objects_pb2.ObjectSummary
        action_key: _magneto_external_base_pb2.ObjectActionKey
        def __init__(self, error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., object_id: _Optional[int] = ..., protection_groups_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ProtectionGroupSpec, _Mapping]]] = ..., is_protected: bool = ..., protected_atleast_once: bool = ..., object_backup_spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., auto_protect_parent_spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_backup_configuration: _Optional[_Union[_object_protection_pb2.ObjectSpecInfo, _Mapping]] = ..., object_summary: _Optional[_Union[_magneto_external_objects_pb2.ObjectSummary, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROTECTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    object_info_vec: _containers.RepeatedCompositeFieldContainer[GetProtectedObjectsResult.ObjectInfo]
    object_protections_count: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., object_info_vec: _Optional[_Iterable[_Union[GetProtectedObjectsResult.ObjectInfo, _Mapping]]] = ..., object_protections_count: _Optional[int] = ...) -> None: ...

class PerformObjectBackupActionArg(_message.Message):
    __slots__ = ("base", "object_ids", "object_string_ids", "action_type", "action_params", "action_keys")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STRING_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEYS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_ids: _containers.RepeatedScalarFieldContainer[int]
    object_string_ids: _containers.RepeatedScalarFieldContainer[str]
    action_type: _enums_pb2.ObjectBackupActionType.Type
    action_params: _magneto_external_base_pb2.ObjectBackupActionParams
    action_keys: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ObjectActionKey]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_ids: _Optional[_Iterable[int]] = ..., object_string_ids: _Optional[_Iterable[str]] = ..., action_type: _Optional[_Union[_enums_pb2.ObjectBackupActionType.Type, str]] = ..., action_params: _Optional[_Union[_magneto_external_base_pb2.ObjectBackupActionParams, _Mapping]] = ..., action_keys: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]]] = ...) -> None: ...

class PerformObjectBackupActionResult(_message.Message):
    __slots__ = ("base", "action_type", "action_status")
    class ActionStatus(_message.Message):
        __slots__ = ("object", "error", "action_key")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
        object: _magneto_external_base_pb2.ObjectProto
        error: _magneto_external_base_pb2.ErrorProto
        action_key: _magneto_external_base_pb2.ObjectActionKey
        def __init__(self, object: _Optional[_Union[_magneto_external_base_pb2.ObjectProto, _Mapping]] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    action_type: _enums_pb2.ObjectBackupActionType.Type
    action_status: _containers.RepeatedCompositeFieldContainer[PerformObjectBackupActionResult.ActionStatus]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., action_type: _Optional[_Union[_enums_pb2.ObjectBackupActionType.Type, str]] = ..., action_status: _Optional[_Iterable[_Union[PerformObjectBackupActionResult.ActionStatus, _Mapping]]] = ...) -> None: ...

class CancelObjectSnapshotArg(_message.Message):
    __slots__ = ("base", "object_snapshots_vec")
    class ObjectSnapshots(_message.Message):
        __slots__ = ("object_id", "snapshot_start_time_usecs_vec", "cancel_all_active_snapshots", "snapshot_target_vec", "cancel_all_snapshot_targets", "copy_snapshot_uid_vec", "action_key")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_START_TIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
        CANCEL_ALL_ACTIVE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
        CANCEL_ALL_SNAPSHOT_TARGETS_FIELD_NUMBER: _ClassVar[int]
        COPY_SNAPSHOT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        snapshot_start_time_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
        cancel_all_active_snapshots: bool
        snapshot_target_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.SnapshotTargetProto]
        cancel_all_snapshot_targets: bool
        copy_snapshot_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        action_key: _magneto_external_base_pb2.ObjectActionKey
        def __init__(self, object_id: _Optional[int] = ..., snapshot_start_time_usecs_vec: _Optional[_Iterable[int]] = ..., cancel_all_active_snapshots: bool = ..., snapshot_target_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.SnapshotTargetProto, _Mapping]]] = ..., cancel_all_snapshot_targets: bool = ..., copy_snapshot_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SNAPSHOTS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_snapshots_vec: _containers.RepeatedCompositeFieldContainer[CancelObjectSnapshotArg.ObjectSnapshots]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_snapshots_vec: _Optional[_Iterable[_Union[CancelObjectSnapshotArg.ObjectSnapshots, _Mapping]]] = ...) -> None: ...

class CancelObjectSnapshotResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class CancelResult(_message.Message):
        __slots__ = ("object_id", "error", "action_key", "cancelling_snapshot_start_time_usecs_vec", "cancelling_copy_runs_vec")
        class CancellingCopyTasks(_message.Message):
            __slots__ = ("backup_run_start_time", "copy_snapshot_uid_vec")
            BACKUP_RUN_START_TIME_FIELD_NUMBER: _ClassVar[int]
            COPY_SNAPSHOT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
            backup_run_start_time: int
            copy_snapshot_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
            def __init__(self, backup_run_start_time: _Optional[int] = ..., copy_snapshot_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
        CANCELLING_SNAPSHOT_START_TIME_USECS_VEC_FIELD_NUMBER: _ClassVar[int]
        CANCELLING_COPY_RUNS_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        error: _magneto_external_base_pb2.ErrorProto
        action_key: _magneto_external_base_pb2.ObjectActionKey
        cancelling_snapshot_start_time_usecs_vec: _containers.RepeatedScalarFieldContainer[int]
        cancelling_copy_runs_vec: _containers.RepeatedCompositeFieldContainer[CancelObjectSnapshotResult.CancelResult.CancellingCopyTasks]
        def __init__(self, object_id: _Optional[int] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ..., cancelling_snapshot_start_time_usecs_vec: _Optional[_Iterable[int]] = ..., cancelling_copy_runs_vec: _Optional[_Iterable[_Union[CancelObjectSnapshotResult.CancelResult.CancellingCopyTasks, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[CancelObjectSnapshotResult.CancelResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[CancelObjectSnapshotResult.CancelResult, _Mapping]]] = ...) -> None: ...

class UpdateEntityProvenanceEdgesArg(_message.Message):
    __slots__ = ("base", "action", "link_type", "source_target_entity_id_map")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnspecified: _ClassVar[UpdateEntityProvenanceEdgesArg.Action]
        kLink: _ClassVar[UpdateEntityProvenanceEdgesArg.Action]
        kUnlink: _ClassVar[UpdateEntityProvenanceEdgesArg.Action]
    kUnspecified: UpdateEntityProvenanceEdgesArg.Action
    kLink: UpdateEntityProvenanceEdgesArg.Action
    kUnlink: UpdateEntityProvenanceEdgesArg.Action
    class LinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[UpdateEntityProvenanceEdgesArg.LinkType]
        kReplication: _ClassVar[UpdateEntityProvenanceEdgesArg.LinkType]
        kFailoverRestore: _ClassVar[UpdateEntityProvenanceEdgesArg.LinkType]
        kVMMigration: _ClassVar[UpdateEntityProvenanceEdgesArg.LinkType]
    kUnused: UpdateEntityProvenanceEdgesArg.LinkType
    kReplication: UpdateEntityProvenanceEdgesArg.LinkType
    kFailoverRestore: UpdateEntityProvenanceEdgesArg.LinkType
    kVMMigration: UpdateEntityProvenanceEdgesArg.LinkType
    class SourceTargetEntityIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TARGET_ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    action: UpdateEntityProvenanceEdgesArg.Action
    link_type: UpdateEntityProvenanceEdgesArg.LinkType
    source_target_entity_id_map: _containers.ScalarMap[int, int]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., action: _Optional[_Union[UpdateEntityProvenanceEdgesArg.Action, str]] = ..., link_type: _Optional[_Union[UpdateEntityProvenanceEdgesArg.LinkType, str]] = ..., source_target_entity_id_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class UpdateEntityProvenanceEdgesResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class PauseProtectionGroupRunsArg(_message.Message):
    __slots__ = ("base", "run_and_task_ids_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_AND_TASK_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_and_task_ids_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.RunAndTaskIds]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_and_task_ids_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.RunAndTaskIds, _Mapping]]] = ...) -> None: ...

class PauseProtectionGroupRunsResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class PauseResult(_message.Message):
        __slots__ = ("job_instance_id", "error")
        JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        job_instance_id: int
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, job_instance_id: _Optional[int] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[PauseProtectionGroupRunsResult.PauseResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[PauseProtectionGroupRunsResult.PauseResult, _Mapping]]] = ...) -> None: ...

class ResumeProtectionGroupRunsArg(_message.Message):
    __slots__ = ("base", "run_and_task_ids_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_AND_TASK_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_and_task_ids_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.RunAndTaskIds]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_and_task_ids_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.RunAndTaskIds, _Mapping]]] = ...) -> None: ...

class ResumeProtectionGroupRunsResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class ResumeResult(_message.Message):
        __slots__ = ("job_instance_id", "error")
        JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        job_instance_id: int
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, job_instance_id: _Optional[int] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[ResumeProtectionGroupRunsResult.ResumeResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[ResumeProtectionGroupRunsResult.ResumeResult, _Mapping]]] = ...) -> None: ...

class StartExternallyTriggeredBackupArg(_message.Message):
    __slots__ = ("base", "session_id", "view_name", "tag", "job_instance_start_time", "job_params")
    class ExternallyTriggeredJobParams(_message.Message):
        __slots__ = ("client_type", "sbt_params")
        class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kGeneric: _ClassVar[StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType]
            kSbt: _ClassVar[StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType]
        kGeneric: StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType
        kSbt: StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType
        class ExternallyTriggeredSbtParams(_message.Message):
            __slots__ = ("catalog_view",)
            CATALOG_VIEW_FIELD_NUMBER: _ClassVar[int]
            catalog_view: str
            def __init__(self, catalog_view: _Optional[str] = ...) -> None: ...
        CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SBT_PARAMS_FIELD_NUMBER: _ClassVar[int]
        client_type: StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType
        sbt_params: StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ExternallyTriggeredSbtParams
        def __init__(self, client_type: _Optional[_Union[StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ClientType, str]] = ..., sbt_params: _Optional[_Union[StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams.ExternallyTriggeredSbtParams, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    session_id: int
    view_name: str
    tag: str
    job_instance_start_time: int
    job_params: StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., session_id: _Optional[int] = ..., view_name: _Optional[str] = ..., tag: _Optional[str] = ..., job_instance_start_time: _Optional[int] = ..., job_params: _Optional[_Union[StartExternallyTriggeredBackupArg.ExternallyTriggeredJobParams, _Mapping]] = ...) -> None: ...

class StartExternallyTriggeredBackupResult(_message.Message):
    __slots__ = ("base", "job_id", "job_instance_start_time", "snapshot_view_name")
    BASE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    job_id: int
    job_instance_start_time: int
    snapshot_view_name: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., job_id: _Optional[int] = ..., job_instance_start_time: _Optional[int] = ..., snapshot_view_name: _Optional[str] = ...) -> None: ...

class EndExternallyTriggeredBackupArg(_message.Message):
    __slots__ = ("base", "session_id", "job_id", "tag", "job_instance_start_time", "backup_error", "error_msg")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    session_id: int
    job_id: int
    tag: str
    job_instance_start_time: int
    backup_error: bool
    error_msg: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., session_id: _Optional[int] = ..., job_id: _Optional[int] = ..., tag: _Optional[str] = ..., job_instance_start_time: _Optional[int] = ..., backup_error: bool = ..., error_msg: _Optional[str] = ...) -> None: ...

class EndExternallyTriggeredBackupResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class ExternallyTriggeredKeepAliveArg(_message.Message):
    __slots__ = ("base", "session_id", "job_id", "tag", "job_instance_start_time", "verbose", "msg")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    session_id: int
    job_id: int
    tag: str
    job_instance_start_time: int
    verbose: int
    msg: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., session_id: _Optional[int] = ..., job_id: _Optional[int] = ..., tag: _Optional[str] = ..., job_instance_start_time: _Optional[int] = ..., verbose: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class ExternallyTriggeredKeepAliveResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class ExpandObjectBackupSourceCookie(_message.Message):
    __slots__ = ("object_id", "object_string_id", "last_leaf_object_id", "last_leaf_object_string_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_LEAF_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_LEAF_OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    object_string_id: str
    last_leaf_object_id: int
    last_leaf_object_string_id: str
    def __init__(self, object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., last_leaf_object_id: _Optional[int] = ..., last_leaf_object_string_id: _Optional[str] = ...) -> None: ...

class ExpandObjectBackupSourceResult(_message.Message):
    __slots__ = ("base", "protected_objects")
    class LeafObject(_message.Message):
        __slots__ = ("object_id", "object_string_id")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        object_string_id: str
        def __init__(self, object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ...) -> None: ...
    class ProtectedObject(_message.Message):
        __slots__ = ("object_id", "object_string_id", "leaf_objects", "error")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
        LEAF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        object_string_id: str
        leaf_objects: _containers.RepeatedCompositeFieldContainer[ExpandObjectBackupSourceResult.LeafObject]
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, object_id: _Optional[int] = ..., object_string_id: _Optional[str] = ..., leaf_objects: _Optional[_Iterable[_Union[ExpandObjectBackupSourceResult.LeafObject, _Mapping]]] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    protected_objects: _containers.RepeatedCompositeFieldContainer[ExpandObjectBackupSourceResult.ProtectedObject]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., protected_objects: _Optional[_Iterable[_Union[ExpandObjectBackupSourceResult.ProtectedObject, _Mapping]]] = ...) -> None: ...

class RestrictSourceEntitiesArg(_message.Message):
    __slots__ = ("base", "registered_source_id", "registered_source_string_id", "restricted_object_id_vec", "restricted_object_string_id_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_OBJECT_STRING_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    registered_source_id: int
    registered_source_string_id: str
    restricted_object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    restricted_object_string_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., registered_source_id: _Optional[int] = ..., registered_source_string_id: _Optional[str] = ..., restricted_object_id_vec: _Optional[_Iterable[int]] = ..., restricted_object_string_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RestrictSourceEntitiesResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ...) -> None: ...

class EditObjectBackupRunsMetadataArg(_message.Message):
    __slots__ = ("base", "object_run_identifier_vec", "time_range", "enable_legal_hold", "release_legal_hold", "retention_policy")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RUN_IDENTIFIER_VEC_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    RELEASE_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    object_run_identifier_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ObjectRunIdentifier]
    time_range: _magneto_external_base_pb2.TimeRangeUsecs
    enable_legal_hold: bool
    release_legal_hold: bool
    retention_policy: _retention_policy_pb2.RetentionPolicyProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., object_run_identifier_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ObjectRunIdentifier, _Mapping]]] = ..., time_range: _Optional[_Union[_magneto_external_base_pb2.TimeRangeUsecs, _Mapping]] = ..., enable_legal_hold: bool = ..., release_legal_hold: bool = ..., retention_policy: _Optional[_Union[_retention_policy_pb2.RetentionPolicyProto, _Mapping]] = ...) -> None: ...

class EditObjectBackupRunsMetadataResult(_message.Message):
    __slots__ = ("base", "edit_object_runs_vec")
    class ObjectRunResult(_message.Message):
        __slots__ = ("object", "err")
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        ERR_FIELD_NUMBER: _ClassVar[int]
        object: _magneto_external_base_pb2.ObjectRunIdentifier
        err: _magneto_external_base_pb2.ErrorProto
        def __init__(self, object: _Optional[_Union[_magneto_external_base_pb2.ObjectRunIdentifier, _Mapping]] = ..., err: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    EDIT_OBJECT_RUNS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    edit_object_runs_vec: _containers.RepeatedCompositeFieldContainer[EditObjectBackupRunsMetadataResult.ObjectRunResult]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., edit_object_runs_vec: _Optional[_Iterable[_Union[EditObjectBackupRunsMetadataResult.ObjectRunResult, _Mapping]]] = ...) -> None: ...
