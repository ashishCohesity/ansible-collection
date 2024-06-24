from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFlagSetting(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TestRepeatedProto(_message.Message):
    __slots__ = ("gflag_setting_vec",)
    GFLAG_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    gflag_setting_vec: _containers.RepeatedCompositeFieldContainer[GFlagSetting]
    def __init__(self, gflag_setting_vec: _Optional[_Iterable[_Union[GFlagSetting, _Mapping]]] = ...) -> None: ...
