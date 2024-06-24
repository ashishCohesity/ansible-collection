from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudFunctionRestoreBodyProto(_message.Message):
    __slots__ = ("internal_ip", "os_type", "username", "password", "private_key", "file_copy_information", "owner_name")
    class OsType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kLinux: _ClassVar[CloudFunctionRestoreBodyProto.OsType.Type]
            kWindows: _ClassVar[CloudFunctionRestoreBodyProto.OsType.Type]
        kLinux: CloudFunctionRestoreBodyProto.OsType.Type
        kWindows: CloudFunctionRestoreBodyProto.OsType.Type
        def __init__(self) -> None: ...
    class FileCopyInformation(_message.Message):
        __slots__ = ("src_file_path", "dest_file_path")
        SRC_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        DEST_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        src_file_path: str
        dest_file_path: str
        def __init__(self, src_file_path: _Optional[str] = ..., dest_file_path: _Optional[str] = ...) -> None: ...
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_COPY_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    internal_ip: str
    os_type: CloudFunctionRestoreBodyProto.OsType.Type
    username: str
    password: str
    private_key: str
    file_copy_information: _containers.RepeatedCompositeFieldContainer[CloudFunctionRestoreBodyProto.FileCopyInformation]
    owner_name: str
    def __init__(self, internal_ip: _Optional[str] = ..., os_type: _Optional[_Union[CloudFunctionRestoreBodyProto.OsType.Type, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., private_key: _Optional[str] = ..., file_copy_information: _Optional[_Iterable[_Union[CloudFunctionRestoreBodyProto.FileCopyInformation, _Mapping]]] = ..., owner_name: _Optional[str] = ...) -> None: ...
