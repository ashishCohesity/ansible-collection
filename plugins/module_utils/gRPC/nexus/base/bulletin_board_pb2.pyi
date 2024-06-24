from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BulletinProto(_message.Message):
    __slots__ = ("row_vec",)
    class StateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kClusterVersion: _ClassVar[BulletinProto.StateType]
        kAppVersion: _ClassVar[BulletinProto.StateType]
    kClusterVersion: BulletinProto.StateType
    kAppVersion: BulletinProto.StateType
    class AppStateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGet: _ClassVar[BulletinProto.AppStateType]
        kInstall: _ClassVar[BulletinProto.AppStateType]
    kGet: BulletinProto.AppStateType
    kInstall: BulletinProto.AppStateType
    class StateValue(_message.Message):
        __slots__ = ("package_url", "target_software_version", "type", "app_id", "app_version")
        PACKAGE_URL_FIELD_NUMBER: _ClassVar[int]
        TARGET_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        APP_VERSION_FIELD_NUMBER: _ClassVar[int]
        package_url: str
        target_software_version: str
        type: BulletinProto.AppStateType
        app_id: int
        app_version: int
        def __init__(self, package_url: _Optional[str] = ..., target_software_version: _Optional[str] = ..., type: _Optional[_Union[BulletinProto.AppStateType, str]] = ..., app_id: _Optional[int] = ..., app_version: _Optional[int] = ...) -> None: ...
    class ClusterInfo(_message.Message):
        __slots__ = ("cluster_id", "cluster_incarnation_id")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        cluster_id: int
        cluster_incarnation_id: int
        def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...
    class UserInfo(_message.Message):
        __slots__ = ("name", "sid", "domain")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SID_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        name: str
        sid: str
        domain: str
        def __init__(self, name: _Optional[str] = ..., sid: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ("type", "state", "cluster_vec", "timestamp_msecs", "user")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        type: BulletinProto.StateType
        state: BulletinProto.StateValue
        cluster_vec: _containers.RepeatedCompositeFieldContainer[BulletinProto.ClusterInfo]
        timestamp_msecs: int
        user: BulletinProto.UserInfo
        def __init__(self, type: _Optional[_Union[BulletinProto.StateType, str]] = ..., state: _Optional[_Union[BulletinProto.StateValue, _Mapping]] = ..., cluster_vec: _Optional[_Iterable[_Union[BulletinProto.ClusterInfo, _Mapping]]] = ..., timestamp_msecs: _Optional[int] = ..., user: _Optional[_Union[BulletinProto.UserInfo, _Mapping]] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[BulletinProto.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[BulletinProto.Row, _Mapping]]] = ...) -> None: ...
