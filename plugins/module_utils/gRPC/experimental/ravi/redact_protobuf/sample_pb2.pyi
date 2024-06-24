from experimental.ravi.redact_protobuf import redact_util_pb2 as _redact_util_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ("id", "provider")
    class Provider(_message.Message):
        __slots__ = ("access_key_id", "encrypted_secret_access_key", "region")
        ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        access_key_id: str
        encrypted_secret_access_key: bytes
        region: str
        def __init__(self, access_key_id: _Optional[str] = ..., encrypted_secret_access_key: _Optional[bytes] = ..., region: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    id: int
    provider: Credentials.Provider
    def __init__(self, id: _Optional[int] = ..., provider: _Optional[_Union[Credentials.Provider, _Mapping]] = ...) -> None: ...
