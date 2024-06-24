from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sentinel(_message.Message):
    __slots__ = ("default_int32", "default_int64", "default_unit32", "default_uint64", "default_string", "default_bool", "default_float", "default_double", "default_bytes")
    DEFAULT_INT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UNIT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UINT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BOOL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BYTES_FIELD_NUMBER: _ClassVar[int]
    default_int32: int
    default_int64: int
    default_unit32: int
    default_uint64: int
    default_string: str
    default_bool: bool
    default_float: float
    default_double: float
    default_bytes: bytes
    def __init__(self, default_int32: _Optional[int] = ..., default_int64: _Optional[int] = ..., default_unit32: _Optional[int] = ..., default_uint64: _Optional[int] = ..., default_string: _Optional[str] = ..., default_bool: bool = ..., default_float: _Optional[float] = ..., default_double: _Optional[float] = ..., default_bytes: _Optional[bytes] = ...) -> None: ...
