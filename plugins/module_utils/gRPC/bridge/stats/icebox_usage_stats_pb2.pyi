from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IceboxUsageStatsProto(_message.Message):
    __slots__ = ("type", "vault_id", "job_vault_id", "usage_bytes", "unmorphed_bytes_archived", "morphed_bytes_archived", "unmorphed_bytes_restored", "morphed_bytes_restored", "morphed_bytes_gced", "unmorphed_bytes_gced", "unmorphed_bytes_uptiered", "morphed_bytes_uptiered", "morphed_bytes_downtiered", "vault_type", "cloud_domain_id")
    class IceboxUsageStatsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVault: _ClassVar[IceboxUsageStatsProto.IceboxUsageStatsType]
        kJobVault: _ClassVar[IceboxUsageStatsProto.IceboxUsageStatsType]
        kCloudDomain: _ClassVar[IceboxUsageStatsProto.IceboxUsageStatsType]
    kVault: IceboxUsageStatsProto.IceboxUsageStatsType
    kJobVault: IceboxUsageStatsProto.IceboxUsageStatsType
    kCloudDomain: IceboxUsageStatsProto.IceboxUsageStatsType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_BYTES_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_BYTES_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_BYTES_GCED_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_BYTES_GCED_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_BYTES_UPTIERED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_BYTES_UPTIERED_FIELD_NUMBER: _ClassVar[int]
    MORPHED_BYTES_DOWNTIERED_FIELD_NUMBER: _ClassVar[int]
    VAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    type: IceboxUsageStatsProto.IceboxUsageStatsType
    vault_id: int
    job_vault_id: str
    usage_bytes: int
    unmorphed_bytes_archived: int
    morphed_bytes_archived: int
    unmorphed_bytes_restored: int
    morphed_bytes_restored: int
    morphed_bytes_gced: int
    unmorphed_bytes_gced: int
    unmorphed_bytes_uptiered: int
    morphed_bytes_uptiered: int
    morphed_bytes_downtiered: int
    vault_type: str
    cloud_domain_id: int
    def __init__(self, type: _Optional[_Union[IceboxUsageStatsProto.IceboxUsageStatsType, str]] = ..., vault_id: _Optional[int] = ..., job_vault_id: _Optional[str] = ..., usage_bytes: _Optional[int] = ..., unmorphed_bytes_archived: _Optional[int] = ..., morphed_bytes_archived: _Optional[int] = ..., unmorphed_bytes_restored: _Optional[int] = ..., morphed_bytes_restored: _Optional[int] = ..., morphed_bytes_gced: _Optional[int] = ..., unmorphed_bytes_gced: _Optional[int] = ..., unmorphed_bytes_uptiered: _Optional[int] = ..., morphed_bytes_uptiered: _Optional[int] = ..., morphed_bytes_downtiered: _Optional[int] = ..., vault_type: _Optional[str] = ..., cloud_domain_id: _Optional[int] = ...) -> None: ...
