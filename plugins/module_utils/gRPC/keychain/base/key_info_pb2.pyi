from keychain.base import keychain_pb2 as _keychain_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyInfoProto(_message.Message):
    __slots__ = ("key_id", "entity", "kms_server_id", "key_uid", "edek", "dek_creation_timestamp_msecs", "kek_last_rotation_timestamp_msecs", "kek", "random_nonce", "cluster_instance_id")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    KMS_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_UID_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    DEK_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    KEK_LAST_ROTATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    KEK_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: int
    entity: _keychain_pb2.EntityId
    kms_server_id: int
    key_uid: bytes
    edek: bytes
    dek_creation_timestamp_msecs: int
    kek_last_rotation_timestamp_msecs: int
    kek: bytes
    random_nonce: bytes
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    def __init__(self, key_id: _Optional[int] = ..., entity: _Optional[_Union[_keychain_pb2.EntityId, _Mapping]] = ..., kms_server_id: _Optional[int] = ..., key_uid: _Optional[bytes] = ..., edek: _Optional[bytes] = ..., dek_creation_timestamp_msecs: _Optional[int] = ..., kek_last_rotation_timestamp_msecs: _Optional[int] = ..., kek: _Optional[bytes] = ..., random_nonce: _Optional[bytes] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ...) -> None: ...

class KeyInfoList(_message.Message):
    __slots__ = ("key_info_vec", "cluster_config_version", "object_state_version")
    KEY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    key_info_vec: _containers.RepeatedCompositeFieldContainer[KeyInfoProto]
    cluster_config_version: int
    object_state_version: int
    def __init__(self, key_info_vec: _Optional[_Iterable[_Union[KeyInfoProto, _Mapping]]] = ..., cluster_config_version: _Optional[int] = ..., object_state_version: _Optional[int] = ...) -> None: ...

class UploadedKeyInfoProto(_message.Message):
    __slots__ = ("key_id", "kms_server_id", "key_uid", "edek")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_UID_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    key_id: int
    kms_server_id: int
    key_uid: bytes
    edek: bytes
    def __init__(self, key_id: _Optional[int] = ..., kms_server_id: _Optional[int] = ..., key_uid: _Optional[bytes] = ..., edek: _Optional[bytes] = ...) -> None: ...

class UploadedKeyInfoMap(_message.Message):
    __slots__ = ("uploaded_key_info_map", "cluster_config_version")
    class UploadedKeyInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UploadedKeyInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UploadedKeyInfoProto, _Mapping]] = ...) -> None: ...
    UPLOADED_KEY_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    uploaded_key_info_map: _containers.MessageMap[int, UploadedKeyInfoProto]
    cluster_config_version: int
    def __init__(self, uploaded_key_info_map: _Optional[_Mapping[int, UploadedKeyInfoProto]] = ..., cluster_config_version: _Optional[int] = ...) -> None: ...
