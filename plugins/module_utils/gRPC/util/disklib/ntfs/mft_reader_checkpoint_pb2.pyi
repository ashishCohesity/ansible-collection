from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MFTReaderCheckpoint(_message.Message):
    __slots__ = ("in_file", "last_visited_mft_reference", "db_type")
    class DBType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLevelDB: _ClassVar[MFTReaderCheckpoint.DBType]
        kRocksDB: _ClassVar[MFTReaderCheckpoint.DBType]
    kLevelDB: MFTReaderCheckpoint.DBType
    kRocksDB: MFTReaderCheckpoint.DBType
    IN_FILE_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_MFT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DB_TYPE_FIELD_NUMBER: _ClassVar[int]
    in_file: bool
    last_visited_mft_reference: int
    db_type: MFTReaderCheckpoint.DBType
    def __init__(self, in_file: bool = ..., last_visited_mft_reference: _Optional[int] = ..., db_type: _Optional[_Union[MFTReaderCheckpoint.DBType, str]] = ...) -> None: ...
