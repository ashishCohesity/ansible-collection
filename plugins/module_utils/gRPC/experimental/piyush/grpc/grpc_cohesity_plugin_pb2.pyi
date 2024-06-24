from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MessageBase(_message.Message):
    __slots__ = ("req_id",)
    REQ_ID_FIELD_NUMBER: _ClassVar[int]
    req_id: RequestId
    def __init__(self, req_id: _Optional[_Union[RequestId, _Mapping]] = ...) -> None: ...

class TestRequest(_message.Message):
    __slots__ = ("base_message",)
    BASE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    base_message: MessageBase
    def __init__(self, base_message: _Optional[_Union[MessageBase, _Mapping]] = ...) -> None: ...

class TestResponse(_message.Message):
    __slots__ = ("base_message",)
    BASE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    base_message: MessageBase
    def __init__(self, base_message: _Optional[_Union[MessageBase, _Mapping]] = ...) -> None: ...
