from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalKMSState(_message.Message):
    __slots__ = ("key_object_vec",)
    class KeyObject(_message.Message):
        __slots__ = ("uid", "key")
        UID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        uid: bytes
        key: bytes
        def __init__(self, uid: _Optional[bytes] = ..., key: _Optional[bytes] = ...) -> None: ...
    KEY_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    key_object_vec: _containers.RepeatedCompositeFieldContainer[InternalKMSState.KeyObject]
    def __init__(self, key_object_vec: _Optional[_Iterable[_Union[InternalKMSState.KeyObject, _Mapping]]] = ...) -> None: ...
