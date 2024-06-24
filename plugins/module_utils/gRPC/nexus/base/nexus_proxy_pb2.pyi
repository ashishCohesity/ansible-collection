from configs import cluster_config_pb2 as _cluster_config_pb2
from configs.uda import uda_configs_pb2 as _uda_configs_pb2
from nexus.base import error_pb2 as _error_pb2
from nexus.base import liveness_pb2 as _liveness_pb2
from nexus.base import packages_pb2 as _packages_pb2
from nexus.base import test_dev_pb2 as _test_dev_pb2
from nexus.base import axon_pb2 as _axon_pb2
from nexus.base import fru_data_pb2 as _fru_data_pb2
from nexus.base import axon_config_pb2 as _axon_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ("error", "error_message")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto.Type
    error_message: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class DiscoverNodesResult(_message.Message):
    __slots__ = ("status", "node_vec")
    class Node(_message.Message):
        __slots__ = ("id", "address_vec", "txt_record_vec")
        class Address(_message.Message):
            __slots__ = ("ip_address", "port", "local_interface_index")
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            LOCAL_INTERFACE_INDEX_FIELD_NUMBER: _ClassVar[int]
            ip_address: str
            port: int
            local_interface_index: int
            def __init__(self, ip_address: _Optional[str] = ..., port: _Optional[int] = ..., local_interface_index: _Optional[int] = ...) -> None: ...
        class NameValuePair(_message.Message):
            __slots__ = ("name", "value")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
        TXT_RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
        id: int
        address_vec: _containers.RepeatedCompositeFieldContainer[DiscoverNodesResult.Node.Address]
        txt_record_vec: _containers.RepeatedCompositeFieldContainer[DiscoverNodesResult.Node.NameValuePair]
        def __init__(self, id: _Optional[int] = ..., address_vec: _Optional[_Iterable[_Union[DiscoverNodesResult.Node.Address, _Mapping]]] = ..., txt_record_vec: _Optional[_Iterable[_Union[DiscoverNodesResult.Node.NameValuePair, _Mapping]]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_vec: _containers.RepeatedCompositeFieldContainer[DiscoverNodesResult.Node]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[DiscoverNodesResult.Node, _Mapping]]] = ...) -> None: ...

