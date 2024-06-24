from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NLMLockInfo(_message.Message):
    __slots__ = ("locks", "view_id", "root_inode_id", "entity_id")
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
        lock_ranges: _containers.RepeatedCompositeFieldContainer[NLMLockInfo.EntityLockStateProto.LockRangeProto]
        def __init__(self, lock_ranges: _Optional[_Iterable[_Union[NLMLockInfo.EntityLockStateProto.LockRangeProto, _Mapping]]] = ...) -> None: ...
    class LocksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NLMLockInfo.EntityLockStateProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NLMLockInfo.EntityLockStateProto, _Mapping]] = ...) -> None: ...
    LOCKS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    locks: _containers.MessageMap[str, NLMLockInfo.EntityLockStateProto]
    view_id: int
    root_inode_id: int
    entity_id: int
    def __init__(self, locks: _Optional[_Mapping[str, NLMLockInfo.EntityLockStateProto]] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...

class ListNLMLocksResult(_message.Message):
    __slots__ = ("result_vec", "cookie")
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[NLMLockInfo]
    cookie: str
    def __init__(self, result_vec: _Optional[_Iterable[_Union[NLMLockInfo, _Mapping]]] = ..., cookie: _Optional[str] = ...) -> None: ...
