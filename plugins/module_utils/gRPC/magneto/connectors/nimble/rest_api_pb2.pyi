from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Volume(_message.Message):
    __slots__ = ("creation_time", "name", "serial_number", "size", "parent_vol_name", "id", "online", "online_snaps", "total_usage_bytes", "target_name", "base_snap_id", "lun")
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PARENT_VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SNAPS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAP_ID_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    creation_time: int
    name: str
    serial_number: str
    size: int
    parent_vol_name: str
    id: str
    online: bool
    online_snaps: _containers.RepeatedCompositeFieldContainer[Volume]
    total_usage_bytes: int
    target_name: str
    base_snap_id: str
    lun: int
    def __init__(self, creation_time: _Optional[int] = ..., name: _Optional[str] = ..., serial_number: _Optional[str] = ..., size: _Optional[int] = ..., parent_vol_name: _Optional[str] = ..., id: _Optional[str] = ..., online: bool = ..., online_snaps: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., total_usage_bytes: _Optional[int] = ..., target_name: _Optional[str] = ..., base_snap_id: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...

class GetAllVolumesResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, data: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("hgroup", "hgroup_id", "id", "ip_address", "name", "iqn", "wwn", "wwpn")
    HGROUP_FIELD_NUMBER: _ClassVar[int]
    HGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    WWPN_FIELD_NUMBER: _ClassVar[int]
    hgroup: str
    hgroup_id: str
    id: str
    ip_address: str
    name: str
    iqn: _containers.RepeatedScalarFieldContainer[str]
    wwn: _containers.RepeatedScalarFieldContainer[str]
    wwpn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hgroup: _Optional[str] = ..., hgroup_id: _Optional[str] = ..., id: _Optional[str] = ..., ip_address: _Optional[str] = ..., name: _Optional[str] = ..., iqn: _Optional[_Iterable[str]] = ..., wwn: _Optional[_Iterable[str]] = ..., wwpn: _Optional[_Iterable[str]] = ...) -> None: ...

class FCInterface(_message.Message):
    __slots__ = ("wwpn",)
    WWPN_FIELD_NUMBER: _ClassVar[int]
    wwpn: str
    def __init__(self, wwpn: _Optional[str] = ...) -> None: ...

class FetchFCResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[FCInterface]
    def __init__(self, data: _Optional[_Iterable[_Union[FCInterface, _Mapping]]] = ...) -> None: ...

class VolumeArea(_message.Message):
    __slots__ = ("offset", "length", "startRow", "endRow")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    STARTROW_FIELD_NUMBER: _ClassVar[int]
    ENDROW_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    startRow: int
    endRow: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., startRow: _Optional[int] = ..., endRow: _Optional[int] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateVolumeRequest(_message.Message):
    __slots__ = ("name", "size", "clone", "base_snap_id", "online", "perfpolicy_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CLONE_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAP_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    PERFPOLICY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    clone: bool
    base_snap_id: str
    online: bool
    perfpolicy_id: str
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., clone: bool = ..., base_snap_id: _Optional[str] = ..., online: bool = ..., perfpolicy_id: _Optional[str] = ...) -> None: ...

class CreateVolumeRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: CreateVolumeRequest
    def __init__(self, data: _Optional[_Union[CreateVolumeRequest, _Mapping]] = ...) -> None: ...

class CreateVolumeResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateVolumeResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Volume
    def __init__(self, data: _Optional[_Union[Volume, _Mapping]] = ...) -> None: ...

class OfflineVolumeRequest(_message.Message):
    __slots__ = ("name", "id", "online", "online_snaps", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SNAPS_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    online: bool
    online_snaps: _containers.RepeatedCompositeFieldContainer[Volume]
    force: bool
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., online: bool = ..., online_snaps: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., force: bool = ...) -> None: ...

class OfflineVolumeResponse(_message.Message):
    __slots__ = ("name", "id", "online", "online_snaps")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SNAPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    online: bool
    online_snaps: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., online: bool = ..., online_snaps: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class OfflineVolumeRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: OfflineVolumeRequest
    def __init__(self, data: _Optional[_Union[OfflineVolumeRequest, _Mapping]] = ...) -> None: ...

