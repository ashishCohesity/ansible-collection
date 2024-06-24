from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseosPatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnKnown: _ClassVar[BaseosPatchStatus]
    kNotStarted: _ClassVar[BaseosPatchStatus]
    kInProgress: _ClassVar[BaseosPatchStatus]
    kFailed: _ClassVar[BaseosPatchStatus]
    kSucceeded: _ClassVar[BaseosPatchStatus]
kUnKnown: BaseosPatchStatus
kNotStarted: BaseosPatchStatus
kInProgress: BaseosPatchStatus
kFailed: BaseosPatchStatus
kSucceeded: BaseosPatchStatus

class PatchManagementEndpoints(_message.Message):
    __slots__ = ("available_patches", "applied_patches", "patches_history", "operation_status", "baseos_patch_download", "baseos_patch_apply", "baseos_patch_log", "baseos_patch_list", "baseos_patch_remove")
    AVAILABLE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PATCHES_FIELD_NUMBER: _ClassVar[int]
    PATCHES_HISTORY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BASEOS_PATCH_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    BASEOS_PATCH_APPLY_FIELD_NUMBER: _ClassVar[int]
    BASEOS_PATCH_LOG_FIELD_NUMBER: _ClassVar[int]
    BASEOS_PATCH_LIST_FIELD_NUMBER: _ClassVar[int]
    BASEOS_PATCH_REMOVE_FIELD_NUMBER: _ClassVar[int]
    available_patches: str
    applied_patches: str
    patches_history: str
    operation_status: str
    baseos_patch_download: str
    baseos_patch_apply: str
    baseos_patch_log: str
    baseos_patch_list: str
    baseos_patch_remove: str
    def __init__(self, available_patches: _Optional[str] = ..., applied_patches: _Optional[str] = ..., patches_history: _Optional[str] = ..., operation_status: _Optional[str] = ..., baseos_patch_download: _Optional[str] = ..., baseos_patch_apply: _Optional[str] = ..., baseos_patch_log: _Optional[str] = ..., baseos_patch_list: _Optional[str] = ..., baseos_patch_remove: _Optional[str] = ...) -> None: ...

class BaseosPatchRemoveArg(_message.Message):
    __slots__ = ("patch_name", "forceRemove")
    PATCH_NAME_FIELD_NUMBER: _ClassVar[int]
    FORCEREMOVE_FIELD_NUMBER: _ClassVar[int]
    patch_name: str
    forceRemove: bool
    def __init__(self, patch_name: _Optional[str] = ..., forceRemove: bool = ...) -> None: ...

class BaseosPatchDownloadArg(_message.Message):
    __slots__ = ("patch_url",)
    PATCH_URL_FIELD_NUMBER: _ClassVar[int]
    patch_url: str
    def __init__(self, patch_url: _Optional[str] = ...) -> None: ...

class BaseosPatchApplyArg(_message.Message):
    __slots__ = ("patch_name",)
    PATCH_NAME_FIELD_NUMBER: _ClassVar[int]
    patch_name: str
    def __init__(self, patch_name: _Optional[str] = ...) -> None: ...

class BaseosPatchLogArg(_message.Message):
    __slots__ = ("patch_name",)
    PATCH_NAME_FIELD_NUMBER: _ClassVar[int]
    patch_name: str
    def __init__(self, patch_name: _Optional[str] = ...) -> None: ...

class BaseosPatchLogResult(_message.Message):
    __slots__ = ("log", "status")
    LOG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    log: str
    status: BaseosPatchStatus
    def __init__(self, log: _Optional[str] = ..., status: _Optional[_Union[BaseosPatchStatus, str]] = ...) -> None: ...

class BaseosPatchListItem(_message.Message):
    __slots__ = ("name", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: BaseosPatchStatus
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[BaseosPatchStatus, str]] = ...) -> None: ...

class BaseosPatchListResult(_message.Message):
    __slots__ = ("baseos_patch_list",)
    BASEOS_PATCH_LIST_FIELD_NUMBER: _ClassVar[int]
    baseos_patch_list: _containers.RepeatedCompositeFieldContainer[BaseosPatchListItem]
    def __init__(self, baseos_patch_list: _Optional[_Iterable[_Union[BaseosPatchListItem, _Mapping]]] = ...) -> None: ...

class GetAvailablePatchesArg(_message.Message):
    __slots__ = ("service", "include_details")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    service: str
    include_details: bool
    def __init__(self, service: _Optional[str] = ..., include_details: bool = ...) -> None: ...

class GetAvailablePatchesResult(_message.Message):
    __slots__ = ("available_patches",)
    AVAILABLE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    available_patches: _containers.RepeatedCompositeFieldContainer[AvailablePatch]
    def __init__(self, available_patches: _Optional[_Iterable[_Union[AvailablePatch, _Mapping]]] = ...) -> None: ...

