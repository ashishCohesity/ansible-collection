from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OldProto(_message.Message):
    __slots__ = ("nested_field", "int_field")
    class NestedProto(_message.Message):
        __slots__ = ("bytes_field",)
        BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
        bytes_field: bytes
        def __init__(self, bytes_field: _Optional[bytes] = ...) -> None: ...
    NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    nested_field: OldProto.NestedProto
    int_field: int
    def __init__(self, nested_field: _Optional[_Union[OldProto.NestedProto, _Mapping]] = ..., int_field: _Optional[int] = ...) -> None: ...

class NewProto(_message.Message):
    __slots__ = ("int_field", "bytes_field")
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    int_field: int
    bytes_field: int
    def __init__(self, int_field: _Optional[int] = ..., bytes_field: _Optional[int] = ...) -> None: ...
