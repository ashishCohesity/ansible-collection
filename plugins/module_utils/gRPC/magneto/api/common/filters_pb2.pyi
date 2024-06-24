from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SourceFilters(_message.Message):
    __slots__ = ("exclude_source_filter_vec",)
    class SourceFilter(_message.Message):
        __slots__ = ("source_filter", "is_regex", "case_sensitive")
        SOURCE_FILTER_FIELD_NUMBER: _ClassVar[int]
        IS_REGEX_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        source_filter: str
        is_regex: bool
        case_sensitive: bool
        def __init__(self, source_filter: _Optional[str] = ..., is_regex: bool = ..., case_sensitive: bool = ...) -> None: ...
    EXCLUDE_SOURCE_FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
    exclude_source_filter_vec: _containers.RepeatedCompositeFieldContainer[SourceFilters.SourceFilter]
    def __init__(self, exclude_source_filter_vec: _Optional[_Iterable[_Union[SourceFilters.SourceFilter, _Mapping]]] = ...) -> None: ...

class FilteringPolicyProto(_message.Message):
    __slots__ = ("allow_filters", "deny_filters")
    ALLOW_FILTERS_FIELD_NUMBER: _ClassVar[int]
    DENY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    allow_filters: _containers.RepeatedScalarFieldContainer[str]
    deny_filters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow_filters: _Optional[_Iterable[str]] = ..., deny_filters: _Optional[_Iterable[str]] = ...) -> None: ...
