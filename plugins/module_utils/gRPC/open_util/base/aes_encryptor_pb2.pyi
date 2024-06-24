from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AESEncryptorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCBC: _ClassVar[AESEncryptorMode]
    kGCM: _ClassVar[AESEncryptorMode]
kCBC: AESEncryptorMode
kGCM: AESEncryptorMode

class EncryptHeader(_message.Message):
    __slots__ = ("iv", "morphed_data_length", "key", "version", "encrypted_len", "tag")
    IV_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_LEN_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    iv: bytes
    morphed_data_length: int
    key: bytes
    version: int
    encrypted_len: int
    tag: bytes
    def __init__(self, iv: _Optional[bytes] = ..., morphed_data_length: _Optional[int] = ..., key: _Optional[bytes] = ..., version: _Optional[int] = ..., encrypted_len: _Optional[int] = ..., tag: _Optional[bytes] = ...) -> None: ...
