from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NexusHmacKeyProto(_message.Message):
    __slots__ = ("version", "encrypted_hmac_key", "allow_api_based_fetch")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_HMAC_KEY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_API_BASED_FETCH_FIELD_NUMBER: _ClassVar[int]
    version: int
    encrypted_hmac_key: bytes
    allow_api_based_fetch: bool
    def __init__(self, version: _Optional[int] = ..., encrypted_hmac_key: _Optional[bytes] = ..., allow_api_based_fetch: bool = ...) -> None: ...
