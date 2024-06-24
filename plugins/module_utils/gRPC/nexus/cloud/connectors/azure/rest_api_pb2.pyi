from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenResponse(_message.Message):
    __slots__ = ("resource", "token_type", "access_token", "expires_in", "expires_on")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_ON_FIELD_NUMBER: _ClassVar[int]
    resource: str
    token_type: str
    access_token: str
    expires_in: str
    expires_on: str
    def __init__(self, resource: _Optional[str] = ..., token_type: _Optional[str] = ..., access_token: _Optional[str] = ..., expires_in: _Optional[str] = ..., expires_on: _Optional[str] = ...) -> None: ...

class AzureStackADFSTokenResponse(_message.Message):
    __slots__ = ("token_type", "access_token", "expires_in")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    token_type: str
    access_token: str
    expires_in: int
    def __init__(self, token_type: _Optional[str] = ..., access_token: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class EndpointResponse(_message.Message):
    __slots__ = ("authentication",)
    class Authentication(_message.Message):
        __slots__ = ("audiences",)
        AUDIENCES_FIELD_NUMBER: _ClassVar[int]
        audiences: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, audiences: _Optional[_Iterable[str]] = ...) -> None: ...
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    authentication: EndpointResponse.Authentication
    def __init__(self, authentication: _Optional[_Union[EndpointResponse.Authentication, _Mapping]] = ...) -> None: ...

class ResourceGroupDetails(_message.Message):
    __slots__ = ("id", "name", "location", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState",)
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    properties: ResourceGroupDetails.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[ResourceGroupDetails.Properties, _Mapping]] = ...) -> None: ...

