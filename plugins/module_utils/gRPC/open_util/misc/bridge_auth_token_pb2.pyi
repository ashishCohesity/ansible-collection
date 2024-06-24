from configs import service_auth_config_pb2 as _service_auth_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthTokenProto(_message.Message):
    __slots__ = ("version", "creation_time", "encrypted_secret", "client", "client_id")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_SECRET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    version: int
    creation_time: int
    encrypted_secret: bytes
    client: _service_auth_config_pb2.ServiceAuthConfigProto.ClientComponent
    client_id: _service_auth_config_pb2.ServiceAuthConfigProto.ClientID
    def __init__(self, version: _Optional[int] = ..., creation_time: _Optional[int] = ..., encrypted_secret: _Optional[bytes] = ..., client: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto.ClientComponent, str]] = ..., client_id: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto.ClientID, _Mapping]] = ...) -> None: ...
