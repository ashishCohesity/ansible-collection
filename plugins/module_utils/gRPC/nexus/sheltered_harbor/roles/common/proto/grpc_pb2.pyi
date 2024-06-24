from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[OperationState]
    WAITING: _ClassVar[OperationState]
    IN_PROGRESS: _ClassVar[OperationState]
    COMPELETED: _ClassVar[OperationState]
    FAILED: _ClassVar[OperationState]
NONE: OperationState
WAITING: OperationState
IN_PROGRESS: OperationState
COMPELETED: OperationState
FAILED: OperationState

class CommonError(_message.Message):
    __slots__ = ("timestamp", "code", "summary", "details")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    code: int
    summary: str
    details: str
    def __init__(self, timestamp: _Optional[int] = ..., code: _Optional[int] = ..., summary: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...

class ListParameters(_message.Message):
    __slots__ = ("offset", "limit")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class TLSBootstrapReq(_message.Message):
    __slots__ = ("join_token", "cluster_id", "cluster_name", "trust_bundle")
    JOIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TRUST_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    join_token: str
    cluster_id: str
    cluster_name: str
    trust_bundle: str
    def __init__(self, join_token: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., trust_bundle: _Optional[str] = ...) -> None: ...

class TLSBootstrapReply(_message.Message):
    __slots__ = ("error", "cluster_id", "cluster_name", "cluster_type", "trust_bundle")
    class ClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIMARY: _ClassVar[TLSBootstrapReply.ClusterType]
        RECOVERY: _ClassVar[TLSBootstrapReply.ClusterType]
    PRIMARY: TLSBootstrapReply.ClusterType
    RECOVERY: TLSBootstrapReply.ClusterType
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRUST_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    error: CommonError
    cluster_id: str
    cluster_name: str
    cluster_type: TLSBootstrapReply.ClusterType
    trust_bundle: str
    def __init__(self, error: _Optional[_Union[CommonError, _Mapping]] = ..., cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster_type: _Optional[_Union[TLSBootstrapReply.ClusterType, str]] = ..., trust_bundle: _Optional[str] = ...) -> None: ...
