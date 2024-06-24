from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestConfig(_message.Message):
    __slots__ = ("storage_account_name", "access_key", "container_name", "function_app_name", "function_app_deployment_key", "subscription_id", "resource_group", "application_id", "application_key", "tenant_id", "bearer_token", "client_id", "sas_token")
    STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_APP_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_APP_DEPLOYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SAS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    storage_account_name: str
    access_key: str
    container_name: str
    function_app_name: str
    function_app_deployment_key: str
    subscription_id: str
    resource_group: str
    application_id: str
    application_key: str
    tenant_id: str
    bearer_token: str
    client_id: str
    sas_token: str
    def __init__(self, storage_account_name: _Optional[str] = ..., access_key: _Optional[str] = ..., container_name: _Optional[str] = ..., function_app_name: _Optional[str] = ..., function_app_deployment_key: _Optional[str] = ..., subscription_id: _Optional[str] = ..., resource_group: _Optional[str] = ..., application_id: _Optional[str] = ..., application_key: _Optional[str] = ..., tenant_id: _Optional[str] = ..., bearer_token: _Optional[str] = ..., client_id: _Optional[str] = ..., sas_token: _Optional[str] = ...) -> None: ...
