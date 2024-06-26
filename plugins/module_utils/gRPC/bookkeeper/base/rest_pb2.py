# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookkeeper/base/rest.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo.mr.base import utils_pb2 as apollo_dot_mr_dot_base_dot_utils__pb2
from bookkeeper.base import error_pb2 as bookkeeper_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x62ookkeeper/base/rest.proto\x12\x18\x63ohesity.bookkeeper.rest\x1a\x1a\x61pollo/mr/base/utils.proto\x1a\x1b\x62ookkeeper/base/error.proto\"\x9b\x03\n\x10GroupFilterProto\x12\x15\n\rtenant_id_vec\x18\x01 \x03(\t\x12\x1d\n\x15storage_domain_id_vec\x18\x02 \x03(\x03\x12J\n\x08\x63onsumer\x18\x03 \x01(\x0b\x32\x38.cohesity.bookkeeper.rest.GroupFilterProto.ConsumerProto\x12\x13\n\x0bnull_tenant\x18\x04 \x01(\x08\x1a\xef\x01\n\rConsumerProto\x12K\n\x04type\x18\x01 \x01(\x0e\x32=.cohesity.bookkeeper.rest.GroupFilterProto.ConsumerProto.Type\"\x90\x01\n\x04Type\x12\t\n\x05kNone\x10\x00\x12\n\n\x06kViews\x10\x01\x12\x0f\n\x0bkBackupRuns\x10\x02\x12\x14\n\x10kReplicationRuns\x10\x03\x12\x0c\n\x08kObjects\x10\x04\x12\x10\n\x0ckDataProtect\x10\x05\x12\x11\n\rkDataPlatform\x10\x06\x12\x17\n\x13kViewProtectionRuns\x10\x07\"\x96\x05\n\x15GroupInformationProto\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12X\n\nattributes\x18\x03 \x01(\x0b\x32\x44.cohesity.bookkeeper.rest.GroupInformationProto.GroupAttributesProto\x12\x1b\n\x13stats_entity_id_str\x18\x04 \x01(\t\x12J\n\nmetric_vec\x18\x05 \x03(\x0b\x32\x36.cohesity.bookkeeper.rest.GroupInformationProto.Metric\x12\x1d\n\x15stats_timestamp_usecs\x18\x06 \x01(\x03\x1a\xbf\x02\n\x14GroupAttributesProto\x12 \n\x14tenant_id_deprecated\x18\x01 \x01(\tB\x02\x18\x01\x12\x19\n\x11storage_domain_id\x18\x02 \x01(\x03\x12J\n\x08\x63onsumer\x18\x03 \x01(\x0b\x32\x38.cohesity.bookkeeper.rest.GroupFilterProto.ConsumerProto\x12\x64\n\x0btenant_info\x18\x04 \x01(\x0b\x32O.cohesity.bookkeeper.rest.GroupInformationProto.GroupAttributesProto.TenantInfo\x1a\x38\n\nTenantInfo\x12\x15\n\rtenant_id_str\x18\x01 \x01(\t\x12\x13\n\x0bnull_tenant\x18\x02 \x01(\x08\x1a?\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\x12\x18\n\x10time_stamp_usecs\x18\x03 \x01(\x03\"\x91\x01\n\x1fGetStorageDomainStorageStatsArg\x12@\n\x0cquery_filter\x18\x01 \x01(\x0b\x32*.cohesity.bookkeeper.rest.GroupFilterProto\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\"\xd4\x02\n\"GetStorageDomainStorageStatsResult\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.cohesity.bookkeeper.ErrorProto\x12o\n\x17storage_domain_info_vec\x18\x02 \x03(\x0b\x32N.cohesity.bookkeeper.rest.GetStorageDomainStorageStatsResult.StorageDomainInfo\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\x1ar\n\x11StorageDomainInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x43\n\ngroup_info\x18\x03 \x01(\x0b\x32/.cohesity.bookkeeper.rest.GroupInformationProto\"\x8a\x01\n\x18GetTenantStorageStatsArg\x12@\n\x0cquery_filter\x18\x01 \x01(\x0b\x32*.cohesity.bookkeeper.rest.GroupFilterProto\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\"\xc6\x02\n\x1bGetTenantStorageStatsResult\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.cohesity.bookkeeper.ErrorProto\x12Y\n\x0ftenant_info_vec\x18\x02 \x03(\x0b\x32@.cohesity.bookkeeper.rest.GetTenantStorageStatsResult.TenantInfo\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\x1a\x80\x01\n\nTenantInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x43\n\ngroup_info\x18\x03 \x01(\x0b\x32/.cohesity.bookkeeper.rest.GroupInformationProto\x12\x13\n\x0bnull_tenant\x18\x04 \x01(\x08\"\x8c\x01\n\x1aGetConsumerStorageStatsArg\x12@\n\x0cquery_filter\x18\x01 \x01(\x0b\x32*.cohesity.bookkeeper.rest.GroupFilterProto\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\"\xa0\x02\n\x1dGetConsumerStorageStatsResult\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.cohesity.bookkeeper.ErrorProto\x12_\n\x11\x63onsumer_info_vec\x18\x02 \x03(\x0b\x32\x44.cohesity.bookkeeper.rest.GetConsumerStorageStatsResult.ConsumerInfo\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\x1aS\n\x0c\x43onsumerInfo\x12\x43\n\ngroup_info\x18\x03 \x01(\x0b\x32/.cohesity.bookkeeper.rest.GroupInformationProto\"\x87\x01\n\x15GetJobStorageStatsArg\x12@\n\x0cquery_filter\x18\x01 \x01(\x0b\x32*.cohesity.bookkeeper.rest.GroupFilterProto\x12\x19\n\x11pagination_cookie\x18\x02 \x01(\t\x12\x11\n\tmax_count\x18\x03 \x01(\x05\"\xca\x02\n\x18GetJobStorageStatsResult\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.cohesity.bookkeeper.ErrorProto\x12R\n\x0cjob_info_vec\x18\x02 \x03(\x0b\x32<.cohesity.bookkeeper.rest.GetJobStorageStatsResult.GroupInfo\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\x1a\x8e\x01\n\tGroupInfo\x12.\n\x02id\x18\x01 \x01(\x0b\x32\".cohesity.apollo.mr.ObjectUidProto\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x43\n\ngroup_info\x18\x03 \x01(\x0b\x32/.cohesity.bookkeeper.rest.GroupInformationProto\"\x88\x01\n\x16GetViewStorageStatsArg\x12@\n\x0cquery_filter\x18\x01 \x01(\x0b\x32*.cohesity.bookkeeper.rest.GroupFilterProto\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\"\xa6\x02\n\x19GetViewStorageStatsResult\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.cohesity.bookkeeper.ErrorProto\x12S\n\rview_info_vec\x18\x02 \x03(\x0b\x32<.cohesity.bookkeeper.rest.GetViewStorageStatsResult.ViewInfo\x12\x19\n\x11pagination_cookie\x18\x03 \x01(\t\x1ai\n\x08ViewInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x43\n\ngroup_info\x18\x03 \x01(\x0b\x32/.cohesity.bookkeeper.rest.GroupInformationProtoB\x1aZ\x18\x63ohesity/bookkeeper/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bookkeeper.base.rest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/bookkeeper/base'
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO'].fields_by_name['tenant_id_deprecated']._loaded_options = None
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO'].fields_by_name['tenant_id_deprecated']._serialized_options = b'\030\001'
  _globals['_GROUPFILTERPROTO']._serialized_start=114
  _globals['_GROUPFILTERPROTO']._serialized_end=525
  _globals['_GROUPFILTERPROTO_CONSUMERPROTO']._serialized_start=286
  _globals['_GROUPFILTERPROTO_CONSUMERPROTO']._serialized_end=525
  _globals['_GROUPFILTERPROTO_CONSUMERPROTO_TYPE']._serialized_start=381
  _globals['_GROUPFILTERPROTO_CONSUMERPROTO_TYPE']._serialized_end=525
  _globals['_GROUPINFORMATIONPROTO']._serialized_start=528
  _globals['_GROUPINFORMATIONPROTO']._serialized_end=1190
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO']._serialized_start=806
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO']._serialized_end=1125
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO_TENANTINFO']._serialized_start=1069
  _globals['_GROUPINFORMATIONPROTO_GROUPATTRIBUTESPROTO_TENANTINFO']._serialized_end=1125
  _globals['_GROUPINFORMATIONPROTO_METRIC']._serialized_start=1127
  _globals['_GROUPINFORMATIONPROTO_METRIC']._serialized_end=1190
  _globals['_GETSTORAGEDOMAINSTORAGESTATSARG']._serialized_start=1193
  _globals['_GETSTORAGEDOMAINSTORAGESTATSARG']._serialized_end=1338
  _globals['_GETSTORAGEDOMAINSTORAGESTATSRESULT']._serialized_start=1341
  _globals['_GETSTORAGEDOMAINSTORAGESTATSRESULT']._serialized_end=1681
  _globals['_GETSTORAGEDOMAINSTORAGESTATSRESULT_STORAGEDOMAININFO']._serialized_start=1567
  _globals['_GETSTORAGEDOMAINSTORAGESTATSRESULT_STORAGEDOMAININFO']._serialized_end=1681
  _globals['_GETTENANTSTORAGESTATSARG']._serialized_start=1684
  _globals['_GETTENANTSTORAGESTATSARG']._serialized_end=1822
  _globals['_GETTENANTSTORAGESTATSRESULT']._serialized_start=1825
  _globals['_GETTENANTSTORAGESTATSRESULT']._serialized_end=2151
  _globals['_GETTENANTSTORAGESTATSRESULT_TENANTINFO']._serialized_start=2023
  _globals['_GETTENANTSTORAGESTATSRESULT_TENANTINFO']._serialized_end=2151
  _globals['_GETCONSUMERSTORAGESTATSARG']._serialized_start=2154
  _globals['_GETCONSUMERSTORAGESTATSARG']._serialized_end=2294
  _globals['_GETCONSUMERSTORAGESTATSRESULT']._serialized_start=2297
  _globals['_GETCONSUMERSTORAGESTATSRESULT']._serialized_end=2585
  _globals['_GETCONSUMERSTORAGESTATSRESULT_CONSUMERINFO']._serialized_start=2502
  _globals['_GETCONSUMERSTORAGESTATSRESULT_CONSUMERINFO']._serialized_end=2585
  _globals['_GETJOBSTORAGESTATSARG']._serialized_start=2588
  _globals['_GETJOBSTORAGESTATSARG']._serialized_end=2723
  _globals['_GETJOBSTORAGESTATSRESULT']._serialized_start=2726
  _globals['_GETJOBSTORAGESTATSRESULT']._serialized_end=3056
  _globals['_GETJOBSTORAGESTATSRESULT_GROUPINFO']._serialized_start=2914
  _globals['_GETJOBSTORAGESTATSRESULT_GROUPINFO']._serialized_end=3056
  _globals['_GETVIEWSTORAGESTATSARG']._serialized_start=3059
  _globals['_GETVIEWSTORAGESTATSARG']._serialized_end=3195
  _globals['_GETVIEWSTORAGESTATSRESULT']._serialized_start=3198
  _globals['_GETVIEWSTORAGESTATSRESULT']._serialized_end=3492
  _globals['_GETVIEWSTORAGESTATSRESULT_VIEWINFO']._serialized_start=3387
  _globals['_GETVIEWSTORAGESTATSRESULT_VIEWINFO']._serialized_end=3492
# @@protoc_insertion_point(module_scope)
