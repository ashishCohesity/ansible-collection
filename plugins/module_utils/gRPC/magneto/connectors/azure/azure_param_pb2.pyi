from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskMetadata(_message.Message):
    __slots__ = ("disk_id", "disk_size_bytes", "disk_type", "is_encrypted", "blob_info", "managed_disk_info", "is_bootable", "lun", "caching", "name")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_FIELD_NUMBER: _ClassVar[int]
    MANAGED_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    CACHING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    disk_id: str
    disk_size_bytes: int
    disk_type: str
    is_encrypted: bool
    blob_info: BlobProperties
    managed_disk_info: DiskOrSnapshotInfo
    is_bootable: bool
    lun: int
    caching: str
    name: str
    def __init__(self, disk_id: _Optional[str] = ..., disk_size_bytes: _Optional[int] = ..., disk_type: _Optional[str] = ..., is_encrypted: bool = ..., blob_info: _Optional[_Union[BlobProperties, _Mapping]] = ..., managed_disk_info: _Optional[_Union[DiskOrSnapshotInfo, _Mapping]] = ..., is_bootable: bool = ..., lun: _Optional[int] = ..., caching: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ManagedDiskInfo(_message.Message):
    __slots__ = ("storage_params", "managed_disk_name", "disk_info")
    STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MANAGED_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    storage_params: CommonStorageParams
    managed_disk_name: str
    disk_info: DiskOrSnapshotInfo
    def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., managed_disk_name: _Optional[str] = ..., disk_info: _Optional[_Union[DiskOrSnapshotInfo, _Mapping]] = ...) -> None: ...

class DiskSecurityProfile(_message.Message):
    __slots__ = ("security_type", "secure_set_id")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    security_type: str
    secure_set_id: str
    def __init__(self, security_type: _Optional[str] = ..., secure_set_id: _Optional[str] = ...) -> None: ...