class LookupKeyResult(_message.Message):
    __slots__ = ("status", "key", "data", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    data: bytes
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., data: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class UpdateKeyArg(_message.Message):
    __slots__ = ("key", "expected_version", "data", "writer_writes_unique_data")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WRITER_WRITES_UNIQUE_DATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    expected_version: int
    data: bytes
    writer_writes_unique_data: bool
    def __init__(self, key: _Optional[str] = ..., expected_version: _Optional[int] = ..., data: _Optional[bytes] = ..., writer_writes_unique_data: bool = ...) -> None: ...

class UpdateKeyResult(_message.Message):
    __slots__ = ("status", "key", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DeleteKeyArg(_message.Message):
    __slots__ = ("key", "expected_version")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    key: str
    expected_version: int
    def __init__(self, key: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class DeleteKeyResult(_message.Message):
    __slots__ = ("status", "key", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class WatchClusterConfigArg(_message.Message):
    __slots__ = ("version", "client_name")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    version: int
    client_name: str
    def __init__(self, version: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...

class WatchAxonConfigArg(_message.Message):
    __slots__ = ("version", "client_name")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    version: int
    client_name: str
    def __init__(self, version: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...

class WatchClusterConfigResult(_message.Message):
    __slots__ = ("status", "version", "config_proto")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: int
    config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[int] = ..., config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class WatchAxonConfigResult(_message.Message):
    __slots__ = ("status", "version", "axon_config_proto")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AXON_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: int
    axon_config_proto: _axon_config_pb2.AxonConfig
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[int] = ..., axon_config_proto: _Optional[_Union[_axon_config_pb2.AxonConfig, _Mapping]] = ...) -> None: ...

class NotifyArg(_message.Message):
    __slots__ = ("in_cluster", "update_package_list", "reassign_vips")
    IN_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PACKAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    REASSIGN_VIPS_FIELD_NUMBER: _ClassVar[int]
    in_cluster: bool
    update_package_list: bool
    reassign_vips: bool
    def __init__(self, in_cluster: bool = ..., update_package_list: bool = ..., reassign_vips: bool = ...) -> None: ...

class NotifyResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class AllocateConstituentIdResult(_message.Message):
    __slots__ = ("status", "constituent_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    constituent_id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., constituent_id: _Optional[int] = ...) -> None: ...

class AcquireUpgradeTicketArg(_message.Message):
    __slots__ = ("node_id", "timeout_secs")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    timeout_secs: int
    def __init__(self, node_id: _Optional[int] = ..., timeout_secs: _Optional[int] = ...) -> None: ...

class AcquireUpgradeTicketResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UDAConnectorConfigResult(_message.Message):
    __slots__ = ("status", "config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    config: _uda_configs_pb2.UDAConnectorConfiguration
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., config: _Optional[_Union[_uda_configs_pb2.UDAConnectorConfiguration, _Mapping]] = ...) -> None: ...

class ReleaseUpgradeTicketArg(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class ReleaseUpgradeTicketResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class NodesLivenessResult(_message.Message):
    __slots__ = ("status", "node_vec")
    class Node(_message.Message):
        __slots__ = ("id", "liveness_data")
        ID_FIELD_NUMBER: _ClassVar[int]
        LIVENESS_DATA_FIELD_NUMBER: _ClassVar[int]
        id: int
        liveness_data: _liveness_pb2.LivenessProto
        def __init__(self, id: _Optional[int] = ..., liveness_data: _Optional[_Union[_liveness_pb2.LivenessProto, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_vec: _containers.RepeatedCompositeFieldContainer[NodesLivenessResult.Node]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[NodesLivenessResult.Node, _Mapping]]] = ...) -> None: ...

class PackageListResult(_message.Message):
    __slots__ = ("status", "node_vec")
    class Node(_message.Message):
        __slots__ = ("id", "packages_data")
        ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGES_DATA_FIELD_NUMBER: _ClassVar[int]
        id: int
        packages_data: _packages_pb2.PackagesProto
        def __init__(self, id: _Optional[int] = ..., packages_data: _Optional[_Union[_packages_pb2.PackagesProto, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_vec: _containers.RepeatedCompositeFieldContainer[PackageListResult.Node]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[PackageListResult.Node, _Mapping]]] = ...) -> None: ...

class NexusProxyUrisProto(_message.Message):
    __slots__ = ("base_uri", "node_discover_uri", "lookup_key_uri", "update_key_uri", "delete_key_uri", "watch_config_uri", "notif_uri", "alloc_constituent_id_uri", "acquire_upgrade_ticket_uri", "release_upgrade_ticket_uri", "fetch_liveness_data_uri", "list_packages_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_DISCOVER_URI_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    WATCH_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    NOTIF_URI_FIELD_NUMBER: _ClassVar[int]
    ALLOC_CONSTITUENT_ID_URI_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_UPGRADE_TICKET_URI_FIELD_NUMBER: _ClassVar[int]
    RELEASE_UPGRADE_TICKET_URI_FIELD_NUMBER: _ClassVar[int]
    FETCH_LIVENESS_DATA_URI_FIELD_NUMBER: _ClassVar[int]
    LIST_PACKAGES_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    node_discover_uri: str
    lookup_key_uri: str
    update_key_uri: str
    delete_key_uri: str
    watch_config_uri: str
    notif_uri: str
    alloc_constituent_id_uri: str
    acquire_upgrade_ticket_uri: str
    release_upgrade_ticket_uri: str
    fetch_liveness_data_uri: str
    list_packages_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., node_discover_uri: _Optional[str] = ..., lookup_key_uri: _Optional[str] = ..., update_key_uri: _Optional[str] = ..., delete_key_uri: _Optional[str] = ..., watch_config_uri: _Optional[str] = ..., notif_uri: _Optional[str] = ..., alloc_constituent_id_uri: _Optional[str] = ..., acquire_upgrade_ticket_uri: _Optional[str] = ..., release_upgrade_ticket_uri: _Optional[str] = ..., fetch_liveness_data_uri: _Optional[str] = ..., list_packages_uri: _Optional[str] = ...) -> None: ...

class InitializationStatus(_message.Message):
    __slots__ = ("is_initialized",)
    IS_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    is_initialized: bool
    def __init__(self, is_initialized: bool = ...) -> None: ...

class TimeServiceStatus(_message.Message):
    __slots__ = ("status", "is_time_set", "is_daemon_running")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_TIME_SET_FIELD_NUMBER: _ClassVar[int]
    IS_DAEMON_RUNNING_FIELD_NUMBER: _ClassVar[int]
    status: Status
    is_time_set: bool
    is_daemon_running: bool
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., is_time_set: bool = ..., is_daemon_running: bool = ...) -> None: ...

class VersionProto(_message.Message):
    __slots__ = ("kms_version", "incarnation_id")
    KMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    kms_version: int
    incarnation_id: int
    def __init__(self, kms_version: _Optional[int] = ..., incarnation_id: _Optional[int] = ...) -> None: ...

class KeyProto(_message.Message):
    __slots__ = ("key", "creation_timestamp_secs", "version", "last_key_rotation_timestamp_secs")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_KEY_ROTATION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    creation_timestamp_secs: int
    version: VersionProto
    last_key_rotation_timestamp_secs: int
    def __init__(self, key: _Optional[bytes] = ..., creation_timestamp_secs: _Optional[int] = ..., version: _Optional[_Union[VersionProto, _Mapping]] = ..., last_key_rotation_timestamp_secs: _Optional[int] = ...) -> None: ...

class GetKeyArg(_message.Message):
    __slots__ = ("disk_id", "viewbox_id")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    viewbox_id: int
    def __init__(self, disk_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ...) -> None: ...

class GetKeyResult(_message.Message):
    __slots__ = ("error", "key", "alternate_key")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_KEY_FIELD_NUMBER: _ClassVar[int]
    error: Status
    key: KeyProto
    alternate_key: KeyProto
    def __init__(self, error: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[_Union[KeyProto, _Mapping]] = ..., alternate_key: _Optional[_Union[KeyProto, _Mapping]] = ...) -> None: ...

class KeyRotationArg(_message.Message):
    __slots__ = ("disk_serial_number",)
    DISK_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    disk_serial_number: str
    def __init__(self, disk_serial_number: _Optional[str] = ...) -> None: ...

class StartDiskKeyRotationResult(_message.Message):
    __slots__ = ("error", "new_key", "current_key")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NEW_KEY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_KEY_FIELD_NUMBER: _ClassVar[int]
    error: Status
    new_key: KeyProto
    current_key: KeyProto
    def __init__(self, error: _Optional[_Union[Status, _Mapping]] = ..., new_key: _Optional[_Union[KeyProto, _Mapping]] = ..., current_key: _Optional[_Union[KeyProto, _Mapping]] = ...) -> None: ...

class FinalizeDiskKeyRotationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Status
    def __init__(self, error: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetTestDevMasterNodeIdResult(_message.Message):
    __slots__ = ("status", "node_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetAxonMasterNodeIdResult(_message.Message):
    __slots__ = ("status", "node_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetBreakfixMasterNodeIdResult(_message.Message):
    __slots__ = ("status", "node_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    node_id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., node_id: _Optional[int] = ...) -> None: ...

class CreateIscsiViewRequest(_message.Message):
    __slots__ = ("storage_domain", "view_name")
    STORAGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    storage_domain: str
    view_name: str
    def __init__(self, storage_domain: _Optional[str] = ..., view_name: _Optional[str] = ...) -> None: ...

class CreateIscsiViewResult(_message.Message):
    __slots__ = ("target_name", "error")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    error: str
    def __init__(self, target_name: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class DeleteIscsiViewRequest(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class DeleteIscsiViewResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class CloneToIscsiLunRequest(_message.Message):
    __slots__ = ("src_file", "iscsi_view_name")
    SRC_FILE_FIELD_NUMBER: _ClassVar[int]
    ISCSI_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    src_file: str
    iscsi_view_name: str
    def __init__(self, src_file: _Optional[str] = ..., iscsi_view_name: _Optional[str] = ...) -> None: ...

class CloneToIscsiLunResult(_message.Message):
    __slots__ = ("target_name", "lun", "error")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    lun: int
    error: str
    def __init__(self, target_name: _Optional[str] = ..., lun: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class CreateIscsiLunRequest(_message.Message):
    __slots__ = ("target_name", "file_size", "sub_file_size")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    file_size: int
    sub_file_size: int
    def __init__(self, target_name: _Optional[str] = ..., file_size: _Optional[int] = ..., sub_file_size: _Optional[int] = ...) -> None: ...

class CreateIscsiLunResult(_message.Message):
    __slots__ = ("lun", "error")
    LUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    lun: int
    error: str
    def __init__(self, lun: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class DeleteIscsiLunRequest(_message.Message):
    __slots__ = ("target_name", "lun_number")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    lun_number: int
    def __init__(self, target_name: _Optional[str] = ..., lun_number: _Optional[int] = ...) -> None: ...

class DeleteIscsiLunResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GetTestDevVMConfigResult(_message.Message):
    __slots__ = ("status", "vm_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    vm_config: _test_dev_pb2.VMConfig
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., vm_config: _Optional[_Union[_test_dev_pb2.VMConfig, _Mapping]] = ...) -> None: ...

class UpdateTestDevVMConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteVMConfigArg(_message.Message):
    __slots__ = ("vm_uuid",)
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ...) -> None: ...

class DeleteTestDevVMConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetAllTestDevVMConfigResult(_message.Message):
    __slots__ = ("status", "vm_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    vm_config: _containers.RepeatedCompositeFieldContainer[_test_dev_pb2.VMConfig]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., vm_config: _Optional[_Iterable[_Union[_test_dev_pb2.VMConfig, _Mapping]]] = ...) -> None: ...

class GetFRUDataResult(_message.Message):
    __slots__ = ("status", "fru_data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FRU_DATA_FIELD_NUMBER: _ClassVar[int]
    status: Status
    fru_data: _fru_data_pb2.FRUData
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., fru_data: _Optional[_Union[_fru_data_pb2.FRUData, _Mapping]] = ...) -> None: ...

class SetFRUDataResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class AllocateIdsResult(_message.Message):
    __slots__ = ("status", "id", "num_ids_allocated")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_IDS_ALLOCATED_FIELD_NUMBER: _ClassVar[int]
    status: Status
    id: int
    num_ids_allocated: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., id: _Optional[int] = ..., num_ids_allocated: _Optional[int] = ...) -> None: ...

class ListAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status", "network_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    network_config: NetworkStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., network_config: _Optional[_Union[NetworkStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonNetworkConfigArg(_message.Message):
    __slots__ = ("network_uuid",)
    NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
    network_uuid: str
    def __init__(self, network_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonNetworkConfigResult(_message.Message):
    __slots__ = ("status", "network_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    network_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Network]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., network_config: _Optional[_Iterable[_Union[_axon_pb2.Network, _Mapping]]] = ...) -> None: ...

class ListAxonPortConfigResult(_message.Message):
    __slots__ = ("status", "port_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    port_config: PortStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., port_config: _Optional[_Union[PortStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonPortConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonPortConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonPortConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonPortConfigArg(_message.Message):
    __slots__ = ("port_uuid",)
    PORT_UUID_FIELD_NUMBER: _ClassVar[int]
    port_uuid: str
    def __init__(self, port_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonPortConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonPortConfigResult(_message.Message):
    __slots__ = ("status", "port_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    port_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Port]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., port_config: _Optional[_Iterable[_Union[_axon_pb2.Port, _Mapping]]] = ...) -> None: ...

class ListAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status", "port_profile_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PORT_PROFILE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    port_profile_config: PortProfileStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., port_profile_config: _Optional[_Union[PortProfileStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonPortProfileConfigArg(_message.Message):
    __slots__ = ("port_profile_uuid",)
    PORT_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    port_profile_uuid: str
    def __init__(self, port_profile_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonPortProfileConfigResult(_message.Message):
    __slots__ = ("status", "port_profile_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PORT_PROFILE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    port_profile_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.PortProfile]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., port_profile_config: _Optional[_Iterable[_Union[_axon_pb2.PortProfile, _Mapping]]] = ...) -> None: ...

class ListAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status", "sec_grp_rule_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEC_GRP_RULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    sec_grp_rule_config: SecGrpRuleStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., sec_grp_rule_config: _Optional[_Union[SecGrpRuleStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonSecurityGroupRuleConfigArg(_message.Message):
    __slots__ = ("sec_grp_rule_uuid",)
    SEC_GRP_RULE_UUID_FIELD_NUMBER: _ClassVar[int]
    sec_grp_rule_uuid: str
    def __init__(self, sec_grp_rule_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonSecurityGroupRuleConfigResult(_message.Message):
    __slots__ = ("status", "sec_grp_rule_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEC_GRP_RULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    sec_grp_rule_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.SecurityGroupRule]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., sec_grp_rule_config: _Optional[_Iterable[_Union[_axon_pb2.SecurityGroupRule, _Mapping]]] = ...) -> None: ...

class ListAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status", "sec_grp_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEC_GRP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    sec_grp_config: SecGrpStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., sec_grp_config: _Optional[_Union[SecGrpStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonSecurityGroupConfigArg(_message.Message):
    __slots__ = ("sec_grp_uuid",)
    SEC_GRP_UUID_FIELD_NUMBER: _ClassVar[int]
    sec_grp_uuid: str
    def __init__(self, sec_grp_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonSecurityGroupConfigResult(_message.Message):
    __slots__ = ("status", "sec_grp_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEC_GRP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    sec_grp_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.SecurityGroup]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., sec_grp_config: _Optional[_Iterable[_Union[_axon_pb2.SecurityGroup, _Mapping]]] = ...) -> None: ...

class ListAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status", "subnet_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    subnet_config: SubnetStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., subnet_config: _Optional[_Union[SubnetStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonSubnetConfigArg(_message.Message):
    __slots__ = ("subnet_uuid",)
    SUBNET_UUID_FIELD_NUMBER: _ClassVar[int]
    subnet_uuid: str
    def __init__(self, subnet_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonSubnetConfigResult(_message.Message):
    __slots__ = ("status", "subnet_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    subnet_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Subnet]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., subnet_config: _Optional[_Iterable[_Union[_axon_pb2.Subnet, _Mapping]]] = ...) -> None: ...

class ListAxonRouterConfigResult(_message.Message):
    __slots__ = ("status", "router_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    router_config: RouterStateObject
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., router_config: _Optional[_Union[RouterStateObject, _Mapping]] = ...) -> None: ...

class CreateAxonRouterConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateAxonRouterConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RevertAxonRouterConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteAxonRouterConfigArg(_message.Message):
    __slots__ = ("router_uuid",)
    ROUTER_UUID_FIELD_NUMBER: _ClassVar[int]
    router_uuid: str
    def __init__(self, router_uuid: _Optional[str] = ...) -> None: ...

class DeleteAxonRouterConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ListAllAxonRouterConfigResult(_message.Message):
    __slots__ = ("status", "router_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    router_config: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Router]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., router_config: _Optional[_Iterable[_Union[_axon_pb2.Router, _Mapping]]] = ...) -> None: ...

class AcquireAxonWorkerLockArg(_message.Message):
    __slots__ = ("lock_names",)
    LOCK_NAMES_FIELD_NUMBER: _ClassVar[int]
    lock_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lock_names: _Optional[_Iterable[str]] = ...) -> None: ...

class AcquireAxonWorkerLockResult(_message.Message):
    __slots__ = ("status", "lock_ids")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    lock_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., lock_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ReleaseAxonWorkerLockArg(_message.Message):
    __slots__ = ("lock_names",)
    LOCK_NAMES_FIELD_NUMBER: _ClassVar[int]
    lock_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lock_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ReleaseAxonWorkerLockResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class NetworkStateObject(_message.Message):
    __slots__ = ("network",)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Network]
    def __init__(self, network: _Optional[_Iterable[_Union[_axon_pb2.Network, _Mapping]]] = ...) -> None: ...

class PortStateObject(_message.Message):
    __slots__ = ("port",)
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Port]
    def __init__(self, port: _Optional[_Iterable[_Union[_axon_pb2.Port, _Mapping]]] = ...) -> None: ...

class PortProfileStateObject(_message.Message):
    __slots__ = ("port_profile",)
    PORT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    port_profile: _containers.RepeatedCompositeFieldContainer[_axon_pb2.PortProfile]
    def __init__(self, port_profile: _Optional[_Iterable[_Union[_axon_pb2.PortProfile, _Mapping]]] = ...) -> None: ...

class SecGrpRuleStateObject(_message.Message):
    __slots__ = ("sec_grp_rule",)
    SEC_GRP_RULE_FIELD_NUMBER: _ClassVar[int]
    sec_grp_rule: _containers.RepeatedCompositeFieldContainer[_axon_pb2.SecurityGroupRule]
    def __init__(self, sec_grp_rule: _Optional[_Iterable[_Union[_axon_pb2.SecurityGroupRule, _Mapping]]] = ...) -> None: ...

class SecGrpStateObject(_message.Message):
    __slots__ = ("sec_grp",)
    SEC_GRP_FIELD_NUMBER: _ClassVar[int]
    sec_grp: _containers.RepeatedCompositeFieldContainer[_axon_pb2.SecurityGroup]
    def __init__(self, sec_grp: _Optional[_Iterable[_Union[_axon_pb2.SecurityGroup, _Mapping]]] = ...) -> None: ...

class SubnetStateObject(_message.Message):
    __slots__ = ("subnet",)
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    subnet: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Subnet]
    def __init__(self, subnet: _Optional[_Iterable[_Union[_axon_pb2.Subnet, _Mapping]]] = ...) -> None: ...

class RouterStateObject(_message.Message):
    __slots__ = ("router",)
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    router: _containers.RepeatedCompositeFieldContainer[_axon_pb2.Router]
    def __init__(self, router: _Optional[_Iterable[_Union[_axon_pb2.Router, _Mapping]]] = ...) -> None: ...

class GetAxonJWTTokenArg(_message.Message):
    __slots__ = ("tenant_id", "user_id", "cluster_id", "issuer", "user_roles")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    USER_ROLES_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    user_id: str
    cluster_id: str
    issuer: str
    user_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenant_id: _Optional[str] = ..., user_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., issuer: _Optional[str] = ..., user_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAxonJWTTokenResult(_message.Message):
    __slots__ = ("status", "token")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: Status
    token: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...
