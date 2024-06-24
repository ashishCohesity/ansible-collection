from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.s3_portal.base import s3_error_pb2 as _s3_error_pb2
from magneto.object_walker import object_metadata_pb2 as _object_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateObjectArg(_message.Message):
    __slots__ = ("key", "bucket_name", "is_mega_file", "obj_metadata", "sub_file_size")
    KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    OBJ_METADATA_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    key: str
    bucket_name: str
    is_mega_file: bool
    obj_metadata: _object_metadata_pb2.ObjectMetadata
    sub_file_size: int
    def __init__(self, key: _Optional[str] = ..., bucket_name: _Optional[str] = ..., is_mega_file: bool = ..., obj_metadata: _Optional[_Union[_object_metadata_pb2.ObjectMetadata, _Mapping]] = ..., sub_file_size: _Optional[int] = ...) -> None: ...

class CreateObjectResult(_message.Message):
    __slots__ = ("object_eh", "error")
    OBJECT_EH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    object_eh: _entity_handle_pb2.EntityHandleProto
    error: _s3_error_pb2.S3ErrorProto
    def __init__(self, object_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., error: _Optional[_Union[_s3_error_pb2.S3ErrorProto, _Mapping]] = ...) -> None: ...

class FinalizeObjectArg(_message.Message):
    __slots__ = ("object_eh", "etag")
    OBJECT_EH_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    object_eh: _entity_handle_pb2.EntityHandleProto
    etag: str
    def __init__(self, object_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., etag: _Optional[str] = ...) -> None: ...

class FinalizeObjectResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _s3_error_pb2.S3ErrorProto
    def __init__(self, error: _Optional[_Union[_s3_error_pb2.S3ErrorProto, _Mapping]] = ...) -> None: ...

class GetObjectVersionsArg(_message.Message):
    __slots__ = ("bucket_name", "key")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    key: str
    def __init__(self, bucket_name: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class GetObjectVersionsResult(_message.Message):
    __slots__ = ("error", "entity_handles")
    class EntityHandleVersionTuple(_message.Message):
        __slots__ = ("version_id", "object_eh", "external_version_id")
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_EH_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        version_id: int
        object_eh: _entity_handle_pb2.EntityHandleProto
        external_version_id: str
        def __init__(self, version_id: _Optional[int] = ..., object_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., external_version_id: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLES_FIELD_NUMBER: _ClassVar[int]
    error: _s3_error_pb2.S3ErrorProto
    entity_handles: _containers.RepeatedCompositeFieldContainer[GetObjectVersionsResult.EntityHandleVersionTuple]
    def __init__(self, error: _Optional[_Union[_s3_error_pb2.S3ErrorProto, _Mapping]] = ..., entity_handles: _Optional[_Iterable[_Union[GetObjectVersionsResult.EntityHandleVersionTuple, _Mapping]]] = ...) -> None: ...

class DeleteObjectVersionArg(_message.Message):
    __slots__ = ("bucket_name", "key", "external_version_id")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    key: str
    external_version_id: str
    def __init__(self, bucket_name: _Optional[str] = ..., key: _Optional[str] = ..., external_version_id: _Optional[str] = ...) -> None: ...

class DeleteObjectVersionResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _s3_error_pb2.S3ErrorProto
    def __init__(self, error: _Optional[_Union[_s3_error_pb2.S3ErrorProto, _Mapping]] = ...) -> None: ...