class DiskOrSnapshotInfo(_message.Message):
    __slots__ = ("managing_vm", "type", "location", "id", "name", "sku", "properties", "tags", "zones")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kResourceDisk: _ClassVar[DiskOrSnapshotInfo.Type]
        kResourceSnapshot: _ClassVar[DiskOrSnapshotInfo.Type]
    kResourceDisk: DiskOrSnapshotInfo.Type
    kResourceSnapshot: DiskOrSnapshotInfo.Type
    class Properties(_message.Message):
        __slots__ = ("os_type", "creation_data", "disk_size_bytes", "disk_state", "encryption_settings", "creation_time_secs", "provisioning_state", "hyperv_generation", "encryption_settings_collection", "is_incremental", "disk_access_id", "network_access_policy", "public_network_access", "security_profile")
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
        DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        DISK_STATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        HYPERV_GENERATION_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        IS_INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
        DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
        os_type: str
        creation_data: DiskOrSnapshotInfo.Properties.CreationData
        disk_size_bytes: int
        disk_state: str
        encryption_settings: EncryptionSettings
        creation_time_secs: str
        provisioning_state: str
        hyperv_generation: str
        encryption_settings_collection: DiskOrSnapshotInfo.Properties.EncryptionSettingsCollection
        is_incremental: bool
        disk_access_id: str
        network_access_policy: str
        public_network_access: str
        security_profile: DiskSecurityProfile
        def __init__(self, os_type: _Optional[str] = ..., creation_data: _Optional[_Union[DiskOrSnapshotInfo.Properties.CreationData, _Mapping]] = ..., disk_size_bytes: _Optional[int] = ..., disk_state: _Optional[str] = ..., encryption_settings: _Optional[_Union[EncryptionSettings, _Mapping]] = ..., creation_time_secs: _Optional[str] = ..., provisioning_state: _Optional[str] = ..., hyperv_generation: _Optional[str] = ..., encryption_settings_collection: _Optional[_Union[DiskOrSnapshotInfo.Properties.EncryptionSettingsCollection, _Mapping]] = ..., is_incremental: bool = ..., disk_access_id: _Optional[str] = ..., network_access_policy: _Optional[str] = ..., public_network_access: _Optional[str] = ..., security_profile: _Optional[_Union[DiskSecurityProfile, _Mapping]] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MANAGING_VM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    managing_vm: str
    type: DiskOrSnapshotInfo.Type
    location: str
    id: str
    name: str
    sku: str
    properties: DiskOrSnapshotInfo.Properties
    tags: _containers.ScalarMap[str, str]
    zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, managing_vm: _Optional[str] = ..., type: _Optional[_Union[DiskOrSnapshotInfo.Type, str]] = ..., location: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., sku: _Optional[str] = ..., properties: _Optional[_Union[DiskOrSnapshotInfo.Properties, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...

class VMInfoArg(_message.Message):
    __slots__ = ("resource_group_name", "vm_name")
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_group_name: str
    vm_name: str
    def __init__(self, resource_group_name: _Optional[str] = ..., vm_name: _Optional[str] = ...) -> None: ...

class SecurityProfile(_message.Message):
    __slots__ = ("secure_boot_enabled", "vtpm_enabled", "security_type", "encryption_at_host")
    SECURE_BOOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VTPM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_AT_HOST_FIELD_NUMBER: _ClassVar[int]
    secure_boot_enabled: bool
    vtpm_enabled: bool
    security_type: str
    encryption_at_host: bool
    def __init__(self, secure_boot_enabled: bool = ..., vtpm_enabled: bool = ..., security_type: _Optional[str] = ..., encryption_at_host: bool = ...) -> None: ...

class VMInfoResult(_message.Message):
    __slots__ = ("id", "name", "location", "type", "disk_metadata_vec", "properties", "plan", "tags", "zones")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kManaged: _ClassVar[VMInfoResult.Type]
        kUnmanaged: _ClassVar[VMInfoResult.Type]
    kManaged: VMInfoResult.Type
    kUnmanaged: VMInfoResult.Type
    class Properties(_message.Message):
        __slots__ = ("provisioning_state", "vm_id", "hardware_profile", "network_profile", "os_type", "encryption_settings", "license_type", "availability_set", "security_profile")
        class HardwareProfile(_message.Message):
            __slots__ = ("vm_size_type",)
            VM_SIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
            vm_size_type: str
            def __init__(self, vm_size_type: _Optional[str] = ...) -> None: ...
        class NetworkProfile(_message.Message):
            __slots__ = ("network_interface_vec",)
            class NetworkInterfaces(_message.Message):
                __slots__ = ("id", "resource_group_name", "network_security_group_name", "enable_accelerated_networking", "name", "is_primary", "ip_configuration_vec", "security_resource_group", "tags")
                class IpConfiguration(_message.Message):
                    __slots__ = ("name", "vpn_name", "subnet_name", "subnet_resource_group", "public_ip_name", "private_ip_address", "is_primary")
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    VPN_NAME_FIELD_NUMBER: _ClassVar[int]
                    SUBNET_NAME_FIELD_NUMBER: _ClassVar[int]
                    SUBNET_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
                    PUBLIC_IP_NAME_FIELD_NUMBER: _ClassVar[int]
                    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
                    IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
                    name: str
                    vpn_name: str
                    subnet_name: str
                    subnet_resource_group: str
                    public_ip_name: str
                    private_ip_address: str
                    is_primary: bool
                    def __init__(self, name: _Optional[str] = ..., vpn_name: _Optional[str] = ..., subnet_name: _Optional[str] = ..., subnet_resource_group: _Optional[str] = ..., public_ip_name: _Optional[str] = ..., private_ip_address: _Optional[str] = ..., is_primary: bool = ...) -> None: ...
                class TagsEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: str
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                ID_FIELD_NUMBER: _ClassVar[int]
                RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
                NETWORK_SECURITY_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
                ENABLE_ACCELERATED_NETWORKING_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
                IP_CONFIGURATION_VEC_FIELD_NUMBER: _ClassVar[int]
                SECURITY_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
                TAGS_FIELD_NUMBER: _ClassVar[int]
                id: str
                resource_group_name: str
                network_security_group_name: str
                enable_accelerated_networking: bool
                name: str
                is_primary: bool
                ip_configuration_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.Properties.NetworkProfile.NetworkInterfaces.IpConfiguration]
                security_resource_group: str
                tags: _containers.ScalarMap[str, str]
                def __init__(self, id: _Optional[str] = ..., resource_group_name: _Optional[str] = ..., network_security_group_name: _Optional[str] = ..., enable_accelerated_networking: bool = ..., name: _Optional[str] = ..., is_primary: bool = ..., ip_configuration_vec: _Optional[_Iterable[_Union[VMInfoResult.Properties.NetworkProfile.NetworkInterfaces.IpConfiguration, _Mapping]]] = ..., security_resource_group: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
            NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
            network_interface_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.Properties.NetworkProfile.NetworkInterfaces]
            def __init__(self, network_interface_vec: _Optional[_Iterable[_Union[VMInfoResult.Properties.NetworkProfile.NetworkInterfaces, _Mapping]]] = ...) -> None: ...
        class SubResource(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        VM_ID_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_SET_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: str
        vm_id: str
        hardware_profile: VMInfoResult.Properties.HardwareProfile
        network_profile: VMInfoResult.Properties.NetworkProfile
        os_type: str
        encryption_settings: EncryptionSettings
        license_type: str
        availability_set: VMInfoResult.Properties.SubResource
        security_profile: SecurityProfile
        def __init__(self, provisioning_state: _Optional[str] = ..., vm_id: _Optional[str] = ..., hardware_profile: _Optional[_Union[VMInfoResult.Properties.HardwareProfile, _Mapping]] = ..., network_profile: _Optional[_Union[VMInfoResult.Properties.NetworkProfile, _Mapping]] = ..., os_type: _Optional[str] = ..., encryption_settings: _Optional[_Union[EncryptionSettings, _Mapping]] = ..., license_type: _Optional[str] = ..., availability_set: _Optional[_Union[VMInfoResult.Properties.SubResource, _Mapping]] = ..., security_profile: _Optional[_Union[SecurityProfile, _Mapping]] = ...) -> None: ...
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
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    location: str
    type: VMInfoResult.Type
    disk_metadata_vec: _containers.RepeatedCompositeFieldContainer[DiskMetadata]
    properties: VMInfoResult.Properties
    plan: VMInfoResult.Plan
    tags: _containers.ScalarMap[str, str]
    zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., type: _Optional[_Union[VMInfoResult.Type, str]] = ..., disk_metadata_vec: _Optional[_Iterable[_Union[DiskMetadata, _Mapping]]] = ..., properties: _Optional[_Union[VMInfoResult.Properties, _Mapping]] = ..., plan: _Optional[_Union[VMInfoResult.Plan, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., zones: _Optional[_Iterable[str]] = ...) -> None: ...

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

class CommonStorageParams(_message.Message):
    __slots__ = ("resource_group_name", "storage_account_name", "storage_container_name", "storage_access_key", "azure_stack_region", "azure_stack_hub_domain_name")
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_REGION_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_HUB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_group_name: str
    storage_account_name: str
    storage_container_name: str
    storage_access_key: str
    azure_stack_region: str
    azure_stack_hub_domain_name: str
    def __init__(self, resource_group_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., storage_access_key: _Optional[str] = ..., azure_stack_region: _Optional[str] = ..., azure_stack_hub_domain_name: _Optional[str] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CreateManagedDiskSnapshotArg(_message.Message):
    __slots__ = ("location", "snapshot_name", "create_option", "snapshot_sku", "disk_size_bytes", "source_resource_id", "tag_uuid", "is_incremental", "disk_access_id", "tags_vec")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_OPTION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SKU_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    location: str
    snapshot_name: str
    create_option: str
    snapshot_sku: str
    disk_size_bytes: int
    source_resource_id: str
    tag_uuid: str
    is_incremental: bool
    disk_access_id: str
    tags_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, location: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., create_option: _Optional[str] = ..., snapshot_sku: _Optional[str] = ..., disk_size_bytes: _Optional[int] = ..., source_resource_id: _Optional[str] = ..., tag_uuid: _Optional[str] = ..., is_incremental: bool = ..., disk_access_id: _Optional[str] = ..., tags_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class CreateVMSnapshotArg(_message.Message):
    __slots__ = ("snapshot_arg_vec",)
    class DiskSnapshotArg(_message.Message):
        __slots__ = ("resource_group_name", "disk_id", "disk_url", "storage_params", "managed_disk_snapshot_arg")
        RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_URL_FIELD_NUMBER: _ClassVar[int]
        STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        MANAGED_DISK_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
        resource_group_name: str
        disk_id: str
        disk_url: str
        storage_params: CommonStorageParams
        managed_disk_snapshot_arg: CreateManagedDiskSnapshotArg
        def __init__(self, resource_group_name: _Optional[str] = ..., disk_id: _Optional[str] = ..., disk_url: _Optional[str] = ..., storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., managed_disk_snapshot_arg: _Optional[_Union[CreateManagedDiskSnapshotArg, _Mapping]] = ...) -> None: ...
    SNAPSHOT_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_arg_vec: _containers.RepeatedCompositeFieldContainer[CreateVMSnapshotArg.DiskSnapshotArg]
    def __init__(self, snapshot_arg_vec: _Optional[_Iterable[_Union[CreateVMSnapshotArg.DiskSnapshotArg, _Mapping]]] = ...) -> None: ...

class CreateVMSnapshotResult(_message.Message):
    __slots__ = ("snapshot_result_vec",)
    class DiskSnapshotResult(_message.Message):
        __slots__ = ("disk_id", "snapshot_uuid", "size_bytes", "snapshot_etag")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ETAG_FIELD_NUMBER: _ClassVar[int]
        disk_id: str
        snapshot_uuid: str
        size_bytes: int
        snapshot_etag: str
        def __init__(self, disk_id: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., size_bytes: _Optional[int] = ..., snapshot_etag: _Optional[str] = ...) -> None: ...
    SNAPSHOT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_result_vec: _containers.RepeatedCompositeFieldContainer[CreateVMSnapshotResult.DiskSnapshotResult]
    def __init__(self, snapshot_result_vec: _Optional[_Iterable[_Union[CreateVMSnapshotResult.DiskSnapshotResult, _Mapping]]] = ...) -> None: ...

class GetSASUrlArg(_message.Message):
    __slots__ = ("resource_group_name", "access", "access_expiry_secs", "snapshot_uuid", "is_disk")
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXPIRY_SECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_DISK_FIELD_NUMBER: _ClassVar[int]
    resource_group_name: str
    access: str
    access_expiry_secs: int
    snapshot_uuid: str
    is_disk: bool
    def __init__(self, resource_group_name: _Optional[str] = ..., access: _Optional[str] = ..., access_expiry_secs: _Optional[int] = ..., snapshot_uuid: _Optional[str] = ..., is_disk: bool = ...) -> None: ...

class GetSASUrlResult(_message.Message):
    __slots__ = ("snapshot_uuid", "sas_url")
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SAS_URL_FIELD_NUMBER: _ClassVar[int]
    snapshot_uuid: str
    sas_url: str
    def __init__(self, snapshot_uuid: _Optional[str] = ..., sas_url: _Optional[str] = ...) -> None: ...

class CopySnapshotArg(_message.Message):
    __slots__ = ("resource_group_name", "dest_storage_account_name", "dest_storage_container_name", "dest_storage_access_key", "dest_blob_name", "snapshot_uuid", "sas_url", "should_wait_for_completion")
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    DEST_BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SAS_URL_FIELD_NUMBER: _ClassVar[int]
    SHOULD_WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    resource_group_name: str
    dest_storage_account_name: str
    dest_storage_container_name: str
    dest_storage_access_key: str
    dest_blob_name: str
    snapshot_uuid: str
    sas_url: str
    should_wait_for_completion: bool
    def __init__(self, resource_group_name: _Optional[str] = ..., dest_storage_account_name: _Optional[str] = ..., dest_storage_container_name: _Optional[str] = ..., dest_storage_access_key: _Optional[str] = ..., dest_blob_name: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., sas_url: _Optional[str] = ..., should_wait_for_completion: bool = ...) -> None: ...

class CopySnapshotResult(_message.Message):
    __slots__ = ("snapshot_uuid", "dest_blob_name")
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    DEST_BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    snapshot_uuid: str
    dest_blob_name: str
    def __init__(self, snapshot_uuid: _Optional[str] = ..., dest_blob_name: _Optional[str] = ...) -> None: ...

class ManagedSnapshotInfoArg(_message.Message):
    __slots__ = ("snapshot_info_vec",)
    class ManagedSnapshotInfo(_message.Message):
        __slots__ = ("resource_group_name", "snapshot_id", "is_disk")
        RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        IS_DISK_FIELD_NUMBER: _ClassVar[int]
        resource_group_name: str
        snapshot_id: str
        is_disk: bool
        def __init__(self, resource_group_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., is_disk: bool = ...) -> None: ...
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[ManagedSnapshotInfoArg.ManagedSnapshotInfo]
    def __init__(self, snapshot_info_vec: _Optional[_Iterable[_Union[ManagedSnapshotInfoArg.ManagedSnapshotInfo, _Mapping]]] = ...) -> None: ...

class BlobProperties(_message.Message):
    __slots__ = ("storage_params", "blob_name", "snapshot_uuid", "blob_size_bytes", "blob_etag", "lease_state", "lease_status", "blob_url")
    STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BLOB_ETAG_FIELD_NUMBER: _ClassVar[int]
    LEASE_STATE_FIELD_NUMBER: _ClassVar[int]
    LEASE_STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOB_URL_FIELD_NUMBER: _ClassVar[int]
    storage_params: CommonStorageParams
    blob_name: str
    snapshot_uuid: str
    blob_size_bytes: int
    blob_etag: str
    lease_state: str
    lease_status: str
    blob_url: str
    def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., blob_name: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., blob_size_bytes: _Optional[int] = ..., blob_etag: _Optional[str] = ..., lease_state: _Optional[str] = ..., lease_status: _Optional[str] = ..., blob_url: _Optional[str] = ...) -> None: ...

class GetBlobPropertiesArg(_message.Message):
    __slots__ = ("blob_info_vec",)
    class BlobInfo(_message.Message):
        __slots__ = ("storage_params", "blob_name", "blob_url", "snapshot_uuid")
        STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
        BLOB_URL_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
        storage_params: CommonStorageParams
        blob_name: str
        blob_url: str
        snapshot_uuid: str
        def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., blob_name: _Optional[str] = ..., blob_url: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ...) -> None: ...
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[GetBlobPropertiesArg.BlobInfo]
    def __init__(self, blob_info_vec: _Optional[_Iterable[_Union[GetBlobPropertiesArg.BlobInfo, _Mapping]]] = ...) -> None: ...

class GetBlobPropertiesResult(_message.Message):
    __slots__ = ("blob_properties_map",)
    class BlobPropertiesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BlobProperties
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BlobProperties, _Mapping]] = ...) -> None: ...
    BLOB_PROPERTIES_MAP_FIELD_NUMBER: _ClassVar[int]
    blob_properties_map: _containers.MessageMap[str, BlobProperties]
    def __init__(self, blob_properties_map: _Optional[_Mapping[str, BlobProperties]] = ...) -> None: ...

