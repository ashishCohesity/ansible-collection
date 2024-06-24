from magneto.base.entities import oracle_pb2 as _oracle_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOsBased: _ClassVar[AuthType.Type]
        kUserStringBased: _ClassVar[AuthType.Type]
    kOsBased: AuthType.Type
    kUserStringBased: AuthType.Type
    def __init__(self) -> None: ...

class DatabaseInfoProto(_message.Message):
    __slots__ = ("auth_type", "username", "password", "encrypted_password", "uuid", "unique_name", "db_name", "db_entity_info")
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    auth_type: AuthType.Type
    username: str
    password: str
    encrypted_password: bytes
    uuid: str
    unique_name: str
    db_name: str
    db_entity_info: _oracle_pb2.DBEntityInfo
    def __init__(self, auth_type: _Optional[_Union[AuthType.Type, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., uuid: _Optional[str] = ..., unique_name: _Optional[str] = ..., db_name: _Optional[str] = ..., db_entity_info: _Optional[_Union[_oracle_pb2.DBEntityInfo, _Mapping]] = ...) -> None: ...
