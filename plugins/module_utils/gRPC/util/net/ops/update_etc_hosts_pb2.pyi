from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EtcHostEntry(_message.Message):
    __slots__ = ("ip", "domain_name")
    IP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ip: str
    domain_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip: _Optional[str] = ..., domain_name: _Optional[_Iterable[str]] = ...) -> None: ...

class ClusterGetHostsFile(_message.Message):
    __slots__ = ("hosts", "version")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[EtcHostEntry]
    version: int
    def __init__(self, hosts: _Optional[_Iterable[_Union[EtcHostEntry, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class ClusterUploadHostsFile(_message.Message):
    __slots__ = ("hosts", "validate", "version")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[EtcHostEntry]
    validate: bool
    version: int
    def __init__(self, hosts: _Optional[_Iterable[_Union[EtcHostEntry, _Mapping]]] = ..., validate: bool = ..., version: _Optional[int] = ...) -> None: ...
