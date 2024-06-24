from nexus.halo.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HaloUrisProto(_message.Message):
    __slots__ = ("halo_port", "base_uri", "api_version", "packages_uri", "package_download_uri", "list_notified_clusters_uri", "update_notified_clusters_uri")
    HALO_PORT_FIELD_NUMBER: _ClassVar[int]
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_URI_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_DOWNLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    LIST_NOTIFIED_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_NOTIFIED_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    halo_port: int
    base_uri: str
    api_version: str
    packages_uri: str
    package_download_uri: str
    list_notified_clusters_uri: str
    update_notified_clusters_uri: str
    def __init__(self, halo_port: _Optional[int] = ..., base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., packages_uri: _Optional[str] = ..., package_download_uri: _Optional[str] = ..., list_notified_clusters_uri: _Optional[str] = ..., update_notified_clusters_uri: _Optional[str] = ...) -> None: ...

class ConfigProto(_message.Message):
    __slots__ = ("hostname", "username", "packages_dir_path", "compatibility_file_path", "packages_file_path", "config_file_path", "release_metrics_file_path", "num_days_of_controlled_availability", "max_outstanding_release_notifications", "max_num_downloads", "download_sliding_window_hours", "sandbox_hostname_hq", "sandbox_hostname_colo")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    RELEASE_METRICS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_DAYS_OF_CONTROLLED_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_RELEASE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_DOWNLOADS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SLIDING_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_HOSTNAME_HQ_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_HOSTNAME_COLO_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    username: str
    packages_dir_path: str
    compatibility_file_path: str
    packages_file_path: str
    config_file_path: str
    release_metrics_file_path: str
    num_days_of_controlled_availability: int
    max_outstanding_release_notifications: int
    max_num_downloads: int
    download_sliding_window_hours: int
    sandbox_hostname_hq: str
    sandbox_hostname_colo: str
    def __init__(self, hostname: _Optional[str] = ..., username: _Optional[str] = ..., packages_dir_path: _Optional[str] = ..., compatibility_file_path: _Optional[str] = ..., packages_file_path: _Optional[str] = ..., config_file_path: _Optional[str] = ..., release_metrics_file_path: _Optional[str] = ..., num_days_of_controlled_availability: _Optional[int] = ..., max_outstanding_release_notifications: _Optional[int] = ..., max_num_downloads: _Optional[int] = ..., download_sliding_window_hours: _Optional[int] = ..., sandbox_hostname_hq: _Optional[str] = ..., sandbox_hostname_colo: _Optional[str] = ...) -> None: ...

class ReleaseMetricsProto(_message.Message):
    __slots__ = ("release_metrics_vec",)
    class ReleaseMetricsInfo(_message.Message):
        __slots__ = ("version", "num_downloads", "download_timestamp_vec", "clusters_notified_vec")
        class ClusterInfo(_message.Message):
            __slots__ = ("cluster_id", "chassis_name")
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            CHASSIS_NAME_FIELD_NUMBER: _ClassVar[int]
            cluster_id: int
            chassis_name: str
            def __init__(self, cluster_id: _Optional[int] = ..., chassis_name: _Optional[str] = ...) -> None: ...
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NUM_DOWNLOADS_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_TIMESTAMP_VEC_FIELD_NUMBER: _ClassVar[int]
        CLUSTERS_NOTIFIED_VEC_FIELD_NUMBER: _ClassVar[int]
        version: str
        num_downloads: int
        download_timestamp_vec: _containers.RepeatedScalarFieldContainer[int]
        clusters_notified_vec: _containers.RepeatedCompositeFieldContainer[ReleaseMetricsProto.ReleaseMetricsInfo.ClusterInfo]
        def __init__(self, version: _Optional[str] = ..., num_downloads: _Optional[int] = ..., download_timestamp_vec: _Optional[_Iterable[int]] = ..., clusters_notified_vec: _Optional[_Iterable[_Union[ReleaseMetricsProto.ReleaseMetricsInfo.ClusterInfo, _Mapping]]] = ...) -> None: ...
    RELEASE_METRICS_VEC_FIELD_NUMBER: _ClassVar[int]
    release_metrics_vec: _containers.RepeatedCompositeFieldContainer[ReleaseMetricsProto.ReleaseMetricsInfo]
    def __init__(self, release_metrics_vec: _Optional[_Iterable[_Union[ReleaseMetricsProto.ReleaseMetricsInfo, _Mapping]]] = ...) -> None: ...

class PackagesProto(_message.Message):
    __slots__ = ("software_packages_vec",)
    class PackageInfo(_message.Message):
        __slots__ = ("name", "version", "md5sum", "release_date", "is_downtime_required", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        MD5SUM_FIELD_NUMBER: _ClassVar[int]
        RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        IS_DOWNTIME_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: str
        md5sum: str
        release_date: str
        is_downtime_required: bool
        description: str
        def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., md5sum: _Optional[str] = ..., release_date: _Optional[str] = ..., is_downtime_required: bool = ..., description: _Optional[str] = ...) -> None: ...
    SOFTWARE_PACKAGES_VEC_FIELD_NUMBER: _ClassVar[int]
    software_packages_vec: _containers.RepeatedCompositeFieldContainer[PackagesProto.PackageInfo]
    def __init__(self, software_packages_vec: _Optional[_Iterable[_Union[PackagesProto.PackageInfo, _Mapping]]] = ...) -> None: ...

