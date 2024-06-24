from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectMeta(_message.Message):
    __slots__ = ("name", "namespace", "uid", "annotations", "labels")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    uid: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., uid: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ObjectStatus(_message.Message):
    __slots__ = ("phase", "container_statuses")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_STATUSES_FIELD_NUMBER: _ClassVar[int]
    phase: str
    container_statuses: _containers.RepeatedCompositeFieldContainer[ContainerStatus]
    def __init__(self, phase: _Optional[str] = ..., container_statuses: _Optional[_Iterable[_Union[ContainerStatus, _Mapping]]] = ...) -> None: ...

class ObjectReference(_message.Message):
    __slots__ = ("kind", "api_version", "name", "namespace", "resource_version", "uid", "api_group")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    API_GROUP_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    name: str
    namespace: str
    resource_version: str
    uid: str
    api_group: str
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., resource_version: _Optional[str] = ..., uid: _Optional[str] = ..., api_group: _Optional[str] = ...) -> None: ...

class LabelSelector(_message.Message):
    __slots__ = ("match_labels", "name", "service_name")
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.ScalarMap[str, str]
    name: str
    service_name: str
    def __init__(self, match_labels: _Optional[_Mapping[str, str]] = ..., name: _Optional[str] = ..., service_name: _Optional[str] = ...) -> None: ...

class ServicePort(_message.Message):
    __slots__ = ("protocol", "port", "target_port", "node_port")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    port: int
    target_port: int
    node_port: int
    def __init__(self, protocol: _Optional[str] = ..., port: _Optional[int] = ..., target_port: _Optional[int] = ..., node_port: _Optional[int] = ...) -> None: ...

class ServiceSpec(_message.Message):
    __slots__ = ("type", "ports", "selector", "ip_family_policy")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    IP_FAMILY_POLICY_FIELD_NUMBER: _ClassVar[int]
    type: str
    ports: _containers.RepeatedCompositeFieldContainer[ServicePort]
    selector: LabelSelector
    ip_family_policy: str
    def __init__(self, type: _Optional[str] = ..., ports: _Optional[_Iterable[_Union[ServicePort, _Mapping]]] = ..., selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., ip_family_policy: _Optional[str] = ...) -> None: ...

