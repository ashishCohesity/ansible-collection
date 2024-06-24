from configs import cluster_config_pb2 as _cluster_config_pb2
from bifrost.server import server_config_pb2 as _server_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppStateProto(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppStateProto.Value]
        kInstallInProgress: _ClassVar[AppStateProto.Value]
        kInstallFailed: _ClassVar[AppStateProto.Value]
        kInstalled: _ClassVar[AppStateProto.Value]
        kUninstallInProgress: _ClassVar[AppStateProto.Value]
        kUninstallFailed: _ClassVar[AppStateProto.Value]
        kUninstalled: _ClassVar[AppStateProto.Value]
        kDownloadNotStarted: _ClassVar[AppStateProto.Value]
        kDownloadInProgress: _ClassVar[AppStateProto.Value]
        kDownloadComplete: _ClassVar[AppStateProto.Value]
        kDownloadFailed: _ClassVar[AppStateProto.Value]
    kNotSet: AppStateProto.Value
    kInstallInProgress: AppStateProto.Value
    kInstallFailed: AppStateProto.Value
    kInstalled: AppStateProto.Value
    kUninstallInProgress: AppStateProto.Value
    kUninstallFailed: AppStateProto.Value
    kUninstalled: AppStateProto.Value
    kDownloadNotStarted: AppStateProto.Value
    kDownloadInProgress: AppStateProto.Value
    kDownloadComplete: AppStateProto.Value
    kDownloadFailed: AppStateProto.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: AppStateProto.Value
    def __init__(self, value: _Optional[_Union[AppStateProto.Value, str]] = ...) -> None: ...

class AppAccessRole(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppAccessRole.Value]
        kAll: _ClassVar[AppAccessRole.Value]
        kAdmin: _ClassVar[AppAccessRole.Value]
    kNotSet: AppAccessRole.Value
    kAll: AppAccessRole.Value
    kAdmin: AppAccessRole.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: AppAccessRole.Value
    def __init__(self, value: _Optional[_Union[AppAccessRole.Value, str]] = ...) -> None: ...

class AppInstanceStateProto(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppInstanceStateProto.Value]
        kCreated: _ClassVar[AppInstanceStateProto.Value]
        kLaunched: _ClassVar[AppInstanceStateProto.Value]
        kPaused: _ClassVar[AppInstanceStateProto.Value]
        kTerminated: _ClassVar[AppInstanceStateProto.Value]
        kFailed: _ClassVar[AppInstanceStateProto.Value]
        kUpgrading: _ClassVar[AppInstanceStateProto.Value]
    kNotSet: AppInstanceStateProto.Value
    kCreated: AppInstanceStateProto.Value
    kLaunched: AppInstanceStateProto.Value
    kPaused: AppInstanceStateProto.Value
    kTerminated: AppInstanceStateProto.Value
    kFailed: AppInstanceStateProto.Value
    kUpgrading: AppInstanceStateProto.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: AppInstanceStateProto.Value
    def __init__(self, value: _Optional[_Union[AppInstanceStateProto.Value, str]] = ...) -> None: ...

class HealthStatusProto(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[HealthStatusProto.Value]
        kHealthy: _ClassVar[HealthStatusProto.Value]
        kUnHealthy: _ClassVar[HealthStatusProto.Value]
        kNotApplicable: _ClassVar[HealthStatusProto.Value]
    kNotSet: HealthStatusProto.Value
    kHealthy: HealthStatusProto.Value
    kUnHealthy: HealthStatusProto.Value
    kNotApplicable: HealthStatusProto.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: HealthStatusProto.Value
    def __init__(self, value: _Optional[_Union[HealthStatusProto.Value, str]] = ...) -> None: ...

class ComputeResourceInfo(_message.Message):
    __slots__ = ("name", "kind", "scale_type", "fixed_replicas", "min_replicas", "max_replicas", "share", "fraction")
    class ScaleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFixed: _ClassVar[ComputeResourceInfo.ScaleType]
        kDynamic: _ClassVar[ComputeResourceInfo.ScaleType]
    kFixed: ComputeResourceInfo.ScaleType
    kDynamic: ComputeResourceInfo.ScaleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCALE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXED_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: str
    scale_type: ComputeResourceInfo.ScaleType
    fixed_replicas: int
    min_replicas: int
    max_replicas: int
    share: int
    fraction: float
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., scale_type: _Optional[_Union[ComputeResourceInfo.ScaleType, str]] = ..., fixed_replicas: _Optional[int] = ..., min_replicas: _Optional[int] = ..., max_replicas: _Optional[int] = ..., share: _Optional[int] = ..., fraction: _Optional[float] = ...) -> None: ...

