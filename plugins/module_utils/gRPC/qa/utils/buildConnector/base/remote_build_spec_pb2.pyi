from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ServerConnectionParams(_message.Message):
    __slots__ = ("endpoint", "server_cred")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SERVER_CRED_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    server_cred: ServerCredentials
    def __init__(self, endpoint: _Optional[str] = ..., server_cred: _Optional[_Union[ServerCredentials, _Mapping]] = ...) -> None: ...

class BuildServer(_message.Message):
    __slots__ = ("server", "workspace_path")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_PATH_FIELD_NUMBER: _ClassVar[int]
    server: ServerConnectionParams
    workspace_path: str
    def __init__(self, server: _Optional[_Union[ServerConnectionParams, _Mapping]] = ..., workspace_path: _Optional[str] = ...) -> None: ...

class RemoteBuildServers(_message.Message):
    __slots__ = ("remote_build_server_vec",)
    REMOTE_BUILD_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    remote_build_server_vec: _containers.RepeatedCompositeFieldContainer[BuildServer]
    def __init__(self, remote_build_server_vec: _Optional[_Iterable[_Union[BuildServer, _Mapping]]] = ...) -> None: ...

class NVParamType(_message.Message):
    __slots__ = ("name", "value", "prefix_abs_path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_ABS_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    prefix_abs_path: bool
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., prefix_abs_path: bool = ...) -> None: ...

class SingleParamType(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BuildParam(_message.Message):
    __slots__ = ("s_param", "nv_param")
    S_PARAM_FIELD_NUMBER: _ClassVar[int]
    NV_PARAM_FIELD_NUMBER: _ClassVar[int]
    s_param: SingleParamType
    nv_param: NVParamType
    def __init__(self, s_param: _Optional[_Union[SingleParamType, _Mapping]] = ..., nv_param: _Optional[_Union[NVParamType, _Mapping]] = ...) -> None: ...

class BuildParams(_message.Message):
    __slots__ = ("bld_param", "script_path", "timeout", "output_dir")
    BLD_PARAM_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIR_FIELD_NUMBER: _ClassVar[int]
    bld_param: _containers.RepeatedCompositeFieldContainer[BuildParam]
    script_path: str
    timeout: int
    output_dir: str
    def __init__(self, bld_param: _Optional[_Iterable[_Union[BuildParam, _Mapping]]] = ..., script_path: _Optional[str] = ..., timeout: _Optional[int] = ..., output_dir: _Optional[str] = ...) -> None: ...
