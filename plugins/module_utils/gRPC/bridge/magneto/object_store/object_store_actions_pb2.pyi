from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from nexus.cloud.base import credentials_pb2 as _credentials_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from magneto.object_walker import object_metadata_pb2 as _object_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCreate: _ClassVar[ObjectAction]
    kDelete: _ClassVar[ObjectAction]
kCreate: ObjectAction
kDelete: ObjectAction

class ObjectStoreActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "object_store", "action_type", "prepare_backup_arg", "cancel_task_arg", "list_objects_metadata_arg", "backup_object_area_arg", "delete_object_version_arg", "create_objects_arg", "finalize_cohesity_objects_arg", "finalize_s3_objects_arg", "abort_s3_objects_upload_arg", "restore_object_area_arg", "get_object_versions_arg", "end_backup_arg")
    class ObjectStoreActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kCancelTask: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kListObjectsMetadata: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kBackupObjectArea: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kDeleteObjectVersion: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kCreateObjects: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kFinalizeCohesityObjects: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kFinalizeS3Objects: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kAbortS3ObjectsUpload: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kEndSubTask: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kEndBackup: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kEndRestore: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kRestoreObjectAreas: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
        kGetObjectVersions: _ClassVar[ObjectStoreActionArg.ObjectStoreActionType]
    kPrepareBackup: ObjectStoreActionArg.ObjectStoreActionType
    kCancelTask: ObjectStoreActionArg.ObjectStoreActionType
    kListObjectsMetadata: ObjectStoreActionArg.ObjectStoreActionType
    kBackupObjectArea: ObjectStoreActionArg.ObjectStoreActionType
    kDeleteObjectVersion: ObjectStoreActionArg.ObjectStoreActionType
    kCreateObjects: ObjectStoreActionArg.ObjectStoreActionType
    kFinalizeCohesityObjects: ObjectStoreActionArg.ObjectStoreActionType
    kFinalizeS3Objects: ObjectStoreActionArg.ObjectStoreActionType
    kAbortS3ObjectsUpload: ObjectStoreActionArg.ObjectStoreActionType
    kEndSubTask: ObjectStoreActionArg.ObjectStoreActionType
    kEndBackup: ObjectStoreActionArg.ObjectStoreActionType
    kEndRestore: ObjectStoreActionArg.ObjectStoreActionType
    kRestoreObjectAreas: ObjectStoreActionArg.ObjectStoreActionType
    kGetObjectVersions: ObjectStoreActionArg.ObjectStoreActionType
    OBJECT_STORE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    object_store_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_OBJECTS_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OBJECT_AREA_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_VERSION_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_OBJECTS_ARG_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_COHESITY_OBJECTS_ARG_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_S3_OBJECTS_ARG_FIELD_NUMBER: _ClassVar[int]
    ABORT_S3_OBJECTS_UPLOAD_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_AREA_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_OBJECT_VERSIONS_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    object_store: ObjectStore
    action_type: ObjectStoreActionArg.ObjectStoreActionType
    prepare_backup_arg: PrepareBackupArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    list_objects_metadata_arg: ListObjectsMetadataArg
    backup_object_area_arg: BackupObjectAreaArg
    delete_object_version_arg: DeleteObjectVersionArg
    create_objects_arg: CreateObjectsArg
    finalize_cohesity_objects_arg: FinalizeCohesityObjectsArg
    finalize_s3_objects_arg: FinalizeS3ObjectsArg
    abort_s3_objects_upload_arg: AbortS3ObjectsUploadArg
    restore_object_area_arg: RestoreObjectAreasArg
    get_object_versions_arg: GetObjectVersionsArg
    end_backup_arg: EndBackupArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., object_store: _Optional[_Union[ObjectStore, _Mapping]] = ..., action_type: _Optional[_Union[ObjectStoreActionArg.ObjectStoreActionType, str]] = ..., prepare_backup_arg: _Optional[_Union[PrepareBackupArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., list_objects_metadata_arg: _Optional[_Union[ListObjectsMetadataArg, _Mapping]] = ..., backup_object_area_arg: _Optional[_Union[BackupObjectAreaArg, _Mapping]] = ..., delete_object_version_arg: _Optional[_Union[DeleteObjectVersionArg, _Mapping]] = ..., create_objects_arg: _Optional[_Union[CreateObjectsArg, _Mapping]] = ..., finalize_cohesity_objects_arg: _Optional[_Union[FinalizeCohesityObjectsArg, _Mapping]] = ..., finalize_s3_objects_arg: _Optional[_Union[FinalizeS3ObjectsArg, _Mapping]] = ..., abort_s3_objects_upload_arg: _Optional[_Union[AbortS3ObjectsUploadArg, _Mapping]] = ..., restore_object_area_arg: _Optional[_Union[RestoreObjectAreasArg, _Mapping]] = ..., get_object_versions_arg: _Optional[_Union[GetObjectVersionsArg, _Mapping]] = ..., end_backup_arg: _Optional[_Union[EndBackupArg, _Mapping]] = ...) -> None: ...

class ObjectStore(_message.Message):
    __slots__ = ("type", "name", "region", "object_level_acls_enabled", "aws_credentials")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_ACLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    type: _cluster_config_pb2.ClusterConfigProto.Vault.Type
    name: str
    region: str
    object_level_acls_enabled: bool
    aws_credentials: _credentials_pb2.AwsCredentials
    def __init__(self, type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.Type, str]] = ..., name: _Optional[str] = ..., region: _Optional[str] = ..., object_level_acls_enabled: bool = ..., aws_credentials: _Optional[_Union[_credentials_pb2.AwsCredentials, _Mapping]] = ...) -> None: ...

