from configs import cluster_config_pb2 as _cluster_config_pb2
from keychain.base import error_pb2 as _error_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeychainUrisProto(_message.Message):
    __slots__ = ("kms_status_uri",)
    KMS_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    kms_status_uri: str
    def __init__(self, kms_status_uri: _Optional[str] = ...) -> None: ...

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

class UIDProto(_message.Message):
    __slots__ = ("uid", "creation_timestamp_secs", "version", "last_key_rotation_timestamp_secs")
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_KEY_ROTATION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    uid: bytes
    creation_timestamp_secs: int
    version: VersionProto
    last_key_rotation_timestamp_secs: int
    def __init__(self, uid: _Optional[bytes] = ..., creation_timestamp_secs: _Optional[int] = ..., version: _Optional[_Union[VersionProto, _Mapping]] = ..., last_key_rotation_timestamp_secs: _Optional[int] = ...) -> None: ...

class EntityId(_message.Message):
    __slots__ = ("disk_id_DEPRECATED", "viewbox_id", "disk_serial_number", "obj_id", "vault_id", "cloud_domain_id")
    DISK_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OBJ_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id_DEPRECATED: int
    viewbox_id: int
    disk_serial_number: str
    obj_id: _universal_id_pb2.UniversalIdProto
    vault_id: int
    cloud_domain_id: int
    def __init__(self, disk_id_DEPRECATED: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., disk_serial_number: _Optional[str] = ..., obj_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ...) -> None: ...

class EdekProto(_message.Message):
    __slots__ = ("key_id", "edek", "random_nonce", "cluster_instance_id", "gcm_edek")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    GCM_EDEK_FIELD_NUMBER: _ClassVar[int]
    key_id: int
    edek: bytes
    random_nonce: bytes
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    gcm_edek: bytes
    def __init__(self, key_id: _Optional[int] = ..., edek: _Optional[bytes] = ..., random_nonce: _Optional[bytes] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., gcm_edek: _Optional[bytes] = ...) -> None: ...

class EdekInfoProto(_message.Message):
    __slots__ = ("type", "key_uid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_UID_FIELD_NUMBER: _ClassVar[int]
    type: _cluster_config_pb2.ClusterConfigProto.KMSConfig.Type
    key_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.KMSConfig.Type, str]] = ..., key_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class GetKeyResult(_message.Message):
    __slots__ = ("error", "key", "alternate_key")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_KEY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    key: KeyProto
    alternate_key: KeyProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., key: _Optional[_Union[KeyProto, _Mapping]] = ..., alternate_key: _Optional[_Union[KeyProto, _Mapping]] = ...) -> None: ...

class ExportedKey(_message.Message):
    __slots__ = ("edek", "kek", "magic_number", "entity_id", "cluster_id", "cluster_incarnation_id", "kms_name")
    EDEK_FIELD_NUMBER: _ClassVar[int]
    KEK_FIELD_NUMBER: _ClassVar[int]
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_NAME_FIELD_NUMBER: _ClassVar[int]
    edek: KeyProto
    kek: KeyProto
    magic_number: int
    entity_id: EntityId
    cluster_id: int
    cluster_incarnation_id: int
    kms_name: bytes
    def __init__(self, edek: _Optional[_Union[KeyProto, _Mapping]] = ..., kek: _Optional[_Union[KeyProto, _Mapping]] = ..., magic_number: _Optional[int] = ..., entity_id: _Optional[_Union[EntityId, _Mapping]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., kms_name: _Optional[bytes] = ...) -> None: ...

class ExportKeyResult(_message.Message):
    __slots__ = ("error", "exported_key")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_KEY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    exported_key: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., exported_key: _Optional[bytes] = ...) -> None: ...

class ImportKeyArg(_message.Message):
    __slots__ = ("id", "exported_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_KEY_FIELD_NUMBER: _ClassVar[int]
    id: EntityId
    exported_key: bytes
    def __init__(self, id: _Optional[_Union[EntityId, _Mapping]] = ..., exported_key: _Optional[bytes] = ...) -> None: ...

class ImportKeyResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DestroyKeyResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

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
    error: _error_pb2.ErrorProto
    new_key: KeyProto
    current_key: KeyProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., new_key: _Optional[_Union[KeyProto, _Mapping]] = ..., current_key: _Optional[_Union[KeyProto, _Mapping]] = ...) -> None: ...

class FinalizeDiskKeyRotationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetDekForEntityArg(_message.Message):
    __slots__ = ("entity_id", "fetch_fixed_dek", "random_nonce", "cluster_instance_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIXED_DEK_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: EntityId
    fetch_fixed_dek: bool
    random_nonce: bytes
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    def __init__(self, entity_id: _Optional[_Union[EntityId, _Mapping]] = ..., fetch_fixed_dek: bool = ..., random_nonce: _Optional[bytes] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ...) -> None: ...

class GetDekForEntityResult(_message.Message):
    __slots__ = ("error", "dek", "edek", "key_id", "is_fixed_dek", "random_nonce", "cluster_instance_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEK_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FIXED_DEK_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dek: bytes
    edek: bytes
    key_id: int
    is_fixed_dek: bool
    random_nonce: bytes
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dek: _Optional[bytes] = ..., edek: _Optional[bytes] = ..., key_id: _Optional[int] = ..., is_fixed_dek: bool = ..., random_nonce: _Optional[bytes] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ...) -> None: ...

class GetKeyIdForEntityArg(_message.Message):
    __slots__ = ("entity_id", "fetch_fixed_dek")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIXED_DEK_FIELD_NUMBER: _ClassVar[int]
    entity_id: EntityId
    fetch_fixed_dek: bool
    def __init__(self, entity_id: _Optional[_Union[EntityId, _Mapping]] = ..., fetch_fixed_dek: bool = ...) -> None: ...

class GetKeyIdForEntityResult(_message.Message):
    __slots__ = ("error", "key_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    key_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., key_id: _Optional[int] = ...) -> None: ...

class DecryptEdekArg(_message.Message):
    __slots__ = ("edek", "key_id")
    EDEK_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    edek: bytes
    key_id: int
    def __init__(self, edek: _Optional[bytes] = ..., key_id: _Optional[int] = ...) -> None: ...

class DecryptEdekResult(_message.Message):
    __slots__ = ("error", "dek")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEK_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dek: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dek: _Optional[bytes] = ...) -> None: ...

class GetDekForKeyIdArg(_message.Message):
    __slots__ = ("key_id",)
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: int
    def __init__(self, key_id: _Optional[int] = ...) -> None: ...

class GetDekForKeyIdResult(_message.Message):
    __slots__ = ("error", "dek", "edek", "is_fixed_dek")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEK_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    IS_FIXED_DEK_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dek: bytes
    edek: bytes
    is_fixed_dek: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dek: _Optional[bytes] = ..., edek: _Optional[bytes] = ..., is_fixed_dek: bool = ...) -> None: ...

class GetDekMetadataArg(_message.Message):
    __slots__ = ("key_id",)
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: int
    def __init__(self, key_id: _Optional[int] = ...) -> None: ...

class GetDekMetadataResult(_message.Message):
    __slots__ = ("error", "edek_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    edek_info: EdekInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., edek_info: _Optional[_Union[EdekInfoProto, _Mapping]] = ...) -> None: ...

class UploadKeyFileArg(_message.Message):
    __slots__ = ("uploaded_key", "verify_only")
    UPLOADED_KEY_FIELD_NUMBER: _ClassVar[int]
    VERIFY_ONLY_FIELD_NUMBER: _ClassVar[int]
    uploaded_key: str
    verify_only: bool
    def __init__(self, uploaded_key: _Optional[str] = ..., verify_only: bool = ...) -> None: ...

class UploadKeyFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeletedKeyObjectProto(_message.Message):
    __slots__ = ("key_objects",)
    class KeyObject(_message.Message):
        __slots__ = ("kms_id", "uid", "key", "timestamp_secs")
        KMS_ID_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        kms_id: int
        uid: bytes
        key: bytes
        timestamp_secs: int
        def __init__(self, kms_id: _Optional[int] = ..., uid: _Optional[bytes] = ..., key: _Optional[bytes] = ..., timestamp_secs: _Optional[int] = ...) -> None: ...
    KEY_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    key_objects: _containers.RepeatedCompositeFieldContainer[DeletedKeyObjectProto.KeyObject]
    def __init__(self, key_objects: _Optional[_Iterable[_Union[DeletedKeyObjectProto.KeyObject, _Mapping]]] = ...) -> None: ...

class KMSStatus(_message.Message):
    __slots__ = ("error", "is_kms_reachable", "kms_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_KMS_REACHABLE_FIELD_NUMBER: _ClassVar[int]
    KMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    is_kms_reachable: bool
    kms_version: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_kms_reachable: bool = ..., kms_version: _Optional[int] = ...) -> None: ...
