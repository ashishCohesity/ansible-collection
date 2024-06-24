from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmbAdConfFilesProto(_message.Message):
    __slots__ = ("krb5_conf", "smb_conf", "keytab_file", "secrets_tdb", "smb_conf_data", "krb5_conf_capaths")
    class SmbConf(_message.Message):
        __slots__ = ("sections",)
        class Section(_message.Message):
            __slots__ = ("name", "params")
            class ParamsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            PARAMS_FIELD_NUMBER: _ClassVar[int]
            name: str
            params: _containers.ScalarMap[str, str]
            def __init__(self, name: _Optional[str] = ..., params: _Optional[_Mapping[str, str]] = ...) -> None: ...
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        sections: _containers.RepeatedCompositeFieldContainer[SmbAdConfFilesProto.SmbConf.Section]
        def __init__(self, sections: _Optional[_Iterable[_Union[SmbAdConfFilesProto.SmbConf.Section, _Mapping]]] = ...) -> None: ...
    KRB5_CONF_FIELD_NUMBER: _ClassVar[int]
    SMB_CONF_FIELD_NUMBER: _ClassVar[int]
    KEYTAB_FILE_FIELD_NUMBER: _ClassVar[int]
    SECRETS_TDB_FIELD_NUMBER: _ClassVar[int]
    SMB_CONF_DATA_FIELD_NUMBER: _ClassVar[int]
    KRB5_CONF_CAPATHS_FIELD_NUMBER: _ClassVar[int]
    krb5_conf: bytes
    smb_conf: bytes
    keytab_file: bytes
    secrets_tdb: bytes
    smb_conf_data: SmbAdConfFilesProto.SmbConf
    krb5_conf_capaths: bytes
    def __init__(self, krb5_conf: _Optional[bytes] = ..., smb_conf: _Optional[bytes] = ..., keytab_file: _Optional[bytes] = ..., secrets_tdb: _Optional[bytes] = ..., smb_conf_data: _Optional[_Union[SmbAdConfFilesProto.SmbConf, _Mapping]] = ..., krb5_conf_capaths: _Optional[bytes] = ...) -> None: ...

class TenantSmbAdConfFilesProto(_message.Message):
    __slots__ = ("tenant_2_ad_config_map", "changed_tenant_id")
    class Tenant2AdConfigMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SmbAdConfFilesProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SmbAdConfFilesProto, _Mapping]] = ...) -> None: ...
    TENANT_2_AD_CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
    CHANGED_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_2_ad_config_map: _containers.MessageMap[str, SmbAdConfFilesProto]
    changed_tenant_id: str
    def __init__(self, tenant_2_ad_config_map: _Optional[_Mapping[str, SmbAdConfFilesProto]] = ..., changed_tenant_id: _Optional[str] = ...) -> None: ...