class ResourceRequirements(_message.Message):
    __slots__ = ("limits", "requests")
    class LimitsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RequestsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    limits: _containers.ScalarMap[str, str]
    requests: _containers.ScalarMap[str, str]
    def __init__(self, limits: _Optional[_Mapping[str, str]] = ..., requests: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ("name", "image", "ports", "volume_mounts", "security_context", "command", "image_pull_policy", "resources", "liveness_probe", "env", "args")
    class ContainerPort(_message.Message):
        __slots__ = ("container_port", "protocol")
        CONTAINER_PORT_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        container_port: int
        protocol: str
        def __init__(self, container_port: _Optional[int] = ..., protocol: _Optional[str] = ...) -> None: ...
    class VolumeMount(_message.Message):
        __slots__ = ("mount_path", "name", "mount_propagation", "read_only")
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PROPAGATION_FIELD_NUMBER: _ClassVar[int]
        READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        mount_path: str
        name: str
        mount_propagation: str
        read_only: bool
        def __init__(self, mount_path: _Optional[str] = ..., name: _Optional[str] = ..., mount_propagation: _Optional[str] = ..., read_only: bool = ...) -> None: ...
    class SecurityContext(_message.Message):
        __slots__ = ("privileged",)
        PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
        privileged: bool
        def __init__(self, privileged: bool = ...) -> None: ...
    class EnvVar(_message.Message):
        __slots__ = ("name", "value", "value_from")
        class EnvVarSource(_message.Message):
            __slots__ = ("field_ref",)
            FIELD_REF_FIELD_NUMBER: _ClassVar[int]
            field_ref: ObjectFieldSelector
            def __init__(self, field_ref: _Optional[_Union[ObjectFieldSelector, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FROM_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        value_from: Container.EnvVar.EnvVarSource
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., value_from: _Optional[_Union[Container.EnvVar.EnvVarSource, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PULL_POLICY_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: str
    ports: _containers.RepeatedCompositeFieldContainer[Container.ContainerPort]
    volume_mounts: _containers.RepeatedCompositeFieldContainer[Container.VolumeMount]
    security_context: Container.SecurityContext
    command: _containers.RepeatedScalarFieldContainer[str]
    image_pull_policy: str
    resources: ResourceRequirements
    liveness_probe: Probe
    env: _containers.RepeatedCompositeFieldContainer[Container.EnvVar]
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., image: _Optional[str] = ..., ports: _Optional[_Iterable[_Union[Container.ContainerPort, _Mapping]]] = ..., volume_mounts: _Optional[_Iterable[_Union[Container.VolumeMount, _Mapping]]] = ..., security_context: _Optional[_Union[Container.SecurityContext, _Mapping]] = ..., command: _Optional[_Iterable[str]] = ..., image_pull_policy: _Optional[str] = ..., resources: _Optional[_Union[ResourceRequirements, _Mapping]] = ..., liveness_probe: _Optional[_Union[Probe, _Mapping]] = ..., env: _Optional[_Iterable[_Union[Container.EnvVar, _Mapping]]] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class DaemonSet(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    class DaemonSetSpec(_message.Message):
        __slots__ = ("selector", "template")
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        selector: LabelSelector
        template: PodInfo
        def __init__(self, selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., template: _Optional[_Union[PodInfo, _Mapping]] = ...) -> None: ...
    class DaemonSetStatus(_message.Message):
        __slots__ = ("desired_number_scheduled", "number_ready")
        DESIRED_NUMBER_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        NUMBER_READY_FIELD_NUMBER: _ClassVar[int]
        desired_number_scheduled: int
        number_ready: int
        def __init__(self, desired_number_scheduled: _Optional[int] = ..., number_ready: _Optional[int] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: DaemonSet.DaemonSetSpec
    status: DaemonSet.DaemonSetStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[DaemonSet.DaemonSetSpec, _Mapping]] = ..., status: _Optional[_Union[DaemonSet.DaemonSetStatus, _Mapping]] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("metadata", "status", "spec")
    class NodeStatus(_message.Message):
        __slots__ = ("addresses", "conditions")
        class NodeAddress(_message.Message):
            __slots__ = ("address", "type")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            address: str
            type: str
            def __init__(self, address: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
        class NodeCondition(_message.Message):
            __slots__ = ("type", "status")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            type: str
            status: str
            def __init__(self, type: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...
        ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        addresses: _containers.RepeatedCompositeFieldContainer[NodeInfo.NodeStatus.NodeAddress]
        conditions: _containers.RepeatedCompositeFieldContainer[NodeInfo.NodeStatus.NodeCondition]
        def __init__(self, addresses: _Optional[_Iterable[_Union[NodeInfo.NodeStatus.NodeAddress, _Mapping]]] = ..., conditions: _Optional[_Iterable[_Union[NodeInfo.NodeStatus.NodeCondition, _Mapping]]] = ...) -> None: ...
    class NodeSpec(_message.Message):
        __slots__ = ("unschedulable", "taints", "podCIDR", "podCIDRs")
        class Taint(_message.Message):
            __slots__ = ("key", "value", "effect")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            EFFECT_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            effect: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[str] = ...) -> None: ...
        UNSCHEDULABLE_FIELD_NUMBER: _ClassVar[int]
        TAINTS_FIELD_NUMBER: _ClassVar[int]
        PODCIDR_FIELD_NUMBER: _ClassVar[int]
        PODCIDRS_FIELD_NUMBER: _ClassVar[int]
        unschedulable: bool
        taints: _containers.RepeatedCompositeFieldContainer[NodeInfo.NodeSpec.Taint]
        podCIDR: str
        podCIDRs: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, unschedulable: bool = ..., taints: _Optional[_Iterable[_Union[NodeInfo.NodeSpec.Taint, _Mapping]]] = ..., podCIDR: _Optional[str] = ..., podCIDRs: _Optional[_Iterable[str]] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMeta
    status: NodeInfo.NodeStatus
    spec: NodeInfo.NodeSpec
    def __init__(self, metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., status: _Optional[_Union[NodeInfo.NodeStatus, _Mapping]] = ..., spec: _Optional[_Union[NodeInfo.NodeSpec, _Mapping]] = ...) -> None: ...

class NodeList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ...) -> None: ...

class DaemonSetList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DaemonSet]
    def __init__(self, items: _Optional[_Iterable[_Union[DaemonSet, _Mapping]]] = ...) -> None: ...

class JobInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec")
    class JobSpec(_message.Message):
        __slots__ = ("template",)
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        template: PodInfo
        def __init__(self, template: _Optional[_Union[PodInfo, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: JobInfo.JobSpec
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[JobInfo.JobSpec, _Mapping]] = ...) -> None: ...

class JobList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[JobInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[JobInfo, _Mapping]]] = ...) -> None: ...

class NamespaceInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "status", "spec")
    class NamespaceStatus(_message.Message):
        __slots__ = ("phase",)
        PHASE_FIELD_NUMBER: _ClassVar[int]
        phase: str
        def __init__(self, phase: _Optional[str] = ...) -> None: ...
    class NamespaceSpec(_message.Message):
        __slots__ = ("finalizers",)
        FINALIZERS_FIELD_NUMBER: _ClassVar[int]
        finalizers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, finalizers: _Optional[_Iterable[str]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    status: NamespaceInfo.NamespaceStatus
    spec: NamespaceInfo.NamespaceSpec
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., status: _Optional[_Union[NamespaceInfo.NamespaceStatus, _Mapping]] = ..., spec: _Optional[_Union[NamespaceInfo.NamespaceSpec, _Mapping]] = ...) -> None: ...

class NamespaceList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NamespaceInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[NamespaceInfo, _Mapping]]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ("major_version", "minor_version", "git_version")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    GIT_VERSION_FIELD_NUMBER: _ClassVar[int]
    major_version: str
    minor_version: str
    git_version: str
    def __init__(self, major_version: _Optional[str] = ..., minor_version: _Optional[str] = ..., git_version: _Optional[str] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[ServiceSpec, _Mapping]] = ..., status: _Optional[_Union[ServiceStatus, _Mapping]] = ...) -> None: ...

class ServiceStatus(_message.Message):
    __slots__ = ("loadBalancer",)
    LOADBALANCER_FIELD_NUMBER: _ClassVar[int]
    loadBalancer: LoadBalancerStatus
    def __init__(self, loadBalancer: _Optional[_Union[LoadBalancerStatus, _Mapping]] = ...) -> None: ...

class LoadBalancerStatus(_message.Message):
    __slots__ = ("ingress",)
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    ingress: _containers.RepeatedCompositeFieldContainer[LoadBalancerIngress]
    def __init__(self, ingress: _Optional[_Iterable[_Union[LoadBalancerIngress, _Mapping]]] = ...) -> None: ...

class LoadBalancerIngress(_message.Message):
    __slots__ = ("ip", "hostname", "ports")
    IP_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ip: str
    hostname: str
    ports: _containers.RepeatedCompositeFieldContainer[PortStatus]
    def __init__(self, ip: _Optional[str] = ..., hostname: _Optional[str] = ..., ports: _Optional[_Iterable[_Union[PortStatus, _Mapping]]] = ...) -> None: ...

class PortStatus(_message.Message):
    __slots__ = ("port", "protocol", "error")
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    port: int
    protocol: str
    error: str
    def __init__(self, port: _Optional[int] = ..., protocol: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ServiceList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Service]
    def __init__(self, items: _Optional[_Iterable[_Union[Service, _Mapping]]] = ...) -> None: ...

class DeleteStatus(_message.Message):
    __slots__ = ("status", "kind", "api_version", "metadata")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    kind: str
    api_version: str
    metadata: ObjectMeta
    def __init__(self, status: _Optional[str] = ..., kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ...) -> None: ...

class PodAffinityTerm(_message.Message):
    __slots__ = ("labelSelector", "namespaces", "topologyKey", "namespaceSelector")
    LABELSELECTOR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGYKEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACESELECTOR_FIELD_NUMBER: _ClassVar[int]
    labelSelector: LabelSelector
    namespaces: _containers.RepeatedScalarFieldContainer[str]
    topologyKey: str
    namespaceSelector: LabelSelector
    def __init__(self, labelSelector: _Optional[_Union[LabelSelector, _Mapping]] = ..., namespaces: _Optional[_Iterable[str]] = ..., topologyKey: _Optional[str] = ..., namespaceSelector: _Optional[_Union[LabelSelector, _Mapping]] = ...) -> None: ...

class WeightedPodAffinityTerm(_message.Message):
    __slots__ = ("weight", "podAffinityTerm")
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    PODAFFINITYTERM_FIELD_NUMBER: _ClassVar[int]
    weight: int
    podAffinityTerm: PodAffinityTerm
    def __init__(self, weight: _Optional[int] = ..., podAffinityTerm: _Optional[_Union[PodAffinityTerm, _Mapping]] = ...) -> None: ...

class PodAntiAffinity(_message.Message):
    __slots__ = ("requiredDuringSchedulingIgnoredDuringExecution", "preferredDuringSchedulingIgnoredDuringExecution")
    REQUIREDDURINGSCHEDULINGIGNOREDDURINGEXECUTION_FIELD_NUMBER: _ClassVar[int]
    PREFERREDDURINGSCHEDULINGIGNOREDDURINGEXECUTION_FIELD_NUMBER: _ClassVar[int]
    requiredDuringSchedulingIgnoredDuringExecution: _containers.RepeatedCompositeFieldContainer[PodAffinityTerm]
    preferredDuringSchedulingIgnoredDuringExecution: _containers.RepeatedCompositeFieldContainer[WeightedPodAffinityTerm]
    def __init__(self, requiredDuringSchedulingIgnoredDuringExecution: _Optional[_Iterable[_Union[PodAffinityTerm, _Mapping]]] = ..., preferredDuringSchedulingIgnoredDuringExecution: _Optional[_Iterable[_Union[WeightedPodAffinityTerm, _Mapping]]] = ...) -> None: ...

class Affinity(_message.Message):
    __slots__ = ("podAntiAffinity",)
    PODANTIAFFINITY_FIELD_NUMBER: _ClassVar[int]
    podAntiAffinity: PodAntiAffinity
    def __init__(self, podAntiAffinity: _Optional[_Union[PodAntiAffinity, _Mapping]] = ...) -> None: ...

class ObjectFieldSelector(_message.Message):
    __slots__ = ("api_version", "field_path")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    field_path: str
    def __init__(self, api_version: _Optional[str] = ..., field_path: _Optional[str] = ...) -> None: ...

class PodInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "name", "spec", "status")
    class PodSpec(_message.Message):
        __slots__ = ("volumes", "node_name", "containers", "security_context", "restart_policy", "service_account_name", "tolerations", "affinity")
        class VolumeInfo(_message.Message):
            __slots__ = ("name", "aws_elastic_block_store", "azure_disk", "azure_file", "cephfs", "cinder", "config_map", "empty_dir", "fc", "flocker", "gce_persistent_disk", "glusterfs", "iscsi", "local", "persistent_volume_claim", "nfs", "csi", "downward_api", "ephemeral", "photon_persistent_disk", "portworx_volume", "projected", "quobyte", "rbd", "scale_io", "secret", "storageos", "vsphere_volume", "flex_volume", "secret_volume", "host_path")
            class KeyToPath(_message.Message):
                __slots__ = ("key", "mode", "path")
                KEY_FIELD_NUMBER: _ClassVar[int]
                MODE_FIELD_NUMBER: _ClassVar[int]
                PATH_FIELD_NUMBER: _ClassVar[int]
                key: str
                mode: int
                path: str
                def __init__(self, key: _Optional[str] = ..., mode: _Optional[int] = ..., path: _Optional[str] = ...) -> None: ...
            class AWS_EBS(_message.Message):
                __slots__ = ("volume_id", "fs_type")
                VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                volume_id: str
                fs_type: str
                def __init__(self, volume_id: _Optional[str] = ..., fs_type: _Optional[str] = ...) -> None: ...
            class AzureDisk(_message.Message):
                __slots__ = ("disk_name", "disk_uri")
                DISK_NAME_FIELD_NUMBER: _ClassVar[int]
                DISK_URI_FIELD_NUMBER: _ClassVar[int]
                disk_name: str
                disk_uri: str
                def __init__(self, disk_name: _Optional[str] = ..., disk_uri: _Optional[str] = ...) -> None: ...
            class AzureFile(_message.Message):
                __slots__ = ("secret_name", "share_name", "read_only")
                SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
                SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                secret_name: str
                share_name: str
                read_only: str
                def __init__(self, secret_name: _Optional[str] = ..., share_name: _Optional[str] = ..., read_only: _Optional[str] = ...) -> None: ...
            class Cephfs(_message.Message):
                __slots__ = ("monitors", "user", "secret_file", "read_only")
                MONITORS_FIELD_NUMBER: _ClassVar[int]
                USER_FIELD_NUMBER: _ClassVar[int]
                SECRET_FILE_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                monitors: _containers.RepeatedScalarFieldContainer[str]
                user: str
                secret_file: str
                read_only: str
                def __init__(self, monitors: _Optional[_Iterable[str]] = ..., user: _Optional[str] = ..., secret_file: _Optional[str] = ..., read_only: _Optional[str] = ...) -> None: ...
            class Cinder(_message.Message):
                __slots__ = ("volume_id", "fs_type")
                VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                volume_id: str
                fs_type: str
                def __init__(self, volume_id: _Optional[str] = ..., fs_type: _Optional[str] = ...) -> None: ...
            class ConfigMap(_message.Message):
                __slots__ = ("name",)
                NAME_FIELD_NUMBER: _ClassVar[int]
                name: str
                def __init__(self, name: _Optional[str] = ...) -> None: ...
            class EmptyDir(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class FC(_message.Message):
                __slots__ = ("targetWWNs", "lun", "fs_type")
                TARGETWWNS_FIELD_NUMBER: _ClassVar[int]
                LUN_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                targetWWNs: _containers.RepeatedScalarFieldContainer[str]
                lun: int
                fs_type: str
                def __init__(self, targetWWNs: _Optional[_Iterable[str]] = ..., lun: _Optional[int] = ..., fs_type: _Optional[str] = ...) -> None: ...
            class Flocker(_message.Message):
                __slots__ = ("dataset_name",)
                DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
                dataset_name: str
                def __init__(self, dataset_name: _Optional[str] = ...) -> None: ...
            class GcePersistentDisk(_message.Message):
                __slots__ = ("pd_name", "fs_type")
                PD_NAME_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                pd_name: str
                fs_type: str
                def __init__(self, pd_name: _Optional[str] = ..., fs_type: _Optional[str] = ...) -> None: ...
            class GlusterFs(_message.Message):
                __slots__ = ("endpoints", "path")
                ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
                PATH_FIELD_NUMBER: _ClassVar[int]
                endpoints: str
                path: str
                def __init__(self, endpoints: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...
            class ISCSI(_message.Message):
                __slots__ = ("target_portal", "iqn", "lun")
                TARGET_PORTAL_FIELD_NUMBER: _ClassVar[int]
                IQN_FIELD_NUMBER: _ClassVar[int]
                LUN_FIELD_NUMBER: _ClassVar[int]
                target_portal: str
                iqn: str
                lun: int
                def __init__(self, target_portal: _Optional[str] = ..., iqn: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...
            class Local(_message.Message):
                __slots__ = ("path",)
                PATH_FIELD_NUMBER: _ClassVar[int]
                path: str
                def __init__(self, path: _Optional[str] = ...) -> None: ...
            class PVC(_message.Message):
                __slots__ = ("claim_name", "read_only")
                CLAIM_NAME_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                claim_name: str
                read_only: bool
                def __init__(self, claim_name: _Optional[str] = ..., read_only: bool = ...) -> None: ...
            class NFS(_message.Message):
                __slots__ = ("path", "read_only", "server")
                PATH_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                SERVER_FIELD_NUMBER: _ClassVar[int]
                path: str
                read_only: bool
                server: str
                def __init__(self, path: _Optional[str] = ..., read_only: bool = ..., server: _Optional[str] = ...) -> None: ...
            class CSI(_message.Message):
                __slots__ = ("controller_expand_secret_ref", "controller_publish_secret_ref", "driver", "fs_type", "node_publish_secret_ref", "node_stage_secret_ref", "read_only", "volume_handle", "volume_attributes")
                class VolumeAttributesEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: str
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                CONTROLLER_EXPAND_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                CONTROLLER_PUBLISH_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                DRIVER_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                NODE_PUBLISH_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                NODE_STAGE_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                VOLUME_HANDLE_FIELD_NUMBER: _ClassVar[int]
                VOLUME_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
                controller_expand_secret_ref: ObjectReference
                controller_publish_secret_ref: ObjectReference
                driver: str
                fs_type: str
                node_publish_secret_ref: ObjectReference
                node_stage_secret_ref: ObjectReference
                read_only: bool
                volume_handle: str
                volume_attributes: _containers.ScalarMap[str, str]
                def __init__(self, controller_expand_secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., controller_publish_secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., driver: _Optional[str] = ..., fs_type: _Optional[str] = ..., node_publish_secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., node_stage_secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., read_only: bool = ..., volume_handle: _Optional[str] = ..., volume_attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...
            class DownwardAPIVolumeFile(_message.Message):
                __slots__ = ("mode", "path", "field_ref", "resource_field_ref")
                class ResourceFieldSelector(_message.Message):
                    __slots__ = ("container_name", "resource", "divisor")
                    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
                    RESOURCE_FIELD_NUMBER: _ClassVar[int]
                    DIVISOR_FIELD_NUMBER: _ClassVar[int]
                    container_name: str
                    resource: str
                    divisor: str
                    def __init__(self, container_name: _Optional[str] = ..., resource: _Optional[str] = ..., divisor: _Optional[str] = ...) -> None: ...
                MODE_FIELD_NUMBER: _ClassVar[int]
                PATH_FIELD_NUMBER: _ClassVar[int]
                FIELD_REF_FIELD_NUMBER: _ClassVar[int]
                RESOURCE_FIELD_REF_FIELD_NUMBER: _ClassVar[int]
                mode: int
                path: str
                field_ref: ObjectFieldSelector
                resource_field_ref: PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile.ResourceFieldSelector
                def __init__(self, mode: _Optional[int] = ..., path: _Optional[str] = ..., field_ref: _Optional[_Union[ObjectFieldSelector, _Mapping]] = ..., resource_field_ref: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile.ResourceFieldSelector, _Mapping]] = ...) -> None: ...
            class EphemeralVolumeSource(_message.Message):
                __slots__ = ("read_only", "volumeClaimTemplate")
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                VOLUMECLAIMTEMPLATE_FIELD_NUMBER: _ClassVar[int]
                read_only: bool
                volumeClaimTemplate: PVCInfo
                def __init__(self, read_only: bool = ..., volumeClaimTemplate: _Optional[_Union[PVCInfo, _Mapping]] = ...) -> None: ...
            class DownwardAPI(_message.Message):
                __slots__ = ("default_mode", "items")
                DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
                ITEMS_FIELD_NUMBER: _ClassVar[int]
                default_mode: int
                items: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile]
                def __init__(self, default_mode: _Optional[int] = ..., items: _Optional[_Iterable[_Union[PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile, _Mapping]]] = ...) -> None: ...
            class PhotonPersistentDisk(_message.Message):
                __slots__ = ("fs_type", "pd_id")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                PD_ID_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                pd_id: str
                def __init__(self, fs_type: _Optional[str] = ..., pd_id: _Optional[str] = ...) -> None: ...
            class Portworx(_message.Message):
                __slots__ = ("fs_type", "read_only", "volume_id")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                read_only: bool
                volume_id: str
                def __init__(self, fs_type: _Optional[str] = ..., read_only: bool = ..., volume_id: _Optional[str] = ...) -> None: ...
            class Quobyte(_message.Message):
                __slots__ = ("group", "read_only", "registry", "tenant", "user", "volume")
                GROUP_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                REGISTRY_FIELD_NUMBER: _ClassVar[int]
                TENANT_FIELD_NUMBER: _ClassVar[int]
                USER_FIELD_NUMBER: _ClassVar[int]
                VOLUME_FIELD_NUMBER: _ClassVar[int]
                group: str
                read_only: bool
                registry: str
                tenant: str
                user: str
                volume: str
                def __init__(self, group: _Optional[str] = ..., read_only: bool = ..., registry: _Optional[str] = ..., tenant: _Optional[str] = ..., user: _Optional[str] = ..., volume: _Optional[str] = ...) -> None: ...
            class RBD(_message.Message):
                __slots__ = ("fs_type", "image", "keyring", "monitors", "pool", "read_only", "secret_ref", "user")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                KEYRING_FIELD_NUMBER: _ClassVar[int]
                MONITORS_FIELD_NUMBER: _ClassVar[int]
                POOL_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                USER_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                image: str
                keyring: str
                monitors: _containers.RepeatedScalarFieldContainer[str]
                pool: str
                read_only: bool
                secret_ref: ObjectReference
                user: str
                def __init__(self, fs_type: _Optional[str] = ..., image: _Optional[str] = ..., keyring: _Optional[str] = ..., monitors: _Optional[_Iterable[str]] = ..., pool: _Optional[str] = ..., read_only: bool = ..., secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., user: _Optional[str] = ...) -> None: ...
            class ScaleIO(_message.Message):
                __slots__ = ("fs_type", "gateway", "protection_domain", "read_only", "secret_ref", "ssl_enabled", "storage_mode", "storage_pool", "system", "volume_name")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                GATEWAY_FIELD_NUMBER: _ClassVar[int]
                PROTECTION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                SSL_ENABLED_FIELD_NUMBER: _ClassVar[int]
                STORAGE_MODE_FIELD_NUMBER: _ClassVar[int]
                STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
                SYSTEM_FIELD_NUMBER: _ClassVar[int]
                VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                gateway: str
                protection_domain: str
                read_only: bool
                secret_ref: ObjectReference
                ssl_enabled: bool
                storage_mode: str
                storage_pool: str
                system: str
                volume_name: str
                def __init__(self, fs_type: _Optional[str] = ..., gateway: _Optional[str] = ..., protection_domain: _Optional[str] = ..., read_only: bool = ..., secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., ssl_enabled: bool = ..., storage_mode: _Optional[str] = ..., storage_pool: _Optional[str] = ..., system: _Optional[str] = ..., volume_name: _Optional[str] = ...) -> None: ...
            class StorageOS(_message.Message):
                __slots__ = ("fs_type", "read_only", "secret_ref", "volume_name", "volume_namespace")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
                VOLUME_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                read_only: bool
                secret_ref: ObjectReference
                volume_name: str
                volume_namespace: str
                def __init__(self, fs_type: _Optional[str] = ..., read_only: bool = ..., secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ..., volume_name: _Optional[str] = ..., volume_namespace: _Optional[str] = ...) -> None: ...
            class VsphereVirtualDisk(_message.Message):
                __slots__ = ("fs_type", "storage_policy_i_d", "storage_policy_name", "volume_path")
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                STORAGE_POLICY_I_D_FIELD_NUMBER: _ClassVar[int]
                STORAGE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
                VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
                fs_type: str
                storage_policy_i_d: str
                storage_policy_name: str
                volume_path: str
                def __init__(self, fs_type: _Optional[str] = ..., storage_policy_i_d: _Optional[str] = ..., storage_policy_name: _Optional[str] = ..., volume_path: _Optional[str] = ...) -> None: ...
            class Flex(_message.Message):
                __slots__ = ("driver", "fs_type", "options", "read_only", "secret_ref")
                class OptionsEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: str
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                DRIVER_FIELD_NUMBER: _ClassVar[int]
                FS_TYPE_FIELD_NUMBER: _ClassVar[int]
                OPTIONS_FIELD_NUMBER: _ClassVar[int]
                READ_ONLY_FIELD_NUMBER: _ClassVar[int]
                SECRET_REF_FIELD_NUMBER: _ClassVar[int]
                driver: str
                fs_type: str
                options: _containers.ScalarMap[str, str]
                read_only: bool
                secret_ref: ObjectReference
                def __init__(self, driver: _Optional[str] = ..., fs_type: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ..., read_only: bool = ..., secret_ref: _Optional[_Union[ObjectReference, _Mapping]] = ...) -> None: ...
            class Projected(_message.Message):
                __slots__ = ("default_mode", "sources")
                class VolumeProjection(_message.Message):
                    __slots__ = ("config_map", "downward_api", "secret", "service_account_token")
                    class ConfigMapProjection(_message.Message):
                        __slots__ = ("name", "optional", "items")
                        NAME_FIELD_NUMBER: _ClassVar[int]
                        OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                        ITEMS_FIELD_NUMBER: _ClassVar[int]
                        name: str
                        optional: bool
                        items: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.VolumeInfo.KeyToPath]
                        def __init__(self, name: _Optional[str] = ..., optional: bool = ..., items: _Optional[_Iterable[_Union[PodInfo.PodSpec.VolumeInfo.KeyToPath, _Mapping]]] = ...) -> None: ...
                    class DownwardAPIProjection(_message.Message):
                        __slots__ = ("items",)
                        ITEMS_FIELD_NUMBER: _ClassVar[int]
                        items: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile]
                        def __init__(self, items: _Optional[_Iterable[_Union[PodInfo.PodSpec.VolumeInfo.DownwardAPIVolumeFile, _Mapping]]] = ...) -> None: ...
                    class ServiceAccountTokenProjection(_message.Message):
                        __slots__ = ("audience", "expiration_seconds", "path")
                        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
                        EXPIRATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
                        PATH_FIELD_NUMBER: _ClassVar[int]
                        audience: str
                        expiration_seconds: int
                        path: str
                        def __init__(self, audience: _Optional[str] = ..., expiration_seconds: _Optional[int] = ..., path: _Optional[str] = ...) -> None: ...
                    CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
                    DOWNWARD_API_FIELD_NUMBER: _ClassVar[int]
                    SECRET_FIELD_NUMBER: _ClassVar[int]
                    SERVICE_ACCOUNT_TOKEN_FIELD_NUMBER: _ClassVar[int]
                    config_map: PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ConfigMapProjection
                    downward_api: PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.DownwardAPIProjection
                    secret: PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ConfigMapProjection
                    service_account_token: PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ServiceAccountTokenProjection
                    def __init__(self, config_map: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ConfigMapProjection, _Mapping]] = ..., downward_api: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.DownwardAPIProjection, _Mapping]] = ..., secret: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ConfigMapProjection, _Mapping]] = ..., service_account_token: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection.ServiceAccountTokenProjection, _Mapping]] = ...) -> None: ...
                DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
                SOURCES_FIELD_NUMBER: _ClassVar[int]
                default_mode: int
                sources: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection]
                def __init__(self, default_mode: _Optional[int] = ..., sources: _Optional[_Iterable[_Union[PodInfo.PodSpec.VolumeInfo.Projected.VolumeProjection, _Mapping]]] = ...) -> None: ...
            class HostPath(_message.Message):
                __slots__ = ("path",)
                PATH_FIELD_NUMBER: _ClassVar[int]
                path: str
                def __init__(self, path: _Optional[str] = ...) -> None: ...
            class SecretVolumeSource(_message.Message):
                __slots__ = ("secret_name",)
                SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
                secret_name: str
                def __init__(self, secret_name: _Optional[str] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            AWS_ELASTIC_BLOCK_STORE_FIELD_NUMBER: _ClassVar[int]
            AZURE_DISK_FIELD_NUMBER: _ClassVar[int]
            AZURE_FILE_FIELD_NUMBER: _ClassVar[int]
            CEPHFS_FIELD_NUMBER: _ClassVar[int]
            CINDER_FIELD_NUMBER: _ClassVar[int]
            CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
            EMPTY_DIR_FIELD_NUMBER: _ClassVar[int]
            FC_FIELD_NUMBER: _ClassVar[int]
            FLOCKER_FIELD_NUMBER: _ClassVar[int]
            GCE_PERSISTENT_DISK_FIELD_NUMBER: _ClassVar[int]
            GLUSTERFS_FIELD_NUMBER: _ClassVar[int]
            ISCSI_FIELD_NUMBER: _ClassVar[int]
            LOCAL_FIELD_NUMBER: _ClassVar[int]
            PERSISTENT_VOLUME_CLAIM_FIELD_NUMBER: _ClassVar[int]
            NFS_FIELD_NUMBER: _ClassVar[int]
            CSI_FIELD_NUMBER: _ClassVar[int]
            DOWNWARD_API_FIELD_NUMBER: _ClassVar[int]
            EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
            PHOTON_PERSISTENT_DISK_FIELD_NUMBER: _ClassVar[int]
            PORTWORX_VOLUME_FIELD_NUMBER: _ClassVar[int]
            PROJECTED_FIELD_NUMBER: _ClassVar[int]
            QUOBYTE_FIELD_NUMBER: _ClassVar[int]
            RBD_FIELD_NUMBER: _ClassVar[int]
            SCALE_IO_FIELD_NUMBER: _ClassVar[int]
            SECRET_FIELD_NUMBER: _ClassVar[int]
            STORAGEOS_FIELD_NUMBER: _ClassVar[int]
            VSPHERE_VOLUME_FIELD_NUMBER: _ClassVar[int]
            FLEX_VOLUME_FIELD_NUMBER: _ClassVar[int]
            SECRET_VOLUME_FIELD_NUMBER: _ClassVar[int]
            HOST_PATH_FIELD_NUMBER: _ClassVar[int]
            name: str
            aws_elastic_block_store: PodInfo.PodSpec.VolumeInfo.AWS_EBS
            azure_disk: PodInfo.PodSpec.VolumeInfo.AzureDisk
            azure_file: PodInfo.PodSpec.VolumeInfo.AzureFile
            cephfs: PodInfo.PodSpec.VolumeInfo.Cephfs
            cinder: PodInfo.PodSpec.VolumeInfo.Cinder
            config_map: PodInfo.PodSpec.VolumeInfo.ConfigMap
            empty_dir: PodInfo.PodSpec.VolumeInfo.EmptyDir
            fc: PodInfo.PodSpec.VolumeInfo.FC
            flocker: PodInfo.PodSpec.VolumeInfo.Flocker
            gce_persistent_disk: PodInfo.PodSpec.VolumeInfo.GcePersistentDisk
            glusterfs: PodInfo.PodSpec.VolumeInfo.GlusterFs
            iscsi: PodInfo.PodSpec.VolumeInfo.ISCSI
            local: PodInfo.PodSpec.VolumeInfo.Local
            persistent_volume_claim: PodInfo.PodSpec.VolumeInfo.PVC
            nfs: PodInfo.PodSpec.VolumeInfo.NFS
            csi: PodInfo.PodSpec.VolumeInfo.CSI
            downward_api: PodInfo.PodSpec.VolumeInfo.DownwardAPI
            ephemeral: PodInfo.PodSpec.VolumeInfo.EphemeralVolumeSource
            photon_persistent_disk: PodInfo.PodSpec.VolumeInfo.PhotonPersistentDisk
            portworx_volume: PodInfo.PodSpec.VolumeInfo.Portworx
            projected: PodInfo.PodSpec.VolumeInfo.Projected
            quobyte: PodInfo.PodSpec.VolumeInfo.Quobyte
            rbd: PodInfo.PodSpec.VolumeInfo.RBD
            scale_io: PodInfo.PodSpec.VolumeInfo.ScaleIO
            secret: PodInfo.PodSpec.VolumeInfo.ConfigMap
            storageos: PodInfo.PodSpec.VolumeInfo.StorageOS
            vsphere_volume: PodInfo.PodSpec.VolumeInfo.VsphereVirtualDisk
            flex_volume: PodInfo.PodSpec.VolumeInfo.Flex
            secret_volume: PodInfo.PodSpec.VolumeInfo.SecretVolumeSource
            host_path: PodInfo.PodSpec.VolumeInfo.HostPath
            def __init__(self, name: _Optional[str] = ..., aws_elastic_block_store: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.AWS_EBS, _Mapping]] = ..., azure_disk: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.AzureDisk, _Mapping]] = ..., azure_file: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.AzureFile, _Mapping]] = ..., cephfs: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Cephfs, _Mapping]] = ..., cinder: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Cinder, _Mapping]] = ..., config_map: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.ConfigMap, _Mapping]] = ..., empty_dir: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.EmptyDir, _Mapping]] = ..., fc: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.FC, _Mapping]] = ..., flocker: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Flocker, _Mapping]] = ..., gce_persistent_disk: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.GcePersistentDisk, _Mapping]] = ..., glusterfs: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.GlusterFs, _Mapping]] = ..., iscsi: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.ISCSI, _Mapping]] = ..., local: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Local, _Mapping]] = ..., persistent_volume_claim: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.PVC, _Mapping]] = ..., nfs: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.NFS, _Mapping]] = ..., csi: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.CSI, _Mapping]] = ..., downward_api: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.DownwardAPI, _Mapping]] = ..., ephemeral: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.EphemeralVolumeSource, _Mapping]] = ..., photon_persistent_disk: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.PhotonPersistentDisk, _Mapping]] = ..., portworx_volume: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Portworx, _Mapping]] = ..., projected: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Projected, _Mapping]] = ..., quobyte: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Quobyte, _Mapping]] = ..., rbd: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.RBD, _Mapping]] = ..., scale_io: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.ScaleIO, _Mapping]] = ..., secret: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.ConfigMap, _Mapping]] = ..., storageos: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.StorageOS, _Mapping]] = ..., vsphere_volume: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.VsphereVirtualDisk, _Mapping]] = ..., flex_volume: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.Flex, _Mapping]] = ..., secret_volume: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.SecretVolumeSource, _Mapping]] = ..., host_path: _Optional[_Union[PodInfo.PodSpec.VolumeInfo.HostPath, _Mapping]] = ...) -> None: ...
        class SecurityContext(_message.Message):
            __slots__ = ("run_as_user",)
            RUN_AS_USER_FIELD_NUMBER: _ClassVar[int]
            run_as_user: int
            def __init__(self, run_as_user: _Optional[int] = ...) -> None: ...
        class Toleration(_message.Message):
            __slots__ = ("key", "operator", "value", "effect", "tolerationSeconds")
            KEY_FIELD_NUMBER: _ClassVar[int]
            OPERATOR_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            EFFECT_FIELD_NUMBER: _ClassVar[int]
            TOLERATIONSECONDS_FIELD_NUMBER: _ClassVar[int]
            key: str
            operator: str
            value: str
            effect: str
            tolerationSeconds: int
            def __init__(self, key: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[str] = ..., tolerationSeconds: _Optional[int] = ...) -> None: ...
        VOLUMES_FIELD_NUMBER: _ClassVar[int]
        NODE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINERS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        RESTART_POLICY_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
        AFFINITY_FIELD_NUMBER: _ClassVar[int]
        volumes: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.VolumeInfo]
        node_name: str
        containers: _containers.RepeatedCompositeFieldContainer[Container]
        security_context: PodInfo.PodSpec.SecurityContext
        restart_policy: str
        service_account_name: str
        tolerations: _containers.RepeatedCompositeFieldContainer[PodInfo.PodSpec.Toleration]
        affinity: Affinity
        def __init__(self, volumes: _Optional[_Iterable[_Union[PodInfo.PodSpec.VolumeInfo, _Mapping]]] = ..., node_name: _Optional[str] = ..., containers: _Optional[_Iterable[_Union[Container, _Mapping]]] = ..., security_context: _Optional[_Union[PodInfo.PodSpec.SecurityContext, _Mapping]] = ..., restart_policy: _Optional[str] = ..., service_account_name: _Optional[str] = ..., tolerations: _Optional[_Iterable[_Union[PodInfo.PodSpec.Toleration, _Mapping]]] = ..., affinity: _Optional[_Union[Affinity, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    name: str
    spec: PodInfo.PodSpec
    status: ObjectStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., name: _Optional[str] = ..., spec: _Optional[_Union[PodInfo.PodSpec, _Mapping]] = ..., status: _Optional[_Union[ObjectStatus, _Mapping]] = ...) -> None: ...

class Pods(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    items: _containers.RepeatedCompositeFieldContainer[PodInfo]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[PodInfo, _Mapping]]] = ...) -> None: ...

class PVCInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    class PVCSpec(_message.Message):
        __slots__ = ("volume_name", "resources", "storage_class_name", "selector", "access_modes", "volume_mode", "data_source")
        class Resources(_message.Message):
            __slots__ = ("requests",)
            class RequestsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            REQUESTS_FIELD_NUMBER: _ClassVar[int]
            requests: _containers.ScalarMap[str, str]
            def __init__(self, requests: _Optional[_Mapping[str, str]] = ...) -> None: ...
        VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        STORAGE_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        ACCESS_MODES_FIELD_NUMBER: _ClassVar[int]
        VOLUME_MODE_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
        volume_name: str
        resources: PVCInfo.PVCSpec.Resources
        storage_class_name: str
        selector: LabelSelector
        access_modes: _containers.RepeatedScalarFieldContainer[str]
        volume_mode: str
        data_source: ObjectReference
        def __init__(self, volume_name: _Optional[str] = ..., resources: _Optional[_Union[PVCInfo.PVCSpec.Resources, _Mapping]] = ..., storage_class_name: _Optional[str] = ..., selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., access_modes: _Optional[_Iterable[str]] = ..., volume_mode: _Optional[str] = ..., data_source: _Optional[_Union[ObjectReference, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: PVCInfo.PVCSpec
    status: PeristentVolumeStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[PVCInfo.PVCSpec, _Mapping]] = ..., status: _Optional[_Union[PeristentVolumeStatus, _Mapping]] = ...) -> None: ...

class PVCs(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    items: _containers.RepeatedCompositeFieldContainer[PVCInfo]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[PVCInfo, _Mapping]]] = ...) -> None: ...

