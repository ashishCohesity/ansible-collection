from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
TENANT_MIGRATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
tenant_migration_options: _descriptor.FieldDescriptor

class TenantMigrationFieldOptions(_message.Message):
    __slots__ = ("tenant_migration_mutable",)
    TENANT_MIGRATION_MUTABLE_FIELD_NUMBER: _ClassVar[int]
    tenant_migration_mutable: bool
    def __init__(self, tenant_migration_mutable: bool = ...) -> None: ...