class CompatibilityProto(_message.Message):
    __slots__ = ("hardware_compatibility_vec", "upgrade_compatibility_vec", "modified_time_secs", "created_from")
    class HardwareCompatibility(_message.Message):
        __slots__ = ("hardware_model", "compatible_versions_vec", "compatible_hardware_models_vec")
        HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
        COMPATIBLE_VERSIONS_VEC_FIELD_NUMBER: _ClassVar[int]
        COMPATIBLE_HARDWARE_MODELS_VEC_FIELD_NUMBER: _ClassVar[int]
        hardware_model: str
        compatible_versions_vec: _containers.RepeatedScalarFieldContainer[str]
        compatible_hardware_models_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, hardware_model: _Optional[str] = ..., compatible_versions_vec: _Optional[_Iterable[str]] = ..., compatible_hardware_models_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class UpgradeCompatibility(_message.Message):
        __slots__ = ("upgrade_version", "compatible_versions_vec", "stop_the_world_service_vec", "stop_the_world_source_version_constraints")
        UPGRADE_VERSION_FIELD_NUMBER: _ClassVar[int]
        COMPATIBLE_VERSIONS_VEC_FIELD_NUMBER: _ClassVar[int]
        STOP_THE_WORLD_SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
        STOP_THE_WORLD_SOURCE_VERSION_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
        upgrade_version: str
        compatible_versions_vec: _containers.RepeatedScalarFieldContainer[str]
        stop_the_world_service_vec: _containers.RepeatedScalarFieldContainer[str]
        stop_the_world_source_version_constraints: str
        def __init__(self, upgrade_version: _Optional[str] = ..., compatible_versions_vec: _Optional[_Iterable[str]] = ..., stop_the_world_service_vec: _Optional[_Iterable[str]] = ..., stop_the_world_source_version_constraints: _Optional[str] = ...) -> None: ...
    HARDWARE_COMPATIBILITY_VEC_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_COMPATIBILITY_VEC_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FROM_FIELD_NUMBER: _ClassVar[int]
    hardware_compatibility_vec: _containers.RepeatedCompositeFieldContainer[CompatibilityProto.HardwareCompatibility]
    upgrade_compatibility_vec: _containers.RepeatedCompositeFieldContainer[CompatibilityProto.UpgradeCompatibility]
    modified_time_secs: int
    created_from: str
    def __init__(self, hardware_compatibility_vec: _Optional[_Iterable[_Union[CompatibilityProto.HardwareCompatibility, _Mapping]]] = ..., upgrade_compatibility_vec: _Optional[_Iterable[_Union[CompatibilityProto.UpgradeCompatibility, _Mapping]]] = ..., modified_time_secs: _Optional[int] = ..., created_from: _Optional[str] = ...) -> None: ...

class GetPackagesArg(_message.Message):
    __slots__ = ("modified_time_secs", "cluster_id", "chassis_name", "is_internal_cluster")
    MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    modified_time_secs: int
    cluster_id: int
    chassis_name: str
    is_internal_cluster: bool
    def __init__(self, modified_time_secs: _Optional[int] = ..., cluster_id: _Optional[int] = ..., chassis_name: _Optional[str] = ..., is_internal_cluster: bool = ...) -> None: ...

class GetPackagesResult(_message.Message):
    __slots__ = ("error", "modified_time_secs", "packages", "compatibility_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    modified_time_secs: int
    packages: PackagesProto
    compatibility_proto: CompatibilityProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., modified_time_secs: _Optional[int] = ..., packages: _Optional[_Union[PackagesProto, _Mapping]] = ..., compatibility_proto: _Optional[_Union[CompatibilityProto, _Mapping]] = ...) -> None: ...

class DownloadPackageResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ClusterHasNewPackagesProto(_message.Message):
    __slots__ = ("modified_time_secs", "has_new_packages", "packages")
    MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    HAS_NEW_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    modified_time_secs: int
    has_new_packages: bool
    packages: _containers.RepeatedCompositeFieldContainer[PackagesProto.PackageInfo]
    def __init__(self, modified_time_secs: _Optional[int] = ..., has_new_packages: bool = ..., packages: _Optional[_Iterable[_Union[PackagesProto.PackageInfo, _Mapping]]] = ...) -> None: ...

class UpdateNotifiedClustersArg(_message.Message):
    __slots__ = ("package_version_vec", "cluster_id_vec", "remove_clusters")
    PACKAGE_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    package_version_vec: _containers.RepeatedScalarFieldContainer[str]
    cluster_id_vec: _containers.RepeatedScalarFieldContainer[int]
    remove_clusters: bool
    def __init__(self, package_version_vec: _Optional[_Iterable[str]] = ..., cluster_id_vec: _Optional[_Iterable[int]] = ..., remove_clusters: bool = ...) -> None: ...

class UpdateNotifiedClustersResult(_message.Message):
    __slots__ = ("error", "release_metrics_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RELEASE_METRICS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    release_metrics_vec: _containers.RepeatedCompositeFieldContainer[ReleaseMetricsProto.ReleaseMetricsInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., release_metrics_vec: _Optional[_Iterable[_Union[ReleaseMetricsProto.ReleaseMetricsInfo, _Mapping]]] = ...) -> None: ...
