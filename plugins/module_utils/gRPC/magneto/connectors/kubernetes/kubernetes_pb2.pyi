from magneto.base import common_pb2 as _common_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base.entities import kubernetes_pb2 as _kubernetes_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.kubernetes import kubernetes_api_pb2 as _kubernetes_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kInProgress: _ClassVar[JobStatus]
    kCompleted: _ClassVar[JobStatus]
    kFailed: _ClassVar[JobStatus]

class LimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLimitTypePod: _ClassVar[LimitType]
    kLimitTypeContainer: _ClassVar[LimitType]
    kLimitTypePersistentVolumeClaim: _ClassVar[LimitType]

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSecret: _ClassVar[ResourceType]
    kDeployment: _ClassVar[ResourceType]
    kVolumeSnapshotClass: _ClassVar[ResourceType]
kInProgress: JobStatus
kCompleted: JobStatus
kFailed: JobStatus
kLimitTypePod: LimitType
kLimitTypeContainer: LimitType
kLimitTypePersistentVolumeClaim: LimitType
kSecret: ResourceType
kDeployment: ResourceType
kVolumeSnapshotClass: ResourceType

class GetBackupStorageLocationArg(_message.Message):
    __slots__ = ("namespace", "name")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetBackupStorageLocationResult(_message.Message):
    __slots__ = ("error", "namespace", "name", "uuid", "bucket", "prefix")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    namespace: str
    name: str
    uuid: str
    bucket: str
    prefix: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., namespace: _Optional[str] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., bucket: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...

class CreateBackupStorageLocationArg(_message.Message):
    __slots__ = ("namespace", "name", "hostname", "ca_certificate", "labels", "secret_name", "secret_key")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    hostname: str
    ca_certificate: str
    labels: _containers.ScalarMap[str, str]
    secret_name: str
    secret_key: str
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., hostname: _Optional[str] = ..., ca_certificate: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., secret_name: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class CreateBackupStorageLocationResult(_message.Message):
    __slots__ = ("error", "name", "uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class DeleteBackupStorageLocationArg(_message.Message):
    __slots__ = ("namespace", "name", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteBackupStorageLocationResult(_message.Message):
    __slots__ = ("error", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class CreateBackupJobArg(_message.Message):
    __slots__ = ("namespace", "name", "task_id", "backup_location", "included_namespaces", "excluded_namespaces", "label_selector", "volume_snapshot_locations", "include_cluster_resources")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLUSTER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    task_id: int
    backup_location: str
    included_namespaces: _containers.RepeatedScalarFieldContainer[str]
    excluded_namespaces: _containers.RepeatedScalarFieldContainer[str]
    label_selector: _containers.ScalarMap[str, str]
    volume_snapshot_locations: str
    include_cluster_resources: bool
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., task_id: _Optional[int] = ..., backup_location: _Optional[str] = ..., included_namespaces: _Optional[_Iterable[str]] = ..., excluded_namespaces: _Optional[_Iterable[str]] = ..., label_selector: _Optional[_Mapping[str, str]] = ..., volume_snapshot_locations: _Optional[str] = ..., include_cluster_resources: bool = ...) -> None: ...

class CreateBackupJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateRestoreJobArg(_message.Message):
    __slots__ = ("namespace", "name", "task_id", "backup_name", "included_namespaces", "excluded_namespaces", "included_resources", "excluded_resources", "namespace_mapping", "label_selector", "include_cluster_resources", "labels")
    class NamespaceMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLUSTER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    task_id: int
    backup_name: str
    included_namespaces: _containers.RepeatedScalarFieldContainer[str]
    excluded_namespaces: _containers.RepeatedScalarFieldContainer[str]
    included_resources: _containers.RepeatedScalarFieldContainer[str]
    excluded_resources: _containers.RepeatedScalarFieldContainer[str]
    namespace_mapping: _containers.ScalarMap[str, str]
    label_selector: _containers.ScalarMap[str, str]
    include_cluster_resources: bool
    labels: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., task_id: _Optional[int] = ..., backup_name: _Optional[str] = ..., included_namespaces: _Optional[_Iterable[str]] = ..., excluded_namespaces: _Optional[_Iterable[str]] = ..., included_resources: _Optional[_Iterable[str]] = ..., excluded_resources: _Optional[_Iterable[str]] = ..., namespace_mapping: _Optional[_Mapping[str, str]] = ..., label_selector: _Optional[_Mapping[str, str]] = ..., include_cluster_resources: bool = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateRestoreJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetNamespaceInfoArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNamespaceInfoResult(_message.Message):
    __slots__ = ("error", "name", "uuid", "labels", "annotations", "finalizers")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FINALIZERS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    uuid: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    finalizers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., finalizers: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNamespaceListArg(_message.Message):
    __slots__ = ("label_selector",)
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetNamespaceListResult(_message.Message):
    __slots__ = ("error", "namespace_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    namespace_vec: _containers.RepeatedCompositeFieldContainer[GetNamespaceInfoResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., namespace_vec: _Optional[_Iterable[_Union[GetNamespaceInfoResult, _Mapping]]] = ...) -> None: ...

class GetEventListArg(_message.Message):
    __slots__ = ("uid", "namespace")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    namespace: str
    def __init__(self, uid: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class GetEventListResult(_message.Message):
    __slots__ = ("error", "event_vec")
    class Event(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    event_vec: _containers.RepeatedCompositeFieldContainer[GetEventListResult.Event]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., event_vec: _Optional[_Iterable[_Union[GetEventListResult.Event, _Mapping]]] = ...) -> None: ...

class GetPodsInfoArg(_message.Message):
    __slots__ = ("namespace", "pod_name", "node_name", "include_only_mounted_volumes", "label_selector", "phase")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    POD_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ONLY_MOUNTED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    pod_name: str
    node_name: str
    include_only_mounted_volumes: bool
    label_selector: _containers.ScalarMap[str, str]
    phase: str
    def __init__(self, namespace: _Optional[str] = ..., pod_name: _Optional[str] = ..., node_name: _Optional[str] = ..., include_only_mounted_volumes: bool = ..., label_selector: _Optional[_Mapping[str, str]] = ..., phase: _Optional[str] = ...) -> None: ...

class PodMetaInfo(_message.Message):
    __slots__ = ("name", "uid", "node_name", "volume_vec", "pvc_to_pv_map", "status", "is_cohesity_object", "pvc_to_sc_map", "labels", "annotations", "container_name_to_id_map", "pvc_to_labels_map")
    class PvcToPvMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PvcToScMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ContainerNameToIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Labels(_message.Message):
        __slots__ = ("labels",)
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        LABELS_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.ScalarMap[str, str]
        def __init__(self, labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class PvcToLabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PodMetaInfo.Labels
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PodMetaInfo.Labels, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    PVC_TO_PV_MAP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_COHESITY_OBJECT_FIELD_NUMBER: _ClassVar[int]
    PVC_TO_SC_MAP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_TO_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    PVC_TO_LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    node_name: str
    volume_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo]
    pvc_to_pv_map: _containers.ScalarMap[str, str]
    status: str
    is_cohesity_object: bool
    pvc_to_sc_map: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    container_name_to_id_map: _containers.ScalarMap[str, str]
    pvc_to_labels_map: _containers.MessageMap[str, PodMetaInfo.Labels]
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., node_name: _Optional[str] = ..., volume_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo, _Mapping]]] = ..., pvc_to_pv_map: _Optional[_Mapping[str, str]] = ..., status: _Optional[str] = ..., is_cohesity_object: bool = ..., pvc_to_sc_map: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., container_name_to_id_map: _Optional[_Mapping[str, str]] = ..., pvc_to_labels_map: _Optional[_Mapping[str, PodMetaInfo.Labels]] = ...) -> None: ...

