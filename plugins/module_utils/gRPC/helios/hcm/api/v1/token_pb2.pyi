from helios.hcm.api.v1 import asset_pb2 as _asset_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClaimTokenData(_message.Message):
    __slots__ = ("asset_type", "sf_account_id", "helios_url", "helios_data_url", "sfdc_cid", "sso_url")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HELIOS_URL_FIELD_NUMBER: _ClassVar[int]
    HELIOS_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    SFDC_CID_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    sf_account_id: str
    helios_url: str
    helios_data_url: str
    sfdc_cid: str
    sso_url: str
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., sf_account_id: _Optional[str] = ..., helios_url: _Optional[str] = ..., helios_data_url: _Optional[str] = ..., sfdc_cid: _Optional[str] = ..., sso_url: _Optional[str] = ...) -> None: ...
