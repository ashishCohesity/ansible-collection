from magneto.master.db_utils import db_restore_pb2 as _db_restore_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OracleDbRestoreNode(_message.Message):
    __slots__ = ("reset_logs_id", "first_scn", "last_scn", "first_scn_time_msecs", "last_scn_time_msecs", "incarnation_id", "first_sequence", "last_sequence", "is_dummy_node", "thread_id_to_seq_map", "is_base_node", "dummy_parent_id")
    class ThreadIdToSeqMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: OracleSequenceRangeInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[OracleSequenceRangeInfo, _Mapping]] = ...) -> None: ...
    ORACLE_DB_RESTORE_NODE_FIELD_NUMBER: _ClassVar[int]
    oracle_db_restore_node: _descriptor.FieldDescriptor
    RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_SCN_FIELD_NUMBER: _ClassVar[int]
    LAST_SCN_FIELD_NUMBER: _ClassVar[int]
    FIRST_SCN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_SCN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    IS_DUMMY_NODE_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_TO_SEQ_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    DUMMY_PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    reset_logs_id: int
    first_scn: int
    last_scn: int
    first_scn_time_msecs: int
    last_scn_time_msecs: int
    incarnation_id: int
    first_sequence: int
    last_sequence: int
    is_dummy_node: bool
    thread_id_to_seq_map: _containers.MessageMap[int, OracleSequenceRangeInfo]
    is_base_node: bool
    dummy_parent_id: int
    def __init__(self, reset_logs_id: _Optional[int] = ..., first_scn: _Optional[int] = ..., last_scn: _Optional[int] = ..., first_scn_time_msecs: _Optional[int] = ..., last_scn_time_msecs: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., first_sequence: _Optional[int] = ..., last_sequence: _Optional[int] = ..., is_dummy_node: bool = ..., thread_id_to_seq_map: _Optional[_Mapping[int, OracleSequenceRangeInfo]] = ..., is_base_node: bool = ..., dummy_parent_id: _Optional[int] = ...) -> None: ...

class OracleSequenceRangeInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("first_sequence", "last_sequence")
        FIRST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        first_sequence: int
        last_sequence: int
        def __init__(self, first_sequence: _Optional[int] = ..., last_sequence: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[OracleSequenceRangeInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[OracleSequenceRangeInfo.Row, _Mapping]]] = ...) -> None: ...
