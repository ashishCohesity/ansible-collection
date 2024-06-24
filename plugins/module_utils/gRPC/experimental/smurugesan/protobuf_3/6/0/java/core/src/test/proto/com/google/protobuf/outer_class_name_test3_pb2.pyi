from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessage3(_message.Message):
    __slots__ = ()
    class NestedMessage(_message.Message):
        __slots__ = ()
        class OuterClassNameTest3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DUMMY_VALUE: _ClassVar[TestMessage3.NestedMessage.OuterClassNameTest3]
        DUMMY_VALUE: TestMessage3.NestedMessage.OuterClassNameTest3
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
