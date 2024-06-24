from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMap(_message.Message):
    __slots__ = ("int32_to_int32_field", "int32_to_string_field", "int32_to_bytes_field", "int32_to_enum_field", "int32_to_message_field", "string_to_int32_field", "uint32_to_int32_field", "int64_to_int32_field")
    class EnumValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestMap.EnumValue]
        BAR: _ClassVar[TestMap.EnumValue]
        BAZ: _ClassVar[TestMap.EnumValue]
        QUX: _ClassVar[TestMap.EnumValue]
    FOO: TestMap.EnumValue
    BAR: TestMap.EnumValue
    BAZ: TestMap.EnumValue
    QUX: TestMap.EnumValue
    class MessageValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class Int32ToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToStringFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Int32ToBytesFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class Int32ToEnumFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestMap.EnumValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestMap.EnumValue, str]] = ...) -> None: ...
    class Int32ToMessageFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestMap.MessageValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestMap.MessageValue, _Mapping]] = ...) -> None: ...
    class StringToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint32ToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int64ToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    INT32_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    int32_to_int32_field: _containers.ScalarMap[int, int]
    int32_to_string_field: _containers.ScalarMap[int, str]
    int32_to_bytes_field: _containers.ScalarMap[int, bytes]
    int32_to_enum_field: _containers.ScalarMap[int, TestMap.EnumValue]
    int32_to_message_field: _containers.MessageMap[int, TestMap.MessageValue]
    string_to_int32_field: _containers.ScalarMap[str, int]
    uint32_to_int32_field: _containers.ScalarMap[int, int]
    int64_to_int32_field: _containers.ScalarMap[int, int]
    def __init__(self, int32_to_int32_field: _Optional[_Mapping[int, int]] = ..., int32_to_string_field: _Optional[_Mapping[int, str]] = ..., int32_to_bytes_field: _Optional[_Mapping[int, bytes]] = ..., int32_to_enum_field: _Optional[_Mapping[int, TestMap.EnumValue]] = ..., int32_to_message_field: _Optional[_Mapping[int, TestMap.MessageValue]] = ..., string_to_int32_field: _Optional[_Mapping[str, int]] = ..., uint32_to_int32_field: _Optional[_Mapping[int, int]] = ..., int64_to_int32_field: _Optional[_Mapping[int, int]] = ...) -> None: ...

class TestOnChangeEventPropagation(_message.Message):
    __slots__ = ("optional_message",)
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_message: TestMap
    def __init__(self, optional_message: _Optional[_Union[TestMap, _Mapping]] = ...) -> None: ...

class BizarroTestMap(_message.Message):
    __slots__ = ("int32_to_int32_field", "int32_to_string_field", "int32_to_bytes_field", "int32_to_enum_field", "int32_to_message_field", "string_to_int32_field")
    class Int32ToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class Int32ToStringFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToBytesFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToEnumFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class Int32ToMessageFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class StringToInt32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    INT32_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    int32_to_int32_field: _containers.ScalarMap[int, bytes]
    int32_to_string_field: _containers.ScalarMap[str, int]
    int32_to_bytes_field: _containers.ScalarMap[str, int]
    int32_to_enum_field: _containers.ScalarMap[str, bytes]
    int32_to_message_field: _containers.ScalarMap[str, bytes]
    string_to_int32_field: _containers.ScalarMap[str, bytes]
    def __init__(self, int32_to_int32_field: _Optional[_Mapping[int, bytes]] = ..., int32_to_string_field: _Optional[_Mapping[str, int]] = ..., int32_to_bytes_field: _Optional[_Mapping[str, int]] = ..., int32_to_enum_field: _Optional[_Mapping[str, bytes]] = ..., int32_to_message_field: _Optional[_Mapping[str, bytes]] = ..., string_to_int32_field: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class ReservedAsMapField(_message.Message):
    __slots__ = ("const", "private", "int", "void", "string", "package", "enum", "null")
    class IfEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ConstEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PrivateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ClassEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class IntEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class VoidEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class StringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PackageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class NullEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    IF_FIELD_NUMBER: _ClassVar[int]
    CONST_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    VOID_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    const: _containers.ScalarMap[str, int]
    private: _containers.ScalarMap[str, int]
    int: _containers.ScalarMap[str, int]
    void: _containers.ScalarMap[str, int]
    string: _containers.ScalarMap[str, int]
    package: _containers.ScalarMap[str, int]
    enum: _containers.ScalarMap[str, int]
    null: _containers.ScalarMap[str, int]
    def __init__(self, const: _Optional[_Mapping[str, int]] = ..., private: _Optional[_Mapping[str, int]] = ..., int: _Optional[_Mapping[str, int]] = ..., void: _Optional[_Mapping[str, int]] = ..., string: _Optional[_Mapping[str, int]] = ..., package: _Optional[_Mapping[str, int]] = ..., enum: _Optional[_Mapping[str, int]] = ..., null: _Optional[_Mapping[str, int]] = ..., **kwargs) -> None: ...

class ReservedAsMapFieldWithEnumValue(_message.Message):
    __slots__ = ("const", "private", "int", "void", "string", "package", "enum", "null")
    class SampleEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        A: _ClassVar[ReservedAsMapFieldWithEnumValue.SampleEnum]
        B: _ClassVar[ReservedAsMapFieldWithEnumValue.SampleEnum]
    A: ReservedAsMapFieldWithEnumValue.SampleEnum
    B: ReservedAsMapFieldWithEnumValue.SampleEnum
    class IfEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class ConstEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class PrivateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class ClassEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class IntEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class VoidEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class StringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class PackageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    class NullEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReservedAsMapFieldWithEnumValue.SampleEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReservedAsMapFieldWithEnumValue.SampleEnum, str]] = ...) -> None: ...
    IF_FIELD_NUMBER: _ClassVar[int]
    CONST_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    VOID_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    const: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    private: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    int: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    void: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    string: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    package: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    enum: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    null: _containers.ScalarMap[str, ReservedAsMapFieldWithEnumValue.SampleEnum]
    def __init__(self, const: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., private: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., int: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., void: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., string: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., package: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., enum: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., null: _Optional[_Mapping[str, ReservedAsMapFieldWithEnumValue.SampleEnum]] = ..., **kwargs) -> None: ...
