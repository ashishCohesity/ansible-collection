from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AthenaMountProto(_message.Message):
    __slots__ = ("view", "options", "view_mount_method", "mountdir", "poduid", "app_instance_authentication_token")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_METHOD_FIELD_NUMBER: _ClassVar[int]
    MOUNTDIR_FIELD_NUMBER: _ClassVar[int]
    PODUID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    view: str
    options: str
    view_mount_method: ViewMountMethod
    mountdir: str
    poduid: str
    app_instance_authentication_token: str
    def __init__(self, view: _Optional[str] = ..., options: _Optional[str] = ..., view_mount_method: _Optional[_Union[ViewMountMethod, _Mapping]] = ..., mountdir: _Optional[str] = ..., poduid: _Optional[str] = ..., app_instance_authentication_token: _Optional[str] = ...) -> None: ...

class ViewMountMethod(_message.Message):
    __slots__ = ("protocol", "server_ip", "username", "password", "namespace_name")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfs: _ClassVar[ViewMountMethod.Protocol]
        kSmb: _ClassVar[ViewMountMethod.Protocol]
        kVolume: _ClassVar[ViewMountMethod.Protocol]
    kNfs: ViewMountMethod.Protocol
    kSmb: ViewMountMethod.Protocol
    kVolume: ViewMountMethod.Protocol
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    protocol: ViewMountMethod.Protocol
    server_ip: str
    username: str
    password: str
    namespace_name: str
    def __init__(self, protocol: _Optional[_Union[ViewMountMethod.Protocol, str]] = ..., server_ip: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., namespace_name: _Optional[str] = ...) -> None: ...