class PrepareBackupArg(_message.Message):
    __slots__ = ("base", "previous_view_name", "view_name", "s3_config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    previous_view_name: str
    view_name: str
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., previous_view_name: _Optional[str] = ..., view_name: _Optional[str] = ..., s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ...) -> None: ...

class EndBackupArg(_message.Message):
    __slots__ = ("base", "entities_in_config_to_delete")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_IN_CONFIG_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    entities_in_config_to_delete: _containers.RepeatedCompositeFieldContainer[_directory_walker_pb2.EntityMetadata]
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., entities_in_config_to_delete: _Optional[_Iterable[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]]] = ...) -> None: ...

class ListObjectsMetadataArg(_message.Message):
    __slots__ = ("start_after_key", "end_key", "continuation_token", "include_versions", "prefix", "include_acls")
    START_AFTER_KEY_FIELD_NUMBER: _ClassVar[int]
    END_KEY_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACLS_FIELD_NUMBER: _ClassVar[int]
    start_after_key: str
    end_key: str
    continuation_token: str
    include_versions: bool
    prefix: str
    include_acls: bool
    def __init__(self, start_after_key: _Optional[str] = ..., end_key: _Optional[str] = ..., continuation_token: _Optional[str] = ..., include_versions: bool = ..., prefix: _Optional[str] = ..., include_acls: bool = ...) -> None: ...

class BackupObjectAreaArg(_message.Message):
    __slots__ = ("base", "object_area_info_vec")
    class ObjectAreaInfo(_message.Message):
        __slots__ = ("object_area", "eh")
        OBJECT_AREA_FIELD_NUMBER: _ClassVar[int]
        EH_FIELD_NUMBER: _ClassVar[int]
        object_area: ObjectArea
        eh: _entity_handle_pb2.EntityHandleProto
        def __init__(self, object_area: _Optional[_Union[ObjectArea, _Mapping]] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AREA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    object_area_info_vec: _containers.RepeatedCompositeFieldContainer[BackupObjectAreaArg.ObjectAreaInfo]
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., object_area_info_vec: _Optional[_Iterable[_Union[BackupObjectAreaArg.ObjectAreaInfo, _Mapping]]] = ...) -> None: ...

class ObjectInfo(_message.Message):
    __slots__ = ("key", "version_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    version_id: str
    def __init__(self, key: _Optional[str] = ..., version_id: _Optional[str] = ...) -> None: ...

class ObjectArea(_message.Message):
    __slots__ = ("object_info", "start_offset", "length", "object_metadata")
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    object_info: ObjectInfo
    start_offset: int
    length: int
    object_metadata: _object_metadata_pb2.ObjectMetadata
    def __init__(self, object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., start_offset: _Optional[int] = ..., length: _Optional[int] = ..., object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ...) -> None: ...

class CreateObjectsArg(_message.Message):
    __slots__ = ("object_action_info_vec", "min_mega_file_size_mb", "sub_file_size")
    class ObjectActionInfo(_message.Message):
        __slots__ = ("object_metadata", "object_action")
        OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ACTION_FIELD_NUMBER: _ClassVar[int]
        object_metadata: _object_metadata_pb2.ObjectMetadata
        object_action: ObjectAction
        def __init__(self, object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., object_action: _Optional[_Union[ObjectAction, str]] = ...) -> None: ...
    OBJECT_ACTION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MIN_MEGA_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    object_action_info_vec: _containers.RepeatedCompositeFieldContainer[CreateObjectsArg.ObjectActionInfo]
    min_mega_file_size_mb: int
    sub_file_size: int
    def __init__(self, object_action_info_vec: _Optional[_Iterable[_Union[CreateObjectsArg.ObjectActionInfo, _Mapping]]] = ..., min_mega_file_size_mb: _Optional[int] = ..., sub_file_size: _Optional[int] = ...) -> None: ...

class FinalizeCohesityObjectsArg(_message.Message):
    __slots__ = ("finalize_object_vec",)
    class FinalizeCohesityObjectInfo(_message.Message):
        __slots__ = ("eh", "etag")
        EH_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        etag: str
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., etag: _Optional[str] = ...) -> None: ...
    FINALIZE_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    finalize_object_vec: _containers.RepeatedCompositeFieldContainer[FinalizeCohesityObjectsArg.FinalizeCohesityObjectInfo]
    def __init__(self, finalize_object_vec: _Optional[_Iterable[_Union[FinalizeCohesityObjectsArg.FinalizeCohesityObjectInfo, _Mapping]]] = ...) -> None: ...

