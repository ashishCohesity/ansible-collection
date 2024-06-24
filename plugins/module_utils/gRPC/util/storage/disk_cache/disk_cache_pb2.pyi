from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheWALRecord(_message.Message):
    __slots__ = ("file_vec",)
    class Entry(_message.Message):
        __slots__ = ("key", "adler_checksum", "block_number", "value_size", "last_access_time_usecs")
        KEY_FIELD_NUMBER: _ClassVar[int]
        ADLER_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        VALUE_SIZE_FIELD_NUMBER: _ClassVar[int]
        LAST_ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        key: bytes
        adler_checksum: int
        block_number: int
        value_size: int
        last_access_time_usecs: int
        def __init__(self, key: _Optional[bytes] = ..., adler_checksum: _Optional[int] = ..., block_number: _Optional[int] = ..., value_size: _Optional[int] = ..., last_access_time_usecs: _Optional[int] = ...) -> None: ...
    class BlockRange(_message.Message):
        __slots__ = ("start_block", "num_blocks")
        START_BLOCK_FIELD_NUMBER: _ClassVar[int]
        NUM_BLOCKS_FIELD_NUMBER: _ClassVar[int]
        start_block: int
        num_blocks: int
        def __init__(self, start_block: _Optional[int] = ..., num_blocks: _Optional[int] = ...) -> None: ...
    class File(_message.Message):
        __slots__ = ("path", "block_size", "epoch", "entry_vec", "free_block_range_vec")
        PATH_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
        FREE_BLOCK_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        path: str
        block_size: int
        epoch: int
        entry_vec: _containers.RepeatedCompositeFieldContainer[CacheWALRecord.Entry]
        free_block_range_vec: _containers.RepeatedCompositeFieldContainer[CacheWALRecord.BlockRange]
        def __init__(self, path: _Optional[str] = ..., block_size: _Optional[int] = ..., epoch: _Optional[int] = ..., entry_vec: _Optional[_Iterable[_Union[CacheWALRecord.Entry, _Mapping]]] = ..., free_block_range_vec: _Optional[_Iterable[_Union[CacheWALRecord.BlockRange, _Mapping]]] = ...) -> None: ...
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    file_vec: _containers.RepeatedCompositeFieldContainer[CacheWALRecord.File]
    def __init__(self, file_vec: _Optional[_Iterable[_Union[CacheWALRecord.File, _Mapping]]] = ...) -> None: ...
