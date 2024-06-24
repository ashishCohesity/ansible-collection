from librarian.base import config_pb2 as _config_pb2
from librarian.base import error_pb2 as _error_pb2
from librarian.base import librarian_pb2 as _librarian_pb2
from librarian.base import schema_pb2 as _schema_pb2
from librarian.master import wal_entry_pb2 as _wal_entry_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateConfigArg(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _config_pb2.Config
    def __init__(self, config: _Optional[_Union[_config_pb2.Config, _Mapping]] = ...) -> None: ...

class UpdateConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateIndexArg(_message.Message):
    __slots__ = ("index_info",)
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    index_info: _config_pb2.IndexInfo
    def __init__(self, index_info: _Optional[_Union[_config_pb2.IndexInfo, _Mapping]] = ...) -> None: ...

class CreateIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteIndexArg(_message.Message):
    __slots__ = ("index_info",)
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    index_info: _config_pb2.IndexInfo
    def __init__(self, index_info: _Optional[_Union[_config_pb2.IndexInfo, _Mapping]] = ...) -> None: ...

class DeleteIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIndexArg(_message.Message):
    __slots__ = ("index_info",)
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    index_info: _config_pb2.IndexInfo
    def __init__(self, index_info: _Optional[_Union[_config_pb2.IndexInfo, _Mapping]] = ...) -> None: ...

class UpdateIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexMigrationTaskArg(_message.Message):
    __slots__ = ("index_name", "incarnation_id", "tasks_vec")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    incarnation_id: int
    tasks_vec: _containers.RepeatedCompositeFieldContainer[_wal_entry_pb2.UpdateIntent]
    def __init__(self, index_name: _Optional[str] = ..., incarnation_id: _Optional[int] = ..., tasks_vec: _Optional[_Iterable[_Union[_wal_entry_pb2.UpdateIntent, _Mapping]]] = ...) -> None: ...

class IndexMigrationTaskResult(_message.Message):
    __slots__ = ("task_status_vec",)
    class SingleTaskStatus(_message.Message):
        __slots__ = ("error", "task_id")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        task_id: int
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...
    TASK_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    task_status_vec: _containers.RepeatedCompositeFieldContainer[IndexMigrationTaskResult.SingleTaskStatus]
    def __init__(self, task_status_vec: _Optional[_Iterable[_Union[IndexMigrationTaskResult.SingleTaskStatus, _Mapping]]] = ...) -> None: ...

class ReplicateDocumentsArg(_message.Message):
    __slots__ = ("index_name", "doc_id_vec", "doc_data_vec", "bucket_id", "destination_disk_id", "source_bucket_incarnation_id", "destination_bucket_incarnation_id", "destination_session_id", "commit", "index_incarnation_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DOC_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    doc_id_vec: _containers.RepeatedScalarFieldContainer[str]
    doc_data_vec: _containers.RepeatedScalarFieldContainer[bytes]
    bucket_id: int
    destination_disk_id: int
    source_bucket_incarnation_id: int
    destination_bucket_incarnation_id: int
    destination_session_id: int
    commit: bool
    index_incarnation_id: int
    def __init__(self, index_name: _Optional[str] = ..., doc_id_vec: _Optional[_Iterable[str]] = ..., doc_data_vec: _Optional[_Iterable[bytes]] = ..., bucket_id: _Optional[int] = ..., destination_disk_id: _Optional[int] = ..., source_bucket_incarnation_id: _Optional[int] = ..., destination_bucket_incarnation_id: _Optional[int] = ..., destination_session_id: _Optional[int] = ..., commit: bool = ..., index_incarnation_id: _Optional[int] = ...) -> None: ...

class ReplicateDocumentsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateReplicaHandleArg(_message.Message):
    __slots__ = ("index_name", "index_schema", "bucket_id", "disk_id", "bucket_incarnation_id", "index_incarnation_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    index_schema: _schema_pb2.IndexSchema
    bucket_id: int
    disk_id: int
    bucket_incarnation_id: int
    index_incarnation_id: int
    def __init__(self, index_name: _Optional[str] = ..., index_schema: _Optional[_Union[_schema_pb2.IndexSchema, _Mapping]] = ..., bucket_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ...) -> None: ...

class CreateReplicaHandleResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
