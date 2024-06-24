from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorContext(_message.Message):
    __slots__ = ("msg", "return_code", "error_code")
    MSG_FIELD_NUMBER: _ClassVar[int]
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    msg: str
    return_code: str
    error_code: str
    def __init__(self, msg: _Optional[str] = ..., return_code: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class ErrorContextVec(_message.Message):
    __slots__ = ("error_ctx_vec",)
    ERROR_CTX_VEC_FIELD_NUMBER: _ClassVar[int]
    error_ctx_vec: _containers.RepeatedCompositeFieldContainer[ErrorContext]
    def __init__(self, error_ctx_vec: _Optional[_Iterable[_Union[ErrorContext, _Mapping]]] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class LsVolumeGroupSnapshotRequest(_message.Message):
    __slots__ = ("snapshot_id", "volumegroup", "parentuid", "snapshot", "filtervalue")
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUMEGROUP_FIELD_NUMBER: _ClassVar[int]
    PARENTUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: str
    volumegroup: str
    parentuid: str
    snapshot: str
    filtervalue: str
    def __init__(self, snapshot_id: _Optional[str] = ..., volumegroup: _Optional[str] = ..., parentuid: _Optional[str] = ..., snapshot: _Optional[str] = ..., filtervalue: _Optional[str] = ...) -> None: ...

class VolumeGroupSnapshot(_message.Message):
    __slots__ = ("id", "name", "volume_group_id", "volume_group_name", "time", "state", "expiration_time", "safeguarded")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SAFEGUARDED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    volume_group_id: str
    volume_group_name: str
    time: str
    state: str
    expiration_time: str
    safeguarded: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., volume_group_id: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., time: _Optional[str] = ..., state: _Optional[str] = ..., expiration_time: _Optional[str] = ..., safeguarded: _Optional[str] = ...) -> None: ...

class LsVolumeGroupSnapshotResponse(_message.Message):
    __slots__ = ("snapshot_vec",)
    SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_vec: _containers.RepeatedCompositeFieldContainer[VolumeGroupSnapshot]
    def __init__(self, snapshot_vec: _Optional[_Iterable[_Union[VolumeGroupSnapshot, _Mapping]]] = ...) -> None: ...

class AddSnapshotRequest(_message.Message):
    __slots__ = ("name", "volumegroup", "volumes", "safeguarded", "retentiondays")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUMEGROUP_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    SAFEGUARDED_FIELD_NUMBER: _ClassVar[int]
    RETENTIONDAYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    volumegroup: str
    volumes: str
    safeguarded: bool
    retentiondays: int
    def __init__(self, name: _Optional[str] = ..., volumegroup: _Optional[str] = ..., volumes: _Optional[str] = ..., safeguarded: bool = ..., retentiondays: _Optional[int] = ...) -> None: ...

class AddSnapshotResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class VolumeGroup(_message.Message):
    __slots__ = ("id", "name", "volume_count", "volume_group_type", "uid")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    volume_count: str
    volume_group_type: str
    uid: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., volume_count: _Optional[str] = ..., volume_group_type: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class LsVolumeGroupRequest(_message.Message):
    __slots__ = ("filtervalue",)
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    filtervalue: str
    def __init__(self, filtervalue: _Optional[str] = ...) -> None: ...

class LsVolumeGroupResponse(_message.Message):
    __slots__ = ("volume_group_vec",)
    VOLUME_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_group_vec: _containers.RepeatedCompositeFieldContainer[VolumeGroup]
    def __init__(self, volume_group_vec: _Optional[_Iterable[_Union[VolumeGroup, _Mapping]]] = ...) -> None: ...

class DeleteVolumeRequest(_message.Message):
    __slots__ = ("removehostmappings", "removercrelationships", "removefcmaps", "discardimage", "cancelbackup")
    REMOVEHOSTMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    REMOVERCRELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    REMOVEFCMAPS_FIELD_NUMBER: _ClassVar[int]
    DISCARDIMAGE_FIELD_NUMBER: _ClassVar[int]
    CANCELBACKUP_FIELD_NUMBER: _ClassVar[int]
    removehostmappings: bool
    removercrelationships: bool
    removefcmaps: bool
    discardimage: bool
    cancelbackup: bool
    def __init__(self, removehostmappings: bool = ..., removercrelationships: bool = ..., removefcmaps: bool = ..., discardimage: bool = ..., cancelbackup: bool = ...) -> None: ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ("volumegroup", "parentuid", "snapshot", "snapshotid")
    VOLUMEGROUP_FIELD_NUMBER: _ClassVar[int]
    PARENTUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTID_FIELD_NUMBER: _ClassVar[int]
    volumegroup: str
    parentuid: int
    snapshot: str
    snapshotid: int
    def __init__(self, volumegroup: _Optional[str] = ..., parentuid: _Optional[int] = ..., snapshot: _Optional[str] = ..., snapshotid: _Optional[int] = ...) -> None: ...

class MkVolumeGroupRequest(_message.Message):
    __slots__ = ("name", "type", "snapshot", "fromsnapshotid", "pool")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FROMSNAPSHOTID_FIELD_NUMBER: _ClassVar[int]
    POOL_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    snapshot: str
    fromsnapshotid: str
    pool: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., snapshot: _Optional[str] = ..., fromsnapshotid: _Optional[str] = ..., pool: _Optional[str] = ...) -> None: ...

class MkVolumeGroupResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class LsVdiskRequest(_message.Message):
    __slots__ = ("filtervalue", "use_bytes")
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    USE_BYTES_FIELD_NUMBER: _ClassVar[int]
    filtervalue: str
    use_bytes: bool
    def __init__(self, filtervalue: _Optional[str] = ..., use_bytes: bool = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("id", "name", "status", "capacity", "type", "vdisk_UID", "volume_group_id", "volume_group_name", "volume_type", "source_volume_id", "source_volume_name", "source_snapshot", "io_group_name", "io_group_id", "mdisk_grp_id", "mdisk_grp_name", "copy_count", "copy_copy_id", "copy_se_copy", "copy_compressed_copy", "copy_deduplicated_copy", "copy_primary")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VDISK_UID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    IO_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MDISK_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    MDISK_GRP_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_COUNT_FIELD_NUMBER: _ClassVar[int]
    COPY_COPY_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_SE_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_COMPRESSED_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_DEDUPLICATED_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: str
    capacity: str
    type: str
    vdisk_UID: str
    volume_group_id: str
    volume_group_name: str
    volume_type: str
    source_volume_id: str
    source_volume_name: str
    source_snapshot: str
    io_group_name: str
    io_group_id: str
    mdisk_grp_id: str
    mdisk_grp_name: str
    copy_count: str
    copy_copy_id: str
    copy_se_copy: str
    copy_compressed_copy: str
    copy_deduplicated_copy: str
    copy_primary: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., capacity: _Optional[str] = ..., type: _Optional[str] = ..., vdisk_UID: _Optional[str] = ..., volume_group_id: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., volume_type: _Optional[str] = ..., source_volume_id: _Optional[str] = ..., source_volume_name: _Optional[str] = ..., source_snapshot: _Optional[str] = ..., io_group_name: _Optional[str] = ..., io_group_id: _Optional[str] = ..., mdisk_grp_id: _Optional[str] = ..., mdisk_grp_name: _Optional[str] = ..., copy_count: _Optional[str] = ..., copy_copy_id: _Optional[str] = ..., copy_se_copy: _Optional[str] = ..., copy_compressed_copy: _Optional[str] = ..., copy_deduplicated_copy: _Optional[str] = ..., copy_primary: _Optional[str] = ...) -> None: ...

class LsVdiskResponse(_message.Message):
    __slots__ = ("volume_vec",)
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class VolumeHostMap(_message.Message):
    __slots__ = ("id", "name", "SCSI_id", "host_id", "host_name", "vdisk_UID")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCSI_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    VDISK_UID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    SCSI_id: str
    host_id: str
    host_name: str
    vdisk_UID: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., SCSI_id: _Optional[str] = ..., host_id: _Optional[str] = ..., host_name: _Optional[str] = ..., vdisk_UID: _Optional[str] = ...) -> None: ...

