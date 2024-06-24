from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScsiPeerInfo(_message.Message):
    __slots__ = ("constituent_id", "incarnation_id")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    incarnation_id: int
    def __init__(self, constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ...) -> None: ...

class LogicalUnitMetadataProto(_message.Message):
    __slots__ = ("file_path", "persistent_reservation", "initiator_condition_map")
    class PersistentReservation(_message.Message):
        __slots__ = ("epoch", "persist_through_power_lost", "registered_key_map", "is_reserved", "reserved_initiator_port_id", "reserved_key", "reserved_type")
        class ReservationKey(_message.Message):
            __slots__ = ("key", "peer_info", "registration_time_usecs")
            KEY_FIELD_NUMBER: _ClassVar[int]
            PEER_INFO_FIELD_NUMBER: _ClassVar[int]
            REGISTRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            key: int
            peer_info: ScsiPeerInfo
            registration_time_usecs: int
            def __init__(self, key: _Optional[int] = ..., peer_info: _Optional[_Union[ScsiPeerInfo, _Mapping]] = ..., registration_time_usecs: _Optional[int] = ...) -> None: ...
        class RegisteredKeyMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: LogicalUnitMetadataProto.PersistentReservation.ReservationKey
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LogicalUnitMetadataProto.PersistentReservation.ReservationKey, _Mapping]] = ...) -> None: ...
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        PERSIST_THROUGH_POWER_LOST_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_KEY_MAP_FIELD_NUMBER: _ClassVar[int]
        IS_RESERVED_FIELD_NUMBER: _ClassVar[int]
        RESERVED_INITIATOR_PORT_ID_FIELD_NUMBER: _ClassVar[int]
        RESERVED_KEY_FIELD_NUMBER: _ClassVar[int]
        RESERVED_TYPE_FIELD_NUMBER: _ClassVar[int]
        epoch: int
        persist_through_power_lost: bool
        registered_key_map: _containers.MessageMap[int, LogicalUnitMetadataProto.PersistentReservation.ReservationKey]
        is_reserved: bool
        reserved_initiator_port_id: int
        reserved_key: int
        reserved_type: int
        def __init__(self, epoch: _Optional[int] = ..., persist_through_power_lost: bool = ..., registered_key_map: _Optional[_Mapping[int, LogicalUnitMetadataProto.PersistentReservation.ReservationKey]] = ..., is_reserved: bool = ..., reserved_initiator_port_id: _Optional[int] = ..., reserved_key: _Optional[int] = ..., reserved_type: _Optional[int] = ...) -> None: ...
    class UnitAttentionCondition(_message.Message):
        __slots__ = ("additional_sense_code", "clear_aca", "creation_time_usecs")
        ADDITIONAL_SENSE_CODE_FIELD_NUMBER: _ClassVar[int]
        CLEAR_ACA_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        additional_sense_code: int
        clear_aca: bool
        creation_time_usecs: int
        def __init__(self, additional_sense_code: _Optional[int] = ..., clear_aca: bool = ..., creation_time_usecs: _Optional[int] = ...) -> None: ...
    class InitiatorUnitAttentionState(_message.Message):
        __slots__ = ("peer_info", "condition_list")
        PEER_INFO_FIELD_NUMBER: _ClassVar[int]
        CONDITION_LIST_FIELD_NUMBER: _ClassVar[int]
        peer_info: ScsiPeerInfo
        condition_list: _containers.RepeatedCompositeFieldContainer[LogicalUnitMetadataProto.UnitAttentionCondition]
        def __init__(self, peer_info: _Optional[_Union[ScsiPeerInfo, _Mapping]] = ..., condition_list: _Optional[_Iterable[_Union[LogicalUnitMetadataProto.UnitAttentionCondition, _Mapping]]] = ...) -> None: ...
    class InitiatorConditionMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LogicalUnitMetadataProto.InitiatorUnitAttentionState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LogicalUnitMetadataProto.InitiatorUnitAttentionState, _Mapping]] = ...) -> None: ...
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_CONDITION_MAP_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    persistent_reservation: LogicalUnitMetadataProto.PersistentReservation
    initiator_condition_map: _containers.MessageMap[int, LogicalUnitMetadataProto.InitiatorUnitAttentionState]
    def __init__(self, file_path: _Optional[str] = ..., persistent_reservation: _Optional[_Union[LogicalUnitMetadataProto.PersistentReservation, _Mapping]] = ..., initiator_condition_map: _Optional[_Mapping[int, LogicalUnitMetadataProto.InitiatorUnitAttentionState]] = ...) -> None: ...
