from configs.form import form_config_pb2 as _form_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HostOSType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KLinux: _ClassVar[HostOSType]
    KWindows: _ClassVar[HostOSType]
    KAix: _ClassVar[HostOSType]
KLinux: HostOSType
KWindows: HostOSType
KAix: HostOSType

class TranslationsConfig(_message.Message):
    __slots__ = ("locale_translations_map",)
    class LocaleSpecificTranslations(_message.Message):
        __slots__ = ("translation_key_mapping",)
        class TranslationKeyMappingEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TRANSLATION_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
        translation_key_mapping: _containers.ScalarMap[str, str]
        def __init__(self, translation_key_mapping: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class LocaleTranslationsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TranslationsConfig.LocaleSpecificTranslations
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TranslationsConfig.LocaleSpecificTranslations, _Mapping]] = ...) -> None: ...
    LOCALE_TRANSLATIONS_MAP_FIELD_NUMBER: _ClassVar[int]
    locale_translations_map: _containers.MessageMap[str, TranslationsConfig.LocaleSpecificTranslations]
    def __init__(self, locale_translations_map: _Optional[_Mapping[str, TranslationsConfig.LocaleSpecificTranslations]] = ...) -> None: ...

class UDAConnectorConfiguration(_message.Message):
    __slots__ = ("index_config", "os_specific_configs_vec", "ui_translations")
    class IndexConfig(_message.Message):
        __slots__ = ("id", "source_type", "label_key", "enabled", "version", "syntax")
        ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SYNTAX_FIELD_NUMBER: _ClassVar[int]
        id: int
        source_type: str
        label_key: str
        enabled: bool
        version: int
        syntax: int
        def __init__(self, id: _Optional[int] = ..., source_type: _Optional[str] = ..., label_key: _Optional[str] = ..., enabled: bool = ..., version: _Optional[int] = ..., syntax: _Optional[int] = ...) -> None: ...
    class DynamicForm(_message.Message):
        __slots__ = ("panels",)
        PANELS_FIELD_NUMBER: _ClassVar[int]
        panels: _containers.RepeatedCompositeFieldContainer[_form_config_pb2.FormPanel]
        def __init__(self, panels: _Optional[_Iterable[_Union[_form_config_pb2.FormPanel, _Mapping]]] = ...) -> None: ...
    class RegistrationConfig(_message.Message):
        __slots__ = ("primary_fields", "dynamic_form", "encrypted_fields")
        class PrimaryFields(_message.Message):
            __slots__ = ("script_dir", "mount_view", "source_registration_args", "app_authentication")
            class ScriptDir(_message.Message):
                __slots__ = ("default_value",)
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                def __init__(self, default_value: _Optional[str] = ...) -> None: ...
            class MountView(_message.Message):
                __slots__ = ("hidden", "default_value")
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                hidden: bool
                default_value: bool
                def __init__(self, hidden: bool = ..., default_value: bool = ...) -> None: ...
            class SourceRegistrationArgs(_message.Message):
                __slots__ = ("default_value", "readonly", "required", "hidden")
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                READONLY_FIELD_NUMBER: _ClassVar[int]
                REQUIRED_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                readonly: bool
                required: bool
                hidden: bool
                def __init__(self, default_value: _Optional[str] = ..., readonly: bool = ..., required: bool = ..., hidden: bool = ...) -> None: ...
            class AppAuthentication(_message.Message):
                __slots__ = ("hidden",)
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                hidden: bool
                def __init__(self, hidden: bool = ...) -> None: ...
            SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
            MOUNT_VIEW_FIELD_NUMBER: _ClassVar[int]
            SOURCE_REGISTRATION_ARGS_FIELD_NUMBER: _ClassVar[int]
            APP_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
            script_dir: UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.ScriptDir
            mount_view: UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.MountView
            source_registration_args: UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.SourceRegistrationArgs
            app_authentication: UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.AppAuthentication
            def __init__(self, script_dir: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.ScriptDir, _Mapping]] = ..., mount_view: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.MountView, _Mapping]] = ..., source_registration_args: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.SourceRegistrationArgs, _Mapping]] = ..., app_authentication: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig.PrimaryFields.AppAuthentication, _Mapping]] = ...) -> None: ...
        PRIMARY_FIELDS_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_FORM_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        primary_fields: UDAConnectorConfiguration.RegistrationConfig.PrimaryFields
        dynamic_form: UDAConnectorConfiguration.DynamicForm
        encrypted_fields: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, primary_fields: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig.PrimaryFields, _Mapping]] = ..., dynamic_form: _Optional[_Union[UDAConnectorConfiguration.DynamicForm, _Mapping]] = ..., encrypted_fields: _Optional[_Iterable[str]] = ...) -> None: ...
    class ProtectionConfig(_message.Message):
        __slots__ = ("primary_fields", "dynamic_form", "encrypted_fields")
        class PrimaryFields(_message.Message):
            __slots__ = ("full_backup_args", "incr_backup_args", "log_backup_args")
            class FullBackupArgs(_message.Message):
                __slots__ = ("default_value", "readonly", "hidden", "required")
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                READONLY_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                REQUIRED_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                readonly: bool
                hidden: bool
                required: bool
                def __init__(self, default_value: _Optional[str] = ..., readonly: bool = ..., hidden: bool = ..., required: bool = ...) -> None: ...
            class IncrBackupArgs(_message.Message):
                __slots__ = ("default_value", "readonly", "hidden", "required")
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                READONLY_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                REQUIRED_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                readonly: bool
                hidden: bool
                required: bool
                def __init__(self, default_value: _Optional[str] = ..., readonly: bool = ..., hidden: bool = ..., required: bool = ...) -> None: ...
            class LogBackupArgs(_message.Message):
                __slots__ = ("default_value", "readonly", "hidden", "required")
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                READONLY_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                REQUIRED_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                readonly: bool
                hidden: bool
                required: bool
                def __init__(self, default_value: _Optional[str] = ..., readonly: bool = ..., hidden: bool = ..., required: bool = ...) -> None: ...
            FULL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
            INCR_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
            LOG_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
            full_backup_args: UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.FullBackupArgs
            incr_backup_args: UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.IncrBackupArgs
            log_backup_args: UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.LogBackupArgs
            def __init__(self, full_backup_args: _Optional[_Union[UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.FullBackupArgs, _Mapping]] = ..., incr_backup_args: _Optional[_Union[UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.IncrBackupArgs, _Mapping]] = ..., log_backup_args: _Optional[_Union[UDAConnectorConfiguration.ProtectionConfig.PrimaryFields.LogBackupArgs, _Mapping]] = ...) -> None: ...
        PRIMARY_FIELDS_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_FORM_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        primary_fields: UDAConnectorConfiguration.ProtectionConfig.PrimaryFields
        dynamic_form: UDAConnectorConfiguration.DynamicForm
        encrypted_fields: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, primary_fields: _Optional[_Union[UDAConnectorConfiguration.ProtectionConfig.PrimaryFields, _Mapping]] = ..., dynamic_form: _Optional[_Union[UDAConnectorConfiguration.DynamicForm, _Mapping]] = ..., encrypted_fields: _Optional[_Iterable[str]] = ...) -> None: ...
    class RecoveryConfig(_message.Message):
        __slots__ = ("primary_fields", "dynamic_form", "encrypted_fields")
        class PrimaryFields(_message.Message):
            __slots__ = ("recovery_args",)
            class RecoveryArgs(_message.Message):
                __slots__ = ("default_value", "readonly", "required", "hidden")
                DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
                READONLY_FIELD_NUMBER: _ClassVar[int]
                REQUIRED_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_FIELD_NUMBER: _ClassVar[int]
                default_value: str
                readonly: bool
                required: bool
                hidden: bool
                def __init__(self, default_value: _Optional[str] = ..., readonly: bool = ..., required: bool = ..., hidden: bool = ...) -> None: ...
            RECOVERY_ARGS_FIELD_NUMBER: _ClassVar[int]
            recovery_args: UDAConnectorConfiguration.RecoveryConfig.PrimaryFields.RecoveryArgs
            def __init__(self, recovery_args: _Optional[_Union[UDAConnectorConfiguration.RecoveryConfig.PrimaryFields.RecoveryArgs, _Mapping]] = ...) -> None: ...
        PRIMARY_FIELDS_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_FORM_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        primary_fields: UDAConnectorConfiguration.RecoveryConfig.PrimaryFields
        dynamic_form: UDAConnectorConfiguration.DynamicForm
        encrypted_fields: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, primary_fields: _Optional[_Union[UDAConnectorConfiguration.RecoveryConfig.PrimaryFields, _Mapping]] = ..., dynamic_form: _Optional[_Union[UDAConnectorConfiguration.DynamicForm, _Mapping]] = ..., encrypted_fields: _Optional[_Iterable[str]] = ...) -> None: ...
    class HostOSSpecificConfiguration(_message.Message):
        __slots__ = ("os_type", "registration_config", "protection_config", "recovery_config", "index_config")
        class OSIndexConfig(_message.Message):
            __slots__ = ("ui_feature_flag",)
            UI_FEATURE_FLAG_FIELD_NUMBER: _ClassVar[int]
            ui_feature_flag: str
            def __init__(self, ui_feature_flag: _Optional[str] = ...) -> None: ...
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
        os_type: HostOSType
        registration_config: UDAConnectorConfiguration.RegistrationConfig
        protection_config: UDAConnectorConfiguration.ProtectionConfig
        recovery_config: UDAConnectorConfiguration.RecoveryConfig
        index_config: UDAConnectorConfiguration.HostOSSpecificConfiguration.OSIndexConfig
        def __init__(self, os_type: _Optional[_Union[HostOSType, str]] = ..., registration_config: _Optional[_Union[UDAConnectorConfiguration.RegistrationConfig, _Mapping]] = ..., protection_config: _Optional[_Union[UDAConnectorConfiguration.ProtectionConfig, _Mapping]] = ..., recovery_config: _Optional[_Union[UDAConnectorConfiguration.RecoveryConfig, _Mapping]] = ..., index_config: _Optional[_Union[UDAConnectorConfiguration.HostOSSpecificConfiguration.OSIndexConfig, _Mapping]] = ...) -> None: ...
    INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OS_SPECIFIC_CONFIGS_VEC_FIELD_NUMBER: _ClassVar[int]
    UI_TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    index_config: UDAConnectorConfiguration.IndexConfig
    os_specific_configs_vec: _containers.RepeatedCompositeFieldContainer[UDAConnectorConfiguration.HostOSSpecificConfiguration]
    ui_translations: TranslationsConfig
    def __init__(self, index_config: _Optional[_Union[UDAConnectorConfiguration.IndexConfig, _Mapping]] = ..., os_specific_configs_vec: _Optional[_Iterable[_Union[UDAConnectorConfiguration.HostOSSpecificConfiguration, _Mapping]]] = ..., ui_translations: _Optional[_Union[TranslationsConfig, _Mapping]] = ...) -> None: ...

