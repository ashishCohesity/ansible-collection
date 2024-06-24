from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestNamespace(_message.Message):
    __slots__ = ("a", "nested_message", "nested_enum", "reserved_name")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestNamespace.NestedEnum]
    ZERO: TestNamespace.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    class Empty(_message.Message):
        __slots__ = ("nested_message", "nested_enum")
        class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ZERO: _ClassVar[TestNamespace.Empty.NestedEnum]
        ZERO: TestNamespace.Empty.NestedEnum
        class NestedMessage(_message.Message):
            __slots__ = ("a",)
            A_FIELD_NUMBER: _ClassVar[int]
            a: int
            def __init__(self, a: _Optional[int] = ...) -> None: ...
        NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
        nested_message: TestNamespace.Empty.NestedMessage
        nested_enum: TestNamespace.Empty.NestedEnum
        def __init__(self, nested_message: _Optional[_Union[TestNamespace.Empty.NestedMessage, _Mapping]] = ..., nested_enum: _Optional[_Union[TestNamespace.Empty.NestedEnum, str]] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    RESERVED_NAME_FIELD_NUMBER: _ClassVar[int]
    a: int
    nested_message: TestNamespace.NestedMessage
    nested_enum: TestNamespace.NestedEnum
    reserved_name: TestNamespace.Empty
    def __init__(self, a: _Optional[int] = ..., nested_message: _Optional[_Union[TestNamespace.NestedMessage, _Mapping]] = ..., nested_enum: _Optional[_Union[TestNamespace.NestedEnum, str]] = ..., reserved_name: _Optional[_Union[TestNamespace.Empty, _Mapping]] = ...) -> None: ...
