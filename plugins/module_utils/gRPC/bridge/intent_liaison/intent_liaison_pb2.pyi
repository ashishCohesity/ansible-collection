from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FixEntityHandleArg(_message.Message):
    __slots__ = ("eh_to_fix", "expected_intent_id_high", "expected_intent_id_low", "request_context")
    EH_TO_FIX_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_INTENT_ID_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_INTENT_ID_LOW_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    eh_to_fix: _entity_handle_pb2.EntityHandleProto
    expected_intent_id_high: int
    expected_intent_id_low: int
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, eh_to_fix: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., expected_intent_id_high: _Optional[int] = ..., expected_intent_id_low: _Optional[int] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class FixEntityHandleResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