class GetBlobRangeArg(_message.Message):
    __slots__ = ("storage_params", "blob_name", "blob_url", "snapshot_uuid", "start_byte_offset", "content_length_bytes", "should_fetch_md5_hash")
    STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    BLOB_URL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    START_BYTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHOULD_FETCH_MD5_HASH_FIELD_NUMBER: _ClassVar[int]
    storage_params: CommonStorageParams
    blob_name: str
    blob_url: str
    snapshot_uuid: str
    start_byte_offset: int
    content_length_bytes: int
    should_fetch_md5_hash: bool
    def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., blob_name: _Optional[str] = ..., blob_url: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., start_byte_offset: _Optional[int] = ..., content_length_bytes: _Optional[int] = ..., should_fetch_md5_hash: bool = ...) -> None: ...

class GetBlobRangeResult(_message.Message):
    __slots__ = ("blob_name", "snapshot_uuid", "start_byte_offset", "content_length_bytes", "blob_content", "content_md5")
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    START_BYTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    BLOB_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MD5_FIELD_NUMBER: _ClassVar[int]
    blob_name: str
    snapshot_uuid: str
    start_byte_offset: int
    content_length_bytes: int
    blob_content: str
    content_md5: str
    def __init__(self, blob_name: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., start_byte_offset: _Optional[int] = ..., content_length_bytes: _Optional[int] = ..., blob_content: _Optional[str] = ..., content_md5: _Optional[str] = ...) -> None: ...

