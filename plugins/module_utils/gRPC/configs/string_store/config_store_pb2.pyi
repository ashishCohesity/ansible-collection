from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigItem(_message.Message):
    __slots__ = ("key", "bool_value", "int32_value", "int64_value", "double_value", "string_value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    bool_value: bool
    int32_value: int
    int64_value: int
    double_value: float
    string_value: str
    def __init__(self, key: _Optional[str] = ..., bool_value: bool = ..., int32_value: _Optional[int] = ..., int64_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ...) -> None: ...

class TenantConfigProto(_message.Message):
    __slots__ = ("tenant_id", "config_item_list")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    config_item_list: _containers.RepeatedCompositeFieldContainer[ConfigItem]
    def __init__(self, tenant_id: _Optional[str] = ..., config_item_list: _Optional[_Iterable[_Union[ConfigItem, _Mapping]]] = ...) -> None: ...

class TenantScopeConfigProto(_message.Message):
    __slots__ = ("version", "sub_scope", "tenant_config_list")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUB_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_CONFIG_LIST_FIELD_NUMBER: _ClassVar[int]
    version: int
    sub_scope: str
    tenant_config_list: _containers.RepeatedCompositeFieldContainer[TenantConfigProto]
    def __init__(self, version: _Optional[int] = ..., sub_scope: _Optional[str] = ..., tenant_config_list: _Optional[_Iterable[_Union[TenantConfigProto, _Mapping]]] = ...) -> None: ...

class ClusterScopeConfigProto(_message.Message):
    __slots__ = ("version", "sub_scope", "config_item_list")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUB_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    version: int
    sub_scope: str
    config_item_list: _containers.RepeatedCompositeFieldContainer[ConfigItem]
    def __init__(self, version: _Optional[int] = ..., sub_scope: _Optional[str] = ..., config_item_list: _Optional[_Iterable[_Union[ConfigItem, _Mapping]]] = ...) -> None: ...
