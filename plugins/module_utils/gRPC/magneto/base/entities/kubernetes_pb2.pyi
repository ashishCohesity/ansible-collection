from magneto.base import common_pb2 as _common_pb2
from magneto.connectors.kubernetes import kubernetes_api_pb2 as _kubernetes_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kIPV4: _ClassVar[IPFamily]
    kIPV6: _ClassVar[IPFamily]

class IPFamilyPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSingleStack: _ClassVar[IPFamilyPolicy]
    kDualStack: _ClassVar[IPFamilyPolicy]

class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterIp: _ClassVar[ServiceType]
    kNodePort: _ClassVar[ServiceType]
    kLoadBalancer: _ClassVar[ServiceType]
kIPV4: IPFamily
kIPV6: IPFamily
kSingleStack: IPFamilyPolicy
kDualStack: IPFamilyPolicy
kClusterIp: ServiceType
kNodePort: ServiceType
kLoadBalancer: ServiceType

class LabelAttributesInfo(_message.Message):
    __slots__ = ("entity_id", "uuid", "name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class IPMode(_message.Message):
    __slots__ = ("ip_family_policy", "preferred_ip_family")
    IP_FAMILY_POLICY_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_IP_FAMILY_FIELD_NUMBER: _ClassVar[int]
    ip_family_policy: IPFamilyPolicy
    preferred_ip_family: IPFamily
    def __init__(self, ip_family_policy: _Optional[_Union[IPFamilyPolicy, str]] = ..., preferred_ip_family: _Optional[_Union[IPFamily, str]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "description", "version", "label_attributes_vec", "namespace", "services_to_connector_ids_map", "pvc_name", "datamover_image_location", "velero_image_location", "velero_aws_plugin_image_location", "init_container_image_location", "velero_openshift_plugin_image_location", "distribution", "velero_version", "velero_upgradability", "datamover_agent_version", "datamover_upgradability", "datamover_service_type", "default_vlan_params", "vlan_info_vec", "service_annotations", "tolerations_vec", "ip_mode", "storage_class_vec", "label_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kNamespace: _ClassVar[Entity.Type]
        kService: _ClassVar[Entity.Type]
        kPVC: _ClassVar[Entity.Type]
        kLabel: _ClassVar[Entity.Type]
        kPersistentVolume: _ClassVar[Entity.Type]
        kPersistentVolumeClaim: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kNamespace: Entity.Type
    kService: Entity.Type
    kPVC: Entity.Type
    kLabel: Entity.Type
    kPersistentVolume: Entity.Type
    kPersistentVolumeClaim: Entity.Type
    class Distribution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMainline: _ClassVar[Entity.Distribution]
        kOpenshift: _ClassVar[Entity.Distribution]
        kRancher: _ClassVar[Entity.Distribution]
        kEKS: _ClassVar[Entity.Distribution]
        kGKE: _ClassVar[Entity.Distribution]
        kAKS: _ClassVar[Entity.Distribution]
        kVMwareTanzu: _ClassVar[Entity.Distribution]
    kMainline: Entity.Distribution
    kOpenshift: Entity.Distribution
    kRancher: Entity.Distribution
    kEKS: Entity.Distribution
    kGKE: Entity.Distribution
    kAKS: Entity.Distribution
    kVMwareTanzu: Entity.Distribution
    class ServicesToConnectorIdsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ServiceAnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class StorageClassInfo(_message.Message):
        __slots__ = ("name", "provisioner")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROVISIONER_FIELD_NUMBER: _ClassVar[int]
        name: str
        provisioner: str
        def __init__(self, name: _Optional[str] = ..., provisioner: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LABEL_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_TO_CONNECTOR_IDS_MAP_FIELD_NUMBER: _ClassVar[int]
    PVC_NAME_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_AWS_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INIT_CONTAINER_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VELERO_OPENSHIFT_PLUGIN_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    VELERO_VERSION_FIELD_NUMBER: _ClassVar[int]
    VELERO_UPGRADABILITY_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_UPGRADABILITY_FIELD_NUMBER: _ClassVar[int]
    DATAMOVER_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    IP_MODE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_VEC_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    description: str
    version: str
    label_attributes_vec: _containers.RepeatedCompositeFieldContainer[LabelAttributesInfo]
    namespace: str
    services_to_connector_ids_map: _containers.ScalarMap[str, int]
    pvc_name: str
    datamover_image_location: str
    velero_image_location: str
    velero_aws_plugin_image_location: str
    init_container_image_location: str
    velero_openshift_plugin_image_location: str
    distribution: Entity.Distribution
    velero_version: str
    velero_upgradability: _common_pb2.Upgradability.State
    datamover_agent_version: str
    datamover_upgradability: _common_pb2.Upgradability.State
    datamover_service_type: ServiceType
    default_vlan_params: _common_pb2.VlanParams
    vlan_info_vec: _containers.RepeatedCompositeFieldContainer[VlanInfo]
    service_annotations: _containers.ScalarMap[str, str]
    tolerations_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration]
    ip_mode: IPMode
    storage_class_vec: _containers.RepeatedCompositeFieldContainer[Entity.StorageClassInfo]
    label_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., label_attributes_vec: _Optional[_Iterable[_Union[LabelAttributesInfo, _Mapping]]] = ..., namespace: _Optional[str] = ..., services_to_connector_ids_map: _Optional[_Mapping[str, int]] = ..., pvc_name: _Optional[str] = ..., datamover_image_location: _Optional[str] = ..., velero_image_location: _Optional[str] = ..., velero_aws_plugin_image_location: _Optional[str] = ..., init_container_image_location: _Optional[str] = ..., velero_openshift_plugin_image_location: _Optional[str] = ..., distribution: _Optional[_Union[Entity.Distribution, str]] = ..., velero_version: _Optional[str] = ..., velero_upgradability: _Optional[_Union[_common_pb2.Upgradability.State, str]] = ..., datamover_agent_version: _Optional[str] = ..., datamover_upgradability: _Optional[_Union[_common_pb2.Upgradability.State, str]] = ..., datamover_service_type: _Optional[_Union[ServiceType, str]] = ..., default_vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., vlan_info_vec: _Optional[_Iterable[_Union[VlanInfo, _Mapping]]] = ..., service_annotations: _Optional[_Mapping[str, str]] = ..., tolerations_vec: _Optional[_Iterable[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.Toleration, _Mapping]]] = ..., ip_mode: _Optional[_Union[IPMode, _Mapping]] = ..., storage_class_vec: _Optional[_Iterable[_Union[Entity.StorageClassInfo, _Mapping]]] = ..., label_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class PodMetadata(_message.Message):
    __slots__ = ("name", "uid", "node_name", "volume_vec")
    class VolumeInfo(_message.Message):
        __slots__ = ("volume", "pv_name", "volume_path", "storage_class")
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        PV_NAME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
        STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
        volume: _kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo
        pv_name: str
        volume_path: str
        storage_class: str
        def __init__(self, volume: _Optional[_Union[_kubernetes_api_pb2.PodInfo.PodSpec.VolumeInfo, _Mapping]] = ..., pv_name: _Optional[str] = ..., volume_path: _Optional[str] = ..., storage_class: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    node_name: str
    volume_vec: _containers.RepeatedCompositeFieldContainer[PodMetadata.VolumeInfo]
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., node_name: _Optional[str] = ..., volume_vec: _Optional[_Iterable[_Union[PodMetadata.VolumeInfo, _Mapping]]] = ...) -> None: ...

class VlanInfo(_message.Message):
    __slots__ = ("vlan_params", "service_annotations")
    class ServiceAnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    vlan_params: _common_pb2.VlanParams
    service_annotations: _containers.ScalarMap[str, str]
    def __init__(self, vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., service_annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...
