from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Enum1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENUM1_ONE: _ClassVar[Enum1]
    ENUM1_TWO: _ClassVar[Enum1]
    ENUM1_THREE: _ClassVar[Enum1]
ENUM1_ONE: Enum1
ENUM1_TWO: Enum1
ENUM1_THREE: Enum1
STRING_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
string_ext_field: _descriptor.FieldDescriptor
INT_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
int_ext_field: _descriptor.FieldDescriptor
FIXED_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
fixed_ext_field: _descriptor.FieldDescriptor
MSG_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
msg_ext_field: _descriptor.FieldDescriptor

class Msg1(_message.Message):
    __slots__ = ("string_field",)
    Extensions: _python_message._ExtensionDict
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    string_field: str
    def __init__(self, string_field: _Optional[str] = ...) -> None: ...

class Msg1A(_message.Message):
    __slots__ = ()
    STRING_EXT2_FIELD_FIELD_NUMBER: _ClassVar[int]
    string_ext2_field: _descriptor.FieldDescriptor
    INT_EXT2_FIELD_FIELD_NUMBER: _ClassVar[int]
    int_ext2_field: _descriptor.FieldDescriptor
    FIXED_EXT2_FIELD_FIELD_NUMBER: _ClassVar[int]
    fixed_ext2_field: _descriptor.FieldDescriptor
    MSG_EXT2_FIELD_FIELD_NUMBER: _ClassVar[int]
    msg_ext2_field: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
