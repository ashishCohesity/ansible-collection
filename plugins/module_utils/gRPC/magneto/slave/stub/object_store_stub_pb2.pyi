from bridge.base import error_pb2 as _error_pb2
from bridge.magneto.object_store import object_store_actions_pb2 as _object_store_actions_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.object_walker import object_metadata_pb2 as _object_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectStoreActionUpdateArg(_message.Message):
    __slots__ = ("type", "list_objects_metadata_result", "backup_objects_area_result", "create_objects_result", "finalize_cohesity_objects_result", "finalize_s3_objects_result", "abort_s3_objects_upload_result", "restore_object_area_result", "get_object_versions_result")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackupUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kListObjectsMetadataUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kBackupObjectAreaUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kCreateObjectsUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kFinalizeCohesityObjectsUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kFinalizeS3ObjectsUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kAbortS3ObjectsUploadUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kRestoreObjectAreasUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
        kGetObjectVersionsUpdate: _ClassVar[ObjectStoreActionUpdateArg.Type]
    kPrepareBackupUpdate: ObjectStoreActionUpdateArg.Type
    kListObjectsMetadataUpdate: ObjectStoreActionUpdateArg.Type
    kBackupObjectAreaUpdate: ObjectStoreActionUpdateArg.Type
    kCreateObjectsUpdate: ObjectStoreActionUpdateArg.Type
    kFinalizeCohesityObjectsUpdate: ObjectStoreActionUpdateArg.Type
    kFinalizeS3ObjectsUpdate: ObjectStoreActionUpdateArg.Type
    kAbortS3ObjectsUploadUpdate: ObjectStoreActionUpdateArg.Type
    kEndSubTaskUpdate: ObjectStoreActionUpdateArg.Type
    kEndBackupUpdate: ObjectStoreActionUpdateArg.Type
    kEndRestoreUpdate: ObjectStoreActionUpdateArg.Type
    kRestoreObjectAreasUpdate: ObjectStoreActionUpdateArg.Type
    kGetObjectVersionsUpdate: ObjectStoreActionUpdateArg.Type
    OBJECT_STORE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    object_store_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_OBJECTS_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OBJECTS_AREA_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_OBJECTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_COHESITY_OBJECTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_S3_OBJECTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    ABORT_S3_OBJECTS_UPLOAD_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_AREA_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_OBJECT_VERSIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    type: ObjectStoreActionUpdateArg.Type
    list_objects_metadata_result: ListObjectsMetadataResult
    backup_objects_area_result: BackupObjectsAreaResult
    create_objects_result: CreateObjectsResult
    finalize_cohesity_objects_result: FinalizeCohesityObjectsResult
    finalize_s3_objects_result: FinalizeS3ObjectsResult
    abort_s3_objects_upload_result: AbortS3ObjectsUploadResult
    restore_object_area_result: RestoreObjectAreasResult
    get_object_versions_result: GetObjectVersionsResult
    def __init__(self, type: _Optional[_Union[ObjectStoreActionUpdateArg.Type, str]] = ..., list_objects_metadata_result: _Optional[_Union[ListObjectsMetadataResult, _Mapping]] = ..., backup_objects_area_result: _Optional[_Union[BackupObjectsAreaResult, _Mapping]] = ..., create_objects_result: _Optional[_Union[CreateObjectsResult, _Mapping]] = ..., finalize_cohesity_objects_result: _Optional[_Union[FinalizeCohesityObjectsResult, _Mapping]] = ..., finalize_s3_objects_result: _Optional[_Union[FinalizeS3ObjectsResult, _Mapping]] = ..., abort_s3_objects_upload_result: _Optional[_Union[AbortS3ObjectsUploadResult, _Mapping]] = ..., restore_object_area_result: _Optional[_Union[RestoreObjectAreasResult, _Mapping]] = ..., get_object_versions_result: _Optional[_Union[GetObjectVersionsResult, _Mapping]] = ...) -> None: ...

class ListObjectsMetadataResult(_message.Message):
    __slots__ = ("next_continuation_token", "object_metadata_vec")
    NEXT_CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    next_continuation_token: str
    object_metadata_vec: _containers.RepeatedCompositeFieldContainer[_object_metadata_pb2.ObjectMetadata]
    def __init__(self, next_continuation_token: _Optional[str] = ..., object_metadata_vec: _Optional[_Iterable[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]]] = ...) -> None: ...

class CreateObjectsResult(_message.Message):
    __slots__ = ("created_object_info_vec",)
    class CreatedObjectInfo(_message.Message):
        __slots__ = ("object_metadata", "eh", "error", "object_action", "upload_id")
        OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        EH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ACTION_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        object_metadata: _object_metadata_pb2.ObjectMetadata
        eh: _entity_handle_pb2.EntityHandleProto
        error: _error_pb2.ErrorProto
        object_action: _object_store_actions_pb2.ObjectAction
        upload_id: str
        def __init__(self, object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_action: _Optional[_Union[_object_store_actions_pb2.ObjectAction, str]] = ..., upload_id: _Optional[str] = ...) -> None: ...
    CREATED_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    created_object_info_vec: _containers.RepeatedCompositeFieldContainer[CreateObjectsResult.CreatedObjectInfo]
    def __init__(self, created_object_info_vec: _Optional[_Iterable[_Union[CreateObjectsResult.CreatedObjectInfo, _Mapping]]] = ...) -> None: ...

