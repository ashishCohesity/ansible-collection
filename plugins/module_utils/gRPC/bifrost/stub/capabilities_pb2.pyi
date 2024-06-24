from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CapabilityProto(_message.Message):
    __slots__ = ("capabilities",)
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BR_kVMWare_kVCenter: _ClassVar[CapabilityProto.Capability]
        BR_kVMWare_kStandaloneHost: _ClassVar[CapabilityProto.Capability]
        BR_kPhysical: _ClassVar[CapabilityProto.Capability]
        BR_kPhysicalFiles: _ClassVar[CapabilityProto.Capability]
        BR_kGenericNas: _ClassVar[CapabilityProto.Capability]
        BR_kIsilon: _ClassVar[CapabilityProto.Capability]
        BR_kSQL_kPhysical: _ClassVar[CapabilityProto.Capability]
        BR_kSQL_kVMWare: _ClassVar[CapabilityProto.Capability]
        BR_kPhysical_kOracle: _ClassVar[CapabilityProto.Capability]
        BR_kView: _ClassVar[CapabilityProto.Capability]
        BR_kHyperV_kStandaloneHost: _ClassVar[CapabilityProto.Capability]
        BR_kHyperV_kStandaloneCluster: _ClassVar[CapabilityProto.Capability]
        BR_kHyperV_kSCVMMServer: _ClassVar[CapabilityProto.Capability]
        BR_kUda: _ClassVar[CapabilityProto.Capability]
        BR_kNetapp_kCluster: _ClassVar[CapabilityProto.Capability]
        BR_kNetapp_kVserver: _ClassVar[CapabilityProto.Capability]
        BR_kAESGCM: _ClassVar[CapabilityProto.Capability]
        BR_kVMWare_NVRAM: _ClassVar[CapabilityProto.Capability]
        PKIRigel_kAgent: _ClassVar[CapabilityProto.Capability]
    BR_kVMWare_kVCenter: CapabilityProto.Capability
    BR_kVMWare_kStandaloneHost: CapabilityProto.Capability
    BR_kPhysical: CapabilityProto.Capability
    BR_kPhysicalFiles: CapabilityProto.Capability
    BR_kGenericNas: CapabilityProto.Capability
    BR_kIsilon: CapabilityProto.Capability
    BR_kSQL_kPhysical: CapabilityProto.Capability
    BR_kSQL_kVMWare: CapabilityProto.Capability
    BR_kPhysical_kOracle: CapabilityProto.Capability
    BR_kView: CapabilityProto.Capability
    BR_kHyperV_kStandaloneHost: CapabilityProto.Capability
    BR_kHyperV_kStandaloneCluster: CapabilityProto.Capability
    BR_kHyperV_kSCVMMServer: CapabilityProto.Capability
    BR_kUda: CapabilityProto.Capability
    BR_kNetapp_kCluster: CapabilityProto.Capability
    BR_kNetapp_kVserver: CapabilityProto.Capability
    BR_kAESGCM: CapabilityProto.Capability
    BR_kVMWare_NVRAM: CapabilityProto.Capability
    PKIRigel_kAgent: CapabilityProto.Capability
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedScalarFieldContainer[CapabilityProto.Capability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[CapabilityProto.Capability, str]]] = ...) -> None: ...
