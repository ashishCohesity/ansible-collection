from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessageSet(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestMessageSetContainer(_message.Message):
    __slots__ = ("message_set",)
    MESSAGE_SET_FIELD_NUMBER: _ClassVar[int]
    message_set: TestMessageSet
    def __init__(self, message_set: _Optional[_Union[TestMessageSet, _Mapping]] = ...) -> None: ...

class TestMessageSetExtension1(_message.Message):
    __slots__ = ("i",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    i: int
    def __init__(self, i: _Optional[int] = ...) -> None: ...

class TestMessageSetExtension2(_message.Message):
    __slots__ = ("str",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    STR_FIELD_NUMBER: _ClassVar[int]
    str: str
    def __init__(self, str: _Optional[str] = ...) -> None: ...

class RawMessageSet(_message.Message):
    __slots__ = ("item",)
    class Item(_message.Message):
        __slots__ = ("type_id", "message")
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        type_id: int
        message: bytes
        def __init__(self, type_id: _Optional[int] = ..., message: _Optional[bytes] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[RawMessageSet.Item]
    def __init__(self, item: _Optional[_Iterable[_Union[RawMessageSet.Item, _Mapping]]] = ...) -> None: ...