class AppConfigProto(_message.Message):
    __slots__ = ("compute_resource_info", "auto_scale")
    COMPUTE_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCALE_FIELD_NUMBER: _ClassVar[int]
    compute_resource_info: _containers.RepeatedCompositeFieldContainer[ComputeResourceInfo]
    auto_scale: bool
    def __init__(self, compute_resource_info: _Optional[_Iterable[_Union[ComputeResourceInfo, _Mapping]]] = ..., auto_scale: bool = ...) -> None: ...

class AppMetaInfoProto(_message.Message):
    __slots__ = ("name", "author", "dev_version", "description", "created_date", "last_modified_date", "icon_image", "access_role", "internal_version", "deployment_type", "app_config_proto", "deployment_parameters")
    class DeploymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAthenaYaml: _ClassVar[AppMetaInfoProto.DeploymentType]
        kHelmChart: _ClassVar[AppMetaInfoProto.DeploymentType]
    kAthenaYaml: AppMetaInfoProto.DeploymentType
    kHelmChart: AppMetaInfoProto.DeploymentType
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DEV_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    ICON_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    author: str
    dev_version: str
    description: str
    created_date: str
    last_modified_date: str
    icon_image: bytes
    access_role: AppAccessRole
    internal_version: str
    deployment_type: AppMetaInfoProto.DeploymentType
    app_config_proto: AppConfigProto
    deployment_parameters: str
    def __init__(self, name: _Optional[str] = ..., author: _Optional[str] = ..., dev_version: _Optional[str] = ..., description: _Optional[str] = ..., created_date: _Optional[str] = ..., last_modified_date: _Optional[str] = ..., icon_image: _Optional[bytes] = ..., access_role: _Optional[_Union[AppAccessRole, _Mapping]] = ..., internal_version: _Optional[str] = ..., deployment_type: _Optional[_Union[AppMetaInfoProto.DeploymentType, str]] = ..., app_config_proto: _Optional[_Union[AppConfigProto, _Mapping]] = ..., deployment_parameters: _Optional[str] = ...) -> None: ...

class AppPrivilegesProto(_message.Message):
    __slots__ = ("access",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppPrivilegesProto.Type]
        kReadAccess: _ClassVar[AppPrivilegesProto.Type]
        kReadWriteAccess: _ClassVar[AppPrivilegesProto.Type]
        kManagementAccess: _ClassVar[AppPrivilegesProto.Type]
        kAutoMountAccess: _ClassVar[AppPrivilegesProto.Type]
        kUnrestrictedAppUIAccess: _ClassVar[AppPrivilegesProto.Type]
        kAuditLogViewReadAccess: _ClassVar[AppPrivilegesProto.Type]
        kProtectedObjectAccess: _ClassVar[AppPrivilegesProto.Type]
    kNotSet: AppPrivilegesProto.Type
    kReadAccess: AppPrivilegesProto.Type
    kReadWriteAccess: AppPrivilegesProto.Type
    kManagementAccess: AppPrivilegesProto.Type
    kAutoMountAccess: AppPrivilegesProto.Type
    kUnrestrictedAppUIAccess: AppPrivilegesProto.Type
    kAuditLogViewReadAccess: AppPrivilegesProto.Type
    kProtectedObjectAccess: AppPrivilegesProto.Type
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    access: AppPrivilegesProto.Type
    def __init__(self, access: _Optional[_Union[AppPrivilegesProto.Type, str]] = ...) -> None: ...

