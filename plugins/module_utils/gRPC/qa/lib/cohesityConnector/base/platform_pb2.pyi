from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoragePolicy(_message.Message):
    __slots__ = ("enable_dedup", "inline_dedup", "enable_strong_encryption", "compression", "erasure_coding")
    ENABLE_DEDUP_FIELD_NUMBER: _ClassVar[int]
    INLINE_DEDUP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STRONG_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    ERASURE_CODING_FIELD_NUMBER: _ClassVar[int]
    enable_dedup: bool
    inline_dedup: bool
    enable_strong_encryption: bool
    compression: str
    erasure_coding: ErasureCodingInfo
    def __init__(self, enable_dedup: bool = ..., inline_dedup: bool = ..., enable_strong_encryption: bool = ..., compression: _Optional[str] = ..., erasure_coding: _Optional[_Union[ErasureCodingInfo, _Mapping]] = ...) -> None: ...

class ErasureCodingInfo(_message.Message):
    __slots__ = ("num_data_stripes", "num_coded_stripes", "erasure_code_delay_secs")
    NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
    NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
    ERASURE_CODE_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
    num_data_stripes: int
    num_coded_stripes: int
    erasure_code_delay_secs: int
    def __init__(self, num_data_stripes: _Optional[int] = ..., num_coded_stripes: _Optional[int] = ..., erasure_code_delay_secs: _Optional[int] = ...) -> None: ...
