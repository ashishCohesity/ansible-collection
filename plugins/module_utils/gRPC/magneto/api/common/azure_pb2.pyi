from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AzureNativeBackupParams(_message.Message):
    __slots__ = ("data_transfer_info",)
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    data_transfer_info: DataTransferInfo
    def __init__(self, data_transfer_info: _Optional[_Union[DataTransferInfo, _Mapping]] = ...) -> None: ...

class DataTransferInfo(_message.Message):
    __slots__ = ("is_private_network", "private_network_info_vec")
    class PrivateNetworkInfo(_message.Message):
        __slots__ = ("vpn", "location", "subnet")
        VPN_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        vpn: AzureEntity
        location: str
        subnet: AzureEntity
        def __init__(self, vpn: _Optional[_Union[AzureEntity, _Mapping]] = ..., location: _Optional[str] = ..., subnet: _Optional[_Union[AzureEntity, _Mapping]] = ...) -> None: ...
    IS_PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    is_private_network: bool
    private_network_info_vec: _containers.RepeatedCompositeFieldContainer[DataTransferInfo.PrivateNetworkInfo]
    def __init__(self, is_private_network: bool = ..., private_network_info_vec: _Optional[_Iterable[_Union[DataTransferInfo.PrivateNetworkInfo, _Mapping]]] = ...) -> None: ...

class AzureEntity(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    display_name: str
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ...) -> None: ...
