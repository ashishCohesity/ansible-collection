from open_util.net import protorpc_pb2 as _protorpc_pb2
from scribe.base import scribe_pb2 as _scribe_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadCookie(_message.Message):
    __slots__ = ("start_key",)
    START_KEY_FIELD_NUMBER: _ClassVar[int]
    start_key: _scribe_pb2.RowColumnKey
    def __init__(self, start_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ...) -> None: ...

class GetNextArg(_message.Message):
    __slots__ = ("table_name", "columns", "batch_size", "cookie")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    columns: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
    batch_size: int
    cookie: bytes
    def __init__(self, table_name: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., batch_size: _Optional[int] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class GetNextResult(_message.Message):
    __slots__ = ("rows", "cookie")
    class RowData(_message.Message):
        __slots__ = ("key", "column_data")
        class ColumnData(_message.Message):
            __slots__ = ("name", "value")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: _scribe_pb2.RowColumnKey
            value: bytes
            def __init__(self, name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., value: _Optional[bytes] = ...) -> None: ...
        KEY_FIELD_NUMBER: _ClassVar[int]
        COLUMN_DATA_FIELD_NUMBER: _ClassVar[int]
        key: _scribe_pb2.RowColumnKey
        column_data: _containers.RepeatedCompositeFieldContainer[GetNextResult.RowData.ColumnData]
        def __init__(self, key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., column_data: _Optional[_Iterable[_Union[GetNextResult.RowData.ColumnData, _Mapping]]] = ...) -> None: ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[GetNextResult.RowData]
    cookie: bytes
    def __init__(self, rows: _Optional[_Iterable[_Union[GetNextResult.RowData, _Mapping]]] = ..., cookie: _Optional[bytes] = ...) -> None: ...
