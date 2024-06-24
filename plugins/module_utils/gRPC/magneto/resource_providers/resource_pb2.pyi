from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ResourceProto.Type]
        kBackupControlPathSlot: _ClassVar[ResourceProto.Type]
        kBackupDataPathSlot: _ClassVar[ResourceProto.Type]
        kBackupExternalEntitySlot: _ClassVar[ResourceProto.Type]
        kBackupBifrostSlot: _ClassVar[ResourceProto.Type]
        kO365Application: _ClassVar[ResourceProto.Type]
        kLogBackupExternalEntitySlot: _ClassVar[ResourceProto.Type]
        kRestoreExternalEntitySlot: _ClassVar[ResourceProto.Type]
        kAnyJobExternalEntitySlot: _ClassVar[ResourceProto.Type]
        kBifrostDiskSlot: _ClassVar[ResourceProto.Type]
        kPowerShellSlot: _ClassVar[ResourceProto.Type]
    kInvalid: ResourceProto.Type
    kBackupControlPathSlot: ResourceProto.Type
    kBackupDataPathSlot: ResourceProto.Type
    kBackupExternalEntitySlot: ResourceProto.Type
    kBackupBifrostSlot: ResourceProto.Type
    kO365Application: ResourceProto.Type
    kLogBackupExternalEntitySlot: ResourceProto.Type
    kRestoreExternalEntitySlot: ResourceProto.Type
    kAnyJobExternalEntitySlot: ResourceProto.Type
    kBifrostDiskSlot: ResourceProto.Type
    kPowerShellSlot: ResourceProto.Type
    def __init__(self) -> None: ...

class ResourceProviderProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ResourceProviderProto.Type]
        kMagnetoSlave: _ClassVar[ResourceProviderProto.Type]
        kBridge: _ClassVar[ResourceProviderProto.Type]
        kExternalEntity: _ClassVar[ResourceProviderProto.Type]
        kBifrost: _ClassVar[ResourceProviderProto.Type]
    kInvalid: ResourceProviderProto.Type
    kMagnetoSlave: ResourceProviderProto.Type
    kBridge: ResourceProviderProto.Type
    kExternalEntity: ResourceProviderProto.Type
    kBifrost: ResourceProviderProto.Type
    def __init__(self) -> None: ...

class ResourceProviderTagProto(_message.Message):
    __slots__ = ()
    class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ResourceProviderTagProto.Key]
        kProviderType: _ClassVar[ResourceProviderTagProto.Key]
        kFiberChannel: _ClassVar[ResourceProviderTagProto.Key]
    kInvalid: ResourceProviderTagProto.Key
    kProviderType: ResourceProviderTagProto.Key
    kFiberChannel: ResourceProviderTagProto.Key
    def __init__(self) -> None: ...
