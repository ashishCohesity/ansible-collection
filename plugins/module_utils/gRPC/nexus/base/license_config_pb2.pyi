from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Identity(_message.Message):
    __slots__ = ("cluster_id", "incarnation_id", "node_hardware_vec")
    class NodeHardware(_message.Message):
        __slots__ = ("serial_no", "model", "chassis_serial", "mac_address_vec")
        SERIAL_NO_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        CHASSIS_SERIAL_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
        serial_no: str
        model: _cluster_config_pb2.ClusterConfigProto.ProductModel
        chassis_serial: str
        mac_address_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, serial_no: _Optional[str] = ..., model: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]] = ..., chassis_serial: _Optional[str] = ..., mac_address_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_HARDWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    incarnation_id: int
    node_hardware_vec: _containers.RepeatedCompositeFieldContainer[Identity.NodeHardware]
    def __init__(self, cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., node_hardware_vec: _Optional[_Iterable[_Union[Identity.NodeHardware, _Mapping]]] = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("name", "attributes", "activation_time_secs", "stats_time_secs", "expiry_time_secs", "overuse_time_secs", "is_unlimited", "license_type", "product_description", "product_info")
    class FeatureName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        unknownFeature: _ClassVar[Feature.FeatureName]
        dataPlatform: _ClassVar[Feature.FeatureName]
        dataProtect: _ClassVar[Feature.FeatureName]
        cloudTier: _ClassVar[Feature.FeatureName]
        cloudArchive: _ClassVar[Feature.FeatureName]
        cloudSpin: _ClassVar[Feature.FeatureName]
        dataPlatform_ve: _ClassVar[Feature.FeatureName]
        dataPlatform_ce: _ClassVar[Feature.FeatureName]
        helios: _ClassVar[Feature.FeatureName]
        dataPlatform_UCSC240M4: _ClassVar[Feature.FeatureName]
        dataPlatform_UCSC240M5: _ClassVar[Feature.FeatureName]
        dataProtectReplica: _ClassVar[Feature.FeatureName]
        archive: _ClassVar[Feature.FeatureName]
        smartFiles: _ClassVar[Feature.FeatureName]
        dataProtectService: _ClassVar[Feature.FeatureName]
        dataProtectExpress: _ClassVar[Feature.FeatureName]
        cloudArchiveDirectV2: _ClassVar[Feature.FeatureName]
        baasFetb: _ClassVar[Feature.FeatureName]
        baasBetb: _ClassVar[Feature.FeatureName]
        baasM365UserCount: _ClassVar[Feature.FeatureName]
        gaiaIndxStorage: _ClassVar[Feature.FeatureName]
        llmNumGenAns: _ClassVar[Feature.FeatureName]
        externalViews: _ClassVar[Feature.FeatureName]
        externalViewSnapshots: _ClassVar[Feature.FeatureName]
    unknownFeature: Feature.FeatureName
    dataPlatform: Feature.FeatureName
    dataProtect: Feature.FeatureName
    cloudTier: Feature.FeatureName
    cloudArchive: Feature.FeatureName
    cloudSpin: Feature.FeatureName
    dataPlatform_ve: Feature.FeatureName
    dataPlatform_ce: Feature.FeatureName
    helios: Feature.FeatureName
    dataPlatform_UCSC240M4: Feature.FeatureName
    dataPlatform_UCSC240M5: Feature.FeatureName
    dataProtectReplica: Feature.FeatureName
    archive: Feature.FeatureName
    smartFiles: Feature.FeatureName
    dataProtectService: Feature.FeatureName
    dataProtectExpress: Feature.FeatureName
    cloudArchiveDirectV2: Feature.FeatureName
    baasFetb: Feature.FeatureName
    baasBetb: Feature.FeatureName
    baasM365UserCount: Feature.FeatureName
    gaiaIndxStorage: Feature.FeatureName
    llmNumGenAns: Feature.FeatureName
    externalViews: Feature.FeatureName
    externalViewSnapshots: Feature.FeatureName
    class Attributes(_message.Message):
        __slots__ = ("capacity_bytes", "num_nodes", "num_vms")
        CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_NODES_FIELD_NUMBER: _ClassVar[int]
        NUM_VMS_FIELD_NUMBER: _ClassVar[int]
        capacity_bytes: int
        num_nodes: int
        num_vms: int
        def __init__(self, capacity_bytes: _Optional[int] = ..., num_nodes: _Optional[int] = ..., num_vms: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    STATS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    OVERUSE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    name: Feature.FeatureName
    attributes: Feature.Attributes
    activation_time_secs: int
    stats_time_secs: int
    expiry_time_secs: int
    overuse_time_secs: int
    is_unlimited: bool
    license_type: str
    product_description: str
    product_info: str
    def __init__(self, name: _Optional[_Union[Feature.FeatureName, str]] = ..., attributes: _Optional[_Union[Feature.Attributes, _Mapping]] = ..., activation_time_secs: _Optional[int] = ..., stats_time_secs: _Optional[int] = ..., expiry_time_secs: _Optional[int] = ..., overuse_time_secs: _Optional[int] = ..., is_unlimited: bool = ..., license_type: _Optional[str] = ..., product_description: _Optional[str] = ..., product_info: _Optional[str] = ...) -> None: ...

class HistoryValue(_message.Message):
    __slots__ = ("featureName", "value", "timestamp")
    FEATURENAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    featureName: str
    value: float
    timestamp: int
    def __init__(self, featureName: _Optional[str] = ..., value: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AuditReportProto(_message.Message):
    __slots__ = ("id", "timestamp_secs", "identity", "version", "feature_usage_vec", "is_trial", "daily_usage_history", "daily_entitlement_history", "cluster_node_ids", "raw_metrics_to_usage_map")
    class RawMetricsToUsageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_TRIAL_FIELD_NUMBER: _ClassVar[int]
    DAILY_USAGE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    DAILY_ENTITLEMENT_HISTORY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    RAW_METRICS_TO_USAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    id: int
    timestamp_secs: int
    identity: Identity
    version: int
    feature_usage_vec: _containers.RepeatedCompositeFieldContainer[Feature]
    is_trial: bool
    daily_usage_history: _containers.RepeatedCompositeFieldContainer[HistoryValue]
    daily_entitlement_history: _containers.RepeatedCompositeFieldContainer[HistoryValue]
    cluster_node_ids: _containers.RepeatedScalarFieldContainer[int]
    raw_metrics_to_usage_map: _containers.ScalarMap[str, int]
    def __init__(self, id: _Optional[int] = ..., timestamp_secs: _Optional[int] = ..., identity: _Optional[_Union[Identity, _Mapping]] = ..., version: _Optional[int] = ..., feature_usage_vec: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., is_trial: bool = ..., daily_usage_history: _Optional[_Iterable[_Union[HistoryValue, _Mapping]]] = ..., daily_entitlement_history: _Optional[_Iterable[_Union[HistoryValue, _Mapping]]] = ..., cluster_node_ids: _Optional[_Iterable[int]] = ..., raw_metrics_to_usage_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class LicenseProto(_message.Message):
    __slots__ = ("id", "timestamp_secs", "identity", "expiry_time_secs", "min_activation_time_secs", "min_activation_time_days", "max_activation_time_secs", "account_licensed_feature_usage_vec", "account_feature_usage_vec", "is_trial_allowed", "account_overusage_vec", "free_setup_mode", "last_metric_timestamp_secs")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    MIN_ACTIVATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    MIN_ACTIVATION_TIME_DAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_ACTIVATION_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LICENSED_FEATURE_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FEATURE_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_TRIAL_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OVERUSAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    FREE_SETUP_MODE_FIELD_NUMBER: _ClassVar[int]
    LAST_METRIC_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    id: int
    timestamp_secs: int
    identity: Identity
    expiry_time_secs: int
    min_activation_time_secs: int
    min_activation_time_days: int
    max_activation_time_secs: int
    account_licensed_feature_usage_vec: _containers.RepeatedCompositeFieldContainer[Feature]
    account_feature_usage_vec: _containers.RepeatedCompositeFieldContainer[Feature]
    is_trial_allowed: bool
    account_overusage_vec: _containers.RepeatedCompositeFieldContainer[Feature]
    free_setup_mode: bool
    last_metric_timestamp_secs: int
    def __init__(self, id: _Optional[int] = ..., timestamp_secs: _Optional[int] = ..., identity: _Optional[_Union[Identity, _Mapping]] = ..., expiry_time_secs: _Optional[int] = ..., min_activation_time_secs: _Optional[int] = ..., min_activation_time_days: _Optional[int] = ..., max_activation_time_secs: _Optional[int] = ..., account_licensed_feature_usage_vec: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., account_feature_usage_vec: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., is_trial_allowed: bool = ..., account_overusage_vec: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., free_setup_mode: bool = ..., last_metric_timestamp_secs: _Optional[int] = ...) -> None: ...

class SignedLicenseProto(_message.Message):
    __slots__ = ("signature", "license")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    license: LicenseProto
    def __init__(self, signature: _Optional[bytes] = ..., license: _Optional[_Union[LicenseProto, _Mapping]] = ...) -> None: ...

class LicenseManagerProto(_message.Message):
    __slots__ = ("gandalf_key", "signed_license", "audit_report", "classified_account")
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LICENSE_FIELD_NUMBER: _ClassVar[int]
    AUDIT_REPORT_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    signed_license: SignedLicenseProto
    audit_report: AuditReportProto
    classified_account: ClassifiedAccountProto
    def __init__(self, gandalf_key: _Optional[str] = ..., signed_license: _Optional[_Union[SignedLicenseProto, _Mapping]] = ..., audit_report: _Optional[_Union[AuditReportProto, _Mapping]] = ..., classified_account: _Optional[_Union[ClassifiedAccountProto, _Mapping]] = ...) -> None: ...

class ClassifiedAccountProto(_message.Message):
    __slots__ = ("activation_timestamp", "is_cluster_activated")
    ACTIVATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_CLUSTER_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    activation_timestamp: int
    is_cluster_activated: bool
    def __init__(self, activation_timestamp: _Optional[int] = ..., is_cluster_activated: bool = ...) -> None: ...

class SkuDefinitionsProto(_message.Message):
    __slots__ = ("sku_definition_vec",)
    class SkuDefinition(_message.Message):
        __slots__ = ("name", "display_name", "model_vec", "feature_vec", "is_perpetual", "is_poc")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        MODEL_VEC_FIELD_NUMBER: _ClassVar[int]
        FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_PERPETUAL_FIELD_NUMBER: _ClassVar[int]
        IS_POC_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        model_vec: _containers.RepeatedScalarFieldContainer[_cluster_config_pb2.ClusterConfigProto.ProductModel]
        feature_vec: _containers.RepeatedCompositeFieldContainer[Feature]
        is_perpetual: bool
        is_poc: bool
        def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., model_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]]] = ..., feature_vec: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., is_perpetual: bool = ..., is_poc: bool = ...) -> None: ...
    SKU_DEFINITION_VEC_FIELD_NUMBER: _ClassVar[int]
    sku_definition_vec: _containers.RepeatedCompositeFieldContainer[SkuDefinitionsProto.SkuDefinition]
    def __init__(self, sku_definition_vec: _Optional[_Iterable[_Union[SkuDefinitionsProto.SkuDefinition, _Mapping]]] = ...) -> None: ...

class LicenseKey(_message.Message):
    __slots__ = ("public_key",)
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    def __init__(self, public_key: _Optional[str] = ...) -> None: ...
