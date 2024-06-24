from google.protobuf import wrappers_pb2 as _wrappers_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EchoMessageArg(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _wrappers_pb2.BytesValue
    def __init__(self, data: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class EchoMessageResult(_message.Message):
    __slots__ = ("data", "server_proc_recv_usecs")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_PROC_RECV_USECS_FIELD_NUMBER: _ClassVar[int]
    data: _wrappers_pb2.BytesValue
    server_proc_recv_usecs: int
    def __init__(self, data: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., server_proc_recv_usecs: _Optional[int] = ...) -> None: ...
