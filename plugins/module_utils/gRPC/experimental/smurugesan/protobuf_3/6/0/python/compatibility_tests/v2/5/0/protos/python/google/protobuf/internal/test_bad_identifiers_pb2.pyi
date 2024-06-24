from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
MESSAGE_FIELD_NUMBER: _ClassVar[int]
message: _descriptor.FieldDescriptor
DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
descriptor: _descriptor.FieldDescriptor
REFLECTION_FIELD_NUMBER: _ClassVar[int]
reflection: _descriptor.FieldDescriptor
SERVICE_FIELD_NUMBER: _ClassVar[int]
service: _descriptor.FieldDescriptor

class TestBadIdentifiers(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class AnotherMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AnotherService(_service.service): ...

class AnotherService_Stub(AnotherService): ...