class GetPodsInfoResult(_message.Message):
    __slots__ = ("error", "pod_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POD_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pod_vec: _containers.RepeatedCompositeFieldContainer[PodMetaInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pod_vec: _Optional[_Iterable[_Union[PodMetaInfo, _Mapping]]] = ...) -> None: ...

class GetBackupJobArg(_message.Message):
    __slots__ = ("name", "namespace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class GetBackupJobResult(_message.Message):
    __slots__ = ("error", "name", "uuid", "status", "stats")
    class BackupStats(_message.Message):
        __slots__ = ("total_items_to_backup", "items_backed_up")
        TOTAL_ITEMS_TO_BACKUP_FIELD_NUMBER: _ClassVar[int]
        ITEMS_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
        total_items_to_backup: int
        items_backed_up: int
        def __init__(self, total_items_to_backup: _Optional[int] = ..., items_backed_up: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    uuid: str
    status: JobStatus
    stats: GetBackupJobResult.BackupStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., status: _Optional[_Union[JobStatus, str]] = ..., stats: _Optional[_Union[GetBackupJobResult.BackupStats, _Mapping]] = ...) -> None: ...

class CreatePodJobArg(_message.Message):
    __slots__ = ("job_info",)
    JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    job_info: _kubernetes_api_pb2.JobInfo
    def __init__(self, job_info: _Optional[_Union[_kubernetes_api_pb2.JobInfo, _Mapping]] = ...) -> None: ...

class CreatePodJobResult(_message.Message):
    __slots__ = ("pod_uid", "node_name")
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    pod_uid: str
    node_name: str
    def __init__(self, pod_uid: _Optional[str] = ..., node_name: _Optional[str] = ...) -> None: ...

class MountVolumesArg(_message.Message):
    __slots__ = ("namespace", "management_namespace", "job_name", "volume_vec", "cluster_software_version", "labels", "image_location")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    management_namespace: str
    job_name: str
    volume_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo]
    cluster_software_version: str
    labels: _containers.ScalarMap[str, str]
    image_location: str
    def __init__(self, namespace: _Optional[str] = ..., management_namespace: _Optional[str] = ..., job_name: _Optional[str] = ..., volume_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo, _Mapping]]] = ..., cluster_software_version: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., image_location: _Optional[str] = ...) -> None: ...

class MountVolumesResult(_message.Message):
    __slots__ = ("error", "uid", "node_name")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uid: str
    node_name: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uid: _Optional[str] = ..., node_name: _Optional[str] = ...) -> None: ...

class DeletePodJobArg(_message.Message):
    __slots__ = ("name", "namespace", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeletePodJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRestoreJobArg(_message.Message):
    __slots__ = ("name", "namespace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class GetRestoreJobResult(_message.Message):
    __slots__ = ("error", "name", "uuid", "status", "status_detail")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    uuid: str
    status: JobStatus
    status_detail: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., status: _Optional[_Union[JobStatus, str]] = ..., status_detail: _Optional[str] = ...) -> None: ...

class GetClusterConfigArg(_message.Message):
    __slots__ = ("k8s_distribution",)
    K8S_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    k8s_distribution: _kubernetes_pb2.Entity.Distribution
    def __init__(self, k8s_distribution: _Optional[_Union[_kubernetes_pb2.Entity.Distribution, str]] = ...) -> None: ...

class GetClusterConfigResult(_message.Message):
    __slots__ = ("error", "cluster_uuid", "version", "ip_mode")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IP_MODE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cluster_uuid: str
    version: str
    ip_mode: _kubernetes_pb2.IPMode
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cluster_uuid: _Optional[str] = ..., version: _Optional[str] = ..., ip_mode: _Optional[_Union[_kubernetes_pb2.IPMode, _Mapping]] = ...) -> None: ...

class CreateNamespaceArg(_message.Message):
    __slots__ = ("name", "labels", "annotations", "finalizers")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FINALIZERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    finalizers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., finalizers: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateNamespaceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LabelNamespaceArg(_message.Message):
    __slots__ = ("name", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LabelNamespaceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteNamespaceArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteNamespaceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteServicesArg(_message.Message):
    __slots__ = ("namespace", "labels", "annotations")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteServicesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteCrdArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteCrdResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClusterRoleBindingArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteClusterRoleBindingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClusterRoleArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteClusterRoleResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CleanupVeleroArg(_message.Message):
    __slots__ = ("management_namespace",)
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    def __init__(self, management_namespace: _Optional[str] = ...) -> None: ...

class CleanupVeleroResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetNodeInfoArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNodeInfoResult(_message.Message):
    __slots__ = ("node_info_vec",)
    NODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_info_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.NodeInfo]
    def __init__(self, node_info_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.NodeInfo, _Mapping]]] = ...) -> None: ...

