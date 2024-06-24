from bridge.base import error_pb2 as _error_pb2
from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScanCookie(_message.Message):
    __slots__ = ("current_offset", "max_logical_offset")
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MAX_LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    current_offset: int
    max_logical_offset: int
    def __init__(self, current_offset: _Optional[int] = ..., max_logical_offset: _Optional[int] = ...) -> None: ...

class ScanArg(_message.Message):
    __slots__ = ("blob_id", "cookie", "view_id", "request_context", "is_canonical_blob", "entry_reservation")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_CANONICAL_BLOB_FIELD_NUMBER: _ClassVar[int]
    ENTRY_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    cookie: ScanCookie
    view_id: int
    request_context: _request_context_pb2.RequestContextProto
    is_canonical_blob: bool
    entry_reservation: int
    def __init__(self, blob_id: _Optional[int] = ..., cookie: _Optional[_Union[ScanCookie, _Mapping]] = ..., view_id: _Optional[int] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., is_canonical_blob: bool = ..., entry_reservation: _Optional[int] = ...) -> None: ...

class ScanResult(_message.Message):
    __slots__ = ("cookie", "view_snap_tree_value_vec", "snap_tree_value_version_vec", "blob_owner_session_id")
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_VALUE_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_OWNER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    cookie: ScanCookie
    view_snap_tree_value_vec: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.ViewSnapTreeValueProto]
    snap_tree_value_version_vec: _containers.RepeatedCompositeFieldContainer[_snap_tree_pb2.SnapTreeValueVersionProto]
    blob_owner_session_id: int
    def __init__(self, cookie: _Optional[_Union[ScanCookie, _Mapping]] = ..., view_snap_tree_value_vec: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]]] = ..., snap_tree_value_version_vec: _Optional[_Iterable[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]]] = ..., blob_owner_session_id: _Optional[int] = ...) -> None: ...

class LookupArg(_message.Message):
    __slots__ = ("eh", "is_forwarded", "request_context", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "eh_ticket_sequencer_high", "eh_ticket_sequencer_low")
    EH_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    is_forwarded: bool
    request_context: _request_context_pb2.RequestContextProto
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    eh_ticket_sequencer_high: int
    eh_ticket_sequencer_low: int
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_forwarded: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., eh_ticket_sequencer_high: _Optional[int] = ..., eh_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class LookupResult(_message.Message):
    __slots__ = ("view_snap_tree_value", "snap_tree_value_version", "value_ttl_usecs")
    VIEW_SNAP_TREE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_TTL_USECS_FIELD_NUMBER: _ClassVar[int]
    view_snap_tree_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
    snap_tree_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    value_ttl_usecs: int
    def __init__(self, view_snap_tree_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., snap_tree_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., value_ttl_usecs: _Optional[int] = ...) -> None: ...

class BatchLookupArg(_message.Message):
    __slots__ = ("lookup_entity_vec", "is_forwarded", "blob_id", "request_context", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "entry_reservation")
    class LookupEntityProto(_message.Message):
        __slots__ = ("eh", "eh_ticket_sequencer_high", "eh_ticket_sequencer_low", "offset")
        EH_FIELD_NUMBER: _ClassVar[int]
        EH_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
        EH_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        eh_ticket_sequencer_high: int
        eh_ticket_sequencer_low: int
        offset: int
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., eh_ticket_sequencer_high: _Optional[int] = ..., eh_ticket_sequencer_low: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
    LOOKUP_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    ENTRY_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    lookup_entity_vec: _containers.RepeatedCompositeFieldContainer[BatchLookupArg.LookupEntityProto]
    is_forwarded: bool
    blob_id: int
    request_context: _request_context_pb2.RequestContextProto
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    entry_reservation: int
    def __init__(self, lookup_entity_vec: _Optional[_Iterable[_Union[BatchLookupArg.LookupEntityProto, _Mapping]]] = ..., is_forwarded: bool = ..., blob_id: _Optional[int] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., entry_reservation: _Optional[int] = ...) -> None: ...

class BatchLookupResult(_message.Message):
    __slots__ = ("lookup_entity_result_vec",)
    class LookupEntityResultProto(_message.Message):
        __slots__ = ("error", "view_snap_tree_value", "snap_tree_value_version", "value_ttl_usecs")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_VALUE_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        VALUE_TTL_USECS_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        view_snap_tree_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
        snap_tree_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        value_ttl_usecs: int
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_snap_tree_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., snap_tree_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., value_ttl_usecs: _Optional[int] = ...) -> None: ...
    LOOKUP_ENTITY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    lookup_entity_result_vec: _containers.RepeatedCompositeFieldContainer[BatchLookupResult.LookupEntityResultProto]
    def __init__(self, lookup_entity_result_vec: _Optional[_Iterable[_Union[BatchLookupResult.LookupEntityResultProto, _Mapping]]] = ...) -> None: ...

class UpdateArg(_message.Message):
    __slots__ = ("eh", "view_snap_tree_value", "snap_tree_value_version", "is_forwarded", "request_context", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "eh_ticket_sequencer_high", "eh_ticket_sequencer_low", "view_clone_epoch_id", "clear_blur_record", "flush_blur_record")
    EH_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    VIEW_CLONE_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    CLEAR_BLUR_RECORD_FIELD_NUMBER: _ClassVar[int]
    FLUSH_BLUR_RECORD_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    view_snap_tree_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
    snap_tree_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    is_forwarded: bool
    request_context: _request_context_pb2.RequestContextProto
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    eh_ticket_sequencer_high: int
    eh_ticket_sequencer_low: int
    view_clone_epoch_id: int
    clear_blur_record: bool
    flush_blur_record: bool
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., view_snap_tree_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., snap_tree_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., is_forwarded: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., eh_ticket_sequencer_high: _Optional[int] = ..., eh_ticket_sequencer_low: _Optional[int] = ..., view_clone_epoch_id: _Optional[int] = ..., clear_blur_record: bool = ..., flush_blur_record: bool = ...) -> None: ...

class UpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateEntityProto(_message.Message):
    __slots__ = ("eh", "snap_tree_value_version", "blob_offset", "eh_ticket_sequencer_high", "eh_ticket_sequencer_low", "entry_size")
    EH_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EH_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    ENTRY_SIZE_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    snap_tree_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    blob_offset: int
    eh_ticket_sequencer_high: int
    eh_ticket_sequencer_low: int
    entry_size: int
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., snap_tree_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., blob_offset: _Optional[int] = ..., eh_ticket_sequencer_high: _Optional[int] = ..., eh_ticket_sequencer_low: _Optional[int] = ..., entry_size: _Optional[int] = ...) -> None: ...

class MultiUpdateArg(_message.Message):
    __slots__ = ("update_entity_vec", "is_forwarded", "blob_id", "request_context", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "view_clone_epoch_id")
    UPDATE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    VIEW_CLONE_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    update_entity_vec: _containers.RepeatedCompositeFieldContainer[UpdateEntityProto]
    is_forwarded: bool
    blob_id: int
    request_context: _request_context_pb2.RequestContextProto
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    view_clone_epoch_id: int
    def __init__(self, update_entity_vec: _Optional[_Iterable[_Union[UpdateEntityProto, _Mapping]]] = ..., is_forwarded: bool = ..., blob_id: _Optional[int] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., view_clone_epoch_id: _Optional[int] = ...) -> None: ...

class MultiUpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
