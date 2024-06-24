from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptHeaderLegacy(_message.Message):
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
    version: _aes_encryptor_pb2.AESEncryptorMode
    encrypted_len: int
    tag: bytes
    def __init__(self, iv: _Optional[bytes] = ..., morphed_data_length: _Optional[int] = ..., key: _Optional[bytes] = ..., version: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., encrypted_len: _Optional[int] = ..., tag: _Optional[bytes] = ...) -> None: ...
