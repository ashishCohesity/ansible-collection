from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DBInfo(_message.Message):
    __slots__ = ("name", "size_bytes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    size_bytes: int
    def __init__(self, name: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class DBsInfo(_message.Message):
    __slots__ = ("db_count", "db_info_vec")
    DB_COUNT_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_count: int
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DBInfo]
    def __init__(self, db_count: _Optional[int] = ..., db_info_vec: _Optional[_Iterable[_Union[DBInfo, _Mapping]]] = ...) -> None: ...
