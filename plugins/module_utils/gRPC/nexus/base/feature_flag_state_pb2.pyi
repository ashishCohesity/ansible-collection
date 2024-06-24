from nexus.base import ticket_approval_list_pb2 as _ticket_approval_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureFlagOverrideState(_message.Message):
    __slots__ = ("feature_name", "is_approved", "reason", "timestamp_secs")
    FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    feature_name: str
    is_approved: bool
    reason: str
    timestamp_secs: int
    def __init__(self, feature_name: _Optional[str] = ..., is_approved: bool = ..., reason: _Optional[str] = ..., timestamp_secs: _Optional[int] = ...) -> None: ...

class FeatureApprovalState(_message.Message):
    __slots__ = ("feature_flag_state_key", "ticket_approval_list", "ui_feature_override_list", "backend_feature_override_list", "cluster_software_version")
    FEATURE_FLAG_STATE_KEY_FIELD_NUMBER: _ClassVar[int]
    TICKET_APPROVAL_LIST_FIELD_NUMBER: _ClassVar[int]
    UI_FEATURE_OVERRIDE_LIST_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FEATURE_OVERRIDE_LIST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    feature_flag_state_key: str
    ticket_approval_list: _ticket_approval_list_pb2.TicketApprovalListProto
    ui_feature_override_list: _containers.RepeatedCompositeFieldContainer[FeatureFlagOverrideState]
    backend_feature_override_list: _containers.RepeatedCompositeFieldContainer[FeatureFlagOverrideState]
    cluster_software_version: str
    def __init__(self, feature_flag_state_key: _Optional[str] = ..., ticket_approval_list: _Optional[_Union[_ticket_approval_list_pb2.TicketApprovalListProto, _Mapping]] = ..., ui_feature_override_list: _Optional[_Iterable[_Union[FeatureFlagOverrideState, _Mapping]]] = ..., backend_feature_override_list: _Optional[_Iterable[_Union[FeatureFlagOverrideState, _Mapping]]] = ..., cluster_software_version: _Optional[str] = ...) -> None: ...
