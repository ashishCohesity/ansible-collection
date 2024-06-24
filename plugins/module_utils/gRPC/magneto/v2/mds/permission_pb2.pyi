from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityPermissionInfo(_message.Message):
    __slots__ = ("tenant_id", "sid")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    sid: _permissions_external_pb2.SID
    def __init__(self, tenant_id: _Optional[str] = ..., sid: _Optional[_Union[_permissions_external_pb2.SID, _Mapping]] = ...) -> None: ...
