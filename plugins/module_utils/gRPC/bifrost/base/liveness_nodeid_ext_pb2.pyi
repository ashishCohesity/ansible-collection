from bifrost.base import bifrost_base_pb2 as _bifrost_base_pb2
from gandalf.util import liveness_pb2 as _liveness_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessNodeIdExtension(_message.Message):
    __slots__ = ("node_id", "broker_constituent_id", "broker_session_id", "server_liveness_vec", "version_id", "liveness_namespace")
    class BifrostServerLiveness(_message.Message):
        __slots__ = ("tenant_id", "network_realm_id", "constituent_id", "session_id", "ip_addr", "version", "cohesity_side_ip", "tenant_source_side_ip", "connection_timestamp_usecs", "hyx_connector_id", "connector_group_id", "is_rigel_mode", "resource_capacity", "cloud_metadata", "initiator_type")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDR_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        COHESITY_SIDE_IP_FIELD_NUMBER: _ClassVar[int]
        TENANT_SOURCE_SIDE_IP_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        HYX_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        IS_RIGEL_MODE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        CLOUD_METADATA_FIELD_NUMBER: _ClassVar[int]
        INITIATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        network_realm_id: int
        constituent_id: int
        session_id: int
        ip_addr: str
        version: str
        cohesity_side_ip: str
        tenant_source_side_ip: str
        connection_timestamp_usecs: int
        hyx_connector_id: int
        connector_group_id: int
        is_rigel_mode: bool
        resource_capacity: _bifrost_base_pb2.BifrostResourceCapacityProto
        cloud_metadata: _bifrost_base_pb2.BifrostCloudMetadataProto
        initiator_type: _bifrost_base_pb2.NetworkRealm.Type
        def __init__(self, tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., ip_addr: _Optional[str] = ..., version: _Optional[str] = ..., cohesity_side_ip: _Optional[str] = ..., tenant_source_side_ip: _Optional[str] = ..., connection_timestamp_usecs: _Optional[int] = ..., hyx_connector_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., is_rigel_mode: bool = ..., resource_capacity: _Optional[_Union[_bifrost_base_pb2.BifrostResourceCapacityProto, _Mapping]] = ..., cloud_metadata: _Optional[_Union[_bifrost_base_pb2.BifrostCloudMetadataProto, _Mapping]] = ..., initiator_type: _Optional[_Union[_bifrost_base_pb2.NetworkRealm.Type, str]] = ...) -> None: ...
    LIVENESS_EXT_FIELD_NUMBER: _ClassVar[int]
    liveness_ext: _descriptor.FieldDescriptor
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BROKER_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BROKER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_LIVENESS_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    broker_constituent_id: int
    broker_session_id: int
    server_liveness_vec: _containers.RepeatedCompositeFieldContainer[LivenessNodeIdExtension.BifrostServerLiveness]
    version_id: int
    liveness_namespace: str
    def __init__(self, node_id: _Optional[int] = ..., broker_constituent_id: _Optional[int] = ..., broker_session_id: _Optional[int] = ..., server_liveness_vec: _Optional[_Iterable[_Union[LivenessNodeIdExtension.BifrostServerLiveness, _Mapping]]] = ..., version_id: _Optional[int] = ..., liveness_namespace: _Optional[str] = ...) -> None: ...
