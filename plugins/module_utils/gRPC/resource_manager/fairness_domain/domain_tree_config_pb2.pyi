from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FairnessDomainNodeConfigProto(_message.Message):
    __slots__ = ("domain_name", "shares_pct_of_parent", "child_domain_config_vec")
    class SharesPercentage(_message.Message):
        __slots__ = ("min_pct", "max_pct")
        MIN_PCT_FIELD_NUMBER: _ClassVar[int]
        MAX_PCT_FIELD_NUMBER: _ClassVar[int]
        min_pct: float
        max_pct: float
        def __init__(self, min_pct: _Optional[float] = ..., max_pct: _Optional[float] = ...) -> None: ...
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARES_PCT_OF_PARENT_FIELD_NUMBER: _ClassVar[int]
    CHILD_DOMAIN_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    shares_pct_of_parent: FairnessDomainNodeConfigProto.SharesPercentage
    child_domain_config_vec: _containers.RepeatedCompositeFieldContainer[FairnessDomainNodeConfigProto]
    def __init__(self, domain_name: _Optional[str] = ..., shares_pct_of_parent: _Optional[_Union[FairnessDomainNodeConfigProto.SharesPercentage, _Mapping]] = ..., child_domain_config_vec: _Optional[_Iterable[_Union[FairnessDomainNodeConfigProto, _Mapping]]] = ...) -> None: ...

class FairnessDomainSharesConfigProto(_message.Message):
    __slots__ = ("version", "resource_id_vec", "domain_tree_root")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    version: int
    resource_id_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_tree_root: FairnessDomainNodeConfigProto
    def __init__(self, version: _Optional[int] = ..., resource_id_vec: _Optional[_Iterable[str]] = ..., domain_tree_root: _Optional[_Union[FairnessDomainNodeConfigProto, _Mapping]] = ...) -> None: ...
