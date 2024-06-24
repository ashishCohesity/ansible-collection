from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.cloud import cloud_pb2 as _cloud_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from magneto.connectors.gcp import gcp_param_pb2 as _gcp_param_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersistentDisk(_message.Message):
    __slots__ = ("key", "disk_device_info", "snapshot_id", "snapshot_creation_time_usecs", "snapshot_disk_info", "status", "delta_type", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "error", "vm_disk_relative_path")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[PersistentDisk.Status]
        kSnapshotCreated: _ClassVar[PersistentDisk.Status]
        kSnapshotFinished: _ClassVar[PersistentDisk.Status]
        kSnapshotAttached: _ClassVar[PersistentDisk.Status]
        kSubTasksFinished: _ClassVar[PersistentDisk.Status]
        kSnapshotDetached: _ClassVar[PersistentDisk.Status]
        kDiskDeleted: _ClassVar[PersistentDisk.Status]
        kSnapshotDeleted: _ClassVar[PersistentDisk.Status]
    kStarted: PersistentDisk.Status
    kSnapshotCreated: PersistentDisk.Status
    kSnapshotFinished: PersistentDisk.Status
    kSnapshotAttached: PersistentDisk.Status
    kSubTasksFinished: PersistentDisk.Status
    kSnapshotDetached: PersistentDisk.Status
    kDiskDeleted: PersistentDisk.Status
    kSnapshotDeleted: PersistentDisk.Status
    class SnapshotDiskInfo(_message.Message):
        __slots__ = ("snapshot_persistent_disk_name", "proxy_info")
        SNAPSHOT_PERSISTENT_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
        snapshot_persistent_disk_name: str
        proxy_info: _proxy_pb2.ProxyInfo
        def __init__(self, snapshot_persistent_disk_name: _Optional[str] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ...) -> None: ...
    GCP_PERSISTENT_DISK_FIELD_NUMBER: _ClassVar[int]
    gcp_persistent_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    key: int
    disk_device_info: _gcp_param_pb2.DiskDeviceInfo
    snapshot_id: str
    snapshot_creation_time_usecs: int
    snapshot_disk_info: PersistentDisk.SnapshotDiskInfo
    status: PersistentDisk.Status
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    error: _error_pb2.ErrorProto
    vm_disk_relative_path: str
    def __init__(self, key: _Optional[int] = ..., disk_device_info: _Optional[_Union[_gcp_param_pb2.DiskDeviceInfo, _Mapping]] = ..., snapshot_id: _Optional[str] = ..., snapshot_creation_time_usecs: _Optional[int] = ..., snapshot_disk_info: _Optional[_Union[PersistentDisk.SnapshotDiskInfo, _Mapping]] = ..., status: _Optional[_Union[PersistentDisk.Status, str]] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_disk_relative_path: _Optional[str] = ...) -> None: ...

class VMNetworkInterface(_message.Message):
    __slots__ = ("network_ip", "name", "vpc_name", "subnet_name", "access_configs_vec")
    class VMNetworkInterfaceAccessConfigs(_message.Message):
        __slots__ = ("type", "name", "nat_ip", "network_tier")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        NAT_IP_FIELD_NUMBER: _ClassVar[int]
        NETWORK_TIER_FIELD_NUMBER: _ClassVar[int]
        type: str
        name: str
        nat_ip: str
        network_tier: str
        def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., nat_ip: _Optional[str] = ..., network_tier: _Optional[str] = ...) -> None: ...
    NETWORK_IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONFIGS_VEC_FIELD_NUMBER: _ClassVar[int]
    network_ip: str
    name: str
    vpc_name: str
    subnet_name: str
    access_configs_vec: _containers.RepeatedCompositeFieldContainer[VMNetworkInterface.VMNetworkInterfaceAccessConfigs]
    def __init__(self, network_ip: _Optional[str] = ..., name: _Optional[str] = ..., vpc_name: _Optional[str] = ..., subnet_name: _Optional[str] = ..., access_configs_vec: _Optional[_Iterable[_Union[VMNetworkInterface.VMNetworkInterfaceAccessConfigs, _Mapping]]] = ...) -> None: ...

