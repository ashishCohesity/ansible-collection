from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceUpgradeScriptsProto(_message.Message):
    __slots__ = ("upgrade_scripts_dirpath", "upgrade_scripts_vec")
    class UpgradeStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAfterNodeUpgradeBeforeServiceStartStage: _ClassVar[ServiceUpgradeScriptsProto.UpgradeStage]
        kAfterNodeUpgradeAfterServiceStartStage: _ClassVar[ServiceUpgradeScriptsProto.UpgradeStage]
        kBeforeClusterUpgradeStage: _ClassVar[ServiceUpgradeScriptsProto.UpgradeStage]
        kAfterClusterUpgradeStage: _ClassVar[ServiceUpgradeScriptsProto.UpgradeStage]
    kAfterNodeUpgradeBeforeServiceStartStage: ServiceUpgradeScriptsProto.UpgradeStage
    kAfterNodeUpgradeAfterServiceStartStage: ServiceUpgradeScriptsProto.UpgradeStage
    kBeforeClusterUpgradeStage: ServiceUpgradeScriptsProto.UpgradeStage
    kAfterClusterUpgradeStage: ServiceUpgradeScriptsProto.UpgradeStage
    class UpgradeScript(_message.Message):
        __slots__ = ("file_name", "upgrade_stage", "version_constraint", "timeout_secs", "service_type")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_STAGE_FIELD_NUMBER: _ClassVar[int]
        VERSION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        upgrade_stage: ServiceUpgradeScriptsProto.UpgradeStage
        version_constraint: str
        timeout_secs: int
        service_type: _cluster_config_pb2.ClusterConfigProto.Bulletin.ServiceName
        def __init__(self, file_name: _Optional[str] = ..., upgrade_stage: _Optional[_Union[ServiceUpgradeScriptsProto.UpgradeStage, str]] = ..., version_constraint: _Optional[str] = ..., timeout_secs: _Optional[int] = ..., service_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Bulletin.ServiceName, str]] = ...) -> None: ...
    UPGRADE_SCRIPTS_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SCRIPTS_VEC_FIELD_NUMBER: _ClassVar[int]
    upgrade_scripts_dirpath: str
    upgrade_scripts_vec: _containers.RepeatedCompositeFieldContainer[ServiceUpgradeScriptsProto.UpgradeScript]
    def __init__(self, upgrade_scripts_dirpath: _Optional[str] = ..., upgrade_scripts_vec: _Optional[_Iterable[_Union[ServiceUpgradeScriptsProto.UpgradeScript, _Mapping]]] = ...) -> None: ...
