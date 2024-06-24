from magneto.base.entities import s3_pb2 as _s3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockDeviceMapping(_message.Message):
    __slots__ = ("device_name", "ebs_volume_id", "volume_size_bytes", "volume_type", "delete_on_termination", "is_encrypted", "kms_key_id", "snapshot_id", "src_snapshot_id", "num_iops", "is_marketplace", "creation_time_msecs", "state", "volume_tags_vec", "volume_name", "throughput")
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    EBS_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_IOPS_FIELD_NUMBER: _ClassVar[int]
    IS_MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    device_name: str
    ebs_volume_id: str
    volume_size_bytes: int
    volume_type: str
    delete_on_termination: bool
    is_encrypted: bool
    kms_key_id: str
    snapshot_id: str
    src_snapshot_id: str
    num_iops: int
    is_marketplace: bool
    creation_time_msecs: int
    state: str
    volume_tags_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    volume_name: str
    throughput: int
    def __init__(self, device_name: _Optional[str] = ..., ebs_volume_id: _Optional[str] = ..., volume_size_bytes: _Optional[int] = ..., volume_type: _Optional[str] = ..., delete_on_termination: bool = ..., is_encrypted: bool = ..., kms_key_id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., src_snapshot_id: _Optional[str] = ..., num_iops: _Optional[int] = ..., is_marketplace: bool = ..., creation_time_msecs: _Optional[int] = ..., state: _Optional[str] = ..., volume_tags_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., volume_name: _Optional[str] = ..., throughput: _Optional[int] = ...) -> None: ...

