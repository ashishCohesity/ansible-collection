from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VipEpoch(_message.Message):
    __slots__ = ("vip", "epoch")
    VIP_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    vip: str
    epoch: int
    def __init__(self, vip: _Optional[str] = ..., epoch: _Optional[int] = ...) -> None: ...

class LocalVipEpochProto(_message.Message):
    __slots__ = ("vip_epochs",)
    VIP_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    vip_epochs: _containers.RepeatedCompositeFieldContainer[VipEpoch]
    def __init__(self, vip_epochs: _Optional[_Iterable[_Union[VipEpoch, _Mapping]]] = ...) -> None: ...

class ReloadVipEpochArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReloadVipEpochResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
