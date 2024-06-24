from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ("username", "enc_pass", "prev_enc_pass")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENC_PASS_FIELD_NUMBER: _ClassVar[int]
    PREV_ENC_PASS_FIELD_NUMBER: _ClassVar[int]
    username: str
    enc_pass: bytes
    prev_enc_pass: bytes
    def __init__(self, username: _Optional[str] = ..., enc_pass: _Optional[bytes] = ..., prev_enc_pass: _Optional[bytes] = ...) -> None: ...

class DatabaseInfo(_message.Message):
    __slots__ = ("cred_vec", "cred_version")
    CRED_VEC_FIELD_NUMBER: _ClassVar[int]
    CRED_VERSION_FIELD_NUMBER: _ClassVar[int]
    cred_vec: _containers.RepeatedCompositeFieldContainer[Credentials]
    cred_version: int
    def __init__(self, cred_vec: _Optional[_Iterable[_Union[Credentials, _Mapping]]] = ..., cred_version: _Optional[int] = ...) -> None: ...
