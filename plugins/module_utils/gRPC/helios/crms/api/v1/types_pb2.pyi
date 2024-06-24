from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EntitlementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kEntitlementTypeNotSet: _ClassVar[EntitlementType]
    kDMaas: _ClassVar[EntitlementType]
    kFortnox: _ClassVar[EntitlementType]
    kDataHawk: _ClassVar[EntitlementType]

class OfferingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kOfferingTypeNotSet: _ClassVar[OfferingType]
    kDataProtect: _ClassVar[OfferingType]
    kSiteContinuity: _ClassVar[OfferingType]
    kRansomware: _ClassVar[OfferingType]
    kFortKnox: _ClassVar[OfferingType]
    kDataGovern: _ClassVar[OfferingType]
    kThreatProtection: _ClassVar[OfferingType]
    kClassification: _ClassVar[OfferingType]
kEntitlementTypeNotSet: EntitlementType
kDMaas: EntitlementType
kFortnox: EntitlementType
kDataHawk: EntitlementType
kOfferingTypeNotSet: OfferingType
kDataProtect: OfferingType
kSiteContinuity: OfferingType
kRansomware: OfferingType
kFortKnox: OfferingType
kDataGovern: OfferingType
kThreatProtection: OfferingType
kClassification: OfferingType
