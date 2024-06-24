from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndexSchema(_message.Message):
    __slots__ = ("name", "num_replicas", "default_text_indexing", "field_properties", "sharding_function", "merge_function", "deletion_function", "comparator_function", "fields_extractor_function")
    class FieldMapping(_message.Message):
        __slots__ = ("index", "tokenize", "index_with_field_name", "type", "force_index")
        class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kString: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kInt64: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kUInt64: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kBool: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kMultiValuedString: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kMultiValuedInt64: _ClassVar[IndexSchema.FieldMapping.FieldType]
            kMultiValuedUInt64: _ClassVar[IndexSchema.FieldMapping.FieldType]
        kString: IndexSchema.FieldMapping.FieldType
        kInt64: IndexSchema.FieldMapping.FieldType
        kUInt64: IndexSchema.FieldMapping.FieldType
        kBool: IndexSchema.FieldMapping.FieldType
        kMultiValuedString: IndexSchema.FieldMapping.FieldType
        kMultiValuedInt64: IndexSchema.FieldMapping.FieldType
        kMultiValuedUInt64: IndexSchema.FieldMapping.FieldType
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TOKENIZE_FIELD_NUMBER: _ClassVar[int]
        INDEX_WITH_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        FORCE_INDEX_FIELD_NUMBER: _ClassVar[int]
        index: bool
        tokenize: bool
        index_with_field_name: bool
        type: IndexSchema.FieldMapping.FieldType
        force_index: bool
        def __init__(self, index: bool = ..., tokenize: bool = ..., index_with_field_name: bool = ..., type: _Optional[_Union[IndexSchema.FieldMapping.FieldType, str]] = ..., force_index: bool = ...) -> None: ...
    class FieldPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IndexSchema.FieldMapping
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IndexSchema.FieldMapping, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TEXT_INDEXING_FIELD_NUMBER: _ClassVar[int]
    FIELD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SHARDING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    MERGE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    DELETION_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    COMPARATOR_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_EXTRACTOR_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_replicas: int
    default_text_indexing: bool
    field_properties: _containers.MessageMap[str, IndexSchema.FieldMapping]
    sharding_function: str
    merge_function: str
    deletion_function: str
    comparator_function: str
    fields_extractor_function: str
    def __init__(self, name: _Optional[str] = ..., num_replicas: _Optional[int] = ..., default_text_indexing: bool = ..., field_properties: _Optional[_Mapping[str, IndexSchema.FieldMapping]] = ..., sharding_function: _Optional[str] = ..., merge_function: _Optional[str] = ..., deletion_function: _Optional[str] = ..., comparator_function: _Optional[str] = ..., fields_extractor_function: _Optional[str] = ...) -> None: ...

class AllIndexSchema(_message.Message):
    __slots__ = ("indices",)
    INDICES_FIELD_NUMBER: _ClassVar[int]
    indices: _containers.RepeatedCompositeFieldContainer[IndexSchema]
    def __init__(self, indices: _Optional[_Iterable[_Union[IndexSchema, _Mapping]]] = ...) -> None: ...

class SearchClause(_message.Message):
    __slots__ = ("term_query", "range_query", "boolean_query")
    class TermQuery(_message.Message):
        __slots__ = ("field_name", "query")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        query: str
        def __init__(self, field_name: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...
    class RangeQuery(_message.Message):
        __slots__ = ("field_name", "lower_bound", "lower_bound_comparison_type", "upper_bound", "upper_bound_comparison_type")
        class ComparisonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LT: _ClassVar[SearchClause.RangeQuery.ComparisonType]
            LE: _ClassVar[SearchClause.RangeQuery.ComparisonType]
            EQ: _ClassVar[SearchClause.RangeQuery.ComparisonType]
            GT: _ClassVar[SearchClause.RangeQuery.ComparisonType]
            GE: _ClassVar[SearchClause.RangeQuery.ComparisonType]
        LT: SearchClause.RangeQuery.ComparisonType
        LE: SearchClause.RangeQuery.ComparisonType
        EQ: SearchClause.RangeQuery.ComparisonType
        GT: SearchClause.RangeQuery.ComparisonType
        GE: SearchClause.RangeQuery.ComparisonType
        class RangeValue(_message.Message):
            __slots__ = ("int64_value", "uint64_value", "string_value")
            INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
            UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
            STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
            int64_value: int
            uint64_value: int
            string_value: str
            def __init__(self, int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., string_value: _Optional[str] = ...) -> None: ...
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
        LOWER_BOUND_COMPARISON_TYPE_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_COMPARISON_TYPE_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        lower_bound: SearchClause.RangeQuery.RangeValue
        lower_bound_comparison_type: SearchClause.RangeQuery.ComparisonType
        upper_bound: SearchClause.RangeQuery.RangeValue
        upper_bound_comparison_type: SearchClause.RangeQuery.ComparisonType
        def __init__(self, field_name: _Optional[str] = ..., lower_bound: _Optional[_Union[SearchClause.RangeQuery.RangeValue, _Mapping]] = ..., lower_bound_comparison_type: _Optional[_Union[SearchClause.RangeQuery.ComparisonType, str]] = ..., upper_bound: _Optional[_Union[SearchClause.RangeQuery.RangeValue, _Mapping]] = ..., upper_bound_comparison_type: _Optional[_Union[SearchClause.RangeQuery.ComparisonType, str]] = ...) -> None: ...
    class BooleanQuery(_message.Message):
        __slots__ = ("type", "clauses_vec")
        class QueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNegation: _ClassVar[SearchClause.BooleanQuery.QueryType]
            kDisjunction: _ClassVar[SearchClause.BooleanQuery.QueryType]
            kConjunction: _ClassVar[SearchClause.BooleanQuery.QueryType]
        kNegation: SearchClause.BooleanQuery.QueryType
        kDisjunction: SearchClause.BooleanQuery.QueryType
        kConjunction: SearchClause.BooleanQuery.QueryType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CLAUSES_VEC_FIELD_NUMBER: _ClassVar[int]
        type: SearchClause.BooleanQuery.QueryType
        clauses_vec: _containers.RepeatedCompositeFieldContainer[SearchClause]
        def __init__(self, type: _Optional[_Union[SearchClause.BooleanQuery.QueryType, str]] = ..., clauses_vec: _Optional[_Iterable[_Union[SearchClause, _Mapping]]] = ...) -> None: ...
    TERM_QUERY_FIELD_NUMBER: _ClassVar[int]
    RANGE_QUERY_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_QUERY_FIELD_NUMBER: _ClassVar[int]
    term_query: SearchClause.TermQuery
    range_query: SearchClause.RangeQuery
    boolean_query: SearchClause.BooleanQuery
    def __init__(self, term_query: _Optional[_Union[SearchClause.TermQuery, _Mapping]] = ..., range_query: _Optional[_Union[SearchClause.RangeQuery, _Mapping]] = ..., boolean_query: _Optional[_Union[SearchClause.BooleanQuery, _Mapping]] = ...) -> None: ...
