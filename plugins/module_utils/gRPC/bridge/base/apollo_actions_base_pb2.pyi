from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SnapTreeName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kBlobSnapTree: _ClassVar[SnapTreeName]
    kViewSnapTree: _ClassVar[SnapTreeName]
    kQuotaSnapTree: _ClassVar[SnapTreeName]
    kQuotaUsageSnapTree: _ClassVar[SnapTreeName]
    kAntivirusSnapTree: _ClassVar[SnapTreeName]
    kS3ObjectSnapTree: _ClassVar[SnapTreeName]
    kDirQuotaSnapTree: _ClassVar[SnapTreeName]
kBlobSnapTree: SnapTreeName
kViewSnapTree: SnapTreeName
kQuotaSnapTree: SnapTreeName
kQuotaUsageSnapTree: SnapTreeName
kAntivirusSnapTree: SnapTreeName
kS3ObjectSnapTree: SnapTreeName
kDirQuotaSnapTree: SnapTreeName
