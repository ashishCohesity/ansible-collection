from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MysqlMetadataProto(_message.Message):
    __slots__ = ("backup_info_vec",)
    class BackupInfo(_message.Message):
        __slots__ = ("type", "backup_image_name")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFull: _ClassVar[MysqlMetadataProto.BackupInfo.Type]
            kIncremental: _ClassVar[MysqlMetadataProto.BackupInfo.Type]
            kLog: _ClassVar[MysqlMetadataProto.BackupInfo.Type]
            kOther: _ClassVar[MysqlMetadataProto.BackupInfo.Type]
        kFull: MysqlMetadataProto.BackupInfo.Type
        kIncremental: MysqlMetadataProto.BackupInfo.Type
        kLog: MysqlMetadataProto.BackupInfo.Type
        kOther: MysqlMetadataProto.BackupInfo.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BACKUP_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        type: MysqlMetadataProto.BackupInfo.Type
        backup_image_name: str
        def __init__(self, type: _Optional[_Union[MysqlMetadataProto.BackupInfo.Type, str]] = ..., backup_image_name: _Optional[str] = ...) -> None: ...
    BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_info_vec: _containers.RepeatedCompositeFieldContainer[MysqlMetadataProto.BackupInfo]
    def __init__(self, backup_info_vec: _Optional[_Iterable[_Union[MysqlMetadataProto.BackupInfo, _Mapping]]] = ...) -> None: ...

class SybaseAseMetadataProto(_message.Message):
    __slots__ = ("backup_info_vec",)
    class BackupInfo(_message.Message):
        __slots__ = ("type", "backup_image_name", "backup_streams", "backup_instant_time")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFull: _ClassVar[SybaseAseMetadataProto.BackupInfo.Type]
            kIncremental: _ClassVar[SybaseAseMetadataProto.BackupInfo.Type]
            kLog: _ClassVar[SybaseAseMetadataProto.BackupInfo.Type]
            kOther: _ClassVar[SybaseAseMetadataProto.BackupInfo.Type]
        kFull: SybaseAseMetadataProto.BackupInfo.Type
        kIncremental: SybaseAseMetadataProto.BackupInfo.Type
        kLog: SybaseAseMetadataProto.BackupInfo.Type
        kOther: SybaseAseMetadataProto.BackupInfo.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BACKUP_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        BACKUP_STREAMS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_INSTANT_TIME_FIELD_NUMBER: _ClassVar[int]
        type: SybaseAseMetadataProto.BackupInfo.Type
        backup_image_name: str
        backup_streams: int
        backup_instant_time: str
        def __init__(self, type: _Optional[_Union[SybaseAseMetadataProto.BackupInfo.Type, str]] = ..., backup_image_name: _Optional[str] = ..., backup_streams: _Optional[int] = ..., backup_instant_time: _Optional[str] = ...) -> None: ...
    BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_info_vec: _containers.RepeatedCompositeFieldContainer[SybaseAseMetadataProto.BackupInfo]
    def __init__(self, backup_info_vec: _Optional[_Iterable[_Union[SybaseAseMetadataProto.BackupInfo, _Mapping]]] = ...) -> None: ...
