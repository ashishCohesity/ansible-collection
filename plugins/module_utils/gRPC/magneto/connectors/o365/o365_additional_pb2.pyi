from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365RegionProto(_message.Message):
    __slots__ = ("country",)
    class Country(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefault: _ClassVar[O365RegionProto.Country]
        kChina: _ClassVar[O365RegionProto.Country]
        kGermany: _ClassVar[O365RegionProto.Country]
        kUSDoD: _ClassVar[O365RegionProto.Country]
        kUSGccHigh: _ClassVar[O365RegionProto.Country]
    kDefault: O365RegionProto.Country
    kChina: O365RegionProto.Country
    kGermany: O365RegionProto.Country
    kUSDoD: O365RegionProto.Country
    kUSGccHigh: O365RegionProto.Country
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: O365RegionProto.Country
    def __init__(self, country: _Optional[_Union[O365RegionProto.Country, str]] = ...) -> None: ...
