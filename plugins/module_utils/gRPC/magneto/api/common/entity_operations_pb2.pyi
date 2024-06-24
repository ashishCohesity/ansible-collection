from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityOperationSpecProto(_message.Message):
    __slots__ = ("mark_source_for_unregistration_params",)
    class MarkSourceForUnregistrationParams(_message.Message):
        __slots__ = ("should_delete_snapshots",)
        SHOULD_DELETE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        should_delete_snapshots: bool
        def __init__(self, should_delete_snapshots: bool = ...) -> None: ...
    MARK_SOURCE_FOR_UNREGISTRATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    mark_source_for_unregistration_params: EntityOperationSpecProto.MarkSourceForUnregistrationParams
    def __init__(self, mark_source_for_unregistration_params: _Optional[_Union[EntityOperationSpecProto.MarkSourceForUnregistrationParams, _Mapping]] = ...) -> None: ...

class EntityOperationStatusProto(_message.Message):
    __slots__ = ("unregister",)
    class Unregistration(_message.Message):
        __slots__ = ("unregister_in_progress",)
        UNREGISTER_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        unregister_in_progress: bool
        def __init__(self, unregister_in_progress: bool = ...) -> None: ...
    UNREGISTER_FIELD_NUMBER: _ClassVar[int]
    unregister: EntityOperationStatusProto.Unregistration
    def __init__(self, unregister: _Optional[_Union[EntityOperationStatusProto.Unregistration, _Mapping]] = ...) -> None: ...

class EntityOperationInfoProto(_message.Message):
    __slots__ = ("entity_id", "spec", "status")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    spec: EntityOperationSpecProto
    status: EntityOperationStatusProto
    def __init__(self, entity_id: _Optional[int] = ..., spec: _Optional[_Union[EntityOperationSpecProto, _Mapping]] = ..., status: _Optional[_Union[EntityOperationStatusProto, _Mapping]] = ...) -> None: ...