class AvailablePatch(_message.Message):
    __slots__ = ("service", "component", "version", "fixed_issues", "count", "dependencies")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FIXED_ISSUES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    service: str
    component: str
    version: str
    fixed_issues: _containers.RepeatedCompositeFieldContainer[FixedIssue]
    count: int
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service: _Optional[str] = ..., component: _Optional[str] = ..., version: _Optional[str] = ..., fixed_issues: _Optional[_Iterable[_Union[FixedIssue, _Mapping]]] = ..., count: _Optional[int] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

class FixedIssue(_message.Message):
    __slots__ = ("id", "release_note")
    ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTE_FIELD_NUMBER: _ClassVar[int]
    id: int
    release_note: str
    def __init__(self, id: _Optional[int] = ..., release_note: _Optional[str] = ...) -> None: ...

class ApplyPatchesArg(_message.Message):
    __slots__ = ("service", "user", "domain", "all")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    service: str
    user: str
    domain: str
    all: bool
    def __init__(self, service: _Optional[str] = ..., user: _Optional[str] = ..., domain: _Optional[str] = ..., all: bool = ...) -> None: ...

class ApplyPatchesResult(_message.Message):
    __slots__ = ("service_patch_levels",)
    SERVICE_PATCH_LEVELS_FIELD_NUMBER: _ClassVar[int]
    service_patch_levels: _containers.RepeatedCompositeFieldContainer[ServicePatchLevel]
    def __init__(self, service_patch_levels: _Optional[_Iterable[_Union[ServicePatchLevel, _Mapping]]] = ...) -> None: ...

class ServicePatchLevel(_message.Message):
    __slots__ = ("service", "patch_level", "patch_version", "start_level", "start_version")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    START_LEVEL_FIELD_NUMBER: _ClassVar[int]
    START_VERSION_FIELD_NUMBER: _ClassVar[int]
    service: str
    patch_level: int
    patch_version: str
    start_level: int
    start_version: str
    def __init__(self, service: _Optional[str] = ..., patch_level: _Optional[int] = ..., patch_version: _Optional[str] = ..., start_level: _Optional[int] = ..., start_version: _Optional[str] = ...) -> None: ...

class GetAppliedPatchesArg(_message.Message):
    __slots__ = ("service", "include_details")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    service: str
    include_details: bool
    def __init__(self, service: _Optional[str] = ..., include_details: bool = ...) -> None: ...

class GetAppliedPatchesResult(_message.Message):
    __slots__ = ("applied_patches",)
    APPLIED_PATCHES_FIELD_NUMBER: _ClassVar[int]
    applied_patches: _containers.RepeatedCompositeFieldContainer[AppliedPatch]
    def __init__(self, applied_patches: _Optional[_Iterable[_Union[AppliedPatch, _Mapping]]] = ...) -> None: ...

class AppliedPatch(_message.Message):
    __slots__ = ("service", "component", "version", "versionReplaced", "patch_level", "applied_time_msecs", "fixed_issues", "count", "dependencies")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSIONREPLACED_FIELD_NUMBER: _ClassVar[int]
    PATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    APPLIED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    FIXED_ISSUES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    service: str
    component: str
    version: str
    versionReplaced: str
    patch_level: int
    applied_time_msecs: int
    fixed_issues: _containers.RepeatedCompositeFieldContainer[FixedIssue]
    count: int
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service: _Optional[str] = ..., component: _Optional[str] = ..., version: _Optional[str] = ..., versionReplaced: _Optional[str] = ..., patch_level: _Optional[int] = ..., applied_time_msecs: _Optional[int] = ..., fixed_issues: _Optional[_Iterable[_Union[FixedIssue, _Mapping]]] = ..., count: _Optional[int] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

