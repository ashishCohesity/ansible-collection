from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackagesProto(_message.Message):
    __slots__ = ("cohesity_software_packages_vec", "packages_key")
    COHESITY_SOFTWARE_PACKAGES_VEC_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_KEY_FIELD_NUMBER: _ClassVar[int]
    cohesity_software_packages_vec: _containers.RepeatedScalarFieldContainer[str]
    packages_key: str
    def __init__(self, cohesity_software_packages_vec: _Optional[_Iterable[str]] = ..., packages_key: _Optional[str] = ...) -> None: ...

class PackagesConfigProto(_message.Message):
    __slots__ = ("repository_config_vec", "customer_software_packages_vec", "update_software_packages_vec", "update_all_packages", "custom_baseos_setup", "custom_baseos_linux_release_rpm_url", "customer_managed_baseos_setup")
    class RepositoryOption(_message.Message):
        __slots__ = ("option", "value")
        OPTION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        option: str
        value: str
        def __init__(self, option: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RepositoryConfig(_message.Message):
        __slots__ = ("id", "name", "url_path", "gpgkey", "enabled", "options_vec")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        URL_PATH_FIELD_NUMBER: _ClassVar[int]
        GPGKEY_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_VEC_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        url_path: str
        gpgkey: str
        enabled: bool
        options_vec: _containers.RepeatedCompositeFieldContainer[PackagesConfigProto.RepositoryOption]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., url_path: _Optional[str] = ..., gpgkey: _Optional[str] = ..., enabled: bool = ..., options_vec: _Optional[_Iterable[_Union[PackagesConfigProto.RepositoryOption, _Mapping]]] = ...) -> None: ...
    REPOSITORY_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SOFTWARE_PACKAGES_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SOFTWARE_PACKAGES_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ALL_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BASEOS_SETUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BASEOS_LINUX_RELEASE_RPM_URL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MANAGED_BASEOS_SETUP_FIELD_NUMBER: _ClassVar[int]
    repository_config_vec: _containers.RepeatedCompositeFieldContainer[PackagesConfigProto.RepositoryConfig]
    customer_software_packages_vec: _containers.RepeatedScalarFieldContainer[str]
    update_software_packages_vec: _containers.RepeatedScalarFieldContainer[str]
    update_all_packages: bool
    custom_baseos_setup: bool
    custom_baseos_linux_release_rpm_url: str
    customer_managed_baseos_setup: bool
    def __init__(self, repository_config_vec: _Optional[_Iterable[_Union[PackagesConfigProto.RepositoryConfig, _Mapping]]] = ..., customer_software_packages_vec: _Optional[_Iterable[str]] = ..., update_software_packages_vec: _Optional[_Iterable[str]] = ..., update_all_packages: bool = ..., custom_baseos_setup: bool = ..., custom_baseos_linux_release_rpm_url: _Optional[str] = ..., customer_managed_baseos_setup: bool = ...) -> None: ...

class PackagesStatusProto(_message.Message):
    __slots__ = ("software_version", "package_info_vec")
    class PackageInfo(_message.Message):
        __slots__ = ("name", "version", "release", "architecture", "signature", "packager", "vendor")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        RELEASE_FIELD_NUMBER: _ClassVar[int]
        ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        PACKAGER_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: str
        release: str
        architecture: str
        signature: str
        packager: str
        vendor: str
        def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., release: _Optional[str] = ..., architecture: _Optional[str] = ..., signature: _Optional[str] = ..., packager: _Optional[str] = ..., vendor: _Optional[str] = ...) -> None: ...
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    software_version: str
    package_info_vec: _containers.RepeatedCompositeFieldContainer[PackagesStatusProto.PackageInfo]
    def __init__(self, software_version: _Optional[str] = ..., package_info_vec: _Optional[_Iterable[_Union[PackagesStatusProto.PackageInfo, _Mapping]]] = ...) -> None: ...
