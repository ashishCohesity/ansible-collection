from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessage2(_message.Message):
    __slots__ = ()
    class NestedMessage(_message.Message):
        __slots__ = ()
        class OuterClassNameTest2(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
