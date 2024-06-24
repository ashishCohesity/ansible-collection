from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
optional_uint64: _descriptor.FieldDescriptor
OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
optional_int64: _descriptor.FieldDescriptor

class OutOfOrderFields(_message.Message):
    __slots__ = ("optional_sint32", "optional_uint32", "optional_int32")
    Extensions: _python_message._ExtensionDict
    OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    optional_sint32: int
    optional_uint32: int
    optional_int32: int
    def __init__(self, optional_sint32: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_int32: _Optional[int] = ...) -> None: ...
