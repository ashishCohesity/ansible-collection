from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "product_version")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kServer: _ClassVar[Entity.Type]
    kServer: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_VERSION_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    product_version: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., product_version: _Optional[str] = ...) -> None: ...
