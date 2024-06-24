from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionConfigProto(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "current_encryptor")
    class EncryptorInfo(_message.Message):
        __slots__ = ("key_encryption_method", "key_locator", "key")
        class KeyEncryptionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kEncryptionNone: _ClassVar[EncryptionConfigProto.EncryptorInfo.KeyEncryptionMethod]
        kEncryptionNone: EncryptionConfigProto.EncryptorInfo.KeyEncryptionMethod
        KEY_ENCRYPTION_METHOD_FIELD_NUMBER: _ClassVar[int]
        KEY_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        key_encryption_method: EncryptionConfigProto.EncryptorInfo.KeyEncryptionMethod
        key_locator: str
        key: bytes
        def __init__(self, key_encryption_method: _Optional[_Union[EncryptionConfigProto.EncryptorInfo.KeyEncryptionMethod, str]] = ..., key_locator: _Optional[str] = ..., key: _Optional[bytes] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENCRYPTOR_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    current_encryptor: EncryptionConfigProto.EncryptorInfo
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., current_encryptor: _Optional[_Union[EncryptionConfigProto.EncryptorInfo, _Mapping]] = ...) -> None: ...
