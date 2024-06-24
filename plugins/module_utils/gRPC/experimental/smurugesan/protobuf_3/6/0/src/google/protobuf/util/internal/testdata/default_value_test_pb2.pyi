from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultValueTest(_message.Message):
    __slots__ = ("double_value", "repeated_double", "float_value", "int64_value", "uint64_value", "int32_value", "uint32_value", "bool_value", "string_value", "bytes_value", "enum_value")
    class EnumDefault(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_FIRST: _ClassVar[DefaultValueTest.EnumDefault]
        ENUM_SECOND: _ClassVar[DefaultValueTest.EnumDefault]
        ENUM_THIRD: _ClassVar[DefaultValueTest.EnumDefault]
    ENUM_FIRST: DefaultValueTest.EnumDefault
    ENUM_SECOND: DefaultValueTest.EnumDefault
    ENUM_THIRD: DefaultValueTest.EnumDefault
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    double_value: float
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    float_value: float
    int64_value: int
    uint64_value: int
    int32_value: int
    uint32_value: int
    bool_value: bool
    string_value: str
    bytes_value: bytes
    enum_value: DefaultValueTest.EnumDefault
    def __init__(self, double_value: _Optional[float] = ..., repeated_double: _Optional[_Iterable[float]] = ..., float_value: _Optional[float] = ..., int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., int32_value: _Optional[int] = ..., uint32_value: _Optional[int] = ..., bool_value: bool = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ..., enum_value: _Optional[_Union[DefaultValueTest.EnumDefault, str]] = ...) -> None: ...
