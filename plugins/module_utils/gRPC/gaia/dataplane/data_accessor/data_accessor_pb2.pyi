from gaia.dataplane.api import api_pb2 as _api_pb2
from gaia.dataplane.api import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MasterWALRecordProto(_message.Message):
    __slots__ = ("latest_arg_vec",)
    LATEST_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    latest_arg_vec: _containers.RepeatedCompositeFieldContainer[_api_pb2.UpdateCleanupStateArg]
    def __init__(self, latest_arg_vec: _Optional[_Iterable[_Union[_api_pb2.UpdateCleanupStateArg, _Mapping]]] = ...) -> None: ...

class GetObjectsCookie(_message.Message):
    __slots__ = ("next_get_protected_objects_cookie", "next_object_id", "next_get_object_runs_cookie", "last_snapshot_id")
    NEXT_GET_PROTECTED_OBJECTS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    NEXT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_GET_OBJECT_RUNS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    next_get_protected_objects_cookie: bytes
    next_object_id: int
    next_get_object_runs_cookie: bytes
    last_snapshot_id: str
    def __init__(self, next_get_protected_objects_cookie: _Optional[bytes] = ..., next_object_id: _Optional[int] = ..., next_get_object_runs_cookie: _Optional[bytes] = ..., last_snapshot_id: _Optional[str] = ...) -> None: ...

class GaiaObjectProto(_message.Message):
    __slots__ = ("account_id", "tenant_id", "magneto_object_id", "object_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    magneto_object_id: int
    object_type: _base_pb2.Object.ObjectType
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., magneto_object_id: _Optional[int] = ..., object_type: _Optional[_Union[_base_pb2.Object.ObjectType, str]] = ...) -> None: ...

class DocumentIdProto(_message.Message):
    __slots__ = ("storage_id", "rocksdb_blob_snapfs_file_path")
    STORAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ROCKSDB_BLOB_SNAPFS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    storage_id: bytes
    rocksdb_blob_snapfs_file_path: str
    def __init__(self, storage_id: _Optional[bytes] = ..., rocksdb_blob_snapfs_file_path: _Optional[str] = ...) -> None: ...

class ListMailboxDocumentsCookie(_message.Message):
    __slots__ = ("next_document_proto", "next_offset")
    NEXT_DOCUMENT_PROTO_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    next_document_proto: DocumentIdProto
    next_offset: int
    def __init__(self, next_document_proto: _Optional[_Union[DocumentIdProto, _Mapping]] = ..., next_offset: _Optional[int] = ...) -> None: ...

class ListOneDriveDocumentsCookie(_message.Message):
    __slots__ = ("path_child_idx_vec",)
    PATH_CHILD_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    path_child_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, path_child_idx_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ListDocumentsCookie(_message.Message):
    __slots__ = ("mail_box_cookie", "one_drive_cookie")
    MAIL_BOX_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    mail_box_cookie: ListMailboxDocumentsCookie
    one_drive_cookie: ListOneDriveDocumentsCookie
    def __init__(self, mail_box_cookie: _Optional[_Union[ListMailboxDocumentsCookie, _Mapping]] = ..., one_drive_cookie: _Optional[_Union[ListOneDriveDocumentsCookie, _Mapping]] = ...) -> None: ...
