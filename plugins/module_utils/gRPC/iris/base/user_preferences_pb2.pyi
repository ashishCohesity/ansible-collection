from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserPreferencesProto(_message.Message):
    __slots__ = ("user_preferences_list", "version")
    USER_PREFERENCES_LIST_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    user_preferences_list: _containers.RepeatedCompositeFieldContainer[UserPreferences]
    version: int
    def __init__(self, user_preferences_list: _Optional[_Iterable[_Union[UserPreferences, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class UserPreferences(_message.Message):
    __slots__ = ("sid", "preference_list")
    SID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    sid: str
    preference_list: _containers.RepeatedCompositeFieldContainer[Preference]
    def __init__(self, sid: _Optional[str] = ..., preference_list: _Optional[_Iterable[_Union[Preference, _Mapping]]] = ...) -> None: ...

class Preference(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
