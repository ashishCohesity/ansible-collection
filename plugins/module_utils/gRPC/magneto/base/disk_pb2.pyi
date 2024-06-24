from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class DiskAreaProto(_message.Message):
    __slots__ = ("start_pos", "length", "image_offset", "disk_name", "token", "region", "token_vec", "is_disk_area_zero_filled")
    Extensions: _python_message._ExtensionDict
    START_POS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_DISK_AREA_ZERO_FILLED_FIELD_NUMBER: _ClassVar[int]
    start_pos: int
    length: int
    image_offset: int
    disk_name: str
    token: str
    region: str
    token_vec: _containers.RepeatedScalarFieldContainer[str]
    is_disk_area_zero_filled: bool
    def __init__(self, start_pos: _Optional[int] = ..., length: _Optional[int] = ..., image_offset: _Optional[int] = ..., disk_name: _Optional[str] = ..., token: _Optional[str] = ..., region: _Optional[str] = ..., token_vec: _Optional[_Iterable[str]] = ..., is_disk_area_zero_filled: bool = ...) -> None: ...

class DiskAreaListProto(_message.Message):
    __slots__ = ("area_vec", "total_disk_area_size", "size", "max_disk_area_size")
    AREA_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_AREA_SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_AREA_SIZE_FIELD_NUMBER: _ClassVar[int]
    area_vec: _containers.RepeatedCompositeFieldContainer[DiskAreaProto]
    total_disk_area_size: int
    size: int
    max_disk_area_size: int
    def __init__(self, area_vec: _Optional[_Iterable[_Union[DiskAreaProto, _Mapping]]] = ..., total_disk_area_size: _Optional[int] = ..., size: _Optional[int] = ..., max_disk_area_size: _Optional[int] = ...) -> None: ...
