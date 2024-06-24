from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SizeInfo(_message.Message):
    __slots__ = ("size_bytes", "computation_method")
    class ComputationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kProvisionedLogicalSize: _ClassVar[SizeInfo.ComputationMethod]
        kProvisionedPhysicalSize_DEPRECATED: _ClassVar[SizeInfo.ComputationMethod]
        kProtectedPhysicalSize_DEPRECATED: _ClassVar[SizeInfo.ComputationMethod]
        kProtectedLogicalSize: _ClassVar[SizeInfo.ComputationMethod]
        kHypervisorGuestOSVolumesUsedBytes: _ClassVar[SizeInfo.ComputationMethod]
    kProvisionedLogicalSize: SizeInfo.ComputationMethod
    kProvisionedPhysicalSize_DEPRECATED: SizeInfo.ComputationMethod
    kProtectedPhysicalSize_DEPRECATED: SizeInfo.ComputationMethod
    kProtectedLogicalSize: SizeInfo.ComputationMethod
    kHypervisorGuestOSVolumesUsedBytes: SizeInfo.ComputationMethod
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    size_bytes: int
    computation_method: SizeInfo.ComputationMethod
    def __init__(self, size_bytes: _Optional[int] = ..., computation_method: _Optional[_Union[SizeInfo.ComputationMethod, str]] = ...) -> None: ...