class GetPageRangesArg(_message.Message):
    __slots__ = ("storage_params", "blob_name", "source_url", "base_snapshot_uuid", "current_snapshot_uuid", "snapshot_size_bytes", "is_sas_source", "previous_snapshot_url", "private_ip_address", "private_host_name")
    STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_SAS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    storage_params: CommonStorageParams
    blob_name: str
    source_url: str
    base_snapshot_uuid: str
    current_snapshot_uuid: str
    snapshot_size_bytes: int
    is_sas_source: bool
    previous_snapshot_url: str
    private_ip_address: str
    private_host_name: str
    def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., blob_name: _Optional[str] = ..., source_url: _Optional[str] = ..., base_snapshot_uuid: _Optional[str] = ..., current_snapshot_uuid: _Optional[str] = ..., snapshot_size_bytes: _Optional[int] = ..., is_sas_source: bool = ..., previous_snapshot_url: _Optional[str] = ..., private_ip_address: _Optional[str] = ..., private_host_name: _Optional[str] = ...) -> None: ...

class GetPageRangesResult(_message.Message):
    __slots__ = ("delta_type", "delta_info", "cleared_delta_info")
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    CLEARED_DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    cleared_delta_info: _cbt_delta_pb2.CBTDeltaInfo
    def __init__(self, delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., cleared_delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ...) -> None: ...