class BootMode(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLegacyBIOS: _ClassVar[BootMode.Type]
        kUEFI: _ClassVar[BootMode.Type]
    kLegacyBIOS: BootMode.Type
    kUEFI: BootMode.Type
    def __init__(self) -> None: ...

class VMInfoArg(_message.Message):
    __slots__ = ("region_name", "instance_id", "should_populate_marketplace_info", "should_populate_kms_aliases", "instance_tags_vec", "should_populate_boot_mode")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_MARKETPLACE_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_KMS_ALIASES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_BOOT_MODE_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    instance_id: str
    should_populate_marketplace_info: bool
    should_populate_kms_aliases: bool
    instance_tags_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    should_populate_boot_mode: bool
    def __init__(self, region_name: _Optional[str] = ..., instance_id: _Optional[str] = ..., should_populate_marketplace_info: bool = ..., should_populate_kms_aliases: bool = ..., instance_tags_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., should_populate_boot_mode: bool = ...) -> None: ...

class VMInfoResult(_message.Message):
    __slots__ = ("region_name", "block_device_mapping_vec", "instance_id", "instance_type", "image_id", "subnet_id", "vpc_id", "kernel_id", "ram_disk_id", "public_ip_address", "private_ip_address", "security_group_ids", "key_pair_name", "placement_group", "is_ebs_optimized", "is_ena_supported", "network_interface_vec", "tag_specification_vec", "instance_name", "root_device_name", "architecture", "virtualization", "platform", "is_marketplace", "state", "attached_iam_role", "size_in_bytes", "launch_time", "launch_time_msecs", "iam_instance_profile", "monitoring", "cpu_options", "capacity_reservation_specification", "hibernation_options", "license_configurations_vec", "metadata_options", "enclave_options", "boot_mode", "private_ip_addresses")
    class PlacementGroup(_message.Message):
        __slots__ = ("tenancy", "availability_zone")
        TENANCY_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
        tenancy: str
        availability_zone: str
        def __init__(self, tenancy: _Optional[str] = ..., availability_zone: _Optional[str] = ...) -> None: ...
    class NetworkInterface(_message.Message):
        __slots__ = ("description", "device_index", "subnet_id", "network_card_index", "network_interface_id", "private_ip_address_vec", "ipv6_address_vec", "security_group_id_vec")
        class InstanceIpAddress(_message.Message):
            __slots__ = ("private_ip_address", "primary")
            PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_FIELD_NUMBER: _ClassVar[int]
            private_ip_address: str
            primary: bool
            def __init__(self, private_ip_address: _Optional[str] = ..., primary: bool = ...) -> None: ...
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
        IPV6_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
        SECURITY_GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        description: str
        device_index: int
        subnet_id: str
        network_card_index: int
        network_interface_id: str
        private_ip_address_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.NetworkInterface.InstanceIpAddress]
        ipv6_address_vec: _containers.RepeatedScalarFieldContainer[str]
        security_group_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, description: _Optional[str] = ..., device_index: _Optional[int] = ..., subnet_id: _Optional[str] = ..., network_card_index: _Optional[int] = ..., network_interface_id: _Optional[str] = ..., private_ip_address_vec: _Optional[_Iterable[_Union[VMInfoResult.NetworkInterface.InstanceIpAddress, _Mapping]]] = ..., ipv6_address_vec: _Optional[_Iterable[str]] = ..., security_group_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class TagSpecifications(_message.Message):
        __slots__ = ("resource_type", "tag_info_vec")
        class TagInfo(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TAG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        tag_info_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.TagSpecifications.TagInfo]
        def __init__(self, resource_type: _Optional[str] = ..., tag_info_vec: _Optional[_Iterable[_Union[VMInfoResult.TagSpecifications.TagInfo, _Mapping]]] = ...) -> None: ...
    class IAMInstanceProfile(_message.Message):
        __slots__ = ("arn", "id")
        ARN_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        arn: str
        id: str
        def __init__(self, arn: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class Monitoring(_message.Message):
        __slots__ = ("state",)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: str
        def __init__(self, state: _Optional[str] = ...) -> None: ...
    class CpuOptions(_message.Message):
        __slots__ = ("core_count", "threads_per_core")
        CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
        THREADS_PER_CORE_FIELD_NUMBER: _ClassVar[int]
        core_count: int
        threads_per_core: int
        def __init__(self, core_count: _Optional[int] = ..., threads_per_core: _Optional[int] = ...) -> None: ...
    class CapacityReservationSpecification(_message.Message):
        __slots__ = ("capacity_reservation_preference", "capacity_reservation_target")
        class CapacityReservationTarget(_message.Message):
            __slots__ = ("capacity_reservation_id", "capacity_reservation_resource_group_arn")
            CAPACITY_RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
            CAPACITY_RESERVATION_RESOURCE_GROUP_ARN_FIELD_NUMBER: _ClassVar[int]
            capacity_reservation_id: str
            capacity_reservation_resource_group_arn: str
            def __init__(self, capacity_reservation_id: _Optional[str] = ..., capacity_reservation_resource_group_arn: _Optional[str] = ...) -> None: ...
        CAPACITY_RESERVATION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_RESERVATION_TARGET_FIELD_NUMBER: _ClassVar[int]
        capacity_reservation_preference: str
        capacity_reservation_target: VMInfoResult.CapacityReservationSpecification.CapacityReservationTarget
        def __init__(self, capacity_reservation_preference: _Optional[str] = ..., capacity_reservation_target: _Optional[_Union[VMInfoResult.CapacityReservationSpecification.CapacityReservationTarget, _Mapping]] = ...) -> None: ...
    class HibernationOptions(_message.Message):
        __slots__ = ("is_configured",)
        IS_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
        is_configured: bool
        def __init__(self, is_configured: bool = ...) -> None: ...
    class LicenseConfiguration(_message.Message):
        __slots__ = ("license_configuration_arn",)
        LICENSE_CONFIGURATION_ARN_FIELD_NUMBER: _ClassVar[int]
        license_configuration_arn: str
        def __init__(self, license_configuration_arn: _Optional[str] = ...) -> None: ...
    class MetadataOptions(_message.Message):
        __slots__ = ("http_tokens", "http_put_response_hop_limit", "http_endpoint")
        HTTP_TOKENS_FIELD_NUMBER: _ClassVar[int]
        HTTP_PUT_RESPONSE_HOP_LIMIT_FIELD_NUMBER: _ClassVar[int]
        HTTP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        http_tokens: str
        http_put_response_hop_limit: int
        http_endpoint: str
        def __init__(self, http_tokens: _Optional[str] = ..., http_put_response_hop_limit: _Optional[int] = ..., http_endpoint: _Optional[str] = ...) -> None: ...
    class EnclaveOptions(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICE_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    KERNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RAM_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_PAIR_NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    IS_EBS_OPTIMIZED_FIELD_NUMBER: _ClassVar[int]
    IS_ENA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_SPECIFICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TIME_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    IAM_INSTANCE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    CPU_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_RESERVATION_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    HIBERNATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LICENSE_CONFIGURATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENCLAVE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BOOT_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    block_device_mapping_vec: _containers.RepeatedCompositeFieldContainer[BlockDeviceMapping]
    instance_id: str
    instance_type: str
    image_id: str
    subnet_id: str
    vpc_id: str
    kernel_id: str
    ram_disk_id: str
    public_ip_address: str
    private_ip_address: str
    security_group_ids: _containers.RepeatedScalarFieldContainer[str]
    key_pair_name: str
    placement_group: VMInfoResult.PlacementGroup
    is_ebs_optimized: bool
    is_ena_supported: bool
    network_interface_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.NetworkInterface]
    tag_specification_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.TagSpecifications]
    instance_name: str
    root_device_name: str
    architecture: str
    virtualization: str
    platform: str
    is_marketplace: bool
    state: str
    attached_iam_role: str
    size_in_bytes: int
    launch_time: str
    launch_time_msecs: int
    iam_instance_profile: VMInfoResult.IAMInstanceProfile
    monitoring: VMInfoResult.Monitoring
    cpu_options: VMInfoResult.CpuOptions
    capacity_reservation_specification: VMInfoResult.CapacityReservationSpecification
    hibernation_options: VMInfoResult.HibernationOptions
    license_configurations_vec: _containers.RepeatedCompositeFieldContainer[VMInfoResult.LicenseConfiguration]
    metadata_options: VMInfoResult.MetadataOptions
    enclave_options: VMInfoResult.EnclaveOptions
    boot_mode: BootMode.Type
    private_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, region_name: _Optional[str] = ..., block_device_mapping_vec: _Optional[_Iterable[_Union[BlockDeviceMapping, _Mapping]]] = ..., instance_id: _Optional[str] = ..., instance_type: _Optional[str] = ..., image_id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., vpc_id: _Optional[str] = ..., kernel_id: _Optional[str] = ..., ram_disk_id: _Optional[str] = ..., public_ip_address: _Optional[str] = ..., private_ip_address: _Optional[str] = ..., security_group_ids: _Optional[_Iterable[str]] = ..., key_pair_name: _Optional[str] = ..., placement_group: _Optional[_Union[VMInfoResult.PlacementGroup, _Mapping]] = ..., is_ebs_optimized: bool = ..., is_ena_supported: bool = ..., network_interface_vec: _Optional[_Iterable[_Union[VMInfoResult.NetworkInterface, _Mapping]]] = ..., tag_specification_vec: _Optional[_Iterable[_Union[VMInfoResult.TagSpecifications, _Mapping]]] = ..., instance_name: _Optional[str] = ..., root_device_name: _Optional[str] = ..., architecture: _Optional[str] = ..., virtualization: _Optional[str] = ..., platform: _Optional[str] = ..., is_marketplace: bool = ..., state: _Optional[str] = ..., attached_iam_role: _Optional[str] = ..., size_in_bytes: _Optional[int] = ..., launch_time: _Optional[str] = ..., launch_time_msecs: _Optional[int] = ..., iam_instance_profile: _Optional[_Union[VMInfoResult.IAMInstanceProfile, _Mapping]] = ..., monitoring: _Optional[_Union[VMInfoResult.Monitoring, _Mapping]] = ..., cpu_options: _Optional[_Union[VMInfoResult.CpuOptions, _Mapping]] = ..., capacity_reservation_specification: _Optional[_Union[VMInfoResult.CapacityReservationSpecification, _Mapping]] = ..., hibernation_options: _Optional[_Union[VMInfoResult.HibernationOptions, _Mapping]] = ..., license_configurations_vec: _Optional[_Iterable[_Union[VMInfoResult.LicenseConfiguration, _Mapping]]] = ..., metadata_options: _Optional[_Union[VMInfoResult.MetadataOptions, _Mapping]] = ..., enclave_options: _Optional[_Union[VMInfoResult.EnclaveOptions, _Mapping]] = ..., boot_mode: _Optional[_Union[BootMode.Type, str]] = ..., private_ip_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateVMSnapshotArg(_message.Message):
    __slots__ = ("region_name", "snapshot_arg_vec")
    class EBSVolumeSnapshotArg(_message.Message):
        __slots__ = ("id", "tag_uuid", "tag_vec")
        ID_FIELD_NUMBER: _ClassVar[int]
        TAG_UUID_FIELD_NUMBER: _ClassVar[int]
        TAG_VEC_FIELD_NUMBER: _ClassVar[int]
        id: str
        tag_uuid: str
        tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
        def __init__(self, id: _Optional[str] = ..., tag_uuid: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_arg_vec: _containers.RepeatedCompositeFieldContainer[CreateVMSnapshotArg.EBSVolumeSnapshotArg]
    def __init__(self, region_name: _Optional[str] = ..., snapshot_arg_vec: _Optional[_Iterable[_Union[CreateVMSnapshotArg.EBSVolumeSnapshotArg, _Mapping]]] = ...) -> None: ...

class CreateVMSnapshotResult(_message.Message):
    __slots__ = ("snapshot_result_vec",)
    class EBSVolumeSnapshotResult(_message.Message):
        __slots__ = ("id", "snapshot_id", "size_bytes")
        ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        id: str
        snapshot_id: str
        size_bytes: int
        def __init__(self, id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    SNAPSHOT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_result_vec: _containers.RepeatedCompositeFieldContainer[CreateVMSnapshotResult.EBSVolumeSnapshotResult]
    def __init__(self, snapshot_result_vec: _Optional[_Iterable[_Union[CreateVMSnapshotResult.EBSVolumeSnapshotResult, _Mapping]]] = ...) -> None: ...

class FetchEBSSnapshotsInfoArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id_vec", "volume_id", "snapshot_tag")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TAG_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
    volume_id: str
    snapshot_tag: str
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id_vec: _Optional[_Iterable[str]] = ..., volume_id: _Optional[str] = ..., snapshot_tag: _Optional[str] = ...) -> None: ...

class FetchEBSSnapshotsInfoResult(_message.Message):
    __slots__ = ("snapshot_info_vec",)
    class SnapshotInfo(_message.Message):
        __slots__ = ("snapshot_id", "volume_id", "volume_size_gib", "progress_pct", "state", "start_time_msecs", "state_message", "snapshot_tags_vec")
        class SnapshotState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kPending: _ClassVar[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState]
            kComplete: _ClassVar[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState]
            kError: _ClassVar[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState]
            kNotSet: _ClassVar[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState]
            kUnknown: _ClassVar[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState]
        kPending: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        kComplete: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        kError: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        kNotSet: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        kUnknown: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_PCT_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        snapshot_id: str
        volume_id: str
        volume_size_gib: int
        progress_pct: int
        state: FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState
        start_time_msecs: int
        state_message: str
        snapshot_tags_vec: _containers.RepeatedCompositeFieldContainer[Tag]
        def __init__(self, snapshot_id: _Optional[str] = ..., volume_id: _Optional[str] = ..., volume_size_gib: _Optional[int] = ..., progress_pct: _Optional[int] = ..., state: _Optional[_Union[FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState, str]] = ..., start_time_msecs: _Optional[int] = ..., state_message: _Optional[str] = ..., snapshot_tags_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[FetchEBSSnapshotsInfoResult.SnapshotInfo]
    def __init__(self, snapshot_info_vec: _Optional[_Iterable[_Union[FetchEBSSnapshotsInfoResult.SnapshotInfo, _Mapping]]] = ...) -> None: ...

class DiskFormat(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVHD: _ClassVar[DiskFormat.Type]
        kVMDK: _ClassVar[DiskFormat.Type]
        kRAW: _ClassVar[DiskFormat.Type]
        kOVA: _ClassVar[DiskFormat.Type]
    kVHD: DiskFormat.Type
    kVMDK: DiskFormat.Type
    kRAW: DiskFormat.Type
    kOVA: DiskFormat.Type
    def __init__(self) -> None: ...

class ImportSnapshotArg(_message.Message):
    __slots__ = ("region_name", "s3_bucket", "s3_key", "client_token", "disk_format", "should_encrypt", "kms_key_id", "using_user_provided_kms_key")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    S3_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ENCRYPT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    USING_USER_PROVIDED_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    s3_bucket: str
    s3_key: str
    client_token: str
    disk_format: DiskFormat.Type
    should_encrypt: bool
    kms_key_id: str
    using_user_provided_kms_key: bool
    def __init__(self, region_name: _Optional[str] = ..., s3_bucket: _Optional[str] = ..., s3_key: _Optional[str] = ..., client_token: _Optional[str] = ..., disk_format: _Optional[_Union[DiskFormat.Type, str]] = ..., should_encrypt: bool = ..., kms_key_id: _Optional[str] = ..., using_user_provided_kms_key: bool = ...) -> None: ...

class ImportSnapshotResult(_message.Message):
    __slots__ = ("import_snapshot_task_id",)
    IMPORT_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    import_snapshot_task_id: str
    def __init__(self, import_snapshot_task_id: _Optional[str] = ...) -> None: ...

class CancelImportSnapshotTaskArg(_message.Message):
    __slots__ = ("region_name", "import_snapshot_task_id", "cancel_reason")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    import_snapshot_task_id: str
    cancel_reason: str
    def __init__(self, region_name: _Optional[str] = ..., import_snapshot_task_id: _Optional[str] = ..., cancel_reason: _Optional[str] = ...) -> None: ...

class CancelImportSnapshotTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelImportImageTaskArg(_message.Message):
    __slots__ = ("region_name", "import_image_task_id", "cancel_reason")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_IMAGE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    import_image_task_id: str
    cancel_reason: str
    def __init__(self, region_name: _Optional[str] = ..., import_image_task_id: _Optional[str] = ..., cancel_reason: _Optional[str] = ...) -> None: ...

class ImportSnapshotTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kError: _ClassVar[ImportSnapshotTaskStatus.Type]
        kComplete: _ClassVar[ImportSnapshotTaskStatus.Type]
        kActive: _ClassVar[ImportSnapshotTaskStatus.Type]
        kDeleted: _ClassVar[ImportSnapshotTaskStatus.Type]
        kDeleting: _ClassVar[ImportSnapshotTaskStatus.Type]
    kError: ImportSnapshotTaskStatus.Type
    kComplete: ImportSnapshotTaskStatus.Type
    kActive: ImportSnapshotTaskStatus.Type
    kDeleted: ImportSnapshotTaskStatus.Type
    kDeleting: ImportSnapshotTaskStatus.Type
    def __init__(self) -> None: ...

class DescribeImportSnapshotTaskArg(_message.Message):
    __slots__ = ("region_name", "import_snapshot_task_id", "wait_for_completion")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    import_snapshot_task_id: str
    wait_for_completion: bool
    def __init__(self, region_name: _Optional[str] = ..., import_snapshot_task_id: _Optional[str] = ..., wait_for_completion: bool = ...) -> None: ...

class DescribeImportSnapshotTaskResult(_message.Message):
    __slots__ = ("import_snapshot_task_status", "percentage_task_completion", "snapshot_id")
    IMPORT_SNAPSHOT_TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_TASK_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    import_snapshot_task_status: ImportSnapshotTaskStatus.Type
    percentage_task_completion: int
    snapshot_id: str
    def __init__(self, import_snapshot_task_status: _Optional[_Union[ImportSnapshotTaskStatus.Type, str]] = ..., percentage_task_completion: _Optional[int] = ..., snapshot_id: _Optional[str] = ...) -> None: ...

class CreateAMIFromSnapshotArg(_message.Message):
    __slots__ = ("region_name", "ami_name", "virtualization_type", "architecture_type", "root_device_name", "kernel_id", "ram_disk_id", "ena_supported", "block_device_mapping_vec", "boot_mode")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    AMI_NAME_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    KERNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RAM_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    ENA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICE_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    BOOT_MODE_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    ami_name: str
    virtualization_type: str
    architecture_type: str
    root_device_name: str
    kernel_id: str
    ram_disk_id: str
    ena_supported: bool
    block_device_mapping_vec: _containers.RepeatedCompositeFieldContainer[BlockDeviceMapping]
    boot_mode: BootMode.Type
    def __init__(self, region_name: _Optional[str] = ..., ami_name: _Optional[str] = ..., virtualization_type: _Optional[str] = ..., architecture_type: _Optional[str] = ..., root_device_name: _Optional[str] = ..., kernel_id: _Optional[str] = ..., ram_disk_id: _Optional[str] = ..., ena_supported: bool = ..., block_device_mapping_vec: _Optional[_Iterable[_Union[BlockDeviceMapping, _Mapping]]] = ..., boot_mode: _Optional[_Union[BootMode.Type, str]] = ...) -> None: ...

class CreateAMIFromSnapshotResult(_message.Message):
    __slots__ = ("image_id",)
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    def __init__(self, image_id: _Optional[str] = ...) -> None: ...

class DeleteSnapshotArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ...) -> None: ...

class DeleteSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateVMInstanceArg(_message.Message):
    __slots__ = ("vm_info", "power_on", "wait_for_status_check", "set_private_ip", "return_early_in_pending_state", "device_tag_map")
    class Tags(_message.Message):
        __slots__ = ("tags",)
        TAGS_FIELD_NUMBER: _ClassVar[int]
        tags: _containers.RepeatedCompositeFieldContainer[Tag]
        def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...
    class DeviceTagMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CreateVMInstanceArg.Tags
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CreateVMInstanceArg.Tags, _Mapping]] = ...) -> None: ...
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_STATUS_CHECK_FIELD_NUMBER: _ClassVar[int]
    SET_PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    RETURN_EARLY_IN_PENDING_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAG_MAP_FIELD_NUMBER: _ClassVar[int]
    vm_info: VMInfoResult
    power_on: bool
    wait_for_status_check: bool
    set_private_ip: bool
    return_early_in_pending_state: bool
    device_tag_map: _containers.MessageMap[str, CreateVMInstanceArg.Tags]
    def __init__(self, vm_info: _Optional[_Union[VMInfoResult, _Mapping]] = ..., power_on: bool = ..., wait_for_status_check: bool = ..., set_private_ip: bool = ..., return_early_in_pending_state: bool = ..., device_tag_map: _Optional[_Mapping[str, CreateVMInstanceArg.Tags]] = ...) -> None: ...

