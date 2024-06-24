from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PbmCapabilityMetadataUniqueId(_message.Message):
    __slots__ = ("namespace_name", "id")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    id: str
    def __init__(self, namespace_name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class PbmCapabilityNamespaceInfo(_message.Message):
    __slots__ = ("namespace_name", "version")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    version: str
    def __init__(self, namespace_name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class PbmCapabilitySchemaVendorInfo(_message.Message):
    __slots__ = ("vendor_id",)
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    def __init__(self, vendor_id: _Optional[str] = ...) -> None: ...

class PbmCapabilityPropertyMetadata(_message.Message):
    __slots__ = ("id", "mandatory")
    ID_FIELD_NUMBER: _ClassVar[int]
    MANDATORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    mandatory: bool
    def __init__(self, id: _Optional[str] = ..., mandatory: bool = ...) -> None: ...

class PbmCapabilityMetadata(_message.Message):
    __slots__ = ("id", "property_metadata_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    id: PbmCapabilityMetadataUniqueId
    property_metadata_vec: _containers.RepeatedCompositeFieldContainer[PbmCapabilityPropertyMetadata]
    def __init__(self, id: _Optional[_Union[PbmCapabilityMetadataUniqueId, _Mapping]] = ..., property_metadata_vec: _Optional[_Iterable[_Union[PbmCapabilityPropertyMetadata, _Mapping]]] = ...) -> None: ...

class PbmCapabilityMetadataPerCategory(_message.Message):
    __slots__ = ("sub_category", "capability_metadata_vec")
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    sub_category: str
    capability_metadata_vec: _containers.RepeatedCompositeFieldContainer[PbmCapabilityMetadata]
    def __init__(self, sub_category: _Optional[str] = ..., capability_metadata_vec: _Optional[_Iterable[_Union[PbmCapabilityMetadata, _Mapping]]] = ...) -> None: ...

class PbmCapabilitySchema(_message.Message):
    __slots__ = ("capability_metadata_per_category_vec", "namespace_info", "vendor_info")
    CAPABILITY_METADATA_PER_CATEGORY_VEC_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    VENDOR_INFO_FIELD_NUMBER: _ClassVar[int]
    capability_metadata_per_category_vec: _containers.RepeatedCompositeFieldContainer[PbmCapabilityMetadataPerCategory]
    namespace_info: PbmCapabilityNamespaceInfo
    vendor_info: PbmCapabilitySchemaVendorInfo
    def __init__(self, capability_metadata_per_category_vec: _Optional[_Iterable[_Union[PbmCapabilityMetadataPerCategory, _Mapping]]] = ..., namespace_info: _Optional[_Union[PbmCapabilityNamespaceInfo, _Mapping]] = ..., vendor_info: _Optional[_Union[PbmCapabilitySchemaVendorInfo, _Mapping]] = ...) -> None: ...
