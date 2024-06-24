from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LazyMessageLite(_message.Message):
    __slots__ = ("num", "num_with_default", "inner", "repeated_inner", "oneof_num", "oneof_inner")
    NUM_FIELD_NUMBER: _ClassVar[int]
    NUM_WITH_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    INNER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INNER_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INNER_FIELD_NUMBER: _ClassVar[int]
    num: int
    num_with_default: int
    inner: LazyInnerMessageLite
    repeated_inner: _containers.RepeatedCompositeFieldContainer[LazyInnerMessageLite]
    oneof_num: int
    oneof_inner: LazyInnerMessageLite
    def __init__(self, num: _Optional[int] = ..., num_with_default: _Optional[int] = ..., inner: _Optional[_Union[LazyInnerMessageLite, _Mapping]] = ..., repeated_inner: _Optional[_Iterable[_Union[LazyInnerMessageLite, _Mapping]]] = ..., oneof_num: _Optional[int] = ..., oneof_inner: _Optional[_Union[LazyInnerMessageLite, _Mapping]] = ...) -> None: ...

class LazyInnerMessageLite(_message.Message):
    __slots__ = ("num", "num_with_default", "nested")
    Extensions: _python_message._ExtensionDict
    NUM_FIELD_NUMBER: _ClassVar[int]
    NUM_WITH_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    num: int
    num_with_default: int
    nested: LazyNestedInnerMessageLite
    def __init__(self, num: _Optional[int] = ..., num_with_default: _Optional[int] = ..., nested: _Optional[_Union[LazyNestedInnerMessageLite, _Mapping]] = ...) -> None: ...

class LazyExtension(_message.Message):
    __slots__ = ("name",)
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: _descriptor.FieldDescriptor
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LazyNestedInnerMessageLite(_message.Message):
    __slots__ = ("num", "num_with_default")
    NUM_FIELD_NUMBER: _ClassVar[int]
    NUM_WITH_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    num: int
    num_with_default: int
    def __init__(self, num: _Optional[int] = ..., num_with_default: _Optional[int] = ...) -> None: ...
