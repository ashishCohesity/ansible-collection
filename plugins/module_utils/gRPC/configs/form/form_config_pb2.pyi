from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormField(_message.Message):
    __slots__ = ("id", "label_key", "key", "type", "string_config", "boolean_config", "number_config", "radio_group_config", "password_config")
    class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KString: _ClassVar[FormField.FieldType]
        KBoolean: _ClassVar[FormField.FieldType]
        KNumber: _ClassVar[FormField.FieldType]
        KRadioGroup: _ClassVar[FormField.FieldType]
        KPassword: _ClassVar[FormField.FieldType]
    KString: FormField.FieldType
    KBoolean: FormField.FieldType
    KNumber: FormField.FieldType
    KRadioGroup: FormField.FieldType
    KPassword: FormField.FieldType
    class StringConfig(_message.Message):
        __slots__ = ("required", "default_value", "description_key", "placeholder_key")
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        required: bool
        default_value: str
        description_key: str
        placeholder_key: str
        def __init__(self, required: bool = ..., default_value: _Optional[str] = ..., description_key: _Optional[str] = ..., placeholder_key: _Optional[str] = ...) -> None: ...
    class PasswordConfig(_message.Message):
        __slots__ = ("required", "description_key", "placeholder_key")
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        required: bool
        description_key: str
        placeholder_key: str
        def __init__(self, required: bool = ..., description_key: _Optional[str] = ..., placeholder_key: _Optional[str] = ...) -> None: ...
    class BooleanConfig(_message.Message):
        __slots__ = ("default_value", "description_key")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        default_value: bool
        description_key: str
        def __init__(self, default_value: bool = ..., description_key: _Optional[str] = ...) -> None: ...
    class NumberConfig(_message.Message):
        __slots__ = ("required", "default_value", "minimum_value", "maximum_value", "description_key", "placeholder_key")
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
        required: bool
        default_value: str
        minimum_value: str
        maximum_value: str
        description_key: str
        placeholder_key: str
        def __init__(self, required: bool = ..., default_value: _Optional[str] = ..., minimum_value: _Optional[str] = ..., maximum_value: _Optional[str] = ..., description_key: _Optional[str] = ..., placeholder_key: _Optional[str] = ...) -> None: ...
    class RadioGroupConfig(_message.Message):
        __slots__ = ("required", "radio_buttons", "default_value")
        class RadioButton(_message.Message):
            __slots__ = ("id", "label_key", "value", "panel")
            ID_FIELD_NUMBER: _ClassVar[int]
            LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            PANEL_FIELD_NUMBER: _ClassVar[int]
            id: str
            label_key: str
            value: str
            panel: FormPanel
            def __init__(self, id: _Optional[str] = ..., label_key: _Optional[str] = ..., value: _Optional[str] = ..., panel: _Optional[_Union[FormPanel, _Mapping]] = ...) -> None: ...
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        RADIO_BUTTONS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        required: bool
        radio_buttons: _containers.RepeatedCompositeFieldContainer[FormField.RadioGroupConfig.RadioButton]
        default_value: str
        def __init__(self, required: bool = ..., radio_buttons: _Optional[_Iterable[_Union[FormField.RadioGroupConfig.RadioButton, _Mapping]]] = ..., default_value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NUMBER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RADIO_GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    label_key: str
    key: str
    type: FormField.FieldType
    string_config: FormField.StringConfig
    boolean_config: FormField.BooleanConfig
    number_config: FormField.NumberConfig
    radio_group_config: FormField.RadioGroupConfig
    password_config: FormField.PasswordConfig
    def __init__(self, id: _Optional[str] = ..., label_key: _Optional[str] = ..., key: _Optional[str] = ..., type: _Optional[_Union[FormField.FieldType, str]] = ..., string_config: _Optional[_Union[FormField.StringConfig, _Mapping]] = ..., boolean_config: _Optional[_Union[FormField.BooleanConfig, _Mapping]] = ..., number_config: _Optional[_Union[FormField.NumberConfig, _Mapping]] = ..., radio_group_config: _Optional[_Union[FormField.RadioGroupConfig, _Mapping]] = ..., password_config: _Optional[_Union[FormField.PasswordConfig, _Mapping]] = ...) -> None: ...

class FormPanel(_message.Message):
    __slots__ = ("id", "optional", "title_key", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    TITLE_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    optional: bool
    title_key: str
    fields: _containers.RepeatedCompositeFieldContainer[FormField]
    def __init__(self, id: _Optional[str] = ..., optional: bool = ..., title_key: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[FormField, _Mapping]]] = ...) -> None: ...
