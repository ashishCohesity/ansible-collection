# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/service_upgrade_scripts.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(nexus/base/service_upgrade_scripts.proto\x12\x13\x63ohesity.nexus.base\x1a\x1c\x63onfigs/cluster_config.proto\"\xf7\x04\n\x1aServiceUpgradeScriptsProto\x12I\n\x17upgrade_scripts_dirpath\x18\x01 \x01(\t:(/home/cohesity/software/crux/bin/upgrade\x12Z\n\x13upgrade_scripts_vec\x18\x02 \x03(\x0b\x32=.cohesity.nexus.base.ServiceUpgradeScriptsProto.UpgradeScript\x1a\x86\x02\n\rUpgradeScript\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12S\n\rupgrade_stage\x18\x02 \x02(\x0e\x32<.cohesity.nexus.base.ServiceUpgradeScriptsProto.UpgradeStage\x12\x1a\n\x12version_constraint\x18\x04 \x01(\t\x12\x1a\n\x0ctimeout_secs\x18\x05 \x01(\x03:\x04\x33\x36\x30\x30\x12O\n\x0cservice_type\x18\x06 \x02(\x0e\x32\x39.cohesity.configs.ClusterConfigProto.Bulletin.ServiceNameJ\x04\x08\x03\x10\x04\"\xa8\x01\n\x0cUpgradeStage\x12,\n(kAfterNodeUpgradeBeforeServiceStartStage\x10\x01\x12+\n\'kAfterNodeUpgradeAfterServiceStartStage\x10\x02\x12\x1e\n\x1akBeforeClusterUpgradeStage\x10\x03\x12\x1d\n\x19kAfterClusterUpgradeStage\x10\x04\x42\'Z%nexus/base/service_upgrade_scripts.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.service_upgrade_scripts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%nexus/base/service_upgrade_scripts.pb'
  _globals['_SERVICEUPGRADESCRIPTSPROTO']._serialized_start=96
  _globals['_SERVICEUPGRADESCRIPTSPROTO']._serialized_end=727
  _globals['_SERVICEUPGRADESCRIPTSPROTO_UPGRADESCRIPT']._serialized_start=294
  _globals['_SERVICEUPGRADESCRIPTSPROTO_UPGRADESCRIPT']._serialized_end=556
  _globals['_SERVICEUPGRADESCRIPTSPROTO_UPGRADESTAGE']._serialized_start=559
  _globals['_SERVICEUPGRADESCRIPTSPROTO_UPGRADESTAGE']._serialized_end=727
# @@protoc_insertion_point(module_scope)
