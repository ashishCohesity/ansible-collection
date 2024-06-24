from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kMCMCohesity: _ClassVar[ClusterProviderType]
    kIBMStorageProtect: _ClassVar[ClusterProviderType]
kMCMCohesity: ClusterProviderType
kIBMStorageProtect: ClusterProviderType

class ClusterClaimInfo(_message.Message):
    __slots__ = ("account_id", "cluster_id", "cluster_incarnation_id", "name", "helios_claimed", "dark_site")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CLAIMED_FIELD_NUMBER: _ClassVar[int]
    DARK_SITE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: int
    cluster_incarnation_id: int
    name: str
    helios_claimed: bool
    dark_site: bool
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., name: _Optional[str] = ..., helios_claimed: bool = ..., dark_site: bool = ...) -> None: ...
