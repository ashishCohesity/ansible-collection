from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ("oid", "oid_ref", "username", "password")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    username: str
    password: str
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SubnetInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "gateway_ip", "mask_ip")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    MASK_IP_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    gateway_ip: str
    mask_ip: str
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., gateway_ip: _Optional[str] = ..., mask_ip: _Optional[str] = ...) -> None: ...