class UDAConfigurations(_message.Message):
    __slots__ = ("uda_configs_map",)
    class UdaConfigsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UDAConnectorConfiguration
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UDAConnectorConfiguration, _Mapping]] = ...) -> None: ...
    UDA_CONFIGS_MAP_FIELD_NUMBER: _ClassVar[int]
    uda_configs_map: _containers.MessageMap[str, UDAConnectorConfiguration]
    def __init__(self, uda_configs_map: _Optional[_Mapping[str, UDAConnectorConfiguration]] = ...) -> None: ...

class UDAConnectorConfigJsonArgs(_message.Message):
    __slots__ = ("index_config", "os_configs_vec", "ui_translations", "privileged", "replace")
    class LocaleSpecificTranslations(_message.Message):
        __slots__ = ("locale_name", "locale_config")
        LOCALE_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCALE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        locale_name: str
        locale_config: str
        def __init__(self, locale_name: _Optional[str] = ..., locale_config: _Optional[str] = ...) -> None: ...
    class OSSpecificConfig(_message.Message):
        __slots__ = ("os_type", "registration_config", "protection_config", "recovery_config", "index_config")
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
        os_type: str
        registration_config: str
        protection_config: str
        recovery_config: str
        index_config: str
        def __init__(self, os_type: _Optional[str] = ..., registration_config: _Optional[str] = ..., protection_config: _Optional[str] = ..., recovery_config: _Optional[str] = ..., index_config: _Optional[str] = ...) -> None: ...
    INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OS_CONFIGS_VEC_FIELD_NUMBER: _ClassVar[int]
    UI_TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    index_config: str
    os_configs_vec: _containers.RepeatedCompositeFieldContainer[UDAConnectorConfigJsonArgs.OSSpecificConfig]
    ui_translations: _containers.RepeatedCompositeFieldContainer[UDAConnectorConfigJsonArgs.LocaleSpecificTranslations]
    privileged: bool
    replace: bool
    def __init__(self, index_config: _Optional[str] = ..., os_configs_vec: _Optional[_Iterable[_Union[UDAConnectorConfigJsonArgs.OSSpecificConfig, _Mapping]]] = ..., ui_translations: _Optional[_Iterable[_Union[UDAConnectorConfigJsonArgs.LocaleSpecificTranslations, _Mapping]]] = ..., privileged: bool = ..., replace: bool = ...) -> None: ...
