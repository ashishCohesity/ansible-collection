from helios.base import cluster_claim_pb2 as _cluster_claim_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterCertificatesStore(_message.Message):
    __slots__ = ("account_id", "cluster_id", "cluster_incarnation_id", "certificate", "is_valid", "last_updated_timestamp_usecs", "cluster_provider_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: int
    cluster_incarnation_id: int
    certificate: str
    is_valid: bool
    last_updated_timestamp_usecs: int
    cluster_provider_type: _cluster_claim_pb2.ClusterProviderType
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., certificate: _Optional[str] = ..., is_valid: bool = ..., last_updated_timestamp_usecs: _Optional[int] = ..., cluster_provider_type: _Optional[_Union[_cluster_claim_pb2.ClusterProviderType, str]] = ...) -> None: ...
