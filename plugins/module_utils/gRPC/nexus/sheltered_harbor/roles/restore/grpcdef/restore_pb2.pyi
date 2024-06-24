from nexus.sheltered_harbor.roles.common.proto import grpc_pb2 as _grpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArchiveTranferStatusReq(_message.Message):
    __slots__ = ("archive_id",)
    ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    archive_id: str
    def __init__(self, archive_id: _Optional[str] = ...) -> None: ...

class ArchiveTranferStatusReply(_message.Message):
    __slots__ = ("error", "state", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _grpc_pb2.CommonError
    state: _grpc_pb2.OperationState
    status: str
    def __init__(self, error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ..., state: _Optional[_Union[_grpc_pb2.OperationState, str]] = ..., status: _Optional[str] = ...) -> None: ...
