from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeScanConsistency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kConsistent: _ClassVar[RangeScanConsistency]
    kInconsistentOk: _ClassVar[RangeScanConsistency]
    kSmallTableUrgentRangeScan: _ClassVar[RangeScanConsistency]
    kReserved: _ClassVar[RangeScanConsistency]
kConsistent: RangeScanConsistency
kInconsistentOk: RangeScanConsistency
kSmallTableUrgentRangeScan: RangeScanConsistency
kReserved: RangeScanConsistency

class RowColumnKey(_message.Message):
    __slots__ = ("int_key", "str_key")
    INT_KEY_FIELD_NUMBER: _ClassVar[int]
    STR_KEY_FIELD_NUMBER: _ClassVar[int]
    int_key: int
    str_key: bytes
    def __init__(self, int_key: _Optional[int] = ..., str_key: _Optional[bytes] = ...) -> None: ...

class SequencerProto(_message.Message):
    __slots__ = ("high", "low")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: int
    low: int
    def __init__(self, high: _Optional[int] = ..., low: _Optional[int] = ...) -> None: ...

class RowData(_message.Message):
    __slots__ = ("key", "column_data")
    class ColumnData(_message.Message):
        __slots__ = ("name", "value")
        class ColumnValue(_message.Message):
            __slots__ = ("payload_data_size", "payload_offset", "payload_adler32_checksum")
            PAYLOAD_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_ADLER32_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
            payload_data_size: int
            payload_offset: int
            payload_adler32_checksum: int
            def __init__(self, payload_data_size: _Optional[int] = ..., payload_offset: _Optional[int] = ..., payload_adler32_checksum: _Optional[int] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: RowColumnKey
        value: RowData.ColumnData.ColumnValue
        def __init__(self, name: _Optional[_Union[RowColumnKey, _Mapping]] = ..., value: _Optional[_Union[RowData.ColumnData.ColumnValue, _Mapping]] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DATA_FIELD_NUMBER: _ClassVar[int]
    key: RowColumnKey
    column_data: _containers.RepeatedCompositeFieldContainer[RowData.ColumnData]
    def __init__(self, key: _Optional[_Union[RowColumnKey, _Mapping]] = ..., column_data: _Optional[_Iterable[_Union[RowData.ColumnData, _Mapping]]] = ...) -> None: ...

class RowRange(_message.Message):
    __slots__ = ("key", "start_key", "end_key", "list_only", "reverse")
    KEY_FIELD_NUMBER: _ClassVar[int]
    START_KEY_FIELD_NUMBER: _ClassVar[int]
    END_KEY_FIELD_NUMBER: _ClassVar[int]
    LIST_ONLY_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    key: RowColumnKey
    start_key: RowColumnKey
    end_key: RowColumnKey
    list_only: bool
    reverse: bool
    def __init__(self, key: _Optional[_Union[RowColumnKey, _Mapping]] = ..., start_key: _Optional[_Union[RowColumnKey, _Mapping]] = ..., end_key: _Optional[_Union[RowColumnKey, _Mapping]] = ..., list_only: bool = ..., reverse: bool = ...) -> None: ...

class ReadRowResult(_message.Message):
    __slots__ = ("row_data", "sequencer", "version", "op_clock_vec", "is_deleted", "reason_vec")
    ROW_DATA_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    row_data: RowData
    sequencer: SequencerProto
    version: int
    op_clock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    is_deleted: bool
    reason_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, row_data: _Optional[_Union[RowData, _Mapping]] = ..., sequencer: _Optional[_Union[SequencerProto, _Mapping]] = ..., version: _Optional[int] = ..., op_clock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., is_deleted: bool = ..., reason_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ScribeQoSParams(_message.Message):
    __slots__ = ("principal_id", "weight", "min_requests_executing", "client_name")
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIN_REQUESTS_EXECUTING_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    principal_id: int
    weight: int
    min_requests_executing: int
    client_name: str
    def __init__(self, principal_id: _Optional[int] = ..., weight: _Optional[int] = ..., min_requests_executing: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...