class VMDisk(_message.Message):
    __slots__ = ("id", "name", "is_bootable", "mode", "description", "status", "source", "auto_delete", "interface", "type", "device_name", "region", "replica_zones", "size_gb", "licenses", "guest_os_features", "disk_encryption_key", "labels_map")
    class GuestOsFeatures(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str
        def __init__(self, type: _Optional[str] = ...) -> None: ...
    class DiskEncryptionKey(_message.Message):
        __slots__ = ("kms_key_name",)
        KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        kms_key_name: str
        def __init__(self, kms_key_name: _Optional[str] = ...) -> None: ...
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURES_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    is_bootable: bool
    mode: str
    description: str
    status: str
    source: str
    auto_delete: bool
    interface: str
    type: str
    device_name: str
    region: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    size_gb: int
    licenses: _containers.RepeatedScalarFieldContainer[str]
    guest_os_features: _containers.RepeatedCompositeFieldContainer[VMDisk.GuestOsFeatures]
    disk_encryption_key: VMDisk.DiskEncryptionKey
    labels_map: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., is_bootable: bool = ..., mode: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., source: _Optional[str] = ..., auto_delete: bool = ..., interface: _Optional[str] = ..., type: _Optional[str] = ..., device_name: _Optional[str] = ..., region: _Optional[str] = ..., replica_zones: _Optional[_Iterable[str]] = ..., size_gb: _Optional[int] = ..., licenses: _Optional[_Iterable[str]] = ..., guest_os_features: _Optional[_Iterable[_Union[VMDisk.GuestOsFeatures, _Mapping]]] = ..., disk_encryption_key: _Optional[_Union[VMDisk.DiskEncryptionKey, _Mapping]] = ..., labels_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VMMetadata(_message.Message):
    __slots__ = ("fingerprint", "items")
    class VMMetadataKeyValue(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    items: _containers.RepeatedCompositeFieldContainer[VMMetadata.VMMetadataKeyValue]
    def __init__(self, fingerprint: _Optional[str] = ..., items: _Optional[_Iterable[_Union[VMMetadata.VMMetadataKeyValue, _Mapping]]] = ...) -> None: ...

class Scheduling(_message.Message):
    __slots__ = ("automatic_restart", "on_host_maintenance", "preemptible")
    AUTOMATIC_RESTART_FIELD_NUMBER: _ClassVar[int]
    ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    automatic_restart: bool
    on_host_maintenance: str
    preemptible: bool
    def __init__(self, automatic_restart: bool = ..., on_host_maintenance: _Optional[str] = ..., preemptible: bool = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ("email", "scopes")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ...) -> None: ...

class VMInfo(_message.Message):
    __slots__ = ("id", "name", "project_id", "description", "status", "status_message", "zone", "region", "type", "vm_network_interfaces_vec", "vm_metadata", "vm_disks_vec", "vm_tags", "labels_map", "deletion_protection", "can_ip_forward", "scheduling", "service_accounts")
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_NETWORK_INTERFACES_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_METADATA_FIELD_NUMBER: _ClassVar[int]
    VM_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_TAGS_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    project_id: str
    description: str
    status: str
    status_message: str
    zone: str
    region: str
    type: str
    vm_network_interfaces_vec: _containers.RepeatedCompositeFieldContainer[VMNetworkInterface]
    vm_metadata: VMMetadata
    vm_disks_vec: _containers.RepeatedCompositeFieldContainer[VMDisk]
    vm_tags: _containers.RepeatedScalarFieldContainer[str]
    labels_map: _containers.ScalarMap[str, str]
    deletion_protection: bool
    can_ip_forward: bool
    scheduling: Scheduling
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., project_id: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., status_message: _Optional[str] = ..., zone: _Optional[str] = ..., region: _Optional[str] = ..., type: _Optional[str] = ..., vm_network_interfaces_vec: _Optional[_Iterable[_Union[VMNetworkInterface, _Mapping]]] = ..., vm_metadata: _Optional[_Union[VMMetadata, _Mapping]] = ..., vm_disks_vec: _Optional[_Iterable[_Union[VMDisk, _Mapping]]] = ..., vm_tags: _Optional[_Iterable[str]] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., deletion_protection: bool = ..., can_ip_forward: bool = ..., scheduling: _Optional[_Union[Scheduling, _Mapping]] = ..., service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("vm_info", "persistent_disks_vec")
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_info: VMInfo
    persistent_disks_vec: _containers.RepeatedCompositeFieldContainer[PersistentDisk]
    def __init__(self, vm_info: _Optional[_Union[VMInfo, _Mapping]] = ..., persistent_disks_vec: _Optional[_Iterable[_Union[PersistentDisk, _Mapping]]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "source_vm_info", "status", "disks", "sub_tasks_vec", "error", "snapshot_deletion_error", "quiesced", "sub_file_size_mb", "region", "zone", "subnet", "multiple_subnet_enabled")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kVMInfoFetched: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotInitialized: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kVMInfoFetched: SnapshotInfo.Status
    kCreateSnapshotInitialized: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    GCP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_SUBNET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    source_vm_info: VMInfo
    status: SnapshotInfo.Status
    disks: _containers.RepeatedCompositeFieldContainer[PersistentDisk]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    quiesced: bool
    sub_file_size_mb: int
    region: str
    zone: str
    subnet: str
    multiple_subnet_enabled: bool
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., source_vm_info: _Optional[_Union[VMInfo, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., disks: _Optional[_Iterable[_Union[PersistentDisk, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., quiesced: bool = ..., sub_file_size_mb: _Optional[int] = ..., region: _Optional[str] = ..., zone: _Optional[str] = ..., subnet: _Optional[str] = ..., multiple_subnet_enabled: bool = ...) -> None: ...

class CloudDeployEntityInfo(_message.Message):
    __slots__ = ("vm_info", "common_info")
    class DiskInfo(_message.Message):
        __slots__ = ("vm_disk_relative_path", "is_boot_disk", "snapshot_name", "copy_disk_name", "restored_disk_name", "restored_disk", "disk_device_info")
        VM_DISK_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        IS_BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
        COPY_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        RESTORED_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        RESTORED_DISK_FIELD_NUMBER: _ClassVar[int]
        DISK_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
        vm_disk_relative_path: str
        is_boot_disk: bool
        snapshot_name: str
        copy_disk_name: str
        restored_disk_name: str
        restored_disk: PersistentDisk
        disk_device_info: _gcp_param_pb2.DiskDeviceInfo
        def __init__(self, vm_disk_relative_path: _Optional[str] = ..., is_boot_disk: bool = ..., snapshot_name: _Optional[str] = ..., copy_disk_name: _Optional[str] = ..., restored_disk_name: _Optional[str] = ..., restored_disk: _Optional[_Union[PersistentDisk, _Mapping]] = ..., disk_device_info: _Optional[_Union[_gcp_param_pb2.DiskDeviceInfo, _Mapping]] = ...) -> None: ...
    class VMInfo(_message.Message):
        __slots__ = ("name", "restored_instance_name", "project_id", "disk_info_map", "boot_disk_name", "vm_config", "region", "zone", "subnet")
        class DiskInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: CloudDeployEntityInfo.DiskInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CloudDeployEntityInfo.DiskInfo, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESTORED_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        ZONE_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        name: str
        restored_instance_name: str
        project_id: str
        disk_info_map: _containers.MessageMap[int, CloudDeployEntityInfo.DiskInfo]
        boot_disk_name: str
        vm_config: VMConfig
        region: str
        zone: str
        subnet: str
        def __init__(self, name: _Optional[str] = ..., restored_instance_name: _Optional[str] = ..., project_id: _Optional[str] = ..., disk_info_map: _Optional[_Mapping[int, CloudDeployEntityInfo.DiskInfo]] = ..., boot_disk_name: _Optional[str] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., region: _Optional[str] = ..., zone: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...
    GCP_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_restore_entity_info: _descriptor.FieldDescriptor
    GCP_CLOUD_DEPLOY_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_cloud_deploy_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: CloudDeployEntityInfo.VMInfo
    common_info: _cloud_pb2.CloudEntityCommonInfo
    def __init__(self, vm_info: _Optional[_Union[CloudDeployEntityInfo.VMInfo, _Mapping]] = ..., common_info: _Optional[_Union[_cloud_pb2.CloudEntityCommonInfo, _Mapping]] = ...) -> None: ...

class CloudDeployInfo(_message.Message):
    __slots__ = ("status", "error", "view_deletion_error", "sub_tasks_vec", "total_bytes_to_write_to_source", "permit_on_restore_region", "multiple_subnet_enabled")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CloudDeployInfo.Status]
        kCloned: _ClassVar[CloudDeployInfo.Status]
        kVMInfoFetched: _ClassVar[CloudDeployInfo.Status]
        kPermitGranted: _ClassVar[CloudDeployInfo.Status]
        kDisksAttached: _ClassVar[CloudDeployInfo.Status]
        kSubTasksCreated: _ClassVar[CloudDeployInfo.Status]
        kSubTasksFinished: _ClassVar[CloudDeployInfo.Status]
        kSnapshotsCreated: _ClassVar[CloudDeployInfo.Status]
        kDisksRestored: _ClassVar[CloudDeployInfo.Status]
        kVMCreated: _ClassVar[CloudDeployInfo.Status]
        kEndRestoreFinished: _ClassVar[CloudDeployInfo.Status]
        kFinished: _ClassVar[CloudDeployInfo.Status]
    kStarted: CloudDeployInfo.Status
    kCloned: CloudDeployInfo.Status
    kVMInfoFetched: CloudDeployInfo.Status
    kPermitGranted: CloudDeployInfo.Status
    kDisksAttached: CloudDeployInfo.Status
    kSubTasksCreated: CloudDeployInfo.Status
    kSubTasksFinished: CloudDeployInfo.Status
    kSnapshotsCreated: CloudDeployInfo.Status
    kDisksRestored: CloudDeployInfo.Status
    kVMCreated: CloudDeployInfo.Status
    kEndRestoreFinished: CloudDeployInfo.Status
    kFinished: CloudDeployInfo.Status
    GCP_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_restore_info: _descriptor.FieldDescriptor
    GCP_CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_cloud_deploy_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMIT_ON_RESTORE_REGION_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_SUBNET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    status: CloudDeployInfo.Status
    error: _error_pb2.ErrorProto
    view_deletion_error: _error_pb2.ErrorProto
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    total_bytes_to_write_to_source: int
    permit_on_restore_region: bool
    multiple_subnet_enabled: bool
    def __init__(self, status: _Optional[_Union[CloudDeployInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., permit_on_restore_region: bool = ..., multiple_subnet_enabled: bool = ...) -> None: ...

class GcpVMRestoreSubTaskInfo(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[GcpVMRestoreSubTaskInfo.Status]
        kDiskCopied: _ClassVar[GcpVMRestoreSubTaskInfo.Status]
        kDiskRestored: _ClassVar[GcpVMRestoreSubTaskInfo.Status]
        kProxyVMDiskDeleted: _ClassVar[GcpVMRestoreSubTaskInfo.Status]
    kStarted: GcpVMRestoreSubTaskInfo.Status
    kDiskCopied: GcpVMRestoreSubTaskInfo.Status
    kDiskRestored: GcpVMRestoreSubTaskInfo.Status
    kProxyVMDiskDeleted: GcpVMRestoreSubTaskInfo.Status
    GCP_VM_RESTORE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_vm_restore_sub_task_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: GcpVMRestoreSubTaskInfo.Status
    error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[GcpVMRestoreSubTaskInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("server_vm_info", "username", "public_key", "private_key", "proxy_info", "copy_disk_name", "snapshot_name", "user_disk_name", "user_disk_device_name", "https_trigger_url", "file_batches", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreEnvironmentInfo.Status]
        kVMInfoFetched: _ClassVar[RestoreEnvironmentInfo.Status]
    kStarted: RestoreEnvironmentInfo.Status
    kVMInfoFetched: RestoreEnvironmentInfo.Status
    class FileBatch(_message.Message):
        __slots__ = ("batch_number", "absolute_file_paths", "processed")
        BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
        PROCESSED_FIELD_NUMBER: _ClassVar[int]
        batch_number: int
        absolute_file_paths: _containers.RepeatedScalarFieldContainer[str]
        processed: bool
        def __init__(self, batch_number: _Optional[int] = ..., absolute_file_paths: _Optional[_Iterable[str]] = ..., processed: bool = ...) -> None: ...
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    COPY_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DISK_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    HTTPS_TRIGGER_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_BATCHES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    server_vm_info: VMInfo
    username: str
    public_key: str
    private_key: str
    proxy_info: _proxy_pb2.ProxyInfo
    copy_disk_name: str
    snapshot_name: str
    user_disk_name: str
    user_disk_device_name: str
    https_trigger_url: str
    file_batches: _containers.RepeatedCompositeFieldContainer[RestoreEnvironmentInfo.FileBatch]
    status: RestoreEnvironmentInfo.Status
    def __init__(self, server_vm_info: _Optional[_Union[VMInfo, _Mapping]] = ..., username: _Optional[str] = ..., public_key: _Optional[str] = ..., private_key: _Optional[str] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ..., copy_disk_name: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., user_disk_name: _Optional[str] = ..., user_disk_device_name: _Optional[str] = ..., https_trigger_url: _Optional[str] = ..., file_batches: _Optional[_Iterable[_Union[RestoreEnvironmentInfo.FileBatch, _Mapping]]] = ..., status: _Optional[_Union[RestoreEnvironmentInfo.Status, str]] = ...) -> None: ...
