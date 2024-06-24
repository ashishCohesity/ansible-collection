from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Descriptor(_message.Message):
    __slots__ = ("descriptor", "nested_descriptor")
    class NestedDescriptor(_message.Message):
        __slots__ = ("descriptor",)
        DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        descriptor: str
        def __init__(self, descriptor: _Optional[str] = ...) -> None: ...
    DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    NESTED_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    descriptor: str
    nested_descriptor: Descriptor.NestedDescriptor
    def __init__(self, descriptor: _Optional[str] = ..., nested_descriptor: _Optional[_Union[Descriptor.NestedDescriptor, _Mapping]] = ...) -> None: ...

class Parser(_message.Message):
    __slots__ = ("parser",)
    class ParserEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARSER: _ClassVar[Parser.ParserEnum]
    PARSER: Parser.ParserEnum
    PARSER_FIELD_NUMBER: _ClassVar[int]
    parser: Parser.ParserEnum
    def __init__(self, parser: _Optional[_Union[Parser.ParserEnum, str]] = ...) -> None: ...

class Deprecated(_message.Message):
    __slots__ = ("field1", "field2", "field3")
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[Deprecated.TestEnum]
    FOO: Deprecated.TestEnum
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    field1: int
    field2: Deprecated.TestEnum
    field3: TestMessage
    def __init__(self, field1: _Optional[int] = ..., field2: _Optional[_Union[Deprecated.TestEnum, str]] = ..., field3: _Optional[_Union[TestMessage, _Mapping]] = ...) -> None: ...

class Override(_message.Message):
    __slots__ = ("override",)
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    override: int
    def __init__(self, override: _Optional[int] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("object", "string_object")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    STRING_OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: int
    string_object: str
    def __init__(self, object: _Optional[int] = ..., string_object: _Optional[str] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...

class Integer(_message.Message):
    __slots__ = ("integer",)
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    integer: int
    def __init__(self, integer: _Optional[int] = ...) -> None: ...

class Long(_message.Message):
    __slots__ = ("long",)
    LONG_FIELD_NUMBER: _ClassVar[int]
    long: int
    def __init__(self, long: _Optional[int] = ...) -> None: ...

class Float(_message.Message):
    __slots__ = ("float",)
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    float: float
    def __init__(self, float: _Optional[float] = ...) -> None: ...

class Double(_message.Message):
    __slots__ = ("double",)
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    double: float
    def __init__(self, double: _Optional[float] = ...) -> None: ...
