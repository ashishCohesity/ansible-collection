from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppTdmTaskEnumProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[AppTdmTaskEnumProto.Type]
        kProtectDatabaseClones: _ClassVar[AppTdmTaskEnumProto.Type]
        kProtectDatabaseClonesBatch: _ClassVar[AppTdmTaskEnumProto.Type]
        kDatabaseClone: _ClassVar[AppTdmTaskEnumProto.Type]
        kRefreshDatabaseClone: _ClassVar[AppTdmTaskEnumProto.Type]
        kCloneOfDatabaseClone: _ClassVar[AppTdmTaskEnumProto.Type]
        kRewindDatabaseClone: _ClassVar[AppTdmTaskEnumProto.Type]
    kUnused: AppTdmTaskEnumProto.Type
    kProtectDatabaseClones: AppTdmTaskEnumProto.Type
    kProtectDatabaseClonesBatch: AppTdmTaskEnumProto.Type
    kDatabaseClone: AppTdmTaskEnumProto.Type
    kRefreshDatabaseClone: AppTdmTaskEnumProto.Type
    kCloneOfDatabaseClone: AppTdmTaskEnumProto.Type
    kRewindDatabaseClone: AppTdmTaskEnumProto.Type
    def __init__(self) -> None: ...