class CreateVMInstanceResult(_message.Message):
    __slots__ = ("instance_id", "public_ip_address", "private_ip_address", "instance_type", "availability_zone")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    public_ip_address: str
    private_ip_address: str
    instance_type: str
    availability_zone: str
    def __init__(self, instance_id: _Optional[str] = ..., public_ip_address: _Optional[str] = ..., private_ip_address: _Optional[str] = ..., instance_type: _Optional[str] = ..., availability_zone: _Optional[str] = ...) -> None: ...

class StartInstanceArg(_message.Message):
    __slots__ = ("instance_id", "region_name", "wait_for_status_check")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_STATUS_CHECK_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    region_name: str
    wait_for_status_check: bool
    def __init__(self, instance_id: _Optional[str] = ..., region_name: _Optional[str] = ..., wait_for_status_check: bool = ...) -> None: ...

class CreateEBSSnapshotArg(_message.Message):
    __slots__ = ("region_name", "volume_id", "description", "tag_uuid", "tag_vec", "wait_for_completion")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAG_UUID_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    volume_id: str
    description: str
    tag_uuid: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    wait_for_completion: bool
    def __init__(self, region_name: _Optional[str] = ..., volume_id: _Optional[str] = ..., description: _Optional[str] = ..., tag_uuid: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., wait_for_completion: bool = ...) -> None: ...

