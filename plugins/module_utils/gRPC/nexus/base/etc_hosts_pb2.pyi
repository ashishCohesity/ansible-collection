from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EtcHostEntryProto(_message.Message):
    __slots__ = ("ip", "domain_names", "description")
    IP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ip: str
    domain_names: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, ip: _Optional[str] = ..., domain_names: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

class EtcHostsProto(_message.Message):
    __slots__ = ("hosts", "gandalf_key")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[EtcHostEntryProto]
    gandalf_key: str
    def __init__(self, hosts: _Optional[_Iterable[_Union[EtcHostEntryProto, _Mapping]]] = ..., gandalf_key: _Optional[str] = ...) -> None: ...
