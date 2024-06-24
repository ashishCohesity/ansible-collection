from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProtoRpcOverGrpcTransportArg(_message.Message):
    __slots__ = ("arg_str",)
    ARG_STR_FIELD_NUMBER: _ClassVar[int]
    arg_str: bytes
    def __init__(self, arg_str: _Optional[bytes] = ...) -> None: ...

class ProtoRpcOverGrpcTransportResult(_message.Message):
    __slots__ = ("result_str",)
    RESULT_STR_FIELD_NUMBER: _ClassVar[int]
    result_str: bytes
    def __init__(self, result_str: _Optional[bytes] = ...) -> None: ...
