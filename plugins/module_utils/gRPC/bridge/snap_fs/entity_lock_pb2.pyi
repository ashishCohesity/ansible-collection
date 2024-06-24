from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityLockMetadataProto(_message.Message):
    __slots__ = ("locks",)
    class EntityLockStateProto(_message.Message):
        __slots__ = ("lock_ranges",)
        class LockRangeProto(_message.Message):
            __slots__ = ("offset", "length", "is_exclusive")
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            offset: int
            length: int
            is_exclusive: bool
            def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., is_exclusive: bool = ...) -> None: ...
        LOCK_RANGES_FIELD_NUMBER: _ClassVar[int]
        lock_ranges: _containers.RepeatedCompositeFieldContainer[EntityLockMetadataProto.EntityLockStateProto.LockRangeProto]
        def __init__(self, lock_ranges: _Optional[_Iterable[_Union[EntityLockMetadataProto.EntityLockStateProto.LockRangeProto, _Mapping]]] = ...) -> None: ...
    class LocksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EntityLockMetadataProto.EntityLockStateProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EntityLockMetadataProto.EntityLockStateProto, _Mapping]] = ...) -> None: ...
    LOCKS_FIELD_NUMBER: _ClassVar[int]
    locks: _containers.MessageMap[str, EntityLockMetadataProto.EntityLockStateProto]
    def __init__(self, locks: _Optional[_Mapping[str, EntityLockMetadataProto.EntityLockStateProto]] = ...) -> None: ...
