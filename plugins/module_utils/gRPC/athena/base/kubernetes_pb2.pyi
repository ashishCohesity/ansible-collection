from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectMDProto(_message.Message):
    __slots__ = ("name", "namespace_name", "creation_timestamp", "labels", "uid", "deletion_timestamp", "annotations")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DELETION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace_name: str
    creation_timestamp: str
    labels: _containers.ScalarMap[str, str]
    uid: str
    deletion_timestamp: str
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., namespace_name: _Optional[str] = ..., creation_timestamp: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., uid: _Optional[str] = ..., deletion_timestamp: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NamespaceStatusProto(_message.Message):
    __slots__ = ("phase",)
    PHASE_FIELD_NUMBER: _ClassVar[int]
    phase: str
    def __init__(self, phase: _Optional[str] = ...) -> None: ...

class NamespaceProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: NamespaceStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[NamespaceStatusProto, _Mapping]] = ...) -> None: ...

class NamespaceListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NamespaceProto]
    def __init__(self, items: _Optional[_Iterable[_Union[NamespaceProto, _Mapping]]] = ...) -> None: ...

class SecretProto(_message.Message):
    __slots__ = ("name", "default_mode")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_mode: str
    def __init__(self, name: _Optional[str] = ..., default_mode: _Optional[str] = ...) -> None: ...

class VolumeProto(_message.Message):
    __slots__ = ("name", "secret")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    name: str
    secret: SecretProto
    def __init__(self, name: _Optional[str] = ..., secret: _Optional[_Union[SecretProto, _Mapping]] = ...) -> None: ...

class VolumeListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[VolumeProto]
    def __init__(self, items: _Optional[_Iterable[_Union[VolumeProto, _Mapping]]] = ...) -> None: ...

class PodSpecProto(_message.Message):
    __slots__ = ("nodeName", "volumes")
    NODENAME_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    nodeName: str
    volumes: VolumeListProto
    def __init__(self, nodeName: _Optional[str] = ..., volumes: _Optional[_Union[VolumeListProto, _Mapping]] = ...) -> None: ...

class PodStatusProto(_message.Message):
    __slots__ = ("phase", "message", "reason", "hostIP", "podIP", "startTime", "containerStatuses")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    HOSTIP_FIELD_NUMBER: _ClassVar[int]
    PODIP_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    CONTAINERSTATUSES_FIELD_NUMBER: _ClassVar[int]
    phase: str
    message: str
    reason: str
    hostIP: str
    podIP: str
    startTime: str
    containerStatuses: _containers.RepeatedCompositeFieldContainer[ContainerStatusProto]
    def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., reason: _Optional[str] = ..., hostIP: _Optional[str] = ..., podIP: _Optional[str] = ..., startTime: _Optional[str] = ..., containerStatuses: _Optional[_Iterable[_Union[ContainerStatusProto, _Mapping]]] = ...) -> None: ...

class ContainerStatusProto(_message.Message):
    __slots__ = ("name", "image", "containerID", "containerState")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ContainerStatusProto.State]
        kRunning: _ClassVar[ContainerStatusProto.State]
        kWaiting: _ClassVar[ContainerStatusProto.State]
        kTerminated: _ClassVar[ContainerStatusProto.State]
    kUnknown: ContainerStatusProto.State
    kRunning: ContainerStatusProto.State
    kWaiting: ContainerStatusProto.State
    kTerminated: ContainerStatusProto.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINERID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERSTATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: str
    containerID: str
    containerState: ContainerStatusProto.State
    def __init__(self, name: _Optional[str] = ..., image: _Optional[str] = ..., containerID: _Optional[str] = ..., containerState: _Optional[_Union[ContainerStatusProto.State, str]] = ...) -> None: ...

class PodProto(_message.Message):
    __slots__ = ("metadata", "spec", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    spec: PodSpecProto
    status: PodStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., spec: _Optional[_Union[PodSpecProto, _Mapping]] = ..., status: _Optional[_Union[PodStatusProto, _Mapping]] = ...) -> None: ...

class PodListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PodProto]
    def __init__(self, items: _Optional[_Iterable[_Union[PodProto, _Mapping]]] = ...) -> None: ...

