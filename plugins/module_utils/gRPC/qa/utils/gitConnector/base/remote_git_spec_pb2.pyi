from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RemoteConnectionParams(_message.Message):
    __slots__ = ("endpoint", "remote_cred")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CRED_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    remote_cred: RemoteCredentials
    def __init__(self, endpoint: _Optional[str] = ..., remote_cred: _Optional[_Union[RemoteCredentials, _Mapping]] = ...) -> None: ...

class GitRemote(_message.Message):
    __slots__ = ("machine", "base_path")
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    machine: RemoteConnectionParams
    base_path: str
    def __init__(self, machine: _Optional[_Union[RemoteConnectionParams, _Mapping]] = ..., base_path: _Optional[str] = ...) -> None: ...
