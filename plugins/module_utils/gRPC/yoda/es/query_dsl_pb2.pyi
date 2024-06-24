from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryDsl(_message.Message):
    __slots__ = ("query", "filter", "filtered")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FILTERED_FIELD_NUMBER: _ClassVar[int]
    query: Query
    filter: Filter
    filtered: FilteredQuery
    def __init__(self, query: _Optional[_Union[Query, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., filtered: _Optional[_Union[FilteredQuery, _Mapping]] = ...) -> None: ...

class FilteredQuery(_message.Message):
    __slots__ = ("query", "filter")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    query: Query
    filter: Filter
    def __init__(self, query: _Optional[_Union[Query, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class StringStringMapEntry(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: str
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...

class MapEntryStringMap(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: _containers.RepeatedCompositeFieldContainer[MapEntryStringInt]
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[_Iterable[_Union[MapEntryStringInt, _Mapping]]] = ...) -> None: ...

class MapEntryStringInt(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: int
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[int] = ...) -> None: ...

class Query(_message.Message):
    __slots__ = ("term_query", "prefix_query", "query_string_query", "range_query")
    TERM_QUERY_FIELD_NUMBER: _ClassVar[int]
    PREFIX_QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRING_QUERY_FIELD_NUMBER: _ClassVar[int]
    RANGE_QUERY_FIELD_NUMBER: _ClassVar[int]
    term_query: _containers.RepeatedCompositeFieldContainer[StringStringMapEntry]
    prefix_query: _containers.RepeatedCompositeFieldContainer[StringStringMapEntry]
    query_string_query: QueryStringQuery
    range_query: _containers.RepeatedCompositeFieldContainer[MapEntryStringMap]
    def __init__(self, term_query: _Optional[_Iterable[_Union[StringStringMapEntry, _Mapping]]] = ..., prefix_query: _Optional[_Iterable[_Union[StringStringMapEntry, _Mapping]]] = ..., query_string_query: _Optional[_Union[QueryStringQuery, _Mapping]] = ..., range_query: _Optional[_Iterable[_Union[MapEntryStringMap, _Mapping]]] = ...) -> None: ...

class QueryStringQuery(_message.Message):
    __slots__ = ("query", "default_field")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_FIELD_NUMBER: _ClassVar[int]
    query: str
    default_field: str
    def __init__(self, query: _Optional[str] = ..., default_field: _Optional[str] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("term_filter", "not_filter", "and_filter", "or_filter")
    TERM_FILTER_FIELD_NUMBER: _ClassVar[int]
    NOT_FILTER_FIELD_NUMBER: _ClassVar[int]
    AND_FILTER_FIELD_NUMBER: _ClassVar[int]
    OR_FILTER_FIELD_NUMBER: _ClassVar[int]
    term_filter: _containers.RepeatedCompositeFieldContainer[StringStringMapEntry]
    not_filter: Filter
    and_filter: _containers.RepeatedCompositeFieldContainer[Filter]
    or_filter: _containers.RepeatedCompositeFieldContainer[Filter]
    def __init__(self, term_filter: _Optional[_Iterable[_Union[StringStringMapEntry, _Mapping]]] = ..., not_filter: _Optional[_Union[Filter, _Mapping]] = ..., and_filter: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ..., or_filter: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ...) -> None: ...
