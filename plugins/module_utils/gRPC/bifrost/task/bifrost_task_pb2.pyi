from bifrost.base import error_pb2 as _error_pb2
from bifrost.stub import bridge_auth_params_pb2 as _bridge_auth_params_pb2
from bifrost.stub import magneto_connector_params_pb2 as _magneto_connector_params_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostScheduleTaskArg(_message.Message):
    __slots__ = ("source_type", "source_constituent_id", "task_id")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMagneto: _ClassVar[BifrostScheduleTaskArg.SourceType]
        kBridge: _ClassVar[BifrostScheduleTaskArg.SourceType]
    kMagneto: BifrostScheduleTaskArg.SourceType
    kBridge: BifrostScheduleTaskArg.SourceType
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    source_type: BifrostScheduleTaskArg.SourceType
    source_constituent_id: int
    task_id: int
    def __init__(self, source_type: _Optional[_Union[BifrostScheduleTaskArg.SourceType, str]] = ..., source_constituent_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class BifrostScheduleTaskResult(_message.Message):
    __slots__ = ("bifrost_task_id",)
    BIFROST_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    bifrost_task_id: int
    def __init__(self, bifrost_task_id: _Optional[int] = ...) -> None: ...

class UpdateBifrostTaskArg(_message.Message):
    __slots__ = ("api_version", "tenant_id", "bifrost_constituent_id", "bifrost_session_id", "task_id", "magneto_connector_result", "bridge_auth_result")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CONNECTOR_RESULT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_AUTH_RESULT_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    tenant_id: str
    bifrost_constituent_id: int
    bifrost_session_id: int
    task_id: int
    magneto_connector_result: _magneto_connector_params_pb2.MagnetoConnectorResult
    bridge_auth_result: _bridge_auth_params_pb2.BridgeAuthResult
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., tenant_id: _Optional[str] = ..., bifrost_constituent_id: _Optional[int] = ..., bifrost_session_id: _Optional[int] = ..., task_id: _Optional[int] = ..., magneto_connector_result: _Optional[_Union[_magneto_connector_params_pb2.MagnetoConnectorResult, _Mapping]] = ..., bridge_auth_result: _Optional[_Union[_bridge_auth_params_pb2.BridgeAuthResult, _Mapping]] = ...) -> None: ...

class UpdateBifrostTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