class RunCommandRequest(_message.Message):
    __slots__ = ("command_id", "parameters", "script")
    class RunCommandInputParameter(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    parameters: _containers.RepeatedCompositeFieldContainer[RunCommandRequest.RunCommandInputParameter]
    script: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, command_id: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[RunCommandRequest.RunCommandInputParameter, _Mapping]]] = ..., script: _Optional[_Iterable[str]] = ...) -> None: ...

class SetBlobPropertiesArg(_message.Message):
    __slots__ = ("blob_info_vec",)
    class BlobInfo(_message.Message):
        __slots__ = ("storage_params", "blob_name", "blob_url", "new_size")
        STORAGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
        BLOB_URL_FIELD_NUMBER: _ClassVar[int]
        NEW_SIZE_FIELD_NUMBER: _ClassVar[int]
        storage_params: CommonStorageParams
        blob_name: str
        blob_url: str
        new_size: int
        def __init__(self, storage_params: _Optional[_Union[CommonStorageParams, _Mapping]] = ..., blob_name: _Optional[str] = ..., blob_url: _Optional[str] = ..., new_size: _Optional[int] = ...) -> None: ...
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[SetBlobPropertiesArg.BlobInfo]
    def __init__(self, blob_info_vec: _Optional[_Iterable[_Union[SetBlobPropertiesArg.BlobInfo, _Mapping]]] = ...) -> None: ...
