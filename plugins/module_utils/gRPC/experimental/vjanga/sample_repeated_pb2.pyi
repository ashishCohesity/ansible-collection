from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleRepeated(_message.Message):
    __slots__ = ("string_vec",)
    class SimpleString(_message.Message):
        __slots__ = ("msg",)
        MSG_FIELD_NUMBER: _ClassVar[int]
        msg: bytes
        def __init__(self, msg: _Optional[bytes] = ...) -> None: ...
    STRING_VEC_FIELD_NUMBER: _ClassVar[int]
    string_vec: _containers.RepeatedCompositeFieldContainer[SampleRepeated.SimpleString]
    def __init__(self, string_vec: _Optional[_Iterable[_Union[SampleRepeated.SimpleString, _Mapping]]] = ...) -> None: ...