class LsVolumeHostMapResponse(_message.Message):
    __slots__ = ("volume_host_map_vec",)
    VOLUME_HOST_MAP_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_host_map_vec: _containers.RepeatedCompositeFieldContainer[VolumeHostMap]
    def __init__(self, volume_host_map_vec: _Optional[_Iterable[_Union[VolumeHostMap, _Mapping]]] = ...) -> None: ...

class MkVolumeHostMapRequest(_message.Message):
    __slots__ = ("host", "scsi")
    HOST_FIELD_NUMBER: _ClassVar[int]
    SCSI_FIELD_NUMBER: _ClassVar[int]
    host: str
    scsi: str
    def __init__(self, host: _Optional[str] = ..., scsi: _Optional[str] = ...) -> None: ...

class MkVolumeHostMapResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RmVolumeHostMapRequest(_message.Message):
    __slots__ = ("host",)
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: str
    def __init__(self, host: _Optional[str] = ...) -> None: ...

class LsVolumePopulationRequest(_message.Message):
    __slots__ = ("filtervalue",)
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    filtervalue: str
    def __init__(self, filtervalue: _Optional[str] = ...) -> None: ...

class LsVolumePopulationResponse(_message.Message):
    __slots__ = ("volume_vec",)
    class Volume(_message.Message):
        __slots__ = ("volume_id", "volume_name", "volume_group_id", "volume_group_name", "volume_type", "source_volume_id", "source_volume_name", "source_snapshot")
        VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        volume_id: str
        volume_name: str
        volume_group_id: str
        volume_group_name: str
        volume_type: str
        source_volume_id: str
        source_volume_name: str
        source_snapshot: str
        def __init__(self, volume_id: _Optional[str] = ..., volume_name: _Optional[str] = ..., volume_group_id: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., volume_type: _Optional[str] = ..., source_volume_id: _Optional[str] = ..., source_volume_name: _Optional[str] = ..., source_snapshot: _Optional[str] = ...) -> None: ...
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[LsVolumePopulationResponse.Volume]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[LsVolumePopulationResponse.Volume, _Mapping]]] = ...) -> None: ...

class LsFlashSystemRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FlashSystem(_message.Message):
    __slots__ = ("id", "id_alias", "name", "code_level")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_ALIAS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    id_alias: str
    name: str
    code_level: str
    def __init__(self, id: _Optional[str] = ..., id_alias: _Optional[str] = ..., name: _Optional[str] = ..., code_level: _Optional[str] = ...) -> None: ...

class LsSystemResponse(_message.Message):
    __slots__ = ("system",)
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    system: FlashSystem
    def __init__(self, system: _Optional[_Union[FlashSystem, _Mapping]] = ...) -> None: ...

class LsNodeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Node(_message.Message):
    __slots__ = ("id", "name", "iscsi_name", "io_group_id", "io_group_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISCSI_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IO_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    iscsi_name: str
    io_group_id: str
    io_group_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., iscsi_name: _Optional[str] = ..., io_group_id: _Optional[str] = ..., io_group_name: _Optional[str] = ...) -> None: ...