class PVs(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    items: _containers.RepeatedCompositeFieldContainer[PersistentVolume]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[PersistentVolume, _Mapping]]] = ...) -> None: ...

class PersistentVolumeSpec(_message.Message):
    __slots__ = ("csi", "storage_class_name", "claim_ref")
    class CSIInfo(_message.Message):
        __slots__ = ("driver",)
        DRIVER_FIELD_NUMBER: _ClassVar[int]
        driver: str
        def __init__(self, driver: _Optional[str] = ...) -> None: ...
    class ClaimRef(_message.Message):
        __slots__ = ("name", "namespace")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        name: str
        namespace: str
        def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...
    CSI_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    CLAIM_REF_FIELD_NUMBER: _ClassVar[int]
    csi: PersistentVolumeSpec.CSIInfo
    storage_class_name: str
    claim_ref: PersistentVolumeSpec.ClaimRef
    def __init__(self, csi: _Optional[_Union[PersistentVolumeSpec.CSIInfo, _Mapping]] = ..., storage_class_name: _Optional[str] = ..., claim_ref: _Optional[_Union[PersistentVolumeSpec.ClaimRef, _Mapping]] = ...) -> None: ...

class PeristentVolumeStatus(_message.Message):
    __slots__ = ("phase", "capacity")
    class CapacityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PHASE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    phase: str
    capacity: _containers.ScalarMap[str, str]
    def __init__(self, phase: _Optional[str] = ..., capacity: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PersistentVolume(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: PersistentVolumeSpec
    status: PeristentVolumeStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[PersistentVolumeSpec, _Mapping]] = ..., status: _Optional[_Union[PeristentVolumeStatus, _Mapping]] = ...) -> None: ...

