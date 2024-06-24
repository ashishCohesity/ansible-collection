from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaxosErrorProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[PaxosErrorProto.Type]
        kTransportError: _ClassVar[PaxosErrorProto.Type]
        kUnresolvable: _ClassVar[PaxosErrorProto.Type]
        kTimeout: _ClassVar[PaxosErrorProto.Type]
        kRetry: _ClassVar[PaxosErrorProto.Type]
        kIncorrectNodeId: _ClassVar[PaxosErrorProto.Type]
        kProposerNotInView: _ClassVar[PaxosErrorProto.Type]
        kInstanceAlreadyChosen: _ClassVar[PaxosErrorProto.Type]
        kPreviousInstanceUnchosen: _ClassVar[PaxosErrorProto.Type]
        kLeasedToAnotherNode: _ClassVar[PaxosErrorProto.Type]
        kPreempted: _ClassVar[PaxosErrorProto.Type]
        kNoAcceptedValue: _ClassVar[PaxosErrorProto.Type]
        kAcceptedValueMismatch: _ClassVar[PaxosErrorProto.Type]
        kCannotGarbageCollect: _ClassVar[PaxosErrorProto.Type]
        kNoValueForInstance: _ClassVar[PaxosErrorProto.Type]
        kClusterIdMismatch: _ClassVar[PaxosErrorProto.Type]
        kEncryptionRequired: _ClassVar[PaxosErrorProto.Type]
    kNoError: PaxosErrorProto.Type
    kTransportError: PaxosErrorProto.Type
    kUnresolvable: PaxosErrorProto.Type
    kTimeout: PaxosErrorProto.Type
    kRetry: PaxosErrorProto.Type
    kIncorrectNodeId: PaxosErrorProto.Type
    kProposerNotInView: PaxosErrorProto.Type
    kInstanceAlreadyChosen: PaxosErrorProto.Type
    kPreviousInstanceUnchosen: PaxosErrorProto.Type
    kLeasedToAnotherNode: PaxosErrorProto.Type
    kPreempted: PaxosErrorProto.Type
    kNoAcceptedValue: PaxosErrorProto.Type
    kAcceptedValueMismatch: PaxosErrorProto.Type
    kCannotGarbageCollect: PaxosErrorProto.Type
    kNoValueForInstance: PaxosErrorProto.Type
    kClusterIdMismatch: PaxosErrorProto.Type
    kEncryptionRequired: PaxosErrorProto.Type
    def __init__(self) -> None: ...

class ViewDescriptor(_message.Message):
    __slots__ = ("node_ids", "target_view_size", "spare_node_id", "node_endpoints", "supports_grpc", "paxos_supports_grpc")
    class NodeEndpointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_SIZE_FIELD_NUMBER: _ClassVar[int]
    SPARE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_GRPC_FIELD_NUMBER: _ClassVar[int]
    PAXOS_SUPPORTS_GRPC_FIELD_NUMBER: _ClassVar[int]
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    target_view_size: int
    spare_node_id: int
    node_endpoints: _containers.ScalarMap[int, str]
    supports_grpc: bool
    paxos_supports_grpc: bool
    def __init__(self, node_ids: _Optional[_Iterable[int]] = ..., target_view_size: _Optional[int] = ..., spare_node_id: _Optional[int] = ..., node_endpoints: _Optional[_Mapping[int, str]] = ..., supports_grpc: bool = ..., paxos_supports_grpc: bool = ...) -> None: ...