class LsNodeResponse(_message.Message):
    __slots__ = ("node_vec",)
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, node_vec: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class LsIpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NodeIp(_message.Message):
    __slots__ = ("id", "node_id", "node_name", "ip_address")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    node_id: str
    node_name: str
    ip_address: str
    def __init__(self, id: _Optional[str] = ..., node_id: _Optional[str] = ..., node_name: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...

class LsIpResponse(_message.Message):
    __slots__ = ("node_ip_vec",)
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    node_ip_vec: _containers.RepeatedCompositeFieldContainer[NodeIp]
    def __init__(self, node_ip_vec: _Optional[_Iterable[_Union[NodeIp, _Mapping]]] = ...) -> None: ...

class LsHostRequest(_message.Message):
    __slots__ = ("filtervalue",)
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    filtervalue: str
    def __init__(self, filtervalue: _Optional[str] = ...) -> None: ...

class LsHostResponse(_message.Message):
    __slots__ = ("id", "name", "port_count", "type", "status", "protocol", "nodes", "portset_id", "portset_name")
    class HostPort(_message.Message):
        __slots__ = ("iscsi_name", "node_logged_in_count", "state", "wwpn")
        ISCSI_NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_LOGGED_IN_COUNT_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        WWPN_FIELD_NUMBER: _ClassVar[int]
        iscsi_name: str
        node_logged_in_count: str
        state: str
        wwpn: str
        def __init__(self, iscsi_name: _Optional[str] = ..., node_logged_in_count: _Optional[str] = ..., state: _Optional[str] = ..., wwpn: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    PORTSET_ID_FIELD_NUMBER: _ClassVar[int]
    PORTSET_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    port_count: str
    type: str
    status: str
    protocol: str
    nodes: _containers.RepeatedCompositeFieldContainer[LsHostResponse.HostPort]
    portset_id: str
    portset_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., port_count: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[str] = ..., protocol: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[LsHostResponse.HostPort, _Mapping]]] = ..., portset_id: _Optional[str] = ..., portset_name: _Optional[str] = ...) -> None: ...

class MkHostRequest(_message.Message):
    __slots__ = ("name", "protocol", "fcwwpn", "iscsiname", "force", "hostcluster")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FCWWPN_FIELD_NUMBER: _ClassVar[int]
    ISCSINAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    HOSTCLUSTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    protocol: str
    fcwwpn: str
    iscsiname: str
    force: bool
    hostcluster: str
    def __init__(self, name: _Optional[str] = ..., protocol: _Optional[str] = ..., fcwwpn: _Optional[str] = ..., iscsiname: _Optional[str] = ..., force: bool = ..., hostcluster: _Optional[str] = ...) -> None: ...

class MkHostResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class AddHostportRequest(_message.Message):
    __slots__ = ("fcwwpn", "iscsiname")
    FCWWPN_FIELD_NUMBER: _ClassVar[int]
    ISCSINAME_FIELD_NUMBER: _ClassVar[int]
    fcwwpn: str
    iscsiname: str
    def __init__(self, fcwwpn: _Optional[str] = ..., iscsiname: _Optional[str] = ...) -> None: ...

class RmHostportRequest(_message.Message):
    __slots__ = ("fcwwpn", "iscsiname")
    FCWWPN_FIELD_NUMBER: _ClassVar[int]
    ISCSINAME_FIELD_NUMBER: _ClassVar[int]
    fcwwpn: str
    iscsiname: str
    def __init__(self, fcwwpn: _Optional[str] = ..., iscsiname: _Optional[str] = ...) -> None: ...

class MkVolumeRequest(_message.Message):
    __slots__ = ("name", "pool", "size", "unit", "volumegroup", "thin", "compressed", "deduplicated")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POOL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VOLUMEGROUP_FIELD_NUMBER: _ClassVar[int]
    THIN_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    pool: str
    size: int
    unit: str
    volumegroup: str
    thin: bool
    compressed: bool
    deduplicated: bool
    def __init__(self, name: _Optional[str] = ..., pool: _Optional[str] = ..., size: _Optional[int] = ..., unit: _Optional[str] = ..., volumegroup: _Optional[str] = ..., thin: bool = ..., compressed: bool = ..., deduplicated: bool = ...) -> None: ...

class MkVolumeResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class LsMdiskgrpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Mdiskgrp(_message.Message):
    __slots__ = ("id", "name", "type", "status", "parent_mdisk_grp_id", "parent_mdisk_grp_name", "data_reduction", "provisioning_policy_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PARENT_MDISK_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MDISK_GRP_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    status: str
    parent_mdisk_grp_id: str
    parent_mdisk_grp_name: str
    data_reduction: str
    provisioning_policy_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[str] = ..., parent_mdisk_grp_id: _Optional[str] = ..., parent_mdisk_grp_name: _Optional[str] = ..., data_reduction: _Optional[str] = ..., provisioning_policy_id: _Optional[str] = ...) -> None: ...

