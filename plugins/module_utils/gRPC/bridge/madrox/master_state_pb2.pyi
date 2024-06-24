from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteClusterInfoProto(_message.Message):
    __slots__ = ("remote_cluster_id", "remote_cluster_incarnation_id", "last_heard_time_usecs", "encrypt_handshake_supported")
    REMOTE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARD_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_HANDSHAKE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    remote_cluster_id: int
    remote_cluster_incarnation_id: int
    last_heard_time_usecs: int
    encrypt_handshake_supported: bool
    def __init__(self, remote_cluster_id: _Optional[int] = ..., remote_cluster_incarnation_id: _Optional[int] = ..., last_heard_time_usecs: _Optional[int] = ..., encrypt_handshake_supported: bool = ...) -> None: ...
