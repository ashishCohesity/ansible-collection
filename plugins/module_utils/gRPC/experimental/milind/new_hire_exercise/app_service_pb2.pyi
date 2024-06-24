from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequestArg(_message.Message):
    __slots__ = ("say_hello",)
    SAY_HELLO_FIELD_NUMBER: _ClassVar[int]
    say_hello: bool
    def __init__(self, say_hello: bool = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("hello",)
    HELLO_FIELD_NUMBER: _ClassVar[int]
    hello: bool
    def __init__(self, hello: bool = ...) -> None: ...