class AppInstanceResourcesProto(_message.Message):
    __slots__ = ("memory_requests_quota_mb", "memory_limits_quota_mb", "cpu_requests_quota_millicores", "cpu_limits_quota_millicores", "memory_requests_usage_mb", "memory_limits_usage_mb", "cpu_requests_usage_millicores", "cpu_limits_usage_millicores", "num_pods", "num_nodes")
    MEMORY_REQUESTS_QUOTA_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMITS_QUOTA_MB_FIELD_NUMBER: _ClassVar[int]
    CPU_REQUESTS_QUOTA_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMITS_QUOTA_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_REQUESTS_USAGE_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMITS_USAGE_MB_FIELD_NUMBER: _ClassVar[int]
    CPU_REQUESTS_USAGE_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMITS_USAGE_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    NUM_PODS_FIELD_NUMBER: _ClassVar[int]
    NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    memory_requests_quota_mb: int
    memory_limits_quota_mb: int
    cpu_requests_quota_millicores: int
    cpu_limits_quota_millicores: int
    memory_requests_usage_mb: int
    memory_limits_usage_mb: int
    cpu_requests_usage_millicores: int
    cpu_limits_usage_millicores: int
    num_pods: int
    num_nodes: int
    def __init__(self, memory_requests_quota_mb: _Optional[int] = ..., memory_limits_quota_mb: _Optional[int] = ..., cpu_requests_quota_millicores: _Optional[int] = ..., cpu_limits_quota_millicores: _Optional[int] = ..., memory_requests_usage_mb: _Optional[int] = ..., memory_limits_usage_mb: _Optional[int] = ..., cpu_requests_usage_millicores: _Optional[int] = ..., cpu_limits_usage_millicores: _Optional[int] = ..., num_pods: _Optional[int] = ..., num_nodes: _Optional[int] = ...) -> None: ...

