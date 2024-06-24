from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestProto(_message.Message):
    __slots__ = ("test_field",)
    TEST_FIELD_FIELD_NUMBER: _ClassVar[int]
    test_field: str
    def __init__(self, test_field: _Optional[str] = ...) -> None: ...

class EmptyProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
