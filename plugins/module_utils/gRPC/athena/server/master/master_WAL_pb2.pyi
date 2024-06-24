from athena.base import athena_version_pb2 as _athena_version_pb2
from athena.base import athena_pb2 as _athena_pb2
from athena.base import rest_pb2 as _rest_pb2
from athena.server.master import master_pb2 as _master_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MasterWALRecordProto(_message.Message):
    __slots__ = ("version", "installed_app_vec", "launched_app_instance_vec", "volume_info_vec", "network_vec", "app_view_info_vec", "create_app_instance_spec", "update_app_instance_spec", "update_app_instance_status", "add_or_update_app_info", "delete_app_info", "delete_app_instance_id", "add_or_update_volume_info", "delete_volume_info_name", "add_or_update_network", "delete_network_name", "add_or_update_app_view_info", "delete_app_view_info_name")
    class LaunchedAppInstance(_message.Message):
        __slots__ = ("spec", "status")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        spec: _master_pb2.AppInstanceSpecProto
        status: _master_pb2.AppInstanceStatusProto
        def __init__(self, spec: _Optional[_Union[_master_pb2.AppInstanceSpecProto, _Mapping]] = ..., status: _Optional[_Union[_master_pb2.AppInstanceStatusProto, _Mapping]] = ...) -> None: ...
    class VolumeRecord(_message.Message):
        __slots__ = ("volume_info_proto", "create_volume_arg")
        VOLUME_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        CREATE_VOLUME_ARG_FIELD_NUMBER: _ClassVar[int]
        volume_info_proto: _athena_pb2.VolumeInfoProto
        create_volume_arg: _rest_pb2.CreateVolumeArg
        def __init__(self, volume_info_proto: _Optional[_Union[_athena_pb2.VolumeInfoProto, _Mapping]] = ..., create_volume_arg: _Optional[_Union[_rest_pb2.CreateVolumeArg, _Mapping]] = ...) -> None: ...
    class AppViewRecord(_message.Message):
        __slots__ = ("app_view_info_proto", "app_view_create_arg")
        APP_VIEW_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        APP_VIEW_CREATE_ARG_FIELD_NUMBER: _ClassVar[int]
        app_view_info_proto: _athena_pb2.AppViewInfoProto
        app_view_create_arg: _rest_pb2.AppViewCreateArg
        def __init__(self, app_view_info_proto: _Optional[_Union[_athena_pb2.AppViewInfoProto, _Mapping]] = ..., app_view_create_arg: _Optional[_Union[_rest_pb2.AppViewCreateArg, _Mapping]] = ...) -> None: ...
    class AppUidVersion(_message.Message):
        __slots__ = ("app_uid", "app_version")
        APP_UID_FIELD_NUMBER: _ClassVar[int]
        APP_VERSION_FIELD_NUMBER: _ClassVar[int]
        app_uid: int
        app_version: int
        def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_APP_VEC_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_APP_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_APP_INSTANCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_APP_INSTANCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_APP_INSTANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_APP_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_APP_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_VOLUME_INFO_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DELETE_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_APP_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_APP_VIEW_INFO_NAME_FIELD_NUMBER: _ClassVar[int]
    version: _athena_version_pb2.AthenaVersionProto
    installed_app_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.AppInfoProto]
    launched_app_instance_vec: _containers.RepeatedCompositeFieldContainer[MasterWALRecordProto.LaunchedAppInstance]
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[MasterWALRecordProto.VolumeRecord]
    network_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.NetworkProto]
    app_view_info_vec: _containers.RepeatedCompositeFieldContainer[MasterWALRecordProto.AppViewRecord]
    create_app_instance_spec: _master_pb2.AppInstanceSpecProto
    update_app_instance_spec: _master_pb2.AppInstanceSpecProto
    update_app_instance_status: _master_pb2.AppInstanceStatusProto
    add_or_update_app_info: _master_pb2.AppInfoProto
    delete_app_info: MasterWALRecordProto.AppUidVersion
    delete_app_instance_id: int
    add_or_update_volume_info: MasterWALRecordProto.VolumeRecord
    delete_volume_info_name: str
    add_or_update_network: _master_pb2.NetworkProto
    delete_network_name: str
    add_or_update_app_view_info: MasterWALRecordProto.AppViewRecord
    delete_app_view_info_name: str
    def __init__(self, version: _Optional[_Union[_athena_version_pb2.AthenaVersionProto, _Mapping]] = ..., installed_app_vec: _Optional[_Iterable[_Union[_master_pb2.AppInfoProto, _Mapping]]] = ..., launched_app_instance_vec: _Optional[_Iterable[_Union[MasterWALRecordProto.LaunchedAppInstance, _Mapping]]] = ..., volume_info_vec: _Optional[_Iterable[_Union[MasterWALRecordProto.VolumeRecord, _Mapping]]] = ..., network_vec: _Optional[_Iterable[_Union[_master_pb2.NetworkProto, _Mapping]]] = ..., app_view_info_vec: _Optional[_Iterable[_Union[MasterWALRecordProto.AppViewRecord, _Mapping]]] = ..., create_app_instance_spec: _Optional[_Union[_master_pb2.AppInstanceSpecProto, _Mapping]] = ..., update_app_instance_spec: _Optional[_Union[_master_pb2.AppInstanceSpecProto, _Mapping]] = ..., update_app_instance_status: _Optional[_Union[_master_pb2.AppInstanceStatusProto, _Mapping]] = ..., add_or_update_app_info: _Optional[_Union[_master_pb2.AppInfoProto, _Mapping]] = ..., delete_app_info: _Optional[_Union[MasterWALRecordProto.AppUidVersion, _Mapping]] = ..., delete_app_instance_id: _Optional[int] = ..., add_or_update_volume_info: _Optional[_Union[MasterWALRecordProto.VolumeRecord, _Mapping]] = ..., delete_volume_info_name: _Optional[str] = ..., add_or_update_network: _Optional[_Union[_master_pb2.NetworkProto, _Mapping]] = ..., delete_network_name: _Optional[str] = ..., add_or_update_app_view_info: _Optional[_Union[MasterWALRecordProto.AppViewRecord, _Mapping]] = ..., delete_app_view_info_name: _Optional[str] = ...) -> None: ...
