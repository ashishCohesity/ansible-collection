from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosTenant(_message.Message):
    __slots__ = ("helios_tenant_id",)
    HELIOS_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    helios_tenant_id: str
    def __init__(self, helios_tenant_id: _Optional[str] = ...) -> None: ...

class HeliosTenants(_message.Message):
    __slots__ = ("tenants_list",)
    TENANTS_LIST_FIELD_NUMBER: _ClassVar[int]
    tenants_list: _containers.RepeatedCompositeFieldContainer[HeliosTenant]
    def __init__(self, tenants_list: _Optional[_Iterable[_Union[HeliosTenant, _Mapping]]] = ...) -> None: ...
