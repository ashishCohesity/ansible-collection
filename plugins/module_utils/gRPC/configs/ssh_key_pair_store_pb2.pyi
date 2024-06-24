from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SshKeyPairStoreProto(_message.Message):
    __slots__ = ("ssh_key_pair_vec",)
    class SshKeyPair(_message.Message):
        __slots__ = ("key", "public_key", "enc_private_key")
        KEY_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        ENC_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        key: str
        public_key: str
        enc_private_key: str
        def __init__(self, key: _Optional[str] = ..., public_key: _Optional[str] = ..., enc_private_key: _Optional[str] = ...) -> None: ...
    SSH_KEY_PAIR_VEC_FIELD_NUMBER: _ClassVar[int]
    ssh_key_pair_vec: _containers.RepeatedCompositeFieldContainer[SshKeyPairStoreProto.SshKeyPair]
    def __init__(self, ssh_key_pair_vec: _Optional[_Iterable[_Union[SshKeyPairStoreProto.SshKeyPair, _Mapping]]] = ...) -> None: ...
