from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProtectionSpecAttributeNamesProto(_message.Message):
    __slots__ = ("is_external", "storage_domain_id", "is_paused", "job_type", "is_active", "pending_deletion", "snapshots_marked_for_deletion", "is_auto_protect", "registered_source_pk")
    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[ProtectionSpecAttributeNamesProto.JobType]
        kLocal: _ClassVar[ProtectionSpecAttributeNamesProto.JobType]
        kRemote: _ClassVar[ProtectionSpecAttributeNamesProto.JobType]
    kUnused: ProtectionSpecAttributeNamesProto.JobType
    kLocal: ProtectionSpecAttributeNamesProto.JobType
    kRemote: ProtectionSpecAttributeNamesProto.JobType
    IS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PENDING_DELETION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_PROTECT_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PK_FIELD_NUMBER: _ClassVar[int]
    is_external: str
    storage_domain_id: str
    is_paused: str
    job_type: str
    is_active: str
    pending_deletion: str
    snapshots_marked_for_deletion: str
    is_auto_protect: str
    registered_source_pk: str
    def __init__(self, is_external: _Optional[str] = ..., storage_domain_id: _Optional[str] = ..., is_paused: _Optional[str] = ..., job_type: _Optional[str] = ..., is_active: _Optional[str] = ..., pending_deletion: _Optional[str] = ..., snapshots_marked_for_deletion: _Optional[str] = ..., is_auto_protect: _Optional[str] = ..., registered_source_pk: _Optional[str] = ...) -> None: ...

class EntityParamsAttributeNamesProto(_message.Message):
    __slots__ = ("is_paused",)
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    is_paused: str
    def __init__(self, is_paused: _Optional[str] = ...) -> None: ...

class ProtectionSpecAttachmentNamesProto(_message.Message):
    __slots__ = ("common_backup_params", "backup_job_desc")
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_DESC_FIELD_NUMBER: _ClassVar[int]
    common_backup_params: str
    backup_job_desc: str
    def __init__(self, common_backup_params: _Optional[str] = ..., backup_job_desc: _Optional[str] = ...) -> None: ...

class HasProtectionEdgeAttributeNamesProto(_message.Message):
    __slots__ = ("entity_protection_params_uid", "env_protection_params_uid", "protection_environment", "is_auto_protected")
    ENTITY_PROTECTION_PARAMS_UID_FIELD_NUMBER: _ClassVar[int]
    ENV_PROTECTION_PARAMS_UID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    entity_protection_params_uid: str
    env_protection_params_uid: str
    protection_environment: str
    is_auto_protected: str
    def __init__(self, entity_protection_params_uid: _Optional[str] = ..., env_protection_params_uid: _Optional[str] = ..., protection_environment: _Optional[str] = ..., is_auto_protected: _Optional[str] = ...) -> None: ...

class EnvProtectionParamsAttachmentNamesProto(_message.Message):
    __slots__ = ("env_specific_backup_params",)
    ENV_SPECIFIC_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    env_specific_backup_params: str
    def __init__(self, env_specific_backup_params: _Optional[str] = ...) -> None: ...

class EntityProtectionParamsAttachmentNamesProto(_message.Message):
    __slots__ = ("object_specific_backup_params",)
    OBJECT_SPECIFIC_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    object_specific_backup_params: str
    def __init__(self, object_specific_backup_params: _Optional[str] = ...) -> None: ...