class CreateEBSSnapshotResult(_message.Message):
    __slots__ = ("snapshot_id", "volume_size_gib", "time_taken_usecs")
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: str
    volume_size_gib: int
    time_taken_usecs: int
    def __init__(self, snapshot_id: _Optional[str] = ..., volume_size_gib: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ...) -> None: ...

class CopySnapshotArg(_message.Message):
    __slots__ = ("name", "source_snapshot_id", "source_region", "dest_region", "description", "should_encrypt", "kms_key_id", "tag_vec", "wait_for_completion")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REGION_FIELD_NUMBER: _ClassVar[int]
    DEST_REGION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ENCRYPT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_snapshot_id: str
    source_region: str
    dest_region: str
    description: str
    should_encrypt: bool
    kms_key_id: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    wait_for_completion: bool
    def __init__(self, name: _Optional[str] = ..., source_snapshot_id: _Optional[str] = ..., source_region: _Optional[str] = ..., dest_region: _Optional[str] = ..., description: _Optional[str] = ..., should_encrypt: bool = ..., kms_key_id: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., wait_for_completion: bool = ...) -> None: ...

class CopySnapshotResult(_message.Message):
    __slots__ = ("snapshot_id",)
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: str
    def __init__(self, snapshot_id: _Optional[str] = ...) -> None: ...

class CreateEBSVolumeArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id", "availability_zone", "ebs_volume_type", "num_iops", "volume_size_gib", "encrypt_volume", "kms_key_id", "tag_uuid", "tag_vec", "throughput")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    EBS_VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_IOPS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_UUID_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    availability_zone: str
    ebs_volume_type: str
    num_iops: int
    volume_size_gib: int
    encrypt_volume: bool
    kms_key_id: str
    tag_uuid: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    throughput: int
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., availability_zone: _Optional[str] = ..., ebs_volume_type: _Optional[str] = ..., num_iops: _Optional[int] = ..., volume_size_gib: _Optional[int] = ..., encrypt_volume: bool = ..., kms_key_id: _Optional[str] = ..., tag_uuid: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., throughput: _Optional[int] = ...) -> None: ...

class CreateEBSVolumeResult(_message.Message):
    __slots__ = ("volume_id", "volume_size_gibs", "availability_zone")
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_GIBS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    volume_id: str
    volume_size_gibs: int
    availability_zone: str
    def __init__(self, volume_id: _Optional[str] = ..., volume_size_gibs: _Optional[int] = ..., availability_zone: _Optional[str] = ...) -> None: ...

class DescribeEBSVolumesArg(_message.Message):
    __slots__ = ("region_name", "volume_id_vec", "volume_tag")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TAG_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    volume_id_vec: _containers.RepeatedScalarFieldContainer[str]
    volume_tag: str
    def __init__(self, region_name: _Optional[str] = ..., volume_id_vec: _Optional[_Iterable[str]] = ..., volume_tag: _Optional[str] = ...) -> None: ...

