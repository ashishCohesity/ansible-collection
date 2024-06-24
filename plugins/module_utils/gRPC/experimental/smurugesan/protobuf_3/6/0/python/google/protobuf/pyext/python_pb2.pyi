from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_nested_message_extension: _descriptor.FieldDescriptor
REPEATED_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_nested_message_extension: _descriptor.FieldDescriptor

class TestAllTypes(_message.Message):
    __slots__ = ("repeated_nested_message", "optional_nested_message", "optional_int32")
    class NestedMessage(_message.Message):
        __slots__ = ("bb", "cc")
        BB_FIELD_NUMBER: _ClassVar[int]
        CC_FIELD_NUMBER: _ClassVar[int]
        bb: int
        cc: ForeignMessage
        def __init__(self, bb: _Optional[int] = ..., cc: _Optional[_Union[ForeignMessage, _Mapping]] = ...) -> None: ...
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    optional_nested_message: TestAllTypes.NestedMessage
    optional_int32: int
    def __init__(self, repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_int32: _Optional[int] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c", "d")
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    c: int
    d: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, c: _Optional[int] = ..., d: _Optional[_Iterable[int]] = ...) -> None: ...

class TestAllExtensions(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...