class ServiceSpec(_message.Message):
    __slots__ = ("ports", "selector", "clusterIP", "type", "clusterIPs")
    class SelectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    CLUSTERIP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTERIPS_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[ServicePortProto]
    selector: _containers.ScalarMap[str, str]
    clusterIP: str
    type: str
    clusterIPs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ports: _Optional[_Iterable[_Union[ServicePortProto, _Mapping]]] = ..., selector: _Optional[_Mapping[str, str]] = ..., clusterIP: _Optional[str] = ..., type: _Optional[str] = ..., clusterIPs: _Optional[_Iterable[str]] = ...) -> None: ...

class ServicePortProto(_message.Message):
    __slots__ = ("name", "protocol", "port", "targetport", "nodePort")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TARGETPORT_FIELD_NUMBER: _ClassVar[int]
    NODEPORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    protocol: str
    port: int
    targetport: str
    nodePort: int
    def __init__(self, name: _Optional[str] = ..., protocol: _Optional[str] = ..., port: _Optional[int] = ..., targetport: _Optional[str] = ..., nodePort: _Optional[int] = ...) -> None: ...

class ServiceProto(_message.Message):
    __slots__ = ("metadata", "spec")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    spec: ServiceSpec
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., spec: _Optional[_Union[ServiceSpec, _Mapping]] = ...) -> None: ...

class ServiceListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ServiceProto]
    def __init__(self, items: _Optional[_Iterable[_Union[ServiceProto, _Mapping]]] = ...) -> None: ...

class PersistentVolumeSpecProto(_message.Message):
    __slots__ = ("accessModes", "driver", "fsType", "volumeName", "capacity", "targetPortal", "portals", "iqn", "lun")
    class CapacityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: QuantityProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[QuantityProto, _Mapping]] = ...) -> None: ...
    ACCESSMODES_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    FSTYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    TARGETPORTAL_FIELD_NUMBER: _ClassVar[int]
    PORTALS_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    accessModes: _containers.RepeatedScalarFieldContainer[str]
    driver: str
    fsType: str
    volumeName: str
    capacity: _containers.MessageMap[str, QuantityProto]
    targetPortal: str
    portals: _containers.RepeatedScalarFieldContainer[str]
    iqn: str
    lun: int
    def __init__(self, accessModes: _Optional[_Iterable[str]] = ..., driver: _Optional[str] = ..., fsType: _Optional[str] = ..., volumeName: _Optional[str] = ..., capacity: _Optional[_Mapping[str, QuantityProto]] = ..., targetPortal: _Optional[str] = ..., portals: _Optional[_Iterable[str]] = ..., iqn: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...

class PersistentVolumeStatusProto(_message.Message):
    __slots__ = ("phase", "message", "reason")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    phase: str
    message: str
    reason: str
    def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class PersistentVolumeProto(_message.Message):
    __slots__ = ("metadata", "spec", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    spec: PersistentVolumeSpecProto
    status: PersistentVolumeStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., spec: _Optional[_Union[PersistentVolumeSpecProto, _Mapping]] = ..., status: _Optional[_Union[PersistentVolumeStatusProto, _Mapping]] = ...) -> None: ...

class PersistentVolumeListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PersistentVolumeProto]
    def __init__(self, items: _Optional[_Iterable[_Union[PersistentVolumeProto, _Mapping]]] = ...) -> None: ...

class PersistentVolumeClaimSpecProto(_message.Message):
    __slots__ = ("accessModes", "volumeName", "matchLabels")
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCESSMODES_FIELD_NUMBER: _ClassVar[int]
    VOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    MATCHLABELS_FIELD_NUMBER: _ClassVar[int]
    accessModes: _containers.RepeatedScalarFieldContainer[str]
    volumeName: str
    matchLabels: _containers.ScalarMap[str, str]
    def __init__(self, accessModes: _Optional[_Iterable[str]] = ..., volumeName: _Optional[str] = ..., matchLabels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PersistentVolumeClaimStatusProto(_message.Message):
    __slots__ = ("phase", "accessModes")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    ACCESSMODES_FIELD_NUMBER: _ClassVar[int]
    phase: str
    accessModes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, phase: _Optional[str] = ..., accessModes: _Optional[_Iterable[str]] = ...) -> None: ...

