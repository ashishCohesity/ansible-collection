from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AccessProtocol(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAccessProtocolAll: _ClassVar[AccessProtocol.Type]
        kAccessProtocolNFSOnly: _ClassVar[AccessProtocol.Type]
        kAccessProtocolSMBOnly: _ClassVar[AccessProtocol.Type]
        kAccessProtocolS3Only: _ClassVar[AccessProtocol.Type]
        kAccessProtocolNFS3Only: _ClassVar[AccessProtocol.Type]
        kAccessProtocolNFS4Only: _ClassVar[AccessProtocol.Type]
        kAccessProtocolUnknown: _ClassVar[AccessProtocol.Type]
        kAccessProtocolSwiftOnly: _ClassVar[AccessProtocol.Type]
    kAccessProtocolAll: AccessProtocol.Type
    kAccessProtocolNFSOnly: AccessProtocol.Type
    kAccessProtocolSMBOnly: AccessProtocol.Type
    kAccessProtocolS3Only: AccessProtocol.Type
    kAccessProtocolNFS3Only: AccessProtocol.Type
    kAccessProtocolNFS4Only: AccessProtocol.Type
    kAccessProtocolUnknown: AccessProtocol.Type
    kAccessProtocolSwiftOnly: AccessProtocol.Type
    def __init__(self) -> None: ...

class DataLock(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCompliance: _ClassVar[DataLock.Type]
        kEnterprise: _ClassVar[DataLock.Type]
        kNone: _ClassVar[DataLock.Type]
    kCompliance: DataLock.Type
    kEnterprise: DataLock.Type
    kNone: DataLock.Type
    def __init__(self) -> None: ...
