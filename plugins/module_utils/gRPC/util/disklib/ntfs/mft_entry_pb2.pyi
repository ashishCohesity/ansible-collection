from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MFTEntryProto(_message.Message):
    __slots__ = ("mft_reference", "is_file", "file_names", "size_bytes", "mtime_usecs", "physical_offset")
    class NTFSNamespace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPosix: _ClassVar[MFTEntryProto.NTFSNamespace]
        kWin32: _ClassVar[MFTEntryProto.NTFSNamespace]
        kDOS: _ClassVar[MFTEntryProto.NTFSNamespace]
        kWin32AndDOS: _ClassVar[MFTEntryProto.NTFSNamespace]
    kPosix: MFTEntryProto.NTFSNamespace
    kWin32: MFTEntryProto.NTFSNamespace
    kDOS: MFTEntryProto.NTFSNamespace
    kWin32AndDOS: MFTEntryProto.NTFSNamespace
    class FileName(_message.Message):
        __slots__ = ("name", "parent_mft_reference", "file_namespace", "parent_path")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_MFT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
        FILE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        parent_mft_reference: int
        file_namespace: MFTEntryProto.NTFSNamespace
        parent_path: str
        def __init__(self, name: _Optional[str] = ..., parent_mft_reference: _Optional[int] = ..., file_namespace: _Optional[_Union[MFTEntryProto.NTFSNamespace, str]] = ..., parent_path: _Optional[str] = ...) -> None: ...
    MFT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    mft_reference: int
    is_file: bool
    file_names: _containers.RepeatedCompositeFieldContainer[MFTEntryProto.FileName]
    size_bytes: int
    mtime_usecs: int
    physical_offset: int
    def __init__(self, mft_reference: _Optional[int] = ..., is_file: bool = ..., file_names: _Optional[_Iterable[_Union[MFTEntryProto.FileName, _Mapping]]] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., physical_offset: _Optional[int] = ...) -> None: ...
