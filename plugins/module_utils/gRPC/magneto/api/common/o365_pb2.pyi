from magneto.api.common import filters_pb2 as _filters_pb2
from magneto.api.common import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OutlookEnvBackupParamsProto(_message.Message):
    __slots__ = ("filtering_policy", "should_backup_mailbox")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BACKUP_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: _filters_pb2.FilteringPolicyProto
    should_backup_mailbox: bool
    def __init__(self, filtering_policy: _Optional[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]] = ..., should_backup_mailbox: bool = ...) -> None: ...

class SharepPointSiteEnvBackupParamsProto(_message.Message):
    __slots__ = ("doc_lib_filtering_policy",)
    DOC_LIB_FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    doc_lib_filtering_policy: _filters_pb2.FilteringPolicyProto
    def __init__(self, doc_lib_filtering_policy: _Optional[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]] = ...) -> None: ...

class EnvBackupParamsProto(_message.Message):
    __slots__ = ("outlook_backup_params", "indexing_policy", "site_backup_params")
    OUTLOOK_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SITE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    outlook_backup_params: OutlookEnvBackupParamsProto
    indexing_policy: _base_pb2.IndexingPolicyProto
    site_backup_params: SharepPointSiteEnvBackupParamsProto
    def __init__(self, outlook_backup_params: _Optional[_Union[OutlookEnvBackupParamsProto, _Mapping]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ..., site_backup_params: _Optional[_Union[SharepPointSiteEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class CommonO365EnvBackupParamsProto(_message.Message):
    __slots__ = ("filtering_policy", "indexing_policy")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: _filters_pb2.FilteringPolicyProto
    indexing_policy: _base_pb2.IndexingPolicyProto
    def __init__(self, filtering_policy: _Optional[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ...) -> None: ...

class O365ExchangeEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_backup_params",)
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: CommonO365EnvBackupParamsProto
    def __init__(self, common_backup_params: _Optional[_Union[CommonO365EnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class O365OneDriveEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_backup_params", "phl_params")
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: CommonO365EnvBackupParamsProto
    phl_params: PreservationHoldLibraryProtectionParams
    def __init__(self, common_backup_params: _Optional[_Union[CommonO365EnvBackupParamsProto, _Mapping]] = ..., phl_params: _Optional[_Union[PreservationHoldLibraryProtectionParams, _Mapping]] = ...) -> None: ...

class O365SharepointEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_backup_params", "phl_params")
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: CommonO365EnvBackupParamsProto
    phl_params: PreservationHoldLibraryProtectionParams
    def __init__(self, common_backup_params: _Optional[_Union[CommonO365EnvBackupParamsProto, _Mapping]] = ..., phl_params: _Optional[_Union[PreservationHoldLibraryProtectionParams, _Mapping]] = ...) -> None: ...

class O365TeamsEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_backup_params",)
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: CommonO365EnvBackupParamsProto
    def __init__(self, common_backup_params: _Optional[_Union[CommonO365EnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class O365GroupsEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_backup_params",)
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: CommonO365EnvBackupParamsProto
    def __init__(self, common_backup_params: _Optional[_Union[CommonO365EnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class SharepointBackupSourceParams(_message.Message):
    __slots__ = ("autoprotect_entity",)
    AUTOPROTECT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    autoprotect_entity: bool
    def __init__(self, autoprotect_entity: bool = ...) -> None: ...

class PreservationHoldLibraryProtectionParams(_message.Message):
    __slots__ = ("should_protect_phl",)
    SHOULD_PROTECT_PHL_FIELD_NUMBER: _ClassVar[int]
    should_protect_phl: bool
    def __init__(self, should_protect_phl: bool = ...) -> None: ...