class DescribeEBSVolumesResult(_message.Message):
    __slots__ = ("block_device_mapping_vec",)
    BLOCK_DEVICE_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    block_device_mapping_vec: _containers.RepeatedCompositeFieldContainer[BlockDeviceMapping]
    def __init__(self, block_device_mapping_vec: _Optional[_Iterable[_Union[BlockDeviceMapping, _Mapping]]] = ...) -> None: ...

class AttachEBSVolumeArg(_message.Message):
    __slots__ = ("volume_id", "instance_id", "device_name", "region_name", "delete_on_termination")
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    volume_id: str
    instance_id: str
    device_name: str
    region_name: str
    delete_on_termination: bool
    def __init__(self, volume_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., device_name: _Optional[str] = ..., region_name: _Optional[str] = ..., delete_on_termination: bool = ...) -> None: ...

class AttachEBSVolumeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteEBSVolumeArg(_message.Message):
    __slots__ = ("region_name", "volume_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    volume_id: str
    def __init__(self, region_name: _Optional[str] = ..., volume_id: _Optional[str] = ...) -> None: ...

class DeleteEBSVolumeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetachEBSVolumeArg(_message.Message):
    __slots__ = ("volume_id", "region_name")
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    volume_id: str
    region_name: str
    def __init__(self, volume_id: _Optional[str] = ..., region_name: _Optional[str] = ...) -> None: ...

class DetachEBSVolumeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubnetAddrMask(_message.Message):
    __slots__ = ("subnet_ip", "subnet_mask")
    SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    SUBNET_MASK_FIELD_NUMBER: _ClassVar[int]
    subnet_ip: str
    subnet_mask: str
    def __init__(self, subnet_ip: _Optional[str] = ..., subnet_mask: _Optional[str] = ...) -> None: ...

class CreateSecurityGroupArg(_message.Message):
    __slots__ = ("vpc_id", "region_name", "security_group_name", "incoming_tcp_ports", "cluster_subnet_address_vec")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    INCOMING_TCP_PORTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    region_name: str
    security_group_name: str
    incoming_tcp_ports: _containers.RepeatedScalarFieldContainer[int]
    cluster_subnet_address_vec: _containers.RepeatedCompositeFieldContainer[SubnetAddrMask]
    def __init__(self, vpc_id: _Optional[str] = ..., region_name: _Optional[str] = ..., security_group_name: _Optional[str] = ..., incoming_tcp_ports: _Optional[_Iterable[int]] = ..., cluster_subnet_address_vec: _Optional[_Iterable[_Union[SubnetAddrMask, _Mapping]]] = ...) -> None: ...

class CreateSecurityGroupResult(_message.Message):
    __slots__ = ("security_group_id",)
    SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    security_group_id: str
    def __init__(self, security_group_id: _Optional[str] = ...) -> None: ...

class ModifySnapshotPermissionsArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id", "account_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    account_id: str
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class ModifySnapshotPermissionsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SSMSendCommandArg(_message.Message):
    __slots__ = ("region", "instance_ids", "document_name", "parameters", "comment")
    class Parameter(_message.Message):
        __slots__ = ("key", "values")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        key: str
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    REGION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    region: str
    instance_ids: _containers.RepeatedScalarFieldContainer[str]
    document_name: str
    parameters: _containers.RepeatedCompositeFieldContainer[SSMSendCommandArg.Parameter]
    comment: str
    def __init__(self, region: _Optional[str] = ..., instance_ids: _Optional[_Iterable[str]] = ..., document_name: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[SSMSendCommandArg.Parameter, _Mapping]]] = ..., comment: _Optional[str] = ...) -> None: ...