class ResourceGroupResponse(_message.Message):
    __slots__ = ("value", "next_url")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ResourceGroupDetails]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[ResourceGroupDetails, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class GetCommandResponse(_message.Message):
    __slots__ = ("id", "name", "location", "properties")
    class Properties(_message.Message):
        __slots__ = ("instanceView",)
        class InstanceView(_message.Message):
            __slots__ = ("error", "executionMessage", "executionState", "exitCode", "output")
            ERROR_FIELD_NUMBER: _ClassVar[int]
            EXECUTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
            EXECUTIONSTATE_FIELD_NUMBER: _ClassVar[int]
            EXITCODE_FIELD_NUMBER: _ClassVar[int]
            OUTPUT_FIELD_NUMBER: _ClassVar[int]
            error: str
            executionMessage: str
            executionState: str
            exitCode: int
            output: str
            def __init__(self, error: _Optional[str] = ..., executionMessage: _Optional[str] = ..., executionState: _Optional[str] = ..., exitCode: _Optional[int] = ..., output: _Optional[str] = ...) -> None: ...
        INSTANCEVIEW_FIELD_NUMBER: _ClassVar[int]
        instanceView: GetCommandResponse.Properties.InstanceView
        def __init__(self, instanceView: _Optional[_Union[GetCommandResponse.Properties.InstanceView, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    properties: GetCommandResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[GetCommandResponse.Properties, _Mapping]] = ...) -> None: ...

class StorageAccountResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "kind")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        kind: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[StorageAccountResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[StorageAccountResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class NetworkSecurityGroupResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState",)
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: NetworkSecurityGroupResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[NetworkSecurityGroupResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[NetworkSecurityGroupResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[NetworkSecurityGroupResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class VirtualNetworkResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState",)
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: VirtualNetworkResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[VirtualNetworkResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[VirtualNetworkResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[VirtualNetworkResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class SubnetResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState",)
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        properties: SubnetResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[SubnetResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SubnetResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[SubnetResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class InstanceMetadata(_message.Message):
    __slots__ = ("compute",)
    class Compute(_message.Message):
        __slots__ = ("location", "id", "resource_group_name", "subscription_id")
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        location: str
        id: str
        resource_group_name: str
        subscription_id: str
        def __init__(self, location: _Optional[str] = ..., id: _Optional[str] = ..., resource_group_name: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    compute: InstanceMetadata.Compute
    def __init__(self, compute: _Optional[_Union[InstanceMetadata.Compute, _Mapping]] = ...) -> None: ...

class SecurityProfile(_message.Message):
    __slots__ = ("uefi_settings", "security_type", "encryption_at_host")
    class UefiSettings(_message.Message):
        __slots__ = ("secure_boot_enabled", "vtpm_enabled")
        SECURE_BOOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        VTPM_ENABLED_FIELD_NUMBER: _ClassVar[int]
        secure_boot_enabled: bool
        vtpm_enabled: bool
        def __init__(self, secure_boot_enabled: bool = ..., vtpm_enabled: bool = ...) -> None: ...
    UEFI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_AT_HOST_FIELD_NUMBER: _ClassVar[int]
    uefi_settings: SecurityProfile.UefiSettings
    security_type: str
    encryption_at_host: bool
    def __init__(self, uefi_settings: _Optional[_Union[SecurityProfile.UefiSettings, _Mapping]] = ..., security_type: _Optional[str] = ..., encryption_at_host: bool = ...) -> None: ...

class DiskSecurityProfile(_message.Message):
    __slots__ = ("security_type", "secure_set_id")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    security_type: str
    secure_set_id: str
    def __init__(self, security_type: _Optional[str] = ..., secure_set_id: _Optional[str] = ...) -> None: ...

class VMInfo(_message.Message):
    __slots__ = ("id", "name", "location", "properties", "disk_info_vec", "plan", "tags", "zones")
    class ManagedDisk(_message.Message):
        __slots__ = ("storage_account_type", "id")
        STORAGE_ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        storage_account_type: str
        id: str
        def __init__(self, storage_account_type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class VHD(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("provisioning_state", "vm_id", "hardware_profile", "storage_profile", "network_profile", "network_interfaces", "license_type", "availability_set", "security_profile")
        class HardwareProfile(_message.Message):
            __slots__ = ("vm_size",)
            VM_SIZE_FIELD_NUMBER: _ClassVar[int]
            vm_size: str
            def __init__(self, vm_size: _Optional[str] = ...) -> None: ...
        class StorageProfile(_message.Message):
            __slots__ = ("os_disk", "data_disks")
            class OSDisk(_message.Message):
                __slots__ = ("os_type", "name", "create_option", "disk_size_GB", "caching", "managed_disk", "vhd", "encryption_settings")
                OS_TYPE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
                DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
                CACHING_FIELD_NUMBER: _ClassVar[int]
                MANAGED_DISK_FIELD_NUMBER: _ClassVar[int]
                VHD_FIELD_NUMBER: _ClassVar[int]
                ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
                os_type: str
                name: str
                create_option: str
                disk_size_GB: int
                caching: str
                managed_disk: VMInfo.ManagedDisk
                vhd: VMInfo.VHD
                encryption_settings: EncryptionSettings
                def __init__(self, os_type: _Optional[str] = ..., name: _Optional[str] = ..., create_option: _Optional[str] = ..., disk_size_GB: _Optional[int] = ..., caching: _Optional[str] = ..., managed_disk: _Optional[_Union[VMInfo.ManagedDisk, _Mapping]] = ..., vhd: _Optional[_Union[VMInfo.VHD, _Mapping]] = ..., encryption_settings: _Optional[_Union[EncryptionSettings, _Mapping]] = ...) -> None: ...
            class DataDisk(_message.Message):
                __slots__ = ("lun", "name", "create_option", "disk_size_GB", "caching", "managed_disk", "vhd", "to_be_detached", "managed_by")
                LUN_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
                DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
                CACHING_FIELD_NUMBER: _ClassVar[int]
                MANAGED_DISK_FIELD_NUMBER: _ClassVar[int]
                VHD_FIELD_NUMBER: _ClassVar[int]
                TO_BE_DETACHED_FIELD_NUMBER: _ClassVar[int]
                MANAGED_BY_FIELD_NUMBER: _ClassVar[int]
                lun: int
                name: str
                create_option: str
                disk_size_GB: int
                caching: str
                managed_disk: VMInfo.ManagedDisk
                vhd: VMInfo.VHD
                to_be_detached: bool
                managed_by: str
                def __init__(self, lun: _Optional[int] = ..., name: _Optional[str] = ..., create_option: _Optional[str] = ..., disk_size_GB: _Optional[int] = ..., caching: _Optional[str] = ..., managed_disk: _Optional[_Union[VMInfo.ManagedDisk, _Mapping]] = ..., vhd: _Optional[_Union[VMInfo.VHD, _Mapping]] = ..., to_be_detached: bool = ..., managed_by: _Optional[str] = ...) -> None: ...
            OS_DISK_FIELD_NUMBER: _ClassVar[int]
            DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
            os_disk: VMInfo.Properties.StorageProfile.OSDisk
            data_disks: _containers.RepeatedCompositeFieldContainer[VMInfo.Properties.StorageProfile.DataDisk]
            def __init__(self, os_disk: _Optional[_Union[VMInfo.Properties.StorageProfile.OSDisk, _Mapping]] = ..., data_disks: _Optional[_Iterable[_Union[VMInfo.Properties.StorageProfile.DataDisk, _Mapping]]] = ...) -> None: ...
        class NetworkProfile(_message.Message):
            __slots__ = ("network_interfaces",)
            class NetworkInterfaces(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: str
                def __init__(self, id: _Optional[str] = ...) -> None: ...
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            network_interfaces: _containers.RepeatedCompositeFieldContainer[VMInfo.Properties.NetworkProfile.NetworkInterfaces]
            def __init__(self, network_interfaces: _Optional[_Iterable[_Union[VMInfo.Properties.NetworkProfile.NetworkInterfaces, _Mapping]]] = ...) -> None: ...
        class SubResource(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        VM_ID_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
        LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_SET_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: str
        vm_id: str
        hardware_profile: VMInfo.Properties.HardwareProfile
        storage_profile: VMInfo.Properties.StorageProfile
        network_profile: VMInfo.Properties.NetworkProfile
        network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterfaceResponse]
        license_type: str
        availability_set: VMInfo.Properties.SubResource
        security_profile: SecurityProfile
        def __init__(self, provisioning_state: _Optional[str] = ..., vm_id: _Optional[str] = ..., hardware_profile: _Optional[_Union[VMInfo.Properties.HardwareProfile, _Mapping]] = ..., storage_profile: _Optional[_Union[VMInfo.Properties.StorageProfile, _Mapping]] = ..., network_profile: _Optional[_Union[VMInfo.Properties.NetworkProfile, _Mapping]] = ..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterfaceResponse, _Mapping]]] = ..., license_type: _Optional[str] = ..., availability_set: _Optional[_Union[VMInfo.Properties.SubResource, _Mapping]] = ..., security_profile: _Optional[_Union[SecurityProfile, _Mapping]] = ...) -> None: ...
    class DiskInfoProto(_message.Message):
        __slots__ = ("blob_info", "managed_disk_info", "is_bootable", "os_type", "lun", "caching", "name")
        BLOB_INFO_FIELD_NUMBER: _ClassVar[int]
        MANAGED_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        LUN_FIELD_NUMBER: _ClassVar[int]
        CACHING_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        blob_info: BlobProperties
        managed_disk_info: DiskOrSnapshotInfo
        is_bootable: bool
        os_type: str
        lun: int
        caching: str
        name: str
        def __init__(self, blob_info: _Optional[_Union[BlobProperties, _Mapping]] = ..., managed_disk_info: _Optional[_Union[DiskOrSnapshotInfo, _Mapping]] = ..., is_bootable: bool = ..., os_type: _Optional[str] = ..., lun: _Optional[int] = ..., caching: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    properties: VMInfo.Properties
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[VMInfo.DiskInfoProto]
    plan: Plan
    tags: _containers.ScalarMap[str, str]
    zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[VMInfo.Properties, _Mapping]] = ..., disk_info_vec: _Optional[_Iterable[_Union[VMInfo.DiskInfoProto, _Mapping]]] = ..., plan: _Optional[_Union[Plan, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...

class ListVMInfo(_message.Message):
    __slots__ = ("value", "nextLink")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXTLINK_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[VMInfo]
    nextLink: str
    def __init__(self, value: _Optional[_Iterable[_Union[VMInfo, _Mapping]]] = ..., nextLink: _Optional[str] = ...) -> None: ...

class SQLServerResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties", "private_endpoint_subnet_id_vec")
        class Properties(_message.Message):
            __slots__ = ("administrator_login", "version", "state", "fqdn", "public_network_access", "private_endpoint_connections")
            ADMINISTRATOR_LOGIN_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            FQDN_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
            PRIVATE_ENDPOINT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
            administrator_login: str
            version: str
            state: str
            fqdn: str
            public_network_access: str
            private_endpoint_connections: _containers.RepeatedCompositeFieldContainer[PrivateEndpointConnections]
            def __init__(self, administrator_login: _Optional[str] = ..., version: _Optional[str] = ..., state: _Optional[str] = ..., fqdn: _Optional[str] = ..., public_network_access: _Optional[str] = ..., private_endpoint_connections: _Optional[_Iterable[_Union[PrivateEndpointConnections, _Mapping]]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_SUBNET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: SQLServerResponse.Value.Properties
        private_endpoint_subnet_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[SQLServerResponse.Value.Properties, _Mapping]] = ..., private_endpoint_subnet_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SQLServerResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[SQLServerResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class SQLManagedInstanceResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties")
        class Properties(_message.Message):
            __slots__ = ("administrator_login", "version", "state", "fqdn", "public_network_access")
            ADMINISTRATOR_LOGIN_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            FQDN_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
            administrator_login: str
            version: str
            state: str
            fqdn: str
            public_network_access: str
            def __init__(self, administrator_login: _Optional[str] = ..., version: _Optional[str] = ..., state: _Optional[str] = ..., fqdn: _Optional[str] = ..., public_network_access: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: SQLManagedInstanceResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[SQLManagedInstanceResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SQLManagedInstanceResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[SQLManagedInstanceResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class SQLDatabaseSizeResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "type", "properties")
        class Properties(_message.Message):
            __slots__ = ("current_value", "display_name", "limit", "unit")
            CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            LIMIT_FIELD_NUMBER: _ClassVar[int]
            UNIT_FIELD_NUMBER: _ClassVar[int]
            current_value: int
            display_name: str
            limit: int
            unit: str
            def __init__(self, current_value: _Optional[int] = ..., display_name: _Optional[str] = ..., limit: _Optional[int] = ..., unit: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        type: str
        properties: SQLDatabaseSizeResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Union[SQLDatabaseSizeResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SQLDatabaseSizeResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[SQLDatabaseSizeResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class SQLDatabaseResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties", "sku", "tags")
        class Properties(_message.Message):
            __slots__ = ("collation", "max_size_bytes", "status", "creation_date")
            COLLATION_FIELD_NUMBER: _ClassVar[int]
            MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
            collation: str
            max_size_bytes: int
            status: str
            creation_date: str
            def __init__(self, collation: _Optional[str] = ..., max_size_bytes: _Optional[int] = ..., status: _Optional[str] = ..., creation_date: _Optional[str] = ...) -> None: ...
        class SKU(_message.Message):
            __slots__ = ("name", "tier", "capacity")
            NAME_FIELD_NUMBER: _ClassVar[int]
            TIER_FIELD_NUMBER: _ClassVar[int]
            CAPACITY_FIELD_NUMBER: _ClassVar[int]
            name: str
            tier: str
            capacity: int
            def __init__(self, name: _Optional[str] = ..., tier: _Optional[str] = ..., capacity: _Optional[int] = ...) -> None: ...
        class TagsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        SKU_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: SQLDatabaseResponse.Value.Properties
        sku: SQLDatabaseResponse.Value.SKU
        tags: _containers.ScalarMap[str, str]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[SQLDatabaseResponse.Value.Properties, _Mapping]] = ..., sku: _Optional[_Union[SQLDatabaseResponse.Value.SKU, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SQLDatabaseResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[SQLDatabaseResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class VMOptionsResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("name", "numberOfCores", "memoryInMB", "maxDataDiskCount")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NUMBEROFCORES_FIELD_NUMBER: _ClassVar[int]
        MEMORYINMB_FIELD_NUMBER: _ClassVar[int]
        MAXDATADISKCOUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        numberOfCores: int
        memoryInMB: int
        maxDataDiskCount: int
        def __init__(self, name: _Optional[str] = ..., numberOfCores: _Optional[int] = ..., memoryInMB: _Optional[int] = ..., maxDataDiskCount: _Optional[int] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[VMOptionsResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[VMOptionsResponse.Value, _Mapping]]] = ...) -> None: ...

class CreateResourceGroupRequest(_message.Message):
    __slots__ = ("location", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    location: str
    tags: _containers.ScalarMap[str, str]
    def __init__(self, location: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateStorageAccountRequest(_message.Message):
    __slots__ = ("location", "properties", "sku", "kind", "tags")
    class Properties(_message.Message):
        __slots__ = ("accessTier", "supportsHttpsTrafficOnly")
        ACCESSTIER_FIELD_NUMBER: _ClassVar[int]
        SUPPORTSHTTPSTRAFFICONLY_FIELD_NUMBER: _ClassVar[int]
        accessTier: str
        supportsHttpsTrafficOnly: bool
        def __init__(self, accessTier: _Optional[str] = ..., supportsHttpsTrafficOnly: bool = ...) -> None: ...
    class Sku(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    location: str
    properties: CreateStorageAccountRequest.Properties
    sku: CreateStorageAccountRequest.Sku
    kind: str
    tags: _containers.ScalarMap[str, str]
    def __init__(self, location: _Optional[str] = ..., properties: _Optional[_Union[CreateStorageAccountRequest.Properties, _Mapping]] = ..., sku: _Optional[_Union[CreateStorageAccountRequest.Sku, _Mapping]] = ..., kind: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateStorageAccountResponse(_message.Message):
    __slots__ = ("id", "name", "location", "type", "kind")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    type: str
    kind: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., type: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class ListStorageAccountKeyResponse(_message.Message):
    __slots__ = ("keys",)
    class Keys(_message.Message):
        __slots__ = ("keyName", "value", "permissions")
        KEYNAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        keyName: str
        value: str
        permissions: str
        def __init__(self, keyName: _Optional[str] = ..., value: _Optional[str] = ..., permissions: _Optional[str] = ...) -> None: ...
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[ListStorageAccountKeyResponse.Keys]
    def __init__(self, keys: _Optional[_Iterable[_Union[ListStorageAccountKeyResponse.Keys, _Mapping]]] = ...) -> None: ...

class CreateVirtualNetworkRequest(_message.Message):
    __slots__ = ("location", "properties", "tags")
    class Properties(_message.Message):
        __slots__ = ("addressSpace", "subnets")
        class AddressSpace(_message.Message):
            __slots__ = ("addressPrefixes",)
            ADDRESSPREFIXES_FIELD_NUMBER: _ClassVar[int]
            addressPrefixes: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, addressPrefixes: _Optional[_Iterable[str]] = ...) -> None: ...
        class Subnet(_message.Message):
            __slots__ = ("name", "properties")
            class Properties(_message.Message):
                __slots__ = ("addressPrefix",)
                ADDRESSPREFIX_FIELD_NUMBER: _ClassVar[int]
                addressPrefix: str
                def __init__(self, addressPrefix: _Optional[str] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            name: str
            properties: CreateVirtualNetworkRequest.Properties.Subnet.Properties
            def __init__(self, name: _Optional[str] = ..., properties: _Optional[_Union[CreateVirtualNetworkRequest.Properties.Subnet.Properties, _Mapping]] = ...) -> None: ...
        ADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
        SUBNETS_FIELD_NUMBER: _ClassVar[int]
        addressSpace: CreateVirtualNetworkRequest.Properties.AddressSpace
        subnets: _containers.RepeatedCompositeFieldContainer[CreateVirtualNetworkRequest.Properties.Subnet]
        def __init__(self, addressSpace: _Optional[_Union[CreateVirtualNetworkRequest.Properties.AddressSpace, _Mapping]] = ..., subnets: _Optional[_Iterable[_Union[CreateVirtualNetworkRequest.Properties.Subnet, _Mapping]]] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    location: str
    properties: CreateVirtualNetworkRequest.Properties
    tags: _containers.ScalarMap[str, str]
    def __init__(self, location: _Optional[str] = ..., properties: _Optional[_Union[CreateVirtualNetworkRequest.Properties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateVirtualNetworkResponse(_message.Message):
    __slots__ = ("id", "name", "location")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class CreateSubnetRequest(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("addressPrefix",)
        ADDRESSPREFIX_FIELD_NUMBER: _ClassVar[int]
        addressPrefix: str
        def __init__(self, addressPrefix: _Optional[str] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: CreateSubnetRequest.Properties
    def __init__(self, properties: _Optional[_Union[CreateSubnetRequest.Properties, _Mapping]] = ...) -> None: ...

class CreateSubnetResponse(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("templateLink", "template", "mode", "debugSetting", "parameters")
        class TemplateLink(_message.Message):
            __slots__ = ("uri", "contentVersion")
            URI_FIELD_NUMBER: _ClassVar[int]
            CONTENTVERSION_FIELD_NUMBER: _ClassVar[int]
            uri: str
            contentVersion: str
            def __init__(self, uri: _Optional[str] = ..., contentVersion: _Optional[str] = ...) -> None: ...
        class DebugSetting(_message.Message):
            __slots__ = ("detailLevel",)
            DETAILLEVEL_FIELD_NUMBER: _ClassVar[int]
            detailLevel: str
            def __init__(self, detailLevel: _Optional[str] = ...) -> None: ...
        class Parameters(_message.Message):
            __slots__ = ("customVmName", "sizeOfEachSSDDiskInGB", "sizeOfEachHDDDiskInGB", "adminUsername", "adminPassword", "vmSize", "osFileName", "vpnResourceGroupName", "vpnVirtualNetworkName", "vpnSubnetName", "productOffer", "numVMs", "vmIpAddresses", "numVMsPerStorageAccount", "numStorageAccounts", "vmStartIndex", "resourceGroupIndex", "storageServiceUrlSuffix", "storageAccountName", "deletionPrevention", "hyperVGeneration", "numSSDDisks", "SSDDiskType", "SSDDiskIOPs", "SSDDiskThroughputInMB", "numHDDDisks", "HDDDiskType", "HDDDiskIOPs", "HDDDiskThroughputInMB", "vmZone", "vhdResourceGroup", "location", "privateIPAllocationMethod", "cohesityTags")
            class Value(_message.Message):
                __slots__ = ("value",)
                VALUE_FIELD_NUMBER: _ClassVar[int]
                value: str
                def __init__(self, value: _Optional[str] = ...) -> None: ...
            class Tags(_message.Message):
                __slots__ = ("value",)
                class ValueEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: str
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                VALUE_FIELD_NUMBER: _ClassVar[int]
                value: _containers.ScalarMap[str, str]
                def __init__(self, value: _Optional[_Mapping[str, str]] = ...) -> None: ...
            CUSTOMVMNAME_FIELD_NUMBER: _ClassVar[int]
            SIZEOFEACHSSDDISKINGB_FIELD_NUMBER: _ClassVar[int]
            SIZEOFEACHHDDDISKINGB_FIELD_NUMBER: _ClassVar[int]
            ADMINUSERNAME_FIELD_NUMBER: _ClassVar[int]
            ADMINPASSWORD_FIELD_NUMBER: _ClassVar[int]
            VMSIZE_FIELD_NUMBER: _ClassVar[int]
            OSFILENAME_FIELD_NUMBER: _ClassVar[int]
            VPNRESOURCEGROUPNAME_FIELD_NUMBER: _ClassVar[int]
            VPNVIRTUALNETWORKNAME_FIELD_NUMBER: _ClassVar[int]
            VPNSUBNETNAME_FIELD_NUMBER: _ClassVar[int]
            PRODUCTOFFER_FIELD_NUMBER: _ClassVar[int]
            NUMVMS_FIELD_NUMBER: _ClassVar[int]
            VMIPADDRESSES_FIELD_NUMBER: _ClassVar[int]
            NUMVMSPERSTORAGEACCOUNT_FIELD_NUMBER: _ClassVar[int]
            NUMSTORAGEACCOUNTS_FIELD_NUMBER: _ClassVar[int]
            VMSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
            RESOURCEGROUPINDEX_FIELD_NUMBER: _ClassVar[int]
            STORAGESERVICEURLSUFFIX_FIELD_NUMBER: _ClassVar[int]
            STORAGEACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
            DELETIONPREVENTION_FIELD_NUMBER: _ClassVar[int]
            HYPERVGENERATION_FIELD_NUMBER: _ClassVar[int]
            NUMSSDDISKS_FIELD_NUMBER: _ClassVar[int]
            SSDDISKTYPE_FIELD_NUMBER: _ClassVar[int]
            SSDDISKIOPS_FIELD_NUMBER: _ClassVar[int]
            SSDDISKTHROUGHPUTINMB_FIELD_NUMBER: _ClassVar[int]
            NUMHDDDISKS_FIELD_NUMBER: _ClassVar[int]
            HDDDISKTYPE_FIELD_NUMBER: _ClassVar[int]
            HDDDISKIOPS_FIELD_NUMBER: _ClassVar[int]
            HDDDISKTHROUGHPUTINMB_FIELD_NUMBER: _ClassVar[int]
            VMZONE_FIELD_NUMBER: _ClassVar[int]
            VHDRESOURCEGROUP_FIELD_NUMBER: _ClassVar[int]
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            PRIVATEIPALLOCATIONMETHOD_FIELD_NUMBER: _ClassVar[int]
            COHESITYTAGS_FIELD_NUMBER: _ClassVar[int]
            customVmName: CreateDeploymentRequest.Properties.Parameters.Value
            sizeOfEachSSDDiskInGB: CreateDeploymentRequest.Properties.Parameters.Value
            sizeOfEachHDDDiskInGB: CreateDeploymentRequest.Properties.Parameters.Value
            adminUsername: CreateDeploymentRequest.Properties.Parameters.Value
            adminPassword: CreateDeploymentRequest.Properties.Parameters.Value
            vmSize: CreateDeploymentRequest.Properties.Parameters.Value
            osFileName: CreateDeploymentRequest.Properties.Parameters.Value
            vpnResourceGroupName: CreateDeploymentRequest.Properties.Parameters.Value
            vpnVirtualNetworkName: CreateDeploymentRequest.Properties.Parameters.Value
            vpnSubnetName: CreateDeploymentRequest.Properties.Parameters.Value
            productOffer: CreateDeploymentRequest.Properties.Parameters.Value
            numVMs: CreateDeploymentRequest.Properties.Parameters.Value
            vmIpAddresses: CreateDeploymentRequest.Properties.Parameters.Value
            numVMsPerStorageAccount: CreateDeploymentRequest.Properties.Parameters.Value
            numStorageAccounts: CreateDeploymentRequest.Properties.Parameters.Value
            vmStartIndex: CreateDeploymentRequest.Properties.Parameters.Value
            resourceGroupIndex: CreateDeploymentRequest.Properties.Parameters.Value
            storageServiceUrlSuffix: CreateDeploymentRequest.Properties.Parameters.Value
            storageAccountName: CreateDeploymentRequest.Properties.Parameters.Value
            deletionPrevention: CreateDeploymentRequest.Properties.Parameters.Value
            hyperVGeneration: CreateDeploymentRequest.Properties.Parameters.Value
            numSSDDisks: CreateDeploymentRequest.Properties.Parameters.Value
            SSDDiskType: CreateDeploymentRequest.Properties.Parameters.Value
            SSDDiskIOPs: CreateDeploymentRequest.Properties.Parameters.Value
            SSDDiskThroughputInMB: CreateDeploymentRequest.Properties.Parameters.Value
            numHDDDisks: CreateDeploymentRequest.Properties.Parameters.Value
            HDDDiskType: CreateDeploymentRequest.Properties.Parameters.Value
            HDDDiskIOPs: CreateDeploymentRequest.Properties.Parameters.Value
            HDDDiskThroughputInMB: CreateDeploymentRequest.Properties.Parameters.Value
            vmZone: CreateDeploymentRequest.Properties.Parameters.Value
            vhdResourceGroup: CreateDeploymentRequest.Properties.Parameters.Value
            location: CreateDeploymentRequest.Properties.Parameters.Value
            privateIPAllocationMethod: CreateDeploymentRequest.Properties.Parameters.Value
            cohesityTags: CreateDeploymentRequest.Properties.Parameters.Tags
            def __init__(self, customVmName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., sizeOfEachSSDDiskInGB: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., sizeOfEachHDDDiskInGB: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., adminUsername: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., adminPassword: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vmSize: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., osFileName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vpnResourceGroupName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vpnVirtualNetworkName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vpnSubnetName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., productOffer: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., numVMs: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vmIpAddresses: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., numVMsPerStorageAccount: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., numStorageAccounts: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vmStartIndex: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., resourceGroupIndex: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., storageServiceUrlSuffix: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., storageAccountName: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., deletionPrevention: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., hyperVGeneration: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., numSSDDisks: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., SSDDiskType: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., SSDDiskIOPs: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., SSDDiskThroughputInMB: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., numHDDDisks: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., HDDDiskType: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., HDDDiskIOPs: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., HDDDiskThroughputInMB: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vmZone: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., vhdResourceGroup: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., location: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., privateIPAllocationMethod: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Value, _Mapping]] = ..., cohesityTags: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters.Tags, _Mapping]] = ...) -> None: ...
        TEMPLATELINK_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        DEBUGSETTING_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        templateLink: CreateDeploymentRequest.Properties.TemplateLink
        template: str
        mode: str
        debugSetting: CreateDeploymentRequest.Properties.DebugSetting
        parameters: CreateDeploymentRequest.Properties.Parameters
        def __init__(self, templateLink: _Optional[_Union[CreateDeploymentRequest.Properties.TemplateLink, _Mapping]] = ..., template: _Optional[str] = ..., mode: _Optional[str] = ..., debugSetting: _Optional[_Union[CreateDeploymentRequest.Properties.DebugSetting, _Mapping]] = ..., parameters: _Optional[_Union[CreateDeploymentRequest.Properties.Parameters, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: CreateDeploymentRequest.Properties
    def __init__(self, properties: _Optional[_Union[CreateDeploymentRequest.Properties, _Mapping]] = ...) -> None: ...

class CreateDeploymentResponse(_message.Message):
    __slots__ = ("id", "name", "properties")
    class PrivateIPAddress(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...
    class Outputs(_message.Message):
        __slots__ = ("privateIPAddress",)
        PRIVATEIPADDRESS_FIELD_NUMBER: _ClassVar[int]
        privateIPAddress: CreateDeploymentResponse.PrivateIPAddress
        def __init__(self, privateIPAddress: _Optional[_Union[CreateDeploymentResponse.PrivateIPAddress, _Mapping]] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("provisioningState", "outputs")
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        outputs: CreateDeploymentResponse.Outputs
        def __init__(self, provisioningState: _Optional[str] = ..., outputs: _Optional[_Union[CreateDeploymentResponse.Outputs, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    properties: CreateDeploymentResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[CreateDeploymentResponse.Properties, _Mapping]] = ...) -> None: ...

class CreateClonedVMRequest(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("templateLink", "template", "mode", "parameters")
        class TemplateLink(_message.Message):
            __slots__ = ("uri", "contentVersion")
            URI_FIELD_NUMBER: _ClassVar[int]
            CONTENTVERSION_FIELD_NUMBER: _ClassVar[int]
            uri: str
            contentVersion: str
            def __init__(self, uri: _Optional[str] = ..., contentVersion: _Optional[str] = ...) -> None: ...
        class Parameters(_message.Message):
            __slots__ = ("vmName", "osDiskVhdUri", "osType", "vmSize", "networkResourceGroup", "vnetName", "subnetName", "numDataDiskUrl", "listDataDiskUrl", "hyperVGeneration", "storageAccountId", "create_managed_disk", "managed_os_disk_name", "os_disk_sku", "list_managed_data_disk_name", "list_managed_data_disk_sku", "max_no_of_data_disks_supported", "availabilitySetId")
            class Value(_message.Message):
                __slots__ = ("value",)
                VALUE_FIELD_NUMBER: _ClassVar[int]
                value: str
                def __init__(self, value: _Optional[str] = ...) -> None: ...
            VMNAME_FIELD_NUMBER: _ClassVar[int]
            OSDISKVHDURI_FIELD_NUMBER: _ClassVar[int]
            OSTYPE_FIELD_NUMBER: _ClassVar[int]
            VMSIZE_FIELD_NUMBER: _ClassVar[int]
            NETWORKRESOURCEGROUP_FIELD_NUMBER: _ClassVar[int]
            VNETNAME_FIELD_NUMBER: _ClassVar[int]
            SUBNETNAME_FIELD_NUMBER: _ClassVar[int]
            NUMDATADISKURL_FIELD_NUMBER: _ClassVar[int]
            LISTDATADISKURL_FIELD_NUMBER: _ClassVar[int]
            HYPERVGENERATION_FIELD_NUMBER: _ClassVar[int]
            STORAGEACCOUNTID_FIELD_NUMBER: _ClassVar[int]
            CREATE_MANAGED_DISK_FIELD_NUMBER: _ClassVar[int]
            MANAGED_OS_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
            OS_DISK_SKU_FIELD_NUMBER: _ClassVar[int]
            LIST_MANAGED_DATA_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
            LIST_MANAGED_DATA_DISK_SKU_FIELD_NUMBER: _ClassVar[int]
            MAX_NO_OF_DATA_DISKS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
            AVAILABILITYSETID_FIELD_NUMBER: _ClassVar[int]
            vmName: CreateClonedVMRequest.Properties.Parameters.Value
            osDiskVhdUri: CreateClonedVMRequest.Properties.Parameters.Value
            osType: CreateClonedVMRequest.Properties.Parameters.Value
            vmSize: CreateClonedVMRequest.Properties.Parameters.Value
            networkResourceGroup: CreateClonedVMRequest.Properties.Parameters.Value
            vnetName: CreateClonedVMRequest.Properties.Parameters.Value
            subnetName: CreateClonedVMRequest.Properties.Parameters.Value
            numDataDiskUrl: CreateClonedVMRequest.Properties.Parameters.Value
            listDataDiskUrl: CreateClonedVMRequest.Properties.Parameters.Value
            hyperVGeneration: CreateClonedVMRequest.Properties.Parameters.Value
            storageAccountId: CreateClonedVMRequest.Properties.Parameters.Value
            create_managed_disk: CreateClonedVMRequest.Properties.Parameters.Value
            managed_os_disk_name: CreateClonedVMRequest.Properties.Parameters.Value
            os_disk_sku: CreateClonedVMRequest.Properties.Parameters.Value
            list_managed_data_disk_name: CreateClonedVMRequest.Properties.Parameters.Value
            list_managed_data_disk_sku: CreateClonedVMRequest.Properties.Parameters.Value
            max_no_of_data_disks_supported: CreateClonedVMRequest.Properties.Parameters.Value
            availabilitySetId: CreateClonedVMRequest.Properties.Parameters.Value
            def __init__(self, vmName: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., osDiskVhdUri: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., osType: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., vmSize: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., networkResourceGroup: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., vnetName: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., subnetName: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., numDataDiskUrl: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., listDataDiskUrl: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., hyperVGeneration: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., storageAccountId: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., create_managed_disk: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., managed_os_disk_name: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., os_disk_sku: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., list_managed_data_disk_name: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., list_managed_data_disk_sku: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., max_no_of_data_disks_supported: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ..., availabilitySetId: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters.Value, _Mapping]] = ...) -> None: ...
        TEMPLATELINK_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        templateLink: CreateClonedVMRequest.Properties.TemplateLink
        template: str
        mode: str
        parameters: CreateClonedVMRequest.Properties.Parameters
        def __init__(self, templateLink: _Optional[_Union[CreateClonedVMRequest.Properties.TemplateLink, _Mapping]] = ..., template: _Optional[str] = ..., mode: _Optional[str] = ..., parameters: _Optional[_Union[CreateClonedVMRequest.Properties.Parameters, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: CreateClonedVMRequest.Properties
    def __init__(self, properties: _Optional[_Union[CreateClonedVMRequest.Properties, _Mapping]] = ...) -> None: ...

class CreateClonedVMResponse(_message.Message):
    __slots__ = ("id", "name", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState", "timestamp", "error")
        class Error(_message.Message):
            __slots__ = ("code", "message", "details")
            class Details(_message.Message):
                __slots__ = ("code", "message")
                CODE_FIELD_NUMBER: _ClassVar[int]
                MESSAGE_FIELD_NUMBER: _ClassVar[int]
                code: str
                message: str
                def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
            CODE_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            code: str
            message: str
            details: _containers.RepeatedCompositeFieldContainer[CreateClonedVMResponse.Properties.Error.Details]
            def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[CreateClonedVMResponse.Properties.Error.Details, _Mapping]]] = ...) -> None: ...
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        timestamp: str
        error: CreateClonedVMResponse.Properties.Error
        def __init__(self, provisioningState: _Optional[str] = ..., timestamp: _Optional[str] = ..., error: _Optional[_Union[CreateClonedVMResponse.Properties.Error, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    properties: CreateClonedVMResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[CreateClonedVMResponse.Properties, _Mapping]] = ...) -> None: ...

class GetNicAddressResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "name", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState", "ipConfigurations")
            class IpConfigurations(_message.Message):
                __slots__ = ("id", "name", "properties")
                class Properties(_message.Message):
                    __slots__ = ("provisioningState", "privateIPAddress", "subnet", "loadBalancerBackendAddressPools")
                    class Subnet(_message.Message):
                        __slots__ = ("id",)
                        ID_FIELD_NUMBER: _ClassVar[int]
                        id: str
                        def __init__(self, id: _Optional[str] = ...) -> None: ...
                    class LoadBalancerBackendAddressPools(_message.Message):
                        __slots__ = ("id",)
                        ID_FIELD_NUMBER: _ClassVar[int]
                        id: str
                        def __init__(self, id: _Optional[str] = ...) -> None: ...
                    PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
                    PRIVATEIPADDRESS_FIELD_NUMBER: _ClassVar[int]
                    SUBNET_FIELD_NUMBER: _ClassVar[int]
                    LOADBALANCERBACKENDADDRESSPOOLS_FIELD_NUMBER: _ClassVar[int]
                    provisioningState: str
                    privateIPAddress: str
                    subnet: GetNicAddressResponse.Value.Properties.IpConfigurations.Properties.Subnet
                    loadBalancerBackendAddressPools: _containers.RepeatedCompositeFieldContainer[GetNicAddressResponse.Value.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools]
                    def __init__(self, provisioningState: _Optional[str] = ..., privateIPAddress: _Optional[str] = ..., subnet: _Optional[_Union[GetNicAddressResponse.Value.Properties.IpConfigurations.Properties.Subnet, _Mapping]] = ..., loadBalancerBackendAddressPools: _Optional[_Iterable[_Union[GetNicAddressResponse.Value.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools, _Mapping]]] = ...) -> None: ...
                ID_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                id: str
                name: str
                properties: GetNicAddressResponse.Value.Properties.IpConfigurations.Properties
                def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetNicAddressResponse.Value.Properties.IpConfigurations.Properties, _Mapping]] = ...) -> None: ...
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            IPCONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            ipConfigurations: _containers.RepeatedCompositeFieldContainer[GetNicAddressResponse.Value.Properties.IpConfigurations]
            def __init__(self, provisioningState: _Optional[str] = ..., ipConfigurations: _Optional[_Iterable[_Union[GetNicAddressResponse.Value.Properties.IpConfigurations, _Mapping]]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        properties: GetNicAddressResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetNicAddressResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[GetNicAddressResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[GetNicAddressResponse.Value, _Mapping]]] = ...) -> None: ...

class GetSpecificNicAddressResponse(_message.Message):
    __slots__ = ("id", "name", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState", "ipConfigurations")
        class IpConfigurations(_message.Message):
            __slots__ = ("id", "name", "properties")
            class Properties(_message.Message):
                __slots__ = ("provisioningState", "privateIPAddress", "subnet", "loadBalancerBackendAddressPools")
                class Subnet(_message.Message):
                    __slots__ = ("id",)
                    ID_FIELD_NUMBER: _ClassVar[int]
                    id: str
                    def __init__(self, id: _Optional[str] = ...) -> None: ...
                class LoadBalancerBackendAddressPools(_message.Message):
                    __slots__ = ("id",)
                    ID_FIELD_NUMBER: _ClassVar[int]
                    id: str
                    def __init__(self, id: _Optional[str] = ...) -> None: ...
                PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
                PRIVATEIPADDRESS_FIELD_NUMBER: _ClassVar[int]
                SUBNET_FIELD_NUMBER: _ClassVar[int]
                LOADBALANCERBACKENDADDRESSPOOLS_FIELD_NUMBER: _ClassVar[int]
                provisioningState: str
                privateIPAddress: str
                subnet: GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties.Subnet
                loadBalancerBackendAddressPools: _containers.RepeatedCompositeFieldContainer[GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools]
                def __init__(self, provisioningState: _Optional[str] = ..., privateIPAddress: _Optional[str] = ..., subnet: _Optional[_Union[GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties.Subnet, _Mapping]] = ..., loadBalancerBackendAddressPools: _Optional[_Iterable[_Union[GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools, _Mapping]]] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            properties: GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetSpecificNicAddressResponse.Properties.IpConfigurations.Properties, _Mapping]] = ...) -> None: ...
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        IPCONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        ipConfigurations: _containers.RepeatedCompositeFieldContainer[GetSpecificNicAddressResponse.Properties.IpConfigurations]
        def __init__(self, provisioningState: _Optional[str] = ..., ipConfigurations: _Optional[_Iterable[_Union[GetSpecificNicAddressResponse.Properties.IpConfigurations, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    properties: GetSpecificNicAddressResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetSpecificNicAddressResponse.Properties, _Mapping]] = ...) -> None: ...

class GetPublicIPResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "name", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState", "ipAddress", "dnsSettings")
            class DnsSettings(_message.Message):
                __slots__ = ("domainNameLabel", "fqdn")
                DOMAINNAMELABEL_FIELD_NUMBER: _ClassVar[int]
                FQDN_FIELD_NUMBER: _ClassVar[int]
                domainNameLabel: str
                fqdn: str
                def __init__(self, domainNameLabel: _Optional[str] = ..., fqdn: _Optional[str] = ...) -> None: ...
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            IPADDRESS_FIELD_NUMBER: _ClassVar[int]
            DNSSETTINGS_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            ipAddress: str
            dnsSettings: GetPublicIPResponse.Value.Properties.DnsSettings
            def __init__(self, provisioningState: _Optional[str] = ..., ipAddress: _Optional[str] = ..., dnsSettings: _Optional[_Union[GetPublicIPResponse.Value.Properties.DnsSettings, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        properties: GetPublicIPResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetPublicIPResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[GetPublicIPResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[GetPublicIPResponse.Value, _Mapping]]] = ...) -> None: ...

class DissociateVMPublicIPRequest(_message.Message):
    __slots__ = ("location", "properties")
    class Properties(_message.Message):
        __slots__ = ("ipConfigurations",)
        class IpConfigurations(_message.Message):
            __slots__ = ("name", "properties")
            class Properties(_message.Message):
                __slots__ = ("subnet", "privateIPAllocationMethod", "loadBalancerBackendAddressPools")
                class Subnet(_message.Message):
                    __slots__ = ("id",)
                    ID_FIELD_NUMBER: _ClassVar[int]
                    id: str
                    def __init__(self, id: _Optional[str] = ...) -> None: ...
                class LoadBalancerBackendAddressPools(_message.Message):
                    __slots__ = ("id",)
                    ID_FIELD_NUMBER: _ClassVar[int]
                    id: str
                    def __init__(self, id: _Optional[str] = ...) -> None: ...
                SUBNET_FIELD_NUMBER: _ClassVar[int]
                PRIVATEIPALLOCATIONMETHOD_FIELD_NUMBER: _ClassVar[int]
                LOADBALANCERBACKENDADDRESSPOOLS_FIELD_NUMBER: _ClassVar[int]
                subnet: DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties.Subnet
                privateIPAllocationMethod: str
                loadBalancerBackendAddressPools: _containers.RepeatedCompositeFieldContainer[DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools]
                def __init__(self, subnet: _Optional[_Union[DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties.Subnet, _Mapping]] = ..., privateIPAllocationMethod: _Optional[str] = ..., loadBalancerBackendAddressPools: _Optional[_Iterable[_Union[DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties.LoadBalancerBackendAddressPools, _Mapping]]] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            name: str
            properties: DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties
            def __init__(self, name: _Optional[str] = ..., properties: _Optional[_Union[DissociateVMPublicIPRequest.Properties.IpConfigurations.Properties, _Mapping]] = ...) -> None: ...
        IPCONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
        ipConfigurations: _containers.RepeatedCompositeFieldContainer[DissociateVMPublicIPRequest.Properties.IpConfigurations]
        def __init__(self, ipConfigurations: _Optional[_Iterable[_Union[DissociateVMPublicIPRequest.Properties.IpConfigurations, _Mapping]]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    location: str
    properties: DissociateVMPublicIPRequest.Properties
    def __init__(self, location: _Optional[str] = ..., properties: _Optional[_Union[DissociateVMPublicIPRequest.Properties, _Mapping]] = ...) -> None: ...

class DissociateVMPublicIPResponse(_message.Message):
    __slots__ = ("name", "id", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState",)
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    properties: DissociateVMPublicIPResponse.Properties
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., properties: _Optional[_Union[DissociateVMPublicIPResponse.Properties, _Mapping]] = ...) -> None: ...

class GetVirtualNetworkInfoResponse(_message.Message):
    __slots__ = ("id", "name", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState", "subnets")
        class Subnets(_message.Message):
            __slots__ = ("id", "name", "properties")
            class Properties(_message.Message):
                __slots__ = ("provisioningState", "addressPrefix")
                PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
                ADDRESSPREFIX_FIELD_NUMBER: _ClassVar[int]
                provisioningState: str
                addressPrefix: str
                def __init__(self, provisioningState: _Optional[str] = ..., addressPrefix: _Optional[str] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            properties: GetVirtualNetworkInfoResponse.Properties.Subnets.Properties
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetVirtualNetworkInfoResponse.Properties.Subnets.Properties, _Mapping]] = ...) -> None: ...
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        SUBNETS_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        subnets: _containers.RepeatedCompositeFieldContainer[GetVirtualNetworkInfoResponse.Properties.Subnets]
        def __init__(self, provisioningState: _Optional[str] = ..., subnets: _Optional[_Iterable[_Union[GetVirtualNetworkInfoResponse.Properties.Subnets, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    properties: GetVirtualNetworkInfoResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetVirtualNetworkInfoResponse.Properties, _Mapping]] = ...) -> None: ...

class GetLoadBalancerInfoResponse(_message.Message):
    __slots__ = ("id", "name", "properties")
    class Properties(_message.Message):
        __slots__ = ("provisioningState", "frontendIPConfigurations")
        class FrontendIPConfigurations(_message.Message):
            __slots__ = ("id", "name", "properties")
            class Properties(_message.Message):
                __slots__ = ("provisioningState", "privateIPAddress")
                PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
                PRIVATEIPADDRESS_FIELD_NUMBER: _ClassVar[int]
                provisioningState: str
                privateIPAddress: str
                def __init__(self, provisioningState: _Optional[str] = ..., privateIPAddress: _Optional[str] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            properties: GetLoadBalancerInfoResponse.Properties.FrontendIPConfigurations.Properties
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetLoadBalancerInfoResponse.Properties.FrontendIPConfigurations.Properties, _Mapping]] = ...) -> None: ...
        PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
        FRONTENDIPCONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
        provisioningState: str
        frontendIPConfigurations: _containers.RepeatedCompositeFieldContainer[GetLoadBalancerInfoResponse.Properties.FrontendIPConfigurations]
        def __init__(self, provisioningState: _Optional[str] = ..., frontendIPConfigurations: _Optional[_Iterable[_Union[GetLoadBalancerInfoResponse.Properties.FrontendIPConfigurations, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    properties: GetLoadBalancerInfoResponse.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Union[GetLoadBalancerInfoResponse.Properties, _Mapping]] = ...) -> None: ...

class ListSASTokenResponse(_message.Message):
    __slots__ = ("accountSasToken",)
    ACCOUNTSASTOKEN_FIELD_NUMBER: _ClassVar[int]
    accountSasToken: str
    def __init__(self, accountSasToken: _Optional[str] = ...) -> None: ...

class VMEntitiesResponse(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("vmId", "storageProfile", "networkProfile")
        class StorageProfile(_message.Message):
            __slots__ = ("osDisk", "dataDisks")
            class OsDisk(_message.Message):
                __slots__ = ("osType", "name", "createOption", "diskSizeGB", "vhd")
                class Vhd(_message.Message):
                    __slots__ = ("uri",)
                    URI_FIELD_NUMBER: _ClassVar[int]
                    uri: str
                    def __init__(self, uri: _Optional[str] = ...) -> None: ...
                OSTYPE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                CREATEOPTION_FIELD_NUMBER: _ClassVar[int]
                DISKSIZEGB_FIELD_NUMBER: _ClassVar[int]
                VHD_FIELD_NUMBER: _ClassVar[int]
                osType: str
                name: str
                createOption: str
                diskSizeGB: int
                vhd: VMEntitiesResponse.Properties.StorageProfile.OsDisk.Vhd
                def __init__(self, osType: _Optional[str] = ..., name: _Optional[str] = ..., createOption: _Optional[str] = ..., diskSizeGB: _Optional[int] = ..., vhd: _Optional[_Union[VMEntitiesResponse.Properties.StorageProfile.OsDisk.Vhd, _Mapping]] = ...) -> None: ...
            class DataDisk(_message.Message):
                __slots__ = ("diskSizeGB", "vhd")
                class Vhd(_message.Message):
                    __slots__ = ("uri",)
                    URI_FIELD_NUMBER: _ClassVar[int]
                    uri: str
                    def __init__(self, uri: _Optional[str] = ...) -> None: ...
                DISKSIZEGB_FIELD_NUMBER: _ClassVar[int]
                VHD_FIELD_NUMBER: _ClassVar[int]
                diskSizeGB: int
                vhd: VMEntitiesResponse.Properties.StorageProfile.DataDisk.Vhd
                def __init__(self, diskSizeGB: _Optional[int] = ..., vhd: _Optional[_Union[VMEntitiesResponse.Properties.StorageProfile.DataDisk.Vhd, _Mapping]] = ...) -> None: ...
            OSDISK_FIELD_NUMBER: _ClassVar[int]
            DATADISKS_FIELD_NUMBER: _ClassVar[int]
            osDisk: VMEntitiesResponse.Properties.StorageProfile.OsDisk
            dataDisks: _containers.RepeatedCompositeFieldContainer[VMEntitiesResponse.Properties.StorageProfile.DataDisk]
            def __init__(self, osDisk: _Optional[_Union[VMEntitiesResponse.Properties.StorageProfile.OsDisk, _Mapping]] = ..., dataDisks: _Optional[_Iterable[_Union[VMEntitiesResponse.Properties.StorageProfile.DataDisk, _Mapping]]] = ...) -> None: ...
        class NetworkProfile(_message.Message):
            __slots__ = ("networkInterfaces",)
            class NetworkInterfaces(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: str
                def __init__(self, id: _Optional[str] = ...) -> None: ...
            NETWORKINTERFACES_FIELD_NUMBER: _ClassVar[int]
            networkInterfaces: _containers.RepeatedCompositeFieldContainer[VMEntitiesResponse.Properties.NetworkProfile.NetworkInterfaces]
            def __init__(self, networkInterfaces: _Optional[_Iterable[_Union[VMEntitiesResponse.Properties.NetworkProfile.NetworkInterfaces, _Mapping]]] = ...) -> None: ...
        VMID_FIELD_NUMBER: _ClassVar[int]
        STORAGEPROFILE_FIELD_NUMBER: _ClassVar[int]
        NETWORKPROFILE_FIELD_NUMBER: _ClassVar[int]
        vmId: str
        storageProfile: VMEntitiesResponse.Properties.StorageProfile
        networkProfile: VMEntitiesResponse.Properties.NetworkProfile
        def __init__(self, vmId: _Optional[str] = ..., storageProfile: _Optional[_Union[VMEntitiesResponse.Properties.StorageProfile, _Mapping]] = ..., networkProfile: _Optional[_Union[VMEntitiesResponse.Properties.NetworkProfile, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: VMEntitiesResponse.Properties
    def __init__(self, properties: _Optional[_Union[VMEntitiesResponse.Properties, _Mapping]] = ...) -> None: ...

class DiskOrSnapshotInfo(_message.Message):
    __slots__ = ("managed_by", "type", "location", "id", "name", "sku", "properties", "tags", "zones")
    class Sku(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("os_type", "creation_data", "disk_size_GB", "disk_state", "encryption_settings", "time_created", "provisioning_state", "hyper_v_generation", "disk_size_bytes", "encryption_settings_collection", "incremental", "disk_access_id", "network_access_policy", "public_network_access", "security_profile")
        class CreationData(_message.Message):
            __slots__ = ("create_option", "image_disk_reference", "source_resource_id", "source_uri", "storage_account_id", "upload_size_bytes")
            class ImageDiskReference(_message.Message):
                __slots__ = ("id", "lun")
                ID_FIELD_NUMBER: _ClassVar[int]
                LUN_FIELD_NUMBER: _ClassVar[int]
                id: str
                lun: int
                def __init__(self, id: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...
            CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
            IMAGE_DISK_REFERENCE_FIELD_NUMBER: _ClassVar[int]
            SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
            SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
            UPLOAD_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            create_option: str
            image_disk_reference: DiskOrSnapshotInfo.Properties.CreationData.ImageDiskReference
            source_resource_id: str
            source_uri: str
            storage_account_id: str
            upload_size_bytes: int
            def __init__(self, create_option: _Optional[str] = ..., image_disk_reference: _Optional[_Union[DiskOrSnapshotInfo.Properties.CreationData.ImageDiskReference, _Mapping]] = ..., source_resource_id: _Optional[str] = ..., source_uri: _Optional[str] = ..., storage_account_id: _Optional[str] = ..., upload_size_bytes: _Optional[int] = ...) -> None: ...
        class EncryptionSettingsCollection(_message.Message):
            __slots__ = ("enabled", "encryption_settings", "encryption_settings_version")
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_SETTINGS_VERSION_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            encryption_settings: _containers.RepeatedCompositeFieldContainer[EncryptionSettings]
            encryption_settings_version: str
            def __init__(self, enabled: bool = ..., encryption_settings: _Optional[_Iterable[_Union[EncryptionSettings, _Mapping]]] = ..., encryption_settings_version: _Optional[str] = ...) -> None: ...
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATA_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        DISK_STATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        HYPER_V_GENERATION_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
        DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
        os_type: str
        creation_data: DiskOrSnapshotInfo.Properties.CreationData
        disk_size_GB: int
        disk_state: str
        encryption_settings: EncryptionSettings
        time_created: str
        provisioning_state: str
        hyper_v_generation: str
        disk_size_bytes: int
        encryption_settings_collection: DiskOrSnapshotInfo.Properties.EncryptionSettingsCollection
        incremental: bool
        disk_access_id: str
        network_access_policy: str
        public_network_access: str
        security_profile: DiskSecurityProfile
        def __init__(self, os_type: _Optional[str] = ..., creation_data: _Optional[_Union[DiskOrSnapshotInfo.Properties.CreationData, _Mapping]] = ..., disk_size_GB: _Optional[int] = ..., disk_state: _Optional[str] = ..., encryption_settings: _Optional[_Union[EncryptionSettings, _Mapping]] = ..., time_created: _Optional[str] = ..., provisioning_state: _Optional[str] = ..., hyper_v_generation: _Optional[str] = ..., disk_size_bytes: _Optional[int] = ..., encryption_settings_collection: _Optional[_Union[DiskOrSnapshotInfo.Properties.EncryptionSettingsCollection, _Mapping]] = ..., incremental: bool = ..., disk_access_id: _Optional[str] = ..., network_access_policy: _Optional[str] = ..., public_network_access: _Optional[str] = ..., security_profile: _Optional[_Union[DiskSecurityProfile, _Mapping]] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MANAGED_BY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    managed_by: str
    type: str
    location: str
    id: str
    name: str
    sku: DiskOrSnapshotInfo.Sku
    properties: DiskOrSnapshotInfo.Properties
    tags: _containers.ScalarMap[str, str]
    zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, managed_by: _Optional[str] = ..., type: _Optional[str] = ..., location: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., sku: _Optional[_Union[DiskOrSnapshotInfo.Sku, _Mapping]] = ..., properties: _Optional[_Union[DiskOrSnapshotInfo.Properties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("location", "tags", "sku", "properties")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Sku(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("creation_data", "disk_size_GB", "incremental", "disk_access_id", "network_access_policy")
        class CreationData(_message.Message):
            __slots__ = ("create_option", "source_resource_id")
            CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
            SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
            create_option: str
            source_resource_id: str
            def __init__(self, create_option: _Optional[str] = ..., source_resource_id: _Optional[str] = ...) -> None: ...
        CREATION_DATA_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
        DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
        creation_data: CreateSnapshotRequest.Properties.CreationData
        disk_size_GB: int
        incremental: bool
        disk_access_id: str
        network_access_policy: str
        def __init__(self, creation_data: _Optional[_Union[CreateSnapshotRequest.Properties.CreationData, _Mapping]] = ..., disk_size_GB: _Optional[int] = ..., incremental: bool = ..., disk_access_id: _Optional[str] = ..., network_access_policy: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    location: str
    tags: _containers.ScalarMap[str, str]
    sku: CreateSnapshotRequest.Sku
    properties: CreateSnapshotRequest.Properties
    def __init__(self, location: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., sku: _Optional[_Union[CreateSnapshotRequest.Sku, _Mapping]] = ..., properties: _Optional[_Union[CreateSnapshotRequest.Properties, _Mapping]] = ...) -> None: ...

class UpdateSnapshotRequest(_message.Message):
    __slots__ = ("sku", "tags", "location", "properties")
    class Sku(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("creation_data", "disk_access_id", "network_access_policy")
        class CreationData(_message.Message):
            __slots__ = ("create_option", "source_resource_id")
            CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
            SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
            create_option: str
            source_resource_id: str
            def __init__(self, create_option: _Optional[str] = ..., source_resource_id: _Optional[str] = ...) -> None: ...
        CREATION_DATA_FIELD_NUMBER: _ClassVar[int]
        DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
        creation_data: UpdateSnapshotRequest.Properties.CreationData
        disk_access_id: str
        network_access_policy: str
        def __init__(self, creation_data: _Optional[_Union[UpdateSnapshotRequest.Properties.CreationData, _Mapping]] = ..., disk_access_id: _Optional[str] = ..., network_access_policy: _Optional[str] = ...) -> None: ...
    SKU_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    sku: UpdateSnapshotRequest.Sku
    tags: _containers.ScalarMap[str, str]
    location: str
    properties: UpdateSnapshotRequest.Properties
    def __init__(self, sku: _Optional[_Union[UpdateSnapshotRequest.Sku, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[UpdateSnapshotRequest.Properties, _Mapping]] = ...) -> None: ...

class GetSASUrlRequest(_message.Message):
    __slots__ = ("access", "duration_in_seconds")
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    access: str
    duration_in_seconds: int
    def __init__(self, access: _Optional[str] = ..., duration_in_seconds: _Optional[int] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("start_time", "end_time", "status", "properties", "name")
    class Properties(_message.Message):
        __slots__ = ("output",)
        class Output(_message.Message):
            __slots__ = ("access_SAS",)
            ACCESS_SAS_FIELD_NUMBER: _ClassVar[int]
            access_SAS: str
            def __init__(self, access_SAS: _Optional[str] = ...) -> None: ...
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        output: StatusResponse.Properties.Output
        def __init__(self, output: _Optional[_Union[StatusResponse.Properties.Output, _Mapping]] = ...) -> None: ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    end_time: str
    status: str
    properties: StatusResponse.Properties
    name: str
    def __init__(self, start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., status: _Optional[str] = ..., properties: _Optional[_Union[StatusResponse.Properties, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class BlobProperties(_message.Message):
    __slots__ = ("blob_name", "snapshot_id", "blob_size_bytes", "blob_logical_size_bytes", "blob_sequence_number", "blob_etag", "lease_state", "lease_status", "blob_url", "storage_account", "storage_access_key", "storage_container", "azure_stack_region", "azure_stack_hub_domain_name")
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BLOB_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BLOB_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOB_ETAG_FIELD_NUMBER: _ClassVar[int]
    LEASE_STATE_FIELD_NUMBER: _ClassVar[int]
    LEASE_STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOB_URL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_REGION_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_HUB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    blob_name: str
    snapshot_id: str
    blob_size_bytes: int
    blob_logical_size_bytes: int
    blob_sequence_number: int
    blob_etag: str
    lease_state: str
    lease_status: str
    blob_url: str
    storage_account: str
    storage_access_key: str
    storage_container: str
    azure_stack_region: str
    azure_stack_hub_domain_name: str
    def __init__(self, blob_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., blob_size_bytes: _Optional[int] = ..., blob_logical_size_bytes: _Optional[int] = ..., blob_sequence_number: _Optional[int] = ..., blob_etag: _Optional[str] = ..., lease_state: _Optional[str] = ..., lease_status: _Optional[str] = ..., blob_url: _Optional[str] = ..., storage_account: _Optional[str] = ..., storage_access_key: _Optional[str] = ..., storage_container: _Optional[str] = ..., azure_stack_region: _Optional[str] = ..., azure_stack_hub_domain_name: _Optional[str] = ...) -> None: ...

class NetworkInterfaceProperties(_message.Message):
    __slots__ = ("ip_configurations", "enable_accelerated_networking", "network_security_group", "primary", "mac_address")
    class IPConfigurations(_message.Message):
        __slots__ = ("name", "id", "properties")
        class Properties(_message.Message):
            __slots__ = ("public_ip", "privateIPAddress", "provisioning_state", "subnet", "primary")
            class PublicIPAddress(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: str
                def __init__(self, id: _Optional[str] = ...) -> None: ...
            class Subnet(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: str
                def __init__(self, id: _Optional[str] = ...) -> None: ...
            PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
            PRIVATEIPADDRESS_FIELD_NUMBER: _ClassVar[int]
            PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
            SUBNET_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_FIELD_NUMBER: _ClassVar[int]
            public_ip: NetworkInterfaceProperties.IPConfigurations.Properties.PublicIPAddress
            privateIPAddress: str
            provisioning_state: str
            subnet: NetworkInterfaceProperties.IPConfigurations.Properties.Subnet
            primary: bool
            def __init__(self, public_ip: _Optional[_Union[NetworkInterfaceProperties.IPConfigurations.Properties.PublicIPAddress, _Mapping]] = ..., privateIPAddress: _Optional[str] = ..., provisioning_state: _Optional[str] = ..., subnet: _Optional[_Union[NetworkInterfaceProperties.IPConfigurations.Properties.Subnet, _Mapping]] = ..., primary: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: str
        properties: NetworkInterfaceProperties.IPConfigurations.Properties
        def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., properties: _Optional[_Union[NetworkInterfaceProperties.IPConfigurations.Properties, _Mapping]] = ...) -> None: ...
    class NetworkSecurityGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    IP_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ACCELERATED_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ip_configurations: _containers.RepeatedCompositeFieldContainer[NetworkInterfaceProperties.IPConfigurations]
    enable_accelerated_networking: bool
    network_security_group: NetworkInterfaceProperties.NetworkSecurityGroup
    primary: bool
    mac_address: str
    def __init__(self, ip_configurations: _Optional[_Iterable[_Union[NetworkInterfaceProperties.IPConfigurations, _Mapping]]] = ..., enable_accelerated_networking: bool = ..., network_security_group: _Optional[_Union[NetworkInterfaceProperties.NetworkSecurityGroup, _Mapping]] = ..., primary: bool = ..., mac_address: _Optional[str] = ...) -> None: ...

class CreateNetworkInterfaceRequest(_message.Message):
    __slots__ = ("etag", "id", "location", "properties", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    etag: str
    id: str
    location: str
    properties: NetworkInterfaceProperties
    tags: _containers.ScalarMap[str, str]
    def __init__(self, etag: _Optional[str] = ..., id: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[NetworkInterfaceProperties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NetworkInterfaceResponse(_message.Message):
    __slots__ = ("name", "id", "location", "properties", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    location: str
    properties: NetworkInterfaceProperties
    tags: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[NetworkInterfaceProperties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NetworkProfile(_message.Message):
    __slots__ = ("network_interfaces",)
    class NetworkInterfaces(_message.Message):
        __slots__ = ("id", "properties")
        class Properties(_message.Message):
            __slots__ = ("primary",)
            PRIMARY_FIELD_NUMBER: _ClassVar[int]
            primary: bool
            def __init__(self, primary: bool = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        properties: NetworkProfile.NetworkInterfaces.Properties
        def __init__(self, id: _Optional[str] = ..., properties: _Optional[_Union[NetworkProfile.NetworkInterfaces.Properties, _Mapping]] = ...) -> None: ...
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkProfile.NetworkInterfaces]
    def __init__(self, network_interfaces: _Optional[_Iterable[_Union[NetworkProfile.NetworkInterfaces, _Mapping]]] = ...) -> None: ...

class CreateVMRequest(_message.Message):
    __slots__ = ("location", "properties", "tags", "name", "plan", "zones")
    class ManagedDisk(_message.Message):
        __slots__ = ("storage_account_type", "id")
        STORAGE_ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        storage_account_type: str
        id: str
        def __init__(self, storage_account_type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class VHD(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    class DiskProfile(_message.Message):
        __slots__ = ("os_type", "caching", "create_option", "name", "disk_size_GB", "lun", "vhd", "managed_disk", "encryption_settings", "to_be_detached", "managed_by")
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        CACHING_FIELD_NUMBER: _ClassVar[int]
        CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        LUN_FIELD_NUMBER: _ClassVar[int]
        VHD_FIELD_NUMBER: _ClassVar[int]
        MANAGED_DISK_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        TO_BE_DETACHED_FIELD_NUMBER: _ClassVar[int]
        MANAGED_BY_FIELD_NUMBER: _ClassVar[int]
        os_type: str
        caching: str
        create_option: str
        name: str
        disk_size_GB: float
        lun: float
        vhd: CreateVMRequest.VHD
        managed_disk: CreateVMRequest.ManagedDisk
        encryption_settings: EncryptionSettings
        to_be_detached: bool
        managed_by: str
        def __init__(self, os_type: _Optional[str] = ..., caching: _Optional[str] = ..., create_option: _Optional[str] = ..., name: _Optional[str] = ..., disk_size_GB: _Optional[float] = ..., lun: _Optional[float] = ..., vhd: _Optional[_Union[CreateVMRequest.VHD, _Mapping]] = ..., managed_disk: _Optional[_Union[CreateVMRequest.ManagedDisk, _Mapping]] = ..., encryption_settings: _Optional[_Union[EncryptionSettings, _Mapping]] = ..., to_be_detached: bool = ..., managed_by: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("hardware_profile", "storage_profile", "os_profile", "network_profile", "license_type", "availability_set", "security_profile")
        class HardwareProfile(_message.Message):
            __slots__ = ("vm_size",)
            VM_SIZE_FIELD_NUMBER: _ClassVar[int]
            vm_size: str
            def __init__(self, vm_size: _Optional[str] = ...) -> None: ...
        class StorageProfile(_message.Message):
            __slots__ = ("image_reference", "os_disk", "data_disks")
            class ImageReference(_message.Message):
                __slots__ = ("sku", "publisher", "version", "offer")
                SKU_FIELD_NUMBER: _ClassVar[int]
                PUBLISHER_FIELD_NUMBER: _ClassVar[int]
                VERSION_FIELD_NUMBER: _ClassVar[int]
                OFFER_FIELD_NUMBER: _ClassVar[int]
                sku: str
                publisher: str
                version: str
                offer: str
                def __init__(self, sku: _Optional[str] = ..., publisher: _Optional[str] = ..., version: _Optional[str] = ..., offer: _Optional[str] = ...) -> None: ...
            IMAGE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
            OS_DISK_FIELD_NUMBER: _ClassVar[int]
            DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
            image_reference: CreateVMRequest.Properties.StorageProfile.ImageReference
            os_disk: CreateVMRequest.DiskProfile
            data_disks: _containers.RepeatedCompositeFieldContainer[CreateVMRequest.DiskProfile]
            def __init__(self, image_reference: _Optional[_Union[CreateVMRequest.Properties.StorageProfile.ImageReference, _Mapping]] = ..., os_disk: _Optional[_Union[CreateVMRequest.DiskProfile, _Mapping]] = ..., data_disks: _Optional[_Iterable[_Union[CreateVMRequest.DiskProfile, _Mapping]]] = ...) -> None: ...
        class OSProfile(_message.Message):
            __slots__ = ("admin_username", "admin_password", "computer_name")
            ADMIN_USERNAME_FIELD_NUMBER: _ClassVar[int]
            ADMIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
            admin_username: str
            admin_password: str
            computer_name: str
            def __init__(self, admin_username: _Optional[str] = ..., admin_password: _Optional[str] = ..., computer_name: _Optional[str] = ...) -> None: ...
        class SubResource(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        HARDWARE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        OS_PROFILE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
        LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_SET_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
        hardware_profile: CreateVMRequest.Properties.HardwareProfile
        storage_profile: CreateVMRequest.Properties.StorageProfile
        os_profile: CreateVMRequest.Properties.OSProfile
        network_profile: NetworkProfile
        license_type: str
        availability_set: CreateVMRequest.Properties.SubResource
        security_profile: SecurityProfile
        def __init__(self, hardware_profile: _Optional[_Union[CreateVMRequest.Properties.HardwareProfile, _Mapping]] = ..., storage_profile: _Optional[_Union[CreateVMRequest.Properties.StorageProfile, _Mapping]] = ..., os_profile: _Optional[_Union[CreateVMRequest.Properties.OSProfile, _Mapping]] = ..., network_profile: _Optional[_Union[NetworkProfile, _Mapping]] = ..., license_type: _Optional[str] = ..., availability_set: _Optional[_Union[CreateVMRequest.Properties.SubResource, _Mapping]] = ..., security_profile: _Optional[_Union[SecurityProfile, _Mapping]] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    location: str
    properties: CreateVMRequest.Properties
    tags: _containers.ScalarMap[str, str]
    name: str
    plan: Plan
    zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, location: _Optional[str] = ..., properties: _Optional[_Union[CreateVMRequest.Properties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., name: _Optional[str] = ..., plan: _Optional[_Union[Plan, _Mapping]] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...

class EncryptionSettings(_message.Message):
    __slots__ = ("enabled", "disk_encryption_key", "key_encryption_key")
    class DiskEncryptionKey(_message.Message):
        __slots__ = ("source_vault", "secret_url")
        class SourceVault(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        SOURCE_VAULT_FIELD_NUMBER: _ClassVar[int]
        SECRET_URL_FIELD_NUMBER: _ClassVar[int]
        source_vault: EncryptionSettings.DiskEncryptionKey.SourceVault
        secret_url: str
        def __init__(self, source_vault: _Optional[_Union[EncryptionSettings.DiskEncryptionKey.SourceVault, _Mapping]] = ..., secret_url: _Optional[str] = ...) -> None: ...
    class KeyEncryptionKey(_message.Message):
        __slots__ = ("source_vault", "key_url")
        class SourceVault(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        SOURCE_VAULT_FIELD_NUMBER: _ClassVar[int]
        KEY_URL_FIELD_NUMBER: _ClassVar[int]
        source_vault: EncryptionSettings.KeyEncryptionKey.SourceVault
        key_url: str
        def __init__(self, source_vault: _Optional[_Union[EncryptionSettings.KeyEncryptionKey.SourceVault, _Mapping]] = ..., key_url: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    disk_encryption_key: EncryptionSettings.DiskEncryptionKey
    key_encryption_key: EncryptionSettings.KeyEncryptionKey
    def __init__(self, enabled: bool = ..., disk_encryption_key: _Optional[_Union[EncryptionSettings.DiskEncryptionKey, _Mapping]] = ..., key_encryption_key: _Optional[_Union[EncryptionSettings.KeyEncryptionKey, _Mapping]] = ...) -> None: ...

class CreateStorageContainerRequest(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("metadata", "public_access")
        class PublicAccess(_message.Message):
            __slots__ = ("access_level",)
            ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
            access_level: str
            def __init__(self, access_level: _Optional[str] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_ACCESS_FIELD_NUMBER: _ClassVar[int]
        metadata: str
        public_access: CreateStorageContainerRequest.Properties.PublicAccess
        def __init__(self, metadata: _Optional[str] = ..., public_access: _Optional[_Union[CreateStorageContainerRequest.Properties.PublicAccess, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: CreateStorageContainerRequest.Properties
    def __init__(self, properties: _Optional[_Union[CreateStorageContainerRequest.Properties, _Mapping]] = ...) -> None: ...

class CreateStorageContainerResponse(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Plan(_message.Message):
    __slots__ = ("name", "publisher", "product", "promotion_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    publisher: str
    product: str
    promotion_code: str
    def __init__(self, name: _Optional[str] = ..., publisher: _Optional[str] = ..., product: _Optional[str] = ..., promotion_code: _Optional[str] = ...) -> None: ...

class RunCommandRequest(_message.Message):
    __slots__ = ("commandId", "parameters", "script")
    class RunCommandInputParameter(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMANDID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    commandId: str
    parameters: _containers.RepeatedCompositeFieldContainer[RunCommandRequest.RunCommandInputParameter]
    script: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, commandId: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[RunCommandRequest.RunCommandInputParameter, _Mapping]]] = ..., script: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateCommandRequest(_message.Message):
    __slots__ = ("location", "properties")
    class Properties(_message.Message):
        __slots__ = ("source", "parameters", "async_execution", "timeout")
        class ScriptSource(_message.Message):
            __slots__ = ("script",)
            SCRIPT_FIELD_NUMBER: _ClassVar[int]
            script: str
            def __init__(self, script: _Optional[str] = ...) -> None: ...
        class ScriptInputParameter(_message.Message):
            __slots__ = ("name", "value")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        ASYNC_EXECUTION_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        source: CreateCommandRequest.Properties.ScriptSource
        parameters: _containers.RepeatedCompositeFieldContainer[CreateCommandRequest.Properties.ScriptInputParameter]
        async_execution: bool
        timeout: int
        def __init__(self, source: _Optional[_Union[CreateCommandRequest.Properties.ScriptSource, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[CreateCommandRequest.Properties.ScriptInputParameter, _Mapping]]] = ..., async_execution: bool = ..., timeout: _Optional[int] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    location: str
    properties: CreateCommandRequest.Properties
    def __init__(self, location: _Optional[str] = ..., properties: _Optional[_Union[CreateCommandRequest.Properties, _Mapping]] = ...) -> None: ...

class ListServiceSASRequest(_message.Message):
    __slots__ = ("canonicalized_resource_path", "signed_expiry", "signed_ip", "signed_permission", "signed_protocol", "signed_resource")
    CANONICALIZED_RESOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIGNED_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    SIGNED_IP_FIELD_NUMBER: _ClassVar[int]
    SIGNED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SIGNED_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SIGNED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    canonicalized_resource_path: str
    signed_expiry: str
    signed_ip: str
    signed_permission: str
    signed_protocol: str
    signed_resource: str
    def __init__(self, canonicalized_resource_path: _Optional[str] = ..., signed_expiry: _Optional[str] = ..., signed_ip: _Optional[str] = ..., signed_permission: _Optional[str] = ..., signed_protocol: _Optional[str] = ..., signed_resource: _Optional[str] = ...) -> None: ...

class ListServiceSASResponse(_message.Message):
    __slots__ = ("service_sas_token",)
    SERVICE_SAS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_sas_token: str
    def __init__(self, service_sas_token: _Optional[str] = ...) -> None: ...

class AvailabilitySet(_message.Message):
    __slots__ = ("id", "name", "location", "properties")
    class Properties(_message.Message):
        __slots__ = ("platform_fault_domain_count", "platform_update_domain_count")
        PLATFORM_FAULT_DOMAIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_UPDATE_DOMAIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        platform_fault_domain_count: int
        platform_update_domain_count: int
        def __init__(self, platform_fault_domain_count: _Optional[int] = ..., platform_update_domain_count: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    properties: AvailabilitySet.Properties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[AvailabilitySet.Properties, _Mapping]] = ...) -> None: ...

class AvailabilitySetsResponse(_message.Message):
    __slots__ = ("value", "next_url")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[AvailabilitySet]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[AvailabilitySet, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...

class PrivateLinkServiceConnections(_message.Message):
    __slots__ = ("name", "properties")
    class Properties(_message.Message):
        __slots__ = ("private_link_service_id", "group_ids", "provisioning_state", "connection_status")
        class PrivateLinkServiceConnectionState(_message.Message):
            __slots__ = ("status",)
            STATUS_FIELD_NUMBER: _ClassVar[int]
            status: str
            def __init__(self, status: _Optional[str] = ...) -> None: ...
        PRIVATE_LINK_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        private_link_service_id: str
        group_ids: _containers.RepeatedScalarFieldContainer[str]
        provisioning_state: str
        connection_status: PrivateLinkServiceConnections.Properties.PrivateLinkServiceConnectionState
        def __init__(self, private_link_service_id: _Optional[str] = ..., group_ids: _Optional[_Iterable[str]] = ..., provisioning_state: _Optional[str] = ..., connection_status: _Optional[_Union[PrivateLinkServiceConnections.Properties.PrivateLinkServiceConnectionState, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    properties: PrivateLinkServiceConnections.Properties
    def __init__(self, name: _Optional[str] = ..., properties: _Optional[_Union[PrivateLinkServiceConnections.Properties, _Mapping]] = ...) -> None: ...

class PrivateEndpointConfig(_message.Message):
    __slots__ = ("location", "id", "tags", "properties")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("provisioning_state", "private_link_service_connections", "subnet", "custom_dns_configs")
        class Subnet(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class CustomDnsConfigs(_message.Message):
            __slots__ = ("fqdn", "ip_addresses")
            FQDN_FIELD_NUMBER: _ClassVar[int]
            IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            fqdn: str
            ip_addresses: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, fqdn: _Optional[str] = ..., ip_addresses: _Optional[_Iterable[str]] = ...) -> None: ...
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_LINK_SERVICE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_DNS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: str
        private_link_service_connections: _containers.RepeatedCompositeFieldContainer[PrivateLinkServiceConnections]
        subnet: PrivateEndpointConfig.Properties.Subnet
        custom_dns_configs: _containers.RepeatedCompositeFieldContainer[PrivateEndpointConfig.Properties.CustomDnsConfigs]
        def __init__(self, provisioning_state: _Optional[str] = ..., private_link_service_connections: _Optional[_Iterable[_Union[PrivateLinkServiceConnections, _Mapping]]] = ..., subnet: _Optional[_Union[PrivateEndpointConfig.Properties.Subnet, _Mapping]] = ..., custom_dns_configs: _Optional[_Iterable[_Union[PrivateEndpointConfig.Properties.CustomDnsConfigs, _Mapping]]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    location: str
    id: str
    tags: _containers.ScalarMap[str, str]
    properties: PrivateEndpointConfig.Properties
    def __init__(self, location: _Optional[str] = ..., id: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., properties: _Optional[_Union[PrivateEndpointConfig.Properties, _Mapping]] = ...) -> None: ...

class PrivateEndpointConnections(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("provisioning_state", "private_endpoint", "connection_status")
        class PrivateEndpoint(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PrivateLinkServiceConnectionState(_message.Message):
            __slots__ = ("status",)
            STATUS_FIELD_NUMBER: _ClassVar[int]
            status: str
            def __init__(self, status: _Optional[str] = ...) -> None: ...
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: str
        private_endpoint: PrivateEndpointConnections.Properties.PrivateEndpoint
        connection_status: PrivateEndpointConnections.Properties.PrivateLinkServiceConnectionState
        def __init__(self, provisioning_state: _Optional[str] = ..., private_endpoint: _Optional[_Union[PrivateEndpointConnections.Properties.PrivateEndpoint, _Mapping]] = ..., connection_status: _Optional[_Union[PrivateEndpointConnections.Properties.PrivateLinkServiceConnectionState, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: PrivateEndpointConnections.Properties
    def __init__(self, properties: _Optional[_Union[PrivateEndpointConnections.Properties, _Mapping]] = ...) -> None: ...

class DiskAccessConfig(_message.Message):
    __slots__ = ("location", "id", "tags", "properties")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Properties(_message.Message):
        __slots__ = ("provisioning_state", "private_endpoint_connections")
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: str
        private_endpoint_connections: _containers.RepeatedCompositeFieldContainer[PrivateEndpointConnections]
        def __init__(self, provisioning_state: _Optional[str] = ..., private_endpoint_connections: _Optional[_Iterable[_Union[PrivateEndpointConnections, _Mapping]]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    location: str
    id: str
    tags: _containers.ScalarMap[str, str]
    properties: DiskAccessConfig.Properties
    def __init__(self, location: _Optional[str] = ..., id: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., properties: _Optional[_Union[DiskAccessConfig.Properties, _Mapping]] = ...) -> None: ...

class CreateDnsRecordConfig(_message.Message):
    __slots__ = ("id", "etag", "name", "type", "properties")
    class Properties(_message.Message):
        __slots__ = ("ttl", "fqdn", "is_auto_registered", "a_records")
        class ARecords(_message.Message):
            __slots__ = ("ip_addresses",)
            IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            ip_addresses: str
            def __init__(self, ip_addresses: _Optional[str] = ...) -> None: ...
        TTL_FIELD_NUMBER: _ClassVar[int]
        FQDN_FIELD_NUMBER: _ClassVar[int]
        IS_AUTO_REGISTERED_FIELD_NUMBER: _ClassVar[int]
        A_RECORDS_FIELD_NUMBER: _ClassVar[int]
        ttl: int
        fqdn: str
        is_auto_registered: bool
        a_records: _containers.RepeatedCompositeFieldContainer[CreateDnsRecordConfig.Properties.ARecords]
        def __init__(self, ttl: _Optional[int] = ..., fqdn: _Optional[str] = ..., is_auto_registered: bool = ..., a_records: _Optional[_Iterable[_Union[CreateDnsRecordConfig.Properties.ARecords, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    etag: str
    name: str
    type: str
    properties: CreateDnsRecordConfig.Properties
    def __init__(self, id: _Optional[str] = ..., etag: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Union[CreateDnsRecordConfig.Properties, _Mapping]] = ...) -> None: ...

class ListResourceSkusResponse(_message.Message):
    __slots__ = ("value",)
    class SkuInfo(_message.Message):
        __slots__ = ("resource_type", "name", "locations", "location_info")
        class LocationInfo(_message.Message):
            __slots__ = ("location", "zones")
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            ZONES_FIELD_NUMBER: _ClassVar[int]
            location: str
            zones: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, location: _Optional[str] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        name: str
        locations: _containers.RepeatedScalarFieldContainer[str]
        location_info: _containers.RepeatedCompositeFieldContainer[ListResourceSkusResponse.SkuInfo.LocationInfo]
        def __init__(self, resource_type: _Optional[str] = ..., name: _Optional[str] = ..., locations: _Optional[_Iterable[str]] = ..., location_info: _Optional[_Iterable[_Union[ListResourceSkusResponse.SkuInfo.LocationInfo, _Mapping]]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ListResourceSkusResponse.SkuInfo]
    def __init__(self, value: _Optional[_Iterable[_Union[ListResourceSkusResponse.SkuInfo, _Mapping]]] = ...) -> None: ...

class LocationsResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[LocationsResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[LocationsResponse.Value, _Mapping]]] = ...) -> None: ...

class ApplicationSecurityGroupResponse(_message.Message):
    __slots__ = ("value", "next_url")
    class Value(_message.Message):
        __slots__ = ("id", "name", "location", "properties")
        class Properties(_message.Message):
            __slots__ = ("provisioningState",)
            PROVISIONINGSTATE_FIELD_NUMBER: _ClassVar[int]
            provisioningState: str
            def __init__(self, provisioningState: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        location: str
        properties: ApplicationSecurityGroupResponse.Value.Properties
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., properties: _Optional[_Union[ApplicationSecurityGroupResponse.Value.Properties, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_URL_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ApplicationSecurityGroupResponse.Value]
    next_url: str
    def __init__(self, value: _Optional[_Iterable[_Union[ApplicationSecurityGroupResponse.Value, _Mapping]]] = ..., next_url: _Optional[str] = ...) -> None: ...
