from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScribeTestMetadataColumn(_message.Message):
    __slots__ = ("column_to_checksum",)
    class ColumnToChecksumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    COLUMN_TO_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    column_to_checksum: _containers.ScalarMap[int, bytes]
    def __init__(self, column_to_checksum: _Optional[_Mapping[int, bytes]] = ...) -> None: ...
