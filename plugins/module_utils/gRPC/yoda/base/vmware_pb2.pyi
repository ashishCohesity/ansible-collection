from magneto.connectors.vmware import vmware_base_pb2 as _vmware_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMwareAddSnapshotArg(_message.Message):
    __slots__ = ("additional_file_info_vec", "is_quiesced")
    class AdditionalFileInfo(_message.Message):
        __slots__ = ("file_type", "file_name", "error_msg")
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
        file_type: _vmware_base_pb2.FileType
        file_name: str
        error_msg: str
        def __init__(self, file_type: _Optional[_Union[_vmware_base_pb2.FileType, str]] = ..., file_name: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...
    ADDITIONAL_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_QUIESCED_FIELD_NUMBER: _ClassVar[int]
    additional_file_info_vec: _containers.RepeatedCompositeFieldContainer[VMwareAddSnapshotArg.AdditionalFileInfo]
    is_quiesced: bool
    def __init__(self, additional_file_info_vec: _Optional[_Iterable[_Union[VMwareAddSnapshotArg.AdditionalFileInfo, _Mapping]]] = ..., is_quiesced: bool = ...) -> None: ...