class RevertPatchesArg(_message.Message):
    __slots__ = ("service", "patch_level", "user", "domain")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    service: str
    patch_level: int
    user: str
    domain: str
    def __init__(self, service: _Optional[str] = ..., patch_level: _Optional[int] = ..., user: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class RevertPatchesResult(_message.Message):
    __slots__ = ("service_patch_levels",)
    SERVICE_PATCH_LEVELS_FIELD_NUMBER: _ClassVar[int]
    service_patch_levels: _containers.RepeatedCompositeFieldContainer[ServicePatchLevel]
    def __init__(self, service_patch_levels: _Optional[_Iterable[_Union[ServicePatchLevel, _Mapping]]] = ...) -> None: ...

class ImportPatchesArg(_message.Message):
    __slots__ = ("file_name", "user", "domain", "sender_ip")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SENDER_IP_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    user: str
    domain: str
    sender_ip: str
    def __init__(self, file_name: _Optional[str] = ..., user: _Optional[str] = ..., domain: _Optional[str] = ..., sender_ip: _Optional[str] = ...) -> None: ...

class ImportPatchesResult(_message.Message):
    __slots__ = ("imported_patches",)
    IMPORTED_PATCHES_FIELD_NUMBER: _ClassVar[int]
    imported_patches: _containers.RepeatedCompositeFieldContainer[ImportedPatchDetail]
    def __init__(self, imported_patches: _Optional[_Iterable[_Union[ImportedPatchDetail, _Mapping]]] = ...) -> None: ...

class ImportedPatchDetail(_message.Message):
    __slots__ = ("service", "component", "version", "import_version", "status")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IMPORT_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    service: str
    component: str
    version: str
    import_version: str
    status: str
    def __init__(self, service: _Optional[str] = ..., component: _Optional[str] = ..., version: _Optional[str] = ..., import_version: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class GetPatchesHistoryArg(_message.Message):
    __slots__ = ("service", "user", "domain")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    service: str
    user: str
    domain: str
    def __init__(self, service: _Optional[str] = ..., user: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class GetPatchesHistoryResult(_message.Message):
    __slots__ = ("patch_operations",)
    PATCH_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    patch_operations: _containers.RepeatedCompositeFieldContainer[PatchOperation]
    def __init__(self, patch_operations: _Optional[_Iterable[_Union[PatchOperation, _Mapping]]] = ...) -> None: ...

class PatchOperation(_message.Message):
    __slots__ = ("service", "component", "version", "versionReplaced", "operation", "operation_time_msecs", "user", "domain")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSIONREPLACED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    service: str
    component: str
    version: str
    versionReplaced: str
    operation: str
    operation_time_msecs: int
    user: str
    domain: str
    def __init__(self, service: _Optional[str] = ..., component: _Optional[str] = ..., version: _Optional[str] = ..., versionReplaced: _Optional[str] = ..., operation: _Optional[str] = ..., operation_time_msecs: _Optional[int] = ..., user: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class GetPatchOperationStatusArg(_message.Message):
    __slots__ = ("include_details",)
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    include_details: bool
    def __init__(self, include_details: bool = ...) -> None: ...

class GetPatchOperationStatusResult(_message.Message):
    __slots__ = ("in_progress", "operation", "services_progress", "operation_message", "percentage", "time_remaining_seconds", "time_taken_seconds")
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERVICES_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    in_progress: bool
    operation: str
    services_progress: _containers.RepeatedCompositeFieldContainer[ServiceUnitProgress]
    operation_message: str
    percentage: int
    time_remaining_seconds: int
    time_taken_seconds: int
    def __init__(self, in_progress: bool = ..., operation: _Optional[str] = ..., services_progress: _Optional[_Iterable[_Union[ServiceUnitProgress, _Mapping]]] = ..., operation_message: _Optional[str] = ..., percentage: _Optional[int] = ..., time_remaining_seconds: _Optional[int] = ..., time_taken_seconds: _Optional[int] = ...) -> None: ...

class ServiceUnitProgress(_message.Message):
    __slots__ = ("service", "service_message", "percentage", "time_remaining_seconds", "time_taken_seconds", "in_progress", "nodes_progress")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NODES_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    service: str
    service_message: str
    percentage: int
    time_remaining_seconds: int
    time_taken_seconds: int
    in_progress: bool
    nodes_progress: _containers.RepeatedCompositeFieldContainer[NodeUnitProgress]
    def __init__(self, service: _Optional[str] = ..., service_message: _Optional[str] = ..., percentage: _Optional[int] = ..., time_remaining_seconds: _Optional[int] = ..., time_taken_seconds: _Optional[int] = ..., in_progress: bool = ..., nodes_progress: _Optional[_Iterable[_Union[NodeUnitProgress, _Mapping]]] = ...) -> None: ...

class NodeUnitProgress(_message.Message):
    __slots__ = ("in_progress", "node_ip", "patch_level_transition", "percentage", "time_taken_seconds", "node_message")
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    PATCH_LEVEL_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NODE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    in_progress: bool
    node_ip: str
    patch_level_transition: str
    percentage: int
    time_taken_seconds: int
    node_message: str
    def __init__(self, in_progress: bool = ..., node_ip: _Optional[str] = ..., patch_level_transition: _Optional[str] = ..., percentage: _Optional[int] = ..., time_taken_seconds: _Optional[int] = ..., node_message: _Optional[str] = ...) -> None: ...

class PatchServerEndpoints(_message.Message):
    __slots__ = ("patches_metadata", "patches")
    PATCHES_METADATA_FIELD_NUMBER: _ClassVar[int]
    PATCHES_FIELD_NUMBER: _ClassVar[int]
    patches_metadata: str
    patches: str
    def __init__(self, patches_metadata: _Optional[str] = ..., patches: _Optional[str] = ...) -> None: ...
