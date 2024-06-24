from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SQLActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kExecuteSQLQuery: _ClassVar[SQLActionType]
kExecuteSQLQuery: SQLActionType

class SQLColumnAttributes(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[int] = ...) -> None: ...

class SQLCell(_message.Message):
    __slots__ = ("type", "is_null_valued", "string_value", "integer_value", "u16_string_value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kString: _ClassVar[SQLCell.Type]
        kInteger: _ClassVar[SQLCell.Type]
        kTimestamp: _ClassVar[SQLCell.Type]
    kString: SQLCell.Type
    kInteger: SQLCell.Type
    kTimestamp: SQLCell.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_NULL_VALUED_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    U16_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: SQLCell.Type
    is_null_valued: bool
    string_value: bytes
    integer_value: int
    u16_string_value: bytes
    def __init__(self, type: _Optional[_Union[SQLCell.Type, str]] = ..., is_null_valued: bool = ..., string_value: _Optional[bytes] = ..., integer_value: _Optional[int] = ..., u16_string_value: _Optional[bytes] = ...) -> None: ...

class SQLRow(_message.Message):
    __slots__ = ("cell_vec",)
    CELL_VEC_FIELD_NUMBER: _ClassVar[int]
    cell_vec: _containers.RepeatedCompositeFieldContainer[SQLCell]
    def __init__(self, cell_vec: _Optional[_Iterable[_Union[SQLCell, _Mapping]]] = ...) -> None: ...

class SQLResult(_message.Message):
    __slots__ = ("column_attributes_vec", "row_vec")
    COLUMN_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    column_attributes_vec: _containers.RepeatedCompositeFieldContainer[SQLColumnAttributes]
    row_vec: _containers.RepeatedCompositeFieldContainer[SQLRow]
    def __init__(self, column_attributes_vec: _Optional[_Iterable[_Union[SQLColumnAttributes, _Mapping]]] = ..., row_vec: _Optional[_Iterable[_Union[SQLRow, _Mapping]]] = ...) -> None: ...

class ExecuteSQLQueryArg(_message.Message):
    __slots__ = ("instance_name", "query")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    instance_name: bytes
    query: bytes
    def __init__(self, instance_name: _Optional[bytes] = ..., query: _Optional[bytes] = ...) -> None: ...

class ExecuteSQLActionArg(_message.Message):
    __slots__ = ("action_type", "execute_sql_query_arg")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_SQL_QUERY_ARG_FIELD_NUMBER: _ClassVar[int]
    action_type: SQLActionType
    execute_sql_query_arg: ExecuteSQLQueryArg
    def __init__(self, action_type: _Optional[_Union[SQLActionType, str]] = ..., execute_sql_query_arg: _Optional[_Union[ExecuteSQLQueryArg, _Mapping]] = ...) -> None: ...

class ExecuteSQLQueryResult(_message.Message):
    __slots__ = ("sql_result",)
    SQL_RESULT_FIELD_NUMBER: _ClassVar[int]
    sql_result: SQLResult
    def __init__(self, sql_result: _Optional[_Union[SQLResult, _Mapping]] = ...) -> None: ...

class ExecuteSQLActionResult(_message.Message):
    __slots__ = ("action_type", "execute_sql_query_result")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_SQL_QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_type: SQLActionType
    execute_sql_query_result: ExecuteSQLQueryResult
    def __init__(self, action_type: _Optional[_Union[SQLActionType, str]] = ..., execute_sql_query_result: _Optional[_Union[ExecuteSQLQueryResult, _Mapping]] = ...) -> None: ...