class DeleteObjectVersionArg(_message.Message):
    __slots__ = ("object_info",)
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    object_info: ObjectInfo
    def __init__(self, object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ...) -> None: ...

class FinalizeS3ObjectsArg(_message.Message):
    __slots__ = ("finalize_objects_vec",)
    class FinalizeS3ObjectInfo(_message.Message):
        __slots__ = ("object_info", "upload_id", "part_info_vec")
        class PartInfo(_message.Message):
            __slots__ = ("part_id", "etag")
            PART_ID_FIELD_NUMBER: _ClassVar[int]
            ETAG_FIELD_NUMBER: _ClassVar[int]
            part_id: int
            etag: str
            def __init__(self, part_id: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...
        OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        PART_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        object_info: ObjectInfo
        upload_id: str
        part_info_vec: _containers.RepeatedCompositeFieldContainer[FinalizeS3ObjectsArg.FinalizeS3ObjectInfo.PartInfo]
        def __init__(self, object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., upload_id: _Optional[str] = ..., part_info_vec: _Optional[_Iterable[_Union[FinalizeS3ObjectsArg.FinalizeS3ObjectInfo.PartInfo, _Mapping]]] = ...) -> None: ...
    FINALIZE_OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    finalize_objects_vec: _containers.RepeatedCompositeFieldContainer[FinalizeS3ObjectsArg.FinalizeS3ObjectInfo]
    def __init__(self, finalize_objects_vec: _Optional[_Iterable[_Union[FinalizeS3ObjectsArg.FinalizeS3ObjectInfo, _Mapping]]] = ...) -> None: ...

class AbortS3ObjectsUploadArg(_message.Message):
    __slots__ = ("objects_upload_info_vec",)
    class ObjectUploadInfo(_message.Message):
        __slots__ = ("object_info", "upload_id")
        OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        object_info: ObjectInfo
        upload_id: str
        def __init__(self, object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., upload_id: _Optional[str] = ...) -> None: ...
    OBJECTS_UPLOAD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    objects_upload_info_vec: _containers.RepeatedCompositeFieldContainer[AbortS3ObjectsUploadArg.ObjectUploadInfo]
    def __init__(self, objects_upload_info_vec: _Optional[_Iterable[_Union[AbortS3ObjectsUploadArg.ObjectUploadInfo, _Mapping]]] = ...) -> None: ...

class RestoreObjectAreasArg(_message.Message):
    __slots__ = ("base", "object_area_info_vec")
    class ObjectAreaInfo(_message.Message):
        __slots__ = ("object_area", "upload_id", "part_id", "eh")
        OBJECT_AREA_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        PART_ID_FIELD_NUMBER: _ClassVar[int]
        EH_FIELD_NUMBER: _ClassVar[int]
        object_area: ObjectArea
        upload_id: str
        part_id: int
        eh: _entity_handle_pb2.EntityHandleProto
        def __init__(self, object_area: _Optional[_Union[ObjectArea, _Mapping]] = ..., upload_id: _Optional[str] = ..., part_id: _Optional[int] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AREA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    object_area_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreObjectAreasArg.ObjectAreaInfo]
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., object_area_info_vec: _Optional[_Iterable[_Union[RestoreObjectAreasArg.ObjectAreaInfo, _Mapping]]] = ...) -> None: ...

class GetObjectVersionsArg(_message.Message):
    __slots__ = ("object_key_vec",)
    OBJECT_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    object_key_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_key_vec: _Optional[_Iterable[str]] = ...) -> None: ...
