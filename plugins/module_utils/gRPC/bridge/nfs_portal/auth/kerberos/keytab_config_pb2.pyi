from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeytabProto(_message.Message):
    __slots__ = ("keytab_content",)
    KEYTAB_CONTENT_FIELD_NUMBER: _ClassVar[int]
    keytab_content: str
    def __init__(self, keytab_content: _Optional[str] = ...) -> None: ...

class KeytabConfigProto(_message.Message):
    __slots__ = ("realm_2_keytab_map",)
    class Realm2KeytabMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: KeytabProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[KeytabProto, _Mapping]] = ...) -> None: ...
    REALM_2_KEYTAB_MAP_FIELD_NUMBER: _ClassVar[int]
    realm_2_keytab_map: _containers.MessageMap[str, KeytabProto]
    def __init__(self, realm_2_keytab_map: _Optional[_Mapping[str, KeytabProto]] = ...) -> None: ...
