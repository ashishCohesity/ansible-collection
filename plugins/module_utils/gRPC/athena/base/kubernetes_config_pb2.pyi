from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KubernetesConfigProto(_message.Message):
    __slots__ = ("cluster_status", "etcd_member_vec", "etcd_cluster_token", "etcd_cluster_size", "kubernetes_cluster_service_ip_range", "kubernetes_cluster_service_ip6_range", "kubernetes_cluster_ip", "kubernetes_cluster_ip6", "kubernetes_cluster_dns_ip", "kubernetes_cluster_dns_ip6", "kubernetes_cluster_pod_ip_range", "kubernetes_cluster_pod_ip6_range", "kubernetes_cluster_system_services_ip_range", "kubernetes_cluster_system_services_ip6_range", "enable_kubernetes_cluster_system_services_ip_range", "kubernetes_cluster_axon_cni_apps_ip_range", "kubernetes_cluster_axon_cni_apps_ip6_range", "kubernetes_cluster_axon_cni_system_services_ip_range", "kubernetes_cluster_axon_cni_system_services_ip6_range", "kubernetes_cluster_axon_cni_k8s_system_pods_ip_range", "kubernetes_cluster_axon_cni_k8s_system_pods_ip6_range", "incarnation_id", "vm_ip", "vm_host_ip", "registry_images_version", "root_ca_key_data", "root_ca_data", "quarantined_node_list", "unquarantined_node_list", "has_cleaned_up_default_token_pods")
    class ClusterStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInitializing: _ClassVar[KubernetesConfigProto.ClusterStatus]
        kOperational: _ClassVar[KubernetesConfigProto.ClusterStatus]
    kInitializing: KubernetesConfigProto.ClusterStatus
    kOperational: KubernetesConfigProto.ClusterStatus
    class Constituent(_message.Message):
        __slots__ = ("id", "node_id", "peer_url", "client_url")
        ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        PEER_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_URL_FIELD_NUMBER: _ClassVar[int]
        id: int
        node_id: int
        peer_url: str
        client_url: str
        def __init__(self, id: _Optional[int] = ..., node_id: _Optional[int] = ..., peer_url: _Optional[str] = ..., client_url: _Optional[str] = ...) -> None: ...
    CLUSTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ETCD_MEMBER_VEC_FIELD_NUMBER: _ClassVar[int]
    ETCD_CLUSTER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ETCD_CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_SERVICE_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_SERVICE_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_IP6_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_DNS_IP_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_DNS_IP6_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_POD_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_POD_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_SYSTEM_SERVICES_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_SYSTEM_SERVICES_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_KUBERNETES_CLUSTER_SYSTEM_SERVICES_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_APPS_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_APPS_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_SYSTEM_SERVICES_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_SYSTEM_SERVICES_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_K8S_SYSTEM_PODS_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_AXON_CNI_K8S_SYSTEM_PODS_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    VM_IP_FIELD_NUMBER: _ClassVar[int]
    VM_HOST_IP_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_IMAGES_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROOT_CA_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    ROOT_CA_DATA_FIELD_NUMBER: _ClassVar[int]
    QUARANTINED_NODE_LIST_FIELD_NUMBER: _ClassVar[int]
    UNQUARANTINED_NODE_LIST_FIELD_NUMBER: _ClassVar[int]
    HAS_CLEANED_UP_DEFAULT_TOKEN_PODS_FIELD_NUMBER: _ClassVar[int]
    cluster_status: KubernetesConfigProto.ClusterStatus
    etcd_member_vec: _containers.RepeatedCompositeFieldContainer[KubernetesConfigProto.Constituent]
    etcd_cluster_token: str
    etcd_cluster_size: int
    kubernetes_cluster_service_ip_range: str
    kubernetes_cluster_service_ip6_range: str
    kubernetes_cluster_ip: str
    kubernetes_cluster_ip6: str
    kubernetes_cluster_dns_ip: str
    kubernetes_cluster_dns_ip6: str
    kubernetes_cluster_pod_ip_range: str
    kubernetes_cluster_pod_ip6_range: str
    kubernetes_cluster_system_services_ip_range: str
    kubernetes_cluster_system_services_ip6_range: str
    enable_kubernetes_cluster_system_services_ip_range: bool
    kubernetes_cluster_axon_cni_apps_ip_range: str
    kubernetes_cluster_axon_cni_apps_ip6_range: str
    kubernetes_cluster_axon_cni_system_services_ip_range: str
    kubernetes_cluster_axon_cni_system_services_ip6_range: str
    kubernetes_cluster_axon_cni_k8s_system_pods_ip_range: str
    kubernetes_cluster_axon_cni_k8s_system_pods_ip6_range: str
    incarnation_id: int
    vm_ip: str
    vm_host_ip: str
    registry_images_version: int
    root_ca_key_data: str
    root_ca_data: str
    quarantined_node_list: _containers.RepeatedScalarFieldContainer[int]
    unquarantined_node_list: _containers.RepeatedScalarFieldContainer[int]
    has_cleaned_up_default_token_pods: bool
    def __init__(self, cluster_status: _Optional[_Union[KubernetesConfigProto.ClusterStatus, str]] = ..., etcd_member_vec: _Optional[_Iterable[_Union[KubernetesConfigProto.Constituent, _Mapping]]] = ..., etcd_cluster_token: _Optional[str] = ..., etcd_cluster_size: _Optional[int] = ..., kubernetes_cluster_service_ip_range: _Optional[str] = ..., kubernetes_cluster_service_ip6_range: _Optional[str] = ..., kubernetes_cluster_ip: _Optional[str] = ..., kubernetes_cluster_ip6: _Optional[str] = ..., kubernetes_cluster_dns_ip: _Optional[str] = ..., kubernetes_cluster_dns_ip6: _Optional[str] = ..., kubernetes_cluster_pod_ip_range: _Optional[str] = ..., kubernetes_cluster_pod_ip6_range: _Optional[str] = ..., kubernetes_cluster_system_services_ip_range: _Optional[str] = ..., kubernetes_cluster_system_services_ip6_range: _Optional[str] = ..., enable_kubernetes_cluster_system_services_ip_range: bool = ..., kubernetes_cluster_axon_cni_apps_ip_range: _Optional[str] = ..., kubernetes_cluster_axon_cni_apps_ip6_range: _Optional[str] = ..., kubernetes_cluster_axon_cni_system_services_ip_range: _Optional[str] = ..., kubernetes_cluster_axon_cni_system_services_ip6_range: _Optional[str] = ..., kubernetes_cluster_axon_cni_k8s_system_pods_ip_range: _Optional[str] = ..., kubernetes_cluster_axon_cni_k8s_system_pods_ip6_range: _Optional[str] = ..., incarnation_id: _Optional[int] = ..., vm_ip: _Optional[str] = ..., vm_host_ip: _Optional[str] = ..., registry_images_version: _Optional[int] = ..., root_ca_key_data: _Optional[str] = ..., root_ca_data: _Optional[str] = ..., quarantined_node_list: _Optional[_Iterable[int]] = ..., unquarantined_node_list: _Optional[_Iterable[int]] = ..., has_cleaned_up_default_token_pods: bool = ...) -> None: ...