class StorageClass(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "provisioner")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    provisioner: str
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., provisioner: _Optional[str] = ...) -> None: ...

class StorageClasses(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    items: _containers.RepeatedCompositeFieldContainer[StorageClass]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[StorageClass, _Mapping]]] = ...) -> None: ...

class VolumeSnapshotClass(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "driver", "deletion_policy", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    DELETION_POLICY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    driver: str
    deletion_policy: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., driver: _Optional[str] = ..., deletion_policy: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VolumeSnapshotClasses(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    items: _containers.RepeatedCompositeFieldContainer[VolumeSnapshotClass]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[VolumeSnapshotClass, _Mapping]]] = ...) -> None: ...

class VolumeSnapshotInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    class VolumeSnapshotSpec(_message.Message):
        __slots__ = ("source", "volume_snapshot_class_name")
        class Source(_message.Message):
            __slots__ = ("persistent_volume_claim_name", "volume_snapshot_content_name")
            PERSISTENT_VOLUME_CLAIM_NAME_FIELD_NUMBER: _ClassVar[int]
            VOLUME_SNAPSHOT_CONTENT_NAME_FIELD_NUMBER: _ClassVar[int]
            persistent_volume_claim_name: str
            volume_snapshot_content_name: str
            def __init__(self, persistent_volume_claim_name: _Optional[str] = ..., volume_snapshot_content_name: _Optional[str] = ...) -> None: ...
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        VOLUME_SNAPSHOT_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
        source: VolumeSnapshotInfo.VolumeSnapshotSpec.Source
        volume_snapshot_class_name: str
        def __init__(self, source: _Optional[_Union[VolumeSnapshotInfo.VolumeSnapshotSpec.Source, _Mapping]] = ..., volume_snapshot_class_name: _Optional[str] = ...) -> None: ...
    class VolumeSnapshotStatus(_message.Message):
        __slots__ = ("bound_volume_snapshot_content_name", "ready_to_use", "restore_size_string")
        BOUND_VOLUME_SNAPSHOT_CONTENT_NAME_FIELD_NUMBER: _ClassVar[int]
        READY_TO_USE_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SIZE_STRING_FIELD_NUMBER: _ClassVar[int]
        bound_volume_snapshot_content_name: str
        ready_to_use: bool
        restore_size_string: str
        def __init__(self, bound_volume_snapshot_content_name: _Optional[str] = ..., ready_to_use: bool = ..., restore_size_string: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: VolumeSnapshotInfo.VolumeSnapshotSpec
    status: VolumeSnapshotInfo.VolumeSnapshotStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[VolumeSnapshotInfo.VolumeSnapshotSpec, _Mapping]] = ..., status: _Optional[_Union[VolumeSnapshotInfo.VolumeSnapshotStatus, _Mapping]] = ...) -> None: ...

