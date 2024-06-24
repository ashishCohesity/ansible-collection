from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionKey(_message.Message):
    __slots__ = ("raw_key", "kms_key_name", "sha256")
    RAW_KEY_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    raw_key: str
    kms_key_name: str
    sha256: str
    def __init__(self, raw_key: _Optional[str] = ..., kms_key_name: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...

class DiskInfo(_message.Message):
    __slots__ = ("id", "creation_timestamp", "name", "description", "size_gb", "zone", "status", "source_snapshot", "source_snapshot_id", "options", "selflink", "source_image", "source_image_id", "disk_type", "licenses", "guest_os_features", "lastAttachTimestamp", "lastDetachTimestamp", "users", "disk_encryption_key", "source_image_encryption_key", "source_snapshot_encryption_key", "labels_map", "label_fingerprint", "region", "replica_zones", "license_codes", "physical_block_size_bytes", "kind")
    class GuestOsFeatures(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str
        def __init__(self, type: _Optional[str] = ...) -> None: ...
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SELFLINK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURES_FIELD_NUMBER: _ClassVar[int]
    LASTATTACHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LASTDETACHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    LABEL_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    LICENSE_CODES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BLOCK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    creation_timestamp: str
    name: str
    description: str
    size_gb: int
    zone: str
    status: str
    source_snapshot: str
    source_snapshot_id: str
    options: str
    selflink: str
    source_image: str
    source_image_id: str
    disk_type: str
    licenses: _containers.RepeatedScalarFieldContainer[str]
    guest_os_features: _containers.RepeatedCompositeFieldContainer[DiskInfo.GuestOsFeatures]
    lastAttachTimestamp: str
    lastDetachTimestamp: str
    users: _containers.RepeatedScalarFieldContainer[str]
    disk_encryption_key: EncryptionKey
    source_image_encryption_key: EncryptionKey
    source_snapshot_encryption_key: EncryptionKey
    labels_map: _containers.ScalarMap[str, str]
    label_fingerprint: str
    region: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    license_codes: _containers.RepeatedScalarFieldContainer[str]
    physical_block_size_bytes: str
    kind: str
    def __init__(self, id: _Optional[str] = ..., creation_timestamp: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., size_gb: _Optional[int] = ..., zone: _Optional[str] = ..., status: _Optional[str] = ..., source_snapshot: _Optional[str] = ..., source_snapshot_id: _Optional[str] = ..., options: _Optional[str] = ..., selflink: _Optional[str] = ..., source_image: _Optional[str] = ..., source_image_id: _Optional[str] = ..., disk_type: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., guest_os_features: _Optional[_Iterable[_Union[DiskInfo.GuestOsFeatures, _Mapping]]] = ..., lastAttachTimestamp: _Optional[str] = ..., lastDetachTimestamp: _Optional[str] = ..., users: _Optional[_Iterable[str]] = ..., disk_encryption_key: _Optional[_Union[EncryptionKey, _Mapping]] = ..., source_image_encryption_key: _Optional[_Union[EncryptionKey, _Mapping]] = ..., source_snapshot_encryption_key: _Optional[_Union[EncryptionKey, _Mapping]] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., label_fingerprint: _Optional[str] = ..., region: _Optional[str] = ..., replica_zones: _Optional[_Iterable[str]] = ..., license_codes: _Optional[_Iterable[str]] = ..., physical_block_size_bytes: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...
