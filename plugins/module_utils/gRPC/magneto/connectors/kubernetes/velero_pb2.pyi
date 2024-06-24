from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypeMeta(_message.Message):
    __slots__ = ("kind", "api_version")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ...) -> None: ...

class ObjectMeta(_message.Message):
    __slots__ = ("name", "namespace", "uid", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    uid: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., uid: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LabelSelector(_message.Message):
    __slots__ = ("match_labels",)
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.ScalarMap[str, str]
    def __init__(self, match_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class BackupSpec(_message.Message):
    __slots__ = ("included_namespaces", "excluded_namespaces", "included_resources", "excluded_resources", "label_selector", "snapshot_volumes", "ttl", "include_cluster_resources", "storage_location", "volume_snapshot_locations")
    INCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLUSTER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    included_namespaces: _containers.RepeatedScalarFieldContainer[str]
    excluded_namespaces: _containers.RepeatedScalarFieldContainer[str]
    included_resources: _containers.RepeatedScalarFieldContainer[str]
    excluded_resources: _containers.RepeatedScalarFieldContainer[str]
    label_selector: LabelSelector
    snapshot_volumes: bool
    ttl: str
    include_cluster_resources: bool
    storage_location: str
    volume_snapshot_locations: str
    def __init__(self, included_namespaces: _Optional[_Iterable[str]] = ..., excluded_namespaces: _Optional[_Iterable[str]] = ..., included_resources: _Optional[_Iterable[str]] = ..., excluded_resources: _Optional[_Iterable[str]] = ..., label_selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., snapshot_volumes: bool = ..., ttl: _Optional[str] = ..., include_cluster_resources: bool = ..., storage_location: _Optional[str] = ..., volume_snapshot_locations: _Optional[str] = ...) -> None: ...

class BackupStatus(_message.Message):
    __slots__ = ("version", "expiration", "phase", "start_timestamp", "completion_timestamp", "progress")
    class Progress(_message.Message):
        __slots__ = ("total_items", "items_backed_up")
        TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ITEMS_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
        total_items: int
        items_backed_up: int
        def __init__(self, total_items: _Optional[int] = ..., items_backed_up: _Optional[int] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    version: int
    expiration: str
    phase: str
    start_timestamp: str
    completion_timestamp: str
    progress: BackupStatus.Progress
    def __init__(self, version: _Optional[int] = ..., expiration: _Optional[str] = ..., phase: _Optional[str] = ..., start_timestamp: _Optional[str] = ..., completion_timestamp: _Optional[str] = ..., progress: _Optional[_Union[BackupStatus.Progress, _Mapping]] = ...) -> None: ...

class Backup(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: BackupSpec
    status: BackupStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[BackupSpec, _Mapping]] = ..., status: _Optional[_Union[BackupStatus, _Mapping]] = ...) -> None: ...

class RestoreSpec(_message.Message):
    __slots__ = ("backup_name", "included_namespaces", "excluded_namespaces", "included_resources", "excluded_resources", "namespace_mapping", "label_selector", "restore_pvs", "include_cluster_resources")
    class NamespaceMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BACKUP_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    LABEL_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PVS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLUSTER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    backup_name: str
    included_namespaces: _containers.RepeatedScalarFieldContainer[str]
    excluded_namespaces: _containers.RepeatedScalarFieldContainer[str]
    included_resources: _containers.RepeatedScalarFieldContainer[str]
    excluded_resources: _containers.RepeatedScalarFieldContainer[str]
    namespace_mapping: _containers.ScalarMap[str, str]
    label_selector: LabelSelector
    restore_pvs: bool
    include_cluster_resources: bool
    def __init__(self, backup_name: _Optional[str] = ..., included_namespaces: _Optional[_Iterable[str]] = ..., excluded_namespaces: _Optional[_Iterable[str]] = ..., included_resources: _Optional[_Iterable[str]] = ..., excluded_resources: _Optional[_Iterable[str]] = ..., namespace_mapping: _Optional[_Mapping[str, str]] = ..., label_selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., restore_pvs: bool = ..., include_cluster_resources: bool = ...) -> None: ...

class RestoreStatus(_message.Message):
    __slots__ = ("phase", "failure_reason")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    phase: str
    failure_reason: str
    def __init__(self, phase: _Optional[str] = ..., failure_reason: _Optional[str] = ...) -> None: ...

class Restore(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: RestoreSpec
    status: RestoreStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[RestoreSpec, _Mapping]] = ..., status: _Optional[_Union[RestoreStatus, _Mapping]] = ...) -> None: ...

class ObjectStorage(_message.Message):
    __slots__ = ("bucket", "prefix", "ca_cert")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    prefix: str
    ca_cert: str
    def __init__(self, bucket: _Optional[str] = ..., prefix: _Optional[str] = ..., ca_cert: _Optional[str] = ...) -> None: ...

class SecretKeySelector(_message.Message):
    __slots__ = ("name", "key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class BackupStorageLocationSpec(_message.Message):
    __slots__ = ("provider", "config", "object_storage", "credential")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORAGE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    provider: str
    config: _containers.ScalarMap[str, str]
    object_storage: ObjectStorage
    credential: SecretKeySelector
    def __init__(self, provider: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ..., object_storage: _Optional[_Union[ObjectStorage, _Mapping]] = ..., credential: _Optional[_Union[SecretKeySelector, _Mapping]] = ...) -> None: ...

class BackupStorageLocation(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: BackupStorageLocationSpec
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[BackupStorageLocationSpec, _Mapping]] = ...) -> None: ...

class DeleteBackupRequestStatus(_message.Message):
    __slots__ = ("phase",)
    PHASE_FIELD_NUMBER: _ClassVar[int]
    phase: str
    def __init__(self, phase: _Optional[str] = ...) -> None: ...

class DeleteBackupRequestSpec(_message.Message):
    __slots__ = ("backup_name",)
    BACKUP_NAME_FIELD_NUMBER: _ClassVar[int]
    backup_name: str
    def __init__(self, backup_name: _Optional[str] = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: DeleteBackupRequestSpec
    status: DeleteBackupRequestStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[DeleteBackupRequestSpec, _Mapping]] = ..., status: _Optional[_Union[DeleteBackupRequestStatus, _Mapping]] = ...) -> None: ...
