from cohesion.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateApplianceArg(_message.Message):
    __slots__ = ("activation_string",)
    ACTIVATION_STRING_FIELD_NUMBER: _ClassVar[int]
    activation_string: str
    def __init__(self, activation_string: _Optional[str] = ...) -> None: ...

class ActivateApplianceResult(_message.Message):
    __slots__ = ("activation_status", "error")
    ACTIVATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    activation_status: bool
    error: _error_pb2.ErrorProto
    def __init__(self, activation_status: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CheckActivationArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckActivationResult(_message.Message):
    __slots__ = ("activation_status", "error")
    ACTIVATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    activation_status: bool
    error: _error_pb2.ErrorProto
    def __init__(self, activation_status: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetLocalArnFromCloudArnArg(_message.Message):
    __slots__ = ("cloud_arn",)
    CLOUD_ARN_FIELD_NUMBER: _ClassVar[int]
    cloud_arn: str
    def __init__(self, cloud_arn: _Optional[str] = ...) -> None: ...

class GetLocalArnFromCloudArnResult(_message.Message):
    __slots__ = ("local_snapshot_arn", "error")
    LOCAL_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    local_snapshot_arn: str
    error: _error_pb2.ErrorProto
    def __init__(self, local_snapshot_arn: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
