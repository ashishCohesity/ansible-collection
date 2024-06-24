from keychain.base import keychain_pb2 as _keychain_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectState(_message.Message):
    __slots__ = ("obj_id", "kms_uid", "encrypted_data_encryption_key", "kms_server_id", "dek_rotation_enabled", "fixed_dek_key_id", "current_dek_key_id")
    OBJ_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_UID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_DATA_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    KMS_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    DEK_ROTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FIXED_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    obj_id: _universal_id_pb2.UniversalIdProto
    kms_uid: _keychain_pb2.UIDProto
    encrypted_data_encryption_key: bytes
    kms_server_id: int
    dek_rotation_enabled: bool
    fixed_dek_key_id: int
    current_dek_key_id: int
    def __init__(self, obj_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., kms_uid: _Optional[_Union[_keychain_pb2.UIDProto, _Mapping]] = ..., encrypted_data_encryption_key: _Optional[bytes] = ..., kms_server_id: _Optional[int] = ..., dek_rotation_enabled: bool = ..., fixed_dek_key_id: _Optional[int] = ..., current_dek_key_id: _Optional[int] = ...) -> None: ...

class ObjectStateList(_message.Message):
    __slots__ = ("obj_state_vec",)
    OBJ_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    obj_state_vec: _containers.RepeatedCompositeFieldContainer[ObjectState]
    def __init__(self, obj_state_vec: _Optional[_Iterable[_Union[ObjectState, _Mapping]]] = ...) -> None: ...