class QosTierProto(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[QosTierProto.Value]
        kLow: _ClassVar[QosTierProto.Value]
        kMedium: _ClassVar[QosTierProto.Value]
        kHigh: _ClassVar[QosTierProto.Value]
        kMax: _ClassVar[QosTierProto.Value]
    kNotSet: QosTierProto.Value
    kLow: QosTierProto.Value
    kMedium: QosTierProto.Value
    kHigh: QosTierProto.Value
    kMax: QosTierProto.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: QosTierProto.Value
    def __init__(self, value: _Optional[_Union[QosTierProto.Value, str]] = ...) -> None: ...

class ViewPrivilegesProto(_message.Message):
    __slots__ = ("privileges_type", "view_ids")
    class PrivilegesType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[ViewPrivilegesProto.PrivilegesType]
        kNone: _ClassVar[ViewPrivilegesProto.PrivilegesType]
        kAll: _ClassVar[ViewPrivilegesProto.PrivilegesType]
        kSpecific: _ClassVar[ViewPrivilegesProto.PrivilegesType]
    kNotSet: ViewPrivilegesProto.PrivilegesType
    kNone: ViewPrivilegesProto.PrivilegesType
    kAll: ViewPrivilegesProto.PrivilegesType
    kSpecific: ViewPrivilegesProto.PrivilegesType
    PRIVILEGES_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_IDS_FIELD_NUMBER: _ClassVar[int]
    privileges_type: ViewPrivilegesProto.PrivilegesType
    view_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, privileges_type: _Optional[_Union[ViewPrivilegesProto.PrivilegesType, str]] = ..., view_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ProtectedObjectPrivilegesProto(_message.Message):
    __slots__ = ("privileges_type", "protection_source_ids")
    class PrivilegesType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[ProtectedObjectPrivilegesProto.PrivilegesType]
        kNone: _ClassVar[ProtectedObjectPrivilegesProto.PrivilegesType]
        kAll: _ClassVar[ProtectedObjectPrivilegesProto.PrivilegesType]
        kSpecific: _ClassVar[ProtectedObjectPrivilegesProto.PrivilegesType]
    kNotSet: ProtectedObjectPrivilegesProto.PrivilegesType
    kNone: ProtectedObjectPrivilegesProto.PrivilegesType
    kAll: ProtectedObjectPrivilegesProto.PrivilegesType
    kSpecific: ProtectedObjectPrivilegesProto.PrivilegesType
    PRIVILEGES_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    privileges_type: ProtectedObjectPrivilegesProto.PrivilegesType
    protection_source_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, privileges_type: _Optional[_Union[ProtectedObjectPrivilegesProto.PrivilegesType, str]] = ..., protection_source_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class AppInstanceSettingsProto(_message.Message):
    __slots__ = ("qos_tier", "read_view_privileges", "read_write_view_privileges", "protected_object_privileges", "vm_num_replicas_list")
    QOS_TIER_FIELD_NUMBER: _ClassVar[int]
    READ_VIEW_PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    READ_WRITE_VIEW_PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_OBJECT_PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    VM_NUM_REPLICAS_LIST_FIELD_NUMBER: _ClassVar[int]
    qos_tier: QosTierProto
    read_view_privileges: ViewPrivilegesProto
    read_write_view_privileges: ViewPrivilegesProto
    protected_object_privileges: ProtectedObjectPrivilegesProto
    vm_num_replicas_list: _containers.RepeatedCompositeFieldContainer[VmNumReplicas]
    def __init__(self, qos_tier: _Optional[_Union[QosTierProto, _Mapping]] = ..., read_view_privileges: _Optional[_Union[ViewPrivilegesProto, _Mapping]] = ..., read_write_view_privileges: _Optional[_Union[ViewPrivilegesProto, _Mapping]] = ..., protected_object_privileges: _Optional[_Union[ProtectedObjectPrivilegesProto, _Mapping]] = ..., vm_num_replicas_list: _Optional[_Iterable[_Union[VmNumReplicas, _Mapping]]] = ...) -> None: ...

class VmNumReplicas(_message.Message):
    __slots__ = ("vm_name", "num_replicas")
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    num_replicas: int
    def __init__(self, vm_name: _Optional[str] = ..., num_replicas: _Optional[int] = ...) -> None: ...

class VmNameInfoProto(_message.Message):
    __slots__ = ("vm_name", "ui_name")
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    UI_NAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    ui_name: str
    def __init__(self, vm_name: _Optional[str] = ..., ui_name: _Optional[str] = ...) -> None: ...

class UserInformation(_message.Message):
    __slots__ = ("sid_vec", "tenant_id_vec", "sid", "tenant_id", "user_name", "user_domain", "roles")
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    sid: str
    tenant_id: str
    user_name: str
    user_domain: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., sid: _Optional[str] = ..., tenant_id: _Optional[str] = ..., user_name: _Optional[str] = ..., user_domain: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class AppInstanceTokenProto(_message.Message):
    __slots__ = ("type", "value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppInstanceTokenProto.Type]
        kAuthenticationToken: _ClassVar[AppInstanceTokenProto.Type]
        kAccessToken: _ClassVar[AppInstanceTokenProto.Type]
    kNotSet: AppInstanceTokenProto.Type
    kAuthenticationToken: AppInstanceTokenProto.Type
    kAccessToken: AppInstanceTokenProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: AppInstanceTokenProto.Type
    value: bytes
    def __init__(self, type: _Optional[_Union[AppInstanceTokenProto.Type, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class MountPointInfoProto(_message.Message):
    __slots__ = ("mount_path", "remove_directory")
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    mount_path: str
    remove_directory: bool
    def __init__(self, mount_path: _Optional[str] = ..., remove_directory: bool = ...) -> None: ...

class VolumeInfoProto(_message.Message):
    __slots__ = ("volume_label", "volume_capacity_bytes", "status", "details", "initializing_percentage", "view_name", "lun", "volume_identifier", "retry_on_failure")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[VolumeInfoProto.Status]
        kInitializing: _ClassVar[VolumeInfoProto.Status]
        kVolumeCreated: _ClassVar[VolumeInfoProto.Status]
        kAvailable: _ClassVar[VolumeInfoProto.Status]
        kBound: _ClassVar[VolumeInfoProto.Status]
        kFailed: _ClassVar[VolumeInfoProto.Status]
    kNotSet: VolumeInfoProto.Status
    kInitializing: VolumeInfoProto.Status
    kVolumeCreated: VolumeInfoProto.Status
    kAvailable: VolumeInfoProto.Status
    kBound: VolumeInfoProto.Status
    kFailed: VolumeInfoProto.Status
    VOLUME_LABEL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZING_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    VOLUME_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RETRY_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    volume_label: str
    volume_capacity_bytes: int
    status: VolumeInfoProto.Status
    details: str
    initializing_percentage: int
    view_name: str
    lun: int
    volume_identifier: str
    retry_on_failure: bool
    def __init__(self, volume_label: _Optional[str] = ..., volume_capacity_bytes: _Optional[int] = ..., status: _Optional[_Union[VolumeInfoProto.Status, str]] = ..., details: _Optional[str] = ..., initializing_percentage: _Optional[int] = ..., view_name: _Optional[str] = ..., lun: _Optional[int] = ..., volume_identifier: _Optional[str] = ..., retry_on_failure: bool = ...) -> None: ...

class AppViewInfoProto(_message.Message):
    __slots__ = ("identifier", "view_box_id", "view_name", "source_view_name", "status", "details", "initializing_percentage", "retry_on_failure")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppViewInfoProto.Status]
        kInitializing: _ClassVar[AppViewInfoProto.Status]
        kCreated: _ClassVar[AppViewInfoProto.Status]
        kFailed: _ClassVar[AppViewInfoProto.Status]
    kNotSet: AppViewInfoProto.Status
    kInitializing: AppViewInfoProto.Status
    kCreated: AppViewInfoProto.Status
    kFailed: AppViewInfoProto.Status
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZING_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    RETRY_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    view_box_id: int
    view_name: str
    source_view_name: str
    status: AppViewInfoProto.Status
    details: str
    initializing_percentage: int
    retry_on_failure: bool
    def __init__(self, identifier: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., source_view_name: _Optional[str] = ..., status: _Optional[_Union[AppViewInfoProto.Status, str]] = ..., details: _Optional[str] = ..., initializing_percentage: _Optional[int] = ..., retry_on_failure: bool = ...) -> None: ...

class VMDiskInfoProto(_message.Message):
    __slots__ = ("disk_type", "disk_image_name", "disk_size", "pvc_name", "volume_type", "device_name")
    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[VMDiskInfoProto.DiskType]
        kBoot: _ClassVar[VMDiskInfoProto.DiskType]
        kData: _ClassVar[VMDiskInfoProto.DiskType]
    kNotSet: VMDiskInfoProto.DiskType
    kBoot: VMDiskInfoProto.DiskType
    kData: VMDiskInfoProto.DiskType
    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVolumeTypeNotSet: _ClassVar[VMDiskInfoProto.VolumeType]
        kNfs: _ClassVar[VMDiskInfoProto.VolumeType]
        kIscsi: _ClassVar[VMDiskInfoProto.VolumeType]
    kVolumeTypeNotSet: VMDiskInfoProto.VolumeType
    kNfs: VMDiskInfoProto.VolumeType
    kIscsi: VMDiskInfoProto.VolumeType
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    PVC_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    disk_type: VMDiskInfoProto.DiskType
    disk_image_name: str
    disk_size: int
    pvc_name: str
    volume_type: VMDiskInfoProto.VolumeType
    device_name: str
    def __init__(self, disk_type: _Optional[_Union[VMDiskInfoProto.DiskType, str]] = ..., disk_image_name: _Optional[str] = ..., disk_size: _Optional[int] = ..., pvc_name: _Optional[str] = ..., volume_type: _Optional[_Union[VMDiskInfoProto.VolumeType, str]] = ..., device_name: _Optional[str] = ...) -> None: ...

class NodePortInfoProto(_message.Message):
    __slots__ = ("tag", "env_var", "nodeport", "is_ui_nodeport", "service_name")
    class Tag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefault: _ClassVar[NodePortInfoProto.Tag]
        kHttp: _ClassVar[NodePortInfoProto.Tag]
        kHttps: _ClassVar[NodePortInfoProto.Tag]
        kSsh: _ClassVar[NodePortInfoProto.Tag]
    kDefault: NodePortInfoProto.Tag
    kHttp: NodePortInfoProto.Tag
    kHttps: NodePortInfoProto.Tag
    kSsh: NodePortInfoProto.Tag
    TAG_FIELD_NUMBER: _ClassVar[int]
    ENV_VAR_FIELD_NUMBER: _ClassVar[int]
    NODEPORT_FIELD_NUMBER: _ClassVar[int]
    IS_UI_NODEPORT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    tag: NodePortInfoProto.Tag
    env_var: str
    nodeport: int
    is_ui_nodeport: bool
    service_name: str
    def __init__(self, tag: _Optional[_Union[NodePortInfoProto.Tag, str]] = ..., env_var: _Optional[str] = ..., nodeport: _Optional[int] = ..., is_ui_nodeport: bool = ..., service_name: _Optional[str] = ...) -> None: ...

class UserSshKeyInfo(_message.Message):
    __slots__ = ("username", "public_ssh_key", "private_ssh_key", "base64_user_data")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE64_USER_DATA_FIELD_NUMBER: _ClassVar[int]
    username: str
    public_ssh_key: bytes
    private_ssh_key: bytes
    base64_user_data: str
    def __init__(self, username: _Optional[str] = ..., public_ssh_key: _Optional[bytes] = ..., private_ssh_key: _Optional[bytes] = ..., base64_user_data: _Optional[str] = ...) -> None: ...

class VMInfoProto(_message.Message):
    __slots__ = ("name", "nodeport_info", "health_status", "health_detail", "ssh_key_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODEPORT_INFO_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_DETAIL_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    nodeport_info: _containers.RepeatedCompositeFieldContainer[NodePortInfoProto]
    health_status: HealthStatusProto
    health_detail: str
    ssh_key_info: UserSshKeyInfo
    def __init__(self, name: _Optional[str] = ..., nodeport_info: _Optional[_Iterable[_Union[NodePortInfoProto, _Mapping]]] = ..., health_status: _Optional[_Union[HealthStatusProto, _Mapping]] = ..., health_detail: _Optional[str] = ..., ssh_key_info: _Optional[_Union[UserSshKeyInfo, _Mapping]] = ...) -> None: ...

class VMGroupProto(_message.Message):
    __slots__ = ("name", "vm_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_info: _containers.RepeatedCompositeFieldContainer[VMInfoProto]
    def __init__(self, name: _Optional[str] = ..., vm_info: _Optional[_Iterable[_Union[VMInfoProto, _Mapping]]] = ...) -> None: ...

class PodNetworkingKeyProto(_message.Message):
    __slots__ = ("namespace_name", "pod_name", "network_uuid", "container_id")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    pod_name: str
    network_uuid: str
    container_id: str
    def __init__(self, namespace_name: _Optional[str] = ..., pod_name: _Optional[str] = ..., network_uuid: _Optional[str] = ..., container_id: _Optional[str] = ...) -> None: ...

class PodNetworkingInfoProto(_message.Message):
    __slots__ = ("ip_address_type", "ip_address", "mac_address", "port_identifier", "container_id")
    class IPAddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[PodNetworkingInfoProto.IPAddressType]
        kInternalNetwork: _ClassVar[PodNetworkingInfoProto.IPAddressType]
        kExternalNetwork: _ClassVar[PodNetworkingInfoProto.IPAddressType]
    kNotSet: PodNetworkingInfoProto.IPAddressType
    kInternalNetwork: PodNetworkingInfoProto.IPAddressType
    kExternalNetwork: PodNetworkingInfoProto.IPAddressType
    IP_ADDRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    ip_address_type: PodNetworkingInfoProto.IPAddressType
    ip_address: str
    mac_address: str
    port_identifier: str
    container_id: str
    def __init__(self, ip_address_type: _Optional[_Union[PodNetworkingInfoProto.IPAddressType, str]] = ..., ip_address: _Optional[str] = ..., mac_address: _Optional[str] = ..., port_identifier: _Optional[str] = ..., container_id: _Optional[str] = ...) -> None: ...

class AxonNetworkAccessInfoProto(_message.Message):
    __slots__ = ("token", "access_control_type")
    class AccessControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kAppInstanceAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kAppInstanceWithExternalAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kHostAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kHostWithExternalAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kK8sSystemPodAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kBifrostTenantAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
        kBifrostHostAccess: _ClassVar[AxonNetworkAccessInfoProto.AccessControlType]
    kNotSet: AxonNetworkAccessInfoProto.AccessControlType
    kAppInstanceAccess: AxonNetworkAccessInfoProto.AccessControlType
    kAppInstanceWithExternalAccess: AxonNetworkAccessInfoProto.AccessControlType
    kHostAccess: AxonNetworkAccessInfoProto.AccessControlType
    kHostWithExternalAccess: AxonNetworkAccessInfoProto.AccessControlType
    kK8sSystemPodAccess: AxonNetworkAccessInfoProto.AccessControlType
    kBifrostTenantAccess: AxonNetworkAccessInfoProto.AccessControlType
    kBifrostHostAccess: AxonNetworkAccessInfoProto.AccessControlType
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    token: str
    access_control_type: AxonNetworkAccessInfoProto.AccessControlType
    def __init__(self, token: _Optional[str] = ..., access_control_type: _Optional[_Union[AxonNetworkAccessInfoProto.AccessControlType, str]] = ...) -> None: ...

class ExternalNetworkInfoProto(_message.Message):
    __slots__ = ("vlan_id", "vlan_network_name", "axon_network_name", "axon_provider_net", "interface_group", "changes_per_instance", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    VLAN_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    AXON_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    AXON_PROVIDER_NET_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    CHANGES_PER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    vlan_id: int
    vlan_network_name: str
    axon_network_name: str
    axon_provider_net: bool
    interface_group: str
    changes_per_instance: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, vlan_id: _Optional[int] = ..., vlan_network_name: _Optional[str] = ..., axon_network_name: _Optional[str] = ..., axon_provider_net: bool = ..., interface_group: _Optional[str] = ..., changes_per_instance: bool = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class BifrostConfig(_message.Message):
    __slots__ = ("tenant_id", "server_config", "replica_count")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    server_config: _server_config_pb2.ServerConfigProto
    replica_count: int
    def __init__(self, tenant_id: _Optional[str] = ..., server_config: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., replica_count: _Optional[int] = ...) -> None: ...
