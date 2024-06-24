from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DurableShardedHashMapLogRecordHeader(_message.Message):
    __slots__ = ("record_type", "key_size", "value_size", "multi_erase_key_length")
    class RecordType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpdateKey: _ClassVar[DurableShardedHashMapLogRecordHeader.RecordType]
        kEraseKey: _ClassVar[DurableShardedHashMapLogRecordHeader.RecordType]
        kMultiEraseKey: _ClassVar[DurableShardedHashMapLogRecordHeader.RecordType]
    kUpdateKey: DurableShardedHashMapLogRecordHeader.RecordType
    kEraseKey: DurableShardedHashMapLogRecordHeader.RecordType
    kMultiEraseKey: DurableShardedHashMapLogRecordHeader.RecordType
    RECORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_SIZE_FIELD_NUMBER: _ClassVar[int]
    VALUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MULTI_ERASE_KEY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    record_type: DurableShardedHashMapLogRecordHeader.RecordType
    key_size: int
    value_size: int
    multi_erase_key_length: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, record_type: _Optional[_Union[DurableShardedHashMapLogRecordHeader.RecordType, str]] = ..., key_size: _Optional[int] = ..., value_size: _Optional[int] = ..., multi_erase_key_length: _Optional[_Iterable[int]] = ...) -> None: ...
