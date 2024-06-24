from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JsonInt64TesterProto(_message.Message):
    __slots__ = ("singular_field", "repeated_field", "field_without_options", "repeated_field_without_options")
    SINGULAR_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_WITHOUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELD_WITHOUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    singular_field: int
    repeated_field: _containers.RepeatedScalarFieldContainer[int]
    field_without_options: int
    repeated_field_without_options: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, singular_field: _Optional[int] = ..., repeated_field: _Optional[_Iterable[int]] = ..., field_without_options: _Optional[int] = ..., repeated_field_without_options: _Optional[_Iterable[int]] = ...) -> None: ...
