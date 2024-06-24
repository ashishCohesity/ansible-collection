from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoPackageEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PACKAGE_VALUE_0: _ClassVar[NoPackageEnum]
    NO_PACKAGE_VALUE_1: _ClassVar[NoPackageEnum]
NO_PACKAGE_VALUE_0: NoPackageEnum
NO_PACKAGE_VALUE_1: NoPackageEnum

class NoPackageMessage(_message.Message):
    __slots__ = ("no_package_enum",)
    NO_PACKAGE_ENUM_FIELD_NUMBER: _ClassVar[int]
    no_package_enum: NoPackageEnum
    def __init__(self, no_package_enum: _Optional[_Union[NoPackageEnum, str]] = ...) -> None: ...
