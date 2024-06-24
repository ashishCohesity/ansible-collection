from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertTypeProto(_message.Message):
    __slots__ = ("id",)
    class Id(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kKeyCreated: _ClassVar[AlertTypeProto.Id]
        kKeyRotated: _ClassVar[AlertTypeProto.Id]
        kKeyRotationPolicyChanged: _ClassVar[AlertTypeProto.Id]
        kKMSCreated: _ClassVar[AlertTypeProto.Id]
        kKMSDestroyed: _ClassVar[AlertTypeProto.Id]
        kKMSUnreachable: _ClassVar[AlertTypeProto.Id]
        kKMSCertificateWillExpire: _ClassVar[AlertTypeProto.Id]
        kKMSCertificateExpiration: _ClassVar[AlertTypeProto.Id]
        kKMSError: _ClassVar[AlertTypeProto.Id]
        kKMSFailover: _ClassVar[AlertTypeProto.Id]
    kKeyCreated: AlertTypeProto.Id
    kKeyRotated: AlertTypeProto.Id
    kKeyRotationPolicyChanged: AlertTypeProto.Id
    kKMSCreated: AlertTypeProto.Id
    kKMSDestroyed: AlertTypeProto.Id
    kKMSUnreachable: AlertTypeProto.Id
    kKMSCertificateWillExpire: AlertTypeProto.Id
    kKMSCertificateExpiration: AlertTypeProto.Id
    kKMSError: AlertTypeProto.Id
    kKMSFailover: AlertTypeProto.Id
    ID_FIELD_NUMBER: _ClassVar[int]
    id: AlertTypeProto.Id
    def __init__(self, id: _Optional[_Union[AlertTypeProto.Id, str]] = ...) -> None: ...
