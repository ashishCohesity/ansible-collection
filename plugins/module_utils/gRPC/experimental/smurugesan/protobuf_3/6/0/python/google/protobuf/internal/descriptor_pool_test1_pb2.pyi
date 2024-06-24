from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescriptorPoolTest1(_message.Message):
    __slots__ = ("nested_enum", "nested_message")
    Extensions: _python_message._ExtensionDict
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALPHA: _ClassVar[DescriptorPoolTest1.NestedEnum]
        BETA: _ClassVar[DescriptorPoolTest1.NestedEnum]
    ALPHA: DescriptorPoolTest1.NestedEnum
    BETA: DescriptorPoolTest1.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("nested_enum", "nested_field", "deep_nested_message")
        class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EPSILON: _ClassVar[DescriptorPoolTest1.NestedMessage.NestedEnum]
            ZETA: _ClassVar[DescriptorPoolTest1.NestedMessage.NestedEnum]
        EPSILON: DescriptorPoolTest1.NestedMessage.NestedEnum
        ZETA: DescriptorPoolTest1.NestedMessage.NestedEnum
        class DeepNestedMessage(_message.Message):
            __slots__ = ("nested_enum", "nested_field")
            class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ETA: _ClassVar[DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum]
                THETA: _ClassVar[DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum]
            ETA: DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum
            THETA: DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum
            NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
            NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
            nested_enum: DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum
            nested_field: str
            def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest1.NestedMessage.DeepNestedMessage.NestedEnum, str]] = ..., nested_field: _Optional[str] = ...) -> None: ...
        NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
        NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
        DEEP_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        nested_enum: DescriptorPoolTest1.NestedMessage.NestedEnum
        nested_field: str
        deep_nested_message: DescriptorPoolTest1.NestedMessage.DeepNestedMessage
        def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest1.NestedMessage.NestedEnum, str]] = ..., nested_field: _Optional[str] = ..., deep_nested_message: _Optional[_Union[DescriptorPoolTest1.NestedMessage.DeepNestedMessage, _Mapping]] = ...) -> None: ...
    NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    nested_enum: DescriptorPoolTest1.NestedEnum
    nested_message: DescriptorPoolTest1.NestedMessage
    def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest1.NestedEnum, str]] = ..., nested_message: _Optional[_Union[DescriptorPoolTest1.NestedMessage, _Mapping]] = ...) -> None: ...

class DescriptorPoolTest2(_message.Message):
    __slots__ = ("nested_enum", "nested_message")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GAMMA: _ClassVar[DescriptorPoolTest2.NestedEnum]
        DELTA: _ClassVar[DescriptorPoolTest2.NestedEnum]
    GAMMA: DescriptorPoolTest2.NestedEnum
    DELTA: DescriptorPoolTest2.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("nested_enum", "nested_field", "deep_nested_message")
        class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IOTA: _ClassVar[DescriptorPoolTest2.NestedMessage.NestedEnum]
            KAPPA: _ClassVar[DescriptorPoolTest2.NestedMessage.NestedEnum]
        IOTA: DescriptorPoolTest2.NestedMessage.NestedEnum
        KAPPA: DescriptorPoolTest2.NestedMessage.NestedEnum
        class DeepNestedMessage(_message.Message):
            __slots__ = ("nested_enum", "nested_field")
            class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LAMBDA: _ClassVar[DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum]
                MU: _ClassVar[DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum]
            LAMBDA: DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum
            MU: DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum
            NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
            NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
            nested_enum: DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum
            nested_field: str
            def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest2.NestedMessage.DeepNestedMessage.NestedEnum, str]] = ..., nested_field: _Optional[str] = ...) -> None: ...
        NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
        NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
        DEEP_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        nested_enum: DescriptorPoolTest2.NestedMessage.NestedEnum
        nested_field: str
        deep_nested_message: DescriptorPoolTest2.NestedMessage.DeepNestedMessage
        def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest2.NestedMessage.NestedEnum, str]] = ..., nested_field: _Optional[str] = ..., deep_nested_message: _Optional[_Union[DescriptorPoolTest2.NestedMessage.DeepNestedMessage, _Mapping]] = ...) -> None: ...
    NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    nested_enum: DescriptorPoolTest2.NestedEnum
    nested_message: DescriptorPoolTest2.NestedMessage
    def __init__(self, nested_enum: _Optional[_Union[DescriptorPoolTest2.NestedEnum, str]] = ..., nested_message: _Optional[_Union[DescriptorPoolTest2.NestedMessage, _Mapping]] = ...) -> None: ...
