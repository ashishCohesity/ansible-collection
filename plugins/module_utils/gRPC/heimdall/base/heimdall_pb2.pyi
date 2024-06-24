from heimdall.base import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupMasterResult(_message.Message):
    __slots__ = ("error", "ip", "port")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ip: str
    port: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
