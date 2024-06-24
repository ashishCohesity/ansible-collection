from librarian.base import schema_pb2 as _schema_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataStoreRowMetadata(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class IndexSchemaWrapper(_message.Message):
    __slots__ = ("index_schema", "bucket_incarnation_id")
    INDEX_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    index_schema: _schema_pb2.IndexSchema
    bucket_incarnation_id: int
    def __init__(self, index_schema: _Optional[_Union[_schema_pb2.IndexSchema, _Mapping]] = ..., bucket_incarnation_id: _Optional[int] = ...) -> None: ...

class CookieWrapper(_message.Message):
    __slots__ = ("cookie", "task_id", "bucket_incarnation_id", "index_incarnation_id")
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    cookie: bytes
    task_id: int
    bucket_incarnation_id: int
    index_incarnation_id: int
    def __init__(self, cookie: _Optional[bytes] = ..., task_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ...) -> None: ...
