from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Identity(_message.Message):
    __slots__ = ("id", "display_name", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    email: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class SharepointIdentity(_message.Message):
    __slots__ = ("id", "display_name", "login_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    login_name: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., login_name: _Optional[str] = ...) -> None: ...

class IdentitySet(_message.Message):
    __slots__ = ("application", "device", "user", "owner", "conversation", "conversation_identity_type")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_IDENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    application: Identity
    device: Identity
    user: Identity
    owner: Identity
    conversation: Identity
    conversation_identity_type: Identity
    def __init__(self, application: _Optional[_Union[Identity, _Mapping]] = ..., device: _Optional[_Union[Identity, _Mapping]] = ..., user: _Optional[_Union[Identity, _Mapping]] = ..., owner: _Optional[_Union[Identity, _Mapping]] = ..., conversation: _Optional[_Union[Identity, _Mapping]] = ..., conversation_identity_type: _Optional[_Union[Identity, _Mapping]] = ...) -> None: ...

class SharepointIdentitySet(_message.Message):
    __slots__ = ("application", "device", "group", "user", "site_group", "site_user")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SITE_USER_FIELD_NUMBER: _ClassVar[int]
    application: Identity
    device: Identity
    group: Identity
    user: Identity
    site_group: SharepointIdentity
    site_user: SharepointIdentity
    def __init__(self, application: _Optional[_Union[Identity, _Mapping]] = ..., device: _Optional[_Union[Identity, _Mapping]] = ..., group: _Optional[_Union[Identity, _Mapping]] = ..., user: _Optional[_Union[Identity, _Mapping]] = ..., site_group: _Optional[_Union[SharepointIdentity, _Mapping]] = ..., site_user: _Optional[_Union[SharepointIdentity, _Mapping]] = ...) -> None: ...

class O365ErrorDBReportEntry(_message.Message):
    __slots__ = ("drive_info_vec",)
    class DriveInfo(_message.Message):
        __slots__ = ("drive_id", "drive_name", "num_errors")
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
        drive_id: str
        drive_name: str
        num_errors: int
        def __init__(self, drive_id: _Optional[str] = ..., drive_name: _Optional[str] = ..., num_errors: _Optional[int] = ...) -> None: ...
    DRIVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_info_vec: _containers.RepeatedCompositeFieldContainer[O365ErrorDBReportEntry.DriveInfo]
    def __init__(self, drive_info_vec: _Optional[_Iterable[_Union[O365ErrorDBReportEntry.DriveInfo, _Mapping]]] = ...) -> None: ...