class SSMSendCommandResult(_message.Message):
    __slots__ = ("command_id",)
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    def __init__(self, command_id: _Optional[str] = ...) -> None: ...

class SSMGetCommandOutcomeArg(_message.Message):
    __slots__ = ("region", "command_id", "instance_id", "download_log_files", "is_windows")
    REGION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LOG_FILES_FIELD_NUMBER: _ClassVar[int]
    IS_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    region: str
    command_id: str
    instance_id: str
    download_log_files: bool
    is_windows: bool
    def __init__(self, region: _Optional[str] = ..., command_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., download_log_files: bool = ..., is_windows: bool = ...) -> None: ...

class SSMGetCommandOutcomeResult(_message.Message):
    __slots__ = ("command_status", "command_stdout", "command_stderr")
    COMMAND_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_STDOUT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_STDERR_FIELD_NUMBER: _ClassVar[int]
    command_status: str
    command_stdout: str
    command_stderr: str
    def __init__(self, command_status: _Optional[str] = ..., command_stdout: _Optional[str] = ..., command_stderr: _Optional[str] = ...) -> None: ...

class ModifyInstanceSecurityGroupsArg(_message.Message):
    __slots__ = ("security_group_id", "should_add_security_group", "region_name", "instance_id")
    SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ADD_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    security_group_id: str
    should_add_security_group: bool
    region_name: str
    instance_id: str
    def __init__(self, security_group_id: _Optional[str] = ..., should_add_security_group: bool = ..., region_name: _Optional[str] = ..., instance_id: _Optional[str] = ...) -> None: ...

class ModifyInstanceSecurityGroupsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Tag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetResourcesTagsArg(_message.Message):
    __slots__ = ("region_name", "resource_id_vec", "tag_vec")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    resource_id_vec: _containers.RepeatedScalarFieldContainer[str]
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, region_name: _Optional[str] = ..., resource_id_vec: _Optional[_Iterable[str]] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class SetResourcesTagsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSnapshotBlocksArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id", "base_snapshot_id", "max_results", "next_token", "starting_block_index")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STARTING_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    base_snapshot_id: str
    max_results: int
    next_token: str
    starting_block_index: int
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., base_snapshot_id: _Optional[str] = ..., max_results: _Optional[int] = ..., next_token: _Optional[str] = ..., starting_block_index: _Optional[int] = ...) -> None: ...

class GetSnapshotBlockArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id", "index", "token")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    index: int
    token: str
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., index: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class StartSnapshotArg(_message.Message):
    __slots__ = ("region_name", "volume_size_gb", "description", "is_encrypted", "kms_key_arn", "parent_snapshot_id", "tags_vec", "client_token", "timeout")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    PARENT_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    volume_size_gb: int
    description: str
    is_encrypted: bool
    kms_key_arn: str
    parent_snapshot_id: str
    tags_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    client_token: str
    timeout: int
    def __init__(self, region_name: _Optional[str] = ..., volume_size_gb: _Optional[int] = ..., description: _Optional[str] = ..., is_encrypted: bool = ..., kms_key_arn: _Optional[str] = ..., parent_snapshot_id: _Optional[str] = ..., tags_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., client_token: _Optional[str] = ..., timeout: _Optional[int] = ...) -> None: ...

class PutSnapshotBlockArg(_message.Message):
    __slots__ = ("region_name", "snapshot_id", "block_index", "checksum", "checksum_algorithm", "data_length")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    DATA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    snapshot_id: str
    block_index: int
    checksum: str
    checksum_algorithm: str
    data_length: int
    def __init__(self, region_name: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., block_index: _Optional[int] = ..., checksum: _Optional[str] = ..., checksum_algorithm: _Optional[str] = ..., data_length: _Optional[int] = ...) -> None: ...

class CompleteSnapshotArg(_message.Message):
    __slots__ = ("region_name", "changed_blocks_count", "snapshot_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANGED_BLOCKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    changed_blocks_count: int
    snapshot_id: str
    def __init__(self, region_name: _Optional[str] = ..., changed_blocks_count: _Optional[int] = ..., snapshot_id: _Optional[str] = ...) -> None: ...

class InstanceTypeInfo(_message.Message):
    __slots__ = ("supported_boot_modes_vec",)
    SUPPORTED_BOOT_MODES_VEC_FIELD_NUMBER: _ClassVar[int]
    supported_boot_modes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, supported_boot_modes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DescribeInstanceTypesArg(_message.Message):
    __slots__ = ("region_name", "instance_type")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    instance_type: str
    def __init__(self, region_name: _Optional[str] = ..., instance_type: _Optional[str] = ...) -> None: ...

class DescribeInstanceTypesResult(_message.Message):
    __slots__ = ("instance_type_info",)
    INSTANCE_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    instance_type_info: InstanceTypeInfo
    def __init__(self, instance_type_info: _Optional[_Union[InstanceTypeInfo, _Mapping]] = ...) -> None: ...

class S3BucketInfo(_message.Message):
    __slots__ = ("entity_proto", "bucket_tag_vec")
    ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_proto: _s3_pb2.Entity
    bucket_tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, entity_proto: _Optional[_Union[_s3_pb2.Entity, _Mapping]] = ..., bucket_tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class DescribeS3BucketsArg(_message.Message):
    __slots__ = ("region_name",)
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    def __init__(self, region_name: _Optional[str] = ...) -> None: ...

class DescribeS3BucketsResult(_message.Message):
    __slots__ = ("s3_bucket_info_vec",)
    S3_BUCKET_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    s3_bucket_info_vec: _containers.RepeatedCompositeFieldContainer[S3BucketInfo]
    def __init__(self, s3_bucket_info_vec: _Optional[_Iterable[_Union[S3BucketInfo, _Mapping]]] = ...) -> None: ...
