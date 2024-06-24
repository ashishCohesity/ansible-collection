from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurchasedAppInfo(_message.Message):
    __slots__ = ("name", "version_id", "dev_version", "icon_image", "purchased", "my_prod_version_info", "latest_version_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_VERSION_FIELD_NUMBER: _ClassVar[int]
    ICON_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_FIELD_NUMBER: _ClassVar[int]
    MY_PROD_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_id: int
    dev_version: str
    icon_image: bytes
    purchased: bool
    my_prod_version_info: AppVersionInfo
    latest_version_info: AppVersionInfo
    def __init__(self, name: _Optional[str] = ..., version_id: _Optional[int] = ..., dev_version: _Optional[str] = ..., icon_image: _Optional[bytes] = ..., purchased: bool = ..., my_prod_version_info: _Optional[_Union[AppVersionInfo, _Mapping]] = ..., latest_version_info: _Optional[_Union[AppVersionInfo, _Mapping]] = ...) -> None: ...

class AppVersionInfo(_message.Message):
    __slots__ = ("version_id", "version_name")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    version_name: str
    def __init__(self, version_id: _Optional[int] = ..., version_name: _Optional[str] = ...) -> None: ...

class InstalledAppInfo(_message.Message):
    __slots__ = ("version_id", "installed", "force_update", "latest_compatible_version_id")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_COMPATIBLE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    installed: bool
    force_update: bool
    latest_compatible_version_id: int
    def __init__(self, version_id: _Optional[int] = ..., installed: bool = ..., force_update: bool = ..., latest_compatible_version_id: _Optional[int] = ...) -> None: ...