class VolumeSnapshotRef(_message.Message):
    __slots__ = ("name", "namespace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class VolumeSnapshotContentSpec(_message.Message):
    __slots__ = ("deletion_policy", "driver", "source", "volume_snapshot_class_name", "volume_snapshot_ref")
    class Source(_message.Message):
        __slots__ = ("snapshot_handle",)
        SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
        snapshot_handle: str
        def __init__(self, snapshot_handle: _Optional[str] = ...) -> None: ...
    DELETION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_REF_FIELD_NUMBER: _ClassVar[int]
    deletion_policy: str
    driver: str
    source: VolumeSnapshotContentSpec.Source
    volume_snapshot_class_name: str
    volume_snapshot_ref: VolumeSnapshotRef
    def __init__(self, deletion_policy: _Optional[str] = ..., driver: _Optional[str] = ..., source: _Optional[_Union[VolumeSnapshotContentSpec.Source, _Mapping]] = ..., volume_snapshot_class_name: _Optional[str] = ..., volume_snapshot_ref: _Optional[_Union[VolumeSnapshotRef, _Mapping]] = ...) -> None: ...

class VolumeSnapshotContent(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    class VolumeSnapshotContentStatus(_message.Message):
        __slots__ = ("ready_to_use", "snapshot_handle")
        READY_TO_USE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
        ready_to_use: bool
        snapshot_handle: str
        def __init__(self, ready_to_use: bool = ..., snapshot_handle: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: VolumeSnapshotContentSpec
    status: VolumeSnapshotContent.VolumeSnapshotContentStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[VolumeSnapshotContentSpec, _Mapping]] = ..., status: _Optional[_Union[VolumeSnapshotContent.VolumeSnapshotContentStatus, _Mapping]] = ...) -> None: ...

class ServiceAccountInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ...) -> None: ...

