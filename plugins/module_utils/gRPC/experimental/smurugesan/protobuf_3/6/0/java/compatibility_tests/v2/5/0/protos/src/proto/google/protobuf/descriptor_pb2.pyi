from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileDescriptorSet(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _containers.RepeatedCompositeFieldContainer[FileDescriptorProto]
    def __init__(self, file: _Optional[_Iterable[_Union[FileDescriptorProto, _Mapping]]] = ...) -> None: ...

class FileDescriptorProto(_message.Message):
    __slots__ = ("name", "package", "dependency", "public_dependency", "weak_dependency", "message_type", "enum_type", "service", "extension", "options", "source_code_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    WEAK_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    package: str
    dependency: _containers.RepeatedScalarFieldContainer[str]
    public_dependency: _containers.RepeatedScalarFieldContainer[int]
    weak_dependency: _containers.RepeatedScalarFieldContainer[int]
    message_type: _containers.RepeatedCompositeFieldContainer[DescriptorProto]
    enum_type: _containers.RepeatedCompositeFieldContainer[EnumDescriptorProto]
    service: _containers.RepeatedCompositeFieldContainer[ServiceDescriptorProto]
    extension: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    options: FileOptions
    source_code_info: SourceCodeInfo
    def __init__(self, name: _Optional[str] = ..., package: _Optional[str] = ..., dependency: _Optional[_Iterable[str]] = ..., public_dependency: _Optional[_Iterable[int]] = ..., weak_dependency: _Optional[_Iterable[int]] = ..., message_type: _Optional[_Iterable[_Union[DescriptorProto, _Mapping]]] = ..., enum_type: _Optional[_Iterable[_Union[EnumDescriptorProto, _Mapping]]] = ..., service: _Optional[_Iterable[_Union[ServiceDescriptorProto, _Mapping]]] = ..., extension: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[FileOptions, _Mapping]] = ..., source_code_info: _Optional[_Union[SourceCodeInfo, _Mapping]] = ...) -> None: ...

class DescriptorProto(_message.Message):
    __slots__ = ("name", "field", "extension", "nested_type", "enum_type", "extension_range", "options")
    class ExtensionRange(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    NESTED_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_RANGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    field: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    extension: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    nested_type: _containers.RepeatedCompositeFieldContainer[DescriptorProto]
    enum_type: _containers.RepeatedCompositeFieldContainer[EnumDescriptorProto]
    extension_range: _containers.RepeatedCompositeFieldContainer[DescriptorProto.ExtensionRange]
    options: MessageOptions
    def __init__(self, name: _Optional[str] = ..., field: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., extension: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., nested_type: _Optional[_Iterable[_Union[DescriptorProto, _Mapping]]] = ..., enum_type: _Optional[_Iterable[_Union[EnumDescriptorProto, _Mapping]]] = ..., extension_range: _Optional[_Iterable[_Union[DescriptorProto.ExtensionRange, _Mapping]]] = ..., options: _Optional[_Union[MessageOptions, _Mapping]] = ...) -> None: ...

class FieldDescriptorProto(_message.Message):
    __slots__ = ("name", "number", "label", "type", "type_name", "extendee", "default_value", "options")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_DOUBLE: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FLOAT: _ClassVar[FieldDescriptorProto.Type]
        TYPE_INT64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_UINT64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_INT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FIXED64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FIXED32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_BOOL: _ClassVar[FieldDescriptorProto.Type]
        TYPE_STRING: _ClassVar[FieldDescriptorProto.Type]
        TYPE_GROUP: _ClassVar[FieldDescriptorProto.Type]
        TYPE_MESSAGE: _ClassVar[FieldDescriptorProto.Type]
        TYPE_BYTES: _ClassVar[FieldDescriptorProto.Type]
        TYPE_UINT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_ENUM: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SFIXED32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SFIXED64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SINT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SINT64: _ClassVar[FieldDescriptorProto.Type]
    TYPE_DOUBLE: FieldDescriptorProto.Type
    TYPE_FLOAT: FieldDescriptorProto.Type
    TYPE_INT64: FieldDescriptorProto.Type
    TYPE_UINT64: FieldDescriptorProto.Type
    TYPE_INT32: FieldDescriptorProto.Type
    TYPE_FIXED64: FieldDescriptorProto.Type
    TYPE_FIXED32: FieldDescriptorProto.Type
    TYPE_BOOL: FieldDescriptorProto.Type
    TYPE_STRING: FieldDescriptorProto.Type
    TYPE_GROUP: FieldDescriptorProto.Type
    TYPE_MESSAGE: FieldDescriptorProto.Type
    TYPE_BYTES: FieldDescriptorProto.Type
    TYPE_UINT32: FieldDescriptorProto.Type
    TYPE_ENUM: FieldDescriptorProto.Type
    TYPE_SFIXED32: FieldDescriptorProto.Type
    TYPE_SFIXED64: FieldDescriptorProto.Type
    TYPE_SINT32: FieldDescriptorProto.Type
    TYPE_SINT64: FieldDescriptorProto.Type
    class Label(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LABEL_OPTIONAL: _ClassVar[FieldDescriptorProto.Label]
        LABEL_REQUIRED: _ClassVar[FieldDescriptorProto.Label]
        LABEL_REPEATED: _ClassVar[FieldDescriptorProto.Label]
    LABEL_OPTIONAL: FieldDescriptorProto.Label
    LABEL_REQUIRED: FieldDescriptorProto.Label
    LABEL_REPEATED: FieldDescriptorProto.Label
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENDEE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    label: FieldDescriptorProto.Label
    type: FieldDescriptorProto.Type
    type_name: str
    extendee: str
    default_value: str
    options: FieldOptions
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., label: _Optional[_Union[FieldDescriptorProto.Label, str]] = ..., type: _Optional[_Union[FieldDescriptorProto.Type, str]] = ..., type_name: _Optional[str] = ..., extendee: _Optional[str] = ..., default_value: _Optional[str] = ..., options: _Optional[_Union[FieldOptions, _Mapping]] = ...) -> None: ...

class EnumDescriptorProto(_message.Message):
    __slots__ = ("name", "value", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[EnumValueDescriptorProto]
    options: EnumOptions
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[EnumValueDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[EnumOptions, _Mapping]] = ...) -> None: ...

class EnumValueDescriptorProto(_message.Message):
    __slots__ = ("name", "number", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    options: EnumValueOptions
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., options: _Optional[_Union[EnumValueOptions, _Mapping]] = ...) -> None: ...

class ServiceDescriptorProto(_message.Message):
    __slots__ = ("name", "method", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    method: _containers.RepeatedCompositeFieldContainer[MethodDescriptorProto]
    options: ServiceOptions
    def __init__(self, name: _Optional[str] = ..., method: _Optional[_Iterable[_Union[MethodDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[ServiceOptions, _Mapping]] = ...) -> None: ...

class MethodDescriptorProto(_message.Message):
    __slots__ = ("name", "input_type", "output_type", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_type: str
    output_type: str
    options: MethodOptions
    def __init__(self, name: _Optional[str] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ..., options: _Optional[_Union[MethodOptions, _Mapping]] = ...) -> None: ...

class FileOptions(_message.Message):
    __slots__ = ("java_package", "java_outer_classname", "java_multiple_files", "java_generate_equals_and_hash", "optimize_for", "go_package", "cc_generic_services", "java_generic_services", "py_generic_services", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    class OptimizeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEED: _ClassVar[FileOptions.OptimizeMode]
        CODE_SIZE: _ClassVar[FileOptions.OptimizeMode]
        LITE_RUNTIME: _ClassVar[FileOptions.OptimizeMode]
    SPEED: FileOptions.OptimizeMode
    CODE_SIZE: FileOptions.OptimizeMode
    LITE_RUNTIME: FileOptions.OptimizeMode
    JAVA_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    JAVA_OUTER_CLASSNAME_FIELD_NUMBER: _ClassVar[int]
    JAVA_MULTIPLE_FILES_FIELD_NUMBER: _ClassVar[int]
    JAVA_GENERATE_EQUALS_AND_HASH_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_FOR_FIELD_NUMBER: _ClassVar[int]
    GO_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CC_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    JAVA_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    PY_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    java_package: str
    java_outer_classname: str
    java_multiple_files: bool
    java_generate_equals_and_hash: bool
    optimize_for: FileOptions.OptimizeMode
    go_package: str
    cc_generic_services: bool
    java_generic_services: bool
    py_generic_services: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, java_package: _Optional[str] = ..., java_outer_classname: _Optional[str] = ..., java_multiple_files: bool = ..., java_generate_equals_and_hash: bool = ..., optimize_for: _Optional[_Union[FileOptions.OptimizeMode, str]] = ..., go_package: _Optional[str] = ..., cc_generic_services: bool = ..., java_generic_services: bool = ..., py_generic_services: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class MessageOptions(_message.Message):
    __slots__ = ("message_set_wire_format", "no_standard_descriptor_accessor", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    MESSAGE_SET_WIRE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    NO_STANDARD_DESCRIPTOR_ACCESSOR_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    message_set_wire_format: bool
    no_standard_descriptor_accessor: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, message_set_wire_format: bool = ..., no_standard_descriptor_accessor: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class FieldOptions(_message.Message):
    __slots__ = ("ctype", "packed", "lazy", "deprecated", "experimental_map_key", "weak", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    class CType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRING: _ClassVar[FieldOptions.CType]
        CORD: _ClassVar[FieldOptions.CType]
        STRING_PIECE: _ClassVar[FieldOptions.CType]
    STRING: FieldOptions.CType
    CORD: FieldOptions.CType
    STRING_PIECE: FieldOptions.CType
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIELD_NUMBER: _ClassVar[int]
    LAZY_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_MAP_KEY_FIELD_NUMBER: _ClassVar[int]
    WEAK_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    ctype: FieldOptions.CType
    packed: bool
    lazy: bool
    deprecated: bool
    experimental_map_key: str
    weak: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, ctype: _Optional[_Union[FieldOptions.CType, str]] = ..., packed: bool = ..., lazy: bool = ..., deprecated: bool = ..., experimental_map_key: _Optional[str] = ..., weak: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class EnumOptions(_message.Message):
    __slots__ = ("allow_alias", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    ALLOW_ALIAS_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    allow_alias: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, allow_alias: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class EnumValueOptions(_message.Message):
    __slots__ = ("uninterpreted_option",)
    Extensions: _python_message._ExtensionDict
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class ServiceOptions(_message.Message):
    __slots__ = ("uninterpreted_option",)
    Extensions: _python_message._ExtensionDict
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class MethodOptions(_message.Message):
    __slots__ = ("uninterpreted_option",)
    Extensions: _python_message._ExtensionDict
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class UninterpretedOption(_message.Message):
    __slots__ = ("name", "identifier_value", "positive_int_value", "negative_int_value", "double_value", "string_value", "aggregate_value")
    class NamePart(_message.Message):
        __slots__ = ("name_part", "is_extension")
        NAME_PART_FIELD_NUMBER: _ClassVar[int]
        IS_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        name_part: str
        is_extension: bool
        def __init__(self, name_part: _Optional[str] = ..., is_extension: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_VALUE_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedCompositeFieldContainer[UninterpretedOption.NamePart]
    identifier_value: str
    positive_int_value: int
    negative_int_value: int
    double_value: float
    string_value: bytes
    aggregate_value: str
    def __init__(self, name: _Optional[_Iterable[_Union[UninterpretedOption.NamePart, _Mapping]]] = ..., identifier_value: _Optional[str] = ..., positive_int_value: _Optional[int] = ..., negative_int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[bytes] = ..., aggregate_value: _Optional[str] = ...) -> None: ...

class SourceCodeInfo(_message.Message):
    __slots__ = ("location",)
    class Location(_message.Message):
        __slots__ = ("path", "span", "leading_comments", "trailing_comments")
        PATH_FIELD_NUMBER: _ClassVar[int]
        SPAN_FIELD_NUMBER: _ClassVar[int]
        LEADING_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        TRAILING_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedScalarFieldContainer[int]
        span: _containers.RepeatedScalarFieldContainer[int]
        leading_comments: str
        trailing_comments: str
        def __init__(self, path: _Optional[_Iterable[int]] = ..., span: _Optional[_Iterable[int]] = ..., leading_comments: _Optional[str] = ..., trailing_comments: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _containers.RepeatedCompositeFieldContainer[SourceCodeInfo.Location]
    def __init__(self, location: _Optional[_Iterable[_Union[SourceCodeInfo.Location, _Mapping]]] = ...) -> None: ...
