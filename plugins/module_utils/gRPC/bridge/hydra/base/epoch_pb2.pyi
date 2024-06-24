from keychain.base import keychain_pb2 as _keychain_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SlaveSelection(_message.Message):
    __slots__ = ("node_id", "disk_id", "session_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    disk_id: int
    session_id: int
    def __init__(self, node_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., session_id: _Optional[int] = ...) -> None: ...

class EpochProto(_message.Message):
    __slots__ = ("state", "epoch_id", "replica_vec", "min_expected_sequence_id", "encryption_state", "edek_info")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTemporary: _ClassVar[EpochProto.State]
        kActive: _ClassVar[EpochProto.State]
        kFinalized: _ClassVar[EpochProto.State]
    kTemporary: EpochProto.State
    kActive: EpochProto.State
    kFinalized: EpochProto.State
    class EncryptionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[EpochProto.EncryptionState]
        kEncrypted: _ClassVar[EpochProto.EncryptionState]
        kNotEncrypted: _ClassVar[EpochProto.EncryptionState]
    kUnknown: EpochProto.EncryptionState
    kEncrypted: EpochProto.EncryptionState
    kNotEncrypted: EpochProto.EncryptionState
    STATE_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    MIN_EXPECTED_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    state: EpochProto.State
    epoch_id: int
    replica_vec: _containers.RepeatedCompositeFieldContainer[SlaveSelection]
    min_expected_sequence_id: int
    encryption_state: EpochProto.EncryptionState
    edek_info: _keychain_pb2.EdekProto
    def __init__(self, state: _Optional[_Union[EpochProto.State, str]] = ..., epoch_id: _Optional[int] = ..., replica_vec: _Optional[_Iterable[_Union[SlaveSelection, _Mapping]]] = ..., min_expected_sequence_id: _Optional[int] = ..., encryption_state: _Optional[_Union[EpochProto.EncryptionState, str]] = ..., edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ...) -> None: ...

class CanonicalBlobMetadataProto(_message.Message):
    __slots__ = ("opclock_vec", "blob_id", "canonical_epoch_vec", "view_box_id", "entry_reservation")
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_EPOCH_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    blob_id: int
    canonical_epoch_vec: _containers.RepeatedCompositeFieldContainer[EpochProto]
    view_box_id: int
    entry_reservation: int
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., blob_id: _Optional[int] = ..., canonical_epoch_vec: _Optional[_Iterable[_Union[EpochProto, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., entry_reservation: _Optional[int] = ...) -> None: ...