class RoleRefInfo(_message.Message):
    __slots__ = ("api_group", "kind", "name")
    API_GROUP_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_group: str
    kind: str
    name: str
    def __init__(self, api_group: _Optional[str] = ..., kind: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SubjectItemInfo(_message.Message):
    __slots__ = ("kind", "name", "namespace")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    namespace: str
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class ClusterRoleBindingInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "role_ref", "subjects")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ROLE_REF_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    role_ref: RoleRefInfo
    subjects: _containers.RepeatedCompositeFieldContainer[SubjectItemInfo]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., role_ref: _Optional[_Union[RoleRefInfo, _Mapping]] = ..., subjects: _Optional[_Iterable[_Union[SubjectItemInfo, _Mapping]]] = ...) -> None: ...

class SecretInfo(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "type", "data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    type: str
    data: _containers.ScalarMap[str, str]
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., type: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LimitRangeItem(_message.Message):
    __slots__ = ("type", "maximum_limit", "minimum_request", "default_limit", "default_request")
    class MaximumLimitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MinimumRequestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DefaultLimitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DefaultRequestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    type: str
    maximum_limit: _containers.ScalarMap[str, str]
    minimum_request: _containers.ScalarMap[str, str]
    default_limit: _containers.ScalarMap[str, str]
    default_request: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[str] = ..., maximum_limit: _Optional[_Mapping[str, str]] = ..., minimum_request: _Optional[_Mapping[str, str]] = ..., default_limit: _Optional[_Mapping[str, str]] = ..., default_request: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LimitRangeSpec(_message.Message):
    __slots__ = ("limits",)
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    limits: _containers.RepeatedCompositeFieldContainer[LimitRangeItem]
    def __init__(self, limits: _Optional[_Iterable[_Union[LimitRangeItem, _Mapping]]] = ...) -> None: ...

class LimitRange(_message.Message):
    __slots__ = ("metadata", "spec")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMeta
    spec: LimitRangeSpec
    def __init__(self, metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[LimitRangeSpec, _Mapping]] = ...) -> None: ...

