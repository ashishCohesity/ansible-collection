from atom.base import event_pb2 as _event_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyLogFilesToDiskUpdateArg(_message.Message):
    __slots__ = ("last_applied_seq_num", "total_bytes_read", "io_size_stats_map")
    class IoSizeStatsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LAST_APPLIED_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    IO_SIZE_STATS_MAP_FIELD_NUMBER: _ClassVar[int]
    last_applied_seq_num: _event_pb2.Sequencer
    total_bytes_read: int
    io_size_stats_map: _containers.ScalarMap[int, int]
    def __init__(self, last_applied_seq_num: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., total_bytes_read: _Optional[int] = ..., io_size_stats_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class CDPActionUpdateArg(_message.Message):
    __slots__ = ("type", "apply_log_files_to_disk_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApplyLogFilesToDisk: _ClassVar[CDPActionUpdateArg.Type]
        kCancel: _ClassVar[CDPActionUpdateArg.Type]
    kApplyLogFilesToDisk: CDPActionUpdateArg.Type
    kCancel: CDPActionUpdateArg.Type
    CDP_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    cdp_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLY_LOG_FILES_TO_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: CDPActionUpdateArg.Type
    apply_log_files_to_disk_update_arg: ApplyLogFilesToDiskUpdateArg
    def __init__(self, type: _Optional[_Union[CDPActionUpdateArg.Type, str]] = ..., apply_log_files_to_disk_update_arg: _Optional[_Union[ApplyLogFilesToDiskUpdateArg, _Mapping]] = ...) -> None: ...