class LsMdiskgrpResponse(_message.Message):
    __slots__ = ("mdiskgrp_vec",)
    MDISKGRP_VEC_FIELD_NUMBER: _ClassVar[int]
    mdiskgrp_vec: _containers.RepeatedCompositeFieldContainer[Mdiskgrp]
    def __init__(self, mdiskgrp_vec: _Optional[_Iterable[_Union[Mdiskgrp, _Mapping]]] = ...) -> None: ...

class LsIogrpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Iogrp(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class LsIogrpResponse(_message.Message):
    __slots__ = ("iogrp_vec",)
    IOGRP_VEC_FIELD_NUMBER: _ClassVar[int]
    iogrp_vec: _containers.RepeatedCompositeFieldContainer[Iogrp]
    def __init__(self, iogrp_vec: _Optional[_Iterable[_Union[Iogrp, _Mapping]]] = ...) -> None: ...

class VolumeHostClusterMap(_message.Message):
    __slots__ = ("id", "name", "scsi_id", "volume_id", "volume_name", "volume_uid")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCSI_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_UID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    scsi_id: str
    volume_id: str
    volume_name: str
    volume_uid: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., scsi_id: _Optional[str] = ..., volume_id: _Optional[str] = ..., volume_name: _Optional[str] = ..., volume_uid: _Optional[str] = ...) -> None: ...

class LsVolumeHostClusterMapResponse(_message.Message):
    __slots__ = ("volume_host_cluster_map_vec",)
    VOLUME_HOST_CLUSTER_MAP_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_host_cluster_map_vec: _containers.RepeatedCompositeFieldContainer[VolumeHostClusterMap]
    def __init__(self, volume_host_cluster_map_vec: _Optional[_Iterable[_Union[VolumeHostClusterMap, _Mapping]]] = ...) -> None: ...

class MkVolumeHostClusterMapRequest(_message.Message):
    __slots__ = ("host_cluster", "scsi", "force")
    HOST_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SCSI_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    host_cluster: str
    scsi: str
    force: bool
    def __init__(self, host_cluster: _Optional[str] = ..., scsi: _Optional[str] = ..., force: bool = ...) -> None: ...

class MkVolumeHostClusterMapResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RmVolumeHostClusterMapRequest(_message.Message):
    __slots__ = ("host_cluster",)
    HOST_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    host_cluster: str
    def __init__(self, host_cluster: _Optional[str] = ...) -> None: ...

