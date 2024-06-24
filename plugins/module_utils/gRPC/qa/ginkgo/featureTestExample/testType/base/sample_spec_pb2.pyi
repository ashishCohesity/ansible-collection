from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WindowsCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class WindowsTestServer(_message.Message):
    __slots__ = ("windows_host", "windows_credentials")
    WINDOWS_HOST_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    windows_host: str
    windows_credentials: WindowsCredentials
    def __init__(self, windows_host: _Optional[str] = ..., windows_credentials: _Optional[_Union[WindowsCredentials, _Mapping]] = ...) -> None: ...
