from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UtilityAppInfo(_message.Message):
    __slots__ = ("app_id", "app_version_id", "name", "version")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    app_version_id: int
    name: str
    version: str
    def __init__(self, app_id: _Optional[int] = ..., app_version_id: _Optional[int] = ..., name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class UtilityApps(_message.Message):
    __slots__ = ("app_info_vec",)
    APP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    app_info_vec: _containers.RepeatedCompositeFieldContainer[UtilityAppInfo]
    def __init__(self, app_info_vec: _Optional[_Iterable[_Union[UtilityAppInfo, _Mapping]]] = ...) -> None: ...