class PersistentVolumeClaimProto(_message.Message):
    __slots__ = ("metadata", "spec", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    spec: PersistentVolumeClaimSpecProto
    status: PersistentVolumeClaimStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., spec: _Optional[_Union[PersistentVolumeClaimSpecProto, _Mapping]] = ..., status: _Optional[_Union[PersistentVolumeClaimStatusProto, _Mapping]] = ...) -> None: ...

class PersistentVolumeClaimListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PersistentVolumeClaimProto]
    def __init__(self, items: _Optional[_Iterable[_Union[PersistentVolumeClaimProto, _Mapping]]] = ...) -> None: ...

class DaemonSetStatusProto(_message.Message):
    __slots__ = ("currentNumberScheduled", "numberMisscheduled", "desiredNumberScheduled", "numberReady", "observedGeneration", "updatedNumberScheduled", "numberAvailable", "numberUnavailable")
    CURRENTNUMBERSCHEDULED_FIELD_NUMBER: _ClassVar[int]
    NUMBERMISSCHEDULED_FIELD_NUMBER: _ClassVar[int]
    DESIREDNUMBERSCHEDULED_FIELD_NUMBER: _ClassVar[int]
    NUMBERREADY_FIELD_NUMBER: _ClassVar[int]
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    UPDATEDNUMBERSCHEDULED_FIELD_NUMBER: _ClassVar[int]
    NUMBERAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    NUMBERUNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    currentNumberScheduled: int
    numberMisscheduled: int
    desiredNumberScheduled: int
    numberReady: int
    observedGeneration: int
    updatedNumberScheduled: int
    numberAvailable: int
    numberUnavailable: int
    def __init__(self, currentNumberScheduled: _Optional[int] = ..., numberMisscheduled: _Optional[int] = ..., desiredNumberScheduled: _Optional[int] = ..., numberReady: _Optional[int] = ..., observedGeneration: _Optional[int] = ..., updatedNumberScheduled: _Optional[int] = ..., numberAvailable: _Optional[int] = ..., numberUnavailable: _Optional[int] = ...) -> None: ...

class DaemonSetProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: DaemonSetStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[DaemonSetStatusProto, _Mapping]] = ...) -> None: ...

class DaemonSetListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DaemonSetProto]
    def __init__(self, items: _Optional[_Iterable[_Union[DaemonSetProto, _Mapping]]] = ...) -> None: ...

class ReplicaSetStatusProto(_message.Message):
    __slots__ = ("replicas", "fullyLabeledReplicas", "readyReplicas", "availableReplicas", "observedGeneration")
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    FULLYLABELEDREPLICAS_FIELD_NUMBER: _ClassVar[int]
    READYREPLICAS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEREPLICAS_FIELD_NUMBER: _ClassVar[int]
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    replicas: int
    fullyLabeledReplicas: int
    readyReplicas: int
    availableReplicas: int
    observedGeneration: int
    def __init__(self, replicas: _Optional[int] = ..., fullyLabeledReplicas: _Optional[int] = ..., readyReplicas: _Optional[int] = ..., availableReplicas: _Optional[int] = ..., observedGeneration: _Optional[int] = ...) -> None: ...

class ReplicaSetProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: ReplicaSetStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[ReplicaSetStatusProto, _Mapping]] = ...) -> None: ...

class ReplicaSetListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReplicaSetProto]
    def __init__(self, items: _Optional[_Iterable[_Union[ReplicaSetProto, _Mapping]]] = ...) -> None: ...

