from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VulscanMetadataKafkaMessage(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id", "vulscan_metadata", "is_unregistered")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VULSCAN_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    vulscan_metadata: bytes
    is_unregistered: bool
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., vulscan_metadata: _Optional[bytes] = ..., is_unregistered: bool = ...) -> None: ...
