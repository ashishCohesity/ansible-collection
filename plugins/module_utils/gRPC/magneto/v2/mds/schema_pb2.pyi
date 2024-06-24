from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MagnetoNodeProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[MagnetoNodeProto.Type]
        kPolicy: _ClassVar[MagnetoNodeProto.Type]
        kEntity: _ClassVar[MagnetoNodeProto.Type]
        kEnvProtectionParams: _ClassVar[MagnetoNodeProto.Type]
        kEntityProtectionParams: _ClassVar[MagnetoNodeProto.Type]
        kProtectionSpec: _ClassVar[MagnetoNodeProto.Type]
        kRun: _ClassVar[MagnetoNodeProto.Type]
        kSnapshot: _ClassVar[MagnetoNodeProto.Type]
        kData: _ClassVar[MagnetoNodeProto.Type]
        kPrincipal: _ClassVar[MagnetoNodeProto.Type]
    kUnused: MagnetoNodeProto.Type
    kPolicy: MagnetoNodeProto.Type
    kEntity: MagnetoNodeProto.Type
    kEnvProtectionParams: MagnetoNodeProto.Type
    kEntityProtectionParams: MagnetoNodeProto.Type
    kProtectionSpec: MagnetoNodeProto.Type
    kRun: MagnetoNodeProto.Type
    kSnapshot: MagnetoNodeProto.Type
    kData: MagnetoNodeProto.Type
    kPrincipal: MagnetoNodeProto.Type
    def __init__(self) -> None: ...

class MagnetoEdgeProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[MagnetoEdgeProto.Type]
        kPolicyOf: _ClassVar[MagnetoEdgeProto.Type]
        kHasSnapshot: _ClassVar[MagnetoEdgeProto.Type]
        kHasProtectionSpec: _ClassVar[MagnetoEdgeProto.Type]
        kHasPolicy: _ClassVar[MagnetoEdgeProto.Type]
        kHasParams: _ClassVar[MagnetoEdgeProto.Type]
        kProtectionOf: _ClassVar[MagnetoEdgeProto.Type]
        kHasRun: _ClassVar[MagnetoEdgeProto.Type]
        kHasData: _ClassVar[MagnetoEdgeProto.Type]
        kEHHasChild: _ClassVar[MagnetoEdgeProto.Type]
        kHasPermission: _ClassVar[MagnetoEdgeProto.Type]
        kIsAssignedTo: _ClassVar[MagnetoEdgeProto.Type]
    kUnused: MagnetoEdgeProto.Type
    kPolicyOf: MagnetoEdgeProto.Type
    kHasSnapshot: MagnetoEdgeProto.Type
    kHasProtectionSpec: MagnetoEdgeProto.Type
    kHasPolicy: MagnetoEdgeProto.Type
    kHasParams: MagnetoEdgeProto.Type
    kProtectionOf: MagnetoEdgeProto.Type
    kHasRun: MagnetoEdgeProto.Type
    kHasData: MagnetoEdgeProto.Type
    kEHHasChild: MagnetoEdgeProto.Type
    kHasPermission: MagnetoEdgeProto.Type
    kIsAssignedTo: MagnetoEdgeProto.Type
    def __init__(self) -> None: ...

class NodeAttributeNamesProto(_message.Message):
    __slots__ = ("display_name", "primary_key_attr_name", "v1_uid", "checksum", "avoid_gc_until_timestamp_usecs")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
    V1_UID_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    AVOID_GC_UNTIL_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    primary_key_attr_name: str
    v1_uid: str
    checksum: str
    avoid_gc_until_timestamp_usecs: str
    def __init__(self, display_name: _Optional[str] = ..., primary_key_attr_name: _Optional[str] = ..., v1_uid: _Optional[str] = ..., checksum: _Optional[str] = ..., avoid_gc_until_timestamp_usecs: _Optional[str] = ...) -> None: ...

class AttachmentNamesProto(_message.Message):
    __slots__ = ("information",)
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    information: str
    def __init__(self, information: _Optional[str] = ...) -> None: ...

class LabelPrefixProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[LabelPrefixProto.Type]
        kEnvironment: _ClassVar[LabelPrefixProto.Type]
    kUnused: LabelPrefixProto.Type
    kEnvironment: LabelPrefixProto.Type
    def __init__(self) -> None: ...

class EdgeAttributeNamesProto(_message.Message):
    __slots__ = ("is_defunct",)
    IS_DEFUNCT_FIELD_NUMBER: _ClassVar[int]
    is_defunct: str
    def __init__(self, is_defunct: _Optional[str] = ...) -> None: ...
