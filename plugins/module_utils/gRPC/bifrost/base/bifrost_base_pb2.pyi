from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostRtServiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[BifrostRtServiceStatus]
    kHealthy: _ClassVar[BifrostRtServiceStatus]
    kUnhealthyOrStopped: _ClassVar[BifrostRtServiceStatus]
kUnknown: BifrostRtServiceStatus
kHealthy: BifrostRtServiceStatus
kUnhealthyOrStopped: BifrostRtServiceStatus

class BifrostServerIdProto(_message.Message):
    __slots__ = ("tenant_id", "constituent_id", "session_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    constituent_id: int
    session_id: int
    def __init__(self, tenant_id: _Optional[str] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ...) -> None: ...

class BifrostRtConfigProto(_message.Message):
    __slots__ = ("enable", "end_timestamp_msecs", "rt_remote_port", "rt_host_port", "ssh_port", "ssh_username", "ssh_key", "ssh_key_file_path", "proxy_server")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    RT_REMOTE_PORT_FIELD_NUMBER: _ClassVar[int]
    RT_HOST_PORT_FIELD_NUMBER: _ClassVar[int]
    SSH_PORT_FIELD_NUMBER: _ClassVar[int]
    SSH_USERNAME_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    end_timestamp_msecs: int
    rt_remote_port: int
    rt_host_port: int
    ssh_port: int
    ssh_username: str
    ssh_key: bytes
    ssh_key_file_path: str
    proxy_server: ProxyServerConfigProto
    def __init__(self, enable: bool = ..., end_timestamp_msecs: _Optional[int] = ..., rt_remote_port: _Optional[int] = ..., rt_host_port: _Optional[int] = ..., ssh_port: _Optional[int] = ..., ssh_username: _Optional[str] = ..., ssh_key: _Optional[bytes] = ..., ssh_key_file_path: _Optional[str] = ..., proxy_server: _Optional[_Union[ProxyServerConfigProto, _Mapping]] = ...) -> None: ...

class ProxyServerConfigProto(_message.Message):
    __slots__ = ("name", "ip", "port", "username", "encrypted_password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip: str
    port: int
    username: str
    encrypted_password: bytes
    def __init__(self, name: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("ip", "mask_bits")
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_BITS_FIELD_NUMBER: _ClassVar[int]
    ip: str
    mask_bits: int
    def __init__(self, ip: _Optional[str] = ..., mask_bits: _Optional[int] = ...) -> None: ...

class NetworkConnInfo(_message.Message):
    __slots__ = ("network_gateway", "dns", "ntp", "domain_name")
    NETWORK_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    NTP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    network_gateway: str
    dns: str
    ntp: str
    domain_name: str
    def __init__(self, network_gateway: _Optional[str] = ..., dns: _Optional[str] = ..., ntp: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...

class NetworkRealm(_message.Message):
    __slots__ = ("type", "deleted", "realm_id", "realm_name", "tenant_id", "realm_subnet", "external_bifrost_info", "update_intent", "opclock_vec", "hyx_connector_id_vec", "capabilities_at_broker_vec", "capabilities_map", "network_connection_info", "bw_limits", "ungrouped_hyx_connector_id_vec", "connector_group_vec", "scalable")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[NetworkRealm.Type]
        kExternalBifrost: _ClassVar[NetworkRealm.Type]
        kRigel: _ClassVar[NetworkRealm.Type]
        kCohesityCp: _ClassVar[NetworkRealm.Type]
    kUnknown: NetworkRealm.Type
    kExternalBifrost: NetworkRealm.Type
    kRigel: NetworkRealm.Type
    kCohesityCp: NetworkRealm.Type
    class ExternalBifrostInfo(_message.Message):
        __slots__ = ("hyx_certificate_version",)
        HYX_CERTIFICATE_VERSION_FIELD_NUMBER: _ClassVar[int]
        hyx_certificate_version: int
        def __init__(self, hyx_certificate_version: _Optional[int] = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("adding_network_realm", "renaming_network_realm", "deleting_network_realm")
        class AddingNetworkRealm(_message.Message):
            __slots__ = ("realm_name",)
            REALM_NAME_FIELD_NUMBER: _ClassVar[int]
            realm_name: str
            def __init__(self, realm_name: _Optional[str] = ...) -> None: ...
        class RenamingNetworkRealm(_message.Message):
            __slots__ = ("new_realm_name",)
            NEW_REALM_NAME_FIELD_NUMBER: _ClassVar[int]
            new_realm_name: str
            def __init__(self, new_realm_name: _Optional[str] = ...) -> None: ...
        class DeletingNetworkRealm(_message.Message):
            __slots__ = ("realm_id",)
            REALM_ID_FIELD_NUMBER: _ClassVar[int]
            realm_id: int
            def __init__(self, realm_id: _Optional[int] = ...) -> None: ...
        ADDING_NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
        RENAMING_NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
        DELETING_NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
        adding_network_realm: NetworkRealm.UpdateIntent.AddingNetworkRealm
        renaming_network_realm: NetworkRealm.UpdateIntent.RenamingNetworkRealm
        deleting_network_realm: NetworkRealm.UpdateIntent.DeletingNetworkRealm
        def __init__(self, adding_network_realm: _Optional[_Union[NetworkRealm.UpdateIntent.AddingNetworkRealm, _Mapping]] = ..., renaming_network_realm: _Optional[_Union[NetworkRealm.UpdateIntent.RenamingNetworkRealm, _Mapping]] = ..., deleting_network_realm: _Optional[_Union[NetworkRealm.UpdateIntent.DeletingNetworkRealm, _Mapping]] = ...) -> None: ...
    class CapabilitiesAtBroker(_message.Message):
        __slots__ = ("broker_constituent_id", "capabilities_at_broker_map")
        class CapabilitiesAtBrokerMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
        BROKER_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_AT_BROKER_MAP_FIELD_NUMBER: _ClassVar[int]
        broker_constituent_id: int
        capabilities_at_broker_map: _containers.ScalarMap[str, bool]
        def __init__(self, broker_constituent_id: _Optional[int] = ..., capabilities_at_broker_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...
    class CapabilitiesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class ConnectorGroup(_message.Message):
        __slots__ = ("connector_group_name", "connector_group_id", "hyx_connector_id_vec", "bw_limits")
        CONNECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        HYX_CONNECTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        BW_LIMITS_FIELD_NUMBER: _ClassVar[int]
        connector_group_name: str
        connector_group_id: int
        hyx_connector_id_vec: _containers.RepeatedScalarFieldContainer[int]
        bw_limits: _cluster_config_pb2.ClusterConfigProto.BandwidthLimits
        def __init__(self, connector_group_name: _Optional[str] = ..., connector_group_id: _Optional[int] = ..., hyx_connector_id_vec: _Optional[_Iterable[int]] = ..., bw_limits: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BandwidthLimits, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    REALM_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REALM_SUBNET_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_BIFROST_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    HYX_CONNECTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_AT_BROKER_VEC_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_MAP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    BW_LIMITS_FIELD_NUMBER: _ClassVar[int]
    UNGROUPED_HYX_CONNECTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    SCALABLE_FIELD_NUMBER: _ClassVar[int]
    type: NetworkRealm.Type
    deleted: bool
    realm_id: int
    realm_name: str
    tenant_id: str
    realm_subnet: Subnet
    external_bifrost_info: NetworkRealm.ExternalBifrostInfo
    update_intent: NetworkRealm.UpdateIntent
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    hyx_connector_id_vec: _containers.RepeatedScalarFieldContainer[int]
    capabilities_at_broker_vec: _containers.RepeatedCompositeFieldContainer[NetworkRealm.CapabilitiesAtBroker]
    capabilities_map: _containers.ScalarMap[str, bool]
    network_connection_info: NetworkConnInfo
    bw_limits: _cluster_config_pb2.ClusterConfigProto.BandwidthLimits
    ungrouped_hyx_connector_id_vec: _containers.RepeatedScalarFieldContainer[int]
    connector_group_vec: _containers.RepeatedCompositeFieldContainer[NetworkRealm.ConnectorGroup]
    scalable: bool
    def __init__(self, type: _Optional[_Union[NetworkRealm.Type, str]] = ..., deleted: bool = ..., realm_id: _Optional[int] = ..., realm_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., realm_subnet: _Optional[_Union[Subnet, _Mapping]] = ..., external_bifrost_info: _Optional[_Union[NetworkRealm.ExternalBifrostInfo, _Mapping]] = ..., update_intent: _Optional[_Union[NetworkRealm.UpdateIntent, _Mapping]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., hyx_connector_id_vec: _Optional[_Iterable[int]] = ..., capabilities_at_broker_vec: _Optional[_Iterable[_Union[NetworkRealm.CapabilitiesAtBroker, _Mapping]]] = ..., capabilities_map: _Optional[_Mapping[str, bool]] = ..., network_connection_info: _Optional[_Union[NetworkConnInfo, _Mapping]] = ..., bw_limits: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.BandwidthLimits, _Mapping]] = ..., ungrouped_hyx_connector_id_vec: _Optional[_Iterable[int]] = ..., connector_group_vec: _Optional[_Iterable[_Union[NetworkRealm.ConnectorGroup, _Mapping]]] = ..., scalable: bool = ...) -> None: ...

class HyxConnectorConfigProto(_message.Message):
    __slots__ = ("hyx_connector_id", "hyx_connector_name", "type", "realm_id", "connector_group_id", "certificate_version_vec", "certificate_version", "connection_status", "cohesity_side_ip", "tenant_source_side_ip", "version", "opclock_vec", "cloud_metadata", "initiator_type")
    class ConnectionStatus(_message.Message):
        __slots__ = ("is_connected", "error_msg", "last_connected_timestamp_usecs")
        IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
        ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
        LAST_CONNECTED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        is_connected: bool
        error_msg: str
        last_connected_timestamp_usecs: int
        def __init__(self, is_connected: bool = ..., error_msg: _Optional[str] = ..., last_connected_timestamp_usecs: _Optional[int] = ...) -> None: ...
    HYX_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    HYX_CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COHESITY_SIDE_IP_FIELD_NUMBER: _ClassVar[int]
    TENANT_SOURCE_SIDE_IP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_METADATA_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    hyx_connector_id: int
    hyx_connector_name: str
    type: NetworkRealm.Type
    realm_id: int
    connector_group_id: int
    certificate_version_vec: _containers.RepeatedScalarFieldContainer[int]
    certificate_version: int
    connection_status: HyxConnectorConfigProto.ConnectionStatus
    cohesity_side_ip: str
    tenant_source_side_ip: str
    version: str
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    cloud_metadata: BifrostCloudMetadataProto
    initiator_type: NetworkRealm.Type
    def __init__(self, hyx_connector_id: _Optional[int] = ..., hyx_connector_name: _Optional[str] = ..., type: _Optional[_Union[NetworkRealm.Type, str]] = ..., realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., certificate_version_vec: _Optional[_Iterable[int]] = ..., certificate_version: _Optional[int] = ..., connection_status: _Optional[_Union[HyxConnectorConfigProto.ConnectionStatus, _Mapping]] = ..., cohesity_side_ip: _Optional[str] = ..., tenant_source_side_ip: _Optional[str] = ..., version: _Optional[str] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., cloud_metadata: _Optional[_Union[BifrostCloudMetadataProto, _Mapping]] = ..., initiator_type: _Optional[_Union[NetworkRealm.Type, str]] = ...) -> None: ...

class NetworkRealmNameMappingKey(_message.Message):
    __slots__ = ("realm_name", "tenant_id")
    REALM_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    realm_name: str
    tenant_id: str
    def __init__(self, realm_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class NetworkRealmNameMappingProto(_message.Message):
    __slots__ = ("realm_id", "opclock_vec")
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    realm_id: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, realm_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class BifrostResourceCapacityProto(_message.Message):
    __slots__ = ("legacy_capacity", "max_disks_can_attach")
    LEGACY_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DISKS_CAN_ATTACH_FIELD_NUMBER: _ClassVar[int]
    legacy_capacity: float
    max_disks_can_attach: float
    def __init__(self, legacy_capacity: _Optional[float] = ..., max_disks_can_attach: _Optional[float] = ...) -> None: ...

class BifrostCloudMetadataProto(_message.Message):
    __slots__ = ("aws_metadata", "azure_metadata")
    AWS_METADATA_FIELD_NUMBER: _ClassVar[int]
    AZURE_METADATA_FIELD_NUMBER: _ClassVar[int]
    aws_metadata: BifrostAwsMetadataProto
    azure_metadata: BifrostAzureMetadataProto
    def __init__(self, aws_metadata: _Optional[_Union[BifrostAwsMetadataProto, _Mapping]] = ..., azure_metadata: _Optional[_Union[BifrostAzureMetadataProto, _Mapping]] = ...) -> None: ...

class BifrostAwsMetadataProto(_message.Message):
    __slots__ = ("aws_instance_id",)
    AWS_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    aws_instance_id: str
    def __init__(self, aws_instance_id: _Optional[str] = ...) -> None: ...

class BifrostAzureMetadataProto(_message.Message):
    __slots__ = ("azure_vm_id", "max_data_disk_count")
    AZURE_VM_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    azure_vm_id: str
    max_data_disk_count: int
    def __init__(self, azure_vm_id: _Optional[str] = ..., max_data_disk_count: _Optional[int] = ...) -> None: ...