class OfflineSnapshotRequest(_message.Message):
    __slots__ = ("name", "online")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    name: str
    online: bool
    def __init__(self, name: _Optional[str] = ..., online: bool = ...) -> None: ...

class OfflineSnapshotResponse(_message.Message):
    __slots__ = ("name", "online")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    name: str
    online: bool
    def __init__(self, name: _Optional[str] = ..., online: bool = ...) -> None: ...

class OfflineSnapshotRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: OfflineSnapshotRequest
    def __init__(self, data: _Optional[_Union[OfflineSnapshotRequest, _Mapping]] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("online", "name", "vol_id")
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    online: bool
    name: str
    vol_id: str
    def __init__(self, online: bool = ..., name: _Optional[str] = ..., vol_id: _Optional[str] = ...) -> None: ...

class CreateSnapshotRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: CreateSnapshotRequest
    def __init__(self, data: _Optional[_Union[CreateSnapshotRequest, _Mapping]] = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CreateSnapshotResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: CreateSnapshotResponse
    def __init__(self, data: _Optional[_Union[CreateSnapshotResponse, _Mapping]] = ...) -> None: ...

class AccessControlRecord(_message.Message):
    __slots__ = ("access_protocol", "id", "initiator_group_id", "initiator_group_name", "lun")
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    access_protocol: str
    id: str
    initiator_group_id: str
    initiator_group_name: str
    lun: int
    def __init__(self, access_protocol: _Optional[str] = ..., id: _Optional[str] = ..., initiator_group_id: _Optional[str] = ..., initiator_group_name: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...

class GetVolumeResponse(_message.Message):
    __slots__ = ("id", "name", "online", "size", "owned_by_group_id", "online_snaps", "serial_number", "access_control_records")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OWNED_BY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SNAPS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_RECORDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    online: bool
    size: int
    owned_by_group_id: str
    online_snaps: _containers.RepeatedCompositeFieldContainer[Volume]
    serial_number: str
    access_control_records: _containers.RepeatedCompositeFieldContainer[AccessControlRecord]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., online: bool = ..., size: _Optional[int] = ..., owned_by_group_id: _Optional[str] = ..., online_snaps: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., serial_number: _Optional[str] = ..., access_control_records: _Optional[_Iterable[_Union[AccessControlRecord, _Mapping]]] = ...) -> None: ...

class GetVolumeResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[GetVolumeResponse]
    def __init__(self, data: _Optional[_Iterable[_Union[GetVolumeResponse, _Mapping]]] = ...) -> None: ...

class GetSnapshotsResponse(_message.Message):
    __slots__ = ("id", "vol_name", "vol_id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    vol_name: str
    vol_id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., vol_name: _Optional[str] = ..., vol_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetSnapshotsResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CreateSnapshotResponse]
    def __init__(self, data: _Optional[_Iterable[_Union[CreateSnapshotResponse, _Mapping]]] = ...) -> None: ...

class GetVolumeAreasResponse(_message.Message):
    __slots__ = ("volume_area_vec",)
    VOLUME_AREA_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_area_vec: _containers.RepeatedCompositeFieldContainer[VolumeArea]
    def __init__(self, volume_area_vec: _Optional[_Iterable[_Union[VolumeArea, _Mapping]]] = ...) -> None: ...

class CreateVolumeSnapshotRequest(_message.Message):
    __slots__ = ("writable", "vol_id", "name")
    WRITABLE_FIELD_NUMBER: _ClassVar[int]
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    writable: bool
    vol_id: str
    name: str
    def __init__(self, writable: bool = ..., vol_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateVolumeSnapshotResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: Volume
    def __init__(self, snapshot: _Optional[_Union[Volume, _Mapping]] = ...) -> None: ...

class DeleteVolumeRequest(_message.Message):
    __slots__ = ("online",)
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    online: bool
    def __init__(self, online: bool = ...) -> None: ...

class DeleteVolumeResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetHGroupsResponse(_message.Message):
    __slots__ = ("id", "name", "access_protocol", "iscsi_initiators", "volume_list", "fc_initiators")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ISCSI_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LIST_FIELD_NUMBER: _ClassVar[int]
    FC_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    access_protocol: str
    iscsi_initiators: _containers.RepeatedCompositeFieldContainer[Host]
    volume_list: _containers.RepeatedCompositeFieldContainer[Volume]
    fc_initiators: _containers.RepeatedCompositeFieldContainer[Host]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., access_protocol: _Optional[str] = ..., iscsi_initiators: _Optional[_Iterable[_Union[Host, _Mapping]]] = ..., volume_list: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., fc_initiators: _Optional[_Iterable[_Union[Host, _Mapping]]] = ...) -> None: ...

class GetHGroupsResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[GetHGroupsResponse]
    def __init__(self, data: _Optional[_Iterable[_Union[GetHGroupsResponse, _Mapping]]] = ...) -> None: ...

class Initiator(_message.Message):
    __slots__ = ("iqn", "ip_address", "wwpn", "label", "initiator_group_id", "alias")
    IQN_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WWPN_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    iqn: str
    ip_address: str
    wwpn: str
    label: str
    initiator_group_id: str
    alias: str
    def __init__(self, iqn: _Optional[str] = ..., ip_address: _Optional[str] = ..., wwpn: _Optional[str] = ..., label: _Optional[str] = ..., initiator_group_id: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...

class UpdateIGroupConnectionsRequest(_message.Message):
    __slots__ = ("access_protocol", "initiator_group_id", "name", "iscsi_initiators", "fc_initiators")
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISCSI_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    FC_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    access_protocol: str
    initiator_group_id: str
    name: str
    iscsi_initiators: _containers.RepeatedCompositeFieldContainer[Initiator]
    fc_initiators: _containers.RepeatedCompositeFieldContainer[Initiator]
    def __init__(self, access_protocol: _Optional[str] = ..., initiator_group_id: _Optional[str] = ..., name: _Optional[str] = ..., iscsi_initiators: _Optional[_Iterable[_Union[Initiator, _Mapping]]] = ..., fc_initiators: _Optional[_Iterable[_Union[Initiator, _Mapping]]] = ...) -> None: ...

class UpdateIGroupConnectionsResponse(_message.Message):
    __slots__ = ("name", "id", "iscsi_initiators", "fc_initiators")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISCSI_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    FC_INITIATORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    iscsi_initiators: _containers.RepeatedCompositeFieldContainer[Initiator]
    fc_initiators: _containers.RepeatedCompositeFieldContainer[Initiator]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., iscsi_initiators: _Optional[_Iterable[_Union[Initiator, _Mapping]]] = ..., fc_initiators: _Optional[_Iterable[_Union[Initiator, _Mapping]]] = ...) -> None: ...

class UpdateIGroupConnectionsRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: UpdateIGroupConnectionsRequest
    def __init__(self, data: _Optional[_Union[UpdateIGroupConnectionsRequest, _Mapping]] = ...) -> None: ...

class UpdateIGroupConnectionsResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: UpdateIGroupConnectionsResponse
    def __init__(self, data: _Optional[_Union[UpdateIGroupConnectionsResponse, _Mapping]] = ...) -> None: ...

class UpdateHostConnectionRequest(_message.Message):
    __slots__ = ("vol_id", "apply_to", "initiator_group_id", "chap_user_id")
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    APPLY_TO_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAP_USER_ID_FIELD_NUMBER: _ClassVar[int]
    vol_id: str
    apply_to: str
    initiator_group_id: str
    chap_user_id: str
    def __init__(self, vol_id: _Optional[str] = ..., apply_to: _Optional[str] = ..., initiator_group_id: _Optional[str] = ..., chap_user_id: _Optional[str] = ...) -> None: ...

class UpdateHostConnectionResponse(_message.Message):
    __slots__ = ("id", "vol_name", "vol_id", "initiator_group_id", "initiator_group_name", "lun")
    ID_FIELD_NUMBER: _ClassVar[int]
    VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    id: str
    vol_name: str
    vol_id: str
    initiator_group_id: str
    initiator_group_name: str
    lun: int
    def __init__(self, id: _Optional[str] = ..., vol_name: _Optional[str] = ..., vol_id: _Optional[str] = ..., initiator_group_id: _Optional[str] = ..., initiator_group_name: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...

class UpdateHostConnectionRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: UpdateHostConnectionRequest
    def __init__(self, data: _Optional[_Union[UpdateHostConnectionRequest, _Mapping]] = ...) -> None: ...

class UpdateHostConnectionResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[UpdateHostConnectionResponse]
    def __init__(self, data: _Optional[_Iterable[_Union[UpdateHostConnectionResponse, _Mapping]]] = ...) -> None: ...

class UpdateVolumeInitiatorConnectionsRequest(_message.Message):
    __slots__ = ("id", "name", "owned_by_group_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNED_BY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    owned_by_group_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., owned_by_group_id: _Optional[str] = ...) -> None: ...

class UpdateVolumeInitiatorConnectionsResponse(_message.Message):
    __slots__ = ("id", "name", "owned_by_group_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNED_BY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    owned_by_group_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., owned_by_group_id: _Optional[str] = ...) -> None: ...

class UpdateVolumeInitiatorConnectionsRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: UpdateVolumeInitiatorConnectionsRequest
    def __init__(self, data: _Optional[_Union[UpdateVolumeInitiatorConnectionsRequest, _Mapping]] = ...) -> None: ...

class UpdateVolumeInitiatorConnectionsResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: UpdateVolumeInitiatorConnectionsResponse
    def __init__(self, data: _Optional[_Union[UpdateVolumeInitiatorConnectionsResponse, _Mapping]] = ...) -> None: ...

class GetVolumeInitiatorConnectionsResponse(_message.Message):
    __slots__ = ("id", "iqn", "initiator_group_name", "initiator_group_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    iqn: str
    initiator_group_name: str
    initiator_group_id: str
    def __init__(self, id: _Optional[str] = ..., iqn: _Optional[str] = ..., initiator_group_name: _Optional[str] = ..., initiator_group_id: _Optional[str] = ...) -> None: ...

class CreateTokenRequest(_message.Message):
    __slots__ = ("source_ip", "password", "username")
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    source_ip: str
    password: str
    username: str
    def __init__(self, source_ip: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class CreateTokenResponse(_message.Message):
    __slots__ = ("source_ip", "id", "session_token", "creation_time", "last_modified")
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    source_ip: str
    id: str
    session_token: str
    creation_time: int
    last_modified: int
    def __init__(self, source_ip: _Optional[str] = ..., id: _Optional[str] = ..., session_token: _Optional[str] = ..., creation_time: _Optional[int] = ..., last_modified: _Optional[int] = ...) -> None: ...

class CreateTokenRequestData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: CreateTokenRequest
    def __init__(self, data: _Optional[_Union[CreateTokenRequest, _Mapping]] = ...) -> None: ...

class CreateTokenResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: CreateTokenResponse
    def __init__(self, data: _Optional[_Union[CreateTokenResponse, _Mapping]] = ...) -> None: ...

class GetInitiatorResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Initiator]
    def __init__(self, data: _Optional[_Iterable[_Union[Initiator, _Mapping]]] = ...) -> None: ...

class GetArrayResponse(_message.Message):
    __slots__ = ("name", "id", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    version: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetArrayResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[GetArrayResponse]
    def __init__(self, data: _Optional[_Iterable[_Union[GetArrayResponse, _Mapping]]] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("label", "discovery_ip")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_IP_FIELD_NUMBER: _ClassVar[int]
    label: str
    discovery_ip: str
    def __init__(self, label: _Optional[str] = ..., discovery_ip: _Optional[str] = ...) -> None: ...

class GetSubnetList(_message.Message):
    __slots__ = ("subnet_list",)
    SUBNET_LIST_FIELD_NUMBER: _ClassVar[int]
    subnet_list: _containers.RepeatedCompositeFieldContainer[Subnet]
    def __init__(self, subnet_list: _Optional[_Iterable[_Union[Subnet, _Mapping]]] = ...) -> None: ...

class GetNetworkConfigResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[GetSubnetList]
    def __init__(self, data: _Optional[_Iterable[_Union[GetSubnetList, _Mapping]]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("group_target_enabled", "group_target_name")
    GROUP_TARGET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GROUP_TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    group_target_enabled: bool
    group_target_name: str
    def __init__(self, group_target_enabled: bool = ..., group_target_name: _Optional[str] = ...) -> None: ...

class GetGroupsResponseData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, data: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...
