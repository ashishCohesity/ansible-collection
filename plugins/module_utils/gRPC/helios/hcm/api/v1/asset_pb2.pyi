from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotSetAssetType: _ClassVar[AssetType]
    Regular: _ClassVar[AssetType]
    DMaaS: _ClassVar[AssetType]
    RigelInDataCenter: _ClassVar[AssetType]
    RigelInAWSCloud: _ClassVar[AssetType]
    TenantSNI: _ClassVar[AssetType]
    Agent: _ClassVar[AssetType]
    IBMStorageProtect: _ClassVar[AssetType]

class CAChainType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotSetCAChainType: _ClassVar[CAChainType]
    ClientType: _ClassVar[CAChainType]
    TenantType: _ClassVar[CAChainType]
NotSetAssetType: AssetType
Regular: AssetType
DMaaS: AssetType
RigelInDataCenter: AssetType
RigelInAWSCloud: AssetType
TenantSNI: AssetType
Agent: AssetType
IBMStorageProtect: AssetType
NotSetCAChainType: CAChainType
ClientType: CAChainType
TenantType: CAChainType
