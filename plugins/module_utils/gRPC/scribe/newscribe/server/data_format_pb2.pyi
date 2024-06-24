from scribe.base import scribe_pb2 as _scribe_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayloadRange(_message.Message):
    __slots__ = ("offset", "size")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class UserMD(_message.Message):
    __slots__ = ("version", "sequencer", "op_clock_vec", "is_tombstone", "reason_vec")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
    REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    sequencer: _scribe_pb2.SequencerProto
    op_clock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    is_tombstone: bool
    reason_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, version: _Optional[int] = ..., sequencer: _Optional[_Union[_scribe_pb2.SequencerProto, _Mapping]] = ..., op_clock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., is_tombstone: bool = ..., reason_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PaxosInstance(_message.Message):
    __slots__ = ("sequencer", "local_id")
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    sequencer: int
    local_id: int
    def __init__(self, sequencer: _Optional[int] = ..., local_id: _Optional[int] = ...) -> None: ...

class AcceptedValue(_message.Message):
    __slots__ = ("instance", "previous_chosen_instance", "intent", "is_dummy", "user_md", "columns", "transaction_state")
    class ColumnDescriptor(_message.Message):
        __slots__ = ("name", "data")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: _scribe_pb2.RowColumnKey
        data: PayloadRange
        def __init__(self, name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., data: _Optional[_Union[PayloadRange, _Mapping]] = ...) -> None: ...
    class TransactionState(_message.Message):
        __slots__ = ("keys",)
        KEYS_FIELD_NUMBER: _ClassVar[int]
        keys: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
        def __init__(self, keys: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ...) -> None: ...
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    IS_DUMMY_FIELD_NUMBER: _ClassVar[int]
    USER_MD_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_STATE_FIELD_NUMBER: _ClassVar[int]
    instance: PaxosInstance
    previous_chosen_instance: PaxosInstance
    intent: bool
    is_dummy: bool
    user_md: UserMD
    columns: _containers.RepeatedCompositeFieldContainer[AcceptedValue.ColumnDescriptor]
    transaction_state: AcceptedValue.TransactionState
    def __init__(self, instance: _Optional[_Union[PaxosInstance, _Mapping]] = ..., previous_chosen_instance: _Optional[_Union[PaxosInstance, _Mapping]] = ..., intent: bool = ..., is_dummy: bool = ..., user_md: _Optional[_Union[UserMD, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[AcceptedValue.ColumnDescriptor, _Mapping]]] = ..., transaction_state: _Optional[_Union[AcceptedValue.TransactionState, _Mapping]] = ...) -> None: ...

class PaxosMD(_message.Message):
    __slots__ = ("chosen_instance", "caughtup_sequencer", "accepted_value", "accepted_value_payload_offset")
    CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_VALUE_PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    chosen_instance: PaxosInstance
    caughtup_sequencer: int
    accepted_value: AcceptedValue
    accepted_value_payload_offset: int
    def __init__(self, chosen_instance: _Optional[_Union[PaxosInstance, _Mapping]] = ..., caughtup_sequencer: _Optional[int] = ..., accepted_value: _Optional[_Union[AcceptedValue, _Mapping]] = ..., accepted_value_payload_offset: _Optional[int] = ...) -> None: ...

class InlineColumn(_message.Message):
    __slots__ = ("name", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: _scribe_pb2.RowColumnKey
    data: PayloadRange
    def __init__(self, name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., data: _Optional[_Union[PayloadRange, _Mapping]] = ...) -> None: ...

class SanityChecks(_message.Message):
    __slots__ = ("column_info",)
    class ColumnInfo(_message.Message):
        __slots__ = ("name", "size")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        name: _scribe_pb2.RowColumnKey
        size: int
        def __init__(self, name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., size: _Optional[int] = ...) -> None: ...
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    column_info: _containers.RepeatedCompositeFieldContainer[SanityChecks.ColumnInfo]
    def __init__(self, column_info: _Optional[_Iterable[_Union[SanityChecks.ColumnInfo, _Mapping]]] = ...) -> None: ...

class ScribeRowMD(_message.Message):
    __slots__ = ("paxos_data", "user_md", "inline_columns", "all_columns_inline", "row_sanity_checks")
    PAXOS_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_MD_FIELD_NUMBER: _ClassVar[int]
    INLINE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ALL_COLUMNS_INLINE_FIELD_NUMBER: _ClassVar[int]
    ROW_SANITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    paxos_data: PaxosMD
    user_md: UserMD
    inline_columns: _containers.RepeatedCompositeFieldContainer[InlineColumn]
    all_columns_inline: bool
    row_sanity_checks: SanityChecks
    def __init__(self, paxos_data: _Optional[_Union[PaxosMD, _Mapping]] = ..., user_md: _Optional[_Union[UserMD, _Mapping]] = ..., inline_columns: _Optional[_Iterable[_Union[InlineColumn, _Mapping]]] = ..., all_columns_inline: bool = ..., row_sanity_checks: _Optional[_Union[SanityChecks, _Mapping]] = ...) -> None: ...

class SstFileMetaData(_message.Message):
    __slots__ = ("level", "smallest_seqno", "largest_seqno", "size", "sender_file_name", "sha256", "md5")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SMALLEST_SEQNO_FIELD_NUMBER: _ClassVar[int]
    LARGEST_SEQNO_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    level: int
    smallest_seqno: int
    largest_seqno: int
    size: int
    sender_file_name: bytes
    sha256: bytes
    md5: bytes
    def __init__(self, level: _Optional[int] = ..., smallest_seqno: _Optional[int] = ..., largest_seqno: _Optional[int] = ..., size: _Optional[int] = ..., sender_file_name: _Optional[bytes] = ..., sha256: _Optional[bytes] = ..., md5: _Optional[bytes] = ...) -> None: ...