class PaxosValueHeader(_message.Message):
    __slots__ = ("value_type", "client_value_type", "start_checkpoint_instance", "gc_until_instance")
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownType: _ClassVar[PaxosValueHeader.ValueType]
        kBecomeMaster: _ClassVar[PaxosValueHeader.ValueType]
        kLeaseRenewal: _ClassVar[PaxosValueHeader.ValueType]
        kView: _ClassVar[PaxosValueHeader.ValueType]
        kClientValue: _ClassVar[PaxosValueHeader.ValueType]
        kNumValueTypes: _ClassVar[PaxosValueHeader.ValueType]
    kUnknownType: PaxosValueHeader.ValueType
    kBecomeMaster: PaxosValueHeader.ValueType
    kLeaseRenewal: PaxosValueHeader.ValueType
    kView: PaxosValueHeader.ValueType
    kClientValue: PaxosValueHeader.ValueType
    kNumValueTypes: PaxosValueHeader.ValueType
    class ClientValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownClientValueType: _ClassVar[PaxosValueHeader.ClientValueType]
        kBulkDataRecord: _ClassVar[PaxosValueHeader.ClientValueType]
        kStartCheckpointRecord: _ClassVar[PaxosValueHeader.ClientValueType]
        kFinalizeCheckpointRecord: _ClassVar[PaxosValueHeader.ClientValueType]
        kGarbageCollectionRequest: _ClassVar[PaxosValueHeader.ClientValueType]
        kNumClientValueTypes: _ClassVar[PaxosValueHeader.ClientValueType]
    kUnknownClientValueType: PaxosValueHeader.ClientValueType
    kBulkDataRecord: PaxosValueHeader.ClientValueType
    kStartCheckpointRecord: PaxosValueHeader.ClientValueType
    kFinalizeCheckpointRecord: PaxosValueHeader.ClientValueType
    kGarbageCollectionRequest: PaxosValueHeader.ClientValueType
    kNumClientValueTypes: PaxosValueHeader.ClientValueType
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_CHECKPOINT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    GC_UNTIL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    value_type: PaxosValueHeader.ValueType
    client_value_type: PaxosValueHeader.ClientValueType
    start_checkpoint_instance: int
    gc_until_instance: int
    def __init__(self, value_type: _Optional[_Union[PaxosValueHeader.ValueType, str]] = ..., client_value_type: _Optional[_Union[PaxosValueHeader.ClientValueType, str]] = ..., start_checkpoint_instance: _Optional[int] = ..., gc_until_instance: _Optional[int] = ...) -> None: ...

