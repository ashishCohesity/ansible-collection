from magneto.base.entities import san_entity_pb2 as _san_entity_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProtectionGroup(_message.Message):
    __slots__ = ("name", "source", "version")
    class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[ProtectionGroup.Version]
        kNameIdentifier: _ClassVar[ProtectionGroup.Version]
    kUnused: ProtectionGroup.Version
    kNameIdentifier: ProtectionGroup.Version
    PROTECTION_GROUP_FIELD_NUMBER: _ClassVar[int]
    protection_group: _descriptor.FieldDescriptor
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    source: str
    version: ProtectionGroup.Version
    def __init__(self, name: _Optional[str] = ..., source: _Optional[str] = ..., version: _Optional[_Union[ProtectionGroup.Version, str]] = ...) -> None: ...