class StatefulSetStatusProto(_message.Message):
    __slots__ = ("observedGeneration", "replicas", "readyReplicas", "currentReplicas", "updatedReplicas", "currentRevision", "updateRevision")
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    READYREPLICAS_FIELD_NUMBER: _ClassVar[int]
    CURRENTREPLICAS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDREPLICAS_FIELD_NUMBER: _ClassVar[int]
    CURRENTREVISION_FIELD_NUMBER: _ClassVar[int]
    UPDATEREVISION_FIELD_NUMBER: _ClassVar[int]
    observedGeneration: int
    replicas: int
    readyReplicas: int
    currentReplicas: int
    updatedReplicas: int
    currentRevision: str
    updateRevision: str
    def __init__(self, observedGeneration: _Optional[int] = ..., replicas: _Optional[int] = ..., readyReplicas: _Optional[int] = ..., currentReplicas: _Optional[int] = ..., updatedReplicas: _Optional[int] = ..., currentRevision: _Optional[str] = ..., updateRevision: _Optional[str] = ...) -> None: ...

class StatefulSetProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: StatefulSetStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[StatefulSetStatusProto, _Mapping]] = ...) -> None: ...

class StatefulSetListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[StatefulSetProto]
    def __init__(self, items: _Optional[_Iterable[_Union[StatefulSetProto, _Mapping]]] = ...) -> None: ...

class JobSpecProto(_message.Message):
    __slots__ = ("parallelism", "completions", "activeDeadlineSeconds", "backoffLimit", "manualSelector")
    PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVEDEADLINESECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFFLIMIT_FIELD_NUMBER: _ClassVar[int]
    MANUALSELECTOR_FIELD_NUMBER: _ClassVar[int]
    parallelism: int
    completions: int
    activeDeadlineSeconds: int
    backoffLimit: int
    manualSelector: bool
    def __init__(self, parallelism: _Optional[int] = ..., completions: _Optional[int] = ..., activeDeadlineSeconds: _Optional[int] = ..., backoffLimit: _Optional[int] = ..., manualSelector: bool = ...) -> None: ...

class JobStatusProto(_message.Message):
    __slots__ = ("startTime", "completionTime", "active", "succeeded", "failed")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETIONTIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    startTime: str
    completionTime: str
    active: int
    succeeded: int
    failed: int
    def __init__(self, startTime: _Optional[str] = ..., completionTime: _Optional[str] = ..., active: _Optional[int] = ..., succeeded: _Optional[int] = ..., failed: _Optional[int] = ...) -> None: ...

class JobProto(_message.Message):
    __slots__ = ("metadata", "spec", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    spec: JobSpecProto
    status: JobStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., spec: _Optional[_Union[JobSpecProto, _Mapping]] = ..., status: _Optional[_Union[JobStatusProto, _Mapping]] = ...) -> None: ...

class JobListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[JobProto]
    def __init__(self, items: _Optional[_Iterable[_Union[JobProto, _Mapping]]] = ...) -> None: ...

class NodeProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: NodeStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[NodeStatusProto, _Mapping]] = ...) -> None: ...

class QuantityProto(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...

class NodeConditionProto(_message.Message):
    __slots__ = ("type", "status")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    type: str
    status: str
    def __init__(self, type: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class NodeAddressProto(_message.Message):
    __slots__ = ("type", "address")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: str
    address: str
    def __init__(self, type: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class NodeStatusProto(_message.Message):
    __slots__ = ("capacity", "allocatable", "conditions", "unschedulable", "addresses")
    class CapacityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: QuantityProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[QuantityProto, _Mapping]] = ...) -> None: ...
    class AllocatableEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: QuantityProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[QuantityProto, _Mapping]] = ...) -> None: ...
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATABLE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    UNSCHEDULABLE_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    capacity: _containers.MessageMap[str, QuantityProto]
    allocatable: _containers.MessageMap[str, QuantityProto]
    conditions: _containers.RepeatedCompositeFieldContainer[NodeConditionProto]
    unschedulable: bool
    addresses: _containers.RepeatedCompositeFieldContainer[NodeAddressProto]
    def __init__(self, capacity: _Optional[_Mapping[str, QuantityProto]] = ..., allocatable: _Optional[_Mapping[str, QuantityProto]] = ..., conditions: _Optional[_Iterable[_Union[NodeConditionProto, _Mapping]]] = ..., unschedulable: bool = ..., addresses: _Optional[_Iterable[_Union[NodeAddressProto, _Mapping]]] = ...) -> None: ...

class NodeListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NodeProto]
    def __init__(self, items: _Optional[_Iterable[_Union[NodeProto, _Mapping]]] = ...) -> None: ...

class VmStatusProto(_message.Message):
    __slots__ = ("created", "ready")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    created: bool
    ready: bool
    def __init__(self, created: bool = ..., ready: bool = ...) -> None: ...

class VmProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: VmStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[VmStatusProto, _Mapping]] = ...) -> None: ...

class DeploymentStatusProto(_message.Message):
    __slots__ = ("observedGeneration", "replicas", "updatedReplicas", "readyReplicas", "availableReplicas")
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDREPLICAS_FIELD_NUMBER: _ClassVar[int]
    READYREPLICAS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEREPLICAS_FIELD_NUMBER: _ClassVar[int]
    observedGeneration: int
    replicas: int
    updatedReplicas: int
    readyReplicas: int
    availableReplicas: int
    def __init__(self, observedGeneration: _Optional[int] = ..., replicas: _Optional[int] = ..., updatedReplicas: _Optional[int] = ..., readyReplicas: _Optional[int] = ..., availableReplicas: _Optional[int] = ...) -> None: ...

class DeploymentProto(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ObjectMDProto
    status: DeploymentStatusProto
    def __init__(self, metadata: _Optional[_Union[ObjectMDProto, _Mapping]] = ..., status: _Optional[_Union[DeploymentStatusProto, _Mapping]] = ...) -> None: ...

class EventInfoProto(_message.Message):
    __slots__ = ("reason", "message", "last_timestamp", "type")
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    message: str
    last_timestamp: str
    type: str
    def __init__(self, reason: _Optional[str] = ..., message: _Optional[str] = ..., last_timestamp: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class EventListProto(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EventInfoProto]
    def __init__(self, items: _Optional[_Iterable[_Union[EventInfoProto, _Mapping]]] = ...) -> None: ...

class MetricFamily(_message.Message):
    __slots__ = ("name", "help", "type", "metrics")
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COUNTER: _ClassVar[MetricFamily.MetricType]
        GAUGE: _ClassVar[MetricFamily.MetricType]
        SUMMARY: _ClassVar[MetricFamily.MetricType]
        UNTYPED: _ClassVar[MetricFamily.MetricType]
        HISTOGRAM: _ClassVar[MetricFamily.MetricType]
    COUNTER: MetricFamily.MetricType
    GAUGE: MetricFamily.MetricType
    SUMMARY: MetricFamily.MetricType
    UNTYPED: MetricFamily.MetricType
    HISTOGRAM: MetricFamily.MetricType
    NAME_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    help: str
    type: MetricFamily.MetricType
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, name: _Optional[str] = ..., help: _Optional[str] = ..., type: _Optional[_Union[MetricFamily.MetricType, str]] = ..., metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

class MetricGauge(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class MetricExemplar(_message.Message):
    __slots__ = ("labels", "value")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    value: float
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ..., value: _Optional[float] = ...) -> None: ...

class MetricCounter(_message.Message):
    __slots__ = ("value", "exemplar")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXEMPLAR_FIELD_NUMBER: _ClassVar[int]
    value: float
    exemplar: MetricExemplar
    def __init__(self, value: _Optional[float] = ..., exemplar: _Optional[_Union[MetricExemplar, _Mapping]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("timestamp_ms", "labels", "gauge", "counter")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    GAUGE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    timestamp_ms: int
    labels: _containers.ScalarMap[str, str]
    gauge: MetricGauge
    counter: MetricCounter
    def __init__(self, timestamp_ms: _Optional[int] = ..., labels: _Optional[_Mapping[str, str]] = ..., gauge: _Optional[_Union[MetricGauge, _Mapping]] = ..., counter: _Optional[_Union[MetricCounter, _Mapping]] = ...) -> None: ...

class NodeMetricsCAdvisor(_message.Message):
    __slots__ = ("families",)
    class FamiliesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MetricFamily
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetricFamily, _Mapping]] = ...) -> None: ...
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    families: _containers.MessageMap[str, MetricFamily]
    def __init__(self, families: _Optional[_Mapping[str, MetricFamily]] = ...) -> None: ...