class ProposalId(_message.Message):
    __slots__ = ("local_num", "node_id")
    LOCAL_NUM_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    local_num: int
    node_id: int
    def __init__(self, local_num: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class InstanceRange(_message.Message):
    __slots__ = ("min_chosen_instance", "max_chosen_instance", "unchosen_instance", "finalize_checkpoint", "start_checkpoint")
    MIN_CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UNCHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    START_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    min_chosen_instance: int
    max_chosen_instance: int
    unchosen_instance: int
    finalize_checkpoint: int
    start_checkpoint: int
    def __init__(self, min_chosen_instance: _Optional[int] = ..., max_chosen_instance: _Optional[int] = ..., unchosen_instance: _Optional[int] = ..., finalize_checkpoint: _Optional[int] = ..., start_checkpoint: _Optional[int] = ...) -> None: ...

class AcceptorState(_message.Message):
    __slots__ = ("promised_proposal", "instance_range")
    PROMISED_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    promised_proposal: ProposalId
    instance_range: InstanceRange
    def __init__(self, promised_proposal: _Optional[_Union[ProposalId, _Mapping]] = ..., instance_range: _Optional[_Union[InstanceRange, _Mapping]] = ...) -> None: ...

class PrepareArg(_message.Message):
    __slots__ = ("sender_node_id", "sender_cluster_id", "receiver_node_id", "proposal_id", "instance_num", "proposer_instance_range")
    SENDER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NUM_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INSTANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    sender_node_id: int
    sender_cluster_id: int
    receiver_node_id: int
    proposal_id: ProposalId
    instance_num: int
    proposer_instance_range: InstanceRange
    def __init__(self, sender_node_id: _Optional[int] = ..., sender_cluster_id: _Optional[int] = ..., receiver_node_id: _Optional[int] = ..., proposal_id: _Optional[_Union[ProposalId, _Mapping]] = ..., instance_num: _Optional[int] = ..., proposer_instance_range: _Optional[_Union[InstanceRange, _Mapping]] = ...) -> None: ...

class PrepareResult(_message.Message):
    __slots__ = ("acceptor_state", "accepted_value_proposal")
    ACCEPTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_VALUE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    acceptor_state: AcceptorState
    accepted_value_proposal: ProposalId
    def __init__(self, acceptor_state: _Optional[_Union[AcceptorState, _Mapping]] = ..., accepted_value_proposal: _Optional[_Union[ProposalId, _Mapping]] = ...) -> None: ...

class AcceptArg(_message.Message):
    __slots__ = ("sender_node_id", "sender_cluster_id", "receiver_node_id", "proposal_id", "proposer_instance_range", "instance_num")
    SENDER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INSTANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NUM_FIELD_NUMBER: _ClassVar[int]
    sender_node_id: int
    sender_cluster_id: int
    receiver_node_id: int
    proposal_id: ProposalId
    proposer_instance_range: InstanceRange
    instance_num: int
    def __init__(self, sender_node_id: _Optional[int] = ..., sender_cluster_id: _Optional[int] = ..., receiver_node_id: _Optional[int] = ..., proposal_id: _Optional[_Union[ProposalId, _Mapping]] = ..., proposer_instance_range: _Optional[_Union[InstanceRange, _Mapping]] = ..., instance_num: _Optional[int] = ...) -> None: ...

class AcceptResult(_message.Message):
    __slots__ = ("acceptor_state",)
    ACCEPTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    acceptor_state: AcceptorState
    def __init__(self, acceptor_state: _Optional[_Union[AcceptorState, _Mapping]] = ...) -> None: ...

class MarkChosenArg(_message.Message):
    __slots__ = ("sender_node_id", "sender_cluster_id", "receiver_node_id", "proposal_id", "instance_num", "proposer_instance_range", "value_sha1_checksum")
    SENDER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NUM_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INSTANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    VALUE_SHA1_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    sender_node_id: int
    sender_cluster_id: int
    receiver_node_id: int
    proposal_id: ProposalId
    instance_num: int
    proposer_instance_range: InstanceRange
    value_sha1_checksum: bytes
    def __init__(self, sender_node_id: _Optional[int] = ..., sender_cluster_id: _Optional[int] = ..., receiver_node_id: _Optional[int] = ..., proposal_id: _Optional[_Union[ProposalId, _Mapping]] = ..., instance_num: _Optional[int] = ..., proposer_instance_range: _Optional[_Union[InstanceRange, _Mapping]] = ..., value_sha1_checksum: _Optional[bytes] = ...) -> None: ...

class MarkChosenResult(_message.Message):
    __slots__ = ("acceptor_state",)
    ACCEPTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    acceptor_state: AcceptorState
    def __init__(self, acceptor_state: _Optional[_Union[AcceptorState, _Mapping]] = ...) -> None: ...

class PullChosenInstanceArg(_message.Message):
    __slots__ = ("sender_node_id", "sender_cluster_id", "receiver_node_id", "min_instance")
    SENDER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    sender_node_id: int
    sender_cluster_id: int
    receiver_node_id: int
    min_instance: int
    def __init__(self, sender_node_id: _Optional[int] = ..., sender_cluster_id: _Optional[int] = ..., receiver_node_id: _Optional[int] = ..., min_instance: _Optional[int] = ...) -> None: ...

class PullChosenInstanceResult(_message.Message):
    __slots__ = ("instances", "payload_sizes")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SIZES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedScalarFieldContainer[int]
    payload_sizes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, instances: _Optional[_Iterable[int]] = ..., payload_sizes: _Optional[_Iterable[int]] = ...) -> None: ...

class GarbageCollectArg(_message.Message):
    __slots__ = ("sender_node_id", "sender_cluster_id", "receiver_node_id", "gc_until_instance")
    SENDER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    GC_UNTIL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    sender_node_id: int
    sender_cluster_id: int
    receiver_node_id: int
    gc_until_instance: int
    def __init__(self, sender_node_id: _Optional[int] = ..., sender_cluster_id: _Optional[int] = ..., receiver_node_id: _Optional[int] = ..., gc_until_instance: _Optional[int] = ...) -> None: ...

class GarbageCollectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
