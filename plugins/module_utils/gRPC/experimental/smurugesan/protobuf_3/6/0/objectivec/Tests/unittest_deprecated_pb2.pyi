from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENUM1_ONE: _ClassVar[Enum1]
    ENUM1_TWO: _ClassVar[Enum1]
    ENUM1_THREE: _ClassVar[Enum1]

class Enum2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENUM2_ONE: _ClassVar[Enum2]
    ENUM2_TWO: _ClassVar[Enum2]
    ENUM2_THREE: _ClassVar[Enum2]
ENUM1_ONE: Enum1
ENUM1_TWO: Enum1
ENUM1_THREE: Enum1
ENUM2_ONE: Enum2
ENUM2_TWO: Enum2
ENUM2_THREE: Enum2
STRING_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
string_ext_field: _descriptor.FieldDescriptor
INT_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
int_ext_field: _descriptor.FieldDescriptor
FIXED_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
fixed_ext_field: _descriptor.FieldDescriptor
MSG_EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
msg_ext_field: _descriptor.FieldDescriptor

class Msg1(_message.Message):
    __slots__ = ("string_field", "int_field", "fixed_field", "msg_field")
    Extensions: _python_message._ExtensionDict
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_FIELD_NUMBER: _ClassVar[int]
    string_field: str
    int_field: int
    fixed_field: _containers.RepeatedScalarFieldContainer[int]
    msg_field: Msg1
    def __init__(self, string_field: _Optional[str] = ..., int_field: _Optional[int] = ..., fixed_field: _Optional[_Iterable[int]] = ..., msg_field: _Optional[_Union[Msg1, _Mapping]] = ...) -> None: ...

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

class Msg2(_message.Message):
    __slots__ = ("string_field", "int_field", "fixed_field")
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_FIELD_NUMBER: _ClassVar[int]
    string_field: str
    int_field: int
    fixed_field: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, string_field: _Optional[str] = ..., int_field: _Optional[int] = ..., fixed_field: _Optional[_Iterable[int]] = ...) -> None: ...
