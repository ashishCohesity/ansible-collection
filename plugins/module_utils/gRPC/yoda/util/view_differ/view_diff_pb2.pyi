from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewDiff(_message.Message):
    __slots__ = ("inode_type", "change_type", "new_full_path", "size_bytes", "mtime_usecs")
    class InodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[ViewDiff.InodeType]
        kDirectory: _ClassVar[ViewDiff.InodeType]
        kSymLink: _ClassVar[ViewDiff.InodeType]
    kFile: ViewDiff.InodeType
    kDirectory: ViewDiff.InodeType
    kSymLink: ViewDiff.InodeType
    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[ViewDiff.ChangeType]
        kDeleted: _ClassVar[ViewDiff.ChangeType]
        kRenamed: _ClassVar[ViewDiff.ChangeType]
        kUpdated: _ClassVar[ViewDiff.ChangeType]
    kCreated: ViewDiff.ChangeType
    kDeleted: ViewDiff.ChangeType
    kRenamed: ViewDiff.ChangeType
    kUpdated: ViewDiff.ChangeType
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEW_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    inode_type: ViewDiff.InodeType
    change_type: ViewDiff.ChangeType
    new_full_path: str
    size_bytes: int
    mtime_usecs: int
    def __init__(self, inode_type: _Optional[_Union[ViewDiff.InodeType, str]] = ..., change_type: _Optional[_Union[ViewDiff.ChangeType, str]] = ..., new_full_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ...) -> None: ...