class GetObjectVersionsResult(_message.Message):
    __slots__ = ("get_object_info_vec",)
    class EHVersionsTuple(_message.Message):
        __slots__ = ("eh", "internal_version_id", "external_version_id")
        EH_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        internal_version_id: int
        external_version_id: str
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., internal_version_id: _Optional[int] = ..., external_version_id: _Optional[str] = ...) -> None: ...
    class ObjectVersionInfo(_message.Message):
        __slots__ = ("key", "object_versions", "error")
        KEY_FIELD_NUMBER: _ClassVar[int]
        OBJECT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        key: str
        object_versions: _containers.RepeatedCompositeFieldContainer[GetObjectVersionsResult.EHVersionsTuple]
        error: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., object_versions: _Optional[_Iterable[_Union[GetObjectVersionsResult.EHVersionsTuple, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    GET_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    get_object_info_vec: _containers.RepeatedCompositeFieldContainer[GetObjectVersionsResult.ObjectVersionInfo]
    def __init__(self, get_object_info_vec: _Optional[_Iterable[_Union[GetObjectVersionsResult.ObjectVersionInfo, _Mapping]]] = ...) -> None: ...

class FinalizeCohesityObjectsResult(_message.Message):
    __slots__ = ("finalize_eh_info_vec",)
    class FinalizeEHInfo(_message.Message):
        __slots__ = ("eh", "error")
        EH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        error: _error_pb2.ErrorProto
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    FINALIZE_EH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    finalize_eh_info_vec: _containers.RepeatedCompositeFieldContainer[FinalizeCohesityObjectsResult.FinalizeEHInfo]
    def __init__(self, finalize_eh_info_vec: _Optional[_Iterable[_Union[FinalizeCohesityObjectsResult.FinalizeEHInfo, _Mapping]]] = ...) -> None: ...

class FinalizeS3ObjectsResult(_message.Message):
    __slots__ = ("finalize_s3_objects_info_vec",)
    class FinalizeS3ObjectInfo(_message.Message):
        __slots__ = ("object_metadata", "etag", "error")
        OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object_metadata: _object_metadata_pb2.ObjectMetadata
        etag: str
        error: _error_pb2.ErrorProto
        def __init__(self, object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., etag: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    FINALIZE_S3_OBJECTS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    finalize_s3_objects_info_vec: _containers.RepeatedCompositeFieldContainer[FinalizeS3ObjectsResult.FinalizeS3ObjectInfo]
    def __init__(self, finalize_s3_objects_info_vec: _Optional[_Iterable[_Union[FinalizeS3ObjectsResult.FinalizeS3ObjectInfo, _Mapping]]] = ...) -> None: ...

class AbortS3ObjectsUploadResult(_message.Message):
    __slots__ = ("abort_upload_info_vec",)
    class AbortUploadInfo(_message.Message):
        __slots__ = ("object_metadata", "error")
        OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object_metadata: _object_metadata_pb2.ObjectMetadata
        error: _error_pb2.ErrorProto
        def __init__(self, object_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ABORT_UPLOAD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    abort_upload_info_vec: _containers.RepeatedCompositeFieldContainer[AbortS3ObjectsUploadResult.AbortUploadInfo]
    def __init__(self, abort_upload_info_vec: _Optional[_Iterable[_Union[AbortS3ObjectsUploadResult.AbortUploadInfo, _Mapping]]] = ...) -> None: ...

class BackupObjectsAreaResult(_message.Message):
    __slots__ = ("backup_objects_area_result_info_vec",)
    class BackupObjectsAreaResultInfo(_message.Message):
        __slots__ = ("result_info", "key", "version_id")
        RESULT_INFO_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        result_info: _stub_pb2.BackupDiskUpdateArg
        key: str
        version_id: str
        def __init__(self, result_info: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., key: _Optional[str] = ..., version_id: _Optional[str] = ...) -> None: ...
    BACKUP_OBJECTS_AREA_RESULT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_objects_area_result_info_vec: _containers.RepeatedCompositeFieldContainer[BackupObjectsAreaResult.BackupObjectsAreaResultInfo]
    def __init__(self, backup_objects_area_result_info_vec: _Optional[_Iterable[_Union[BackupObjectsAreaResult.BackupObjectsAreaResultInfo, _Mapping]]] = ...) -> None: ...

class RestoreObjectAreasResult(_message.Message):
    __slots__ = ("restore_object_area_result_info_vec",)
    class RestoreObjectAreaResultInfo(_message.Message):
        __slots__ = ("result_info", "key", "version_id", "part_id", "ctag")
        RESULT_INFO_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        PART_ID_FIELD_NUMBER: _ClassVar[int]
        CTAG_FIELD_NUMBER: _ClassVar[int]
        result_info: _stub_pb2.RestoreDiskUpdateArg
        key: str
        version_id: str
        part_id: int
        ctag: str
        def __init__(self, result_info: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., key: _Optional[str] = ..., version_id: _Optional[str] = ..., part_id: _Optional[int] = ..., ctag: _Optional[str] = ...) -> None: ...
    RESTORE_OBJECT_AREA_RESULT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_object_area_result_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreObjectAreasResult.RestoreObjectAreaResultInfo]
    def __init__(self, restore_object_area_result_info_vec: _Optional[_Iterable[_Union[RestoreObjectAreasResult.RestoreObjectAreaResultInfo, _Mapping]]] = ...) -> None: ...
