# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/service_auth_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!configs/service_auth_config.proto\x12\x10\x63ohesity.configs\x1a\x1cutil/base/universal_id.proto\"\xd3\x03\n\x16ServiceAuthConfigProto\x12q\n\x1f\x63lient_component_2_acl_mask_map\x18\x01 \x03(\x0b\x32H.cohesity.configs.ServiceAuthConfigProto.ClientComponent2AclMaskMapEntry\x1a\x41\n\x1f\x43lientComponent2AclMaskMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x32\n\x08\x43lientID\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xa2\x01\n\x0f\x43lientComponent\x12\x0c\n\x08kUnknown\x10\x00\x12\n\n\x06kOther\x10\x01\x12\n\n\x06kTools\x10\x02\x12\x0b\n\x07kBridge\x10\x03\x12\x0b\n\x07kApollo\x10\x04\x12\x0c\n\x08kMagneto\x10\x05\x12\x0b\n\x07kMadrox\x10\x06\x12\x0b\n\x07kIcebox\x10\x07\x12\t\n\x05kYoda\x10\x08\x12\x0b\n\x07kAthena\x10\t\x12\x0f\n\x0bkAtomRemote\x10\n\"*\n\x11\x41\x43LPermissionType\x12\t\n\x05kRead\x10\x01\x12\n\n\x06kWrite\x10\x02\x42\x16\n\x14\x63om.cohesity.configs')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.service_auth_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.configs'
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT2ACLMASKMAPENTRY']._loaded_options = None
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT2ACLMASKMAPENTRY']._serialized_options = b'8\001'
  _globals['_SERVICEAUTHCONFIGPROTO']._serialized_start=86
  _globals['_SERVICEAUTHCONFIGPROTO']._serialized_end=553
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT2ACLMASKMAPENTRY']._serialized_start=227
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT2ACLMASKMAPENTRY']._serialized_end=292
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTID']._serialized_start=294
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTID']._serialized_end=344
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT']._serialized_start=347
  _globals['_SERVICEAUTHCONFIGPROTO_CLIENTCOMPONENT']._serialized_end=509
  _globals['_SERVICEAUTHCONFIGPROTO_ACLPERMISSIONTYPE']._serialized_start=511
  _globals['_SERVICEAUTHCONFIGPROTO_ACLPERMISSIONTYPE']._serialized_end=553
# @@protoc_insertion_point(module_scope)