class EventInfo(_message.Message):
    __slots__ = ("reason", "message")
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    message: str
    def __init__(self, reason: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class EventList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EventInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[EventInfo, _Mapping]]] = ...) -> None: ...

class Time(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class IntOrString(_message.Message):
    __slots__ = ("type", "intVal", "strVal")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTVAL_FIELD_NUMBER: _ClassVar[int]
    STRVAL_FIELD_NUMBER: _ClassVar[int]
    type: int
    intVal: int
    strVal: str
    def __init__(self, type: _Optional[int] = ..., intVal: _Optional[int] = ..., strVal: _Optional[str] = ...) -> None: ...

class RollingUpdateDeployment(_message.Message):
    __slots__ = ("maxUnavailable", "maxSurge")
    MAXUNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MAXSURGE_FIELD_NUMBER: _ClassVar[int]
    maxUnavailable: IntOrString
    maxSurge: IntOrString
    def __init__(self, maxUnavailable: _Optional[_Union[IntOrString, _Mapping]] = ..., maxSurge: _Optional[_Union[IntOrString, _Mapping]] = ...) -> None: ...

class DeploymentStrategy(_message.Message):
    __slots__ = ("type", "rollingUpdate")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLLINGUPDATE_FIELD_NUMBER: _ClassVar[int]
    type: str
    rollingUpdate: RollingUpdateDeployment
    def __init__(self, type: _Optional[str] = ..., rollingUpdate: _Optional[_Union[RollingUpdateDeployment, _Mapping]] = ...) -> None: ...

class PodTemplateSpec(_message.Message):
    __slots__ = ("metadata", "spec")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMeta
    spec: PodInfo.PodSpec
    def __init__(self, metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[PodInfo.PodSpec, _Mapping]] = ...) -> None: ...

class DeploymentSpec(_message.Message):
    __slots__ = ("replicas", "selector", "template", "strategy", "minReadySeconds", "revisionHistoryLimit", "paused", "progressDeadlineSeconds")
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MINREADYSECONDS_FIELD_NUMBER: _ClassVar[int]
    REVISIONHISTORYLIMIT_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    PROGRESSDEADLINESECONDS_FIELD_NUMBER: _ClassVar[int]
    replicas: int
    selector: LabelSelector
    template: PodTemplateSpec
    strategy: DeploymentStrategy
    minReadySeconds: int
    revisionHistoryLimit: int
    paused: bool
    progressDeadlineSeconds: int
    def __init__(self, replicas: _Optional[int] = ..., selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., template: _Optional[_Union[PodTemplateSpec, _Mapping]] = ..., strategy: _Optional[_Union[DeploymentStrategy, _Mapping]] = ..., minReadySeconds: _Optional[int] = ..., revisionHistoryLimit: _Optional[int] = ..., paused: bool = ..., progressDeadlineSeconds: _Optional[int] = ...) -> None: ...

class DeploymentCondition(_message.Message):
    __slots__ = ("type", "status", "reason", "message")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: str
    status: str
    reason: str
    message: str
    def __init__(self, type: _Optional[str] = ..., status: _Optional[str] = ..., reason: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class DeploymentStatus(_message.Message):
    __slots__ = ("observedGeneration", "replicas", "updatedReplicas", "availableReplicas", "unavailableReplicas", "conditions", "readyReplicas", "collisionCount")
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDREPLICAS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEREPLICAS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLEREPLICAS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    READYREPLICAS_FIELD_NUMBER: _ClassVar[int]
    COLLISIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    observedGeneration: int
    replicas: int
    updatedReplicas: int
    availableReplicas: int
    unavailableReplicas: int
    conditions: _containers.RepeatedCompositeFieldContainer[DeploymentCondition]
    readyReplicas: int
    collisionCount: int
    def __init__(self, observedGeneration: _Optional[int] = ..., replicas: _Optional[int] = ..., updatedReplicas: _Optional[int] = ..., availableReplicas: _Optional[int] = ..., unavailableReplicas: _Optional[int] = ..., conditions: _Optional[_Iterable[_Union[DeploymentCondition, _Mapping]]] = ..., readyReplicas: _Optional[int] = ..., collisionCount: _Optional[int] = ...) -> None: ...

class Deployment(_message.Message):
    __slots__ = ("kind", "api_version", "metadata", "spec", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    metadata: ObjectMeta
    spec: DeploymentSpec
    status: DeploymentStatus
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[DeploymentSpec, _Mapping]] = ..., status: _Optional[_Union[DeploymentStatus, _Mapping]] = ...) -> None: ...

class ContainerStatus(_message.Message):
    __slots__ = ("name", "containerID")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINERID_FIELD_NUMBER: _ClassVar[int]
    name: str
    containerID: str
    def __init__(self, name: _Optional[str] = ..., containerID: _Optional[str] = ...) -> None: ...

class Probe(_message.Message):
    __slots__ = ("tcp_socket", "initial_delay_seconds", "period_seconds", "failure_threshold", "success_threshold", "timeout_seconds")
    class TcpSocketAction(_message.Message):
        __slots__ = ("port",)
        PORT_FIELD_NUMBER: _ClassVar[int]
        port: int
        def __init__(self, port: _Optional[int] = ...) -> None: ...
    TCP_SOCKET_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    tcp_socket: Probe.TcpSocketAction
    initial_delay_seconds: int
    period_seconds: int
    failure_threshold: int
    success_threshold: int
    timeout_seconds: int
    def __init__(self, tcp_socket: _Optional[_Union[Probe.TcpSocketAction, _Mapping]] = ..., initial_delay_seconds: _Optional[int] = ..., period_seconds: _Optional[int] = ..., failure_threshold: _Optional[int] = ..., success_threshold: _Optional[int] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class ClusterNetworkEntry(_message.Message):
    __slots__ = ("cidr",)
    CIDR_FIELD_NUMBER: _ClassVar[int]
    cidr: str
    def __init__(self, cidr: _Optional[str] = ...) -> None: ...

class NetworkStatus(_message.Message):
    __slots__ = ("cluster_network",)
    CLUSTER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    cluster_network: _containers.RepeatedCompositeFieldContainer[ClusterNetworkEntry]
    def __init__(self, cluster_network: _Optional[_Iterable[_Union[ClusterNetworkEntry, _Mapping]]] = ...) -> None: ...

class Network(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: NetworkStatus
    def __init__(self, status: _Optional[_Union[NetworkStatus, _Mapping]] = ...) -> None: ...
