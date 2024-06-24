from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestDocument(_message.Message):
    __slots__ = ("name", "size", "snapshot_info", "numbers_vec")
    class SnapshotInfo(_message.Message):
        __slots__ = ("type", "snapshot_time_secs")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kVMware: _ClassVar[TestDocument.SnapshotInfo.Type]
            kHyperV: _ClassVar[TestDocument.SnapshotInfo.Type]
        kVMware: TestDocument.SnapshotInfo.Type
        kHyperV: TestDocument.SnapshotInfo.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        type: TestDocument.SnapshotInfo.Type
        snapshot_time_secs: int
        def __init__(self, type: _Optional[_Union[TestDocument.SnapshotInfo.Type, str]] = ..., snapshot_time_secs: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    snapshot_info: _containers.RepeatedCompositeFieldContainer[TestDocument.SnapshotInfo]
    numbers_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., snapshot_info: _Optional[_Iterable[_Union[TestDocument.SnapshotInfo, _Mapping]]] = ..., numbers_vec: _Optional[_Iterable[int]] = ...) -> None: ...