class LsPortFcResponse(_message.Message):
    __slots__ = ("fc_ports_vec",)
    class FcPort(_message.Message):
        __slots__ = ("id", "fc_io_port_id", "port_id", "type", "port_speed", "node_id", "node_name", "wwpn", "nportid", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        FC_IO_PORT_ID_FIELD_NUMBER: _ClassVar[int]
        PORT_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PORT_SPEED_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_NAME_FIELD_NUMBER: _ClassVar[int]
        WWPN_FIELD_NUMBER: _ClassVar[int]
        NPORTID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: str
        fc_io_port_id: str
        port_id: str
        type: str
        port_speed: str
        node_id: str
        node_name: str
        wwpn: str
        nportid: str
        status: str
        def __init__(self, id: _Optional[str] = ..., fc_io_port_id: _Optional[str] = ..., port_id: _Optional[str] = ..., type: _Optional[str] = ..., port_speed: _Optional[str] = ..., node_id: _Optional[str] = ..., node_name: _Optional[str] = ..., wwpn: _Optional[str] = ..., nportid: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...
    FC_PORTS_VEC_FIELD_NUMBER: _ClassVar[int]
    fc_ports_vec: _containers.RepeatedCompositeFieldContainer[LsPortFcResponse.FcPort]
    def __init__(self, fc_ports_vec: _Optional[_Iterable[_Union[LsPortFcResponse.FcPort, _Mapping]]] = ...) -> None: ...

class RmHostRequest(_message.Message):
    __slots__ = ("force",)
    FORCE_FIELD_NUMBER: _ClassVar[int]
    force: bool
    def __init__(self, force: bool = ...) -> None: ...

class RmHostClusterRequest(_message.Message):
    __slots__ = ("removeallhosts", "keepmappings", "removemappings", "force")
    REMOVEALLHOSTS_FIELD_NUMBER: _ClassVar[int]
    KEEPMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    REMOVEMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    removeallhosts: bool
    keepmappings: bool
    removemappings: bool
    force: bool
    def __init__(self, removeallhosts: bool = ..., keepmappings: bool = ..., removemappings: bool = ..., force: bool = ...) -> None: ...

class LsHostClusterRequest(_message.Message):
    __slots__ = ("filtervalue",)
    FILTERVALUE_FIELD_NUMBER: _ClassVar[int]
    filtervalue: str
    def __init__(self, filtervalue: _Optional[str] = ...) -> None: ...

class LsHostClusterResponse(_message.Message):
    __slots__ = ("id", "name", "status", "host_count", "mapping_count", "port_count", "protocol")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAPPING_COUNT_FIELD_NUMBER: _ClassVar[int]
    PORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: str
    host_count: str
    mapping_count: str
    port_count: str
    protocol: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., host_count: _Optional[str] = ..., mapping_count: _Optional[str] = ..., port_count: _Optional[str] = ..., protocol: _Optional[str] = ...) -> None: ...

class MkHostClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MkHostClusterResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class LsTargetPortFcResponse(_message.Message):
    __slots__ = ("target_fc_ports_vec",)
    class TargetPortFc(_message.Message):
        __slots__ = ("id", "wwpn", "wwnn", "port_id", "owning_node_id", "current_node_id", "nportid", "host_io_permitted", "virtualized", "protocol", "fc_io_port_id", "portset_count", "host_count", "active_login_count")
        ID_FIELD_NUMBER: _ClassVar[int]
        WWPN_FIELD_NUMBER: _ClassVar[int]
        WWNN_FIELD_NUMBER: _ClassVar[int]
        PORT_ID_FIELD_NUMBER: _ClassVar[int]
        OWNING_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        CURRENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NPORTID_FIELD_NUMBER: _ClassVar[int]
        HOST_IO_PERMITTED_FIELD_NUMBER: _ClassVar[int]
        VIRTUALIZED_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        FC_IO_PORT_ID_FIELD_NUMBER: _ClassVar[int]
        PORTSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        HOST_COUNT_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_LOGIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        wwpn: str
        wwnn: str
        port_id: str
        owning_node_id: str
        current_node_id: str
        nportid: str
        host_io_permitted: str
        virtualized: str
        protocol: str
        fc_io_port_id: str
        portset_count: str
        host_count: str
        active_login_count: str
        def __init__(self, id: _Optional[str] = ..., wwpn: _Optional[str] = ..., wwnn: _Optional[str] = ..., port_id: _Optional[str] = ..., owning_node_id: _Optional[str] = ..., current_node_id: _Optional[str] = ..., nportid: _Optional[str] = ..., host_io_permitted: _Optional[str] = ..., virtualized: _Optional[str] = ..., protocol: _Optional[str] = ..., fc_io_port_id: _Optional[str] = ..., portset_count: _Optional[str] = ..., host_count: _Optional[str] = ..., active_login_count: _Optional[str] = ...) -> None: ...
    TARGET_FC_PORTS_VEC_FIELD_NUMBER: _ClassVar[int]
    target_fc_ports_vec: _containers.RepeatedCompositeFieldContainer[LsTargetPortFcResponse.TargetPortFc]
    def __init__(self, target_fc_ports_vec: _Optional[_Iterable[_Union[LsTargetPortFcResponse.TargetPortFc, _Mapping]]] = ...) -> None: ...
