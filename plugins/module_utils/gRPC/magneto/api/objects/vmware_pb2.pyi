from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MORef(_message.Message):
    __slots__ = ("item", "type")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    item: str
    type: str
    def __init__(self, item: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("type", "uuid", "vm_moref")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVcenter: _ClassVar[Object.Type]
        kVirtualMachine: _ClassVar[Object.Type]
    kVcenter: Object.Type
    kVirtualMachine: Object.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    type: Object.Type
    uuid: str
    vm_moref: MORef
    def __init__(self, type: _Optional[_Union[Object.Type, str]] = ..., uuid: _Optional[str] = ..., vm_moref: _Optional[_Union[MORef, _Mapping]] = ...) -> None: ...
