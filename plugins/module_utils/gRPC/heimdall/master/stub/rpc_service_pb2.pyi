from heimdall.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Environment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAWS: _ClassVar[Environment]
    kAzure: _ClassVar[Environment]

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kFleet: _ClassVar[ResourceType]
    kDiskAccess: _ClassVar[ResourceType]
    kDisks: _ClassVar[ResourceType]

class WorkflowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kYodaBrowsing: _ClassVar[WorkflowType]
    kYodaIndexing: _ClassVar[WorkflowType]
    kMagnetoBackup: _ClassVar[WorkflowType]
    kMagnetoFileRestore: _ClassVar[WorkflowType]
    kMagnetoRestore: _ClassVar[WorkflowType]
    kMagnetoO365PSTRestore: _ClassVar[WorkflowType]
    kMagnetoDBBackupRestore: _ClassVar[WorkflowType]

class FleetOSType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLinux: _ClassVar[FleetOSType]
    kWindows: _ClassVar[FleetOSType]

class RequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kErrorinpassing: _ClassVar[RequestStatus]
    kAcquireInProgress: _ClassVar[RequestStatus]
    kAcquired: _ClassVar[RequestStatus]
    kReleaseInProgress: _ClassVar[RequestStatus]
    kReleased: _ClassVar[RequestStatus]
kAWS: Environment
kAzure: Environment
kFleet: ResourceType
kDiskAccess: ResourceType
kDisks: ResourceType
kYodaBrowsing: WorkflowType
kYodaIndexing: WorkflowType
kMagnetoBackup: WorkflowType
kMagnetoFileRestore: WorkflowType
kMagnetoRestore: WorkflowType
kMagnetoO365PSTRestore: WorkflowType
kMagnetoDBBackupRestore: WorkflowType
kLinux: FleetOSType
kWindows: FleetOSType
kErrorinpassing: RequestStatus
kAcquireInProgress: RequestStatus
kAcquired: RequestStatus
kReleaseInProgress: RequestStatus
kReleased: RequestStatus

class ResourceWeightMap(_message.Message):
    __slots__ = ("resource_weight_map",)
    class ResourceWeightMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    RESOURCE_WEIGHT_MAP_FIELD_NUMBER: _ClassVar[int]
    resource_weight_map: _containers.ScalarMap[str, int]
    def __init__(self, resource_weight_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class RigelInfo(_message.Message):
    __slots__ = ("tenant_id", "network_realm_id", "connector_group_id", "bifrost_constituent_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    network_realm_id: int
    connector_group_id: int
    bifrost_constituent_id: int
    def __init__(self, tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., bifrost_constituent_id: _Optional[int] = ...) -> None: ...

class AcquireFleetArg(_message.Message):
    __slots__ = ("api_version", "request_id", "environment", "workflow_type", "source_entity_id")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_id: str
    environment: Environment
    workflow_type: WorkflowType
    source_entity_id: int
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., environment: _Optional[_Union[Environment, str]] = ..., workflow_type: _Optional[_Union[WorkflowType, str]] = ..., source_entity_id: _Optional[int] = ...) -> None: ...

class AcquireFleetResult(_message.Message):
    __slots__ = ("api_version", "request_status", "error", "ip_address", "fleet_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FLEET_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_status: RequestStatus
    error: _error_pb2.ErrorProto
    ip_address: str
    fleet_id: str
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_status: _Optional[_Union[RequestStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ip_address: _Optional[str] = ..., fleet_id: _Optional[str] = ...) -> None: ...

class ReleaseFleetArg(_message.Message):
    __slots__ = ("api_version", "request_id", "workflow_type", "error")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_id: str
    workflow_type: WorkflowType
    error: _error_pb2.ErrorProto
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., workflow_type: _Optional[_Union[WorkflowType, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReleaseFleetResult(_message.Message):
    __slots__ = ("api_version", "request_status", "error")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_status: RequestStatus
    error: _error_pb2.ErrorProto
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_status: _Optional[_Union[RequestStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AcquireResourceArg(_message.Message):
    __slots__ = ("api_version", "request_id", "environment", "workflow_type", "source_entity_id", "requested_resource_type", "connector_params", "requested_resources_map", "rigel_info")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCES_MAP_FIELD_NUMBER: _ClassVar[int]
    RIGEL_INFO_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_id: str
    environment: Environment
    workflow_type: WorkflowType
    source_entity_id: int
    requested_resource_type: ResourceType
    connector_params: _magneto_pb2.ConnectorParams
    requested_resources_map: ResourceWeightMap
    rigel_info: RigelInfo
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., environment: _Optional[_Union[Environment, str]] = ..., workflow_type: _Optional[_Union[WorkflowType, str]] = ..., source_entity_id: _Optional[int] = ..., requested_resource_type: _Optional[_Union[ResourceType, str]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., requested_resources_map: _Optional[_Union[ResourceWeightMap, _Mapping]] = ..., rigel_info: _Optional[_Union[RigelInfo, _Mapping]] = ...) -> None: ...

class AcquireResourceResult(_message.Message):
    __slots__ = ("api_version", "request_status", "error")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_status: RequestStatus
    error: _error_pb2.ErrorProto
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_status: _Optional[_Union[RequestStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReleaseResourceArg(_message.Message):
    __slots__ = ("api_version", "request_id", "environment", "error", "workflow_type", "requested_resource_type", "connector_params")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_id: str
    environment: Environment
    error: _error_pb2.ErrorProto
    workflow_type: WorkflowType
    requested_resource_type: ResourceType
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_id: _Optional[str] = ..., environment: _Optional[_Union[Environment, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., workflow_type: _Optional[_Union[WorkflowType, str]] = ..., requested_resource_type: _Optional[_Union[ResourceType, str]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class ReleaseResourceResult(_message.Message):
    __slots__ = ("api_version", "request_status", "error")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    request_status: RequestStatus
    error: _error_pb2.ErrorProto
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., request_status: _Optional[_Union[RequestStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class APIVersion(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...
