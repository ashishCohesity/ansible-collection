from magneto.agents.linux.stub import rds_param_pb2 as _rds_param_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kRmanIncremental: _ClassVar[BackupType]
    kRmanArchiveLogSequenceRange: _ClassVar[BackupType]
kRmanIncremental: BackupType
kRmanArchiveLogSequenceRange: BackupType

class RmanCommonParameters(_message.Message):
    __slots__ = ("p_directory_name", "p_label", "p_owner", "p_tag", "p_compress", "p_include_archive_logs", "p_include_controlfile", "p_optimize", "p_parallel", "p_rman_to_dbms_output", "p_section_size_mb", "p_validation_type")
    class ValidationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPhysical: _ClassVar[RmanCommonParameters.ValidationType]
        kPhysicalPlusLogical: _ClassVar[RmanCommonParameters.ValidationType]
    kPhysical: RmanCommonParameters.ValidationType
    kPhysicalPlusLogical: RmanCommonParameters.ValidationType
    P_DIRECTORY_NAME_FIELD_NUMBER: _ClassVar[int]
    P_LABEL_FIELD_NUMBER: _ClassVar[int]
    P_OWNER_FIELD_NUMBER: _ClassVar[int]
    P_TAG_FIELD_NUMBER: _ClassVar[int]
    P_COMPRESS_FIELD_NUMBER: _ClassVar[int]
    P_INCLUDE_ARCHIVE_LOGS_FIELD_NUMBER: _ClassVar[int]
    P_INCLUDE_CONTROLFILE_FIELD_NUMBER: _ClassVar[int]
    P_OPTIMIZE_FIELD_NUMBER: _ClassVar[int]
    P_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    P_RMAN_TO_DBMS_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    P_SECTION_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    P_VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    p_directory_name: str
    p_label: str
    p_owner: str
    p_tag: str
    p_compress: bool
    p_include_archive_logs: bool
    p_include_controlfile: bool
    p_optimize: bool
    p_parallel: int
    p_rman_to_dbms_output: bool
    p_section_size_mb: int
    p_validation_type: RmanCommonParameters.ValidationType
    def __init__(self, p_directory_name: _Optional[str] = ..., p_label: _Optional[str] = ..., p_owner: _Optional[str] = ..., p_tag: _Optional[str] = ..., p_compress: bool = ..., p_include_archive_logs: bool = ..., p_include_controlfile: bool = ..., p_optimize: bool = ..., p_parallel: _Optional[int] = ..., p_rman_to_dbms_output: bool = ..., p_section_size_mb: _Optional[int] = ..., p_validation_type: _Optional[_Union[RmanCommonParameters.ValidationType, str]] = ...) -> None: ...

class OraclePrepareInstanceArg(_message.Message):
    __slots__ = ("backup_type", "rman_prepare_arg")
    ORACLE_PREPARE_ARG_FIELD_NUMBER: _ClassVar[int]
    oracle_prepare_arg: _descriptor.FieldDescriptor
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RMAN_PREPARE_ARG_FIELD_NUMBER: _ClassVar[int]
    backup_type: BackupType
    rman_prepare_arg: RmanPrepareInstanceArg
    def __init__(self, backup_type: _Optional[_Union[BackupType, str]] = ..., rman_prepare_arg: _Optional[_Union[RmanPrepareInstanceArg, _Mapping]] = ...) -> None: ...

class RmanPrepareInstanceArg(_message.Message):
    __slots__ = ("crosscheck_archivelog_common_params", "p_delete_expired", "directory", "largest_sequence_number")
    CROSSCHECK_ARCHIVELOG_COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    P_DELETE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    LARGEST_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    crosscheck_archivelog_common_params: RmanCommonParameters
    p_delete_expired: bool
    directory: str
    largest_sequence_number: int
    def __init__(self, crosscheck_archivelog_common_params: _Optional[_Union[RmanCommonParameters, _Mapping]] = ..., p_delete_expired: bool = ..., directory: _Optional[str] = ..., largest_sequence_number: _Optional[int] = ...) -> None: ...

class OracleBackupArg(_message.Message):
    __slots__ = ("backup_type", "rman_incremental_arg", "rman_archive_log_sequence_range_arg")
    ORACLE_BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    oracle_backup_arg: _descriptor.FieldDescriptor
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RMAN_INCREMENTAL_ARG_FIELD_NUMBER: _ClassVar[int]
    RMAN_ARCHIVE_LOG_SEQUENCE_RANGE_ARG_FIELD_NUMBER: _ClassVar[int]
    backup_type: BackupType
    rman_incremental_arg: RmanIncrementalBackupArg
    rman_archive_log_sequence_range_arg: RmanArchiveLogSequenceRangeBackupArg
    def __init__(self, backup_type: _Optional[_Union[BackupType, str]] = ..., rman_incremental_arg: _Optional[_Union[RmanIncrementalBackupArg, _Mapping]] = ..., rman_archive_log_sequence_range_arg: _Optional[_Union[RmanArchiveLogSequenceRangeBackupArg, _Mapping]] = ...) -> None: ...

class RmanIncrementalBackupArg(_message.Message):
    __slots__ = ("common_params", "p_level")
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    P_LEVEL_FIELD_NUMBER: _ClassVar[int]
    common_params: RmanCommonParameters
    p_level: int
    def __init__(self, common_params: _Optional[_Union[RmanCommonParameters, _Mapping]] = ..., p_level: _Optional[int] = ...) -> None: ...

class RmanArchiveLogSequenceRangeBackupArg(_message.Message):
    __slots__ = ("common_params", "p_from_sequence")
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    P_FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    common_params: RmanCommonParameters
    p_from_sequence: int
    def __init__(self, common_params: _Optional[_Union[RmanCommonParameters, _Mapping]] = ..., p_from_sequence: _Optional[int] = ...) -> None: ...