class LabelPodArg(_message.Message):
    __slots__ = ("namespace", "name", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LabelPodResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WorkloadType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDaemonSet: _ClassVar[WorkloadType.Type]
        kDeployment: _ClassVar[WorkloadType.Type]
    kDaemonSet: WorkloadType.Type
    kDeployment: WorkloadType.Type
    def __init__(self) -> None: ...

class DeployDatamoverResourcesArg(_message.Message):
    __slots__ = ("management_namespace", "cluster_id", "cluster_software_version", "datamover_image_location", "workload_type", "tolerations_vec", "use_certs", "env_var_map")
    class EnvVarMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_CERTS_FIELD_NUMBER: _ClassVar[int]
    ENV_VAR_MAP_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    cluster_id: int
    cluster_software_version: str
    datamover_image_location: str
    workload_type: WorkloadType.Type
    tolerations_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration]
    use_certs: bool
    env_var_map: _containers.ScalarMap[str, str]
    def __init__(self, management_namespace: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_software_version: _Optional[str] = ..., datamover_image_location: _Optional[str] = ..., workload_type: _Optional[_Union[WorkloadType.Type, str]] = ..., tolerations_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration, _Mapping]]] = ..., use_certs: bool = ..., env_var_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeployDatamoverResourcesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeployDatamoverServicesArg(_message.Message):
    __slots__ = ("management_namespace", "cluster_id", "type", "annotations", "vlan_params", "ip_family_policy")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IP_FAMILY_POLICY_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    cluster_id: int
    type: _kubernetes_pb2.ServiceType
    annotations: _containers.ScalarMap[str, str]
    vlan_params: _common_pb2.VlanParams
    ip_family_policy: _kubernetes_pb2.IPFamilyPolicy
    def __init__(self, management_namespace: _Optional[str] = ..., cluster_id: _Optional[int] = ..., type: _Optional[_Union[_kubernetes_pb2.ServiceType, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., ip_family_policy: _Optional[_Union[_kubernetes_pb2.IPFamilyPolicy, str]] = ...) -> None: ...

class DeployDatamoverServicesResult(_message.Message):
    __slots__ = ("error", "service_info_vec", "num_datamover_pods")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_DATAMOVER_PODS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    service_info_vec: _containers.RepeatedCompositeFieldContainer[ServiceInfo]
    num_datamover_pods: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., service_info_vec: _Optional[_Iterable[_Union[ServiceInfo, _Mapping]]] = ..., num_datamover_pods: _Optional[int] = ...) -> None: ...

class CleanupDatamoverResourcesArg(_message.Message):
    __slots__ = ("management_namespace",)
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    def __init__(self, management_namespace: _Optional[str] = ...) -> None: ...

class CleanupDatamoverResourcesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetEntityHierarchyArg(_message.Message):
    __slots__ = ("management_namespace", "should_add_pv_and_pvc_to_eh", "k8s_distribution")
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ADD_PV_AND_PVC_TO_EH_FIELD_NUMBER: _ClassVar[int]
    K8S_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    management_namespace: str
    should_add_pv_and_pvc_to_eh: bool
    k8s_distribution: _kubernetes_pb2.Entity.Distribution
    def __init__(self, management_namespace: _Optional[str] = ..., should_add_pv_and_pvc_to_eh: bool = ..., k8s_distribution: _Optional[_Union[_kubernetes_pb2.Entity.Distribution, str]] = ...) -> None: ...

class GetEntityHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy", "service_name_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    service_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., service_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AnnotatePodsArg(_message.Message):
    __slots__ = ("namespace", "pod_vec", "delete_annotations")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    POD_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    pod_vec: _containers.RepeatedCompositeFieldContainer[PodMetaInfo]
    delete_annotations: bool
    def __init__(self, namespace: _Optional[str] = ..., pod_vec: _Optional[_Iterable[_Union[PodMetaInfo, _Mapping]]] = ..., delete_annotations: bool = ...) -> None: ...

class AnnotatePodsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetServiceInfoArg(_message.Message):
    __slots__ = ("namespace", "label_selector", "annotation_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    annotation_selector: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ..., annotation_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetServiceInfoResult(_message.Message):
    __slots__ = ("service_info_vec",)
    SERVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    service_info_vec: _containers.RepeatedCompositeFieldContainer[ServiceInfo]
    def __init__(self, service_info_vec: _Optional[_Iterable[_Union[ServiceInfo, _Mapping]]] = ...) -> None: ...

class ServiceInfo(_message.Message):
    __slots__ = ("name", "type", "service_port_vec", "uuid", "labels", "annotations", "external_ips")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    service_port_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.ServicePort]
    uuid: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    external_ips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., service_port_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.ServicePort, _Mapping]]] = ..., uuid: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., external_ips: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteBackupJobArg(_message.Message):
    __slots__ = ("name", "namespace", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteBackupJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteRestoreJobArg(_message.Message):
    __slots__ = ("name", "namespace", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteRestoreJobResult(_message.Message):
    __slots__ = ("error", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class GetPvInfoArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PvInfo(_message.Message):
    __slots__ = ("csi_driver", "storage_class", "labels", "name", "uuid", "pvc_name", "pvc_namespace")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CSI_DRIVER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    PVC_NAME_FIELD_NUMBER: _ClassVar[int]
    PVC_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    csi_driver: str
    storage_class: str
    labels: _containers.ScalarMap[str, str]
    name: str
    uuid: str
    pvc_name: str
    pvc_namespace: str
    def __init__(self, csi_driver: _Optional[str] = ..., storage_class: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., pvc_name: _Optional[str] = ..., pvc_namespace: _Optional[str] = ...) -> None: ...

class GetPvInfoResult(_message.Message):
    __slots__ = ("error", "pv_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PV_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pv_vec: _containers.RepeatedCompositeFieldContainer[PvInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pv_vec: _Optional[_Iterable[_Union[PvInfo, _Mapping]]] = ...) -> None: ...

class GetPvcInfoArg(_message.Message):
    __slots__ = ("namespace", "names_vec")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAMES_VEC_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    names_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace: _Optional[str] = ..., names_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class PvcInfo(_message.Message):
    __slots__ = ("name", "uuid", "size_in_bytes", "volume_name", "access_modes", "storage_class", "labels", "annotations", "volume_mode", "phase", "sc_wait_for_first_consumer", "request")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MODE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    SC_WAIT_FOR_FIRST_CONSUMER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    size_in_bytes: int
    volume_name: str
    access_modes: _containers.RepeatedScalarFieldContainer[str]
    storage_class: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    volume_mode: str
    phase: str
    sc_wait_for_first_consumer: bool
    request: int
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., size_in_bytes: _Optional[int] = ..., volume_name: _Optional[str] = ..., access_modes: _Optional[_Iterable[str]] = ..., storage_class: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., volume_mode: _Optional[str] = ..., phase: _Optional[str] = ..., sc_wait_for_first_consumer: bool = ..., request: _Optional[int] = ...) -> None: ...

class PvcInfoResult(_message.Message):
    __slots__ = ("error", "pvc_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PVC_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pvc_vec: _containers.RepeatedCompositeFieldContainer[PvcInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pvc_vec: _Optional[_Iterable[_Union[PvcInfo, _Mapping]]] = ...) -> None: ...

class CreatePvcArg(_message.Message):
    __slots__ = ("name", "namespace", "access_modes", "data_source", "size", "storage_class", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODES_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    access_modes: _containers.RepeatedScalarFieldContainer[str]
    data_source: _kubernetes_api_pb2.ObjectReference
    size: int
    storage_class: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., access_modes: _Optional[_Iterable[str]] = ..., data_source: _Optional[_Union[_kubernetes_api_pb2.ObjectReference, _Mapping]] = ..., size: _Optional[int] = ..., storage_class: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreatePvcResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeletePvcArg(_message.Message):
    __slots__ = ("name", "namespace", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeletePvcResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class StorageClassInfo(_message.Message):
    __slots__ = ("name", "provisioner", "volume_snapshot_class")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASS_FIELD_NUMBER: _ClassVar[int]
    name: str
    provisioner: str
    volume_snapshot_class: str
    def __init__(self, name: _Optional[str] = ..., provisioner: _Optional[str] = ..., volume_snapshot_class: _Optional[str] = ...) -> None: ...

class GetStorageClassInfoArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetStorageClassInfoResult(_message.Message):
    __slots__ = ("error", "storage_class_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    storage_class_info: _containers.RepeatedCompositeFieldContainer[StorageClassInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., storage_class_info: _Optional[_Iterable[_Union[StorageClassInfo, _Mapping]]] = ...) -> None: ...

class VolumeSnapshotClassInfo(_message.Message):
    __slots__ = ("name", "driver")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    name: str
    driver: str
    def __init__(self, name: _Optional[str] = ..., driver: _Optional[str] = ...) -> None: ...

class GetVolumeSnapshotClassesInfo(_message.Message):
    __slots__ = ("error", "snapshot_class_info", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CLASS_INFO_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    snapshot_class_info: _containers.RepeatedCompositeFieldContainer[VolumeSnapshotClassInfo]
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_class_info: _Optional[_Iterable[_Union[VolumeSnapshotClassInfo, _Mapping]]] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateVolumeSnapshotClassArg(_message.Message):
    __slots__ = ("name", "annotations", "labels", "driver", "deletion_policy", "parameters")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    DELETION_POLICY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    driver: str
    deletion_policy: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., driver: _Optional[str] = ..., deletion_policy: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateVolumeSnapshotClassResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateVolumeSnapshotArg(_message.Message):
    __slots__ = ("name", "namespace", "persistent_volume_claim", "volume_snapshot_class", "volume_snapshot_content", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_VOLUME_CLAIM_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    persistent_volume_claim: str
    volume_snapshot_class: str
    volume_snapshot_content: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., persistent_volume_claim: _Optional[str] = ..., volume_snapshot_class: _Optional[str] = ..., volume_snapshot_content: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteVolumeSnapshotArg(_message.Message):
    __slots__ = ("name", "namespace", "label_selector")
    class LabelSelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    label_selector: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., label_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteVolumeSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetVolumeSnapshotArg(_message.Message):
    __slots__ = ("name", "namespace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class VolumeSnapshotResult(_message.Message):
    __slots__ = ("error", "bound_volume_snapshot_content", "ready_to_use", "restore_size")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BOUND_VOLUME_SNAPSHOT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    READY_TO_USE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SIZE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    bound_volume_snapshot_content: str
    ready_to_use: bool
    restore_size: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., bound_volume_snapshot_content: _Optional[str] = ..., ready_to_use: bool = ..., restore_size: _Optional[int] = ...) -> None: ...

class VolumeSnapshotContentInfo(_message.Message):
    __slots__ = ("error", "name", "snapshot_handle", "ready_to_use")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    READY_TO_USE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    snapshot_handle: str
    ready_to_use: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., snapshot_handle: _Optional[str] = ..., ready_to_use: bool = ...) -> None: ...

class CreateVolumeSnapshotContentArg(_message.Message):
    __slots__ = ("name", "snapshot_handle", "driver", "volume_snapshot_ref", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_REF_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    snapshot_handle: str
    driver: str
    volume_snapshot_ref: _kubernetes_api_pb2.VolumeSnapshotRef
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., snapshot_handle: _Optional[str] = ..., driver: _Optional[str] = ..., volume_snapshot_ref: _Optional[_Union[_kubernetes_api_pb2.VolumeSnapshotRef, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateVolumeSnapshotContentResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateServiceAccountArg(_message.Message):
    __slots__ = ("namespace", "name", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateServiceAccountResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSecretArg(_message.Message):
    __slots__ = ("namespace", "name", "labels", "data", "type", "annotations")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    labels: _containers.ScalarMap[str, str]
    data: _containers.ScalarMap[str, str]
    type: str
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., data: _Optional[_Mapping[str, str]] = ..., type: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateSecretResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateResourceFromConfigArg(_message.Message):
    __slots__ = ("config_string", "url")
    CONFIG_STRING_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    config_string: str
    url: str
    def __init__(self, config_string: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CreateResourceFromConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeployVeleroArg(_message.Message):
    __slots__ = ("deploy_restic", "management_namespace", "s3_aws_access_key_id", "s3_aws_secret_access_key", "velero_crd_location", "velero_image_location", "velero_aws_plugin_image_location", "k8s_distribution", "velero_openshift_plugin_image_location", "cluster_id", "velero_version", "create_cluster_role")
    DEPLOY_RESTIC_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    S3_AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    S3_AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    VELERO_CRD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_AWS_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    K8S_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    VELERO_OPENSHIFT_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VELERO_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLUSTER_ROLE_FIELD_NUMBER: _ClassVar[int]
    deploy_restic: bool
    management_namespace: str
    s3_aws_access_key_id: str
    s3_aws_secret_access_key: str
    velero_crd_location: str
    velero_image_location: str
    velero_aws_plugin_image_location: str
    k8s_distribution: _kubernetes_pb2.Entity.Distribution
    velero_openshift_plugin_image_location: str
    cluster_id: int
    velero_version: str
    create_cluster_role: bool
    def __init__(self, deploy_restic: bool = ..., management_namespace: _Optional[str] = ..., s3_aws_access_key_id: _Optional[str] = ..., s3_aws_secret_access_key: _Optional[str] = ..., velero_crd_location: _Optional[str] = ..., velero_image_location: _Optional[str] = ..., velero_aws_plugin_image_location: _Optional[str] = ..., k8s_distribution: _Optional[_Union[_kubernetes_pb2.Entity.Distribution, str]] = ..., velero_openshift_plugin_image_location: _Optional[str] = ..., cluster_id: _Optional[int] = ..., velero_version: _Optional[str] = ..., create_cluster_role: bool = ...) -> None: ...

class DeployVeleroResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateClusterRoleBindingArg(_message.Message):
    __slots__ = ("name", "labels", "role_ref", "subjects")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ROLE_REF_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    role_ref: _kubernetes_api_pb2.RoleRefInfo
    subjects: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.SubjectItemInfo]
    def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., role_ref: _Optional[_Union[_kubernetes_api_pb2.RoleRefInfo, _Mapping]] = ..., subjects: _Optional[_Iterable[_Union[_kubernetes_api_pb2.SubjectItemInfo, _Mapping]]] = ...) -> None: ...

class CreateClusterRoleBindingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateLimitRangeArg(_message.Message):
    __slots__ = ("name", "namespace", "limit_type", "default_cpu_limit", "default_memory_limit", "default_cpu_request", "default_memory_request", "max_cpu_limit", "max_memory_limit", "min_cpu_request", "min_memory_request")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CPU_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MEMORY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAX_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MIN_MEMORY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    limit_type: LimitType
    default_cpu_limit: str
    default_memory_limit: str
    default_cpu_request: str
    default_memory_request: str
    max_cpu_limit: str
    max_memory_limit: str
    min_cpu_request: str
    min_memory_request: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., limit_type: _Optional[_Union[LimitType, str]] = ..., default_cpu_limit: _Optional[str] = ..., default_memory_limit: _Optional[str] = ..., default_cpu_request: _Optional[str] = ..., default_memory_request: _Optional[str] = ..., max_cpu_limit: _Optional[str] = ..., max_memory_limit: _Optional[str] = ..., min_cpu_request: _Optional[str] = ..., min_memory_request: _Optional[str] = ...) -> None: ...

class CreateLimitRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "namespace_info", "status", "error", "backup_job_name", "pod_metadata_vec", "current_pod_idx", "task_id", "job_id", "warnings", "total_bytes_read_from_source", "backed_up_volumes_vec", "current_pod_state", "protection_using_datamover_enabled", "pvc_info_map", "pvc_backup_success_vec", "volume_groups_backup_vec", "v2_backup", "cleanup_error", "excluded_pvc_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kNamespaceInfoFetched: _ClassVar[SnapshotInfo.Status]
        kPermitGranted: _ClassVar[SnapshotInfo.Status]
        kBackupStorageCreated: _ClassVar[SnapshotInfo.Status]
        kPodsAnnotated: _ClassVar[SnapshotInfo.Status]
        kBackupJobSubmitted: _ClassVar[SnapshotInfo.Status]
        kBackupFinished: _ClassVar[SnapshotInfo.Status]
        kS3CloneFinished: _ClassVar[SnapshotInfo.Status]
        kBackupJobDeleted: _ClassVar[SnapshotInfo.Status]
        kVeleroBackupFinished: _ClassVar[SnapshotInfo.Status]
        kDatamoverBackupPrepared: _ClassVar[SnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[SnapshotInfo.Status]
        kVolumeBackupPrepared: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kNamespaceInfoFetched: SnapshotInfo.Status
    kPermitGranted: SnapshotInfo.Status
    kBackupStorageCreated: SnapshotInfo.Status
    kPodsAnnotated: SnapshotInfo.Status
    kBackupJobSubmitted: SnapshotInfo.Status
    kBackupFinished: SnapshotInfo.Status
    kS3CloneFinished: SnapshotInfo.Status
    kBackupJobDeleted: SnapshotInfo.Status
    kVeleroBackupFinished: SnapshotInfo.Status
    kDatamoverBackupPrepared: SnapshotInfo.Status
    kProgressMonitorsCreated: SnapshotInfo.Status
    kVolumeBackupPrepared: SnapshotInfo.Status
    class PodBackupState(_message.Message):
        __slots__ = ("source_volume_paths_vec", "view_volume_paths_vec", "volumes_identifiers_vec", "current_volume_idx", "current_node_ip", "current_service_port", "current_volume_state", "current_service_connector_id")
        class VolumeBackupState(_message.Message):
            __slots__ = ("snapshot_prepared", "temp_pvc_info", "temp_pod_uid", "path_on_dm_pod", "snapshot_name", "csi_driver", "snapshot_class", "service_port", "service_connector_id", "restore_size")
            class SnapshotStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kStarted: _ClassVar[SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus]
                kReady: _ClassVar[SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus]
                kError: _ClassVar[SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus]
                kUnSupported: _ClassVar[SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus]
            kStarted: SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus
            kReady: SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus
            kError: SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus
            kUnSupported: SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus
            SNAPSHOT_PREPARED_FIELD_NUMBER: _ClassVar[int]
            TEMP_PVC_INFO_FIELD_NUMBER: _ClassVar[int]
            TEMP_POD_UID_FIELD_NUMBER: _ClassVar[int]
            PATH_ON_DM_POD_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
            CSI_DRIVER_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_CLASS_FIELD_NUMBER: _ClassVar[int]
            SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
            SERVICE_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
            RESTORE_SIZE_FIELD_NUMBER: _ClassVar[int]
            snapshot_prepared: SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus
            temp_pvc_info: PvcInfo
            temp_pod_uid: str
            path_on_dm_pod: str
            snapshot_name: str
            csi_driver: str
            snapshot_class: str
            service_port: int
            service_connector_id: int
            restore_size: int
            def __init__(self, snapshot_prepared: _Optional[_Union[SnapshotInfo.PodBackupState.VolumeBackupState.SnapshotStatus, str]] = ..., temp_pvc_info: _Optional[_Union[PvcInfo, _Mapping]] = ..., temp_pod_uid: _Optional[str] = ..., path_on_dm_pod: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., csi_driver: _Optional[str] = ..., snapshot_class: _Optional[str] = ..., service_port: _Optional[int] = ..., service_connector_id: _Optional[int] = ..., restore_size: _Optional[int] = ...) -> None: ...
        SOURCE_VOLUME_PATHS_VEC_FIELD_NUMBER: _ClassVar[int]
        VIEW_VOLUME_PATHS_VEC_FIELD_NUMBER: _ClassVar[int]
        VOLUMES_IDENTIFIERS_VEC_FIELD_NUMBER: _ClassVar[int]
        CURRENT_VOLUME_IDX_FIELD_NUMBER: _ClassVar[int]
        CURRENT_NODE_IP_FIELD_NUMBER: _ClassVar[int]
        CURRENT_SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
        CURRENT_VOLUME_STATE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_SERVICE_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        source_volume_paths_vec: _containers.RepeatedScalarFieldContainer[str]
        view_volume_paths_vec: _containers.RepeatedScalarFieldContainer[str]
        volumes_identifiers_vec: _containers.RepeatedScalarFieldContainer[str]
        current_volume_idx: int
        current_node_ip: str
        current_service_port: int
        current_volume_state: SnapshotInfo.PodBackupState.VolumeBackupState
        current_service_connector_id: int
        def __init__(self, source_volume_paths_vec: _Optional[_Iterable[str]] = ..., view_volume_paths_vec: _Optional[_Iterable[str]] = ..., volumes_identifiers_vec: _Optional[_Iterable[str]] = ..., current_volume_idx: _Optional[int] = ..., current_node_ip: _Optional[str] = ..., current_service_port: _Optional[int] = ..., current_volume_state: _Optional[_Union[SnapshotInfo.PodBackupState.VolumeBackupState, _Mapping]] = ..., current_service_connector_id: _Optional[int] = ...) -> None: ...
    class PvcInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PvcInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PvcInfo, _Mapping]] = ...) -> None: ...
    class VolumeInfo(_message.Message):
        __slots__ = ("name", "labels", "annotations", "pod_uid", "pod_name", "pod_node_name", "pvc_info")
        class PvcInfo(_message.Message):
            __slots__ = ("pv_name", "csi_driver", "volume_snapshot_class", "storage_class", "size_in_bytes", "access_modes", "temp_pvc_name", "temp_pv_name", "temp_pod_uid", "temp_pod_node_name", "sc_wait_for_first_consumer", "restore_size")
            PV_NAME_FIELD_NUMBER: _ClassVar[int]
            CSI_DRIVER_FIELD_NUMBER: _ClassVar[int]
            VOLUME_SNAPSHOT_CLASS_FIELD_NUMBER: _ClassVar[int]
            STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
            SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
            ACCESS_MODES_FIELD_NUMBER: _ClassVar[int]
            TEMP_PVC_NAME_FIELD_NUMBER: _ClassVar[int]
            TEMP_PV_NAME_FIELD_NUMBER: _ClassVar[int]
            TEMP_POD_UID_FIELD_NUMBER: _ClassVar[int]
            TEMP_POD_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
            SC_WAIT_FOR_FIRST_CONSUMER_FIELD_NUMBER: _ClassVar[int]
            RESTORE_SIZE_FIELD_NUMBER: _ClassVar[int]
            pv_name: str
            csi_driver: str
            volume_snapshot_class: str
            storage_class: str
            size_in_bytes: int
            access_modes: _containers.RepeatedScalarFieldContainer[str]
            temp_pvc_name: str
            temp_pv_name: str
            temp_pod_uid: str
            temp_pod_node_name: str
            sc_wait_for_first_consumer: bool
            restore_size: int
            def __init__(self, pv_name: _Optional[str] = ..., csi_driver: _Optional[str] = ..., volume_snapshot_class: _Optional[str] = ..., storage_class: _Optional[str] = ..., size_in_bytes: _Optional[int] = ..., access_modes: _Optional[_Iterable[str]] = ..., temp_pvc_name: _Optional[str] = ..., temp_pv_name: _Optional[str] = ..., temp_pod_uid: _Optional[str] = ..., temp_pod_node_name: _Optional[str] = ..., sc_wait_for_first_consumer: bool = ..., restore_size: _Optional[int] = ...) -> None: ...
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class AnnotationsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        POD_UID_FIELD_NUMBER: _ClassVar[int]
        POD_NAME_FIELD_NUMBER: _ClassVar[int]
        POD_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
        PVC_INFO_FIELD_NUMBER: _ClassVar[int]
        name: str
        labels: _containers.ScalarMap[str, str]
        annotations: _containers.ScalarMap[str, str]
        pod_uid: str
        pod_name: str
        pod_node_name: str
        pvc_info: SnapshotInfo.VolumeInfo.PvcInfo
        def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., pod_uid: _Optional[str] = ..., pod_name: _Optional[str] = ..., pod_node_name: _Optional[str] = ..., pvc_info: _Optional[_Union[SnapshotInfo.VolumeInfo.PvcInfo, _Mapping]] = ...) -> None: ...
    class VolumeBackupProto(_message.Message):
        __slots__ = ("volume", "error_map", "parent_snapshot_info_proto", "total_bytes_read_from_source", "progress_monitor_task_path", "view_path")
        class ErrorMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _error_pb2.ErrorProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
        PARENT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
        volume: SnapshotInfo.VolumeInfo
        error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
        parent_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        total_bytes_read_from_source: int
        progress_monitor_task_path: str
        view_path: str
        def __init__(self, volume: _Optional[_Union[SnapshotInfo.VolumeInfo, _Mapping]] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., parent_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., total_bytes_read_from_source: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., view_path: _Optional[str] = ...) -> None: ...
    class VolumeGroupBackupProto(_message.Message):
        __slots__ = ("id", "volume_backup_vec", "status", "parent_snapshot_info_proto", "error", "cleanup_error", "progress_monitor_task_path")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[SnapshotInfo.VolumeGroupBackupProto.Status]
            kVolumesCreated: _ClassVar[SnapshotInfo.VolumeGroupBackupProto.Status]
            kVolumesMounted: _ClassVar[SnapshotInfo.VolumeGroupBackupProto.Status]
            kBackupComplete: _ClassVar[SnapshotInfo.VolumeGroupBackupProto.Status]
            kFinished: _ClassVar[SnapshotInfo.VolumeGroupBackupProto.Status]
        kStarted: SnapshotInfo.VolumeGroupBackupProto.Status
        kVolumesCreated: SnapshotInfo.VolumeGroupBackupProto.Status
        kVolumesMounted: SnapshotInfo.VolumeGroupBackupProto.Status
        kBackupComplete: SnapshotInfo.VolumeGroupBackupProto.Status
        kFinished: SnapshotInfo.VolumeGroupBackupProto.Status
        ID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_BACKUP_VEC_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PARENT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CLEANUP_ERROR_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        id: int
        volume_backup_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.VolumeBackupProto]
        status: SnapshotInfo.VolumeGroupBackupProto.Status
        parent_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        error: _error_pb2.ErrorProto
        cleanup_error: _error_pb2.ErrorProto
        progress_monitor_task_path: str
        def __init__(self, id: _Optional[int] = ..., volume_backup_vec: _Optional[_Iterable[_Union[SnapshotInfo.VolumeBackupProto, _Mapping]]] = ..., status: _Optional[_Union[SnapshotInfo.VolumeGroupBackupProto.Status, str]] = ..., parent_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cleanup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ...) -> None: ...
    KUBERNETES_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    kubernetes_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POD_IDX_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BACKED_UP_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POD_STATE_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_USING_DATAMOVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PVC_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    PVC_BACKUP_SUCCESS_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUPS_BACKUP_VEC_FIELD_NUMBER: _ClassVar[int]
    V2_BACKUP_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PVC_VEC_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    namespace_info: GetNamespaceInfoResult
    status: SnapshotInfo.Status
    error: _error_pb2.ErrorProto
    backup_job_name: str
    pod_metadata_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_pb2.PodMetadata]
    current_pod_idx: int
    task_id: int
    job_id: int
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    total_bytes_read_from_source: int
    backed_up_volumes_vec: _containers.RepeatedScalarFieldContainer[str]
    current_pod_state: SnapshotInfo.PodBackupState
    protection_using_datamover_enabled: bool
    pvc_info_map: _containers.MessageMap[str, PvcInfo]
    pvc_backup_success_vec: _containers.RepeatedScalarFieldContainer[str]
    volume_groups_backup_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.VolumeGroupBackupProto]
    v2_backup: bool
    cleanup_error: _error_pb2.ErrorProto
    excluded_pvc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., namespace_info: _Optional[_Union[GetNamespaceInfoResult, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_job_name: _Optional[str] = ..., pod_metadata_vec: _Optional[_Iterable[_Union[_kubernetes_pb2.PodMetadata, _Mapping]]] = ..., current_pod_idx: _Optional[int] = ..., task_id: _Optional[int] = ..., job_id: _Optional[int] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., total_bytes_read_from_source: _Optional[int] = ..., backed_up_volumes_vec: _Optional[_Iterable[str]] = ..., current_pod_state: _Optional[_Union[SnapshotInfo.PodBackupState, _Mapping]] = ..., protection_using_datamover_enabled: bool = ..., pvc_info_map: _Optional[_Mapping[str, PvcInfo]] = ..., pvc_backup_success_vec: _Optional[_Iterable[str]] = ..., volume_groups_backup_vec: _Optional[_Iterable[_Union[SnapshotInfo.VolumeGroupBackupProto, _Mapping]]] = ..., v2_backup: bool = ..., cleanup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., excluded_pvc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class NamespaceRecoveryInfo(_message.Message):
    __slots__ = ("restore_task_state", "backup_location", "current_pod_idx", "pvc_to_pv_name_map", "restored_volumes_vec", "pod_restore_state", "existing_pvc_vec", "existing_pods_vec", "user_excluded_pvc_vec")
    class RecoverTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kNamespaceFilesCloned: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kPermitGranted: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kRestoreJobCreated: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kBackupStorageCreated: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kBackupSyncFinished: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kVolumeMetaRestoreStarted: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kVolumeMetaRestoreDone: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kVolumeSetupDone: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kProgressMonitorsCreated: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kVolumeDataRestoreDone: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kRestoreJobSubmitted: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kDeleteRestoreJob: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
        kFinished: _ClassVar[NamespaceRecoveryInfo.RecoverTaskState]
    kStarted: NamespaceRecoveryInfo.RecoverTaskState
    kNamespaceFilesCloned: NamespaceRecoveryInfo.RecoverTaskState
    kPermitGranted: NamespaceRecoveryInfo.RecoverTaskState
    kRestoreJobCreated: NamespaceRecoveryInfo.RecoverTaskState
    kBackupStorageCreated: NamespaceRecoveryInfo.RecoverTaskState
    kBackupSyncFinished: NamespaceRecoveryInfo.RecoverTaskState
    kVolumeMetaRestoreStarted: NamespaceRecoveryInfo.RecoverTaskState
    kVolumeMetaRestoreDone: NamespaceRecoveryInfo.RecoverTaskState
    kVolumeSetupDone: NamespaceRecoveryInfo.RecoverTaskState
    kProgressMonitorsCreated: NamespaceRecoveryInfo.RecoverTaskState
    kVolumeDataRestoreDone: NamespaceRecoveryInfo.RecoverTaskState
    kRestoreJobSubmitted: NamespaceRecoveryInfo.RecoverTaskState
    kDeleteRestoreJob: NamespaceRecoveryInfo.RecoverTaskState
    kFinished: NamespaceRecoveryInfo.RecoverTaskState
    class PvcToPvNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PodRestoreState(_message.Message):
        __slots__ = ("volume_restore_prepared", "temp_pod_uid", "node_name", "service_port", "service_name", "datamover_pod_name", "volume_path_map", "current_node_ip", "included_volume_idx_vec", "service_connector_id")
        class VolumePathMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        VOLUME_RESTORE_PREPARED_FIELD_NUMBER: _ClassVar[int]
        TEMP_POD_UID_FIELD_NUMBER: _ClassVar[int]
        NODE_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATAMOVER_POD_NAME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
        CURRENT_NODE_IP_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_VOLUME_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
        SERVICE_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        volume_restore_prepared: bool
        temp_pod_uid: str
        node_name: str
        service_port: int
        service_name: str
        datamover_pod_name: str
        volume_path_map: _containers.ScalarMap[str, str]
        current_node_ip: str
        included_volume_idx_vec: _containers.RepeatedScalarFieldContainer[int]
        service_connector_id: int
        def __init__(self, volume_restore_prepared: bool = ..., temp_pod_uid: _Optional[str] = ..., node_name: _Optional[str] = ..., service_port: _Optional[int] = ..., service_name: _Optional[str] = ..., datamover_pod_name: _Optional[str] = ..., volume_path_map: _Optional[_Mapping[str, str]] = ..., current_node_ip: _Optional[str] = ..., included_volume_idx_vec: _Optional[_Iterable[int]] = ..., service_connector_id: _Optional[int] = ...) -> None: ...
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POD_IDX_FIELD_NUMBER: _ClassVar[int]
    PVC_TO_PV_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTORED_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    POD_RESTORE_STATE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PVC_VEC_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PODS_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_PVC_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: NamespaceRecoveryInfo.RecoverTaskState
    backup_location: str
    current_pod_idx: int
    pvc_to_pv_name_map: _containers.ScalarMap[str, str]
    restored_volumes_vec: _containers.RepeatedScalarFieldContainer[str]
    pod_restore_state: NamespaceRecoveryInfo.PodRestoreState
    existing_pvc_vec: _containers.RepeatedScalarFieldContainer[str]
    existing_pods_vec: _containers.RepeatedCompositeFieldContainer[PodMetaInfo]
    user_excluded_pvc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, restore_task_state: _Optional[_Union[NamespaceRecoveryInfo.RecoverTaskState, str]] = ..., backup_location: _Optional[str] = ..., current_pod_idx: _Optional[int] = ..., pvc_to_pv_name_map: _Optional[_Mapping[str, str]] = ..., restored_volumes_vec: _Optional[_Iterable[str]] = ..., pod_restore_state: _Optional[_Union[NamespaceRecoveryInfo.PodRestoreState, _Mapping]] = ..., existing_pvc_vec: _Optional[_Iterable[str]] = ..., existing_pods_vec: _Optional[_Iterable[_Union[PodMetaInfo, _Mapping]]] = ..., user_excluded_pvc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("namespace_recovery_info", "error")
    KUBERNETES_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    kubernetes_restore_info: _descriptor.FieldDescriptor
    NAMESPACE_RECOVERY_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    namespace_recovery_info: NamespaceRecoveryInfo
    error: _error_pb2.ErrorProto
    def __init__(self, namespace_recovery_info: _Optional[_Union[NamespaceRecoveryInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("namespace_info",)
    class NamespaceInfo(_message.Message):
        __slots__ = ("uuid", "name")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        name: str
        def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    KUBERNETES_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    kubernetes_restore_entity_info: _descriptor.FieldDescriptor
    NAMESPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    namespace_info: RestoreEntityInfo.NamespaceInfo
    def __init__(self, namespace_info: _Optional[_Union[RestoreEntityInfo.NamespaceInfo, _Mapping]] = ...) -> None: ...

class GetPodLogsArg(_message.Message):
    __slots__ = ("namespace", "pod_name", "container", "time_in_secs", "limit_bytes")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    POD_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    pod_name: str
    container: str
    time_in_secs: int
    limit_bytes: int
    def __init__(self, namespace: _Optional[str] = ..., pod_name: _Optional[str] = ..., container: _Optional[str] = ..., time_in_secs: _Optional[int] = ..., limit_bytes: _Optional[int] = ...) -> None: ...

class GetPodLogsResult(_message.Message):
    __slots__ = ("error", "logs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    logs: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., logs: _Optional[str] = ...) -> None: ...

class GetVeleroVersionArg(_message.Message):
    __slots__ = ("namespace",)
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    def __init__(self, namespace: _Optional[str] = ...) -> None: ...

class GetVeleroVersionResult(_message.Message):
    __slots__ = ("error", "version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    version: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class AnnotateWorkloadPodsArg(_message.Message):
    __slots__ = ("namespace", "name", "annotations", "workload_type")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    annotations: _containers.ScalarMap[str, str]
    workload_type: WorkloadType.Type
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., workload_type: _Optional[_Union[WorkloadType.Type, str]] = ...) -> None: ...

class AnnotateWorkloadPodsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetSecretArg(_message.Message):
    __slots__ = ("namespace", "name")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetSecretResult(_message.Message):
    __slots__ = ("error", "name", "data", "labels", "annotations")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    name: str
    data: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteResourceArg(_message.Message):
    __slots__ = ("namespace", "name", "resource_type", "is_cluster_scoped")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CLUSTER_SCOPED_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    resource_type: ResourceType
    is_cluster_scoped: bool
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., resource_type: _Optional[_Union[ResourceType, str]] = ..., is_cluster_scoped: bool = ...) -> None: ...

class DeleteResourceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
