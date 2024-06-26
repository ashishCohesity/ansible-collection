# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/agent.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!magneto/base/entities/agent.proto\x12\x16\x63ohesity.magneto.agent\x1a\x1fmagneto/agents/base/agent.proto\x1a\x18magneto/base/enums.proto\x1a\x18magneto/base/error.proto\x1a\x1cutil/base/universal_id.proto\"\x90\n\n\nProperties\x12\x39\n\x06status\x18\x01 \x01(\x0b\x32).cohesity.magneto.agent.Properties.Status\x12\x1c\n\x14\x61gent_sw_version_str\x18\x02 \x01(\t\x12Q\n\rupgradability\x18\x03 \x01(\x0e\x32\x30.cohesity.magneto.agent.Properties.Upgradability:\x08kUnknown\x12O\n\x0eupgrade_status\x18\x04 \x01(\x0e\x32\x30.cohesity.magneto.agent.Properties.UpgradeStatus:\x05kIdle\x12\x33\n\rupgrade_error\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x34\n\tcbmr_info\x18\x06 \x01(\x0b\x32!.cohesity.magneto.agents.CBMRInfo\x12\x31\n\thost_type\x18\x07 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type\x12U\n\x0elinux_pkg_type\x18\x08 \x01(\x0e\x32=.cohesity.magneto.agents.AgentInfoProto.LinuxAgentPackageType\x12\x45\n\nagent_type\x18\t \x01(\x0e\x32\x31.cohesity.magneto.agents.AgentInfoProto.AgentType\x12\x1a\n\x12machine_identifier\x18\n \x01(\t\x12\x14\n\x0cmachine_uuid\x18\x0b \x01(\t\x12\x36\n\x0cvol_cbt_info\x18\x0c \x01(\x0b\x32 .cohesity.magneto.agents.CbtInfo\x12\x37\n\rfile_cbt_info\x18\r \x01(\x0b\x32 .cohesity.magneto.agents.CbtInfo\x12Y\n\x10solaris_pkg_type\x18\x0f \x01(\x0e\x32?.cohesity.magneto.agents.AgentInfoProto.SolarisAgentPackageType\x1a\xb9\x01\n\x06Status\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32..cohesity.magneto.agent.Properties.Status.Type:\x08kUnknown\x12\x12\n\ndetail_msg\x18\x02 \x01(\t\"S\n\x04Type\x12\x0c\n\x08kUnknown\x10\x01\x12\x10\n\x0ckUnreachable\x10\x02\x12\x0c\n\x08kHealthy\x10\x03\x12\r\n\tkDegraded\x10\x04\x12\x0e\n\nkUnHealthy\x10\x05\"V\n\rUpgradeStatus\x12\t\n\x05kIdle\x10\x00\x12\r\n\tkAccepted\x10\x01\x12\x0c\n\x08kStarted\x10\x02\x12\r\n\tkFinished\x10\x03\x12\x0e\n\nkScheduled\x10\x04\"\x9c\x01\n\rUpgradability\x12\x0f\n\x0bkUpgradable\x10\x00\x12\x0c\n\x08kCurrent\x10\x01\x12\x0c\n\x08kUnknown\x10\x02\x12 \n\x1ckNonUpgradableInvalidVersion\x10\x03\x12\x1e\n\x1akNonUpgradableAgentIsNewer\x10\x04\x12\x1c\n\x18kNonUpgradableAgentIsOld\x10\x05J\x04\x08\x0e\x10\x0fR\x12solaris_agent_info\"\xf6\x05\n\x06\x45ntity\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.cohesity.magneto.agent.Entity.Type\x12-\n\tagent_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x31\n\thost_type\x18\x04 \x01(\x0e\x32\x1e.cohesity.magneto.HostEnv.Type\x12\x36\n\nproperties\x18\x05 \x01(\x0b\x32\".cohesity.magneto.agent.Properties\x12\x1b\n\x13owner_entity_id_vec\x18\t \x03(\x03\x12\x15\n\rinstaller_uri\x18\x06 \x01(\t\x12&\n\x14linux_installer_args\x18\x07 \x01(\t:\x08-- -i -y\x12H\n\x16windows_installer_args\x18\x08 \x01(\t:(/verysilent /suppressmsgboxes /norestart\x12\x1a\n\x12\x61ix_installer_args\x18\x0b \x01(\t\x12\x33\n\rrefresh_error\x18\n \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1a\n\x12supported_features\x18\x10 \x03(\t\x12\x19\n\x11\x63onfig_scribe_key\x18\x11 \x01(\t\x12\x1d\n\x15\x63onfig_file_timestamp\x18\x12 \x01(\x03\x12M\n\x0f\x61gent_cert_info\x18\x13 \x01(\x0b\x32\x34.cohesity.magneto.agents.AgentCertificateInformation\x12\x1e\n\x16solaris_installer_args\x18\x14 \x01(\t\x12\x1b\n\x13hpux_installer_args\x18\x15 \x01(\t\x12\x19\n\nagent_port\x18\x16 \x01(\x05:\x05\x35\x30\x30\x35\x31\"\x1d\n\x04Type\x12\n\n\x06kGroup\x10\x00\x12\t\n\x05kHost\x10\x01\"\x82\x03\n\x0fHostAgentStatus\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x36\n\nproperties\x18\x03 \x01(\x0b\x32\".cohesity.magneto.agent.Properties\x12P\n\x13verification_status\x18\x04 \x01(\x0e\x32).cohesity.magneto.VerificationStatus.Type:\x08kPending\x12\x38\n\x12verification_error\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x33\n\rrefresh_error\x18\x06 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12!\n\x19source_side_dedup_enabled\x18\x07 \x01(\x08\x12\x31\n)oracle_multi_node_multi_channel_supported\x18\x08 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROPERTIES']._serialized_start=177
  _globals['_PROPERTIES']._serialized_end=1473
  _globals['_PROPERTIES_STATUS']._serialized_start=1015
  _globals['_PROPERTIES_STATUS']._serialized_end=1200
  _globals['_PROPERTIES_STATUS_TYPE']._serialized_start=1117
  _globals['_PROPERTIES_STATUS_TYPE']._serialized_end=1200
  _globals['_PROPERTIES_UPGRADESTATUS']._serialized_start=1202
  _globals['_PROPERTIES_UPGRADESTATUS']._serialized_end=1288
  _globals['_PROPERTIES_UPGRADABILITY']._serialized_start=1291
  _globals['_PROPERTIES_UPGRADABILITY']._serialized_end=1447
  _globals['_ENTITY']._serialized_start=1476
  _globals['_ENTITY']._serialized_end=2234
  _globals['_ENTITY_TYPE']._serialized_start=2205
  _globals['_ENTITY_TYPE']._serialized_end=2234
  _globals['_HOSTAGENTSTATUS']._serialized_start=2237
  _globals['_HOSTAGENTSTATUS']._serialized_end=2623
# @@protoc_insertion_point(module_scope)
