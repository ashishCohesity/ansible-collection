from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RestApiError(_message.Message):
    __slots__ = ("type", "title", "status", "detail", "instance", "arguments")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    type: str
    title: str
    status: int
    detail: str
    instance: str
    arguments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., title: _Optional[str] = ..., status: _Optional[int] = ..., detail: _Optional[str] = ..., instance: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...

class TypeUriPrefix(_message.Message):
    __slots__ = ("patch_exec", "patch_server")
    PATCH_EXEC_FIELD_NUMBER: _ClassVar[int]
    PATCH_SERVER_FIELD_NUMBER: _ClassVar[int]
    patch_exec: str
    patch_server: str
    def __init__(self, patch_exec: _Optional[str] = ..., patch_server: _Optional[str] = ...) -> None: ...
