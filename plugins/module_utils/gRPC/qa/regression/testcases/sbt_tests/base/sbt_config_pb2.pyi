from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client_credentials(_message.Message):
    __slots__ = ("username", "password", "rootusername", "rootpassword")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROOTUSERNAME_FIELD_NUMBER: _ClassVar[int]
    ROOTPASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    rootusername: str
    rootpassword: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., rootusername: _Optional[str] = ..., rootpassword: _Optional[str] = ...) -> None: ...

class Script_names(_message.Message):
    __slots__ = ("script_name", "script_path")
    SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    script_name: str
    script_path: str
    def __init__(self, script_name: _Optional[str] = ..., script_path: _Optional[str] = ...) -> None: ...

class Server_end_config(_message.Message):
    __slots__ = ("view_name", "viewbox_name", "mountpoint", "node_ip_vec", "vip_list")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    VIP_LIST_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    viewbox_name: str
    mountpoint: str
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    vip_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_name: _Optional[str] = ..., viewbox_name: _Optional[str] = ..., mountpoint: _Optional[str] = ..., node_ip_vec: _Optional[_Iterable[str]] = ..., vip_list: _Optional[_Iterable[str]] = ...) -> None: ...

class Load_generator_details(_message.Message):
    __slots__ = ("load_tablespace", "load_table_name", "load_table_size")
    LOAD_TABLESPACE_FIELD_NUMBER: _ClassVar[int]
    LOAD_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOAD_TABLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    load_tablespace: str
    load_table_name: str
    load_table_size: int
    def __init__(self, load_tablespace: _Optional[str] = ..., load_table_name: _Optional[str] = ..., load_table_size: _Optional[int] = ...) -> None: ...

class Data_integrity_test(_message.Message):
    __slots__ = ("test_tablespace1", "test_tablespace2", "table_name1", "table_name2", "table_size")
    TEST_TABLESPACE1_FIELD_NUMBER: _ClassVar[int]
    TEST_TABLESPACE2_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME1_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME2_FIELD_NUMBER: _ClassVar[int]
    TABLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    test_tablespace1: str
    test_tablespace2: str
    table_name1: str
    table_name2: str
    table_size: int
    def __init__(self, test_tablespace1: _Optional[str] = ..., test_tablespace2: _Optional[str] = ..., table_name1: _Optional[str] = ..., table_name2: _Optional[str] = ..., table_size: _Optional[int] = ...) -> None: ...

class Client_details(_message.Message):
    __slots__ = ("client_name", "client_ip", "scripts", "rman_path", "cluster_config", "load_generator", "integrity_config", "credential", "home_directory", "oracle_home")
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    RMAN_PATH_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOAD_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    HOME_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    client_ip: str
    scripts: _containers.RepeatedCompositeFieldContainer[Script_names]
    rman_path: str
    cluster_config: Server_end_config
    load_generator: Load_generator_details
    integrity_config: Data_integrity_test
    credential: Client_credentials
    home_directory: str
    oracle_home: str
    def __init__(self, client_name: _Optional[str] = ..., client_ip: _Optional[str] = ..., scripts: _Optional[_Iterable[_Union[Script_names, _Mapping]]] = ..., rman_path: _Optional[str] = ..., cluster_config: _Optional[_Union[Server_end_config, _Mapping]] = ..., load_generator: _Optional[_Union[Load_generator_details, _Mapping]] = ..., integrity_config: _Optional[_Union[Data_integrity_test, _Mapping]] = ..., credential: _Optional[_Union[Client_credentials, _Mapping]] = ..., home_directory: _Optional[str] = ..., oracle_home: _Optional[str] = ...) -> None: ...

class TestServers(_message.Message):
    __slots__ = ("client_machine_vec",)
    CLIENT_MACHINE_VEC_FIELD_NUMBER: _ClassVar[int]
    client_machine_vec: _containers.RepeatedCompositeFieldContainer[Client_details]
    def __init__(self, client_machine_vec: _Optional[_Iterable[_Union[Client_details, _Mapping]]] = ...) -> None: ...
